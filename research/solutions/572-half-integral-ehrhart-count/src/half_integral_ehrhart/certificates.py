"""Check the retained rational inequalities; no optimizer is imported."""
from fractions import Fraction
import json
import re
from pathlib import Path
from .section_model import model


def rational(value):
    if not isinstance(value, str) or not re.fullmatch(r"-?\d+(?:/[1-9]\d*)?", value):
        raise ValueError("Certificate scalars must be exact integer/fraction strings")
    return Fraction(value)


def verify_certificates(path):
    data = json.loads(Path(path).read_text())
    found, report = set(), []
    for case in data["cases"]:
        pair = case["pattern"], case["n"]
        if pair in found:
            raise ValueError(f"Duplicate certificate {pair}")
        found.add(pair)
        m = model(*pair)
        if not set(case["nonzero_weights"]) <= set(m["labels"]):
            raise ValueError(f"Unknown constraint label in {pair}")
        weights = [rational(case["nonzero_weights"].get(k, "0"))
                   for k in m["labels"]]
        if any(w < 0 for w in weights):
            raise ValueError(f"Negative weight in {pair}")
        for j, target in enumerate(m["objective"]):
            actual = sum(w*row[j] for w, row in zip(weights, m["A"]))
            if actual < target:
                raise ValueError(f"Coordinate domination fails at {pair}/{m['names'][j]}")
        bound = sum(w*r for w, r in zip(weights, m["rhs"]))
        if bound != rational(case["upper_bound"]) or bound > 6:
            raise ValueError(f"Invalid bound in {pair}")
        report.append({"pattern": pair[0], "n": pair[1], "bound": str(bound)})
    if found != {(p, n) for p in ("EE", "EO", "OO") for n in range(2, 9)}:
        raise ValueError("Required certificate case coverage is incomplete")
    return {"status": "EXACT_RATIONAL_INEQUALITIES_VERIFIED", "cases": report}
