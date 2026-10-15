"""Version-pinned source-file checking and exact HDF5 coefficient decoding."""
import hashlib
import json
from pathlib import Path
from .signatures import signatures


def verify_input(path, entry):
    raw = Path(path).read_bytes()
    if (len(raw) != entry["bytes"]
            or hashlib.sha256(raw).hexdigest() != entry["sha256"]
            or hashlib.md5(raw).hexdigest() != entry["md5"]):
        raise ValueError(f"Source-file checksum/size mismatch: {path}")


def decode(path, i):
    """Decode all fixed-i functions, including b=0,1, using integer arrays."""
    import h5py  # Optional dependency needed only by source-set verification.
    result = set()
    with h5py.File(path, "r") as f:
        for key, dataset in f.items():
            if not (key.startswith("a") and key[1:].isdigit()):
                continue
            if (not isinstance(dataset, h5py.Dataset)
                    or dataset.ndim != 3 or dataset.shape[1:] != (3, 2)
                    or dataset.dtype.kind not in "iu"):
                raise ValueError(f"Invalid integer coefficient schema at {key}")
            for m in dataset[...]:
                A, b4, B2 = int(m[0, 0]), int(m[1, 0]), int(m[1, 1])
                if (int(m[0, 1]) != A or key != "a"+str(A)
                        or b4 % 4 or B2 % 2 or int(m[2, 1]) != 8):
                    raise ValueError(f"Coefficient normalization mismatch at {key}")
                b, B = b4//4, B2//2
                if (int(m[2, 0]) != 8*i+4*b-A or (A-B) % 2
                        or b < 0 or B < 0):
                    raise ValueError(f"Fixed-i/parity/count mismatch at {key}")
                value = (A, b, B)
                if value in result:
                    raise ValueError(f"Duplicate entire-function signature {value}")
                result.add(value)
    if not result:
        raise ValueError("No coefficient signatures found")
    return result


def compare_source_sets(data_dir, manifest_path):
    manifest = json.loads(Path(manifest_path).read_text())
    if manifest["version"] != "1.0.0":
        raise ValueError("Unexpected source version")
    found, report = set(), []
    for entry in manifest["files"]:
        i = entry["i"]
        if i in found:
            raise ValueError("Duplicate input index")
        found.add(i)
        path = Path(data_dir)/entry["filename"]
        verify_input(path, entry)
        full = decode(path, i)
        actual = {x for x in full if x[1] >= 2}
        expected = signatures(i)
        missing, extra = expected-actual, actual-expected
        if missing or extra:
            raise ValueError(f"Exact set mismatch at i={i}: missing={sorted(missing)[:8]}, extra={sorted(extra)[:8]}")
        report.append({"i": i, "full_functions": len(full),
                       "b_ge_2": len(actual), "C_i": len(expected),
                       "missing": 0, "extra": 0,
                       "input_sha256": entry["sha256"]})
    if found != set(range(2, 17)):
        raise ValueError("Required source input indices are incomplete")
    return {"status": "EXACT_FIXED_SOURCE_SET_EQUALITY_VERIFIED",
            "version": "1.0.0", "cases": report,
            "trust": "Relative to the cited published catalogue completeness; no independent polygon classification"}
