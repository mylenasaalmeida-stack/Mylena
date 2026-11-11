"""Cardápio Speciale · arquivos finais para aprovação (tamanho real, A4 paisagem)."""
import math
from previa_cardapio import G, G2, BK, OW, pizza_line, leaf
from simulacao_cardapio import qr

IG = '@perfildacasa'
TAG = '#EuNaSpeciale'
PRECO = [('Broto', 4, 25, 38), ('Média', 5, 28, 45), ('Grande', 8, 35, 68)]
SAB = [
    ('Portuguesa', 'Molho de tomate artesanal, muçarela, presunto, ovo cozido, cebola, azeitona preta e orégano.', 'port-foto6', 'GLO'),
    ('4 Queijos', 'Muçarela, gorgonzola, provolone ralado, catupiry e orégano.', 'q4-foto3', 'GL'),
    ('Frango com Catupiry', 'Frango desfiado, muçarela, catupiry, azeitona preta e orégano.', 'frango-foto1', 'GL'),
    ('Lombinho', 'Lombo fatiado, muçarela, catupiry, azeitona preta e orégano.', 'lombo-foto2', 'GL'),
]
ALG = {'G': 'Glúten', 'L': 'Leite', 'O': 'Ovo'}
INK = '#0e100f'
MUTE = '#b9bfb8'

CSS = f'''<style>
@import url('fonts.css');
@page{{size:A4 landscape;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Poppins',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact;font-variant-numeric:lining-nums tabular-nums}}
.page{{width:297mm;height:210mm;position:relative;overflow:hidden;page-break-after:always}}
.page:last-child{{page-break-after:auto}}
/* hierarquia tipográfica */
.d1{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;line-height:.9;letter-spacing:-.2px}}
.h2{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:19pt;line-height:1;letter-spacing:.2px}}
.h3{{font-family:'Roboto Condensed';font-weight:700;text-transform:uppercase;font-size:11.5pt;line-height:1.05;letter-spacing:.4px}}
.ov{{font-size:6.2pt;font-weight:600;letter-spacing:2.2px;text-transform:uppercase}}
.bd{{font-size:7.6pt;line-height:1.45}}
.sm{{font-size:6.2pt;line-height:1.4}}
.rule{{width:12mm;height:1.2mm;background:{G};margin:2.5mm 0 4mm}}
.pn{{position:absolute;top:0;bottom:0;width:99mm;overflow:hidden;padding:13mm 10mm 11mm}}
.fold{{position:absolute;top:0;bottom:0;width:0;border-left:.3pt dashed rgba(150,150,150,.6)}}
.logo{{display:flex;align-items:center;gap:7px}}
.logo b{{font-family:'Roboto Condensed';font-weight:800;font-size:15pt;line-height:1;display:block;letter-spacing:.3px}}
.logo i{{font-style:normal;font-size:4.6pt;letter-spacing:2.6px;font-weight:600;display:block;margin-top:1px}}
.al{{display:inline-flex;gap:.8mm}}
.al i{{font-style:normal;width:3.4mm;height:3.4mm;border-radius:50%;border:.7pt solid currentColor;display:inline-flex;align-items:center;justify-content:center;font-size:4.3pt;font-weight:700}}
.ph{{border-radius:50%;overflow:hidden}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block}}
.price{{font-family:'Roboto Condensed';font-weight:800;line-height:1}}
.price sup{{font-size:45%;vertical-align:top;margin-right:.6mm;position:relative;top:1mm}}
.cap{{position:absolute;left:12mm;bottom:5mm;font-size:6pt;color:#888}}
.paper{{background:#e9e7e1}}
</style>'''

LOGO_SVG = ('<svg width="{w}mm" height="{h}mm" viewBox="0 0 46 34"><ellipse cx="9" cy="15" rx="8.5" ry="7" fill="{c}"/>'
            '<ellipse cx="18" cy="27" rx="8" ry="6.5" fill="{c}"/><path d="M18 13 C21 4 33 1 45 2 C42 10 31 15 18 13Z" fill="' + G + '"/></svg>')


def logo(w=10, c='#fff', tc='#fff', big=False):
    h = w * 34 / 46
    sz = 'style="font-size:22pt"' if big else ''
    return f'<div class="logo" style="color:{tc}">{LOGO_SVG.format(w=w, h=h, c=c)}<div><b {sz}>SPECIALE</b><i>PIZZAS ARTESANAIS</i></div></div>'


def alg(codes, color):
    return f'<span class="al" style="color:{color}">' + ''.join(f'<i>{c}</i>' for c in codes) + '</span>'


def price_row(color, accent, size=17):
    return '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2mm">' + ''.join(
        f'<div style="border:.6pt solid {accent};border-radius:3mm;padding:2.6mm 1mm 2.2mm;text-align:center;color:{color}">'
        f'<div class="ov" style="color:{accent};letter-spacing:1.4px">{n}</div>'
        f'<div class="price" style="font-size:{size}pt;margin:1mm 0 .6mm"><sup>R$</sup>{p}</div>'
        f'<div class="sm" style="opacity:.75">{f} fatias · ≈{d} cm</div></div>' for n, f, d, p in PRECO) + '</div>'


def sizes_svg(w=76, color=G2, text='#fff'):
    s = f'<svg width="{w}mm" height="{w * .46:.1f}mm" viewBox="0 0 76 35">'
    x = 3
    for nome, fat, d, _ in PRECO:
        r = d / 35 * 10.8
        cx, cy = x + r, 15
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width=".45"/>'
        for k in range(fat):
            a = math.radians(k * 360 / fat - 90)
            s += f'<line x1="{cx}" y1="{cy}" x2="{cx + r * math.cos(a):.2f}" y2="{cy + r * math.sin(a):.2f}" stroke="{color}" stroke-width=".3"/>'
        s += f'<text x="{cx}" y="{cy + r + 4.4}" text-anchor="middle" font-family="Roboto Condensed" font-weight="800" font-size="3.2" fill="{text}">{nome.upper()}</text>'
        x += 2 * r + 5
    return s + '</svg>'


def frame(n, total, label):
    return f'<div class="cap">Speciale · Cardápio · {label} · página {n} de {total} · tamanho real</div>'


TOTAL = 7

# ============ 1. CAPA DO ARQUIVO ============
capa = f'''<section class="page" style="background:{INK};color:#fff">
<svg style="position:absolute;right:-48mm;top:-36mm" width="220mm" height="220mm" viewBox="0 0 220 220">{pizza_line(110, 110, 104, '#24412e', .7)}</svg>
<div style="position:absolute;left:20mm;top:18mm">{logo(14)}</div>
<div style="position:absolute;left:20mm;top:56mm;width:150mm">
<div class="ov" style="color:{G2}">Cardápio · arquivos para aprovação</div>
<div class="d1" style="font-size:52pt;margin-top:4mm">O novo<br><span style="color:{G2}">cardápio</span></div>
<div class="bd" style="font-size:10.5pt;color:#d5d9d3;margin-top:6mm;max-width:130mm">Duas propostas em tamanho real de impressão, com preços definidos e um kit para o cliente mostrar nas redes que está na Speciale.</div></div>
<div style="position:absolute;left:20mm;right:20mm;bottom:16mm;display:grid;grid-template-columns:1.2fr 1fr;gap:12mm;align-items:end">
<div><div class="ov" style="color:{G2};margin-bottom:2.5mm">Neste arquivo</div>
<div class="bd" style="color:#e6e9e4;line-height:1.9">
<b style="color:{G2}">A</b> · Tríptico de mesa · lado de fora e lado de dentro (págs. 2 e 3)<br>
<b style="color:{G2}">B</b> · Cardápio redondo · frente e verso (págs. 4 e 5)<br>
<b style="color:{G2}">+</b> · Peças de apoio e kit “Estou na Speciale” (págs. 6 e 7)</div></div>
<div><div class="ov" style="color:{G2};margin-bottom:2.5mm">Preços das pizzas</div>{price_row('#fff', G2, 18)}
<div class="sm" style="color:#9aa29b;margin-top:2mm">Base: Média a R$ 45. Mesmo preço para todos os sabores.</div></div></div>
</section>'''

# ============ 2. PROPOSTA A · LADO DE FORA ============
a_fora_1 = f'''<div class="pn" style="left:0;background:{OW};color:{INK}">
<div class="ov" style="color:{G}">Feita aqui</div><div class="h2" style="margin-top:1.5mm">Nossa pizza</div><div class="rule"></div>
<div class="bd" style="color:#3c403d">Massa feita na casa e aberta na hora, molho de tomate artesanal e forno a lenha entre 340 e 380 °C. Cada pizza fica pronta em 3 a 4 minutos.</div>
<div style="height:62mm;border-radius:3mm;overflow:hidden;margin-top:6mm"><img src="img/port-foto2.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div class="sm" style="color:#6b706c;margin-top:1.5mm">Massas abertas na nossa bancada.</div>
<div style="position:absolute;left:10mm;right:10mm;bottom:11mm;border-top:.6pt solid #cfcabf;padding-top:3mm;display:flex;justify-content:space-between;align-items:center">
<div class="h3" style="font-size:9.5pt">Meio a meio</div><div class="sm" style="color:#555;text-align:right">Dois sabores<br>na mesma pizza</div></div></div>'''

a_fora_2 = f'''<div class="pn" style="left:99mm;background:{G};color:#fff">
<div class="ov" style="color:#dff0d6">Estou na Speciale</div><div class="h2" style="margin-top:1.5mm;font-size:21pt">Chegou?<br>Mostra pra gente.</div>
<div style="position:relative;height:84mm;margin-top:6mm">
<div style="position:absolute;left:4mm;top:0;width:60mm;background:#fff;padding:2.5mm 2.5mm 9mm;transform:rotate(-4deg);box-shadow:0 2mm 4mm rgba(0,0,0,.25)">
<div style="height:58mm;overflow:hidden"><img src="img/frango-foto1.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div style="font-family:'Roboto Condensed';font-weight:700;color:{INK};font-size:8pt;margin-top:2mm;text-align:center">{TAG}</div></div></div>
<div style="display:grid;grid-template-columns:auto 1fr;gap:3mm;align-items:start" class="bd">
<b class="price" style="font-size:13pt">1</b><span>Tire a foto da sua pizza.</span>
<b class="price" style="font-size:13pt">2</b><span>Marque <b>{IG}</b> e a localização.</span>
<b class="price" style="font-size:13pt">3</b><span>Use <b>{TAG}</b>.</span></div>
<div style="position:absolute;left:10mm;right:10mm;bottom:11mm;display:flex;gap:3.5mm;align-items:center;border-top:.6pt solid rgba(255,255,255,.45);padding-top:3.5mm">
<div style="background:#fff;padding:1mm;border-radius:1.5mm">{qr(17, INK, '#fff', 3)}</div><div class="sm">Peça pelo WhatsApp<br>e veja bebidas e sobremesas.</div></div></div>'''

a_fora_3 = f'''<div class="pn" style="left:198mm;background:{INK};color:#fff">
<svg style="position:absolute;left:-30mm;bottom:-40mm" width="160mm" height="160mm" viewBox="0 0 160 160">{pizza_line(80, 80, 74, '#26462f', .6)}</svg>
<div style="position:relative">{logo(12)}</div>
<div style="position:absolute;left:10mm;right:10mm;top:60mm">
<div class="ov" style="color:{G2}">Forno a lenha · massa da casa</div>
<div class="d1" style="font-size:40pt;margin-top:3mm">Saiu<br>do <span style="color:{G2}">forno</span><br>agora.</div></div>
<div style="position:absolute;left:10mm;right:10mm;bottom:11mm;display:flex;align-items:center;gap:3.5mm">
<div class="ph" style="width:22mm;height:22mm;border:.9mm solid {G2};flex:none"><img src="img/lombo-foto2.jpg"></div>
<div><div class="h3" style="font-size:10pt">Cardápio</div><div class="sm" style="color:{MUTE}">Pizzas artesanais · Recife</div></div></div></div>'''

pA_fora = f'''<section class="page">{a_fora_1}{a_fora_2}{a_fora_3}<div class="fold" style="left:99mm"></div><div class="fold" style="left:198mm"></div></section>'''

# ============ 3. PROPOSTA A · LADO DE DENTRO ============
a_in_1 = f'''<div class="pn" style="left:0;background:{OW};color:{INK}">
<div class="ov" style="color:{G}">Passo 1</div><div class="h2" style="margin-top:1.5mm">Escolha o tamanho</div><div class="rule"></div>
<div style="background:{INK};border-radius:3mm;padding:4mm 3mm 2.5mm">{sizes_svg(73)}</div>
<div style="margin-top:4mm">{price_row(INK, G, 17)}</div>
<div class="sm" style="color:#6b706c;margin-top:2mm">Mesmo preço para todos os sabores. Diâmetros aproximados.</div>
<div class="ov" style="color:{G};margin-top:7mm">Passo 2</div><div class="h3" style="margin-top:1mm">Escolha um ou dois sabores</div>
<div class="bd" style="color:#3c403d;margin-top:1mm">Os sabores estão no painel ao lado. Quer dois? Peça meio a meio.</div>
<div class="ov" style="color:{G};margin-top:5mm">Passo 3</div><div class="h3" style="margin-top:1mm">Complete o pedido</div>
<div class="bd" style="color:#3c403d;margin-top:1mm">Bebidas e sobremesas no QR Code ou com o atendente.</div>
<div style="position:absolute;left:10mm;right:10mm;bottom:11mm;display:flex;gap:4mm;align-items:center;border-top:.6pt solid #cfcabf;padding-top:3mm" class="sm">
<span>{alg('G', INK)} Glúten</span><span>{alg('L', INK)} Leite</span><span>{alg('O', INK)} Ovo</span><span style="color:#6b706c">Massas com glúten e soja.</span></div></div>'''

items = ''.join(f'''<div style="display:grid;grid-template-columns:22mm 1fr;gap:4mm;align-items:center;padding:3.6mm 0;border-bottom:.5pt solid #2a2e2b">
<div class="ph" style="width:22mm;height:22mm;border:.7mm solid {G}"><img src="img/{f}.jpg"></div>
<div><div style="display:flex;justify-content:space-between;align-items:center;gap:2mm"><span class="h3">{t}</span>{alg(a, G2)}</div>
<div class="bd" style="color:{MUTE};margin-top:1.2mm;font-size:7.2pt">{d}</div></div></div>''' for t, d, f, a in SAB)
a_in_2 = f'''<div class="pn" style="left:99mm;background:{INK};color:#fff">
<div class="ov" style="color:{G2}">Os sabores da casa</div><div class="h2" style="margin-top:1.5mm;color:{G2}">Pizzas</div><div class="rule"></div>{items}
<div style="position:absolute;left:10mm;right:10mm;bottom:11mm;display:flex;justify-content:space-between;align-items:baseline" class="sm">
<span style="color:{MUTE}">Broto · Média · Grande</span><span class="price" style="font-size:12pt;color:#fff"><sup>R$</sup>38 · 45 · 68</span></div></div>'''

a_in_3 = f'''<div class="pn" style="left:198mm;background:{G};color:#fff">
<div class="ov" style="color:#dff0d6">Para acompanhar</div><div class="h2" style="margin-top:1.5mm">Bebidas e sobremesas</div><div class="rule" style="background:#fff"></div>
<div class="bd">Aponte a câmera para o código e veja a lista completa, com preços, ou peça ao atendente.</div>
<div style="display:flex;justify-content:center;margin:7mm 0"><div style="background:#fff;padding:2.5mm;border-radius:2.5mm">{qr(40, INK, '#fff', 9)}</div></div>
<div style="background:{INK};border-radius:3mm;padding:5mm">
<div class="ov" style="color:{G2}">Dica da casa</div><div class="h3" style="margin-top:1.5mm">Meio a meio</div>
<div class="bd" style="color:{MUTE};margin-top:1mm">Portuguesa com Lombinho, 4 Queijos com Frango com Catupiry: dois sabores na mesma pizza.</div></div>
<div style="position:absolute;left:10mm;right:10mm;bottom:11mm" class="sm">Gostou? Poste e marque <b>{IG}</b> · {TAG}</div></div>'''

pA_dentro = f'''<section class="page">{a_in_1}{a_in_2}{a_in_3}<div class="fold" style="left:99mm"></div><div class="fold" style="left:198mm"></div></section>'''

# ============ 4 e 5. PROPOSTA B · REDONDO (Ø 190 mm) ============
D = 190


def round_page(inner, label, n):
    return f'''<section class="page paper"><div style="position:absolute;left:{(297 - D) / 2}mm;top:{(210 - D) / 2}mm;width:{D}mm;height:{D}mm">{inner}</div>
<div style="position:absolute;left:{(297 - D) / 2 - 2}mm;top:{(210 - D) / 2 - 2}mm;width:{D + 4}mm;height:{D + 4}mm;border-radius:50%;border:.3pt dashed #999"></div>
<div style="position:absolute;left:12mm;top:12mm;width:40mm" class="sm"><div class="ov" style="color:{G}">Proposta B</div><div class="h3" style="color:{INK};margin-top:1mm">{label}</div>
<div style="color:#666;margin-top:1.5mm">Cardápio redondo, Ø 19 cm. Linha tracejada: corte.</div></div></section>'''


b_frente = f'''<div style="width:{D}mm;height:{D}mm;border-radius:50%;overflow:hidden;position:relative;background:{INK}">
<img src="img/q4-foto3.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 50%,rgba(14,16,15,.25) 0,rgba(14,16,15,.55) 45%,rgba(14,16,15,.92) 72%)"></div>
<div style="position:absolute;inset:7mm;border-radius:50%;border:.6mm solid {G2}"></div>
<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:92mm;height:92mm;border-radius:50%;background:{INK};display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;box-shadow:0 0 0 1.2mm {G}">
{LOGO_SVG.format(w=20, h=14.8, c='#fff')}
<div class="d1" style="font-size:30pt;margin-top:3mm;letter-spacing:.5px">SPECIALE</div><div style="font-size:6pt;letter-spacing:3.4px;font-weight:600;margin-top:1mm">PIZZAS ARTESANAIS</div>
<div style="width:10mm;height:.6mm;background:{G2};margin:4mm 0 3mm"></div>
<div class="ov" style="color:{G2}">Forno a lenha</div></div>
<div style="position:absolute;left:50%;bottom:16mm;transform:translateX(-50%);text-align:center;color:#fff">
<div class="ov" style="color:{G2};margin-bottom:1.5mm">Vire a pizza</div>
<div style="background:{G};font-size:7pt;font-weight:600;padding:1.4mm 5mm;border-radius:20mm;white-space:nowrap">Poste e marque {IG} · {TAG}</div></div></div>'''


def b_verso_svg():
    cx = cy = D / 2
    R = D / 2
    s = f'<svg width="{D}mm" height="{D}mm" viewBox="0 0 {D} {D}"><defs><clipPath id="disc"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath>'
    for i in range(4):
        s += f'<clipPath id="p{i}"><circle cx="0" cy="0" r="14"/></clipPath>'
    s += f'</defs><g clip-path="url(#disc)"><rect width="{D}" height="{D}" fill="{INK}"/>'
    for i in range(4):
        a1, a2 = i * 90 - 45, (i + 1) * 90 - 45
        p1 = (cx + R * 1.6 * math.sin(math.radians(a1)), cy - R * 1.6 * math.cos(math.radians(a1)))
        p2 = (cx + R * 1.6 * math.sin(math.radians(a2)), cy - R * 1.6 * math.cos(math.radians(a2)))
        s += f'<path d="M{cx},{cy} L{p1[0]:.2f},{p1[1]:.2f} L{p2[0]:.2f},{p2[1]:.2f} Z" fill="{INK if i % 2 == 0 else "#15241a"}"/>'
        s += f'<line x1="{cx}" y1="{cy}" x2="{p1[0]:.2f}" y2="{p1[1]:.2f}" stroke="{G}" stroke-width=".9"/>'
    s += f'</g><circle cx="{cx}" cy="{cy}" r="{R - 4}" fill="none" stroke="{G2}" stroke-width=".5"/>'
    pos = [(cx, cy - R * .81, cx, cy - R * .64), (cx + R * .66, cy - 23, cx + R * .66, cy - 5),
           (cx, cy + R * .87, cx, cy + R * .335), (cx - R * .66, cy - 23, cx - R * .66, cy - 5)]
    for i, ((t, d, f, a), (fx, fy, tx, ty)) in enumerate(zip(SAB, pos)):
        s += f'<g transform="translate({fx:.2f},{fy:.2f})"><circle r="15.3" fill="{G}"/><image href="img/{f}.jpg" x="-14" y="-14" width="28" height="28" preserveAspectRatio="xMidYMid slice" clip-path="url(#p{i})"/></g>'
        s += (f'<foreignObject x="{tx - 21:.2f}" y="{ty:.2f}" width="42" height="32"><div xmlns="http://www.w3.org/1999/xhtml" style="color:#fff;text-align:center;font-family:Poppins;padding-top:1px">'
              f'<div style="font-family:Roboto Condensed;font-weight:700;font-size:5.2px;text-transform:uppercase;letter-spacing:.2px;line-height:1.05">{t}</div>'
              f'<div style="font-size:2.85px;color:{MUTE};line-height:1.32;margin-top:1px">{d}</div>'
              f'<div style="font-size:2.9px;color:{G2};margin-top:1.4px;letter-spacing:.4px">' + ' · '.join(ALG[c].upper() for c in a) + '</div></div></foreignObject>')
    s += f'<circle cx="{cx}" cy="{cy}" r="29" fill="{OW}"/><circle cx="{cx}" cy="{cy}" r="29" fill="none" stroke="{G}" stroke-width="1.4"/>'
    s += (f'<foreignObject x="{cx - 21}" y="{cy - 18}" width="42" height="36"><div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center;font-family:Poppins;color:{INK}">'
          f'<div style="font-size:2.6px;letter-spacing:1px;font-weight:700;color:{G}">TODOS OS SABORES</div>'
          + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:1.2px 3px;border-bottom:.2px solid #cfcabf"><span style="font-family:Roboto Condensed;font-weight:700;font-size:4px;text-transform:uppercase">{n} <span style="font-family:Poppins;font-weight:400;font-size:2.5px;color:#666;text-transform:none">{fa} fatias</span></span><span style="font-family:Roboto Condensed;font-weight:800;font-size:5.4px"><span style="font-size:2.6px">R$</span>{p}</span></div>' for n, fa, _, p in PRECO)
          + f'<div style="font-size:2.3px;color:#666;margin-top:1.4px">Bebidas no QR Code</div></div></foreignObject>')
    return s + '</svg>'


pB_frente = round_page(b_frente, 'Frente · capa', 4)
pB_verso = round_page(b_verso_svg(), 'Verso · sabores e preços', 5)

# ============ 6. PEÇAS DE APOIO ============
cartao_f = f'''<div class="pn" style="left:0;background:{INK};color:#fff">
<div style="position:relative">{logo(10)}</div>
<div class="ov" style="color:{G2};margin-top:10mm">Acompanha o cardápio redondo</div>
<div class="h2" style="margin-top:1.5mm;color:{G2}">Tamanhos</div><div class="rule"></div>
<div style="border:.5pt solid #2d332f;border-radius:3mm;padding:4mm 3mm 2.5mm">{sizes_svg(73)}</div>
<div style="margin-top:4mm">{price_row('#fff', G2, 16)}</div>
<div class="h2" style="margin-top:9mm;color:{G2}">Bebidas e sobremesas</div><div class="rule"></div>
<div style="display:flex;gap:4mm;align-items:center"><div style="background:#fff;padding:1.2mm;border-radius:1.5mm">{qr(22, INK, '#fff', 5)}</div>
<div class="bd" style="color:{MUTE}">Lista completa e preços no QR Code ou com o atendente.</div></div>
<div style="position:absolute;left:10mm;right:10mm;bottom:11mm;display:flex;gap:4mm" class="sm"><span>{alg('G', G2)} Glúten</span><span>{alg('L', G2)} Leite</span><span>{alg('O', G2)} Ovo</span></div></div>'''

display = f'''<div class="pn" style="left:99mm;background:{G};color:#fff;text-align:center;padding-top:16mm">
<div class="ov" style="color:#dff0d6">Display de mesa</div>
<div class="d1" style="font-size:31pt;margin-top:4mm">Você está<br>na Speciale.</div>
<div class="bd" style="margin:4mm auto 0;max-width:70mm">Poste a sua pizza, marque <b>{IG}</b> e a localização da casa.</div>
<div style="display:inline-block;background:#fff;padding:2.5mm;border-radius:2.5mm;margin-top:8mm">{qr(42, INK, '#fff', 13)}</div>
<div class="sm" style="margin-top:2mm">Cardápio, bebidas e pedidos pelo WhatsApp</div>
<div style="position:absolute;left:10mm;right:10mm;bottom:12mm"><div class="price" style="font-size:16pt">{TAG}</div></div></div>'''

story = f'''<div class="pn" style="left:198mm;background:#d9d6cf;padding:9mm 12mm;display:flex;flex-direction:column;align-items:center">
<div class="ov" style="color:{INK}">Moldura para stories</div>
<div style="width:62mm;height:110mm;border-radius:4mm;overflow:hidden;position:relative;margin-top:3mm;box-shadow:0 2mm 5mm rgba(0,0,0,.25);background:{INK}">
<img src="img/lombo-foto2.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
<div style="position:absolute;inset:0;border:2.2mm solid {INK}"></div>
<div style="position:absolute;left:0;right:0;top:0;background:{INK};padding:3mm 4mm 2.5mm;color:#fff;display:flex;justify-content:space-between;align-items:center">{logo(6)}<span class="ov" style="color:{G2};font-size:4.6pt;letter-spacing:1px">Recife</span></div>
<div style="position:absolute;left:4mm;bottom:5mm;background:{G};color:#fff;padding:1.6mm 3mm;border-radius:1.5mm;transform:rotate(-3deg)"><div class="h3" style="font-size:9pt">Estou na Speciale</div></div>
<div style="position:absolute;right:4mm;bottom:5mm;color:#fff;font-size:5.6pt;font-weight:600">{IG}</div></div>
<div class="sm" style="color:#444;margin-top:4mm;text-align:center;max-width:70mm">Arte para a casa repostar fotos dos clientes e para virar figurinha (GIF) no Instagram.</div></div>'''

pApoio = f'''<section class="page">{cartao_f}{display}{story}<div class="fold" style="left:99mm"></div><div class="fold" style="left:198mm"></div></section>'''

# ============ 7. GUIA DE ESTILO ============
def sw(c, n, tc):
    return f'<div><div style="height:22mm;border-radius:2mm;background:{c};border:.3pt solid #ccc"></div><div class="sm" style="margin-top:1.5mm;color:{tc}"><b>{n}</b><br>{c.upper()}</div></div>'


guia = f'''<section class="page" style="background:{OW};color:{INK};padding:16mm 20mm">
<div class="ov" style="color:{G}">Padrão visual do cardápio</div><div class="h2" style="font-size:24pt;margin-top:2mm">Hierarquia e regras</div><div class="rule"></div>
<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:14mm">
<div><div class="ov" style="color:#777;margin-bottom:3mm">Tipografia, do maior para o menor</div>
<div style="border-top:.5pt solid #cfcabf;padding:3mm 0;display:grid;grid-template-columns:30mm 1fr;align-items:baseline"><span class="sm" style="color:#777">Título de capa</span><span class="d1" style="font-size:26pt">Saiu do forno</span></div>
<div style="border-top:.5pt solid #cfcabf;padding:3mm 0;display:grid;grid-template-columns:30mm 1fr;align-items:baseline"><span class="sm" style="color:#777">Seção</span><span class="h2">Pizzas</span></div>
<div style="border-top:.5pt solid #cfcabf;padding:3mm 0;display:grid;grid-template-columns:30mm 1fr;align-items:baseline"><span class="sm" style="color:#777">Nome do sabor</span><span class="h3">Frango com Catupiry</span></div>
<div style="border-top:.5pt solid #cfcabf;padding:3mm 0;display:grid;grid-template-columns:30mm 1fr;align-items:baseline"><span class="sm" style="color:#777">Ingredientes</span><span class="bd">Frango desfiado, muçarela, catupiry, azeitona preta e orégano.</span></div>
<div style="border-top:.5pt solid #cfcabf;padding:3mm 0;display:grid;grid-template-columns:30mm 1fr;align-items:baseline"><span class="sm" style="color:#777">Preço</span><span class="price" style="font-size:20pt"><sup>R$</sup>45</span></div>
<div style="border-top:.5pt solid #cfcabf;border-bottom:.5pt solid #cfcabf;padding:3mm 0;display:grid;grid-template-columns:30mm 1fr;align-items:baseline"><span class="sm" style="color:#777">Apoio</span><span class="ov" style="color:{G}">Forno a lenha · massa da casa</span></div>
<div class="sm" style="color:#555;margin-top:3mm">Títulos e nomes: Roboto Condensed. Textos e informações: Poppins.</div></div>
<div><div class="ov" style="color:#777;margin-bottom:3mm">Cores</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:3mm">{sw(INK, 'Carvão', INK)}{sw(G, 'Manjericão', INK)}{sw(G2, 'Folha', INK)}{sw(OW, 'Farinha', INK)}</div>
<div class="ov" style="color:#777;margin:8mm 0 3mm">Regras para a experiência do cliente</div>
<ul class="bd" style="padding-left:4mm;line-height:1.75">
<li>Preço uma vez só, por tamanho: o cliente compara num olhar.</li>
<li>Pedido em 3 passos: tamanho, sabor e complemento.</li>
<li>Foto real em todo sabor, sempre em círculo.</li>
<li>Alérgenos com ícones, sempre no mesmo lugar.</li>
<li>Toda peça tem o perfil, a hashtag e o QR Code.</li></ul></div></div>
</section>'''

pages = [capa, pA_fora, pA_dentro, pB_frente, pB_verso, pApoio, guia]
open('cardapio_final.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Cardápio Speciale</title>{CSS}</head><body>{"".join(pages)}</body></html>')
