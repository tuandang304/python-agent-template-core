# BibTeX Complete Reference

## Common BibTeX Entry Types

| Entry Type | Purpose | Required Fields |
|---|---|---|
| `@article` | Journal article | author, title, journal, year |
| `@book` | Book | author/editor, title, publisher, year |
| `@inproceedings` | Conference paper | author, title, booktitle, year |
| `@misc` | Miscellaneous resource | (none strictly required) |
| `@techreport` | Technical report | author, title, institution, year |
| `@phdthesis` | PhD dissertation | author, title, school, year |
| `@mastersthesis` | Master's thesis | author, title, school, year |

## Common Bibliography Styles

| Style | Description |
|---|---|
| `plain` | Alphabetical ordering, numeric labels |
| `unsrt` | Order of citation, numeric labels |
| `alpha` | Alphabetical ordering, labels like `[Vas17]` |
| `abbrv` | Abbreviated author names, numeric labels |
| `IEEEtran` | IEEE citation style |
| `apalike` | APA-like style |

## Extended Entry Examples

### Journal Article

```bibtex
@article{vaswani2017attention,
  author  = {Ashish Vaswani and Noam Shazeer and Niki Parmar and Jakob Uszkoreit and Llion Jones and Aidan N. Gomez and Lukasz Kaiser and Illia Polosukhin},
  title   = {Attention Is All You Need},
  journal = {Advances in Neural Information Processing Systems},
  volume  = {30},
  year    = {2017}
}
```

### Book

```bibtex
@book{goodfellow2016dl,
  author    = {Ian Goodfellow and Yoshua Bengio and Aaron Courville},
  title     = {Deep Learning},
  publisher = {MIT Press},
  year      = {2016}
}
```

### Conference Paper

```bibtex
@inproceedings{he2016resnet,
  author    = {Kaiming He and Xiangyu Zhang and Shaoqing Ren and Jian Sun},
  title     = {Deep Residual Learning for Image Recognition},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year      = {2016},
  pages     = {770--778}
}
```

## Overleaf Usage

When using Overleaf, simply click **Recompile**. Overleaf automatically runs BibTeX when necessary — no manual multi-step compilation required.

## Typical Workflow

1. Find the publication.
2. Export or copy its BibTeX entry from Google Scholar or the publisher's site.
3. Paste the entry into `references.bib`.
4. Cite it using `\cite{citation_key}` in the LaTeX document.
5. Compile the document (or recompile in Overleaf).
6. Verify that citations and bibliography render correctly.
