"""Exact integer polynomial algebra for the published rational-series data."""


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def powers(minus, plus):
    p = [1]
    for _ in range(minus):
        p = multiply(p, [1, -1])
    for _ in range(plus):
        p = multiply(p, [1, 1])
    return p


def denominator(degrees):
    p = [1]
    for degree in degrees:
        if degree <= 0:
            raise ValueError("Denominator degrees must be positive.")
        p = multiply(p, [1] + [0] * (degree - 1) + [-1])
    return p


def rational_equal(left, right):
    a, da, sa = left
    b, db, sb = right
    if sa < 0 or sb < 0:
        raise ValueError("This data format uses nonnegative shifts.")
    return multiply([0] * sa + a, denominator(db)) == multiply(
        [0] * sb + b, denominator(da))


EXPECTED = {
    "identity": ([669807, -3348976, 7783173, -10577048, 8928985,
                  -4635736, 1361923, -173936], 8),
    "H": ([2349, -7519, 9303, -5255, 1138], 5),
    "V": ([2069, -6465, 7915, -4447, 960], 5),
    "HV": ([335, -806, 669, -190], 4),
}
COUNT_NUMERATOR = [168640, -844590, 1965375, -2673454,
                   2258540, -1173244, 344837, -44056]


def aggregate(records):
    """Sum full rational functions; no coefficient cutoff."""
    if not records:
        return {"minus_order": 0, "plus_order": 0, "numerator": [0]}
    for record in records:
        assert set(record[1]) <= {1, 2}, "Unexpected denominator degree."
        assert record[2] >= 0
    a = max(len(record[1]) for record in records)
    b = max(record[1].count(2) for record in records)
    numerator = [0]
    for top, degrees, shift in records:
        numerator = add(numerator, multiply(
            [0] * shift + top, powers(a - len(degrees), b - degrees.count(2))))
    return {"minus_order": a, "plus_order": b, "numerator": numerator}


def verify_all_action_sums(action_records):
    sums = {}
    for action, (top, order) in EXPECTED.items():
        data = aggregate(action_records[action])
        a, b = data["minus_order"], data["plus_order"]
        assert a >= order
        assert data["numerator"] == multiply([0] * 4 + top, powers(a - order, b)), action
        sums[action] = data
    a = max(data["minus_order"] for data in sums.values())
    b = max(data["plus_order"] for data in sums.values())
    total = [0]
    for data in sums.values():
        total = add(total, multiply(data["numerator"], powers(
            a - data["minus_order"], b - data["plus_order"])))
    assert total == multiply([0] * 4 + [4 * c for c in COUNT_NUMERATOR], powers(a - 8, b))
    left = [0]
    for k, value in enumerate(COUNT_NUMERATOR):
        term = [value]
        for j in range(7):
            term = multiply(term, [4 - k - j, 1])
        left = add(left, term)
    right = [4 * c for c in multiply(
        [710640, 1665222, 1582743, 685145, 137740, 12928, 512], [1, 1])]
    assert left == right
    return {"action_sums": sums, "scaled_polynomial_coefficients": left,
            "full_rational_differences": [0], "polynomial_coefficient_difference": [0]}
