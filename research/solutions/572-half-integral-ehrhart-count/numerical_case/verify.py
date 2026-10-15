"""Reproduce the paper's retained certificates and fixed-source comparison."""
import argparse
from pathlib import Path
import sys
import json
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from half_integral_ehrhart.certificates import verify_certificates
from half_integral_ehrhart.source_data import compare_source_sets

def main():
    root = Path(__file__).resolve().parent
    p = argparse.ArgumentParser()
    p.add_argument("--data-dir", type=Path)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    result = {"dual": verify_certificates(root/"certificates/dual_weights.json")}
    if args.data_dir:
        result["source_sets"] = compare_source_sets(args.data_dir, root/"input_manifest.json")
    result["python"] = sys.version
    result["integer_arithmetic"] = "Python integers and fractions.Fraction"
    result["assertions_disabled"] = bool(sys.flags.optimize)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v["status"] for k, v in result.items() if isinstance(v, dict)}, indent=2))

if __name__ == "__main__":
    main()
