# Skill: BibTeX Citation Guide

## Purpose

This guide explains how to use **BibTeX** to manage references and citations in LaTeX documents.

---

## 1. Create a `.bib` File

Create a file named `references.bib`.

Example:

```bibtex
@article{vaswani2017attention,
  author  = {Ashish Vaswani and Noam Shazeer and Niki Parmar and Jakob Uszkoreit and Llion Jones and Aidan N. Gomez and Lukasz Kaiser and Illia Polosukhin},
  title   = {Attention Is All You Need},
  journal = {Advances in Neural Information Processing Systems},
  volume  = {30},
  year    = {2017}
}

@book{goodfellow2016dl,
  author    = {Ian Goodfellow and Yoshua Bengio and Aaron Courville},
  title     = {Deep Learning},
  publisher = {MIT Press},
  year      = {2016}
}

@inproceedings{he2016resnet,
  author    = {Kaiming He and Xiangyu Zhang and Shaoqing Ren and Jian Sun},
  title     = {Deep Residual Learning for Image Recognition},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year      = {2016},
  pages     = {770--778}
}
```

Each BibTeX entry consists of:

- Entry type (`@article`, `@book`, `@inproceedings`, etc.)
- Citation key (`vaswani2017attention`)
- Metadata fields (author, title, year, etc.)

---

## 2. Cite References in LaTeX

Use the `\cite{}` command to cite a reference.

Example:

```latex
Transformer was introduced in \cite{vaswani2017attention}.

ResNet was proposed in \cite{he2016resnet}.

The Deep Learning textbook is described in \cite{goodfellow2016dl}.
```

To cite multiple references:

```latex
\cite{vaswani2017attention,he2016resnet}
```

---

## 3. Generate the Bibliography

Add the following commands near the end of your document.

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```

Where:

- `IEEEtran` specifies the bibliography style.
- `references` is the BibTeX filename (without the `.bib` extension).

---

## 4. Compile the Document

### Using BibTeX

Compile in the following order:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Using Overleaf

Simply click **Recompile**. Overleaf automatically runs BibTeX when necessary.

---

## 5. Common Bibliography Styles

| Style | Description |
|--------|-------------|
| plain | Alphabetical ordering |
| unsrt | Order of citation |
| alpha | Labels such as `[Vas17]` |
| abbrv | Abbreviated author names |
| IEEEtran | IEEE citation style |
| apalike | APA-like style |

Example:

```latex
\bibliographystyle{IEEEtran}
```

---

## 6. Obtaining BibTeX Entries

### Google Scholar

1. Search for the paper.
2. Click the **Cite** (`"`) button.
3. Select **BibTeX**.
4. Copy the generated entry into `references.bib`.

Example:

```bibtex
@inproceedings{vaswani2017attention,
  title={Attention Is All You Need},
  author={Vaswani, Ashish and others},
  booktitle={Advances in Neural Information Processing Systems},
  year={2017}
}
```

Other reliable sources include:

- IEEE Xplore
- ACM Digital Library
- SpringerLink
- DBLP
- Crossref

---

## 7. Recommended Citation Key Format

Use descriptive and consistent citation keys.

Recommended:

```text
authorYearKeyword
```

Examples:

```text
vaswani2017attention
he2016resnet
goodfellow2016dl
dosovitskiy2021vit
```

Avoid generic keys such as:

```text
paper1
reference
abc123
```

---

## 8. Common BibTeX Entry Types

| Entry Type | Purpose |
|------------|---------|
| `@article` | Journal article |
| `@book` | Book |
| `@inproceedings` | Conference paper |
| `@misc` | Miscellaneous resource |
| `@techreport` | Technical report |
| `@phdthesis` | PhD dissertation |
| `@mastersthesis` | Master's thesis |

---

## 9. Typical Workflow

1. Find the publication.
2. Export or copy its BibTeX entry.
3. Paste it into `references.bib`.
4. Cite it using `\cite{citation_key}`.
5. Compile the document.
6. Verify that citations and bibliography are generated correctly.

---

## 10. Best Practices

- Maintain a single `.bib` file for the entire project whenever possible.
- Use consistent and descriptive citation keys.
- Avoid manually editing BibTeX fields unless necessary.
- Obtain BibTeX entries from authoritative sources.
- Verify author names, publication year, title, and venue before submission.
- Remove duplicate entries to keep the bibliography clean.
- Use the bibliography style required by your target journal or conference.

---

## 11. BibLaTeX (Recommended for New Projects)

Many modern LaTeX projects use **biblatex** with **biber** instead of traditional BibTeX.

In the preamble:

```latex
\usepackage[backend=biber,style=ieee]{biblatex}
\addbibresource{references.bib}
```

Citing references:

```latex
According to \cite{vaswani2017attention}, ...
```

Print the bibliography:

```latex
\printbibliography
```

Compile using:

```text
pdflatex
biber
pdflatex
pdflatex
```

**Note:** Some conferences (e.g., IEEE, ACM, Springer) require traditional BibTeX. Always follow the instructions provided by the conference or journal template.