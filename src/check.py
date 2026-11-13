import os, sys
from playwright.sync_api import sync_playwright
here=os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto("file://"+os.path.join(here,sys.argv[1])); pg.wait_for_timeout(300)
    r=pg.evaluate("""()=>[...document.querySelectorAll('.page')].map((p,i)=>{const pr=p.getBoundingClientRect();let max=0;p.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.bottom>max)max=r.bottom});return {page:i+1,pageBottom:Math.round(pr.bottom),contentBottom:Math.round(max),over:Math.round(max-pr.bottom)}})""")
    for x in r: print(x)
    b.close()
