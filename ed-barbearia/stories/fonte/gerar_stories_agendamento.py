# Stories do destaque AGENDAMENTO refeitos no padrão: "Agenda aberta" e "App novo".
# Gerar: python3 gerar_stories_agendamento.py && node render_stories.js
from gerar_stories import CSS, st, navalha, Y, K, W

EXTRA = f'''
.item{{display:grid;grid-template-columns:90px 1fr;gap:0 26px;align-items:center;margin-bottom:24px}}
.item .n{{width:90px;height:90px;border-radius:50%;background:{K};color:{Y};font-family:Anton;font-size:54px;display:flex;align-items:center;justify-content:center}}
.item b{{font-family:Anton;font-size:60px;font-weight:400;text-transform:uppercase;line-height:1;display:block}}
.item span{{font-size:30px;font-weight:600;line-height:1.3}}
'''

S = {}
S['11-agenda-aberta'] = st('k', 'Agendamento', f'''
<div class="lab am" style="margin-top:20px">Horários abertos</div>
<div class="big" style="font-size:210px;margin-top:20px">Agenda<br><span class="am">aberta.</span></div>
<div style="margin-top:50px;height:440px;border-radius:30px;overflow:hidden;border:6px solid {Y}">
<img src="img/salao-cadeiras.jpg" style="width:100%;height:100%;object-fit:cover;object-position:40% 60%"></div>
<p class="p" style="margin-top:40px">Escolhe o dia, o horário e o barbeiro direto no app. A cadeira fica te esperando.</p>''',
                           '<span class="am">Toca no link e agenda ↓</span>')

S['12-app-novo'] = st('y', 'Aviso', f'''
<div class="lab" style="margin-top:20px">A ED tá com app novo</div>
<div class="big" style="font-size:180px;line-height:1.02;margin-top:20px">Agendar<br>ficou mais<br>fácil.</div>
<div style="margin:30px 0 36px">{navalha(K, Y, 420)}</div>
<div class="item"><div class="n">1</div><div><b>Toca no link</b><span>Abre o app de agendamento da ED.</span></div></div>
<div class="item"><div class="n">2</div><div><b>Escolhe tudo</b><span>Serviço, dia, horário e barbeiro.</span></div></div>
<div class="item"><div class="n">3</div><div><b>Confirma</b><span>Pronto. Sem esperar resposta no WhatsApp.</span></div></div>''',
                      'Toca no link e agenda ↓')

for n, h in S.items():
    open(f'{n}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}</style></head><body style="margin:0">{h}</body></html>')
print(len(S), 'stories')

# ---- Onde estamos (refeito do story do destaque Localização) ----
S2 = {}
S2['13-onde-estamos'] = st('k', 'Localização', f'''
<div class="lab am" style="margin-top:20px">Casa Amarela · Recife</div>
<div class="big" style="font-size:200px;margin-top:20px">Onde<br><span class="am">estamos.</span></div>
<div style="margin-top:46px;height:330px;border-radius:30px;overflow:hidden;border:6px solid {Y}">
<img src="img/fachada.jpg" style="width:100%;height:100%;object-fit:cover;object-position:15% 0%"></div>
<div style="margin-top:44px;display:grid;grid-template-columns:96px 1fr;gap:0 26px;align-items:center">
<svg viewBox="0 0 24 24" style="width:96px" fill="{Y}"><path d="M12 2a8 8 0 0 0-8 8c0 5.4 7 11.5 7.3 11.8a1 1 0 0 0 1.4 0C13 21.5 20 15.4 20 10a8 8 0 0 0-8-8Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z"/></svg>
<div><div class="big" style="font-size:72px;line-height:1">Rua Paula Batista, 604</div>
<div style="font-size:32px;font-weight:600;color:#bdbab2;margin-top:6px">Casa Amarela, Recife - PE</div></div></div>
<div style="margin-top:30px;background:{Y};color:{K};border-radius:24px;padding:22px 30px;font-size:32px;font-weight:700">Do lado da Delegacia de Casa Amarela</div>''',
                              '<span class="am">Toca na localização e abre o mapa ↓</span>')
for n, h in S2.items():
    open(f'{n}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}</style></head><body style="margin:0">{h}</body></html>')
