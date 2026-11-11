"""Prévia de conceitos de cardápio · preto e verde · Speciale (A4 paisagem)."""
import math

G = '#2f8a4e'      # verde manjericão
G2 = '#9fd18b'     # verde claro
BK = '#111312'     # preto
OW = '#f4f1ea'     # off-white
PR = 'R$ __'

SABORES = [
    ('Portuguesa', 'Molho de tomate artesanal, muçarela, presunto, ovo cozido, cebola, azeitona preta e orégano.', 'port-foto6'),
    ('4 Queijos', 'Muçarela, gorgonzola, provolone ralado, catupiry e orégano.', 'q4-foto3'),
    ('Frango com Catupiry', 'Frango desfiado, muçarela, catupiry, azeitona preta e orégano.', 'frango-foto1'),
    ('Lombinho', 'Lombo fatiado, muçarela, catupiry, azeitona preta e orégano.', 'lombo-foto2'),
]

CSS = f'''<style>
@import url('fonts.css');
@page{{size:A4 landscape;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Poppins',sans-serif;color:#1d1f1e;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:297mm;height:210mm;position:relative;overflow:hidden;page-break-after:always;background:#eceae4}}
.page:last-child{{page-break-after:auto}}
.C{{font-family:'Roboto Condensed',sans-serif;font-weight:800}}
.hd{{position:absolute;left:14mm;top:10mm;right:14mm;display:flex;justify-content:space-between;align-items:flex-end}}
.hd .k{{font-size:7pt;letter-spacing:2px;color:{G};font-weight:700;text-transform:uppercase}}
.hd h2{{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:22pt;text-transform:uppercase;line-height:1}}
.hd p{{font-size:8pt;color:#555;max-width:118mm;text-align:right}}
.ft{{position:absolute;left:14mm;right:14mm;bottom:6mm;display:flex;justify-content:space-between;font-size:6.5pt;color:#777}}
.stage{{position:absolute;left:14mm;right:14mm;top:31mm;bottom:13mm}}
.chip{{display:inline-block;background:{G};color:#fff;font-size:6.5pt;font-weight:700;padding:1px 7px;border-radius:3px;letter-spacing:.5px;text-transform:uppercase}}
.shadow{{box-shadow:0 6px 18px rgba(0,0,0,.28)}}
.logo{{display:flex;align-items:center;gap:6px;color:#fff}}
.logo b{{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:13pt;line-height:1;display:block}}
.logo i{{font-style:normal;font-size:4.2pt;letter-spacing:2.2px;font-weight:600}}
.side{{position:absolute;right:0;top:0;width:66mm;font-size:8pt;color:#333;line-height:1.5}}
.side h4{{grid-column:1/-1;font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:11pt;text-transform:uppercase;margin:0 0 1.5mm}}
.side ul{{padding-left:4mm}}.side li{{margin:1mm 0}}.side li::marker{{color:{G}}}
.side .box{{background:#fff;border-left:3px solid {G};padding:3mm 4mm;margin-top:3mm;border-radius:0 5px 5px 0}}
</style>'''

LOGO_SVG = ('<svg width="{w}" height="{h}" viewBox="0 0 46 34"><ellipse cx="9" cy="15" rx="8.5" ry="7" fill="#fff"/>'
            '<ellipse cx="18" cy="27" rx="8" ry="6.5" fill="#fff"/><path d="M18 13 C21 4 33 1 45 2 C42 10 31 15 18 13Z" fill="' + G + '"/></svg>')


def logo(w=30, h=22):
    return f'<div class="logo">{LOGO_SVG.format(w=w, h=h)}<div><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i></div></div>'


def page(n, kicker, title, note, body):
    return (f'<section class="page"><div class="hd"><div><div class="k">{kicker}</div><h2>{title}</h2></div><p>{note}</p></div>'
            f'<div class="stage">{body}</div><div class="ft"><span>Speciale Pizzas Artesanais · Prévia de cardápio · preto e verde · conceitos para aprovação</span><span>{n} / 6</span></div></section>')


def side(title, items, box):
    return f'<div class="side"><h4>{title}</h4><ul>' + ''.join(f'<li>{x}</li>' for x in items) + f'</ul><div class="box">{box}</div></div>'


# ---------- linha de ilustração (pizza em traço) ----------
def pizza_line(cx, cy, r, stroke=G2, sw=0.6):
    s = f'<g fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round">'
    s += f'<circle cx="{cx}" cy="{cy}" r="{r}"/><circle cx="{cx}" cy="{cy}" r="{r * .86}"/>'
    for k in range(8):
        a = math.radians(k * 45 + 10)
        s += f'<line x1="{cx}" y1="{cy}" x2="{cx + r * .86 * math.cos(a):.2f}" y2="{cy + r * .86 * math.sin(a):.2f}"/>'
    for k, (rr, ang) in enumerate([(.45, 30), (.62, 95), (.5, 160), (.65, 215), (.42, 280), (.66, 330), (.22, 120), (.25, 250)]):
        a = math.radians(ang)
        x, y = cx + r * rr * math.cos(a), cy + r * rr * math.sin(a)
        s += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r * .1:.2f}"/><circle cx="{x:.2f}" cy="{y:.2f}" r="{r * .035:.2f}"/>'
    for ang in (60, 190, 300):
        a = math.radians(ang)
        x, y = cx + r * .72 * math.cos(a), cy + r * .72 * math.sin(a)
        s += f'<path d="M{x:.2f},{y:.2f} q{r * .08:.2f},-{r * .12:.2f} {r * .16:.2f},0 q-{r * .08:.2f},{r * .12:.2f} -{r * .16:.2f},0z"/>'
    return s + '</g>'


def leaf(x, y, s=1, c=G2):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{c}" stroke-width=".6">'
            f'<path d="M0,0 C6,-10 18,-12 26,-10 C22,-2 12,4 0,0Z"/><path d="M0,0 L22,-8"/>'
            f'<path d="M7,-3 L9,-7 M12,-4 L15,-9 M17,-6 L19,-9"/></g>')


# ---------- capa ----------
cover = f'''<section class="page" style="background:{BK};color:#fff">
<svg style="position:absolute;right:-30mm;top:-20mm" width="190mm" height="190mm" viewBox="0 0 190 190">{pizza_line(95, 95, 88, '#2b4a36', .7)}</svg>
<div style="position:absolute;left:18mm;top:18mm">{logo(44, 32)}</div>
<div style="position:absolute;left:18mm;top:62mm;max-width:150mm">
<div style="font-size:8pt;letter-spacing:3px;color:{G2};font-weight:700">PRÉVIA · PARA APROVAÇÃO</div>
<div class="C" style="font-size:46pt;line-height:.92;text-transform:uppercase;margin-top:3mm">Novo cardápio<br><span style="color:{G2}">em preto e verde</span></div>
<p style="font-size:11pt;color:#d9dcd6;margin-top:6mm;line-height:1.5">Quatro formatos para a Speciale escolher: um para a mesa, um para surpreender, um para o delivery e um para a tela do balcão.</p></div>
<div style="position:absolute;left:18mm;bottom:18mm;display:flex;gap:3mm;align-items:flex-end">
''' + ''.join(f'<div style="width:22mm"><div style="height:14mm;border-radius:4px;background:{c};border:1px solid #333"></div><div style="font-size:6.5pt;color:#bbb;margin-top:1mm">{n}<br>{c.upper()}</div></div>' for c, n in [(BK, 'Preto carvão'), (G, 'Verde manjericão'), (G2, 'Verde folha'), (OW, 'Off-white')]) + '''</div>
<div style="position:absolute;right:18mm;bottom:18mm;font-size:7.5pt;color:#aaa;text-align:right">Conteúdo real da casa (sabores e tamanhos das fichas técnicas)<br>Preços em branco: a definir pela Speciale</div>
</section>'''


# ---------- conceito 1: leque fatia ----------
def fan_svg():
    W, H = 200, 118
    cx, cy, R = 100, 112, 100
    wedges = [
        ('Pizzas', SABORES[0][0], SABORES[0][1], BK),
        ('Pizzas', SABORES[1][0], SABORES[1][1], G),
        ('Pizzas', SABORES[2][0], SABORES[2][1], BK),
        ('Pizzas', SABORES[3][0], SABORES[3][1], G),
        ('Tamanhos', 'Broto · Média · Grande', '4, 5 ou 8 fatias.<br>Broto ' + PR + '<br>Média ' + PR + '<br>Grande ' + PR, BK),
        ('Bebidas', 'A definir', 'Itens e preços a confirmar com a casa.', G),
    ]
    n = len(wedges)
    span = 180 / n
    s = f'<svg width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" style="overflow:visible">'
    s += f'<defs><clipPath id="cc"><circle cx="{cx}" cy="{cy}" r="22"/></clipPath></defs>'
    for i, (cat, t, d, col) in enumerate(wedges):
        a1, a2 = -90 + i * span, -90 + (i + 1) * span
        p1 = (cx + R * math.sin(math.radians(a1)), cy - R * math.cos(math.radians(a1)))
        p2 = (cx + R * math.sin(math.radians(a2)), cy - R * math.cos(math.radians(a2)))
        s += f'<path d="M{cx},{cy} L{p1[0]:.2f},{p1[1]:.2f} A{R},{R} 0 0 1 {p2[0]:.2f},{p2[1]:.2f} Z" fill="{col}" stroke="#0b0c0b" stroke-width=".3"/>'
        mid = (a1 + a2) / 2
        tc = '#fff'
        s += (f'<g transform="rotate({mid:.2f} {cx} {cy})"><foreignObject x="{cx - 24}" y="{cy - R + 5}" width="48" height="66">'
              f'<div xmlns="http://www.w3.org/1999/xhtml" style="color:{tc};text-align:center;font-family:Poppins;line-height:1.25">'
              f'<div style="font-size:2.6px;letter-spacing:.5px;color:{G2 if col == BK else "#dff0d6"};font-weight:700;text-transform:uppercase">{cat}</div>'
              f'<div style="font-family:Roboto Condensed;font-weight:800;font-size:4.4px;text-transform:uppercase;margin:.8px 0 1.2px;line-height:1">{t}</div>'
              f'<div style="font-size:2.3px;padding:0 6px">{d}</div>'
              + (f'<div style="font-size:2.3px;margin-top:1.4px;font-weight:600;padding:0 7px">B {PR}<br>M {PR}<br>G {PR}</div>' if cat == 'Pizzas' else '') +
              '</div></foreignObject></g>')
    s += f'<circle cx="{cx}" cy="{cy}" r="23.5" fill="#0b0c0b"/><image href="img/port-foto6.jpg" x="{cx - 22}" y="{cy - 22}" width="44" height="44" preserveAspectRatio="xMidYMid slice" clip-path="url(#cc)"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="2" fill="#ddd"/>'
    return s + '</svg>'


def slice_closed():
    # fatia fechada: setor de 30° visto de pé
    W, H = 64, 110
    cx, cy, R = 32, 106, 102
    a1, a2 = -15, 15
    p1 = (cx + R * math.sin(math.radians(a1)), cy - R * math.cos(math.radians(a1)))
    p2 = (cx + R * math.sin(math.radians(a2)), cy - R * math.cos(math.radians(a2)))
    return (f'<svg width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}"><path d="M{cx},{cy} L{p1[0]:.2f},{p1[1]:.2f} A{R},{R} 0 0 1 {p2[0]:.2f},{p2[1]:.2f} Z" fill="{BK}"/>'
            f'<path d="M{p1[0]:.2f},{p1[1]:.2f} A{R},{R} 0 0 1 {p2[0]:.2f},{p2[1]:.2f} L{p2[0] - 1.5:.2f},{p2[1] + 7:.2f} A{R - 7},{R - 7} 0 0 0 {p1[0] + 1.5:.2f},{p1[1] + 7:.2f}Z" fill="{G}"/>'
            f'{pizza_line(cx, 40, 9, G2, .45)}'
            f'<foreignObject x="{cx - 20}" y="54" width="40" height="30"><div xmlns="http://www.w3.org/1999/xhtml" style="color:#fff;text-align:center;font-family:Poppins">'
            f'<div style="font-family:Roboto Condensed;font-weight:800;font-size:4.6px;line-height:1">SPECIALE</div><div style="font-size:1.4px;letter-spacing:.5px;font-weight:600">PIZZAS ARTESANAIS</div>'
            f'<div style="font-size:2.3px;color:{G2};margin-top:2px;font-weight:600">FORNO A LENHA</div></div></foreignObject></svg>')


p2 = page(2, 'Conceito 1 · Delivery e mesa', 'Leque “fatia”',
          'Fechado, é uma fatia de pizza. Aberto, vira meia pizza com o cardápio inteiro. Ótimo para ir dentro da caixa no delivery.',
          f'''<div style="position:absolute;left:0;top:4mm;text-align:center"><div class="shadow" style="display:inline-block">{slice_closed()}</div><div style="font-size:7pt;color:#555;margin-top:1mm">Fechado</div></div>
<div style="position:absolute;left:76mm;top:4mm;text-align:center"><div style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.3))">{fan_svg().replace('width="200mm" height="118mm"', 'width="190mm" height="112mm"')}</div><div style="font-size:7pt;color:#555;margin-top:1mm">Aberto · cada fatia é uma seção</div></div>
''' + side('Como funciona', [
              'Fatias de papel-cartão presas por um ilhós na ponta.',
              'Uma fatia por sabor, mais tamanhos e bebidas.',
              'Foto real da pizza no centro.',
              'Cabe na caixa e o cliente guarda na geladeira.'],
              '<b>Ponto de atenção:</b> custo de corte especial na gráfica (faca e ilhós). Vale mais em tiragens maiores.').replace('class="side"', 'class="side" style="top:128mm;left:76mm;right:auto;width:190mm;display:grid;grid-template-columns:1fr 1fr;gap:0 8mm"'))


# ---------- conceito 2: tríptico quadro-negro ----------
def trifold():
    items = ''.join(f'''<div style="margin-bottom:3mm"><div class="C" style="font-size:10pt;text-transform:uppercase;color:#fff;line-height:1.1">{t}</div>
<div style="font-size:6.4pt;color:#cfd3cc;line-height:1.35">{d}</div><div style="font-size:6.4pt;color:{G2};font-weight:600;margin-top:.5mm">Broto {PR} · Média {PR} · Grande {PR}</div></div>''' for t, d, _ in SABORES)
    p_a = f'''<div style="background:{BK};padding:7mm 6mm;position:relative;overflow:hidden">
<div style="font-family:'Roboto Condensed';font-weight:800;font-size:18pt;color:{G2};font-style:italic">Pizzas</div>
<div style="font-size:6.3pt;color:#aaa;margin:1mm 0 4mm">Massa artesanal feita na casa, assada no forno a lenha.</div>{items}
<div style="font-size:6.2pt;color:#888;border-top:1px solid #333;padding-top:2mm">Mais sabores: a confirmar com a casa.</div>
<svg style="position:absolute;right:-6mm;bottom:-6mm" width="34mm" height="34mm" viewBox="0 0 34 34">{leaf(4, 26, 1, '#355f44')}</svg></div>'''
    sizes = ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px dashed #c9c4b8;padding:1.6mm 0;font-size:7.5pt"><span><b>{t}</b> · {f} fatias</span><span>{d}</span></div>'
                    for t, f, d in [('Broto', 4, '≈25 cm'), ('Média', 5, '≈28 cm'), ('Grande', 8, '≈35 cm')])
    p_b = f'''<div style="background:{OW};padding:7mm 6mm;position:relative">
<svg width="40mm" height="22mm" viewBox="0 0 40 22">{leaf(2, 18, 1.3, G)}</svg>
<div style="font-family:'Roboto Condensed';font-weight:800;font-size:16pt;color:{G};font-style:italic;margin-top:1mm">Tamanhos</div>{sizes}
<div style="font-size:6pt;color:#777;margin-top:1mm">Diâmetros estimados, em medição.</div>
<div style="font-family:'Roboto Condensed';font-weight:800;font-size:16pt;color:{G};font-style:italic;margin-top:5mm">Bebidas</div>
<div style="font-size:7pt;color:#555">Itens e preços a confirmar.</div>
<div style="font-family:'Roboto Condensed';font-weight:800;font-size:16pt;color:{G};font-style:italic;margin-top:5mm">Doces</div>
<div style="font-size:7pt;color:#555">Itens e preços a confirmar.</div></div>'''
    p_c = f'''<div style="background:{BK};position:relative;overflow:hidden">
<svg style="position:absolute;left:-10mm;top:38mm" width="110mm" height="110mm" viewBox="0 0 110 110">{pizza_line(55, 55, 50, G2, .55)}</svg>
<div style="position:absolute;left:50%;top:12mm;transform:translateX(-50%);width:44mm;height:44mm;border-radius:50%;background:{OW};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:2px solid {G}">
<div class="C" style="font-size:15pt;line-height:1;color:{BK}">SPECIALE</div><div style="font-size:4.4pt;letter-spacing:2px;font-weight:700;color:{G}">PIZZAS ARTESANAIS</div>
<div style="font-size:6pt;color:#555;margin-top:2mm;font-style:italic">assada no forno a lenha</div></div></div>'''
    return f'<div class="shadow" style="display:grid;grid-template-columns:1fr 1fr 1fr;width:192mm;height:150mm">{p_b}{p_a}{p_c}</div>'


p3 = page(3, 'Conceito 2 · Mesa', 'Tríptico “quadro-negro”',
          'Folha dobrada em três, fundo preto com ilustração em traço verde. Clássico, fácil de ler e barato de reimprimir.',
          f'<div style="position:absolute;left:0;top:2mm">{trifold()}<div style="font-size:7pt;color:#555;margin-top:2mm">Lado de fora aberto: tamanhos e bebidas · pizzas · capa</div></div>' + side('Por que funciona', [
              'Leitura rápida: nome grande, ingredientes logo abaixo e os três preços na mesma linha.',
              'A ilustração em traço dá cara artesanal sem depender de fotos.',
              'Papel couché com laminação fosca aguenta o uso na mesa.',
              'O mesmo arquivo vira PDF para WhatsApp e QR Code.'],
              '<b>Recomendado para o salão.</b> É o formato com melhor custo-benefício.'))


# ---------- conceito 3: pop-up / prove ----------
def popup():
    wins = ''.join(f'''<div style="position:relative;width:30mm"><div style="height:30mm;border-radius:4px;overflow:hidden;border:2px solid {G}"><img src="img/{f}.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div style="background:{G};color:#fff;text-align:center;font-family:'Roboto Condensed';font-weight:800;font-size:9pt;border-radius:0 0 6px 6px;padding:{'19mm' if i == 1 else '1.5mm'} 0 1.5mm;position:relative">
{'<div style="position:absolute;left:2mm;right:2mm;top:1.5mm;font-family:Poppins;font-weight:500;font-size:5.2pt;text-align:left;line-height:1.3">' + d + '</div>' if i == 1 else ''}PROVE!</div>
<div class="C" style="font-size:8pt;color:#fff;text-transform:uppercase;margin-top:1.5mm">{t}</div></div>''' for i, (t, d, f) in enumerate(SABORES))
    left = f'''<div style="background:{OW};padding:8mm 7mm"><div style="display:flex;align-items:center;gap:2mm"><div style="width:9mm;height:9mm;border-radius:50%;background:{BK}"></div><div class="C" style="font-size:12pt">SPECIALE</div></div>
<div style="font-size:6.6pt;color:#555;margin:3mm 0 5mm;line-height:1.4">Massa artesanal feita na casa e forno a lenha. Puxe a aba verde de cada sabor e descubra o que vai na pizza.</div>
<div class="C" style="font-size:11pt;color:{G};text-transform:uppercase">Tamanhos</div>
<div style="font-size:7pt;line-height:1.7">Broto · 4 fatias · {PR}<br>Média · 5 fatias · {PR}<br>Grande · 8 fatias · {PR}</div>
<div class="C" style="font-size:11pt;color:{G};text-transform:uppercase;margin-top:4mm">Meio a meio?</div><div style="font-size:7pt">Regra a confirmar com a casa.</div></div>'''
    right = f'''<div style="background:{BK};padding:7mm 7mm;position:relative">
<div style="display:flex;justify-content:center;gap:2mm;margin-bottom:5mm">''' + ''.join(f'<div style="width:20mm;height:20mm;border-radius:50%;overflow:hidden;border:2px solid {OW};transform:translateY({[0, -4, -4, 0][k]}mm) rotate({[-8, -3, 3, 8][k]}deg);box-shadow:0 4px 8px rgba(0,0,0,.5)"><img src="img/{f}.jpg" style="width:100%;height:100%;object-fit:cover"></div>' for k, (_, _, f) in enumerate(SABORES)) + f'''</div>
<div style="display:flex;align-items:center;gap:2mm;margin-bottom:4mm"><span style="background:{G};color:#fff;border-radius:50%;width:8mm;height:8mm;display:flex;align-items:center;justify-content:center" class="C">1</span><span class="C" style="color:#fff;font-size:15pt;text-transform:uppercase">Escolha sua pizza!</span></div>
<div style="display:flex;gap:3mm;align-items:flex-start">{wins}</div></div>'''
    return f'<div class="shadow" style="display:grid;grid-template-columns:52mm 1fr;width:188mm;height:148mm">{left}{right}</div>'


p4 = page(4, 'Conceito 3 · Experiência', 'Livro “Prove!” com abas',
          'Um cardápio para surpreender: as pizzas saltam da página (pop-up) e cada sabor tem uma aba verde que se puxa para ler os ingredientes.',
          f'<div style="position:absolute;left:0;top:2mm">{popup()}</div>' + side('Para quem é', [
              'Casas que querem que o cardápio vire assunto e foto nas redes.',
              'Poucos exemplares, só para as mesas.',
              'Combina com a reabertura: “o cardápio que se mexe”.'],
              '<b>Ponto de atenção:</b> é o formato mais caro e mais frágil. Se escolhido, sugerimos poucas unidades e o tríptico como reserva.').replace('width:66mm', 'width:70mm'))


# ---------- conceito 4: TV / menu board ----------
def tv():
    cols = ''.join(f'''<div style="background:{BK if i % 2 == 0 else '#16271c'};padding:4mm 3.5mm;display:flex;flex-direction:column">
<div style="height:40mm;border-radius:50%;overflow:hidden;border:2px solid {G};margin:0 auto 3mm;width:40mm"><img src="img/{f}.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div class="C" style="font-size:11pt;color:#fff;text-transform:uppercase;line-height:1.05">{t}</div>
<div style="font-size:5.8pt;color:#c8ccc6;line-height:1.35;margin:1.5mm 0 3mm;min-height:13mm">{d}</div>
<div style="margin-top:auto;font-size:6.6pt;color:#fff;line-height:1.7;border-top:1px solid {G};padding-top:1.5mm">
<div style="display:flex;justify-content:space-between"><span style="color:{G2}">BROTO</span><span>{PR}</span></div>
<div style="display:flex;justify-content:space-between"><span style="color:{G2}">MÉDIA</span><span>{PR}</span></div>
<div style="display:flex;justify-content:space-between"><span style="color:{G2}">GRANDE</span><span>{PR}</span></div></div></div>''' for i, (t, d, f) in enumerate(SABORES))
    return f'''<div style="background:#0a0a0a;border-radius:6px;padding:4mm;width:196mm" class="shadow">
<div style="display:flex;justify-content:space-between;align-items:center;background:{G};padding:2mm 4mm;margin-bottom:1mm">{logo(22, 16)}<span class="C" style="color:#fff;font-size:10pt;letter-spacing:1px">FORNO A LENHA · MASSA ARTESANAL</span></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1mm;height:104mm">{cols}</div></div>
<div style="width:30mm;height:8mm;background:#2a2a2a;margin:0 auto;border-radius:0 0 3px 3px"></div>'''


p5 = page(5, 'Conceito 4 · Balcão', 'Cardápio na TV',
          'Para a nova infraestrutura: uma TV no balcão com as pizzas em colunas, foto real, ingredientes e preço por tamanho.',
          f'<div style="position:absolute;left:0;top:2mm">{tv()}</div>' + side('Vantagens', [
              'Muda preço e sabor na hora, sem reimprimir.',
              'Pode alternar telas: pizzas, promoções e bebidas.',
              'As fotos reais da casa vendem por impulso no balcão.',
              'Feito com o mesmo visual do cardápio de mesa.'],
              '<b>Precisa de:</b> TV e um aparelho para exibir as imagens (pen drive ou TV smart). Equipamento não incluso.').replace('width:66mm', 'width:70mm'))

rows = [
    ('1 · Leque “fatia”', 'Delivery e mesa', 'Alto', 'Médio', 'Média', 'Ir dentro da caixa de pizza'),
    ('2 · Tríptico “quadro-negro”', 'Mesa e WhatsApp', 'Médio', 'Baixo', 'Alta', 'Cardápio principal do salão'),
    ('3 · Livro “Prove!”', 'Mesa', 'Muito alto', 'Alto', 'Baixa', 'Poucas unidades, efeito surpresa'),
    ('4 · Cardápio na TV', 'Balcão', 'Alto', 'Equipamento', 'Alta', 'Retirada e pedidos no balcão'),
]
tbl = '<table style="width:100%;border-collapse:collapse;font-size:8.6pt"><thead><tr>' + ''.join(
    f'<th style="background:{BK};color:#fff;font-family:Roboto Condensed;text-transform:uppercase;font-size:8pt;text-align:left;padding:6px 8px">{h}</th>' for h in ['Conceito', 'Onde usar', 'Impacto', 'Custo de produção', 'Durabilidade', 'Melhor uso']) + '</tr></thead><tbody>' + ''.join(
    '<tr>' + ''.join(f'<td style="padding:6px 8px;border-bottom:1px solid #d7d3c9;background:{"#fff" if k % 2 else "#f7f5f0"}">{c}</td>' for c in r) + '</tr>' for k, r in enumerate(rows)) + '</tbody></table>'
p6 = page(6, 'Resumo', 'Qual escolher?',
          'Os formatos podem ser combinados. Todos usam a mesma marca, a mesma paleta e o mesmo conteúdo.',
          tbl + f'''<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:6mm;margin-top:7mm">
<div style="background:{BK};color:#fff;border-radius:8px;padding:6mm 7mm"><div style="font-size:7pt;letter-spacing:2px;color:{G2};font-weight:700">NOSSA SUGESTÃO</div>
<div class="C" style="font-size:17pt;text-transform:uppercase;margin:1.5mm 0 2mm">Tríptico na mesa + TV no balcão</div>
<div style="font-size:8.5pt;color:#d6dad3;line-height:1.5">O tríptico resolve o salão com custo baixo e vira PDF para o WhatsApp. A TV aproveita a reforma e deixa preços e promoções sempre atualizados. O leque pode entrar depois, como material de delivery.</div></div>
<div style="background:#fff;border-radius:8px;padding:6mm 7mm;border-left:4px solid {G}"><div class="C" style="font-size:12pt;text-transform:uppercase;margin-bottom:2mm">Para fechar o cardápio</div>
<ul style="padding-left:4mm;font-size:8pt;line-height:1.6"><li>Quais formatos a casa quer?</li><li>Lista completa de sabores, bebidas e doces.</li><li>Preços por tamanho.</li><li>A paleta preto e verde está aprovada?</li><li>Haverá TV no balcão?</li></ul></div></div>
<p style="font-size:7pt;color:#666;margin-top:5mm">Prévia ilustrativa para aprovação de conceito. Fotos: registros reais da Speciale. Preços em branco até a definição da casa. Os formatos foram inspirados nas referências enviadas e serão desenhados de forma exclusiva para a Speciale.</p>''')

open('previa_cardapio.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Prévia de cardápio · Speciale</title>{CSS}</head><body>{cover}{p2}{p3}{p4}{p5}{p6}</body></html>')
