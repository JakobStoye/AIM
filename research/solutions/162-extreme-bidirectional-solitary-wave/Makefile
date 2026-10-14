LATEXMK ?= latexmk

.PHONY: pdf
pdf:
	$(LATEXMK) -pdf -pdflatex='pdflatex -no-shell-escape %O %S' -interaction=nonstopmode -halt-on-error -outdir=build paper/manuscript.tex
