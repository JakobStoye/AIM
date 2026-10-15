"""Independent point-count controls and effective certificate rejection tests."""
import json
from pathlib import Path
import tempfile
import unittest
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from half_integral_ehrhart.signatures import (
    signature_parts, signatures, signature_count, witness, ehrhart_value,
    has_period_collapse)
from half_integral_ehrhart.geometry import invariants, brute_counts, row_count
from half_integral_ehrhart.certificates import verify_certificates
from half_integral_ehrhart.source_data import decode

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = ROOT/"numerical_case/certificates/dual_weights.json"


class WitnessTests(unittest.TestCase):
    def test_complete_small_sets_against_geometry(self):
        for i in (2, 3):
            parts = signature_parts(i)
            self.assertFalse(parts[0] & parts[1] or parts[0] & parts[2] or parts[1] & parts[2])
            values = signatures(i)
            self.assertEqual(len(values), signature_count(i))
            for value in values:
                q = witness(i, value)
                self.assertEqual(invariants(q), (i, value[1], value[0], value[2]))
                inside, boundary = brute_counts(q)
                self.assertEqual((len(inside), len(boundary)), (i, value[1]))

    def test_dilation_counts(self):
        for value in signatures(2):
            q = witness(2, value)
            self.assertEqual(ehrhart_value(2, value, 0), 1)
            for t in (1, 2, 3, 4, 5):
                scaled = tuple((t*x, t*y) for x, y in q)
                self.assertEqual(row_count(scaled), ehrhart_value(2, value, t))

    def test_large_parameter_endpoints(self):
        for i in (17, 65):
            cases = [
                (6*i+2, 2, 4), (8*i, 2, 4), (12*i+8, 2, 4),
                (16*i+16, 2*i+4, 4*i+8),
                (18*i+18, 3*i+6, 6*i+12),
                (4*i+4, 2, 4), (8*i+8, 2, 4*i+8),
                (12*i+2*(2*i+2)+8, 2*i+2, 2*(2*i+2)+4)]
            for value in cases:
                self.assertEqual(invariants(witness(i, value)),
                                 (i, value[1], value[0], value[2]))

    def test_merged_edge_boundary_point(self):
        q = witness(2, (32, 2, 4))
        self.assertEqual(len(q), 3)
        inside, boundary = brute_counts(q)
        self.assertIn((1, 0), boundary)
        self.assertEqual(invariants(q), (2, 2, 32, 4))

    def test_line_and_body_period_collapse_are_distinct(self):
        body, line = (16, 2, 4), (16, 2, 8)
        self.assertTrue(has_period_collapse(2, body))
        self.assertFalse(has_period_collapse(2, line))
        self.assertEqual(ehrhart_value(2, body, 1), ehrhart_value(2, line, 1))
        self.assertEqual(ehrhart_value(2, body, 2), 11)
        self.assertEqual(ehrhart_value(2, line, 2), 13)
        for value in (body, line):
            self.assertEqual(row_count(tuple((2*x, 2*y) for x, y in witness(2, value))),
                             ehrhart_value(2, value, 2))

    def test_invalid_domain_and_signatures(self):
        for i in (0, 1, -2):
            with self.assertRaises(ValueError):
                signatures(i)
        with self.assertRaises(TypeError):
            signatures(2.0)
        with self.assertRaises(ValueError):
            witness(2, (34, 2, 4))
        with self.assertRaises(ValueError):
            ehrhart_value(2, (16, 2, 4), -1)


class CertificateTests(unittest.TestCase):
    def mutate(self, f):
        value = json.loads(WEIGHTS.read_text())
        f(value)
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"weights.json"
            p.write_text(json.dumps(value))
            with self.assertRaises(ValueError):
                verify_certificates(p)

    def test_valid_all_width_patterns(self):
        self.assertEqual(len(verify_certificates(WEIGHTS)["cases"]), 21)

    def test_missing_case(self):
        self.mutate(lambda v: v["cases"].pop())

    def test_duplicate_case(self):
        self.mutate(lambda v: v["cases"].append(v["cases"][0]))

    def test_unknown_label(self):
        self.mutate(lambda v: v["cases"][0]["nonzero_weights"].update({"not_a_constraint": "1"}))

    def test_negative_weight(self):
        def edit(v):
            key = next(iter(v["cases"][0]["nonzero_weights"]))
            v["cases"][0]["nonzero_weights"][key] = "-1"
        self.mutate(edit)

    def test_float_weight(self):
        def edit(v):
            key = next(iter(v["cases"][0]["nonzero_weights"]))
            v["cases"][0]["nonzero_weights"][key] = 0.5
        self.mutate(edit)

    def test_false_claimed_bound(self):
        self.mutate(lambda v: v["cases"][0].update(upper_bound="7"))

    def test_ineffective_zero_combination(self):
        self.mutate(lambda v: v["cases"][0].update(nonzero_weights={}))


try:
    import h5py
    import numpy as np
except ImportError:
    h5py = None


@unittest.skipIf(h5py is None, "Install the optional pinned source-data dependencies")
class DecoderTests(unittest.TestCase):
    def fixture(self, values, key="a16", dtype="int64", expected=None):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"data.h5"
            with h5py.File(p, "w") as f:
                f.create_dataset(key, data=np.array(values, dtype=dtype))
            if expected is None:
                with self.assertRaises(ValueError):
                    decode(p, 2)
            else:
                self.assertEqual(decode(p, 2), expected)

    def test_integer_residue_normalization(self):
        self.fixture([[[16, 16], [8, 8], [8, 8]]], expected={(16, 2, 4)})

    def test_float_schema_rejected(self):
        self.fixture([[[16, 16], [8, 8], [8, 8]]], dtype="float64")

    def test_wrong_original_interior_count(self):
        self.fixture([[[16, 16], [8, 8], [16, 8]]])

    def test_duplicate_function_rejected(self):
        self.fixture([[[16, 16], [8, 8], [8, 8]]]*2)

    def test_wrong_area_group_rejected(self):
        self.fixture([[[16, 16], [8, 8], [8, 8]]], key="a17")


if __name__ == "__main__":
    unittest.main()
