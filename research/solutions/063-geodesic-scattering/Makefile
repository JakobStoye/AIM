LATEXMK ?= latexmk

.PHONY: all check
all: build/geodesic_scattering.pdf

build/geodesic_scattering.pdf: paper/geodesic_scattering.tex
	mkdir -p build
	$(LATEXMK) -norc -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/geodesic_scattering.tex

check:
	shasum -a 256 -c SHA256SUMS
