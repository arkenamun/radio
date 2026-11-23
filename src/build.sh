#!/bin/sh
# Rebuild the Radio User Guide PDFs into src/out/.
set -e
cd "$(dirname "$0")"
python3 build1.py                 # writes sheets/WAERN-Radios.dc.html
python3 build2.py                 # writes sheets/Talking-on-the-Radio.dc.html
python3 watermark.py sheets/*.dc.html   # DRAFT watermark; delete this line for a final issue
mkdir -p out
python3 mkpdf.py sheets/WAERN-Radios.dc.html out/sheet1.pdf out/sheet1.png
python3 mkpdf.py sheets/Talking-on-the-Radio.dc.html out/sheet2.pdf out/sheet2.png
python3 mkpdf.py sheets/Main.dc.html out/sheet3.pdf out/sheet3.png
python3 combine.py out/sheet1.pdf out/sheet2.pdf out/sheet3.pdf out/radio-user-guide-a4.pdf
