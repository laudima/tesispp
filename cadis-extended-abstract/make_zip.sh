#!/usr/bin/env bash
# Build the Springer LNCS source package for the CADIS paper.
# Compiles main.tex, packs only the files the paper uses, and checks
# that the package compiles on its own in a clean directory.
set -euo pipefail
cd "$(dirname "$0")"

FILES=(
  main.tex main.bbl references.bib llncs.cls splncs04.bst
  fig_design.tex fig_rosen.tex
  tables/variants_rows.tex tables/differences_rows.tex
  tables/cot_variants_rows.tex tables/prior_rows.tex
  figures/accuracy_by_variant.pdf figures/accuracy_direct_vs_cot.pdf
  main.pdf
)

pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
bibtex main >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

rm -f ../cadis-submission.zip
zip -q ../cadis-submission.zip "${FILES[@]}"

test_dir=$(mktemp -d)
unzip -q ../cadis-submission.zip -d "$test_dir"
(cd "$test_dir" && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null \
                && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null)
echo "OK: ../cadis-submission.zip compiles on its own"
rm -rf "$test_dir"
