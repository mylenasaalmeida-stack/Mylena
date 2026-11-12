# Roteiros detalhados dos 7 Reels de novembro (ED Barbearia). Formato celular 540x960.
# Gerar: python3 gerar_roteiros.py && node render_celular.js roteiros  (depois renomear pra ED-Barbearia-Roteiros-Reels-Novembro-2026.pdf)
CSS = '''
@page{size:540px 960px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0e0e0e;color:#f2f0ea;font-family:Poppins,sans-serif;font-size:13px;line-height:1.42}
.pg{width:540px;height:960px;padding:32px 28px 30px;position:relative;overflow:hidden;page-break-after:always;background:#0e0e0e}
.pg.y{background:#f5cf4a;color:#111}
.ey{font-size:9.5px;letter-spacing:.2em;font-weight:700;color:#f5cf4a;text-transform:uppercase;margin-bottom:8px}
.pg.y .ey{color:#111}
h1{font-size:44px;line-height:1.04;font-weight:700;letter-spacing:-.02em;margin-bottom:14px}
h2{font-size:24px;line-height:1.1;font-weight:700;margin-bottom:6px}
h3{font-size:9.5px;letter-spacing:.18em;font-weight:700;color:#f5cf4a;text-transform:uppercase;margin:12px 0 6px}
.am{color:#f5cf4a}
.sub{color:#a9a69e;font-size:12.5px;margin-bottom:10px}
.cod{font-size:34px;font-weight:700;color:#f5cf4a;line-height:1}
.tag{display:inline-block;font-size:9px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:3px 8px;border-radius:20px;background:#222;color:#d9d6ce;margin:0 4px 4px 0}
.tag.am{background:#f5cf4a;color:#111}
.card{background:#1a1a1a;border-radius:12px;padding:9px 12px;margin-bottom:6px}
.card.dest{border:1.5px solid #f5cf4a}
.k{color:#f5cf4a;font-size:9.5px;letter-spacing:.12em;font-weight:700;text-transform:uppercase}
.kv{display:grid;grid-template-columns:74px 1fr;gap:4px 8px}
.kv b{color:#f5cf4a;font-size:10px;letter-spacing:.1em;text-transform:uppercase;padding-top:2px}
ul{list-style:none}
li{padding-left:16px;position:relative;margin-bottom:4px}
li:before{content:'';position:absolute;left:2px;top:7px;width:6px;height:6px;border-radius:50%;background:#f5cf4a}
.pg.y li:before{background:#111}
.tk{display:grid;grid-template-columns:30px 1fr;gap:0 10px;background:#1a1a1a;border-radius:10px;padding:8px 10px;margin-bottom:5px}
.tk .n{font-size:18px;font-weight:700;color:#f5cf4a;line-height:1.1}
.tk .n small{display:block;font-size:8.5px;color:#8a877f;font-weight:600;margin-top:2px;letter-spacing:0}
.tk .h{font-weight:700;font-size:12.5px}
.tk .p{font-size:9.5px;color:#111;background:#f5cf4a;border-radius:4px;padding:1px 5px;font-weight:700;margin-left:4px;vertical-align:1px}
.tk .d{font-size:12px;color:#d6d3cb}
.tk .f{font-size:12px;margin-top:2px}
.tk .f i{font-style:normal;color:#f5cf4a;font-weight:700;font-size:9.5px;letter-spacing:.08em;margin-right:4px}
.leg{background:#1a1a1a;border-left:3px solid #f5cf4a;border-radius:0 10px 10px 0;padding:9px 12px;font-size:12.5px;white-space:pre-line}
.nota{font-size:11.5px;color:#a9a69e}
.foot{position:absolute;left:28px;right:28px;bottom:16px;display:flex;justify-content:space-between;font-size:8.5px;letter-spacing:.16em;color:#666;font-weight:700}
.pg.y .foot{color:#6b5a14}
table{width:100%;border-collapse:collapse;font-size:12px}
td{padding:6px 5px;border-bottom:1px solid #262626;vertical-align:top}
td.t{color:#f5cf4a;font-weight:700;white-space:nowrap;width:70px}
'''

pages = []


def P(ey, body, cls=''):
    pages.append((ey, body, cls))


def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


# ---------------- capa e regras ----------------
P('ED Barbearia × House do Creator · Novembro 2026', '''
<div style="height:110px"></div>
<h1 style="font-size:54px">Roteiros<br><span class="am">dos 7 Reels.</span></h1>
<p class="sub" style="font-size:14px">Tomada por tomada: enquadramento, fala, texto na tela, edição, legenda e o que fazer depois de postar.</p>
<div style="height:24px"></div>
<table>
<tr><td class="t">04/11 qua</td><td><b>R1</b> Degradê sem marca · <b>R2</b> Chegou pedindo socorro</td></tr>
<tr><td class="t">11/11 qua</td><td><b>R3</b> Qual corte pro teu rosto · <b>R4</b> Navalha, parte 2 · <b>R5</b> Agendou pelo app</td></tr>
<tr><td class="t">25/11 qua</td><td><b>R6</b> Barba: o ritual · <b>R7</b> Pai e filho</td></tr>
</table>
<div style="height:24px"></div>
<div class="card"><span class="k">Cada roteiro tem 3 páginas</span>
<div style="margin-top:6px">''' + ul(['<b>Preparação:</b> objetivo, o que precisa e os 3 ganchos',
                                       '<b>Tomadas:</b> o que gravar, em que ordem e de que jeito',
                                       '<b>Edição e post:</b> montagem, áudio, capa, legenda e depois de postar']) + '</div></div>')

P('Antes de tudo · regras de gravação', '''
<h2>Como ler e <span class="am">como gravar.</span></h2>
<h3>Enquadramentos</h3>
<div class="card kv">
<b>PD</b><span>Plano detalhe: bem de perto (máquina, navalha, nuca). Celular a 20–40 cm.</span>
<b>PP</b><span>Primeiro plano: rosto e ombros.</span>
<b>PM</b><span>Plano médio: da cintura pra cima. Ed e cliente juntos.</span>
<b>PA</b><span>Plano aberto: a cadeira inteira, a porta, o salão.</span>
</div>
<h3>Regras do set</h3>''' + ul([
    'Vertical, 4K 30 fps. Câmera lenta (navalha, toalha): 1080p 60 fps.',
    'Lente 1x. A 0,5 deforma o rosto.',
    'Antes de cada tomada, segura o dedo na tela pra travar foco e luz.',
    'Grava <b>3 segundos a mais</b> antes e depois de cada tomada. A edição precisa dessa folga.',
    'Cada tomada pelo menos <b>2 vezes</b>. As falas, 3 vezes.',
    'Grava as <b>3 aberturas</b> (A, B e C). A gente escolhe na edição e testa a outra depois.',
    'O <b>antes</b> se grava antes do primeiro corte. Não tem segunda chance.',
    'Fita crepe no chão marcando cadeira e tripé: antes e depois no mesmo lugar.',
    'Logo da parede no fundo em pelo menos 1 tomada por Reels.',
    'Quando o Ed fala: microfone de lapela, ar-condicionado e secador desligados.',
    'Autorização de imagem antes de ligar a câmera. Criança: só com os pais autorizando por escrito.',
]) + '''
<h3>Texto na tela</h3>''' + ul([
    'Fora do topo e do rodapé, que o Instagram cobre com botões e legenda. Fica no meio.',
    'Fonte grande, no máximo 8 palavras por vez.',
]))

P('Plano de cada dia de gravação', '''
<h2>Ordem do set, <span class="am">visita por visita.</span></h2>
<h3>04/11 · R1 e R2 · ~2h30</h3>
<table>
<tr><td class="t">15 min</td><td>Aprovar a pauta com o Ed, autorizações e a dica de degradê dele (R1)</td></tr>
<tr><td class="t">10 min</td><td>Montar o set: tripé, luz de lado, fita no chão, lapela</td></tr>
<tr><td class="t">5 min</td><td>Gravar o ANTES dos 2 clientes</td></tr>
<tr><td class="t">50 min</td><td>R1 completo, com os 3 ganchos</td></tr>
<tr><td class="t">60 min</td><td>R2 completo, com os 3 ganchos</td></tr>
<tr><td class="t">10 min</td><td>Imagens extras: porta, máquina ligando, bancada, Ed rindo, logo</td></tr>
</table>
<h3>11/11 · R3, R4 e R5 · ~2h</h3>
<table>
<tr><td class="t">10 min</td><td>Set + gravação de tela do agendamento (R5)</td></tr>
<tr><td class="t">25 min</td><td>R3: só o Ed, antes dos clientes chegarem</td></tr>
<tr><td class="t">35 min</td><td>R4: cliente de contorno na navalha</td></tr>
<tr><td class="t">40 min</td><td>R5: cliente novo do 50% + depoimento dele pros stories de 24/11</td></tr>
</table>
<h3>25/11 · R6 e R7 · ~2h</h3>
<table>
<tr><td class="t">10 min</td><td>Set, teste da toalha quente (o vapor tem que aparecer)</td></tr>
<tr><td class="t">40 min</td><td>R6: cliente de barba cheia</td></tr>
<tr><td class="t">60 min</td><td>R7: pai e filho, espaço kids arrumado antes</td></tr>
</table>
<div class="card dest" style="margin-top:12px"><span class="k">Plano B de hoje</span><br>Se o cliente do R2 não chegar com cabelo e barba bem crescidos, grava o R3 hoje (só precisa do Ed) e o R2 vai pra 11/11. Ele sai em 14/11, ainda dá tempo.</div>
''')


# ---------------- reels ----------------
def reel(r):
    tags = ''.join(f'<span class="tag {c}">{t}</span>' for t, c in r['tags'])
    head = f'<div class="cod">{r["cod"]}</div><h2 style="margin-top:4px">{r["titulo"]}</h2><div>{tags}</div>'
    g = ''
    for i, (nome, como, tela) in enumerate(r['ganchos']):
        g += (f'<div class="card{" dest" if i == 0 else ""}"><span class="k">{"ABC"[i]} · {nome}{" · recomendado" if i == 0 else ""}</span>'
              f'<div style="margin-top:3px">{como}</div><div style="margin-top:3px"><b class="am" style="font-size:9.5px;letter-spacing:.1em">FALA / TEXTO</b> {tela}</div></div>')
    P(f'Roteiro {r["cod"]} · 1/3 · preparação', head + f'''
<h3>Pra que serve</h3><div class="card kv">
<b>Objetivo</b><span>{r["obj"]}</span><b>Pra quem</b><span>{r["pub"]}</span><b>Chamada</b><span>{r["cta"]}</span></div>
<h3>O que precisa no set</h3>{ul(r["precisa"])}
<h3>Gancho (0 a 3 s) · gravar os 3</h3>{g}''')

    tk = ''
    for n, (tempo, nome, plano, acao, fala) in enumerate(r['tomadas'], 1):
        fl = ''.join(f'<div class="f"><i>{a}</i>{b}</div>' for a, b in fala)
        tk += (f'<div class="tk"><div class="n">{n:02d}<small>{tempo}</small></div><div><span class="h">{nome}</span>'
               f'<span class="p">{plano}</span><div class="d">{acao}</div>{fl}</div></div>')
    P(f'Roteiro {r["cod"]} · 2/3 · tomadas', f'<h2><span class="am">{r["cod"]}</span> · tomadas</h2>'
      f'<p class="sub">Duração final: {r["dur"]}. Grava nessa ordem; a edição monta na ordem dos números.</p>{tk}')

    P(f'Roteiro {r["cod"]} · 3/3 · edição e post', f'''<h2><span class="am">{r["cod"]}</span> · edição e post</h2>
<h3>Montagem</h3>{ul(r["edicao"])}
<h3>Áudio</h3><p>{r["audio"]}</p>
<h3>Capa</h3><p>{r["capa"]}</p>
<h3>Legenda</h3><div class="leg">{r["leg"]}</div>
<h3>Depois de postar</h3>{ul(r["depois"])}''')


CAMP = '<b>Seg a qua: 50% no 1º corte pelo app</b>'

R = [
dict(cod='R1', titulo='Degradê sem marca', dur='25 a 30 s',
     tags=[('grava 04/11 qua', 'am'), ('posta 10/11 ter 18h30', ''), ('técnica', '')],
     obj='Alcance. Técnica é o que mais roda no perfil. De quebra, lembra da campanha.',
     pub='Homem de 18 a 35 anos, de Casa Amarela e arredores, que corta degradê.',
     cta='Comentar “pente 0 ou 1” + agendar no app com 50%.',
     precisa=['Cliente com as laterais crescidas (3 semanas ou mais sem cortar) que quer degradê',
              'Dica do Ed em 1 frase: o que ele faz pra não marcar linha (perguntar antes de gravar)',
              'Tripé, luz de lado, lapela, escova de nuca, espelho de mão, capa com o logo',
              'Cronometrar o corte do início ao fim (número do gancho C)'],
     ganchos=[('Começa no fim', 'No fim do corte: PD da nuca pronta, celular parado a 20 cm. A mão do Ed entra com a escova e passa de baixo pra cima. 3 s. Na edição, corte seco pro antes.',
               '“Nenhuma linha marcada. Volta comigo do zero.”'),
              ('Ed provoca', 'Antes do corte: PM do Ed de pé atrás do cliente, máquina ligada na mão, olhando pra lente. Grava 3 vezes.',
               'Ed: “Degradê que marca linha é degradê mal feito. Olha.”'),
              ('Som primeiro', 'PD da máquina encostando na nuca, som alto, sem música por cima no primeiro segundo.',
               '“[X] minutos de cadeira em 30 segundos.” (tempo real cronometrado)')],
     tomadas=[('0–2 s', 'Gancho', 'A, B ou C', 'Ver página anterior.', []),
              ('2–4 s', 'Antes', 'PM', 'Cliente sentado com a capa, de perfil. Gira a cadeira devagar uns 90°.', [('TELA', 'ANTES')]),
              ('4–6 s', 'Primeira passada', 'PD', 'Máquina subindo na lateral. Tripé na altura da orelha, a 40 cm.', []),
              ('6–8 s', 'Troca de pente', 'PD', 'Pente encaixando na máquina.', []),
              ('8–10 s', 'Esfumado', 'PD', 'O movimento de concha na transição, onde o degradê some.', []),
              ('10–12 s', 'Nuca', 'PD', 'Nuca vista de trás, máquina descendo.', []),
              ('12–16 s', 'Dica do Ed', 'PP', 'Ed trabalhando e olhando pro corte. A fala vai com a lapela.', [('FALA', 'A dica dele, em 1 frase'), ('TELA', 'Resumo da dica em até 6 palavras')]),
              ('16–20 s', 'Tesoura', 'PM', 'Tesoura no topo: 2 cortes de 2 s.', []),
              ('20–24 s', 'Contorno', 'PD 60 fps', 'Navalha no contorno da orelha e da nuca.', []),
              ('24–30 s', 'Revelação', 'PA → PD', 'Ed gira a cadeira pro espelho, o cliente passa a mão na nuca. Termina no mesmo PD da nuca do gancho A, pra o vídeo emendar no começo.', [('TELA', CAMP)])],
     edicao=['Cortes no ritmo da batida, de 1,5 a 2 s cada.', 'Zoom leve (105%) nos PD pra dar movimento.',
             'Legenda da fala do Ed na tela.', 'O último quadro tem que casar com o primeiro (o vídeo volta sozinho sem parecer que acabou).',
             'Sem marca d’água de app.'],
     audio='Som real da máquina em 100% e música em alta da semana bem baixa (uns 30%). Na dica do Ed, a voz dele na frente.',
     capa='Frame da nuca pronta + “DEGRADÊ SEM MARCA” no meio da tela.',
     leg='Degradê sem marca, do zero ao acabamento. ✂️\nNa lateral tu vai de pente 0 ou 1? Comenta que o Ed responde.\n\nPrimeiro corte na ED? De segunda a quarta sai com 50% agendando pelo app. Link na bio.\n📍 Rua Paula Batista, 604 · Casa Amarela\n\n#degrade #barbeariarecife #casaamarela #edbarbearia',
     depois=['Responder todo comentário na primeira hora.', 'Comentar e fixar: “Pente 0 ou 1? 👇”.',
             'Stories de 10/11: compartilhar o Reels com o link de agendar.']),

dict(cod='R2', titulo='Chegou pedindo socorro', dur='25 a 35 s',
     tags=[('grava 04/11 qua', 'am'), ('posta 14/11 sáb 18h30', ''), ('antes e depois', '')],
     obj='Mostrar a transformação e gerar indicação (um amigo marca o outro).',
     pub='Quem está adiando o corte, e os amigos que marcam essa pessoa.',
     cta='Marcar o amigo que tá precisando + 50% no 1º corte.',
     precisa=['Cliente com cabelo e barba bem crescidos (2 meses ou mais), que topa falar 1 frase',
              'Fita crepe no chão marcando cadeira e tripé', 'Espelho de mão e lapela',
              'Segundo celular pro timelapse (se não tiver, faz 6 cortes rápidos)', 'Anotar o @ do cliente'],
     ganchos=[('O cliente fala', 'Antes de tudo, PP do cliente na cadeira. Pergunta de fora da câmera: “Faz quanto tempo que tu não corta?” Grava a resposta real, sem escrever fala pra ele. Ed responde de fundo.',
               'Cliente: “Faz [X] meses...” · Ed: “Deixa comigo.”'),
              ('Carta branca', 'Texto sobre a imagem do antes. Só usa se ele disse isso mesmo: pergunta antes.',
               '“Ele pediu: faz o que tu achar melhor.”'),
              ('Spoiler', 'Feito na edição: 1 s do antes e do depois lado a lado, e volta pro antes.',
               '“Mesmo cara. Mesmo dia.”')],
     tomadas=[('0–3 s', 'Gancho', 'A, B ou C', 'Ver página anterior.', []),
              ('3–4,5 s', 'Antes: frente', 'PM', 'Câmera na altura dos olhos, cadeira na marca.', [('TELA', 'ANTES')]),
              ('4,5–6 s', 'Antes: perfil', 'PM', 'Cadeira girada 90°.', []),
              ('6–7 s', 'Antes: nuca', 'PM', 'Cadeira de costas.', []),
              ('7–10 s', 'O plano', 'PM', 'Ed de pé ao lado, mão no cabelo do cliente.', [('FALA', 'Ed, em 1 frase: “Vou baixar a lateral, tirar volume e desenhar a barba.” (com as palavras dele)')]),
              ('10–13 s', 'Timelapse', 'PA', 'Segundo celular no modo timelapse, pegando o corte inteiro.', []),
              ('13–19 s', 'Cortes rápidos', 'PD', '4 cortes de 1,5 s: máquina, tesoura, barba na máquina, navalha.', []),
              ('19–21 s', 'Transição', 'PM', 'Ed sacode a capa na frente da lente até tampar. No depois, grava a capa saindo da lente.', []),
              ('21–28 s', 'Depois: 3 ângulos', 'PM', 'Frente, perfil e nuca, no mesmo lugar e na mesma luz do antes.', [('TELA', 'DEPOIS')]),
              ('28–32 s', 'Reação', 'PP', 'Espelho de mão. Deixa ele falar o que quiser. Não pede reação.', [('TELA', 'Teu amigo precisa? 1º corte com 50%, seg a qua')])],
     edicao=['Mesma cor no antes e no depois. Não escurece o antes pra parecer pior.',
             'Antes e depois com o mesmo enquadramento: alinhar na edição se precisar.',
             'Timelapse acelerado até caber em 3 s.', 'Transição da capa exatamente no quadro em que a lente fica tampada.'],
     audio='Música em alta da semana. Abaixa a música quando o cliente fala (gancho A e reação).',
     capa='Antes e depois em tela dividida + “CHEGOU PEDINDO SOCORRO”.',
     leg='Chegou pedindo socorro, saiu pronto pra foto.\nMarca aquele amigo que tá precisando 👇 O primeiro corte dele na ED sai com 50% de segunda a quarta, agendando pelo app. Link na bio.\n\n#antesedepois #barbeariarecife #casaamarela #edbarbearia',
     depois=['Convidar o cliente como colaborador no post (o Reels aparece pros seguidores dele).',
             'Marcar o cliente e o barbeiro.', 'Stories de 14/11: compartilhar com o link de agendar.']),

dict(cod='R3', titulo='O Ed responde: qual corte pro teu rosto', dur='30 a 45 s',
     tags=[('grava 11/11 qua', 'am'), ('posta 17/11 ter 18h30', ''), ('o Ed como rosto da marca', '')],
     obj='Autoridade do Ed e conversa no direct (cada selfie é um possível cliente).',
     pub='Quem não sabe que corte pedir.',
     cta='Comentar ROSTO e mandar selfie no direct.',
     precisa=['Só o Ed, com lapela. Gravar antes dos clientes chegarem.',
              '3 referências: clientes do dia ou fotos do ensaio/arquivo com autorização (rosto redondo, quadrado, alongado)',
              'Fundo com o logo da parede',
              'Antes de gravar, o Ed fala livre por 2 min sobre os 3 formatos. As frases saem dali, sem decorar.'],
     ganchos=[('Proibido', 'PM do Ed olhando pra lente, apontando pra câmera.', 'Ed: “Rosto redondo? Para de pedir esse corte.” (foto do corte na tela)'),
              ('Promessa', 'PM do Ed, braços cruzados.', 'Ed: “Teu corte pode estar errado pro teu rosto. Em 30 segundos tu descobre.”'),
              ('Escolha', 'PM do Ed segurando 3 fotos impressas, uma em cada mão e uma no peito.', 'Ed: “Qual desses é tu?”')],
     tomadas=[('0–3 s', 'Gancho', 'PM', 'Ver página anterior.', []),
              ('3–11 s', 'Rosto redondo', 'PM', 'Ed explica o que fazer e o que evitar.', [('TELA', 'REDONDO'), ('INSERTO', 'Foto ou cliente com o corte indicado, entrando do lado')]),
              ('11–19 s', 'Rosto quadrado', 'PM', 'Mesma estrutura.', [('TELA', 'QUADRADO'), ('INSERTO', 'Referência')]),
              ('19–27 s', 'Rosto alongado', 'PM', 'Mesma estrutura.', [('TELA', 'ALONGADO'), ('INSERTO', 'Referência')]),
              ('27–33 s', 'Fecho', 'PP', 'Ed chega mais perto da câmera.', [('FALA', '“Não sabe o teu? Comenta ROSTO que eu te digo.”')]),
              ('extra', 'Cobertura', 'PD', '10 s de mãos do Ed penteando e cortando, pra cobrir os cortes da fala.', [])],
     edicao=['Corte seco a cada frase, tirando as pausas.', 'Zoom de 110% nas frases mais fortes.',
             'Legenda palavra por palavra, grande, no meio da tela.', 'Referência entra deslizando do lado em cada formato.'],
     audio='Só a voz do Ed (lapela). Música bem baixa ou nenhuma.',
     capa='Ed apontando + “QUAL CORTE PRO TEU ROSTO?”.',
     leg='Qual é o formato do teu rosto? Comenta ROSTO e manda uma selfie de frente no direct que o Ed diz o corte. ✂️\nAgende pelo link da bio.\n\n#cortemasculino #barbeariarecife #casaamarela #edbarbearia',
     depois=['Responder cada ROSTO no direct em até 24 h, com a resposta do Ed.', 'Terminar a resposta com o link de agendar e o 50% de seg a qua.',
             'Anotar as dúvidas que se repetem: viram pauta de dezembro.']),

dict(cod='R4', titulo='Movimentos da navalha, parte 2', dur='25 a 35 s',
     tags=[('grava 11/11 qua', 'am'), ('posta 19/11 qui 18h30', ''), ('técnica · curso', '')],
     obj='Alcance (repetir os 16,6 mil views da parte 1) e levar pro curso.',
     pub='Barbeiros e curiosos. Atrai mais barbeiro do que cliente, por isso a chamada é o curso.',
     cta='Salvar + destaque CURSO.',
     precisa=['Assistir a parte 1 antes, pra repetir o enquadramento e não repetir movimento',
              'Ed escolhe os 3 movimentos e o nome de cada um antes de gravar',
              'Cliente pra contorno (barba ou cabelo), lâmina nova', 'Luz forte de lado, pra textura da pele e do pelo aparecer', '1080p 60 fps'],
     ganchos=[('Prova', 'PD da navalha abrindo.', '“O vídeo da navalha passou de 16 mil views. Faltaram esses 3.”'),
              ('Pedido', 'PP do Ed segurando a navalha.', 'Ed: “O movimento que mais me pedem pra ensinar é esse aqui.”'),
              ('Diferença', 'PD do contorno pronto.', '“3 movimentos de navalha que separam contorno bom de contorno perfeito.”')],
     tomadas=[('0–3 s', 'Gancho', 'PD', 'Ver página anterior.', []),
              ('3–5 s', 'Montagem', 'PD', 'Lâmina nova entrando na navalha.', []),
              ('5–11 s', 'Movimento 1', 'PD 60 fps', 'Movimento inteiro, sem cortar no meio.', [('TELA', '1/3 · [nome do movimento]'), ('FALA', 'Ed narra o nome e pra que serve')]),
              ('11–17 s', 'Movimento 2', 'PD 60 fps', 'Mesma estrutura.', [('TELA', '2/3 · [nome]')]),
              ('17–23 s', 'Movimento 3', 'PD 60 fps', 'Mesma estrutura.', [('TELA', '3/3 · [nome]')]),
              ('23–28 s', 'Resultado', 'PD', 'Contorno pronto, dedo passando na linha.', []),
              ('28–33 s', 'Chamada', 'PP', 'Ed olhando pra lente.', [('FALA', '“Quer aprender de verdade? Destaque CURSO.”')])],
     edicao=['Movimentos em câmera lenta (50%).', 'Numeração 1/3, 2/3, 3/3 sempre na tela: segura a pessoa até o 3.',
             'Mesma cor e mesmo estilo de texto da parte 1.'],
     audio='Voz do Ed e som real da navalha. Música bem baixa.',
     capa='Navalha de perto + “NAVALHA · PARTE 2”.',
     leg='Movimentos da navalha, parte 2. A parte 1 tá no perfil.\nSalva pra treinar depois. Quer aprender com o Ed? Destaque CURSO no perfil.\n\n#navalha #barbeiro #barbeariarecife #edbarbearia',
     depois=['Comentar na parte 1: “Saiu a parte 2, tá no perfil.”', 'Stories de 19/11: compartilhar.',
             'Não contar esse Reels como de agendamento no relatório.']),

dict(cod='R5', titulo='Agendou pelo app, sentou na hora', dur='20 a 30 s',
     tags=[('grava 11/11 qua', 'am'), ('posta 24/11 ter 18h30', ''), ('conversão', '')],
     obj='Converter: mostrar que agendar é fácil e que tem 50% de seg a qua.',
     pub='Quem já conhece a ED pelo Instagram e ainda não marcou.',
     cta='Agendar pelo app com 50%.',
     precisa=['Cliente novo que agendou pelo 50% pra 11/11 (pedir um da agenda ao Ed e confirmar autorização pelo WhatsApp antes)',
              'Gravação de tela: celular da equipe fazendo um agendamento de verdade (depois cancela). Esconder nome e telefone.',
              'Relógio ou celular mostrando a hora quando o cliente chegar',
              'Gravar no mesmo dia o depoimento dele (10 a 15 s) pros stories de 24/11'],
     ganchos=[('Rapidez', 'Gravação de tela com cronômetro na edição.', '“Agendei em 10 segundos. Sentei na hora marcada.”'),
              ('POV', 'PA da cadeira vazia esperando, visão de quem entra.', '“POV: tu chegou na barbearia e não tinha ninguém na tua frente.”'),
              ('Diálogo', 'PA da porta: cliente põe a cabeça pra dentro.', 'Cliente: “Tem horário?” · Ed: “Tem no app.”')],
     tomadas=[('0–3 s', 'Gancho', 'tela / PA', 'Ver página anterior.', []),
              ('3–10 s', 'Agendamento', 'tela', 'Link da bio → serviço → horário → confirmar.', [('TELA', 'Cronômetro + círculo onde o dedo toca')]),
              ('10–12 s', 'Chegada', 'PA', 'De dentro, o cliente entra pela porta.', []),
              ('12–13 s', 'Hora certa', 'PD', 'Celular ou relógio com a mesma hora do agendamento.', []),
              ('13–14 s', 'Senta direto', 'PM', 'Ed puxa a cadeira, ele senta.', []),
              ('14–22 s', 'Corte', 'PD', '4 cortes de 2 s.', []),
              ('22–28 s', 'Resultado', 'PM', 'Cliente se olhando no espelho.', [('TELA', CAMP)])],
     edicao=['Cronômetro parando no “confirmar”.', 'Som de notificação no “confirmar”.',
             'Cortes rápidos na chegada: a ideia é “não esperou nada”.'],
     audio='Música em alta da semana + som de notificação.',
     capa='Celular com o app + “SEM FILA”.',
     leg='Sem fila e sem esperar resposta no WhatsApp: 3 toques no app e a cadeira é tua.\nDe segunda a quarta, o primeiro corte sai com 50%. Link na bio.\n\n#barbeariarecife #casaamarela #edbarbearia',
     depois=['Stories de 24/11: compartilhar + depoimento do cliente.', 'Fixar comentário: “Link na bio, 50% de seg a qua”.']),

dict(cod='R6', titulo='Barba completa: o ritual', dur='20 a 30 s',
     tags=[('grava 25/11 qua', 'am'), ('posta 28/11 sáb 18h30', ''), ('experiência', '')],
     obj='Mostrar a experiência da barba e vender o combo cabelo + barba (R$ 80).',
     pub='Quem faz a barba em casa ou só passa a máquina.',
     cta='Agendar cabelo + barba.',
     precisa=['Cliente de barba cheia', 'Toalha quente testada antes: o vapor tem que aparecer',
              'Fundo escuro atrás do rosto (o vapor aparece contra o escuro), luz de lado',
              'Espuma ou óleo, navalha com lâmina nova', 'Celular perto pra pegar o som (ASMR), 60 fps na navalha'],
     ganchos=[('Vapor', 'PD da toalha saindo do rosto, vapor subindo.', '“Isso aqui não é só fazer a barba.”'),
              ('Som', 'PD da navalha, sem música.', '“Liga o som.”'),
              ('Comparação', 'PM do Ed com a toalha na mão.', 'Ed: “Barba de 5 minutos na máquina, ou isso aqui?”')],
     tomadas=[('0–3 s', 'Gancho', 'PD', 'Ver página anterior.', []),
              ('3–8 s', 'Toalha quente', 'PM', 'Ed coloca a toalha no rosto do cliente.', []),
              ('8–12 s', 'Espuma ou óleo', 'PD', 'Mãos do Ed espalhando.', []),
              ('12–20 s', 'Navalha', 'PD 60 fps', 'Navalha desenhando a linha da bochecha e do pescoço.', []),
              ('20–25 s', 'Acabamento', 'PD', 'Pente, tesoura e finalização.', []),
              ('25–28 s', 'Resultado', 'PP', 'Cliente passa a mão na barba.', [('TELA', 'Cabelo + barba R$ 80')])],
     edicao=['Ritmo mais lento que os outros: tomadas de 2 a 3 s.', 'Câmera lenta na navalha e no vapor.', 'Cor quente, sem exagero.'],
     audio='Som real na frente (toalha, espuma, navalha). Música bem baixa ou nenhuma.',
     capa='Toalha com vapor + “O RITUAL DA BARBA”.',
     leg='O ritual da barba na ED: toalha quente, navalha e acabamento sem pressa.\nBarba R$ 40. Cabelo + barba R$ 80 (tu economiza R$ 10). Agende pelo link da bio.\n\n#barba #barbeariarecife #casaamarela #edbarbearia',
     depois=['Stories de 28/11: compartilhar + “Dezembro lota: já dá pra marcar”.']),

dict(cod='R7', titulo='Pai e filho na mesma cadeira', dur='25 a 35 s',
     tags=[('grava 25/11 qua', 'am'), ('posta 30/11 seg 18h30', ''), ('família · kids', '')],
     obj='Mostrar o espaço kids e abrir a agenda de dezembro.',
     pub='Pais de Casa Amarela.',
     cta='Votar 1 ou 2 nos comentários + agenda de dezembro.',
     precisa=['Pai e filho agendados juntos até 18/11', 'Autorização dos pais por escrito',
              'Espaço kids arrumado antes', 'Se a criança não quiser ser filmada, não grava'],
     ganchos=[('Votação', 'Gravado no final: os dois lado a lado no espelho, cortes prontos.', '“Quem ficou melhor? Vota: 1 ou 2.” (número em cima de cada um)'),
              ('Fala do filho', 'PP do filho olhando o pai. Só se sair natural.', 'Filho: “Pai, agora a gente tá igual.”'),
              ('Programa', 'PA dos dois entrando.', '“O programa deles de pai e filho é aqui.”')],
     tomadas=[('0–3 s', 'Gancho', 'PM', 'Ver página anterior.', []),
              ('3–6 s', 'Chegada', 'PA', 'Os dois entrando juntos pela porta.', []),
              ('6–10 s', 'Espaço kids', 'PA', 'A sala de super-heróis, o filho sentando.', []),
              ('10–15 s', 'Corte do filho', 'PD + PP', 'Corte e a cara da criança.', []),
              ('15–24 s', 'Corte do pai', 'PD', '3 cortes de 3 s.', []),
              ('24–30 s', 'Espelho', 'PM', 'Os dois lado a lado no espelho.', [('TELA', '1 e 2 em cima de cada um + “A agenda de dezembro já tá aberta”')])],
     edicao=['Música leve.', 'Números 1 e 2 no gancho e no final.', 'Reação da criança vale mais que o corte: deixa durar.'],
     audio='Música em alta, leve.',
     capa='Os dois no espelho + “PAI E FILHO”.',
     leg='Pai e filho, mesma cadeira. Quem ficou melhor: 1 ou 2? 👇\nDezembro lota rápido e a agenda já tá aberta no app. Link na bio.\n\n#paiefilho #barbeariarecife #casaamarela #edbarbearia',
     depois=['Convidar o pai como colaborador no post.', 'Stories de 30/11: compartilhar + “agenda de dezembro aberta”.']),
]
for r in R:
    reel(r)

n = len(pages)
html = ''.join(
    f'<section class="pg {c}"><div class="ey">{e}</div>{b}<div class="foot"><span>ED BARBEARIA × HOUSE DO CREATOR</span><span>{i + 1:02d} / {n:02d}</span></div></section>'
    for i, (e, b, c) in enumerate(pages))
open('roteiros.html', 'w').write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>ED Barbearia · Roteiros dos Reels · Novembro 2026</title>
<link rel="stylesheet" href="../../fonte/fonts.css"><style>{CSS}</style></head><body>{html}</body></html>''')
print(n, 'páginas')
