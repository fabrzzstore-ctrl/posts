"""Ilustrações originais em SVG (traço fino, estilo editorial) por tema.
Cada função recebe a cor de destaque (cor do nível) e devolve o conteúdo SVG (viewBox 0 0 904 460)."""

L = '#e6e9ee'   # traço principal
D = '#3a4150'   # traço secundário


def _svg(body):
    return (f'<svg viewBox="0 0 904 460" xmlns="http://www.w3.org/2000/svg" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


def cripto(c):
    coins = ''.join(f'<ellipse cx="300" cy="{330-i*34}" rx="130" ry="34" stroke="{L}" stroke-width="5" fill="#0e1116"/>'
                    for i in range(5))
    top = f'<ellipse cx="300" cy="160" rx="130" ry="34" stroke="{L}" stroke-width="5" fill="#0e1116"/><ellipse cx="300" cy="160" rx="80" ry="18" stroke="{D}" stroke-width="4"/>'
    arrows = ''
    for k, (y, x2) in enumerate([(120, 760), (200, 800), (280, 740)]):
        arrows += (f'<path d="M450 {y} C 560 {y-40}, 640 {y+30}, {x2} {y-10}" stroke="{c}" stroke-width="5" stroke-dasharray="14 12"/>'
                   f'<circle cx="{x2+28}" cy="{y-12}" r="24" stroke="{c}" stroke-width="5"/>')
    return _svg(coins + top + arrows)


def firewall(c):
    bricks = ''
    for r in range(6):
        off = 0 if r % 2 == 0 else 60
        for k in range(-1, 6):
            x = 250 + k * 120 + off
            if 250 <= x <= 650:
                bricks += f'<rect x="{x}" y="{80+r*52}" width="110" height="42" stroke="{L}" stroke-width="4"/>'
    bolt = f'<path d="M150 40 L110 200 L170 200 L120 380" stroke="{c}" stroke-width="7"/>'
    crack = f'<path d="M250 140 L300 190 L280 230 L340 280" stroke="{c}" stroke-width="5"/>'
    return _svg(bricks + bolt + crack)


def vpn(c):
    shield = f'<path d="M452 60 L600 110 V230 C600 320 530 380 452 410 C374 380 304 320 304 230 V110 Z" stroke="{L}" stroke-width="6"/>'
    lock = (f'<rect x="402" y="220" width="100" height="80" rx="8" stroke="{L}" stroke-width="5"/>'
            f'<path d="M422 220 V190 C422 160 482 160 482 190 V220" stroke="{L}" stroke-width="5"/>')
    bypass = (f'<path d="M120 380 C 160 120, 260 40, 452 30 C 650 40, 760 140, 790 380" stroke="{c}" stroke-width="6" stroke-dasharray="18 14"/>'
              f'<path d="M770 350 L790 385 L815 352" stroke="{c}" stroke-width="6"/>')
    return _svg(shield + lock + bypass)


def cadeia(c):
    win = (f'<rect x="150" y="60" width="600" height="340" rx="14" stroke="{L}" stroke-width="5"/>'
           f'<line x1="150" y1="110" x2="750" y2="110" stroke="{L}" stroke-width="4"/>'
           + ''.join(f'<circle cx="{185+i*30}" cy="85" r="8" stroke="{D}" stroke-width="4"/>' for i in range(3)))
    lines = ''
    for i, w in enumerate([300, 420, 260, 380, 330]):
        col = c if i == 2 else D
        sw = 10
        lines += f'<line x1="200" y1="{160+i*45}" x2="{200+w}" y2="{160+i*45}" stroke="{col}" stroke-width="{sw}"/>'
    hook = f'<path d="M560 250 h120" stroke="{c}" stroke-width="5" stroke-dasharray="10 10"/><circle cx="700" cy="250" r="18" stroke="{c}" stroke-width="5"/>'
    return _svg(win + lines + hook)


def fuga_dados(c):
    db = ''
    for i in range(3):
        y = 90 + i * 70
        db += f'<path d="M260 {y} v70" stroke="{L}" stroke-width="5"/><path d="M500 {y} v70" stroke="{L}" stroke-width="5"/>'
        db += f'<path d="M260 {y+70} C260 {y+110} 500 {y+110} 500 {y+70}" stroke="{L}" stroke-width="5"/>'
    db += f'<ellipse cx="380" cy="90" rx="120" ry="38" stroke="{L}" stroke-width="5"/>'
    leak = ''
    for k, (x, y) in enumerate([(560, 170), (630, 220), (700, 160), (660, 300), (760, 250), (590, 330)]):
        leak += f'<rect x="{x}" y="{y}" width="44" height="30" rx="4" stroke="{c}" stroke-width="5" transform="rotate({(k*17)%40-20} {x+22} {y+15})"/>'
    crack = f'<path d="M500 180 L530 200 L515 225 L545 245" stroke="{c}" stroke-width="5"/>'
    return _svg(db + leak + crack)


def conta(c):
    card = (f'<rect x="200" y="70" width="500" height="320" rx="18" stroke="{L}" stroke-width="5"/>'
            f'<circle cx="300" cy="170" r="45" stroke="{L}" stroke-width="5"/>'
            f'<path d="M235 270 C250 225 350 225 365 270" stroke="{L}" stroke-width="5"/>'
            f'<line x1="410" y1="150" x2="640" y2="150" stroke="{D}" stroke-width="10"/>'
            f'<line x1="410" y1="195" x2="580" y2="195" stroke="{D}" stroke-width="10"/>'
            f'<rect x="410" y="250" width="230" height="60" rx="8" stroke="{c}" stroke-width="5"/>'
            + ''.join(f'<circle cx="{445+i*40}" cy="280" r="9" fill="{c}" stroke="none"/>' for i in range(5)))
    key = (f'<circle cx="770" cy="110" r="34" stroke="{c}" stroke-width="5"/>'
           f'<path d="M745 135 L680 200 M700 180 l18 18 M690 190 l14 14" stroke="{c}" stroke-width="5"/>')
    return _svg(card + key)


def grafico(c):
    axis = f'<path d="M160 60 V400 H760" stroke="{L}" stroke-width="5"/>'
    bars = ''
    for i, h in enumerate([90, 130, 120, 180, 230, 310]):
        col = c if i == 5 else L
        bars += f'<rect x="{200+i*92}" y="{400-h}" width="60" height="{h}" stroke="{col}" stroke-width="5"/>'
    trend = f'<path d="M230 300 L322 260 L414 270 L506 210 L598 160 L690 70" stroke="{c}" stroke-width="5" stroke-dasharray="12 10"/>'
    return _svg(axis + bars + trend)


def portatil(c):
    lap = (f'<rect x="230" y="60" width="440" height="280" rx="16" stroke="{L}" stroke-width="5"/>'
           f'<rect x="255" y="85" width="390" height="230" rx="6" stroke="{D}" stroke-width="4"/>'
           f'<path d="M170 360 H730 L700 400 H200 Z" stroke="{L}" stroke-width="5"/>'
           f'<rect x="420" y="76" width="60" height="14" rx="7" fill="{L}" stroke="none"/>')
    touch = ''.join(f'<circle cx="520" cy="210" r="{r}" stroke="{c}" stroke-width="{w}" opacity="{o}"/>'
                    for r, w, o in [(16, 6, 1), (40, 4, .7), (66, 3, .4)])
    return _svg(lap + touch)


def cloud(c):
    cl = f'<path d="M260 330 C170 330 170 210 260 210 C270 120 400 100 440 170 C480 110 610 130 610 220 C690 220 700 330 620 330 Z" stroke="{L}" stroke-width="6"/>'
    chip = (f'<rect x="395" y="225" width="90" height="70" rx="8" stroke="{c}" stroke-width="5"/>'
            + ''.join(f'<line x1="{410+i*20}" y1="215" x2="{410+i*20}" y2="225" stroke="{c}" stroke-width="4"/>'
                      f'<line x1="{410+i*20}" y1="295" x2="{410+i*20}" y2="305" stroke="{c}" stroke-width="4"/>' for i in range(4)))
    up = f'<path d="M720 380 L720 110 M690 145 L720 110 L750 145" stroke="{c}" stroke-width="6"/>'
    return _svg(cl + chip + up)


def phishing(c):
    env = (f'<rect x="200" y="140" width="400" height="250" rx="12" stroke="{L}" stroke-width="5"/>'
           f'<path d="M200 150 L400 280 L600 150" stroke="{L}" stroke-width="5"/>')
    hook = f'<path d="M680 40 V250 C680 310 600 310 600 260 L620 280" stroke="{c}" stroke-width="7"/>'
    return _svg(env + hook)


def telemovel(c):
    ph = (f'<rect x="340" y="40" width="220" height="390" rx="30" stroke="{L}" stroke-width="5"/>'
          f'<line x1="420" y1="70" x2="480" y2="70" stroke="{L}" stroke-width="5"/>'
          f'<rect x="370" y="100" width="160" height="70" rx="10" stroke="{c}" stroke-width="5"/>'
          f'<line x1="390" y1="125" x2="500" y2="125" stroke="{c}" stroke-width="6"/>'
          f'<line x1="390" y1="148" x2="460" y2="148" stroke="{c}" stroke-width="6"/>'
          + ''.join(f'<line x1="370" y1="{210+i*40}" x2="{530 - (i%2)*50}" y2="{210+i*40}" stroke="{D}" stroke-width="10"/>' for i in range(4)))
    return _svg(ph)


def ia(c):
    nodes = [(250, 120), (250, 230), (250, 340), (450, 90), (450, 230), (450, 370), (650, 160), (650, 300)]
    edges = ''
    for a in nodes[:3]:
        for b in nodes[3:6]:
            edges += f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{D}" stroke-width="3"/>'
    for a in nodes[3:6]:
        for b in nodes[6:]:
            edges += f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{D}" stroke-width="3"/>'
    circ = ''.join(f'<circle cx="{x}" cy="{y}" r="24" stroke="{c if i in (4, 7) else L}" stroke-width="5" fill="#151922"/>'
                   for i, (x, y) in enumerate(nodes))
    return _svg(edges + circ)


def escudo(c):
    sh = f'<path d="M452 40 L630 100 V230 C630 330 550 400 452 430 C354 400 274 330 274 230 V100 Z" stroke="{L}" stroke-width="6"/>'
    tick = f'<path d="M380 235 L435 290 L535 180" stroke="{c}" stroke-width="8"/>'
    return _svg(sh + tick)


def gaming(c):
    pad = (f'<path d="M300 130 H604 C680 130 720 190 740 290 C755 370 715 410 670 390 C630 372 610 330 570 320 H334 C294 330 274 372 234 390 C189 410 149 370 164 290 C184 190 224 130 300 130 Z" stroke="{L}" stroke-width="6"/>'
           f'<path d="M300 200 V280 M260 240 H340" stroke="{L}" stroke-width="10"/>'
           + ''.join(f'<circle cx="{x}" cy="{y}" r="16" stroke="{c}" stroke-width="5"/>' for x, y in [(604, 200), (644, 240), (604, 280), (564, 240)])
           + f'<line x1="420" y1="215" x2="450" y2="215" stroke="{D}" stroke-width="8"/><line x1="460" y1="215" x2="490" y2="215" stroke="{D}" stroke-width="8"/>')
    sig = ''.join(f'<path d="M{452-r} {95-r*0.35} Q452 {95-r*0.9} {452+r} {95-r*0.35}" stroke="{c}" stroke-width="5" opacity="{o}"/>'
                  for r, o in [(30, 1), (60, .7), (90, .4)])
    return _svg(pad + sig)


TEMAS = {
    "cripto": cripto, "firewall": firewall, "vpn": vpn, "cadeia": cadeia,
    "fuga-dados": fuga_dados, "conta": conta, "grafico": grafico, "portatil": portatil,
    "cloud": cloud, "phishing": phishing, "telemovel": telemovel, "ia": ia, "escudo": escudo, "gaming": gaming,
}


def svg(tema, cor):
    return TEMAS.get(tema, escudo)(cor)
