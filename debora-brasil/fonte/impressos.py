"""Artes de impressão da Débora Brasil Beauty: bandeira vela (wind banner) e painel da porta.
Gera HTML em tamanho real (mm) para virar PDF vetorial. Uso: python3 impressos.py && node render_impressos.js"""
import os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
WHATS = '(81) 9 0000-0000'          # TROCAR pelo WhatsApp da Débora
INSTA = '@deborabrasilbeauty'


def svg(nome, cor, extra=''):
    s = open(os.path.join(AQUI, 'vetor', nome + '.svg')).read()
    return s.replace('<svg ', f'<svg style="color:{cor}" {extra} ', 1)


FONTES = '''
@font-face{font-family:'Gilda';src:url(fonts/Gilda.woff) format('woff')}
@font-face{font-family:'Garamond';font-style:italic;src:url(fonts/EBG-i.woff) format('woff')}
@font-face{font-family:'Jost';font-weight:400;src:url(fonts/Jost-1.woff) format('woff')}
@font-face{font-family:'Jost';font-weight:500 600;src:url(fonts/Jost-2.woff) format('woff')}
:root{--creme:#F5EFE8;--malva:#9A7070;--rose:#D8BCBC;--tinta:#3E2C2C}
*{box-sizing:border-box;margin:0;padding:0}
body{-webkit-print-color-adjust:exact;print-color-adjust:exact}
'''

# ---------------- BANDEIRA VELA · tecido 750 x 2500 mm (+ 20 mm de sangria) ----------------
W, H, S = 750, 2500, 20          # mm
VW, VH = W + 2 * S, H + 2 * S
# forma de vela: lado do mastro reto (esquerda), topo em curva descendo até a direita
VELA = (f'M0,0 L{S + 30},0 C{S + 470},0 {VW},{S + 260} {VW},{S + 760} '
        f'L{VW},{VH} L0,{VH} Z')

vela = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Bandeira vela · Débora Brasil</title><style>{FONTES}
@page{{size:{VW}mm {VH}mm;margin:0}}
body{{width:{VW}mm;height:{VH}mm;position:relative;overflow:hidden;background:#fff;font-family:'Jost',sans-serif}}
.forma{{position:absolute;inset:0;width:{VW}mm;height:{VH}mm}}
.c{{position:absolute;left:{S}mm;width:{W}mm}}
.lg{{top:{S + 300}mm;left:{S + 55}mm;width:400mm}}
.lg svg{{width:100%;height:auto;display:block}}
.faixa{{top:{S + 960}mm;height:1040mm;display:flex;align-items:center;justify-content:center}}
.faixa div{{writing-mode:vertical-rl;transform:rotate(180deg);color:var(--creme);text-align:center;white-space:nowrap}}
.faixa b{{font-family:'Gilda';font-weight:400;font-size:168mm;line-height:1.05;letter-spacing:2mm}}
.faixa i{{display:block;font-family:'Garamond';font-size:74mm;color:var(--rose);line-height:1.2}}
.zap{{top:{S + 2010}mm;left:{S + 45}mm;width:{W - 90}mm;background:var(--creme);border-radius:60mm;padding:26mm 0 28mm;text-align:center;color:var(--malva)}}
.zap small{{display:block;font-size:34mm;letter-spacing:5mm;text-transform:uppercase;font-weight:600}}
.zap b{{display:block;font-size:66mm;font-weight:600;color:var(--tinta);margin-top:6mm;letter-spacing:1mm}}
.end{{top:{S + 2260}mm;text-align:center;color:var(--creme);font-size:34mm;line-height:1.4}}
.end b{{display:block;font-family:'Garamond';font-style:italic;font-weight:400;font-size:56mm;color:#fff}}
.mastro{{position:absolute;left:0;top:0;bottom:0;width:{S + 60}mm;background:repeating-linear-gradient(0deg,transparent 0 40mm,rgba(0,0,0,.0) 40mm 80mm)}}
</style></head><body>
<svg class="forma" viewBox="0 0 {VW} {VH}" preserveAspectRatio="none">
  <defs><clipPath id="v"><path d="{VELA}"/></clipPath></defs>
  <g clip-path="url(#v)">
    <rect width="{VW}" height="{VH}" fill="#9A7070"/>
    <path d="M0,0 L{VW},0 L{VW},{S + 800} C{VW - 260},{S + 760} {S + 260},{S + 820} 0,{S + 920} Z" fill="#F5EFE8"/>
  </g>
</svg>
<div class="c lg">{svg('logo-circulo', '#9A7070')}</div>
<div class="c faixa"><div><b>Sobrancelhas</b><i>micropigmentação · brow · lash</i></div></div>
<div class="c zap"><small>Agende</small><b>{WHATS}</b></div>
<div class="c end"><b>Galeria Ponto Certo · Sala 7</b>{INSTA}</div>
</body></html>'''

# ---------------- PAINEL DA PORTA · 600 x 900 mm (+ 5 mm de sangria) ----------------
PW, PH, PS = 600, 900, 5
porta = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Painel da porta · Débora Brasil</title><style>{FONTES}
@page{{size:{PW + 2 * PS}mm {PH + 2 * PS}mm;margin:0}}
body{{width:{PW + 2 * PS}mm;height:{PH + 2 * PS}mm;background:var(--creme);font-family:'Jost',sans-serif;color:var(--malva);position:relative;overflow:hidden}}
.in{{position:absolute;left:{PS + 50}mm;right:{PS + 50}mm;top:{PS + 70}mm;bottom:{PS + 55}mm;display:flex;flex-direction:column;align-items:center;text-align:center}}
.fio{{position:absolute;inset:{PS + 22}mm;border:1.2mm solid var(--rose);border-radius:6mm}}
.lg svg{{width:420mm;height:auto;display:block}}
ul{{list-style:none;margin-top:62mm;font-size:24mm;letter-spacing:5mm;text-transform:uppercase;line-height:2.15;color:var(--tinta)}}
li:after{{content:'';display:block;width:40mm;height:.8mm;background:var(--rose);margin:0 auto}}
li:last-child:after{{display:none}}
.rd{{margin-top:auto;width:100%;border-top:1mm solid var(--rose);padding-top:22mm;font-size:20mm;line-height:1.7;color:var(--tinta)}}
.rd b{{color:var(--malva);font-weight:600}}
.rd i{{display:block;font-family:'Garamond';font-size:30mm;color:var(--malva);margin-bottom:6mm}}
</style></head><body>
<div class="fio"></div>
<div class="in">
  <div class="lg">{svg('logo-horizontal', '#9A7070')}</div>
  <ul><li>Design de sobrancelhas</li><li>Micropigmentação</li><li>Brow lamination</li><li>Lash lifting</li><li>Maquiagem</li></ul>
  <div class="rd"><i>Atendimento com hora marcada</i><b>9h às 18h</b> · {INSTA}<br>WhatsApp <b>{WHATS}</b></div>
</div>
</body></html>'''

open(os.path.join(AQUI, 'vela.html'), 'w', encoding='utf-8').write(vela)
open(os.path.join(AQUI, 'porta.html'), 'w', encoding='utf-8').write(porta)
print('ok')
