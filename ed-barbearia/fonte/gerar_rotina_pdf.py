# Rotina da gravação de 13/11 em PDF de celular (540x960), enxuta pra terminar antes das 16h.
# Gerar: python3 gerar_rotina_pdf.py && node render_celular.js rotina
from gerar_roteiros_simples import CSS

EXTRA = '''
table.r{width:100%;border-collapse:collapse;font-size:12.5px}
table.r td{padding:6px 5px;border-bottom:1px solid #262626;vertical-align:top}
table.r td.h{color:#f5cf4a;font-weight:700;white-space:nowrap;width:92px}
table.r td.m{color:#8a877f;white-space:nowrap;width:44px;text-align:right}
table.r tr.g td{background:#1d1b12}
.blk{background:#1a1a1a;border-radius:12px;padding:9px 12px;margin-bottom:7px}
.blk .t{display:flex;justify-content:space-between;align-items:baseline}
.blk .t b{font-size:14px} .blk .t span{color:#f5cf4a;font-weight:700;font-size:12px;white-space:nowrap}
.blk p{font-size:12.3px;margin-top:3px;color:#d6d3cb}
.blk .cut{font-size:11px;color:#8a877f;margin-top:4px}
.box{display:inline-block;width:15px;height:15px;border:2px solid #f5cf4a;border-radius:4px;margin-right:9px;vertical-align:-3px}
.chk{font-size:13px;margin-bottom:7px}
'''

# (início, fim, minutos, atividade, como fazer, se atrasar, gravação?)
BLOCOS = [
    ('', '', 5, 'Chegar e escolher o lugar',
     'Sem montar luz: a iluminação da ED já é boa. Escolhe o canto onde a luz do salão cai de frente no rosto do Ed, com a fachada de vidro fora do fundo. Põe a lapela nele e testa o áudio em 5 s.', 'Não corta', False),
    ('13:10', '13:20', 10, 'Conversa rápida com o Ed',
     'Só o que trava a gravação: a história do V1 (há quantos anos corta, o erro, o que mudou), se os 3 erros do V2 batem e quem da equipe faz o V3. Autorização de imagem.', 'Não corta', False),
    ('13:20', '13:45', 25, 'Gravar V1 · O corte que eu errei',
     'Ed na cadeira vazia. Os 3 ganchos e cada fala 2 vezes. O trecho do espelho de mão fica pro cliente do V2.', 'Grava só o gancho A', True),
    ('13:45', '13:50', 5, 'Passar os stories pra equipe',
     'Mostra pra quem vai postar: bastidor da gravação + story-02 com os horários livres de hoje. A equipe posta enquanto tu grava.', 'Não corta (são 5 min)', False),
    ('13:50', '14:30', 40, 'Gravar V2 + final do V1',
     'Cliente de degradê, com autorização. Close da nuca pronta, os 3 erros com o número na tela e a fala final. Com o mesmo cliente: Ed revisando a nuca com o espelho de mão, pro fim do V1.', 'Nunca corta', True),
    ('14:30', '14:35', 5, 'Conferir os ganchos',
     'Assiste os 3 ganchos de V1 e V2. Se algum ficou ruim, refaz agora. O backup completo tu faz em casa.', 'Não corta', False),
    ('14:35', '15:00', 25, 'Gravar V3 · Os 4 clientes',
     '4 cenas de até 6 s, trocando boné e camisa. O Ed não ri. Celular extra com “CARECA” na tela.', 'Faz só 3 tipos (corta o que dorme)', True),
    ('15:00', '15:10', 10, 'Fotos extras',
     'Fachada inteira com o letreiro, espaço kids, salão feminino e um retrato do Ed com o logo da parede.', 'Faz só a fachada', False),
    ('15:10', '15:20', 10, 'Aprovações com o Ed',
     'Só o que precisa da cara dele: mostra a logo amarela e as 5 artes novas e pega o sim. O resto das perguntas vai por WhatsApp (última página).', 'Manda tudo no WhatsApp', False),
    ('15:20', '15:25', 5, 'Fechar',
     'Recolhe o equipamento e confirma a visita de quarta, 18/11 (ensaio de fotos).', 'Não corta', False),
]

LEVAR = ['Tripé', 'Microfone de lapela (carregado)', 'Power bank e cabo', 'Celular com 10 GB livres, no modo avião',
         'Celular extra com “CARECA” escrito na tela (V3)', 'Boné e 2 camisas diferentes (V3)',
         'Aparelho de barbear e um pote de pomada (V2)',
         'Este PDF e o dos 3 roteiros abertos no celular', 'Logo amarela e as 5 artes no celular, pra mostrar ao Ed']

NA_HORA = ['Há quantos anos ele corta e onde começou (V1)', 'Um corte que deu errado e o que mudou (V1)',
           'Os 3 erros do V2 são os que ele mais vê?', 'Aprova a logo amarela pra foto de perfil?',
           'Aprova as 5 artes extras do feed?']
WHATSAPP = ['Prazos da arte “tempo de corte” (degradê 15 dias, social 30, barba 7 a 15) estão certos?',
            'O espaço kids é uma sala de super-heróis?', 'Serviços e valores do salão feminino pras artes',
            'A ED abre no feriado de 20/11?', 'Quem da equipe posta os stories em cada dia?',
            'Como o app mostra que é o 1º corte (pra conferir o 50%)?', 'O que são os destaques G10 e Barberdy?',
            'A vaga é seg a sáb, 9h às 19h? Divulga salário ou comissão?',
            'Bio: corrigir “9h ás 19h” para “9h às 19h”', 'Dá pra trocar o link do Netlify por um nome da ED?']

# horários calculados a partir das 13h, somando os minutos de cada bloco
_t = 13 * 60
for _i, _b in enumerate(BLOCOS):
    BLOCOS[_i] = (f'{_t // 60}:{_t % 60:02d}', f'{(_t + _b[2]) // 60}:{(_t + _b[2]) % 60:02d}') + _b[2:]
    _t += _b[2]


def fim(atraso):
    t = _t + atraso
    return f'{t // 60}h{t % 60:02d}'


pages = []


def P(ey, body):
    pages.append((ey, body))


tot = sum(b[2] for b in BLOCOS)
linhas = ''.join(f'<tr class="{"g" if g else ""}"><td class="h">{a}–{b}</td><td>{at}</td><td class="m">{m} min</td></tr>'
                 for a, b, m, at, _, _, g in BLOCOS)
P('Sexta, 13/11 · tarde na ED', f'''
<h2>Minha tarde <span class="am">na ED.</span></h2>
<p class="sub">Chegando 13h, saio às <b style="color:#f5cf4a">{fim(0)}</b>. Chegando 13h30, saio às <b style="color:#f5cf4a">{fim(30)}</b>. Antes das 16h nos dois casos.</p>
<table class="r">{linhas}
<tr><td class="h">Total</td><td><b>Tudo</b></td><td class="m"><b>{tot // 60}h{tot % 60:02d}</b></td></tr></table>
<p class="nota" style="font-size:11.5px;color:#a9a69e;margin-top:8px">Linhas em destaque: gravação. Chegou 13h30? Soma 30 min em todos os horários.</p>
<h3>Pra caber antes das 16h</h3>''' + '<ul>' + ''.join(f'<li>{x}</li>' for x in [
    'Sem montar luz: usa a iluminação da ED.',
    'A equipe posta os stories, tu só passa o que é.',
    'Backup completo em casa. Lá, só confere os ganchos.',
    'Com o Ed, só o que precisa dele na hora. O resto vai por WhatsApp.',
]) + '</ul>')

blk = lambda b: (f'<div class="blk"><div class="t"><b>{b[3]}</b><span>{b[0]}–{b[1]} · {b[2]} min</span></div>'
                 f'<p>{b[4]}</p><div class="cut">Se atrasar: {b[5]}</div></div>')
P('Como fazer cada parte · 1/2', '<h2>Passo a passo <span class="am">1/2</span></h2>' + ''.join(blk(b) for b in BLOCOS[:5]))
P('Como fazer cada parte · 2/2', '<h2>Passo a passo <span class="am">2/2</span></h2>' + ''.join(blk(b) for b in BLOCOS[5:]) + '''
<div class="blk" style="border:1.5px solid #f5cf4a"><b>Regra de ouro</b><p>Grava os 3 ganchos de cada vídeo e cada fala 2 vezes. Se atrasar, corta pelo “Se atrasar”, nunca da gravação do V2.</p></div>''')

chk = lambda xs: ''.join(f'<div class="chk"><span class="box"></span>{x}</div>' for x in xs)
P('Antes de sair de casa', '<h2>O que <span class="am">levar.</span></h2><div style="margin-top:12px">' + chk(LEVAR) + '</div>')
P('Perguntas pro Ed', '<h2>Com o Ed, <span class="am">na hora.</span></h2><div style="margin-top:8px">' + chk(NA_HORA) +
  '</div><h3>Por WhatsApp, depois</h3>' + chk(WHATSAPP))

n = len(pages)
html = ''.join(
    f'<section class="pg"><div class="ey">{e}</div>{b}<div class="foot"><span>ED BARBEARIA × HOUSE DO CREATOR</span><span>{i + 1:02d} / {n:02d}</span></div></section>'
    for i, (e, b) in enumerate(pages))
open('rotina.html', 'w').write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Minha tarde na ED · 13/11</title>
<link rel="stylesheet" href="../../fonte/fonts.css"><style>{CSS}{EXTRA}</style></head><body>{html}</body></html>''')
print(n, 'páginas,', tot, 'min')
