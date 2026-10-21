# LatentAtlas paper

**LatentAtlas: Few-Anchor Interfaces for Frozen Reward Transfer Across Autoencoders**

This folder contains the polished **2026-10-20 manuscript snapshot**, including the user-provided overview figure and the completed Cosmos/FLUX matched-baseline results.

| File | Contents |
|---|---|
| [main.pdf](main.pdf) | Main manuscript, 8 pages including references |
| [supplement.pdf](supplement.pdf) | Supplementary material and full supporting proof, 9 pages |
| [latentatlas-overleaf.zip](latentatlas-overleaf.zip) | Self-contained source archive for direct upload to Overleaf |
| [overleaf/](overleaf/) | Unpacked editable LaTeX, bibliography, styles, and required figures |
| [SHA256SUMS](SHA256SUMS) | File checksums for this snapshot |

Upload the ZIP to Overleaf and select `main.tex` with the pdfLaTeX compiler. Select `supplement.tex` to compile the supplement; detailed instructions are in [overleaf/README.md](overleaf/README.md).

The manuscript studies clean-latent, paired-anchor adaptation to a fully frozen DiNa reward. Its main Cosmos/FLUX comparisons use historical development data. The subsequent real-generator and noisy-state pilot records remain in the repository's experiment documentation; this snapshot precedes those pilots.

The PDF and original manuscript sources are preserved byte for byte. The source archive contains only the files needed to edit and compile the paper.
