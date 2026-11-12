# 5 artes extras de feed (1080x1350) no padrão dos fixados, com a logo atual.
# Gerar: python3 gerar_feed_extra.py && node render_feed_extra.js
import sys
sys.path.insert(0, '../../fixados/fonte')
Y, K, W = '#FFC629', '#111111', '#F5F3EE'
FX = '../../fixados/fonte/'
FONTS = f'''
@font-face{{font-family:Anton;src:url('../../marca/fonte/fonts/Anton.ttf')}}
@font-face{{font-family:Poppins;font-weight:500;src:url('../../../fonte/fonts/Poppins-500.woff2')}}
@font-face{{font-family:Poppins;font-weight:600;src:url('../../../fonte/fonts/Poppins-600.woff2')}}
@font-face{{font-family:Poppins;font-weight:700;src:url('../../../fonte/fonts/Poppins-700.woff2')}}
'''
# margem lateral de 90 px: a grade do perfil (3:4) corta ~34 px de cada lado
CSS = FONTS + f'''
*{{box-sizing:border-box;margin:0;padding:0}}
.p{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif}}
.k{{background:{K};color:{W}}} .y{{background:{Y};color:{K}}} .w{{background:{W};color:{K}}}
.hd{{position:absolute;top:64px;left:90px;right:90px;display:flex;justify-content:space-between;align-items:center;z-index:5}}
.hd .l{{display:flex;align-items:center;gap:16px;font-weight:700;font-size:24px;letter-spacing:.2em}}
.hd img{{width:76px;height:76px;border-radius:50%;border:5px solid {K};background:#fff}}
.k .hd img{{border-color:{W}}}
.hd .t{{font-weight:700;font-size:22px;letter-spacing:.14em;text-transform:uppercase;padding:9px 18px;border-radius:30px}}
.k .hd .t{{background:{Y};color:{K}}} .y .hd .t,.w .hd .t{{background:{K};color:{Y}}}
.c{{position:absolute;left:90px;right:90px;top:210px}}
.big{{font-family:Anton;text-transform:uppercase;line-height:.92}}
.lab{{font-weight:700;font-size:26px;letter-spacing:.2em;text-transform:uppercase}}
.txt{{font-size:36px;font-weight:600;line-height:1.3}}
.am{{color:{Y}}}
.rod{{position:absolute;left:90px;right:90px;bottom:70px;display:flex;justify-content:space-between;align-items:center;z-index:5}}
.btn{{font-weight:700;font-size:28px;padding:16px 30px;border-radius:40px}}
.k .btn{{background:{Y};color:{K}}} .y .btn,.w .btn{{background:{K};color:{Y}}}
.end{{font-size:22px;font-weight:600;text-align:right;line-height:1.35;opacity:.75}}
.lin{{display:flex;justify-content:space-between;align-items:center;border-bottom:4px solid {K};padding:22px 0}}
.lin .n{{font-family:Anton;font-size:72px;text-transform:uppercase;line-height:1}}
.lin .n small{{display:block;font-family:Poppins;font-size:24px;font-weight:600;text-transform:none;margin-top:6px;opacity:.7}}
.lin .v{{font-family:Anton;font-size:96px;line-height:1;background:{K};color:{Y};padding:8px 22px;border-radius:18px}}
'''


def hd(tag):
    return f'<div class="hd"><div class="l"><img src="{FX}img/logo-antigo.png"><span>ED BARBEARIA</span></div><div class="t">{tag}</div></div>'


def rod(btn='Agende pelo link da bio'):
    return f'<div class="rod"><div class="btn">{btn}</div><div class="end">Rua Paula Batista, 604<br>Seg a sáb, 9h às 19h</div></div>'


def navalha(cor, fundo, w):
    return f'''<svg viewBox="-100 -20 200 40" style="width:{w}px;display:block"><g transform="scale(1.15)">
<rect x="-92" y="-8" width="96" height="16" rx="8" fill="{cor}"/><circle cx="-78" cy="0" r="2.6" fill="{fundo}"/><circle cx="-12" cy="0" r="2.6" fill="{fundo}"/>
<path d="M2 -9 L74 -9 Q84 -9 84 1 Q84 13 70 15 Q40 17 6 9 Z" fill="{cor}"/><circle cx="2" cy="0" r="6" fill="{cor}" stroke="{fundo}" stroke-width="2.5"/></g></svg>'''


P = {}
P['F1-espaco-kids'] = f'''<section class="p y">{hd('Kids')}
<div class="c"><div class="lab">Corte infantil na ED</div>
<div class="big" style="font-size:190px;margin-top:20px">Tem espaço<br>kids.</div>
<div style="margin:44px 0">{navalha(K, Y, 420)}</div>
<p class="txt" style="max-width:860px">Sala de super-heróis pra os pequenos cortarem com calma.</p>
<p class="txt" style="max-width:860px;margin-top:22px">Pai e filho? Marca os dois juntos no app.</p></div>
{rod()}</section>'''

P['F2-salao-feminino'] = f'''<section class="p k">{hd('Salão')}
<div class="c"><div class="lab am">Na mesma casa</div>
<div class="big" style="font-size:160px;line-height:1.02;margin-top:20px">A ED também<br><span class="am">é salão.</span></div>
<div style="margin-top:50px;height:300px;border-radius:30px;overflow:hidden;border:6px solid {Y}">
<img src="{FX}../../stories/fonte/img/salao-cadeiras.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 45%"></div>
<p class="txt" style="margin-top:36px">Salão feminino na ED. Os serviços e valores estão no app.</p></div>
{rod()}</section>'''

P['F3-tempo-de-corte'] = f'''<section class="p w">{hd('Dica')}
<div class="c"><div class="lab">Salva esse post</div>
<div class="big" style="font-size:118px;line-height:1;margin-top:20px">De quanto em quanto<br>tempo cortar?</div><div style="height:12px;width:300px;background:{Y};margin-top:14px"></div>
<div style="margin-top:40px;border-top:4px solid {K}">
<div class="lin"><div class="n">Degradê<small>pra manter a transição limpa</small></div><div class="v">15 dias</div></div>
<div class="lin"><div class="n">Corte social<small>antes de perder a forma</small></div><div class="v">30 dias</div></div>
<div class="lin"><div class="n">Barba<small>pra a linha não sumir</small></div><div class="v">7 a 15</div></div></div></div>
{rod('Marca o próximo pelo app')}</section>'''

P['F4-black-friday'] = f'''<section class="p k">{hd('Black Friday')}
<div class="c"><div class="lab am">Nada de desconto de um dia só</div>
<div class="big" style="font-size:160px;line-height:1.02;margin-top:20px">A Black<br>da ED é<br><span class="am">toda semana.</span></div>
<div style="margin-top:46px;background:{Y};color:{K};border-radius:30px;padding:30px 36px;display:flex;align-items:center;gap:30px">
<div class="big" style="font-size:150px">50%</div>
<div style="font-size:34px;font-weight:700;line-height:1.2">no 1º corte, de segunda a quarta, agendando pelo app</div></div></div>
{rod()}</section>'''

P['F5-dezembro'] = f'''<section class="p y">{hd('Dezembro')}
<div class="c"><div class="lab">Fim de ano na ED</div>
<div class="big" style="font-size:215px;margin-top:20px">Dezembro<br>lota.</div>
<div style="margin:44px 0">{navalha(K, Y, 420)}</div>
<p class="txt" style="max-width:880px">A agenda de dezembro já tá aberta no app. Quem marca cedo escolhe o horário, o dia e o barbeiro.</p></div>
{rod('Garante o teu pelo link da bio')}</section>'''

for n, h in P.items():
    open(f'{n}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body style="margin:0">{h}</body></html>')
print(len(P), 'artes')
