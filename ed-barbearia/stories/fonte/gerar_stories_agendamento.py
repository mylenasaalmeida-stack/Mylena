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
