"""Generate the fixed certificate in a new output path."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.torusgrid_certificate import make_certificate

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
if args.output.exists():
    raise SystemExit('Output already exists; choose a fresh path')
certificate = make_certificate()
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(certificate, indent=2) + '\n')
print(json.dumps({key: certificate[key] for key in (
    'basis_sha256', 'chain_dimensions', 'residual_chain_dimensions',
    'rank_d4_Q', 'relative_H4_free_rank')}, indent=2))
