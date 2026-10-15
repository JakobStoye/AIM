"""Retrieve the public fixed-version inputs and check their exact bytes."""
from pathlib import Path
import argparse
import json
import os
import sys
import tempfile
import urllib.request
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from half_integral_ehrhart.source_data import verify_input

def main():
    root = Path(__file__).resolve().parent
    p = argparse.ArgumentParser()
    p.add_argument("--destination", type=Path, default=root/"raw/source_data")
    args = p.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((root/"input_manifest.json").read_text())
    for entry in manifest["files"]:
        final = args.destination/entry["filename"]
        if final.exists():
            verify_input(final, entry)
            continue
        fd, temporary = tempfile.mkstemp(prefix=".input-", dir=args.destination)
        try:
            request = urllib.request.Request(entry["url"], headers={"User-Agent": "Ehrhart exact verification"})
            with os.fdopen(fd, "wb") as stream:
                with urllib.request.urlopen(request, timeout=60) as response:
                    while block := response.read(1 << 20):
                        stream.write(block)
            verify_input(temporary, entry)
            os.replace(temporary, final)
            print(f"Verified {entry['filename']}")
        finally:
            if Path(temporary).exists():
                Path(temporary).unlink()

if __name__ == "__main__":
    main()
