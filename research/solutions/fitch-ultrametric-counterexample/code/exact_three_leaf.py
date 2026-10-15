"""Exact rational verification of a twenty-state ultrametric Fitch example.

The proof can be checked by the four-row calculation without executing code.
The independent enumeration below uses every assignment to the four non-root
vertices and applies the literal Fitch recursion. Only Python's standard
library is required.
"""
from fractions import Fraction as F
from itertools import product


R = 20
LEAF_SIGNAL = F(1, 20)
STEM_SIGNAL = F(1, 16)
CHERRY_SIGNAL = F(4, 5)


def transition(signal, source, target):
    return signal * int(source == target) + (1 - signal) / R


def cherry_events():
    """Return the four disjoint cherry events and root conditional payoffs."""
    q = transition(LEAF_SIGNAL, 0, 0)
    p = transition(LEAF_SIGNAL, 0, 1)
    z = transition(STEM_SIGNAL, 0, 0)
    u = transition(CHERRY_SIGNAL, 0, 0)
    w = transition(CHERRY_SIGNAL, 0, 1)
    single = u * u + (R - 1) * w * w
    contains_single = z * u * u + (1 - z) * w * w
    contains_double = z * 2 * u * (1 - u) + (1 - z) * 2 * w * (1 - w)
    probabilities = [contains_single, single - contains_single,
                     contains_double, 1 - single - contains_double]
    payoffs = [q + (R - 1) * p / 2, q / 2,
               q + (R - 2) * p / 3, q / 3]
    return probabilities, payoffs


def four_event_accuracy():
    probabilities, payoffs = cherry_events()
    assert sum(probabilities) == 1
    assert all(0 <= x <= 1 for x in probabilities + payoffs)
    return sum(prob * payoff for prob, payoff in zip(probabilities, payoffs))


def exhaustive_accuracy():
    """Independent literal Fitch calculation; root is fixed to state zero."""
    total_mass = F(0)
    accuracy = F(0)
    root_to_a = [transition(LEAF_SIGNAL, 0, a) for a in range(R)]
    root_to_v = [transition(STEM_SIGNAL, 0, v) for v in range(R)]
    v_to_leaf = [[transition(CHERRY_SIGNAL, v, b) for b in range(R)] for v in range(R)]
    for a, b, c, v in product(range(R), repeat=4):
        prob = root_to_a[a] * root_to_v[v] * v_to_leaf[v][b] * v_to_leaf[v][c]
        left = {a}
        right = {b} & {c} or {b} | {c}
        root_set = left & right or left | right
        total_mass += prob
        accuracy += prob * F(int(0 in root_set), len(root_set))
    assert total_mass == 1
    return accuracy


if __name__ == '__main__':
    import json, sys
    from pathlib import Path
    import hashlib
    import datetime
    ra = four_event_accuracy()
    independent = exhaustive_accuracy()
    q = transition(LEAF_SIGNAL, 0, 0)
    assert STEM_SIGNAL * CHERRY_SIGNAL == LEAF_SIGNAL
    assert ra == independent == F(38829, 400000)
    assert q == F(39, 400)
    assert q - ra == F(171, 400000) > 0
    result = {'alphabet_size':R, 'leaf_signal':str(LEAF_SIGNAL),
              'stem_signal':str(STEM_SIGNAL), 'cherry_signal':str(CHERRY_SIGNAL),
              'event_probabilities':[str(x) for x in cherry_events()[0]],
              'conditional_payoffs':[str(x) for x in cherry_events()[1]],
              'fitch_accuracy':str(ra),'single_leaf_accuracy':str(q),
              'strict_deficit':str(q-ra),'exhaustive_accuracy':str(independent),
              'enumerated_assignments':R**4,'total_probability':'1',
              'arithmetic':'fractions.Fraction; exact rational',
              'python':sys.version.split()[0],
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    print(json.dumps(result,indent=2))
