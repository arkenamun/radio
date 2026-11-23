"""Render one sheet (.dc.html) to an A4 PDF and a PNG preview.

Usage: python3 mkpdf.py sheets/WAERN-Radios.dc.html out.pdf out.png
Uses Playwright's Chromium; set CHROME=/path/to/chrome to use another browser.
"""
import asyncio, os, re, sys
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).resolve().parent
src, out_pdf, out_png = sys.argv[1], sys.argv[2], sys.argv[3]
s = Path(src).read_text()
body = s.split("<x-dc>", 1)[1].split("</x-dc>", 1)[0]
body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
body = body.replace("/_blob/05c1705e66405ecddbcc25eab17e5537", "qr-radio.svg")   # sheet 3 QR (canvas asset)
title = re.search(r"<title>(.*?)</title>", s).group(1)
faces = "\n".join(f"@font-face {{ font-family: '{fam}'; src: url('fonts/{f}.ttf'); font-weight: {w}; }}" for fam, f, w in [
    ("Barlow", "Barlow-Regular", 400), ("Barlow", "Barlow-Medium", 500), ("Barlow", "Barlow-SemiBold", 600), ("Barlow", "Barlow-Bold", 700),
    ("Barlow Semi Condensed", "BarlowSemiCondensed-SemiBold", 600), ("Barlow Semi Condensed", "BarlowSemiCondensed-Bold", 700)])
tmp = HERE / "print_tmp.html"
tmp.write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{faces}
@page {{ size: 794px 1123px; margin: 0; }} html, body {{ margin: 0; padding: 0; }}</style></head><body>{body}</body></html>""")

async def main():
    async with async_playwright() as p:
        opts = {"args": ["--allow-file-access-from-files"]}
        if os.environ.get("CHROME"):
            opts["executable_path"] = os.environ["CHROME"]
        b = await p.chromium.launch(**opts)
        pg = await b.new_page(viewport={"width": 794, "height": 1123})
        await pg.goto(tmp.as_uri()); await pg.evaluate("document.fonts.ready")
        # Fit check: main_overflow must be 0, and nothing may run off the page.
        info = await pg.evaluate("""() => {
            const main = document.querySelector('main');
            const blocks = [...main.children].map(el => [el.tagName, Math.round(el.getBoundingClientRect().top), Math.round(el.getBoundingClientRect().bottom)]);
            const foot = document.querySelector('footer').getBoundingClientRect();
            const over = []; document.querySelectorAll('body *').forEach(el => { const r = el.getBoundingClientRect(); if (r.width && (r.bottom > 1123.5 || r.right > 794.5)) over.push(el.tagName + ':' + (el.textContent||'').trim().slice(0,30)); });
            return {main_overflow: main.scrollHeight - main.clientHeight, blocks, footer: [Math.round(foot.top), Math.round(foot.bottom)], offpage: over.slice(0,5)};
        }""")
        print(Path(src).name, info)
        await pg.screenshot(path=out_png)
        await pg.pdf(path=out_pdf, width="794px", height="1123px", print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}, prefer_css_page_size=True)
        await b.close()
    tmp.unlink()

asyncio.run(main())
