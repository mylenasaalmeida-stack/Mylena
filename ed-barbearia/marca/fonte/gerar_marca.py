# Rebrand ED Barbearia: duas direções de logo + paleta, em vetor.
# Gerar: python3 gerar_marca.py && node render_marca.js
import os

Y, K, W, G = '#FFC629', '#111111', '#F5F3EE', '#8A8F96'

FONTS = '''
@font-face{font-family:Anton;src:url('fonts/Anton.ttf')}
@font-face{font-family:ArchivoBlack;src:url('fonts/ArchivoBlack.ttf')}
@font-face{font-family:Poppins;font-weight:400;src:url('../../../fonte/fonts/Poppins-400.woff2')}
@font-face{font-family:Poppins;font-weight:600;src:url('../../../fonte/fonts/Poppins-600.woff2')}
@font-face{font-family:Poppins;font-weight:700;src:url('../../../fonte/fonts/Poppins-700.woff2')}
'''


# ---------- elementos ----------
def navalha(x, y, s, cor, fundo):
    """Navalha aberta na horizontal. (x,y) = centro do pivô, s = escala (comprimento ~170*s)."""
    return f'''<g transform="translate({x},{y}) scale({s})">
<rect x="-92" y="-8" width="96" height="16" rx="8" fill="{cor}"/>
<circle cx="-78" cy="0" r="2.6" fill="{fundo}"/><circle cx="-12" cy="0" r="2.6" fill="{fundo}"/>
<path d="M2 -9 L74 -9 Q84 -9 84 1 Q84 13 70 15 Q40 17 6 9 Z" fill="{cor}"/>
<circle cx="2" cy="0" r="6" fill="{cor}" stroke="{fundo}" stroke-width="2.5"/>
</g>'''


def ed_cortado(cx, base, size, cor, fundo, uid, ang=-8, gap=None):
    """'ED' em Anton cortado por uma linha de navalha em diagonal.
    A metade de cima desliza ao longo do corte, como se a lâmina tivesse passado."""
    gap = gap if gap is not None else size * 0.03
    cy = base - size * 0.25
    big = size * 3
    shift = size * 0.018
    txt = f'<text x="{cx}" y="{base}" text-anchor="middle" font-family="Anton" font-size="{size}" fill="{cor}" letter-spacing="{-size * 0.01}">ED</text>'
    return f'''<defs>
<clipPath id="t{uid}"><rect x="{cx - big}" y="{cy - big}" width="{2 * big}" height="{big - gap / 2}" transform="rotate({ang} {cx} {cy})"/></clipPath>
<clipPath id="b{uid}"><rect x="{cx - big}" y="{cy + gap / 2}" width="{2 * big}" height="{big}" transform="rotate({ang} {cx} {cy})"/></clipPath>
</defs>
<g clip-path="url(#b{uid})">{txt}</g>
<g clip-path="url(#t{uid})"><g transform="rotate({ang} {cx} {cy}) translate({-shift},0) rotate({-ang} {cx} {cy})">{txt}</g></g>'''


def spaced(x, y, txt, size, cor, ls=0.32, fam='ArchivoBlack', anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{fam}" font-size="{size}" fill="{cor}" letter-spacing="{size * ls}">{txt}</text>'


# ---------- direção A: O Corte ----------
def a_principal(cor=K, fundo=Y, uid='a1', sub=True):
    s = f'<rect width="400" height="400" fill="{fundo}"/>' + ed_cortado(200, 262, 236, cor, fundo, uid)
    if sub:
        s += spaced(205, 318, 'BARBEARIA', 27, cor)
    return f'<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">{s}</svg>'


def a_perfil(uid='ap', cor=K, fundo=Y):
    return (f'<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg"><circle cx="200" cy="200" r="200" fill="{fundo}"/>'
            + ed_cortado(200, 274, 236, cor, fundo, uid) + spaced(206, 324, 'BARBEARIA', 24, cor) + '</svg>')


def a_horizontal(cor=K, fundo=Y, uid='ah', alt=None):
    t = alt or cor
    return (f'<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg"><rect width="760" height="220" fill="{fundo}"/>'
            + ed_cortado(150, 182, 172, cor, fundo, uid)
            + f'<rect x="282" y="48" width="5" height="124" fill="{cor}"/>'
            + spaced(312, 112, 'BARBEARIA', 50, t, ls=0.12, anchor='start')
            + spaced(314, 160, 'CASA AMARELA · RECIFE', 22, t, ls=0.26, fam='ArchivoBlack', anchor='start') + '</svg>')


# ---------- direção B: Selo clássico ----------
def b_selo(uid='b1', anel=Y, miolo=K, texto=Y, size=400):
    import math
    r_txt = 160
    return f'''<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
<defs><path id="arcT{uid}" d="M {200 - r_txt} 200 A {r_txt} {r_txt} 0 0 1 {200 + r_txt} 200"/>
<path id="arcB{uid}" d="M {200 - 178} 200 A 178 178 0 0 0 {200 + 178} 200"/></defs>
<circle cx="200" cy="200" r="200" fill="{anel}"/>
<circle cx="200" cy="200" r="142" fill="{miolo}"/>
<text font-family="ArchivoBlack" font-size="27" fill="{miolo}" letter-spacing="7"><textPath href="#arcT{uid}" startOffset="50%" text-anchor="middle">BARBEARIA</textPath></text>
<text font-family="ArchivoBlack" font-size="20" fill="{miolo}" letter-spacing="5"><textPath href="#arcB{uid}" startOffset="50%" text-anchor="middle">CASA AMARELA · RECIFE</textPath></text>
<circle cx="38" cy="200" r="5" fill="{miolo}"/><circle cx="362" cy="200" r="5" fill="{miolo}"/>
{navalha(205, 128, 0.95, texto, miolo)}
<text x="200" y="285" text-anchor="middle" font-family="Anton" font-size="150" fill="{texto}">ED</text>
<rect x="150" y="300" width="100" height="4" fill="{texto}"/>
</svg>'''


def b_horizontal(cor=K, fundo=Y, uid='bh'):
    return (f'<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg"><rect width="760" height="220" fill="{fundo}"/>'
            + f'<g transform="translate(20,10) scale(0.5)">{b_selo(uid, anel=cor, miolo=fundo, texto=cor)[len("<svg viewBox=\"0 0 400 400\" xmlns=\"http://www.w3.org/2000/svg\">"):-6]}</g>'
            + spaced(250, 118, 'ED BARBEARIA', 56, cor, ls=0.06, fam='Anton', anchor='start')
            + spaced(252, 160, 'CASA AMARELA · RECIFE', 18, cor, ls=0.2, anchor='start') + '</svg>')


# ---------- logo atual (pra comparar) ----------
ATUAL = '<img src="img/logo-atual.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:50%">'

# ---------- página ----------
CSS = FONTS + f'''
@page{{size:1389px 781px;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0b0b0b;color:{W};font-family:Poppins,sans-serif;font-size:14px;line-height:1.45}}
.s{{width:1389px;height:781px;padding:46px 70px;position:relative;overflow:hidden;page-break-after:always;background:#0b0b0b}}
.s.y{{background:{Y};color:{K}}}
.ey{{font-size:11px;letter-spacing:.24em;font-weight:700;color:{Y};text-transform:uppercase}}
.s.y .ey{{color:{K}}}
h1{{font-family:Anton;font-weight:400;font-size:64px;line-height:1;text-transform:uppercase;margin:16px 0 10px;letter-spacing:.005em}}
.am{{color:{Y}}}
.sub{{color:#a3a09a;font-size:15px;max-width:720px}}
.s.y .sub{{color:#3b3108}}
.row{{display:flex;gap:22px;align-items:flex-start}}
.box{{border-radius:16px;overflow:hidden;background:#181818}}
.box svg{{display:block;width:100%;height:auto}}
.lab{{font-size:10.5px;letter-spacing:.18em;font-weight:700;color:#8a877f;text-transform:uppercase;margin-top:9px}}
.card{{background:#181818;border-radius:16px;padding:18px 22px}}
.card h4{{font-size:15px;margin-bottom:6px}}
.card p,.card li{{font-size:13px;color:#b3b0a8}}
ul{{list-style:none}} li{{padding-left:16px;position:relative;margin-bottom:5px}}
li:before{{content:'';position:absolute;left:2px;top:7px;width:6px;height:6px;border-radius:50%;background:{Y}}}
.foot{{position:absolute;left:70px;right:70px;bottom:22px;display:flex;justify-content:space-between;font-size:9.5px;letter-spacing:.2em;font-weight:700;color:#555}}
.s.y .foot{{color:#6b5a14}}
.circ{{border-radius:50%;overflow:hidden;flex:none}}
.circ svg{{display:block;width:100%;height:100%}}
.ig{{background:#000;border-radius:18px;padding:18px 20px;width:360px;color:#fff;font-size:12px}}
.ig .u{{display:flex;gap:16px;align-items:center}}
.ig b{{font-size:13px}}
.sw{{border-radius:14px;height:150px;padding:14px;display:flex;flex-direction:column;justify-content:flex-end;font-size:12px}}
'''

slides = []


def S(ey, body, cls=''):
    slides.append((ey, body, cls))


def box(svg, w, lab='', bg='#181818'):
    return f'<div style="width:{w}px"><div class="box" style="background:{bg}">{svg}</div>{f"<div class=lab>{lab}</div>" if lab else ""}</div>'


def circ(svg, d):
    return f'<div class="circ" style="width:{d}px;height:{d}px">{svg}</div>'


def ig_mock(svg_perfil, nome='edbarbearia'):
    return f'''<div class="ig"><div class="u">{circ(svg_perfil, 86)}
<div style="display:flex;gap:22px;text-align:center"><div><b>296</b><br>posts</div><div><b>3.199</b><br>seguidores</div><div><b>812</b><br>seguindo</div></div></div>
<div style="margin-top:10px"><b>ED Barbearia | Casa Amarela, Recife</b><br>✂️ Degradê, barba, kids e salão feminino<br>🗓️ Seg a sáb, 9h às 19h<br>🎟️ 50% no 1º corte de seg a qua, pelo app<br>👇 Agende pelo link</div></div>'''


# 1 capa
S('ED Barbearia · rebrand · novembro 2026', f'''
<div class="row" style="align-items:center;gap:60px;margin-top:40px">
<div style="flex:1"><h1 style="font-size:96px">Marca nova<br><span class="am">da ED.</span></h1>
<p class="sub" style="font-size:17px;margin-top:20px">Duas direções em preto e amarelo vivo, o mesmo amarelo dos posts. As duas foram feitas pra ler bem na bolinha do perfil, que é onde a maioria vê a marca pela primeira vez.</p>
<p class="sub" style="margin-top:22px"><b style="color:{Y}">A · O Corte</b>: o ED cortado por uma navalha. Moderna, simples, recomendada.<br><b style="color:{Y}">B · Selo clássico</b>: selo de barbearia com navalha. Mais tradicional.</p></div>
{box(a_perfil('c1'), 440, '', 'transparent')}
</div>''')

# 2 por que mudar
S('Por que mudar', f'''<h1>A marca atual <span class="am">não é da ED.</span></h1>
<p class="sub">O barbudo de óculos é um desenho de banco de imagens: o mesmo personagem aparece em centenas de barbearias. E ele não conversa com o feed novo.</p>
<div class="row" style="margin-top:34px;gap:34px">
<div style="width:230px">{circ(ATUAL, 230)}<div class="lab" style="text-align:center">marca atual</div></div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px">
<div class="card"><h4>Genérica</h4><p>Personagem pronto, comum em barbearias do Brasil inteiro. Não diz nada sobre a ED nem sobre o Ed.</p></div>
<div class="card"><h4>Não lê pequeno</h4><p>Na bolinha do perfil (40 px no feed), o rosto vira uma mancha e o nome “ED BARBEARIA” some.</p></div>
<div class="card"><h4>Destoa do feed</h4><p>As artes novas são amarelo vivo e preto, com título grosso. O logo é cinza, com bordinha ondulada e fonte de outro estilo.</p></div>
<div class="card"><h4>O que a marca nova precisa</h4><p>Ser da ED, ler em 40 px, usar o amarelo dos posts e funcionar no avental, na parede e no story.</p></div>
</div></div>''')

# 3 paleta
sw = [(Y, K, 'Amarelo ED', '#FFC629', 'Fundo de post, destaque, preço, botão, logo'),
      (K, W, 'Preto', '#111111', 'Fundo, texto sobre o amarelo, logo'),
      (W, K, 'Branco', '#F5F3EE', 'Texto sobre o preto, papel impresso'),
      (G, K, 'Cinza aço', '#8A8F96', 'Legendas e linhas, sempre em pouca quantidade')]
swh = ''.join(f'<div class="sw" style="background:{a};color:{b};{"border:1px solid #2a2a2a" if a == K else ""}"><b style="font-size:16px">{n}</b>{h} · {r}</div>' for a, b, n, h, r in sw)
S('Cores e letras', f'''<h1>Amarelo vivo <span class="am">e preto.</span></h1>
<p class="sub">Um amarelo só pra tudo: post, story, destaque, logo, avental e fachada. É o mesmo das artes de novembro.</p>
<div style="display:grid;grid-template-columns:1.6fr 1.2fr 1fr .7fr;gap:12px;margin-top:26px">{swh}</div>
<div class="row" style="margin-top:22px;gap:14px">
<div class="card" style="flex:1"><h4>Regra de uso</h4><ul><li>Amarelo e preto juntos sempre. Branco só como apoio.</li><li>Texto preto em cima do amarelo. Nunca branco em cima do amarelo (não dá pra ler).</li><li>Nada de dourado, degradê de cor ou sombra no logo.</li></ul></div>
<div class="card" style="flex:1"><h4>Letras</h4><p><span style="font-family:Anton;font-size:30px;color:{W};line-height:1.1">ANTON · TÍTULOS E LOGO</span><br>A mesma letra grossa dos títulos das artes.<br><span style="font-family:ArchivoBlack;font-size:18px;color:{W}">ARCHIVO BLACK · APOIO DO LOGO</span><br>Textos corridos continuam com a fonte atual das artes.</p></div>
</div>''')

# 4 direção A
S('Direção A · O Corte · recomendada', f'''<h1>O <span class="am">corte</span> é a marca.</h1>
<p class="sub">O “ED” grosso, cortado na diagonal como se a navalha tivesse acabado de passar. É simples, lê em qualquer tamanho e é só da ED.</p>
<div class="row" style="margin-top:22px;gap:18px">
{box(a_principal(K, Y, 'a2'), 300, 'principal · preto no amarelo')}
{box(a_principal(Y, K, 'a3'), 300, 'invertida · amarelo no preto')}
<div style="flex:1;display:flex;flex-direction:column;gap:18px">
{box(a_horizontal(K, Y, 'a4'), 420, 'horizontal · fachada, cartão, rodapé')}
{box(a_horizontal(Y, K, 'a5', alt=W), 420, 'horizontal no preto')}
</div></div>''')

# 5 direção A aplicada
post = f'''<div style="width:250px;height:312px;border-radius:12px;background:{Y};position:relative;overflow:hidden;color:{K};padding:16px">
<div style="width:46px">{a_principal(K, Y, 'a7', sub=False)}</div>
<div style="font-family:Anton;font-size:52px;line-height:.95;margin-top:16px">SEG A QUA</div>
<div style="font-family:Anton;font-size:64px;line-height:1;margin-top:10px">50%</div><div style="font-weight:700;font-size:13px">no seu primeiro corte</div>
<div style="position:absolute;bottom:16px;left:16px;background:{K};color:{Y};font-size:10px;font-weight:700;padding:5px 10px;border-radius:20px">Agende pelo link da bio</div></div>'''
avental = f'''<div style="width:230px;height:312px;border-radius:12px;background:#1b1b1b;position:relative;display:flex;align-items:center;justify-content:center">
<div style="position:absolute;top:0;left:40px;width:16px;height:70px;background:#2a2a2a"></div><div style="position:absolute;top:0;right:40px;width:16px;height:70px;background:#2a2a2a"></div>
<div style="width:120px">{a_principal(Y, '#1b1b1b', 'a8')}</div><div class="lab" style="position:absolute;bottom:8px">avental · bordado amarelo</div></div>'''
S('Direção A · aplicada', f'''<h1>No perfil, no post <span class="am">e no avental.</span></h1>
<div class="row" style="margin-top:26px;gap:24px">
<div>{ig_mock(a_perfil('a6'))}
<div class="row" style="margin-top:18px;gap:14px;align-items:center">{circ(a_perfil('a9'), 56)}{circ(a_perfil('a10'), 40)}{circ(a_perfil('a11'), 28)}<span class="lab" style="margin:0">tamanhos reais do Instagram</span></div></div>
<div>{post}<div class="lab">logo no canto do post</div></div>
<div>{avental}</div>
</div>''')

# 6 direção B
S('Direção B · Selo clássico', f'''<h1>Selo de <span class="am">barbearia.</span></h1>
<p class="sub">Selo redondo com a navalha em cima do “ED”, e o nome e o bairro em volta. Lembra barbearia tradicional e fica bonito bordado e na parede. Perde um pouco de leitura no tamanho bem pequeno.</p>
<div class="row" style="margin-top:22px;gap:18px">
{box(b_selo('b2'), 300, 'principal · selo amarelo', 'transparent')}
{box(b_selo('b3', anel=K, miolo=Y, texto=K), 300, 'invertida · selo preto', 'transparent')}
<div style="flex:1;display:flex;flex-direction:column;gap:18px">
{box(b_horizontal(K, Y, 'b4'), 420, 'horizontal · fachada, cartão, rodapé')}
{box(b_horizontal(Y, K, 'b5'), 420, 'horizontal no preto')}
</div></div>''')

# 7 comparação
def trio(svg_fn, nome):
    return (f'<div class="card" style="flex:1"><h4>{nome}</h4><div class="row" style="align-items:center;gap:16px;margin-top:10px">'
            + circ(svg_fn('x1'), 150) + circ(svg_fn('x2'), 56) + circ(svg_fn('x3'), 40) + '</div></div>')


S('Lado a lado', f'''<h1>Do tamanho que <span class="am">o cliente vê.</span></h1>
<p class="sub">O perfil aparece com uns 40 px no feed e nos stories. É nesse tamanho que a marca tem que funcionar.</p>
<div class="row" style="margin-top:26px;gap:14px">
<div class="card" style="flex:1"><h4>Atual</h4><div class="row" style="align-items:center;gap:16px;margin-top:10px">{circ(ATUAL, 150)}{circ(ATUAL, 56)}{circ(ATUAL, 40)}</div></div>
{trio(lambda u: a_perfil('ca' + u), 'A · O Corte')}
{trio(lambda u: b_selo('cb' + u), 'B · Selo clássico')}
</div>
<div class="card" style="margin-top:16px"><h4>Recomendação: A</h4><p>É a única que continua legível em 40 px, é original (não existe outra barbearia com esse ED cortado) e conversa direto com as artes, que já usam a mesma letra e o mesmo amarelo. O selo B pode virar o bordado do avental e o adesivo da vitrine, se o Ed gostar dele.</p></div>''')

# 8 próximos passos
S('Próximos passos', f'''<h1>Escolheu, <span>a gente troca.</span></h1>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px">
{''.join(f'<div class="card" style="min-height:190px;background:{K};color:{W}"><div style="font-family:Anton;font-size:40px;color:{Y}">{a}</div><h4 style="margin:6px 0">{b}</h4><p>{c}</p></div>' for a, b, c in [
    ('01', 'O Ed escolhe', 'A, B ou ajustes. Aprovação até 08/11 pra o perfil novo estrear com a marca nova em 09/11.'),
    ('02', 'Digital primeiro', 'Foto de perfil, logo nas artes, capas de destaque e stories. Custo zero.'),
    ('03', 'Físico depois', 'Avental, capa, parede e fachada mudam com calma, quando for repor. Nada precisa ser jogado fora agora.'),
    ('04', 'Arquivos finais', 'PNG e PDF em vetor pra gráfica, bordado e adesivo.')])}
</div>
<p style="margin-top:22px;font-size:14px">Todas as versões em PNG estão na pasta <b>marca/png</b>.</p>''', 'y')

html = ''
for i, (ey, body, cls) in enumerate(slides):
    foot = f'<div class="foot"><span>ED BARBEARIA × HOUSE DO CREATOR</span><span>{i + 1:02d}</span></div>'
    html += f'<section class="s {cls}"><div class="ey">{ey}</div>{body}{foot}</section>'
open('marca.html', 'w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>ED Barbearia · Marca nova</title><style>{CSS}</style></head><body>{html}</body></html>')

# arquivos soltos pra exportar em PNG
exp = {
    'A-perfil-instagram': a_perfil('e1'),
    'A-principal-amarelo': a_principal(K, Y, 'e2'),
    'A-principal-preto': a_principal(Y, K, 'e3'),
    'A-horizontal-amarelo': a_horizontal(K, Y, 'e4'),
    'A-horizontal-preto': a_horizontal(Y, K, 'e5', alt=W),
    'B-selo-amarelo': b_selo('e6'),
    'B-selo-preto': b_selo('e7', anel=K, miolo=Y, texto=K),
    'B-horizontal-amarelo': b_horizontal(K, Y, 'e8'),
}
os.makedirs('exp', exist_ok=True)
for n, svg in exp.items():
    open(f'exp/{n}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FONTS.replace("fonts/", "../fonts/").replace("../../../fonte", "../../../../fonte")} body{{margin:0;background:transparent}} svg{{display:block;width:100%;height:auto}}</style></head><body>{svg}</body></html>')
print(len(slides), 'slides,', len(exp), 'exportações')
