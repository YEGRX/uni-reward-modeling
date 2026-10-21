# LatentAtlas Overleaf source

Editable source for *LatentAtlas: Few-Anchor Interfaces for Frozen Reward Transfer Across Autoencoders*. This is the polished 2026-10-20 manuscript snapshot.

## Open in Overleaf

1. Create a project with **New Project → Upload Project** and select `latentatlas-overleaf.zip` from the parent `paper/` directory.
2. Set **Main document** to `main.tex` and **Compiler** to **pdfLaTeX**. Overleaf runs BibTeX automatically.
3. To build the supplementary material, change **Main document** to `supplement.tex`. Its proof section includes `theory-support.tex`.

Both documents use `references.bib`, the bundled `cvpr.sty` and `ieeenat_fullname.bst`, and the figures under `figures/clean/`. Keep these relative paths.

## Local build

For each main document, run pdfLaTeX, BibTeX, and pdfLaTeX twice. Tectonic can also compile each document. The provided PDFs were built from the exact manuscript source in this directory.
