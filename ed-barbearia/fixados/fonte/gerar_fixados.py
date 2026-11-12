# 3 posts fixados que se completam no perfil: AGENDA. → SENTA. → VOLTA.  1080x1350, logo atual.
# Gerar: python3 gerar_fixados.py && node render_fixados.js
Y, K, W = '#FFC629', '#111111', '#F5F3EE'
FONTS = '''
@font-face{font-family:Anton;src:url('../../marca/fonte/fonts/Anton.ttf')}
@font-face{font-family:Poppins;font-weight:500;src:url('../../../fonte/fonts/Poppins-500.woff2')}
@font-face{font-family:Poppins;font-weight:600;src:url('../../../fonte/fonts/Poppins-600.woff2')}
@font-face{font-family:Poppins;font-weight:700;src:url('../../../fonte/fonts/Poppins-700.woff2')}
'''
# A grade do perfil mostra 3:4 e corta ~34 px de cada lado: margem de 90 px protege o conteúdo.
CSS = FONTS + f'''
*{{box-sizing:border-box;margin:0;padding:0}}
.p{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Poppins,sans-serif}}
.k{{background:{K};color:{W}}} .y{{background:{Y};color:{K}}}
.hd{{position:absolute;top:64px;left:90px;right:90px;display:flex;justify-content:space-between;align-items:center;z-index:5}}
.hd .l{{display:flex;align-items:center;gap:16px;font-weight:700;font-size:24px;letter-spacing:.2em}}
.hd img{{width:76px;height:76px;border-radius:50%;border:5px solid {K};background:#fff}}
.k .hd img{{border-color:{W}}}
.hd .n{{font-family:Anton;font-size:34px;letter-spacing:.05em}}
.tt{{position:absolute;left:84px;bottom:220px;font-family:Anton;font-size:250px;line-height:.8;text-transform:uppercase;z-index:5}}
.fio{{position:absolute;left:0;right:0;bottom:190px;height:6px;z-index:5}}
.k .fio{{background:{Y}}} .y .fio{{background:{K}}}
.seta{{position:absolute;right:90px;bottom:236px;font-family:Anton;font-size:64px;z-index:5}}
.rod{{position:absolute;left:90px;right:90px;bottom:62px;font-size:30px;font-weight:600;line-height:1.3;z-index:5}}
.passo{{display:grid;grid-template-columns:86px 1fr;align-items:center;border-radius:24px;padding:22px 28px;margin-bottom:16px;background:#1f1f1f}}
.passo .n{{font-family:Anton;font-size:84px;line-height:1;color:{Y}}}
.passo b{{font-family:Anton;font-size:50px;text-transform:uppercase;line-height:1;display:block;font-weight:400}}
.passo span{{font-size:24px;color:#a9a69e}}
.precos{{display:flex;gap:14px;margin-top:22px}}
.precos div{{flex:1;border:3px solid #333;border-radius:20px;padding:14px 18px}}
.precos div.on{{background:{Y};color:{K};border-color:{Y}}}
.precos small{{display:block;font-size:20px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}}
.precos b{{font-family:Anton;font-size:58px;font-weight:400;line-height:1.05}}
'''


def hd(n):
    return f'<div class="hd"><div class="l"><img src="img/logo-antigo.png"><span>ED BARBEARIA</span></div><div class="n">{n}/3</div></div>'


p1 = f'''<section class="p k">{hd(1)}
<div style="position:absolute;top:210px;left:90px;right:90px">
<div style="font-weight:700;font-size:26px;letter-spacing:.2em;color:{Y};margin-bottom:20px">COMO AGENDAR · 3 TOQUES</div>
<div class="passo"><div class="n">1</div><div><b>Toca no link da bio</b><span>Abre o agendamento da ED.</span></div></div>
<div class="passo"><div class="n">2</div><div><b>Escolhe serviço e hora</b><span>E o barbeiro que tu quiser.</span></div></div>
<div class="passo"><div class="n">3</div><div><b>Confirma e pronto</b><span>Sem fila e sem esperar no WhatsApp.</span></div></div>
<div class="precos"><div><small>Cabelo</small><b>R$ 50</b></div><div><small>Barba</small><b>R$ 40</b></div><div class="on"><small>Cabelo + barba</small><b>R$ 80</b></div></div>
</div>
<div class="tt">Agenda<span style="color:{Y}">.</span></div><div class="seta" style="color:{Y}">→</div><div class="fio"></div>
<div class="rod" style="color:#bdbab2">Corte kids e salão feminino: valores no app.</div></section>'''

p2 = f'''<section class="p y">{hd(2)}
<div style="position:absolute;top:180px;left:90px;right:90px;height:760px;border-radius:30px;overflow:hidden;border:6px solid {K}">
<img src="img/ed-cliente.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 0%;filter:grayscale(1) contrast(1.05)"></div>
<div style="position:absolute;top:780px;right:60px;width:300px;height:300px;border-radius:50%;background:{K};color:{Y};display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);z-index:6;text-align:center">
<div style="font-family:Anton;font-size:120px;line-height:.9">50%</div><div style="font-weight:700;font-size:24px;line-height:1.15;color:{W}">no 1º corte<br>seg a qua</div></div>
<div class="tt">Senta<span>.</span></div><div class="fio"></div>
<div class="rod">Segunda a quarta, teu primeiro corte sai com 50% agendando pelo app.</div></section>'''

p3 = f'''<section class="p k">
<img src="img/ed-retrato.jpg" style="position:absolute;top:0;left:0;width:1080px;height:1060px;object-fit:cover;object-position:62% 0%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.92) 0,rgba(17,17,17,0) 260px,rgba(17,17,17,0) 620px,{K} 1010px)"></div>
{hd(3)}
<div style="position:absolute;left:90px;bottom:500px;font-weight:700;font-size:34px;line-height:1.25;z-index:5;max-width:640px">Quem senta na cadeira da ED,</div>
<div class="tt" style="color:{Y}">Volta<span style="color:{W}">.</span></div><div class="fio"></div>
<div class="rod" style="color:#bdbab2">O Ed revisa cada acabamento antes de tu levantar.<br><span style="color:{W}">Seg a sáb, 9h às 19h · Rua Paula Batista, 604</span></div></section>'''

for n, h in [('fixado-1-agenda', p1), ('fixado-2-senta', p2), ('fixado-3-volta', p3)]:
    open(f'{n}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body style="margin:0">{h}</body></html>')
print('ok')
