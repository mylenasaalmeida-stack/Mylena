# "Estamos contratando": story (1080x1920) e feed (1080x1350) no padrão com a logo atual.
# Gerar: python3 gerar_contratando.py && node render_stories.js && node render_contratando_feed.js
from gerar_stories import CSS, st, navalha, Y, K, W

EXTRA = f'''
.req{{display:grid;grid-template-columns:70px 1fr;gap:0 22px;align-items:center;margin-bottom:22px}}
.req .n{{width:70px;height:70px;border-radius:50%;background:{Y};color:{K};font-family:Anton;font-size:42px;display:flex;align-items:center;justify-content:center}}
.req b{{font-family:Anton;font-size:52px;font-weight:400;text-transform:uppercase;line-height:1;display:block}}
.req span{{font-size:27px;color:#bdbab2;line-height:1.3}}
.cand{{background:{Y};color:{K};border-radius:28px;padding:28px 34px}}
.cand .l{{font-weight:700;font-size:22px;letter-spacing:.2em}}
.cand p{{font-size:34px;font-weight:700;line-height:1.25;margin-top:8px}}
'''

REQ = [('Degradê e barba', 'Máquina, tesoura e navalha, com acabamento caprichado.'),
       ('Gosta de gente', 'Atende bem e faz o cliente querer voltar.'),
       ('Seg a sáb, 9h às 19h', 'Disponível nos dias e horários da casa.')]
req = ''.join(f'<div class="req"><div class="n">{i}</div><div><b>{a}</b><span>{b}</span></div></div>' for i, (a, b) in enumerate(REQ, 1))
CAND = '<div class="cand"><div class="l">COMO SE CANDIDATAR</div><p>Manda no direct: teu nome, há quanto tempo corta e fotos de 3 cortes teus.</p></div>'

story = st('k', 'Vaga aberta', f'''
<div class="lab am" style="margin-top:10px">Barbeiro ou barbeira</div>
<div class="big" style="font-size:168px;margin-top:16px">Estamos<br><span class="am">contratando.</span></div>
<div style="margin:36px 0 40px">{navalha(Y, K, 380)}</div>
{req}
<div style="margin-top:20px">{CAND}</div>''', '<span class="am">Conhece alguém? Compartilha ↓</span>')
open('14-estamos-contratando.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}</style></head><body style="margin:0">{story}</body></html>')

# feed 1080x1350: a grade do perfil corta ~34 px de cada lado, margem de 90 px protege
FEED = f'''
.f{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;background:{K};color:{W};padding:0 90px}}
.f .logo{{top:64px}} .f .tag{{top:92px}}
.f .body{{top:210px}}
'''
feed = st('k', 'Vaga aberta', f'''
<div class="lab am">Barbeiro ou barbeira · Casa Amarela</div>
<div class="big" style="font-size:150px;margin-top:14px">Estamos<br><span class="am">contratando.</span></div>
<div style="margin-top:40px">{req}</div>
<div style="margin-top:14px">{CAND}</div>
<p style="font-size:26px;color:#bdbab2;margin-top:20px">📍 Rua Paula Batista, 604 · Casa Amarela, Recife</p>''').replace('class="st k"', 'class="f k"')
open('feed-estamos-contratando.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}{FEED}</style></head><body style="margin:0">{feed}</body></html>')
print('ok')
