import sys
WM = ('<div aria-hidden="true" data-watermark="draft" style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; pointer-events: none; z-index: 10; overflow: hidden">'
      '<span style="transform: rotate(-35deg); font-family: \'Barlow Semi Condensed\', \'Barlow\', sans-serif; font-weight: 700; font-size: 230px; letter-spacing: 16px; color: rgba(185, 28, 28, 0.13); white-space: nowrap">DRAFT</span></div>')
for p in sys.argv[1:]:
    s = open(p).read()
    if 'data-watermark="draft"' in s: continue
    root = '<div style="width: 794px; height: 1123px; box-sizing: border-box;'
    assert s.count(root) == 1, p
    s = s.replace(root, '<div style="position: relative; width: 794px; height: 1123px; box-sizing: border-box;')
    end = '</div>\n</x-dc>'
    assert s.count(end) == 1, p
    s = s.replace(end, WM + '\n</div>\n</x-dc>')
    open(p, 'w').write(s); print('watermarked', p)
