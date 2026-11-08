# Philosophische Essays

| Essay | Gewähltes Zitat | Dateien |
|---|---|---|
| Gefühl oder Gründe? | „Sind moralische Urteile bloß Ausdruck unserer Gefühle?“ | `Essay_Moralische_Urteile.md/.docx/.pdf` |
| Das übelste der Übel? | „Hoffnung […] ist in Wahrheit das übelste der Übel, weil sie die Qual der Menschen verlängert.“ (Nietzsche) | `Essay_Hoffnung.md/.docx/.pdf` |

Die Markdown-Dateien sind die Quelle. Word- und PDF-Version neu erzeugen:

```bash
python3 build_docx.py Essay_Hoffnung.md Essay_Hoffnung.docx
soffice --headless --convert-to pdf Essay_Hoffnung.docx
```

Format: DIN A4, Times New Roman 12 pt, Zeilenabstand 1,5, Ränder 2,5 cm, Literaturverzeichnis auf eigener Seite.
