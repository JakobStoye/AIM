"""Reject corrupted proof-critical data, beyond ordinary positive-path checks."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "numerical_case"))
from verify import verify


class ExportRejectionControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "numerical_case/exact_series.json").read_text())

    def rejected(self, mutate):
        data = copy.deepcopy(self.data)
        mutate(data)
        raw = ROOT / "numerical_case/raw"
        raw.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=raw) as temporary:
            path = Path(temporary) / "tampered.json"
            path.write_text(json.dumps(data))
            with self.assertRaises(AssertionError):
                verify(path)

    def test_missing_cell_is_rejected(self):
        self.rejected(lambda d: d["groups"][0]["members"].clear())

    def test_wrong_grading_is_rejected(self):
        self.rejected(lambda d: d["groups"][0]["grading_readback"][0].__setitem__(-1, 1))

    def test_changed_series_is_rejected(self):
        self.rejected(lambda d: d["groups"][0]["series"][0].__setitem__(
            0, d["groups"][0]["series"][0][0] + 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
