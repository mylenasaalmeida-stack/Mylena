# 10 stories da pauta de novembro com a logo atual (barbudo). 1080x1920.
# Gerar: python3 gerar_stories.py && node render_stories.js
import sys
sys.path.insert(0, '../../marca/fonte')
Y, K, W = '#FFC629', '#111111', '#F5F3EE'

FONTS = '''
@font-face{font-family:Anton;src:url('../../marca/fonte/fonts/Anton.ttf')}
@font-face{font-family:Poppins;font-weight:500;src:url('../../../fonte/fonts/Poppins-500.woff2')}
@font-face{font-family:Poppins;font-weight:600;src:url('../../../fonte/fonts/Poppins-600.woff2')}
@font-face{font-family:Poppins;font-weight:700;src:url('../../../fonte/fonts/Poppins-700.woff2')}
'''
CSS = FONTS + f'''
*{{box-sizing:border-box;margin:0;padding:0}}
.st{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;padding:0 90px}}
.y{{background:{Y};color:{K}}} .k{{background:{K};color:{W}}} .w{{background:{W};color:{K}}}
.logo{{position:absolute;top:110px;left:90px;display:flex;align-items:center;gap:20px;font-weight:700;font-size:26px;letter-spacing:.2em}}
.logo img{{width:104px;height:104px;border-radius:50%;border:7px solid {K};background:#fff}}
.k .logo img{{border-color:{W}}}
.tag{{position:absolute;top:150px;right:90px;font-weight:700;font-size:24px;letter-spacing:.14em;text-transform:uppercase;padding:10px 20px;border-radius:40px}}
.y .tag{{background:{K};color:{Y}}} .k .tag{{background:{Y};color:{K}}} .w .tag{{background:{K};color:{W}}}
.body{{position:absolute;top:330px;left:90px;right:90px}}
.big{{font-family:Anton;text-transform:uppercase;line-height:.92}}
.lab{{font-weight:700;font-size:28px;letter-spacing:.2em;text-transform:uppercase}}
.p{{font-size:42px;font-weight:600;line-height:1.25}}
.am{{color:{Y}}}
.cta{{position:absolute;left:90px;right:90px;bottom:380px;font-weight:700;font-size:36px;text-align:center}}
.slot{{height:96px;border-radius:24px;margin-bottom:22px;display:flex;align-items:center;padding:0 34px;font-size:34px;font-weight:600}}
.k .slot{{background:#232323;color:#555}}
.foto{{border-radius:30px;display:flex;align-items:flex-start;padding:24px;font-weight:700;font-size:26px;letter-spacing:.12em}}
.row{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:4px solid {K};padding:26px 0}}
.row .n{{font-family:Anton;font-size:110px;line-height:1}}
.row .v{{font-family:Anton;font-size:130px;line-height:1}}
.row .v small{{font-size:44px;vertical-align:60px;margin-right:6px}}
.passo{{display:grid;grid-template-columns:120px 1fr;align-items:center;background:#fff;border-radius:30px;padding:30px 36px;margin-bottom:24px}}
.passo .n{{font-family:Anton;font-size:120px;line-height:1}}
.passo b{{font-family:Anton;font-size:58px;text-transform:uppercase;line-height:1;display:block}}
.passo span{{font-size:30px;color:#555}}
.passo.on{{background:{K};color:{W}}} .passo.on b{{color:{Y}}} .passo.on span{{color:#bbb}}
'''


def navalha(cor, fundo, w=460):
    return f'''<svg viewBox="-100 -20 200 40" style="width:{w}px;display:block">
<g transform="scale(1.15)"><rect x="-92" y="-8" width="96" height="16" rx="8" fill="{cor}"/>
<circle cx="-78" cy="0" r="2.6" fill="{fundo}"/><circle cx="-12" cy="0" r="2.6" fill="{fundo}"/>
<path d="M2 -9 L74 -9 Q84 -9 84 1 Q84 13 70 15 Q40 17 6 9 Z" fill="{cor}"/>
<circle cx="2" cy="0" r="6" fill="{cor}" stroke="{fundo}" stroke-width="2.5"/></g></svg>'''


def st(cls, tag, body, cta=''):
    lg = '<div class="logo"><img src="img/logo-antigo.png"><span>ED BARBEARIA</span></div>'
    return f'<section class="st {cls}">{lg}<div class="tag">{tag}</div><div class="body">{body}</div>{f"<div class=cta>{cta}</div>" if cta else ""}</section>'


S = {}
S['01-campanha-50'] = st('y', 'Seg a qua', f'''
<div class="lab" style="margin-top:40px">Segunda, terça e quarta</div>
<div class="big" style="font-size:420px;margin-top:20px">50%</div>
<div class="big" style="font-size:130px">no teu 1º corte</div>
<div style="margin-top:50px">{navalha(K, Y)}</div>
<p class="p" style="margin-top:44px">Agendando pelo app.<br>Vale de 09 a 30/11.</p>''', 'Toca no link e marca ↓')

S['02-horarios-livres'] = st('k', 'Hoje', f'''
<div class="big" style="font-size:190px;margin-top:20px">Horários<br><span class="am">livres hoje</span></div>
<div style="margin-top:60px">{''.join('<div class="slot"></div>' for _ in range(5))}</div>''', '<span class="am">Toca no link e garante o teu ↓</span>')

S['03-antes-depois'] = st('w', 'Resultado', f'''
<div class="big" style="font-size:150px;margin-top:10px">Antes <span style="color:{Y};-webkit-text-stroke:3px {K}">/</span> depois</div>
<div style="display:grid;grid-template-rows:1fr 1fr;gap:26px;height:1020px;margin-top:40px">
<div class="foto" style="background:#e4e1d9"><span style="background:{K};color:{W};padding:8px 18px;border-radius:30px">ANTES</span></div>
<div class="foto" style="background:#e4e1d9"><span style="background:{Y};color:{K};padding:8px 18px;border-radius:30px">DEPOIS</span></div></div>''')

S['04-qual-corte'] = st('k', 'Caixinha', f'''
{navalha(Y, K, 380)}
<div class="big" style="font-size:210px;margin-top:50px">Qual corte<br><span class="am">tu quer?</span></div>
<p class="p" style="margin-top:50px;color:#ccc">Manda o print do corte aqui na caixinha. O Ed responde se combina com o teu rosto.</p>''', '<span class="am">↓ caixinha aqui embaixo</span>')

S['05-pergunte-ao-ed'] = st('y', 'Pergunte ao Ed', f'''
<div class="lab" style="margin-top:40px">Domingo é dia de dúvida</div>
<div class="big" style="font-size:200px;margin-top:20px">Manda tua<br>dúvida<br>pro Ed.</div>
<p class="p" style="margin-top:50px">Corte, barba, cabelo que não assenta, produto. Ele responde em vídeo na segunda.</p>''', '↓ caixinha aqui embaixo')

S['06-enquete'] = st('k', 'Enquete', f'''
<div class="lab am" style="margin-top:40px">Vota aí</div>
<div class="big" style="font-size:240px;margin-top:20px">Degradê<br><span class="am">ou</span><br>social?</div>''', '<span class="am">↓ enquete aqui embaixo</span>')

S['07-tabela'] = st('y', 'Tabela', f'''
<div class="big" style="font-size:150px;margin-top:20px">Quanto custa</div>
<div style="margin-top:50px;border-top:4px solid {K}">
<div class="row"><span class="n">Cabelo</span><span class="v"><small>R$</small>50</span></div>
<div class="row"><span class="n">Barba</span><span class="v"><small>R$</small>40</span></div></div>
<div style="background:{K};color:{Y};border-radius:30px;padding:30px 36px;margin-top:40px;display:flex;justify-content:space-between;align-items:center">
<div><div class="big" style="font-size:96px">Cabelo + barba</div><div style="color:{W};font-size:30px;font-weight:600">tu economiza R$ 10</div></div>
<div class="big" style="font-size:150px"><small style="font-size:44px;vertical-align:70px">R$</small>80</div></div>
<p style="font-size:32px;font-weight:600;margin-top:36px">Corte kids e salão feminino: os valores estão no app.</p>''', 'Toca no link e agenda ↓')

S['08-como-agendar'] = st('w', 'Como agendar', f'''
<div class="big" style="font-size:150px;margin-top:10px">Agendar leva</div><div class="big" style="font-size:150px;background:{Y};display:inline-block;padding:14px 18px 6px;margin-top:14px">3 toques</div>
<div style="margin-top:60px">
<div class="passo"><div class="n">1</div><div><b>Toca no link</b><span>Abre o agendamento da ED.</span></div></div>
<div class="passo"><div class="n">2</div><div><b>Escolhe serviço e hora</b><span>Corte, barba ou os dois, com o barbeiro que quiser.</span></div></div>
<div class="passo on"><div class="n am">3</div><div><b>Confirma e pronto</b><span>Chega na hora e senta na cadeira.</span></div></div></div>''', 'Sem fila, sem esperar no WhatsApp ↓')

S['09-black'] = st('k', 'Black Friday', f'''
<div class="lab am" style="margin-top:40px">Nada de desconto de um dia só</div>
<div class="big" style="font-size:200px;margin-top:20px">A Black<br>da ED é<br><span class="am">toda semana.</span></div>
<p class="p" style="margin-top:50px">De segunda a quarta, o primeiro corte sai com <span class="am">50%</span> agendando pelo app.</p>''', '<span class="am">Toca no link e marca ↓</span>')

S['10-dezembro'] = st('y', 'Dezembro', f'''
<div class="big" style="font-size:220px;margin-top:20px">Dezembro<br>lota.</div>
<div style="margin-top:50px">{navalha(K, Y)}</div>
<p class="p" style="margin-top:50px">A agenda de dezembro já tá aberta no app. Quem marca cedo escolhe o horário.</p>''', 'Garante o teu pelo link ↓')

for n, h in S.items():
    open(f'{n}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body style="margin:0">{h}</body></html>')
print(len(S), 'stories')
