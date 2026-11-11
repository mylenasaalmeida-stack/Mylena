"""Simulação de cardápio · duas propostas · preto e verde · Speciale (A4 paisagem)."""
import math
import random
from previa_cardapio import CSS, G, G2, BK, OW, pizza_line, leaf, logo

PR = 'R$ __'
IG = '@perfildacasa'
# nome, descrição, foto, alérgenos (fichas técnicas)
SAB = [
    ('Portuguesa', 'Molho de tomate artesanal, muçarela, presunto, ovo cozido, cebola, azeitona preta e orégano.', 'port-foto6', 'GLO'),
    ('4 Queijos', 'Muçarela, gorgonzola, provolone ralado, catupiry e orégano.', 'q4-foto3', 'GL'),
    ('Frango com Catupiry', 'Frango desfiado, muçarela, catupiry, azeitona preta e orégano.', 'frango-foto1', 'GL'),
    ('Lombinho', 'Lombo fatiado, muçarela, catupiry, azeitona preta e orégano.', 'lombo-foto2', 'GL'),
]
ALG = {'G': 'Glúten', 'L': 'Leite', 'O': 'Ovo'}

EXTRA = f'''<style>
.panel{{position:relative;overflow:hidden}}
.al{{display:inline-flex;gap:1mm;vertical-align:1px}}
.al i{{font-style:normal;width:3.6mm;height:3.6mm;border-radius:50%;border:1px solid currentColor;display:inline-flex;align-items:center;justify-content:center;font-size:4.6pt;font-weight:700}}
.h{{font-family:'Roboto Condensed',sans-serif;font-weight:800;text-transform:uppercase;line-height:1}}
.step{{display:grid;grid-template-columns:9mm 1fr;gap:2mm;align-items:start;margin:3.2mm 0}}
.step b{{width:8mm;height:8mm;border-radius:50%;background:{G};color:#fff;display:flex;align-items:center;justify-content:center;font-family:'Roboto Condensed';font-size:12pt}}
.lbl{{font-size:6.5pt;color:#666;text-align:center;margin-top:1.5mm}}
.feat{{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm}}
.feat div{{background:#fff;border-radius:6px;padding:4mm;border-top:3px solid {G};font-size:7.6pt;line-height:1.45}}
.feat h5{{font-family:'Roboto Condensed';font-weight:800;font-size:10pt;text-transform:uppercase;margin-bottom:1mm}}
</style>'''


def page(n, kicker, title, note, body, T=6):
    return (f'<section class="page"><div class="hd"><div><div class="k">{kicker}</div><h2>{title}</h2></div><p>{note}</p></div>'
            f'<div class="stage">{body}</div><div class="ft"><span>Speciale Pizzas Artesanais · Simulação de cardápio · preto e verde</span><span>{n} / {T}</span></div></section>')


def alg(codes, color='#fff'):
    return f'<span class="al" style="color:{color}">' + ''.join(f'<i title="{ALG[c]}">{c}</i>' for c in codes) + '</span>'


def qr(size_mm=24, dark=BK, light='#fff', seed=7):
    random.seed(seed)
    n = 25
    cells = ''
    for y in range(n):
        for x in range(n):
            fin = any(x0 <= x < x0 + 7 and y0 <= y < y0 + 7 for x0, y0 in [(0, 0), (n - 7, 0), (0, n - 7)])
            if fin:
                lx, ly = (x % (n - 7) if x >= n - 7 else x), (y % (n - 7) if y >= n - 7 else y)
                on = lx in (0, 6) or ly in (0, 6) or (2 <= lx <= 4 and 2 <= ly <= 4)
            else:
                on = random.random() < .48
            if on:
                cells += f'<rect x="{x}" y="{y}" width="1" height="1"/>'
    return f'<svg width="{size_mm}mm" height="{size_mm}mm" viewBox="-2 -2 {n + 4} {n + 4}"><rect x="-2" y="-2" width="{n + 4}" height="{n + 4}" fill="{light}"/><g fill="{dark}">{cells}</g></svg>'


def sizes_svg(w=80, color=G2, text='#fff'):
    # círculos em escala: 25, 28, 35 cm
    s = f'<svg width="{w}mm" height="{w * .5}mm" viewBox="0 0 80 40">'
    x = 2
    for nome, d, fat in [('Broto', 25, 4), ('Média', 28, 5), ('Grande', 35, 8)]:
        r = d / 35 * 12.5
        cx = x + r
        cy = 20
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width=".5"/>'
        for k in range(fat):
            a = math.radians(k * 360 / fat - 90)
            s += f'<line x1="{cx}" y1="{cy}" x2="{cx + r * math.cos(a):.2f}" y2="{cy + r * math.sin(a):.2f}" stroke="{color}" stroke-width=".35"/>'
        s += f'<text x="{cx}" y="{cy + r + 4.2}" text-anchor="middle" font-family="Roboto Condensed" font-weight="800" font-size="3.3" fill="{text}">{nome.upper()}</text>'
        s += f'<text x="{cx}" y="{cy + r + 7.6}" text-anchor="middle" font-family="Poppins" font-size="2.3" fill="{text}" opacity=".8">{fat} fatias · ≈{d} cm</text>'
        x += 2 * r + 3.5
    return s + '</svg>'


# ======================= PROPOSTA A · TRÍPTICO =======================
PW, PH = 92, 178   # painel em mm


def panel(bg, inner, color='#fff', pad='8mm 7mm'):
    return f'<div class="panel" style="width:{PW}mm;height:{PH}mm;background:{bg};color:{color};padding:{pad}">{inner}</div>'


a_capa = panel(BK, f'''
<svg style="position:absolute;left:-28mm;bottom:-34mm" width="150mm" height="150mm" viewBox="0 0 150 150">{pizza_line(75, 75, 70, '#2f6a45', .6)}</svg>
<div style="position:relative">{logo(40, 29)}</div>
<div style="position:absolute;left:7mm;right:7mm;top:52mm">
<div style="font-size:6.5pt;letter-spacing:2px;color:{G2};font-weight:700">FORNO A LENHA · MASSA DA CASA</div>
<div class="h" style="font-size:31pt;margin-top:2mm">Saiu do<br><span style="color:{G2}">forno</span><br>agora.</div></div>
<div style="position:absolute;left:7mm;bottom:9mm;right:7mm;display:flex;align-items:center;gap:3mm;background:rgba(17,19,18,.85);padding:2mm;border-radius:4px">
<div style="width:20mm;height:20mm;border-radius:50%;overflow:hidden;border:2px solid {G2};flex:none"><img src="img/lombo-foto2.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div style="font-size:6.6pt;line-height:1.4">Cardápio · Pizzas artesanais<br><span style="color:{G2}">Recife</span></div></div>''')

a_contra = panel(G, f'''
<div class="h" style="font-size:17pt">Tirou foto?<br>Marca a gente!</div>
<div style="font-size:7.4pt;margin:2mm 0 4mm;line-height:1.45">Poste a sua pizza e marque <b>{IG}</b>. As melhores fotos aparecem no nosso perfil.</div>
<div style="height:58mm;border-radius:6px;overflow:hidden;border:3px solid #fff;transform:rotate(-2deg);box-shadow:0 5px 12px rgba(0,0,0,.3)"><img src="img/frango-foto1.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div style="display:flex;gap:4mm;align-items:center;margin-top:7mm">{qr(25, BK, '#fff', 3)}
<div style="font-size:7pt;line-height:1.45"><b class="h" style="font-size:10pt;display:block">Peça pelo WhatsApp</b>Aponte a câmera e veja o cardápio atualizado.</div></div>
<div style="position:absolute;left:7mm;right:7mm;bottom:7mm;font-size:6.4pt;line-height:1.6;border-top:1px solid rgba(255,255,255,.4);padding-top:2mm">
Horário, endereço e telefone: <b>a confirmar</b><br>{IG}</div>''')

a_aba = panel(OW, f'''
<div class="h" style="font-size:17pt;color:{BK}">Como pedir</div>
<div style="font-size:7pt;color:#555;margin:1mm 0 2mm">Em três passos, sem dúvida.</div>
<div class="step"><b>1</b><div><div class="h" style="font-size:10pt">Escolha o tamanho</div><div style="font-size:6.8pt;color:#444">Broto, Média ou Grande. Veja o desenho ao lado.</div></div></div>
<div class="step"><b>2</b><div><div class="h" style="font-size:10pt">Escolha o sabor</div><div style="font-size:6.8pt;color:#444">Um sabor ou meio a meio (regra a confirmar).</div></div></div>
<div class="step"><b>3</b><div><div class="h" style="font-size:10pt">Complete o pedido</div><div style="font-size:6.8pt;color:#444">Bebida e sobremesa no painel ao lado.</div></div></div>
<div style="margin-top:6mm;background:{BK};color:#fff;border-radius:6px;padding:4mm">
<div class="h" style="font-size:10pt;color:{G2};margin-bottom:1.5mm">Legenda</div>
<div style="font-size:6.8pt;line-height:1.9">{alg('G')} Contém glúten<br>{alg('L')} Contém leite<br>{alg('O')} Contém ovo</div>
<div style="font-size:6pt;color:#bbb;margin-top:1.5mm">Todas as massas contêm glúten e soja (óleo da massa).</div></div>
<div style="position:absolute;right:-8mm;bottom:-6mm">{"<svg width='50mm' height='30mm' viewBox='0 0 50 30'>" + leaf(4, 26, 1.6, G) + "</svg>"}</div>''', BK)

a_tam = panel(OW, f'''
<div class="h" style="font-size:20pt;color:{G}">Tamanhos</div>
<div style="font-size:7pt;color:#555;margin:1mm 0 3mm">Desenho em escala: compare antes de pedir.</div>
<div style="background:{BK};border-radius:6px;padding:3mm 2mm 1mm">{sizes_svg(78)}</div>
<div style="font-size:6pt;color:#777;margin-top:1.2mm">Diâmetros estimados, em medição.</div>
<div class="h" style="font-size:20pt;color:{G};margin-top:7mm">Bebidas</div>
''' + ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px dashed #cfc9bd;padding:1.6mm 0;font-size:7.6pt"><span>{x}</span><span>{PR}</span></div>' for x in ['Refrigerante lata · a definir', 'Refrigerante 1 L · a definir', 'Suco · a definir', 'Água · a definir']) + f'''
<div class="h" style="font-size:20pt;color:{G};margin-top:6mm">Doces</div>
''' + ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px dashed #cfc9bd;padding:1.6mm 0;font-size:7.6pt"><span>{x}</span><span>{PR}</span></div>' for x in ['Pizza doce · a definir', 'Sobremesa · a definir']), BK)

a_piz = panel(BK, f'''
<div class="h" style="font-size:22pt;color:{G2}">Pizzas</div>
<div style="font-size:6.8pt;color:#bbb;margin:1mm 0 3mm">Massa feita na casa, assada no forno a lenha.</div>
''' + ''.join(f'''<div style="display:grid;grid-template-columns:19mm 1fr;gap:3mm;align-items:center;padding:2.4mm 0;border-bottom:1px solid #2a2d2b">
<div style="width:19mm;height:19mm;border-radius:50%;overflow:hidden;border:1.5px solid {G}"><img src="img/{f}.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div><div style="display:flex;justify-content:space-between;align-items:center"><span class="h" style="font-size:10.5pt">{t}</span>{alg(a, G2)}</div>
<div style="font-size:6.3pt;color:#cfd3cc;line-height:1.35;margin:.6mm 0 .8mm">{d}</div>
<div style="font-size:6.5pt;color:{G2};font-weight:600">B {PR} · M {PR} · G {PR}</div></div></div>''' for t, d, f, a in SAB) + f'''
<div style="font-size:6.3pt;color:#888;margin-top:2.5mm">Mais sabores: a confirmar com a casa.</div>''')


a_hist = panel(G, f'''
<div class="h" style="font-size:20pt">Nossa pizza</div>
<div style="font-size:7.4pt;line-height:1.5;margin:2mm 0 4mm">Massa feita na casa, coberta com molho de tomate artesanal e assada no forno a lenha, entre 340 e 380 °C, por 3 a 4 minutos.</div>
<div style="height:62mm;border-radius:6px;overflow:hidden;border:3px solid #fff;transform:rotate(2deg);box-shadow:0 5px 12px rgba(0,0,0,.3)"><img src="img/port-foto2.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div style="font-size:6.4pt;margin-top:2mm;opacity:.9">Massas abertas na hora, na nossa bancada.</div>
<div style="margin-top:6mm;background:{BK};border-radius:6px;padding:4mm">
<div class="h" style="font-size:11pt;color:{G2}">Meio a meio</div>
<div style="font-size:6.8pt;margin-top:1mm;line-height:1.45">Pode escolher dois sabores na mesma pizza. Regra de preço a confirmar com a casa.</div></div>''')


def spread(panels, label):
    return f'<div><div class="shadow" style="display:flex">{"".join(panels)}</div><div class="lbl">{label}</div></div>'


pA1 = page(2, 'Proposta A · Tríptico de mesa', 'Lado de fora',
           'Capa que dá vontade, contracapa que puxa para o Instagram e uma aba que ensina a pedir.',
           f'<div style="display:flex;justify-content:center">{spread([a_aba, a_contra, a_capa], "Aba interna (como pedir) · contracapa (foto, QR e Instagram) · capa")}</div>')


# ======================= PROPOSTA B · CARDÁPIO REDONDO =======================
D = 122  # diâmetro em mm


def round_front():
    return f'''<div style="width:{D}mm;height:{D}mm;border-radius:50%;background:{BK};position:relative;overflow:hidden;box-shadow:0 10px 24px rgba(0,0,0,.45);border:4mm solid {G}">
<img src="img/q4-foto3.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.55">
<div style="position:absolute;inset:0;background:radial-gradient(circle,rgba(17,19,18,.15) 30%,rgba(17,19,18,.85) 75%)"></div>
<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:58mm;height:58mm;border-radius:50%;background:{BK};border:2px solid {G2};display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center">
<svg width="16mm" height="12mm" viewBox="0 0 46 34"><ellipse cx="9" cy="15" rx="8.5" ry="7" fill="#fff"/><ellipse cx="18" cy="27" rx="8" ry="6.5" fill="#fff"/><path d="M18 13 C21 4 33 1 45 2 C42 10 31 15 18 13Z" fill="{G}"/></svg>
<div class="h" style="font-size:17pt;margin-top:1.5mm">SPECIALE</div><div style="font-size:5pt;letter-spacing:2.4px;font-weight:600">PIZZAS ARTESANAIS</div>
<div style="font-size:7pt;color:{G2};margin-top:3mm;font-weight:600">VIRE A PIZZA →</div></div>
<div style="position:absolute;left:50%;bottom:9mm;transform:translateX(-50%);background:{G};color:#fff;font-size:7pt;font-weight:700;padding:1.2mm 4mm;border-radius:20px;white-space:nowrap">Poste e marque {IG}</div></div>'''


def round_back():
    cx = cy = D / 2
    R = D / 2 - 4
    n = len(SAB)
    s = f'<svg width="{D}mm" height="{D}mm" viewBox="0 0 {D} {D}" style="filter:drop-shadow(0 10px 14px rgba(0,0,0,.45))">'
    s += f'<circle cx="{cx}" cy="{cy}" r="{D / 2}" fill="{G}"/><defs>'
    for i, (_, _, f, _) in enumerate(SAB):
        s += f'<clipPath id="ph{i}"><circle cx="0" cy="0" r="8.5"/></clipPath>'
    s += '</defs>'
    for i, (t, d, f, a) in enumerate(SAB):
        a1, a2 = i * 360 / n - 45, (i + 1) * 360 / n - 45
        p1 = (cx + R * math.sin(math.radians(a1)), cy - R * math.cos(math.radians(a1)))
        p2 = (cx + R * math.sin(math.radians(a2)), cy - R * math.cos(math.radians(a2)))
        col = BK if i % 2 == 0 else '#1a2e21'
        s += f'<path d="M{cx},{cy} L{p1[0]:.2f},{p1[1]:.2f} A{R},{R} 0 0 1 {p2[0]:.2f},{p2[1]:.2f} Z" fill="{col}" stroke="{G}" stroke-width=".8"/>'
        # posições: foto (fx, fy) e bloco de texto (tx, ty = topo do texto)
        if i == 0:   fx, fy, tx, ty = cx, cy - R * .87, cx, cy - R * .69
        elif i == 2: fx, fy, tx, ty = cx, cy + R * .9, cx, cy + R * .28
        elif i == 1: fx, fy, tx, ty = cx + R * .6, cy - 17, cx + R * .6, cy - 3
        else:        fx, fy, tx, ty = cx - R * .6, cy - 17, cx - R * .6, cy - 3
        s += f'<g transform="translate({fx:.2f},{fy:.2f})"><circle r="9.3" fill="{G2}"/><image href="img/{f}.jpg" x="-8.5" y="-8.5" width="17" height="17" preserveAspectRatio="xMidYMid slice" clip-path="url(#ph{i})"/></g>'
        s += (f'<foreignObject x="{tx - 16:.2f}" y="{ty - 1.5:.2f}" width="32" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="color:#fff;text-align:center;font-family:Poppins;padding-top:1.5px">'
              f'<div style="font-family:Roboto Condensed;font-weight:800;font-size:3.5px;text-transform:uppercase;line-height:1.15">{t}</div>'
              f'<div style="font-size:2px;color:#cfd3cc;line-height:1.3;margin:.7px 0">{d}</div>'
              f'<div style="font-size:2.05px;color:{G2};font-weight:600">B {PR} · M {PR} · G {PR}</div>'
              f'<div style="font-size:1.9px;margin-top:.5px;color:{G2}">' + ' · '.join(ALG[c] for c in a) + '</div></div></foreignObject>')
    s += f'<circle cx="{cx}" cy="{cy}" r="15" fill="{OW}" stroke="{G}" stroke-width="1"/>'
    s += (f'<foreignObject x="{cx - 14}" y="{cy - 11}" width="28" height="22"><div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center;font-family:Poppins;color:{BK}">'
          f'<div style="font-family:Roboto Condensed;font-weight:800;font-size:3.3px">TAMANHOS</div>'
          f'<div style="font-size:2.2px;line-height:1.5;margin-top:.5px">Broto · 4 fatias<br>Média · 5 fatias<br>Grande · 8 fatias</div>'
          f'<div style="font-size:2px;color:{G};margin-top:.6px;font-weight:600">Bebidas no QR Code</div></div></foreignObject>')
    return s + '</svg>'


pB1 = page(4, 'Proposta B · Cardápio redondo', 'Uma pizza na mão',
           'Cardápio em formato de pizza: a frente é a capa para foto; o verso tem uma fatia para cada sabor, com foto, ingredientes e preços.',
           f'''<div style="display:flex;justify-content:center;gap:12mm;align-items:center;margin-top:2mm">
<div>{round_front()}<div class="lbl">Frente · capa para foto</div></div>
<div>{round_back()}<div class="lbl">Verso · uma fatia por sabor, tamanhos no centro</div></div></div>''')


def board():
    # apoio de mesa para o cardápio redondo + cartão de bebidas
    bev = ''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px dashed #3a3f3c;padding:1.5mm 0;font-size:7.2pt"><span>{x}</span><span>{PR}</span></div>' for x in ['Refrigerante lata · a definir', 'Refrigerante 1 L · a definir', 'Suco · a definir', 'Água · a definir', 'Pizza doce · a definir', 'Sobremesa · a definir'])
    return f'''<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6mm">
<div style="background:{BK};color:#fff;border-radius:8px;padding:6mm" class="shadow"><div class="h" style="font-size:15pt;color:{G2}">Cartão de bebidas e doces</div>
<div style="font-size:6.8pt;color:#bbb;margin:1mm 0 3mm">Cartão retangular que acompanha o cardápio redondo.</div>{bev}</div>
<div style="background:{OW};border-radius:8px;padding:6mm" class="shadow"><div class="h" style="font-size:15pt;color:{G}">Tamanhos em escala</div>
<div style="font-size:6.8pt;color:#555;margin:1mm 0 3mm">Impresso no verso do cartão de bebidas.</div>
<div style="background:{BK};border-radius:6px;padding:3mm 2mm 1mm">{sizes_svg(70)}</div>
<div style="font-size:6.8pt;margin-top:4mm;line-height:1.9">{alg('G', BK)} Glúten &nbsp; {alg('L', BK)} Leite &nbsp; {alg('O', BK)} Ovo</div></div>
<div style="background:{G};color:#fff;border-radius:8px;padding:6mm;display:flex;flex-direction:column" class="shadow"><div class="h" style="font-size:15pt">QR na mesa</div>
<div style="font-size:7pt;margin:1mm 0 4mm">Um display pequeno de mesa com QR Code para o cardápio digital e o WhatsApp.</div>
<div style="background:#fff;border-radius:6px;padding:3mm;align-self:center">{qr(34, BK, '#fff', 11)}</div>
<div style="font-size:7pt;margin-top:4mm;text-align:center">Peça pelo WhatsApp · {IG}</div></div></div>'''


pB2 = page(5, 'Proposta B · Cardápio redondo', 'Peças de apoio',
           'O redondo mostra as pizzas. Bebidas, doces e tamanhos ficam num cartão de apoio; o QR Code fica num display de mesa.',
           board())

feat = [
    ('Pedido em 3 passos', 'Tamanho, sabor e bebida, nessa ordem. O cliente decide mais rápido e chama menos o garçom.'),
    ('Tamanhos em escala', 'Desenho de Broto, Média e Grande lado a lado, com fatias e centímetros. Acaba a pergunta “de que tamanho é?”.'),
    ('Alérgenos visíveis', 'Ícones G, L e O em cada sabor, a partir das fichas técnicas. Mais segurança para quem tem restrição.'),
    ('Feito para foto', 'Capa forte, fotos reais da casa e um convite para postar e marcar o perfil. O cardápio vira divulgação.'),
]
rows = [
    ('Proposta A · Tríptico', 'Leitura muito fácil', 'Boa (capa e contracapa)', 'Baixo', 'Alta', 'Salão e PDF no WhatsApp'),
    ('Proposta B · Redondo', 'Fácil (pizzas no verso)', 'Muito alta (formato de pizza)', 'Médio (corte redondo)', 'Média', 'Salão, com cartão de bebidas'),
]
tbl = '<table style="width:100%;border-collapse:collapse;font-size:8.4pt;margin-top:6mm"><thead><tr>' + ''.join(
    f'<th style="background:{BK};color:#fff;font-family:Roboto Condensed;text-transform:uppercase;font-size:8pt;text-align:left;padding:6px 8px">{h}</th>' for h in ['Proposta', 'Experiência', 'Instagramável', 'Custo de impressão', 'Durabilidade', 'Onde usar']) + '</tr></thead><tbody>' + ''.join(
    '<tr>' + ''.join(f'<td style="padding:6px 8px;border-bottom:1px solid #d7d3c9;background:#fff">{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>'
pC = page(6, 'Experiência do cliente', 'O que as duas propostas têm em comum',
          'Os dois formatos usam o mesmo conteúdo e os mesmos recursos para facilitar o pedido.',
          '<div class="feat">' + ''.join(f'<div><h5>{t}</h5>{d}</div>' for t, d in feat) + '</div>' + tbl +
          f'''<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:6mm;margin-top:6mm">
<div style="background:{BK};color:#fff;border-radius:8px;padding:5mm 6mm"><div style="font-size:7pt;letter-spacing:2px;color:{G2};font-weight:700">SUGESTÃO</div>
<div class="h" style="font-size:15pt;margin:1.5mm 0 2mm">Tríptico no dia a dia, redondo como destaque</div>
<div style="font-size:8pt;color:#d6dad3;line-height:1.5">A proposta A resolve o salão e o WhatsApp com custo baixo. A proposta B pode ser usada em poucas mesas, ou na reabertura, para gerar fotos e divulgação.</div></div>
<div style="background:#fff;border-radius:8px;padding:5mm 6mm;border-left:4px solid {G}"><div class="h" style="font-size:11pt;margin-bottom:2mm">Falta para fechar</div>
<ul style="padding-left:4mm;font-size:7.8pt;line-height:1.6"><li>Lista completa de sabores, bebidas e doces</li><li>Preços por tamanho</li><li>Perfil do Instagram, WhatsApp, horário e endereço</li><li>Regra do meio a meio</li></ul></div></div>''')

capa = f'''<section class="page" style="background:{BK};color:#fff">
<svg style="position:absolute;right:-40mm;top:-30mm" width="210mm" height="210mm" viewBox="0 0 210 210">{pizza_line(105, 105, 98, '#2b4a36', .7)}</svg>
<div style="position:absolute;left:18mm;top:18mm">{logo(44, 32)}</div>
<div style="position:absolute;left:18mm;top:60mm;max-width:160mm">
<div style="font-size:8pt;letter-spacing:3px;color:{G2};font-weight:700">SIMULAÇÃO · DUAS PROPOSTAS</div>
<div class="h" style="font-size:48pt;margin-top:3mm">Um cardápio<br><span style="color:{G2}">que dá vontade</span><br>de fotografar</div>
<p style="font-size:11pt;color:#d9dcd6;margin-top:6mm;line-height:1.5">Proposta A: tríptico de mesa, fácil de ler.<br>Proposta B: cardápio redondo, em formato de pizza.</p></div>
<div style="position:absolute;left:18mm;bottom:16mm;font-size:7.5pt;color:#aaa">Conteúdo real da casa (fichas técnicas e fotos). Preços, bebidas, doces e contatos: a definir.</div></section>'''

T = 6
pA2 = page(3, 'Proposta A · Tríptico de mesa', 'Lado de dentro',
           'Ao abrir: tamanhos em escala, pizzas com foto, ingredientes, alérgenos e os três preços na mesma linha.',
           f'<div style="display:flex;justify-content:center">{spread([a_tam, a_piz, a_hist], "Tamanhos, bebidas e doces · pizzas · nossa pizza e meio a meio")}</div>', T)

open('simulacao_cardapio.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Simulação de cardápio · Speciale</title>{CSS}{EXTRA}</head><body>{capa}{pA1}{pA2}{pB1}{pB2}{pC}</body></html>')
