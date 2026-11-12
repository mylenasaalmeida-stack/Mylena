# Stories de vaga de barbeiro(a), 1080x1920, com a marca nova (direção A).
# Gerar: python3 gerar_story_vaga.py && node render_story_vaga.js
from gerar_marca import ed_cortado, navalha, FONTS, Y, K, W

CSS = FONTS + f'''
*{{box-sizing:border-box;margin:0;padding:0}}
body{{margin:0}}
.st{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Poppins,sans-serif;padding:250px 90px 0}}
.st.y{{background:{Y};color:{K}}} .st.k{{background:{K};color:{W}}}
.logo{{position:absolute;top:110px;left:90px;display:flex;align-items:center;gap:18px;font-family:ArchivoBlack;font-size:26px;letter-spacing:.2em}}
.logo svg{{width:96px;height:96px}}
.pg{{position:absolute;top:140px;right:90px;font-weight:700;font-size:28px;opacity:.6}}
.big{{font-family:Anton;text-transform:uppercase;line-height:.92}}
.lab{{font-weight:700;font-size:28px;letter-spacing:.2em;text-transform:uppercase}}
.it{{display:grid;grid-template-columns:70px 1fr;gap:0 24px;margin-bottom:34px;align-items:start}}
.it .n{{font-family:Anton;font-size:58px;line-height:1;color:{Y}}}
.it b{{font-size:40px;line-height:1.15;display:block}}
.it span{{font-size:30px;color:#bdbab2;line-height:1.3}}
.zona{{position:absolute;left:90px;right:90px;border:4px dashed;border-radius:30px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:28px;opacity:.45;text-align:center}}
'''


def logo(cor, fundo, uid):
    return (f'<div class="logo"><svg viewBox="40 30 320 260">{ed_cortado(200, 262, 236, cor, fundo, uid)}</svg>'
            f'<span>ED BARBEARIA</span></div>')


s1 = f'''<section class="st y">{logo(K, Y, 's1')}<div class="pg">1/2</div>
<div class="lab" style="margin-top:60px">Vaga de barbeiro(a) · Casa Amarela</div>
<div class="big" style="font-size:240px;margin-top:30px">Tem<br>cadeira<br>pra ti.</div>
<svg viewBox="-100 -20 200 40" style="width:480px;margin:40px 0 0 -10px">{navalha(0, 0, 1.15, K, Y)}</svg>
<p style="font-size:42px;font-weight:600;line-height:1.25;margin-top:36px;max-width:860px">A ED procura barbeiro ou barbeira que capricha no acabamento e quer crescer numa casa com cliente fiel.</p>
<div style="position:absolute;right:90px;bottom:380px;font-weight:700;font-size:34px">Arrasta pro lado ➜</div>
</section>'''

itens = [('Domina degradê e barba', 'Máquina, tesoura e navalha. Acabamento que o cliente nota.'),
         ('Gosta de gente', 'Atende bem, conversa e faz o cliente querer voltar.'),
         ('Seg a sáb, 9h às 19h', 'Disponível nos dias e horários da casa.'),
         ('Pontual e organizado', 'Bancada limpa, horário do app respeitado.')]
it = ''.join(f'<div class="it"><div class="n">{i}</div><div><b>{a}</b><span>{b}</span></div></div>' for i, (a, b) in enumerate(itens, 1))
s2 = f'''<section class="st k">{logo(Y, K, 's2')}<div class="pg">2/2</div>
<div class="big" style="font-size:120px;margin-top:120px">O que a gente <span style="color:{Y}">procura</span></div>
<div style="margin-top:60px">{it}</div>
<div style="background:{Y};color:{K};border-radius:30px;padding:36px 40px;margin-top:20px">
<div class="lab" style="font-size:24px">Como se candidatar</div>
<p style="font-size:38px;font-weight:700;line-height:1.25;margin-top:10px">Manda no direct: teu nome, há quanto tempo corta e fotos de 3 cortes teus.</p></div>
<p style="font-size:32px;color:#bdbab2;margin-top:30px;line-height:1.4">Conhece alguém? Compartilha esse story.<br>📍 Rua Paula Batista, 604 · Casa Amarela</p>
</section>'''

for n, s in [('vaga-barbeiro-1', s1), ('vaga-barbeiro-2', s2)]:
    open(f'{n}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{s}</body></html>')
print('ok')
