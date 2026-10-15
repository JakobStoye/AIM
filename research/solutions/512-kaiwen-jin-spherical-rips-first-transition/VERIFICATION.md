# Build and file verification

The mathematical evidence is the complete analytic argument in `paper/main.tex` and its cited primary sources. The supplied PDF is the compiled manuscript. File checks and compilation support delivery review; the solution claim is submitted for independent mathematical review.

From this package directory, check the distributed file hashes:

```sh
python3 - <<'PYCODE'
from pathlib import Path
import hashlib
for line in Path("SHA256SUMS").read_text().splitlines():
    expected, filename = line.split(maxsplit=1)
    observed = hashlib.sha256(Path(filename).read_bytes()).hexdigest()
    assert observed == expected, filename
    print("OK", filename)
PYCODE
```

Build using a standard LaTeX distribution with latexmk, amsmath, amssymb, amsthm, geometry, lmodern and hyperref:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The generated PDF is `build/main.pdf`. Checksums identify the distributed files; a rebuilt PDF may have different date and producer metadata. No additional manuscript inputs, graphics, private supplement, proof-critical computation or numerical dataset is required.

The provided source was compiled with pdfTeX 1.40.27 (TeX Live 2025), and all eight rendered pages were inspected. The final isolation-build result is recorded in the package's public manifest.
