import os
BSC = "font-family: 'Barlow Semi Condensed', 'Barlow', sans-serif"
def key(t, bg="#FFFFFF", bd="#9CA3AF"):
    return (f'<span style="display: inline-block; box-sizing: border-box; min-width: 20px; padding: 0 4px; border: 1px solid {bd}; '
            f'border-radius: 4px; background: {bg}; font-size: 13px; font-weight: 700; line-height: 17px; text-align: center; color: #1F2937">{t}</span>')
def b(t): return f'<b style="font-weight: 600">{t}</b>'
def table(rows, label_color, label_w=122):
    cells = []
    for want, do in rows:
        cells.append(f'<div style="font-size: 14px; font-weight: 600; line-height: 1.3; color: {label_color}">{want}</div>')
        cells.append(f'<div style="font-size: 14px; line-height: 1.3; color: #1F2937">{do}</div>')
    return (f'<div style="display: grid; grid-template-columns: {label_w}px minmax(0, 1fr); column-gap: 12px; row-gap: 6px; align-items: baseline">'
            + "\n".join(cells) + '</div>')

def lcd(inner, w=22):
    return (f'<svg width="{w}" height="18" viewBox="0 0 {w} 18" aria-hidden="true" style="display: inline-block; vertical-align: -4px">'
            f'<rect x="0.5" y="0.5" width="{w-1}" height="17" rx="3" fill="#D9F2B4" stroke="#6B7280" stroke-width="1"></rect>{inner}</svg>')
TA_ICON = lcd('<g fill="#1F2937" transform="translate(3 1)"><rect x="1" y="1.5" width="1" height="13"></rect><rect x="2.6" y="3.5" width="1.8" height="11"></rect>'
              '<rect x="11.6" y="1.5" width="1.8" height="13"></rect><rect x="14" y="5" width="1" height="9.5"></rect>'
              '<rect x="5.2" y="7.2" width="2" height="1.6"></rect><polygon points="7.2,5.3 10.2,8 7.2,10.7"></polygon></g>')
def _plus(cy):
    return (f'<rect x="8.4" y="{cy-2.4}" width="1.6" height="4.8"></rect><rect x="6.6" y="{cy-0.8}" width="2" height="1.6"></rect>'
            f'<polygon points="10,{cy-2} 12.6,{cy} 10,{cy+2}"></polygon>')
DUALTX_ICON = lcd('<g fill="#1F2937" transform="translate(3 1)"><rect x="2" y="1.5" width="1" height="13"></rect><rect x="3.6" y="4" width="1.8" height="10.5"></rect>'
                  + _plus(4.6) + _plus(11.2) + '</g>')
ORANGE_KEY = '<span style="display: inline-block; box-sizing: border-box; width: 20px; height: 15px; border: 1px solid #C2410C; border-radius: 7px; background: #FB8C00; vertical-align: -2px"></span>'
GPS_TODO = '<span style="background: #FDE68A; padding: 0 3px; white-space: nowrap">[GPS menu item]</span>'

tait_svg = '''<div style="display: flex; gap: 14px; align-items: flex-end; flex-shrink: 0">
<div style="display: flex; flex-direction: column; align-items: center; gap: 2px">
<svg width="155" height="81" viewBox="0 0 168 88" aria-hidden="true" style="display: block">
<path d="M26 64 C26 74 30 78 38 76 C44 75 46 72 48 70" fill="none" stroke="#1F2937" stroke-width="2"></path>
<rect x="2" y="2" width="40" height="62" rx="13" fill="#1F2937"></rect>
<rect x="0" y="16" width="4" height="20" rx="2" fill="#6B7280"></rect>
<rect x="11" y="8" width="22" height="7" rx="3" fill="#4B5563"></rect>
<g fill="#6B7280"><ellipse cx="14" cy="24" rx="4.2" ry="3"></ellipse><ellipse cx="22" cy="24" rx="4.2" ry="3"></ellipse><ellipse cx="30" cy="24" rx="4.2" ry="3"></ellipse>
<ellipse cx="14" cy="32" rx="4.2" ry="3"></ellipse><ellipse cx="22" cy="32" rx="4.2" ry="3"></ellipse><ellipse cx="30" cy="32" rx="4.2" ry="3"></ellipse>
<ellipse cx="14" cy="40" rx="4.2" ry="3"></ellipse><ellipse cx="22" cy="40" rx="4.2" ry="3"></ellipse><ellipse cx="30" cy="40" rx="4.2" ry="3"></ellipse>
<ellipse cx="14" cy="48" rx="4.2" ry="3"></ellipse><ellipse cx="22" cy="48" rx="4.2" ry="3"></ellipse><ellipse cx="30" cy="48" rx="4.2" ry="3"></ellipse></g>
<rect x="34" y="30" width="132" height="56" rx="20" fill="#FACC15" stroke="#A16207" stroke-width="1.2"></rect>
<circle cx="50" cy="50" r="7.5" fill="#1F2937"></circle>
<circle cx="63" cy="40" r="3.5" fill="#F3F4F6" stroke="#6B7280" stroke-width="0.8"></circle>
<rect x="43" y="64" width="13" height="13" rx="3" fill="#1F2937"></rect>
<rect x="70" y="36" width="58" height="30" rx="8" fill="#111827"></rect>
<rect x="75" y="40" width="48" height="22" rx="3" fill="#D9F2B4"></rect>
<text x="99" y="55" text-anchor="middle" font-size="10" font-weight="700" fill="#1F2937">173</text>
<circle cx="134" cy="38" r="1.6" fill="#DC2626"></circle><circle cx="139" cy="38" r="1.6" fill="#16A34A"></circle><circle cx="144" cy="38" r="1.6" fill="#D97706"></circle>
<g fill="#FFFFFF" stroke="#A16207" stroke-width="0.7"><ellipse cx="72" cy="76" rx="6" ry="4"></ellipse><ellipse cx="85" cy="79" rx="5.5" ry="3.6"></ellipse><ellipse cx="113" cy="79" rx="5.5" ry="3.6"></ellipse><ellipse cx="126" cy="76" rx="6" ry="4"></ellipse></g>
<g fill="#FEF3C7" stroke="#A16207" stroke-width="0.7"><ellipse cx="99" cy="73" rx="7" ry="2.8"></ellipse><ellipse cx="99" cy="80" rx="7" ry="2.8"></ellipse></g>
<g stroke="#A16207" stroke-width="1.6" stroke-linecap="round"><path d="M138 50 H160 M136 56 H161 M136 62 H161 M136 68 H161 M138 74 H160"></path></g>
</svg>
<span style="font-size: 12px; font-weight: 600; color: #713F12; white-space: nowrap">Head: VHF + UHF</span>
</div>
<div style="display: flex; flex-direction: column; align-items: center; gap: 2px">
<svg width="42" height="88" viewBox="0 0 46 96" aria-hidden="true" style="display: block">
<rect x="0" y="34" width="4" height="22" rx="2" fill="#6B7280"></rect>
<rect x="3" y="2" width="40" height="92" rx="14" fill="#FACC15" stroke="#A16207" stroke-width="1.2"></rect>
<rect x="9" y="9" width="28" height="23" rx="5" fill="#111827"></rect>
<rect x="12" y="12" width="22" height="17" rx="2" fill="#D9F2B4"></rect>
<g fill="#FEF3C7" stroke="#A16207" stroke-width="0.7"><ellipse cx="14" cy="38" rx="4" ry="2.4"></ellipse><ellipse cx="32" cy="38" rx="4" ry="2.4"></ellipse><ellipse cx="23" cy="41" rx="5" ry="2.6"></ellipse></g>
<g fill="#FFFFFF" stroke="#A16207" stroke-width="0.6">
<ellipse cx="14" cy="52" rx="4" ry="3"></ellipse><ellipse cx="23" cy="52" rx="4" ry="3"></ellipse><ellipse cx="32" cy="52" rx="4" ry="3"></ellipse>
<ellipse cx="14" cy="61" rx="4" ry="3"></ellipse><ellipse cx="23" cy="61" rx="4" ry="3"></ellipse><ellipse cx="32" cy="61" rx="4" ry="3"></ellipse>
<ellipse cx="14" cy="70" rx="4" ry="3"></ellipse><ellipse cx="23" cy="70" rx="4" ry="3"></ellipse><ellipse cx="32" cy="70" rx="4" ry="3"></ellipse>
<ellipse cx="14" cy="79" rx="4" ry="3"></ellipse><ellipse cx="23" cy="79" rx="4" ry="3"></ellipse><ellipse cx="32" cy="79" rx="4" ry="3"></ellipse></g>
</svg>
<span style="font-size: 12px; font-weight: 600; color: #713F12; white-space: nowrap">Handset: 2nd VHF</span>
</div>
</div>'''

vx_svg = '''<svg width="86" height="232" viewBox="0 0 100 270" aria-hidden="true" style="flex-shrink: 0; display: block">
<rect x="25" y="0" width="9" height="126" rx="4" fill="#1F2937"></rect>
<rect x="25" y="20" width="9" height="80" fill="#FACC15"></rect>
<g transform="translate(0 60)">
<rect x="42" y="38" width="15" height="24" rx="3" fill="#4B5563"></rect>
<rect x="35.5" y="53" width="6" height="8" rx="2.5" fill="#FB8C00"></rect>
<rect x="63" y="50" width="17" height="12" rx="3" fill="#374151"></rect>
<text x="49.5" y="34" text-anchor="middle" font-size="7" font-weight="700" fill="#334155">1–5</text>
<rect x="10" y="60" width="80" height="146" rx="12" fill="#1F2937"></rect>
<circle cx="79" cy="69" r="3" fill="#EF4444"></circle>
<g stroke="#4B5563" stroke-width="2" stroke-linecap="round"><path d="M24 76 H70 M24 82 H76 M24 88 H76 M24 94 H70"></path></g>
<rect x="20" y="100" width="60" height="20" rx="3" fill="#CBD5E1"></rect>
<text x="50" y="114" text-anchor="middle" font-size="11" font-weight="700" fill="#1F2937">360</text>
<g fill="#4B5563">
<rect x="20" y="127" width="12" height="9" rx="2"></rect><rect x="36" y="127" width="12" height="9" rx="2"></rect><rect x="52" y="127" width="12" height="9" rx="2"></rect><rect x="68" y="127" width="12" height="9" rx="2"></rect>
<rect x="20" y="141" width="12" height="9" rx="2"></rect><rect x="36" y="141" width="12" height="9" rx="2"></rect><rect x="52" y="141" width="12" height="9" rx="2"></rect><rect x="68" y="141" width="12" height="9" rx="2"></rect>
<rect x="20" y="155" width="12" height="9" rx="2"></rect><rect x="36" y="155" width="12" height="9" rx="2"></rect><rect x="52" y="155" width="12" height="9" rx="2"></rect><rect x="68" y="155" width="12" height="9" rx="2"></rect>
<rect x="20" y="169" width="12" height="9" rx="2"></rect><rect x="36" y="169" width="12" height="9" rx="2"></rect><rect x="52" y="169" width="12" height="9" rx="2"></rect><rect x="68" y="169" width="12" height="9" rx="2"></rect>
</g>
<g font-size="7" font-weight="700" fill="#F3F4F6" text-anchor="middle"><text x="74" y="134">A</text><text x="74" y="148">B</text><text x="74" y="162">C</text><text x="74" y="176">D</text></g>
<rect x="4" y="86" width="6" height="30" rx="2" fill="#64748B"></rect>
<rect x="4" y="122" width="6" height="11" rx="2" fill="#64748B"></rect>
<rect x="4" y="136" width="6" height="11" rx="2" fill="#64748B"></rect>
</g>
</svg>'''

tait_rows = [
 ("Change channel", f'Key the number on the handset, then {b("Select")}. Or {key("▲▼")} to scroll, then {b("Done")}.'),
 ("Swap VHF / UHF", f'{key("F3")} BAND. The large channel on the display is the radio you talk on.'),
 ("Hear both radios", f'{key("F1")} DUAL MODE once: both channels show, the one you talk on in large type. A second press transmits on both and shows {DUALTX_ICON}. Hold {key("F1")} for 3 seconds to go back to one radio.'),
 ("Talk-Around", f'{key("F4")} TALK AROUND: {TA_ICON} shows top left. {key("F4")} again, or change channel, to cancel. Only when the IC directs, or if you declare an emergency and get no reply: then ask to be relayed.'),
 ("Your location", f'If asked, describe where you are. Give GPS coordinates only if they’re requested: {b("Menu")} › {GPS_TODO}, {key("▲▼")} for latitude/longitude or Zone 50 Easting/Northing.'),
 ("Scan", f'{key("F2")} SCAN. Keep it off at incidents unless the IC directs.'),
]
vx_rows = [
 (f'{ORANGE_KEY} Key lock', 'Long press the orange button on top to lock or unlock the keys.'),
 ("Zone knob", '1 DEC/PaW 501–553 · 2 WAERN 101–353 · 3 WAERN simplex 354–369 · 4 WAERN 371–400 · 5 DEC/PaW 601–653.'),
 (f'{key("A")} Talk-Around', 'Only when the IC directs, or if you declare an emergency and get no reply: then ask to be relayed.'),
 (f'{key("B")} Power', 'Normally left as set.'),
 (f'{key("▲▼")} {key("C")} Channel', 'Side keys, or C then the three-digit channel (zones 2 to 4). Change zone first, or after an off/on it may go to an unintended channel.'),
 (f'{key("D")} Scan', 'Keep it off at incidents unless the IC directs.'),
 ("Your location", 'No GPS. Describe where you are; give coordinates only if requested.'),
 ("Light on top", 'Red: transmitting · green flash: busy · yellow flash: selcall.'),
]

def panel_head(title, sub, color, sub_color):
    return (f'<div style="display: flex; flex-direction: column; gap: 4px; min-width: 0">'
            f'<h2 style="margin: 0; {BSC}; font-weight: 700; font-size: 24px; line-height: 1.1; color: {color}">{title}</h2>'
            f'<p style="margin: 0; font-size: 14px; line-height: 1.35; color: {sub_color}">{sub}</p></div>')

tait_panel = f'''<section style="box-sizing: border-box; padding: 12px 16px 12px 16px; background: #FFF9E0; border: 1.5px solid #EED58A; border-radius: 14px; display: flex; flex-direction: column; gap: 10px">
<div style="display: flex; gap: 16px; align-items: center; justify-content: space-between">
{panel_head("Tait vehicle radio", "Every vehicle has the yellow head, which runs a VHF high-band and a UHF radio. Where a yellow handset with a display replaces the black one, it adds a second VHF: three radios in all.", "#713F12", "#374151")}
{tait_svg}
</div>
{table(tait_rows, "#854D0E")}
</section>'''

vx_panel = f'''<section style="box-sizing: border-box; padding: 12px 16px 12px 16px; background: #F2F4F7; border: 1.5px solid #CDD5DF; border-radius: 14px; display: flex; flex-direction: column; gap: 10px">
<div style="display: flex; align-items: baseline; gap: 10px"><h2 style="margin: 0; {BSC}; font-weight: 700; font-size: 24px; line-height: 1.1; color: #1E293B">Vertex VX-829 handheld</h2><span style="font-size: 14px; color: #374151">Black, VHF high band, yellow aerial.</span></div>
<div style="display: flex; gap: 14px; align-items: flex-start">
{vx_svg}
<div style="flex: 1; min-width: 0">{table(vx_rows, "#334155")}</div>
</div>
<p style="margin: 0; font-size: 14px; line-height: 1.35; color: #1F2937"><b style="font-weight: 600">Use it outdoors</b>, away from the vehicle and obstacles. Not indoors, and not for air operations or as ground controller. On 173 it may hear the repeater but not reach it.</p>
</section>'''

def tag(t, kind):
    styles = {"tait": "background: #FACC15; color: #422006", "vx": "background: #334155; color: #FFFFFF", "cb": "background: #FFFFFF; color: #422006; border: 1px solid #CA8A04"}
    return f'<span style="box-sizing: border-box; padding: 1px 7px; border-radius: 999px; font-size: 12px; font-weight: 600; line-height: 16px; white-space: nowrap; {styles[kind]}">{t}</span>'
TAIT, VX3 = tag("Tait", "tait"), tag("VX 3", "vx")
chans = [
 ("173", "Incident command", [TAIT]),
 ("360", "Initial command → Sector 1", [TAIT, VX3]),
 ("361 · 362", "Sector command", [TAIT, VX3]),
 ("358 · 359 · 367", "Extra sectors", [TAIT, VX3]),
 ("525", "Aerial suppression", [TAIT], 62),
 ("ESC 220", "Rescue helicopter", [tag("Tait UHF", "tait")], 62),
 ("CB 1–80", "Farm, graders, tankers, and talk within your crew", [tag("Tait UHF", "tait"), tag("UHF CB", "cb")], 62, 2),
]
def chan(n, role, tags, numw=100, rows=1):
    lay = "grid-row: span 2; align-items: flex-start" if rows == 2 else "align-items: center"
    return (f'<div style="display: flex; {lay}; gap: 8px; min-width: 0">'
            f'<span style="width: {numw}px; flex-shrink: 0; {BSC}; font-weight: 700; font-size: 16px; line-height: 1.2; color: #14263F">{n}</span>'
            f'<span style="flex: 1; min-width: 0; font-size: 14px; line-height: 1.25; color: #1F2937">{role}</span>'
            f'<span style="display: flex; gap: 4px; flex-shrink: 0">{"".join(tags)}</span></div>')
channels = f'''<div style="box-sizing: border-box; padding: 10px 14px 12px 14px; background: #EEF2F7; border-radius: 12px; display: flex; flex-direction: column; gap: 8px">
<div style="display: flex; align-items: baseline; gap: 10px">
<div style="{BSC}; font-weight: 700; font-size: 19px; line-height: 1.1; color: #14263F; white-space: nowrap">Denmark channels</div>
<div style="font-size: 13px; line-height: 1.3; color: #475569">{TAIT} vehicle radio · {VX3} handheld zone · {tag("UHF CB", "cb")} appliance crew</div>
</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-rows: repeat(4, auto); grid-auto-flow: column; column-gap: 24px; row-gap: 6px">
{"".join(chan(*c) for c in chans)}
</div>
</div>'''

series = '''<div style="width: 232px; flex-shrink: 0; box-sizing: border-box; padding: 10px 12px; background: #FFFFFF; border-radius: 12px; display: flex; flex-direction: column; gap: 4px">
<div style="font-size: 12px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; color: #475569">Radio User Guide</div>
<div style="display: flex; align-items: center; gap: 8px; box-sizing: border-box; padding: 2px 8px; margin: 0 -8px; background: #FDE68A; border-radius: 6px"><span style="font-family: 'Barlow Semi Condensed', 'Barlow', sans-serif; font-weight: 700; font-size: 18px; color: #14263F">1</span><span style="font-size: 15px; font-weight: 700; color: #14263F">WAERN Radios</span></div>
<div style="display: flex; align-items: center; gap: 8px; padding: 2px 0"><span style="font-family: 'Barlow Semi Condensed', 'Barlow', sans-serif; font-weight: 700; font-size: 18px; color: #64748B">2</span><span style="font-size: 15px; color: #374151">Talking on the Radio</span></div>
<div style="display: flex; align-items: center; gap: 8px; padding: 2px 0"><span style="font-family: 'Barlow Semi Condensed', 'Barlow', sans-serif; font-weight: 700; font-size: 18px; color: #64748B">3</span><span style="font-size: 15px; color: #374151">Common Radio Issues</span></div>
</div>'''

header = f'''<header style="height: 150px; flex-shrink: 0; box-sizing: border-box; padding: 22px 40px 0 40px; background: #14263F; display: flex; justify-content: space-between; align-items: flex-start; gap: 24px">
<div style="width: 458px; display: flex; flex-direction: column; gap: 6px">
<div style="font-size: 13px; font-weight: 600; letter-spacing: 1.4px; text-transform: uppercase; color: #F6C35B">Denmark Bushfire Brigades WAERN Radio Use</div>
<h1 style="margin: 0; {BSC}; font-weight: 700; font-size: 46px; line-height: 1; color: #FFFFFF">WAERN Radios</h1>
<p style="margin: 4px 0 0 0; font-size: 17px; font-weight: 500; line-height: 1.3; color: #D6E2F0">Channels, Talk-Around and your position.</p>
</div>
{series}
</header>'''

footer = '''<footer style="flex-shrink: 0; box-sizing: border-box; padding: 10px 40px 40px 40px; display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; font-size: 12px; line-height: 1.3; color: #5B6472">
<span style="flex: 1; min-width: 0">Sources: DFES aide-memoires and channel guide, Shire of Denmark preformed plan. Tait keys as reprogrammed.</span>
<span style="flex-shrink: 0">v1.3 · November 2026</span>
</footer>'''

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>WAERN Radios</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&amp;family=Barlow+Semi+Condensed:wght@600;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:#0F766E}}a:hover{{color:#115E59}}
</style>
</helmet>
<div style="width: 794px; height: 1123px; box-sizing: border-box; display: flex; flex-direction: column; background: #FFFFFF; font-family: 'Barlow', Arial, sans-serif; color: #1F2937; overflow: hidden">
{header}
<main style="flex: 1; min-height: 0; box-sizing: border-box; padding: 12px 40px 0 40px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px">
{tait_panel}
{vx_panel}
{channels}
</main>
{footer}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":794,"height":1123}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{}};
  }}
}}
</script>
</body>
</html>
'''
assert "{{" not in html.split("<x-dc>")[1].split("</x-dc>")[0]
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sheets", "WAERN-Radios.dc.html"), "w").write(html)
print("written", len(html))
