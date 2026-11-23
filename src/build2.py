import os
BSC = "font-family: 'Barlow Semi Condensed', 'Barlow', sans-serif"
WIKI = "https://en.wikipedia.org/wiki/Procedure_word#ACP_125(F)"
def b(t): return f'<b style="font-weight: 600">{t}</b>'
def badge(n, color, size=22, fs=13):
    return (f'<div style="width: {size}px; height: {size}px; flex-shrink: 0; border-radius: 50%; background: {color}; color: #FFFFFF; display: flex; '
            f'align-items: center; justify-content: center; {BSC}; font-weight: 700; font-size: {fs}px; line-height: 1">{n}</div>')
def h2(t, color): return f'<h2 style="margin: 0; {BSC}; font-weight: 700; font-size: 24px; line-height: 1.1; color: {color}">{t}</h2>'
def panel(bg, bd, inner, pad="10px 16px"):
    return f'<section style="box-sizing: border-box; padding: {pad}; background: {bg}; border: 1.5px solid {bd}; border-radius: 14px; display: flex; flex-direction: column; gap: 8px">{inner}</section>'

# 1. Making a call
steps = [("Listen first.", "Wait until the channel is clear and you’ve heard OUT."),
         ("Press PTT, wait one second,", "then talk."),
         ("Call them,", "then say THIS IS and your call sign.")]
steps_html = "".join(f'<div style="display: flex; gap: 8px; align-items: flex-start">{badge(i+1, "#1D4ED8")}<p style="margin: 0; font-size: 15px; line-height: 1.3; color: #1F2937">{b(s)} {r}</p></div>' for i, (s, r) in enumerate(steps))
def word_box(word, text, color):
    return (f'<div style="display: flex; gap: 10px; align-items: center; box-sizing: border-box; padding: 6px 10px; background: #FFFFFF; border: 1.5px solid {color}; border-radius: 10px">'
            f'<a href="{WIKI}" style="width: 52px; flex-shrink: 0; {BSC}; font-weight: 700; font-size: 22px; line-height: 1; color: {color}; text-decoration: none">{word}</a>'
            f'<span style="font-size: 14px; line-height: 1.3; color: #1F2937">{text}</span></div>')
over_out = (word_box("OVER", "My turn is finished. A reply is needed.", "#1D4ED8")
            + word_box("OUT", "Finished, no reply. Only one says it.", "#1E3A8A"))
dialogue = [("You", "Denmark Chief, this is Shadforth Light Tanker, over.", False), ("Denmark Chief", "Shadforth Light Tanker, this is Denmark Chief, go ahead, over.", True),
            ("You", "Arrived on scene, two crew, starting on the north flank, over.", False), ("Denmark Chief", "Roger, out.", True)]
def line(who, text, ctl):
    bg = "#FFFFFF" if not ctl else "#E0E7FF"
    return (f'<div style="display: grid; grid-template-columns: 66px minmax(0, 1fr); column-gap: 6px; align-items: baseline">'
            f'<span style="font-size: 12px; font-weight: 700; line-height: 1.2; letter-spacing: 0.8px; text-transform: uppercase; color: #475569">{who}</span>'
            f'<span style="box-sizing: border-box; padding: 2px 8px; background: {bg}; border-radius: 8px; font-size: 14px; font-weight: 500; line-height: 1.3; color: #1F2937">“{text}”</span></div>')
dialogue_html = "".join(line(*d) for d in dialogue)
callsigns = ('<p style="margin: 0; font-size: 14px; line-height: 1.35; color: #1F2937">'
             '<b style="font-size: 12.5px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; color: #1D4ED8; margin-right: 8px">Call signs</b>'
             'DFES lists when they’re needed: your first call, a station joining or leaving, changing channel, closing down, difficult conditions and multi-agency incidents. Otherwise they can be left out, as in the example.</p>')
call_panel = panel("#EEF4FF", "#C7D7FE",
    h2("Making a call", "#1E3A8A")
    + f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 18px">'
    + f'<div style="display: flex; flex-direction: column; gap: 6px">{steps_html}{over_out}</div>'
    + f'<div style="display: flex; flex-direction: column; gap: 5px">{dialogue_html}</div>'
    + '</div>'
    + callsigns)

# 1b. Emergency message (DFES SOP 3.2.4 and SOP 3.5.11)
em_panel = panel("#FEF2F2", "#FCA5A5",
    '<div style="display: flex; gap: 14px; align-items: baseline">' + h2("Emergency message", "#991B1B").replace('<h2 style="margin: 0;', '<h2 style="margin: 0; flex-shrink: 0; white-space: nowrap;')
    + '<span style="flex: 1; min-width: 0; font-size: 14px; line-height: 1.3; color: #7F1D1D">Extreme emergency only. Everyone else stops transmitting and listens.</span></div>'
    + '<div style="box-sizing: border-box; padding: 6px 10px; background: #FFFFFF; border: 1.5px solid #B91C1C; border-radius: 10px; font-size: 14px; font-weight: 500; line-height: 1.35; color: #1F2937">'
      '“<b style="font-weight: 700; color: #B91C1C">EMERGENCY EMERGENCY EMERGENCY</b>, Denmark Chief, this is Firefighter Smith, Shadforth Light Tanker. Two crew, burnover, sheltering in the appliance at the junction of Turner Rd and Shadforth Rd. Over.”'
      '<span style="display: block; margin-top: 2px; font-size: 12.5px; font-weight: 400; color: #7F1D1D">Name and rank, appliance, crew, SITREP, location. On your sector or control channel*.</span></div>'
    + '<p style="margin: 0; font-size: 14px; line-height: 1.3; color: #1F2937">' + b("AVL:") + ' also hold the Distress Button 4 seconds. ' + b("*No reply:") + ' Talk-Around, ask for a relay.</p>')

# 2. Moving off the command channel
def pwl(t): return '<a href="' + WIKI + '" style="color: inherit; text-decoration: none">' + t + '</a>'
moves = [("“" + pwl("CHANGE TO") + " 360, OVER.”", "Get ready."),
         ("“" + pwl("WILCO") + ", OVER.”", "Or say if you can’t."),
         ("“" + pwl("CHANGE NOW") + ", OUT.”", "Go to 360."),
         ("Radio check on 360", "straight away.")]
move_cells = "".join(f'<div style="display: flex; gap: 6px; align-items: flex-start; box-sizing: border-box; padding: 8px 8px; background: #FFFFFF; border: 1px solid #B5DED5; border-radius: 10px">{badge(i+1, "#0F766E")}<p style="margin: 0; font-size: 14px; line-height: 1.3; color: #1F2937">{b(s)} {r}</p></div>' for i, (s, r) in enumerate(moves))
move_panel = panel("#EAF6F3", "#B5DED5",
    '<div style="display: flex; gap: 18px; align-items: center">' + h2("Moving off the command channel", "#0B5B54")
    + '<p style="margin: 0; flex: 1; min-width: 0; font-size: 14px; line-height: 1.3; color: #134E4A">Keep 173 for command. Crews work on 360, then 361, 362.</p></div>'
    + f'<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px">{move_cells}</div>')

# 3. Prowords
pw = [("WAIT", "Short pause. Others don’t transmit."), ("WAIT OUT", "Long pause. Others may transmit."), ("ROGER", "Message understood. Not a “yes”."), ("WILCO", "Understood, will comply."), ("SAY AGAIN", "Repeat your last message."), ("CORRECTION", "Error. The right version follows."), 
      ("GO AHEAD", "Send your message."), ("SITREP", "What is your situation?")]
pw_cells = "".join(f'<a href="{WIKI}" style="{BSC}; font-weight: 700; font-size: 16px; line-height: 1.3; color: #14263F; text-decoration: none">{p}</a>'
                   f'<span style="font-size: 14px; line-height: 1.3; color: #1F2937">{m}</span>' for p, m in pw)
pw_panel = panel("#F2F4F7", "#CDD5DF",
    '<div style="display: flex; gap: 14px; align-items: baseline">' + h2("Common prowords", "#1E293B")
    + '</div>'
    + f'<div style="display: grid; grid-template-columns: 108px minmax(0, 1fr) 108px minmax(0, 1fr); column-gap: 10px; row-gap: 0px; align-items: baseline">{pw_cells}</div>')

# 4. Phonetic alphabet
letters = "Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu".split()
let_cells = "".join(f'<div style="font-size: 15px; line-height: 1.25; color: #1F2937; white-space: nowrap"><b style="{BSC}; font-weight: 700; color: #B45309; display: inline-block; width: 16px">{w[0]}</b> {w}</div>' for w in letters)
figs = [("0", "zero"), ("1", "wun"), ("2", "too"), ("3", "thuh-ree"), ("4", "fow-wer"), ("5", "fi-yiv"), ("6", "six"), ("7", "se-ven"), ("8", "ate"), ("9", "niner")]
fig_cells = '<span style="color: #B45309">·</span>'.join(f'<span style="font-size: 14px; line-height: 1.3; color: #1F2937; white-space: nowrap"><b style="{BSC}; font-weight: 700; color: #B45309">{n}</b> {w}</span>' for n, w in figs)
ph_panel = panel("#FFF5EA", "#F2C9A0",
    '<div style="display: flex; gap: 14px; align-items: baseline">' + h2("Phonetic alphabet", "#8A3D07").replace('<h2 style="margin: 0;', '<h2 style="margin: 0; flex-shrink: 0; white-space: nowrap;')
    + '<span style="flex: 1; min-width: 0; font-size: 13px; line-height: 1.35; color: #6B3A0A">Only in poor conditions, for hard-to-catch words, and for critical details such as Forest Grid references. To spell a word, say it, then I SPELL.</span></div>'
    + f'<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); column-gap: 8px; row-gap: 0px">{let_cells}</div>'
    + f'<div style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px"><span style="font-size: 12.5px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; color: #A14A08; margin-right: 2px">Figures</span>{fig_cells}</div>')

series_items = [("1", "WAERN Radios"), ("2", "Talking on the Radio"), ("3", "Common Radio Issues")]
def series(current):
    rows = []
    for n, t in series_items:
        if n == current:
            rows.append(f'<div style="display: flex; align-items: center; gap: 8px; box-sizing: border-box; padding: 2px 8px; margin: 0 -8px; background: #FDE68A; border-radius: 6px"><span style="{BSC}; font-weight: 700; font-size: 18px; color: #14263F">{n}</span><span style="font-size: 15px; font-weight: 700; color: #14263F">{t}</span></div>')
        else:
            rows.append(f'<div style="display: flex; align-items: center; gap: 8px; padding: 2px 0"><span style="{BSC}; font-weight: 700; font-size: 18px; color: #64748B">{n}</span><span style="font-size: 15px; color: #374151">{t}</span></div>')
    return ('<div style="width: 232px; flex-shrink: 0; box-sizing: border-box; padding: 10px 12px; background: #FFFFFF; border-radius: 12px; display: flex; flex-direction: column; gap: 4px">'
            '<div style="font-size: 12px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; color: #475569">Radio User Guide</div>' + "".join(rows) + '</div>')

header = f'''<header style="height: 150px; flex-shrink: 0; box-sizing: border-box; padding: 22px 40px 0 40px; background: #14263F; display: flex; justify-content: space-between; align-items: flex-start; gap: 24px">
<div style="width: 458px; display: flex; flex-direction: column; gap: 6px">
<div style="font-size: 13px; font-weight: 600; letter-spacing: 1.4px; text-transform: uppercase; color: #F6C35B">Denmark Bushfire Brigades WAERN Radio Use</div>
<h1 style="margin: 0; {BSC}; font-weight: 700; font-size: 46px; line-height: 1; color: #FFFFFF">Talking on the Radio</h1>
<p style="margin: 4px 0 0 0; font-size: 17px; font-weight: 500; line-height: 1.3; color: #D6E2F0">Call signs, prowords and the phonetic alphabet.</p>
</div>
{series("2")}
</header>'''
footer = '''<footer style="flex-shrink: 0; box-sizing: border-box; padding: 8px 40px 40px 40px; display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; font-size: 12px; line-height: 1.3; color: #5B6472">
<span style="flex: 1; min-width: 0">Sources: DFES Voice Procedures aide-memoire, SOP 3.2.4 and SOP 3.5.11; Field Radio Operator manual; ACP 125(G).</span>
<span style="flex-shrink: 0">v1.3 · November 2026</span>
</footer>'''
html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Talking on the Radio</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&amp;family=Barlow+Semi+Condensed:wght@600;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:#14263F}}a:hover{{color:#1D4ED8}}
</style>
</helmet>
<div style="width: 794px; height: 1123px; box-sizing: border-box; display: flex; flex-direction: column; background: #FFFFFF; font-family: 'Barlow', Arial, sans-serif; color: #1F2937; overflow: hidden">
{header}
<main style="flex: 1; min-height: 0; box-sizing: border-box; padding: 12px 40px 0 40px; display: flex; flex-direction: column; justify-content: space-between; gap: 5px">
{call_panel}
{move_panel}
{pw_panel}
{ph_panel}
{em_panel}
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
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sheets", "Talking-on-the-Radio.dc.html"), "w").write(html)
print("written", len(html))
