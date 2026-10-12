#!/usr/bin/env python3
"""Exact four-vertex checks; these finite checks are not an asymptotic proof."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
import json


def layers(n, edges):
    remaining = set(range(n))
    result = []
    while remaining:
        current = tuple(sorted(v for v in remaining
                               if not any((u, v) in edges for u in remaining)))
        if not current:
            return None
        result.append(current)
        remaining.difference_update(current)
    return tuple(result)


def enumerate_dags(n):
    pairs = tuple(combinations(range(n), 2))
    for choices in product((0, 1, 2), repeat=len(pairs)):
        edges = frozenset((a, b) if c == 1 else (b, a)
                          for (a, b), c in zip(pairs, choices) if c)
        if layers(n, edges) is not None:
            yield edges


def compositions(n):
    if n == 0:
        yield ()
        return
    for cuts in product((False, True), repeat=n - 1):
        sizes = [1]
        for cut in cuts:
            if cut:
                sizes.append(1)
            else:
                sizes[-1] += 1
        yield tuple(sizes)


def weight(sizes):
    result = Fraction(1)
    for h in sizes:
        result *= Fraction(1, factorial(h) * 2 ** (h * (h - 1) // 2))
    for a, b in zip(sizes, sizes[1:]):
        result *= Fraction(2 ** a - 1, 2 ** a) ** b
    return result


def signature(n, edges):
    skeleton = frozenset(frozenset(e) for e in edges)
    colliders = frozenset((a, v, b) for v in range(n)
                         for a, b in combinations(range(n), 2)
                         if (a, v) in edges and (b, v) in edges
                         and frozenset((a, b)) not in skeleton)
    return skeleton, colliders


def verify():
    n = 4
    dags = tuple(enumerate_dags(n))
    count = len(dags)
    normalizers = {j: sum((weight(h) for h in compositions(j)), Fraction())
                   for j in range(n + 1)}
    assert normalizers[n] == Fraction(count, factorial(n) * 2 ** 6)
    assert count == 543

    observed = defaultdict(Fraction)
    vector_mass = defaultdict(Fraction)
    classes = defaultdict(list)
    order_pairs = 0
    for edges in dags:
        hs = layers(n, edges)
        sizes = tuple(map(len, hs))
        vector_mass[sizes] += Fraction(1, count)
        classes[signature(n, edges)].append(edges)
        denominator = count
        for h in sizes:
            denominator *= factorial(h)
        for ordered_layers in product(*(tuple(permutations(h)) for h in hs)):
            order_pairs += 1
            order = sum(ordered_layers, ())
            rank = {v: i for i, v in enumerate(order)}
            ranked = frozenset((rank[a], rank[b]) for a, b in edges)
            q = 0
            for h in sizes:
                q += h
                prefix = frozenset((a, b) for a, b in ranked if b < q)
                observed[q, prefix] += Fraction(1, denominator)

    for h, mass in vector_mass.items():
        assert mass == weight(h) / normalizers[n]

    for (q, prefix), mass in observed.items():
        g = tuple(map(len, layers(q, prefix)))
        interface_sum = sum((weight(h) * (
            Fraction(2 ** g[-1] - 1, 2 ** g[-1]) ** h[0] if h else 1)
                             for h in compositions(n - q)), Fraction())
        expected = Fraction(1, 2 ** (q * (q - 1) // 2)) * interface_sum
        expected /= normalizers[n]
        for size in g:
            expected /= factorial(size)
        assert mass == expected, (q, prefix, mass, expected)

    component_checks = 0
    for (skeleton, _), members in classes.items():
        reversible = [tuple(pair) for pair in skeleton
                      if len({tuple(sorted(pair))[0] == a
                              for edges in members for a, b in edges
                              if frozenset((a, b)) == pair}) > 1]
        adjacency = defaultdict(set)
        for a, b in reversible:
            adjacency[a].add(b)
            adjacency[b].add(a)
        components = []
        unused = set(adjacency)
        while unused:
            todo = [unused.pop()]
            component = set(todo)
            while todo:
                for v in adjacency[todo.pop()]:
                    if v not in component:
                        component.add(v)
                        unused.discard(v)
                        todo.append(v)
            components.append(component)
        bound = 1
        for component in components:
            bound *= factorial(len(component))
            for edges in members:
                outside_parents = [frozenset(u for u in range(n)
                                             if u not in component and (u, v) in edges)
                                   for v in component]
                assert len(set(outside_parents)) == 1
                for v in component:
                    parents = [u for u in component if (u, v) in edges]
                    assert all(frozenset((a, b)) in skeleton
                               for a, b in combinations(parents, 2))
                component_checks += 1
        assert len(members) <= bound
    return dict(vertices=n, labeled_dags=count, equivalence_classes=len(classes),
                graph_order_pairs=order_pairs,
                exact_prefix_identities=len(observed),
                layer_vector_identities=len(vector_mass),
                component_member_checks=component_checks,
                maximum_class_size=max(map(len, classes.values())),
                arithmetic="exact integers and fractions",
                result="PASS", scope="Finite structural and counting checks only")


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
