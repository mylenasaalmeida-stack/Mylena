# Capas de Reels dos 3 vídeos virais (V1, V2, V3). 1080x1920, essencial no miolo 3:4 que a grade mostra.
# Gerar: python3 gerar_capas_virais.py && node render_mockup.js
from gerar_mockup import CAPA_CSS, navalha, ED, Y, K, W

EXTRA = f'''
.x{{display:grid;grid-template-columns:110px 1fr;gap:0 26px;align-items:center;margin-bottom:26px;position:relative;z-index:2}}
.x .n{{width:110px;height:110px;border-radius:50%;background:{K};color:{Y};font-family:Anton;font-size:70px;display:flex;align-items:center;justify-content:center;position:relative}}
.x .n:after{{content:'';position:absolute;inset:-6px;background:linear-gradient(45deg,transparent 46%,#e8473c 46%,#e8473c 54%,transparent 54%)}}
.x b{{font-family:Anton;font-weight:400;font-size:62px;line-height:1;text-transform:uppercase}}
'''

CAPAS = {
    'V1': f'''<section class="c" style="background:{K};color:{W};justify-content:flex-end;padding-bottom:330px">
<img src="{ED}fixados/fonte/img/ed-retrato.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:62% 0">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.05) 25%,{K} 70%)"></div>
<div class="l" style="color:{Y}">ED BARBEARIA</div>
<div class="t" style="font-size:170px">O corte<br>que eu<br><span style="color:{Y}">errei.</span></div></section>''',

    'V2': f'''<section class="c" style="background:{Y};color:{K}">
<div class="l">ED BARBEARIA</div>
<div class="t" style="font-size:140px;line-height:.95">3 coisas que<br>estragam teu<br>corte em 3 dias</div>
<div style="margin-top:60px">
<div class="x"><div class="n">1</div><b>Pezinho em casa</b></div>
<div class="x"><div class="n">2</div><b>Dormir molhado</b></div>
<div class="x"><div class="n">3</div><b>Pomada demais</b></div></div></section>''',

    'V3': f'''<section class="c" style="background:{W};color:{K}">
<div class="l">ED BARBEARIA</div>
<div class="t" style="font-size:150px;line-height:1">Os 4 clientes<br>que todo<br>barbeiro já</div><div class="t" style="font-size:150px;line-height:1;background:{Y};display:inline-block;align-self:flex-start;padding:14px 18px 4px;margin-top:16px">atendeu</div>
<div style="margin-top:50px;font-family:Poppins;font-weight:700;font-size:44px;position:relative;z-index:2">O 3º é tu.</div>
<div class="nv">{navalha(K, W, 420)}</div></section>''',
}
for cod, html in CAPAS.items():
    open(f'capa-reels-{cod}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CAPA_CSS}{EXTRA}</style></head><body>{html}</body></html>')
print(len(CAPAS), 'capas')
