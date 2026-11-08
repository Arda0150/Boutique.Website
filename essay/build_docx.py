import re, sys
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
src, out = sys.argv[1], sys.argv[2]
doc = Document()
sec = doc.sections[0]
sec.page_height, sec.page_width = Cm(29.7), Cm(21)
sec.left_margin = sec.right_margin = Cm(2.5); sec.top_margin = sec.bottom_margin = Cm(2.5)
st = doc.styles['Normal']; st.font.name = 'Times New Roman'; st.font.size = Pt(12)
st.paragraph_format.line_spacing = 1.5; st.paragraph_format.space_after = Pt(6)
def add_runs(p, text):
    for part in re.split(r'(\*[^*]+\*)', text):
        if part.startswith('*') and part.endswith('*'):
            r = p.add_run(part[1:-1]); r.italic = True
        elif part: p.add_run(part)
lit = False
for line in open(src, encoding='utf-8').read().split('\n'):
    if not line.strip() or line.strip() == '---': continue
    if line.startswith('# '):
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(line[2:]); r.bold = True; r.font.size = Pt(16)
    elif line.startswith('## '):
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(line[3:]); r.italic = True
    elif line.startswith('### '):
        lit = 'Literatur' in line
        if lit: doc.add_page_break()
        p = doc.add_paragraph(); r = p.add_run(line[4:]); r.bold = True; r.font.size = Pt(13)
    else:
        p = doc.add_paragraph(); add_runs(p, line)
        if lit:
            p.paragraph_format.left_indent = Cm(1); p.paragraph_format.first_line_indent = Cm(-1)
            p.paragraph_format.line_spacing = 1.15
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
doc.save(out)
