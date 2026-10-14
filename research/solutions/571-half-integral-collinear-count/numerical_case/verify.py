"""Check all exported inputs, multiplicities, gradings and entire rational identities."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from chain_models import models
from exact_algebra import verify_all_action_sums


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def verify(path=None):
    if not __debug__:
        raise RuntimeError("Verification requires ordinary Python; do not use -O.")
    path = Path(path) if path else ROOT / "numerical_case/exact_series.json"
    document = json.loads(path.read_text())
    assert document["format_version"] == 1
    groups = document["groups"]
    assert len(groups) == document["unique_systems"] == 608
    counts = {"identity": 420, "H": 72, "V": 84, "HV": 42}
    cell_models = {action: list(models(action)) for action in counts}
    assert {action: len(items) for action, items in cell_models.items()} == counts
    seen = set()
    seen_inputs = set()
    action_records = {action: [] for action in counts}
    for group in groups:
        payload = group["input"]
        digest = hashlib.sha256(canonical(payload)).hexdigest()
        assert digest == group["input_sha256"]
        assert digest not in seen_inputs
        seen_inputs.add(digest)
        grade = payload["grading"][0]
        assert grade == [0] * (len(grade) - 1) + [1]
        assert group["grading_readback"] == [grade + [0], 1]
        assert group["members"]
        for member in group["members"]:
            action, index = member["action"], member["index"]
            assert (action, index) not in seen
            model = cell_models[action][index]
            expected = {key: model[key] for key in
                        ["inhom_inequalities", "inhom_equations", "grading"]}
            assert expected == payload, (action, index)
            seen.add((action, index))
            action_records[action].append(group["series"])
    assert seen == {(action, index) for action, count in counts.items()
                    for index in range(count)}
    assert len(seen) == document["cell_members"] == 618
    algebra = verify_all_action_sums(action_records)
    return {"status": "STORED_DATA_ALGEBRA_VERIFIED", "unique_inputs": 608,
            "cell_members": 618, "counts": counts, **algebra,
            "scope": "Exact exported-input and integer-algebra verification; does not independently certify Normaliz outputs."}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
