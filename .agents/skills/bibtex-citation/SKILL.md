---
name: BibTeX Citation
description: This skill should be used when the user asks to "add a citation", "cite a reference", "create a .bib file", "add BibTeX entry", "format bibliography", "use BibTeX in LaTeX", "set up references.bib", "cite paper in LaTeX", "bibliography style", "biblatex setup", or needs guidance on managing references, citation keys, compiling with BibTeX/biber, or obtaining BibTeX entries from Google Scholar and academic databases.
version: 0.1.0
---

# BibTeX Citation Guide

Manage references and citations in LaTeX documents using BibTeX or biblatex.

## Core Workflow

1. Create a `.bib` file (e.g., `references.bib`) containing BibTeX entries.
2. Cite references in LaTeX using `\cite{citation_key}`.
3. Add bibliography commands at the end of the document.
4. Compile the document in the correct order.

## BibTeX Entry Structure

Each entry consists of three parts:

- **Entry type**: `@article`, `@book`, `@inproceedings`, `@misc`, etc.
- **Citation key**: A unique identifier (e.g., `vaswani2017attention`)
- **Metadata fields**: `author`, `title`, `year`, `journal`, `booktitle`, etc.

Example entry:

```bibtex
@article{vaswani2017attention,
  author  = {Ashish Vaswani and Noam Shazeer and Niki Parmar and Jakob Uszkoreit and Llion Jones and Aidan N. Gomez and Lukasz Kaiser and Illia Polosukhin},
  title   = {Attention Is All You Need},
  journal = {Advances in Neural Information Processing Systems},
  volume  = {30},
  year    = {2017}
}
```

## Citing References

Single citation:

```latex
Transformer was introduced in \cite{vaswani2017attention}.
```

Multiple citations:

```latex
\cite{vaswani2017attention,he2016resnet}
```

## Bibliography Setup

### Traditional BibTeX

Add near the end of the document:

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```

Compile order:

```
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Modern biblatex (Recommended for New Projects)

In the preamble:

```latex
\usepackage[backend=biber,style=ieee]{biblatex}
\addbibresource{references.bib}
```

Print bibliography:

```latex
\printbibliography
```

Compile order:

```
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

> **Note:** Some conferences (IEEE, ACM, Springer) require traditional BibTeX. Always follow the template instructions.

## Citation Key Convention

Use the format `authorYearKeyword`:

```
vaswani2017attention
he2016resnet
goodfellow2016dl
dosovitskiy2021vit
```

Avoid generic keys like `paper1`, `reference`, or `abc123`.

## Obtaining BibTeX Entries

1. **Google Scholar** → Click Cite (`"`) → Select BibTeX → Copy entry.
2. **IEEE Xplore**, **ACM Digital Library**, **SpringerLink**, **DBLP**, **Crossref** — export BibTeX directly.

## Best Practices

- Maintain a single `.bib` file per project whenever possible.
- Use consistent, descriptive citation keys.
- Obtain entries from authoritative sources rather than writing them manually.
- Verify author names, year, title, and venue before submission.
- Remove duplicate entries.
- Use the bibliography style required by the target journal or conference.

## Additional Resources

### Reference Files

For detailed entry types, common bibliography styles, and advanced examples, consult:
- **`references/guide.md`** — Complete BibTeX reference with entry types table, bibliography styles comparison, and extended examples.
