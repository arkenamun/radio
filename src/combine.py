"""Join the three sheet PDFs into one, with a title and a bookmark per sheet.

Usage: python3 combine.py sheet1.pdf sheet2.pdf sheet3.pdf out.pdf
"""
import sys, pikepdf
from pikepdf import OutlineItem

*parts, out = sys.argv[1:]
pdf = pikepdf.new()
for part in parts:
    pdf.pages.extend(pikepdf.open(part).pages)
with pdf.open_metadata() as m:
    m["dc:title"] = "Radio User Guide"
pdf.docinfo["/Title"] = "Radio User Guide"
pdf.docinfo["/Subject"] = "Denmark Bushfire Brigades WAERN radio use: WAERN Radios, Talking on the Radio, Common Radio Issues"
with pdf.open_outline() as ol:
    ol.root.extend([OutlineItem("1 WAERN Radios", 0), OutlineItem("2 Talking on the Radio", 1), OutlineItem("3 Common Radio Issues", 2)])
pdf.save(out)
print("combined", len(pdf.pages), "pages ->", out)
