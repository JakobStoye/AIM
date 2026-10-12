"""Small exact reference using simple paths and exhaustive separation tests.

Vertices are zero-based. Pair states: absent=0, smaller->larger=1,
larger->smaller=2, bidirected=3. This implementation deliberately does not
use graphical shortcuts for maximality or legitimate mark changes.
"""
from itertools import combinations


class Graph:
    def __init__(self, n, states):
        self.n = n
        self.pairs = list(combinations(range(n), 2))
        self.states = tuple(states)
        assert len(self.states) == len(self.pairs)
        self.index = {pair: k for k, pair in enumerate(self.pairs)}

    @classmethod
    def from_key(cls, n, key):
        return cls(n, [(key >> (2*k)) & 3 for k in range(n*(n-1)//2)])

    @classmethod
    def from_edges(cls, n, directed=(), bidirected=()):
        pairs = list(combinations(range(n), 2)); states = [0]*len(pairs)
        for a, b in directed:
            states[pairs.index(tuple(sorted((a, b))))] = 1 if a < b else 2
        for a, b in bidirected:
            states[pairs.index(tuple(sorted((a, b))))] = 3
        return cls(n, states)

    def key(self):
        return sum(s << (2*k) for k, s in enumerate(self.states))

    def state(self, a, b):
        return self.states[self.index[tuple(sorted((a, b)))]]

    def head(self, a, b):
        s = self.state(a, b)
        return s == 3 or s == (2 if a < b else 1)

    def parents(self, b):
        return {a for a in range(self.n) if a != b and self.state(a, b)
                and self.head(b, a) and not self.head(a, b)}

    def ancestors(self):
        anc = [1 << v for v in range(self.n)]
        for b in range(self.n):
            for a in self.parents(b):
                anc[b] |= 1 << a
        for k in range(self.n):
            for b in range(self.n):
                if anc[b] & (1 << k):
                    anc[b] |= anc[k]
        return anc

    def ancestral(self):
        anc = self.ancestors()
        for k, (a, b) in enumerate(self.pairs):
            s = self.states[k]
            if s == 1 and anc[a] & (1 << b):
                return False
            if s == 2 and anc[b] & (1 << a):
                return False
            if s == 3 and (anc[a] & (1 << b) or anc[b] & (1 << a)):
                return False
        return True

    def mconnected(self, a, b, conditioning):
        anc = self.ancestors()
        activated = 0
        for v in range(self.n):
            if conditioning & (1 << v):
                activated |= anc[v]

        def visit(prev, cur, used):
            if cur == b:
                return True
            for nxt in range(self.n):
                if used & (1 << nxt) or not self.state(cur, nxt):
                    continue
                if prev is not None:
                    collider = self.head(cur, prev) and self.head(cur, nxt)
                    if collider and not activated & (1 << cur):
                        continue
                    if not collider and conditioning & (1 << cur):
                        continue
                if visit(cur, nxt, used | (1 << nxt)):
                    return True
            return False
        return visit(None, a, 1 << a)

    def query_masks(self, a, b):
        remaining = ((1 << self.n)-1) & ~((1 << a) | (1 << b))
        mask = remaining
        while True:
            yield mask
            if not mask:
                break
            mask = (mask-1) & remaining

    def signature(self):
        return tuple(not self.mconnected(a, b, s)
                     for a, b in self.pairs for s in self.query_masks(a, b))

    def maximal(self):
        return all(any(not self.mconnected(a, b, s) for s in self.query_masks(a, b))
                   for k, (a, b) in enumerate(self.pairs) if not self.states[k])

    def closure(self):
        anc = self.ancestors(); states = list(self.states)
        for k, (a, b) in enumerate(self.pairs):
            if not states[k] and all(self.mconnected(a, b, s) for s in self.query_masks(a, b)):
                states[k] = 1 if anc[b] & (1 << a) else 2 if anc[a] & (1 << b) else 3
        return Graph(self.n, states)

    def legitimate_neighbors(self):
        signature = self.signature()
        for k, s in enumerate(self.states):
            for t in ([3] if s in (1, 2) else [1, 2] if s == 3 else []):
                states = list(self.states); states[k] = t
                changed = Graph(self.n, states)
                if changed.ancestral() and changed.maximal() and changed.signature() == signature:
                    yield changed


def adjacency(n, anc, dependences):
    states = []
    for k, (a, b) in enumerate(combinations(range(n), 2)):
        mask = (anc[a] | anc[b]) & ~((1 << a) | (1 << b))
        states.append(0 if not dependences[k][mask] else
                      1 if anc[b] & (1 << a) else
                      2 if anc[a] & (1 << b) else 3)
    return Graph(n, states)


def poset_map(n, anc, dependences):
    first = adjacency(n, anc, dependences)
    return adjacency(n, first.ancestors(), dependences).closure()


def determinant(matrix):
    """Gaussian elimination over rational numbers, including the empty minor."""
    from fractions import Fraction
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    values = [[Fraction(x) for x in row] for row in matrix]
    result = Fraction(1)
    for k in range(n):
        pivot = next((j for j in range(k, n) if values[j][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            values[k], values[pivot] = values[pivot], values[k]
            result = -result
        entry = values[k][k]
        result *= entry
        for j in range(k+1, n):
            multiplier = values[j][k]/entry
            for c in range(k+1, n):
                values[j][c] -= multiplier*values[k][c]
    return result


def gaussian_dependences(covariance):
    """Exact almost-principal minors; zero is Gaussian conditional independence."""
    n = len(covariance)
    assert all(len(row) == n for row in covariance)
    result = []
    for a, b in combinations(range(n), 2):
        row = [False]*(1 << n)
        for mask in range(1 << n):
            if mask & ((1 << a) | (1 << b)):
                continue
            cond = [v for v in range(n) if mask & (1 << v)]
            minor = [[covariance[i][j] for j in [b]+cond] for i in [a]+cond]
            row[mask] = determinant(minor) != 0
        result.append(row)
    return result
