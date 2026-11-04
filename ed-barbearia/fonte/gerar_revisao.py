# Gera revisao.html: revisão do plano de novembro da ED Barbearia + roteiros.
# PDF: node render_celular.js revisao  (página 540x960, pra ler no celular)

CSS = '''
@page{size:540px 960px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0e0e0e;color:#f2f0ea;font-family:Poppins,sans-serif;font-size:13.5px;line-height:1.45}
.pg{width:540px;height:960px;padding:34px 30px 30px;position:relative;overflow:hidden;page-break-after:always;background:#0e0e0e}
.pg.y{background:#f5cf4a;color:#111}
.ey{font-size:9.5px;letter-spacing:.2em;font-weight:700;color:#f5cf4a;text-transform:uppercase;margin-bottom:8px}
.pg.y .ey{color:#111}
h1{font-size:40px;line-height:1.05;font-weight:700;letter-spacing:-.02em;margin-bottom:14px}
h2{font-size:25px;line-height:1.1;font-weight:700;letter-spacing:-.01em;margin-bottom:6px}
h3{font-size:9.5px;letter-spacing:.18em;font-weight:700;color:#f5cf4a;text-transform:uppercase;margin:11px 0 5px}
.am{color:#f5cf4a}
.sub{color:#a9a69e;font-size:12.5px;margin-bottom:12px}
.meta{display:flex;gap:6px;flex-wrap:wrap;margin:4px 0 6px}
.tag{font-size:9.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:3px 8px;border-radius:20px;background:#222;color:#d9d6ce}
.tag.am{background:#f5cf4a;color:#111}
.tag.az{background:#3b6ff5;color:#fff}
.card{background:#1a1a1a;border-radius:12px;padding:9px 12px;margin-bottom:6px}
.card.dest{border:1.5px solid #f5cf4a}
.card b.k{color:#f5cf4a;font-size:10px;letter-spacing:.12em;margin-right:6px}
.g{display:grid;grid-template-columns:auto 1fr;gap:5px 10px;align-items:baseline}
.t{font-weight:700;color:#f5cf4a;font-size:11.5px;white-space:nowrap}
ul{list-style:none}
li{padding-left:18px;position:relative;margin-bottom:5px}
li:before{content:'';position:absolute;left:2px;top:7px;width:7px;height:7px;border-radius:50%;background:#f5cf4a}
ol{list-style:none;counter-reset:n}
ol li{counter-increment:n;padding-left:26px}
ol li:before{content:counter(n);background:#f5cf4a;color:#111;width:18px;height:18px;top:1px;left:0;font-size:10.5px;font-weight:700;text-align:center;line-height:18px}
.leg{background:#1a1a1a;border-left:3px solid #f5cf4a;border-radius:0 10px 10px 0;padding:9px 12px;font-size:12.5px;white-space:pre-line}
.nota{font-size:11.5px;color:#a9a69e}
.ok{color:#7fd38a;font-weight:700}
.x{color:#ff7a6b;font-weight:700}
table{width:100%;border-collapse:collapse;font-size:12px}
td,th{padding:7px 6px;border-bottom:1px solid #262626;vertical-align:top;text-align:left}
th{font-size:9px;letter-spacing:.14em;color:#8a877f;text-transform:uppercase}
td.d{font-weight:700;white-space:nowrap}
tr.vis td{background:#1d1b12}
.foot{position:absolute;left:30px;right:30px;bottom:18px;display:flex;justify-content:space-between;font-size:8.5px;letter-spacing:.16em;color:#666;font-weight:700}
.pg.y .foot{color:#6b5a14}
.pg.y ol li:before{background:#111;color:#f5cf4a}
.big{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;letter-spacing:-.01em}
'''

TOTAL = [0]
pages = []


def pg(eyebrow, body, cls=''):
    pages.append((eyebrow, body, cls))


def lst(items, ordered=False):
    tag = 'ol' if ordered else 'ul'
    return f'<{tag}>' + ''.join(f'<li>{i}</li>' for i in items) + f'</{tag}>'


def cenas(rows):
    return '<div class="g">' + ''.join(f'<span class="t">{t}</span><span>{d}</span>' for t, d in rows) + '</div>'


def ganchos(opts):
    out = ''
    for i, (letra, txt) in enumerate(opts):
        cls = 'card dest' if i == 0 else 'card'
        rot = f'{letra} · RECOMENDADO' if i == 0 else letra
        out += f'<div class="{cls}"><b class="k">{rot}</b>{txt}</div>'
    return out


def reel(cod, titulo, tags, problema, opts, cena_rows, audio, capa, legenda, extra=None):
    tg = ''.join(f'<span class="tag {c}">{t}</span>' for t, c in tags)
    body = f'''<h2><span class="am">{cod}</span> · {titulo}</h2>
<div class="meta">{tg}</div>
{f'<p class="nota" style="margin-top:4px">{problema}</p>' if problema else ''}
<h3>Gancho (0 a 3 s) · grava as 3 aberturas</h3>{ganchos(opts)}
<h3>Cenas</h3>{cenas(cena_rows)}
<h3>Áudio e capa</h3><p style="font-size:12.5px">{audio}<br><b>Capa:</b> {capa}</p>
<h3>Legenda</h3><div class="leg">{legenda}</div>
{f'<h3>Não esquecer</h3>{lst(extra)}' if extra else ''}'''
    pg(f'Roteiro · {cod}', body)


# ---------- 1. capa ----------
pg('ED Barbearia × House do Creator · revisão do plano', '''
<div style="height:120px"></div>
<h1 style="font-size:50px">Visitas na quarta.<br><span class="am">Roteiros com gancho.</span></h1>
<p class="sub" style="font-size:14px">Revisão do plano de novembro: o que mudou, o que melhorar, roteiro de set pra hoje (R1 e R2) e os 7 Reels reescritos.</p>
<div style="height:30px"></div>
<div class="card"><b class="k">HOJE</b>04/11 · quarta · Visita 1 · meta: <b>2 Reels gravados</b></div>
<div class="card"><b class="k">VISITAS</b>04/11, 11/11, 18/11 e 25/11 · todas na quarta</div>
<div class="card"><b class="k">NESTE PDF</b>
<div style="margin-top:6px">''' + lst([
    'Checklist de set de hoje',
    'R1 e R2: roteiro de gravação completo',
    'Cronograma novo e por que quarta',
    'Avaliação do plano: o que manter e o que mudar',
    'R3 a R7 reescritos',
    'Stories dos dias que trocaram',
    'Pendências pra fechar com o Ed hoje',
]) + '</div></div>')

# ---------- 2. set de hoje ----------
pg('Hoje · 04/11 · quarta · Visita 1', '''
<h2>Set de hoje: <span class="am">R1 e R2.</span></h2>
<p class="sub">A reunião de pauta era 05/11, depois da gravação. Aprova a pauta com o Ed hoje, antes de ligar a câmera.</p>
<h3>Ordem de gravação</h3>''' + lst([
    '<b>15 min com o Ed:</b> aprovar a pauta, autorização de imagem dos 2 clientes, e pegar a dica dele de degradê em 1 frase (vai no R1).',
    '<b>Montar o set:</b> tripé, luz de lado (janela ou espelho), fundo com o logo da parede em pelo menos 1 plano. Marcar com fita o lugar da cadeira e do tripé.',
    '<b>Gravar o ANTES dos 2 clientes</b> antes de qualquer corte. O antes não tem segunda chance.',
    '<b>R1 completo</b> com o cliente do degradê.',
    '<b>R2 completo</b> com o cliente de cabelo e barba grandes.',
    '<b>As 3 aberturas de cada Reels</b> (A, B e C). A gente escolhe na edição.',
    '<b>10 min de imagem extra:</b> porta abrindo, máquina ligando, ferramentas na bancada, Ed rindo com cliente, logo da parede. Vira story e Reels depois.',
    '<b>3 stories do dia</b> (página “Stories trocados”).',
], ordered=True) + '''
<h3>Celular</h3>''' + lst([
    '4K 30 fps. Pra câmera lenta da navalha: 1080p 60 fps.',
    'Lente 1x, nunca 0,5 (deforma o rosto). Limpar a lente.',
    'Segurar o dedo na tela pra travar foco e luz. Modo avião ligado.',
]) + '''
<div class="card dest" style="margin-top:10px"><b class="k">PLANO B</b>Se o cliente do R2 não chegar com cabelo e barba bem crescidos, grava o <b>R3</b> (só precisa do Ed) e o R2 passa pra 11/11. Ele sai em 14/11, ainda dá tempo de editar.</div>
''')

# ---------- 3. R1 ----------
reel('R1', 'Degradê sem marca', [('grava hoje 04/11', 'am'), ('posta ter 10/11', ''), ('25 a 30 s', '')],
     'Antes: “Do zero ao degradê em 30 segundos”. Dizia o formato, mas não dava motivo pra ficar. A abertura nova começa no resultado e volta pro início.',
     [('A', 'Abre no resultado: close da nuca pronta, Ed passando a escova. Texto: <b>“Nenhuma linha marcada. Volta comigo do zero.”</b> Corte seco pro cliente antes.'),
      ('B', 'Ed pra câmera, máquina ligada na mão: <b>“Degradê que marca linha é degradê mal feito. Olha.”</b>'),
      ('C', 'Máquina encostando na nuca, som alto. Texto: <b>“40 minutos de cadeira em 30 segundos.”</b> (trocar pelo tempo real)')],
     [('0–2 s', 'Gancho'),
      ('2–4 s', 'Cliente de perfil, antes. Texto: ANTES'),
      ('4–12 s', 'Máquina abrindo o degradê: 4 cortes de 2 s (lateral, pente, esfumado, nuca). Tripé na altura da orelha.'),
      ('12–16 s', 'Dica do Ed em 1 frase, com a voz dele por cima. Texto na tela resume a dica.'),
      ('16–20 s', 'Tesoura no topo'),
      ('20–24 s', 'Contorno na navalha, bem de perto'),
      ('24–30 s', 'Giro da cadeira até o espelho, cliente passa a mão. Último quadro igual ao primeiro (o vídeo volta sozinho). Texto: <b>Seg a qua: 50% no 1º corte pelo app</b>')],
     'Som real da máquina alto, música em alta bem baixa por baixo. Na dica do Ed, a voz dele na frente.',
     'nuca pronta + “DEGRADÊ SEM MARCA”.',
     'Degradê sem marca, do zero ao acabamento. ✂️\nNa lateral tu vai de pente 0 ou 1? Comenta que o Ed responde.\n\nPrimeiro corte na ED? De segunda a quarta sai com 50% agendando pelo app. Link na bio.\n📍 Rua Paula Batista, 604 · Casa Amarela')

# ---------- 4. R2 ----------
reel('R2', 'Chegou pedindo socorro', [('grava hoje 04/11', 'am'), ('posta sáb 14/11', ''), ('25 a 35 s', '')],
     'Antes: “Ele chegou assim...”. Todo antes e depois começa assim. Agora quem abre é o cliente, falando de verdade.',
     [('A', 'Cliente na cadeira, fala pra câmera (sem decorar): <b>“Faz [X] meses que eu não corto.”</b> Ed, de fundo: <b>“Deixa comigo.”</b>'),
      ('B', 'Texto sobre o antes: <b>“Ele pediu: faz o que tu achar melhor.”</b> Só se ele disse isso mesmo.'),
      ('C', 'Antes e depois lado a lado por 1 s. Texto: <b>“Mesmo cara. Mesmo dia.”</b> Volta pro antes.')],
     [('0–3 s', 'Gancho'),
      ('3–7 s', 'Antes em 3 ângulos: frente, perfil, nuca. Cadeira e tripé na marca de fita.'),
      ('7–10 s', 'Ed diz o plano em 1 frase (ex.: “baixar a lateral, tirar volume e desenhar a barba”)'),
      ('10–20 s', 'Corte acelerado: timelapse de 3 s + 4 cortes de 1,5 s (máquina, tesoura, barba, navalha)'),
      ('20–21 s', 'Transição: Ed sacode a capa na frente da lente'),
      ('21–28 s', 'Depois nos mesmos 3 ângulos, mesma luz, mesmo lugar'),
      ('28–32 s', 'Reação no espelho de mão. Deixa ele falar, não pede reação ensaiada. Texto: <b>Teu amigo precisa? 1º corte com 50%, seg a qua</b>')],
     'Música em alta + voz do cliente no gancho e na reação.',
     'antes e depois em tela dividida + “CHEGOU PEDINDO SOCORRO”.',
     'Chegou pedindo socorro, saiu pronto pra foto.\nMarca aquele amigo que tá precisando 👇 O primeiro corte dele na ED sai com 50% de segunda a quarta, agendando pelo app. Link na bio.',
     ['Anotar o @ do cliente e convidar como <b>colaborador</b> no post: o Reels aparece também pros seguidores dele.'])

# ---------- 5. cronograma ----------
rows = [
    ('04/11 qua', 'Visita 1 · Reels', 'Aprova a pauta + grava R1 e R2 + stories', True),
    ('09/11 seg', 'Perfil novo', 'Bio, 8 destaques, A1 fixada, campanha começa', False),
    ('11/11 qua', 'Visita 2 · Reels', 'Grava R3, R4 e R5 + stories', True),
    ('18/11 qua', 'Visita 3 · Fotos', 'Ensaio: cortes, ambiente, equipe e o Ed', True),
    ('25/11 qua', 'Visita 4 · Reels', 'Grava R6 e R7 + stories', True),
    ('30/11 seg', 'Relatório', 'Números do mês e pauta de dezembro', False),
]
tr = ''.join(f'<tr class="{"vis" if v else ""}"><td class="d">{d}</td><td><b>{a}</b></td><td>{b}</td></tr>' for d, a, b, v in rows)
pg('Cronograma novo', f'''
<h2>Toda visita <span class="am">na quarta.</span></h2>
<p class="sub">Continuam 4 visitas e 3 diárias de Reels. A ordem dos posts no feed não muda.</p>
<table><thead><tr><th>Dia</th><th>O quê</th><th>Detalhe</th></tr></thead><tbody>{tr}</tbody></table>
<h3>O que mudou de data</h3>
<table><thead><tr><th></th><th>Antes</th><th>Agora</th></tr></thead><tbody>
<tr><td class="d">Pauta</td><td>05/11 qui</td><td><b>04/11</b>, no começo da visita</td></tr>
<tr><td class="d">Visita 1</td><td>06/11 sex · R1, R2, R3</td><td><b>04/11</b> · R1 e R2</td></tr>
<tr><td class="d">Visita 2</td><td>13/11 sex · R4, R5</td><td><b>11/11</b> · R3, R4 e R5</td></tr>
<tr><td class="d">Visita 3</td><td>19/11 qui · fotos</td><td><b>18/11</b> · fotos</td></tr>
<tr><td class="d">Visita 4</td><td>25/11 qua</td><td>sem mudança</td></tr>
</tbody></table>
<h3>Por que quarta é melhor</h3>''' + lst([
    '<b>É dia vazio.</b> A gravação não toma horário de cliente pagante do Ed.',
    '<b>É dia de campanha.</b> Dá pra gravar cliente que veio pelo 50%. O R5 e o depoimento dos stories ficam reais.',
    '<b>Cada gravação tem 6 dias até a postagem</b> de terça (R3 e R5): dá tempo de editar e aprovar.',
    '<b>O ensaio vem 1 dia antes</b> (18/11). Sobra mais tempo pra trocar as fotos provisórias da A1 e da A4.',
]))

# ---------- 6. avaliação ----------
pg('Avaliação do plano', '''
<h2>O que manter e <span class="am">o que mudar.</span></h2>
<h3>Está bom, manter</h3>''' + lst([
    'Tudo do contrato com data e responsável.',
    'Campanha com mecânica, peças e métrica definidas.',
    'Stories com pauta por dia pra equipe, com modelos prontos.',
    'Perfil novo: bio, 8 destaques e fixados que vendem.',
]) + '''<h3>Mudar</h3>''' + lst([
    '<b>Gancho só em texto é fraco.</b> Agora todo Reels abre com fala ou ação, e tem 3 aberturas pra testar. Se der, posta uma como Reels de teste (só pra quem não segue).',
    '<b>“Agende pelo link da bio” em todas as legendas cansa.</b> Cada legenda agora pede um comentário antes (pente 0 ou 1, ROSTO, 1 ou 2). Comentário aumenta o alcance e mostra quem quer agendar.',
    '<b>R4 atrai mais barbeiro do que cliente.</b> Os 16,6 mil views eram de gente que quer aprender. Bom pra alcance e pro curso, mas não conta como Reels de agendamento.',
    '<b>“Áudio em alta” em todos</b> não serve quando o Ed fala (R3 e R4). Nesses vai a voz dele com legenda na tela.',
    '<b>Como conferir o 50%?</b> Falta definir como a equipe sabe que é o 1º corte do cliente: cupom no app, se tiver, ou cadastro novo. Sem isso, o relatório não fecha.',
    '<b>Collab com o cliente</b> nos Reels de antes e depois (R2 e R7). Alcance de graça.',
    '<b>Paleta:</b> as artes estão no amarelo vivo e o estudo novo sugere dourado seco (#C9A24A). Tem que decidir antes de 09/11, porque se mudar dá pra refazer as artes antes do perfil novo.',
]))

# ---------- 7-11. R3 a R7 ----------
reel('R3', 'O Ed responde: qual corte pro teu rosto', [('grava 11/11', 'az'), ('posta ter 17/11', ''), ('30 a 45 s', '')],
     'O gancho já era bom. Agora fecha pedindo comentário e direct, e as perguntas viram pauta do “Pergunte ao Ed” (15 e 16/11).',
     [('A', 'Ed pra câmera, apontando: <b>“Rosto redondo? Para de pedir esse corte.”</b> Foto do corte aparece na tela.'),
      ('B', 'Ed: <b>“Teu corte pode estar errado pro teu rosto. Em 30 segundos tu descobre.”</b>'),
      ('C', 'Ed segurando 3 fotos: <b>“Qual desses é tu?”</b>')],
     [('0–3 s', 'Gancho'),
      ('3–30 s', 'Para cada formato (redondo, quadrado, alongado): nome grande na tela, cliente real ou foto do ensaio ao lado, e o Ed diz o que fazer e o que evitar, com as palavras dele.'),
      ('30–35 s', 'Ed: <b>“Não sabe o teu? Comenta ROSTO que eu te digo.”</b>')],
     'Voz do Ed com microfone de lapela, música bem baixa ou nenhuma. Legenda na tela o tempo todo (muita gente assiste sem som).',
     'Ed apontando + “QUAL CORTE PRO TEU ROSTO?”.',
     'Qual é o formato do teu rosto? Comenta ROSTO e manda uma selfie de frente no direct que o Ed diz o corte. ✂️\nAgende pelo link da bio.')

reel('R4', 'Movimentos da navalha, parte 2', [('grava 11/11', 'az'), ('posta qui 19/11', ''), ('20 a 35 s', '')],
     'Antes: “Parte 2, porque vocês pediram”. Só funciona pra quem viu a parte 1. Quem chega pela primeira vez passa direto.',
     [('A', 'Navalha abrindo, bem de perto. Texto: <b>“O vídeo da navalha passou de 16 mil views. Faltaram esses 3.”</b>'),
      ('B', 'Ed: <b>“O movimento que mais me pedem pra ensinar é esse aqui.”</b>'),
      ('C', 'Texto: <b>“3 movimentos de navalha que separam contorno bom de contorno perfeito.”</b>')],
     [('0–3 s', 'Gancho'),
      ('3–5 s', 'Navalha sendo montada, lâmina nova'),
      ('5–25 s', '3 movimentos bem de perto, em câmera lenta (60 fps). Nome de cada um na tela, Ed narrando.'),
      ('25–30 s', 'Resultado do contorno'),
      ('30–33 s', 'Ed: <b>“Quer aprender de verdade? Destaque CURSO.”</b>')],
     'Voz do Ed + som real da navalha. Música bem baixa.',
     'navalha de perto + “NAVALHA · PARTE 2”.',
     'Movimentos da navalha, parte 2. A parte 1 tá no perfil.\nSalva pra treinar depois. Quer aprender com o Ed? Destaque CURSO no perfil.')

reel('R5', 'Agendou pelo app, sentou na hora', [('grava 11/11', 'az'), ('posta ter 24/11', ''), ('20 a 30 s', '')],
     'Grava numa quarta de campanha, com um cliente que agendou pelo 50% de verdade.',
     [('A', 'Tela do app com cronômetro na tela. Texto: <b>“Agendei em 10 segundos. Sentei na hora marcada.”</b>'),
      ('B', 'Texto: <b>“POV: tu chegou na barbearia e não tinha ninguém na tua frente.”</b>'),
      ('C', 'Cliente na porta: <b>“Tem horário?”</b> Ed: <b>“Tem no app.”</b>')],
     [('0–3 s', 'Gancho'),
      ('3–10 s', 'Tela gravada: link da bio → serviço → horário → confirmar. Cronômetro na tela. Esconder dados pessoais.'),
      ('10–14 s', 'Cliente entra pela porta, celular mostrando a hora, e senta direto'),
      ('14–24 s', 'Corte rápido: 4 cortes de 2 s'),
      ('24–28 s', 'Resultado. Texto: <b>Seg a qua: 50% no 1º corte pelo app</b>')],
     'Música em alta. Som de notificação no “confirmar”.',
     'celular com o app + “SEM FILA”.',
     'Sem fila e sem esperar resposta no WhatsApp: 3 toques no app e a cadeira é tua.\nDe segunda a quarta, o primeiro corte sai com 50%. Link na bio.')

reel('R6', 'Barba completa: o ritual', [('grava 25/11', 'az'), ('posta sáb 28/11', ''), ('20 a 30 s', '')],
     'Antes não tinha texto nem fala no gancho, só a imagem. Agora tem frase e o som entra como atração.',
     [('A', 'Toalha quente saindo do rosto com vapor, bem de perto. Texto: <b>“Isso aqui não é só fazer a barba.”</b>'),
      ('B', 'Som da navalha, sem música. Texto: <b>“Liga o som.”</b>'),
      ('C', 'Ed: <b>“Barba de 5 minutos na máquina, ou isso aqui?”</b>')],
     [('0–3 s', 'Gancho'),
      ('3–8 s', 'Toalha quente, luz de lado pro vapor aparecer'),
      ('8–12 s', 'Espuma ou óleo'),
      ('12–20 s', 'Navalha desenhando a linha, bem de perto'),
      ('20–25 s', 'Acabamento e finalização'),
      ('25–28 s', 'Cliente passa a mão na barba e sorri. Texto: <b>Cabelo + barba R$ 80</b>')],
     'Som real (toalha, espuma, navalha) na frente, música bem baixa.',
     'toalha com vapor + “O RITUAL DA BARBA”.',
     'O ritual da barba na ED: toalha quente, navalha e acabamento sem pressa.\nBarba R$ 40. Cabelo + barba R$ 80 (tu economiza R$ 10). Agende pelo link da bio.')

reel('R7', 'Pai e filho na mesma cadeira', [('grava 25/11', 'az'), ('posta seg 30/11', ''), ('25 a 35 s', '')],
     'O gancho já era bom. Agora pede voto nos comentários. Tem que agendar pai e filho com antecedência.',
     [('A', 'Pai e filho lado a lado, cortes prontos. Texto: <b>“Quem ficou melhor? Vota: 1 ou 2.”</b>'),
      ('B', 'Filho: <b>“Pai, agora a gente tá igual.”</b> Só se sair natural.'),
      ('C', 'Texto: <b>“O programa deles de pai e filho é aqui.”</b>')],
     [('0–3 s', 'Gancho'),
      ('3–6 s', 'Os dois chegando juntos'),
      ('6–15 s', 'Filho no espaço kids'),
      ('15–24 s', 'Pai na cadeira'),
      ('24–30 s', 'Os dois no espelho. Texto: <b>A agenda de dezembro já tá aberta</b>')],
     'Música em alta, leve.',
     'os dois no espelho + “PAI E FILHO”.',
     'Pai e filho, mesma cadeira. Quem ficou melhor: 1 ou 2? 👇\nDezembro lota rápido e a agenda já tá aberta no app. Link na bio.',
     ['Agendar pai e filho até 18/11.', 'Autorização dos pais por escrito antes de gravar.', 'Convidar o pai como colaborador no post.'])

# ---------- 12. stories ----------
st = [
    ('04/11 qua', 'Dia de gravação · V1', 'Bastidor da House gravando · Cliente do Reels antes · “Tem novidade chegando no perfil dia 9”', 'Enquete: degradê ou social? + link'),
    ('05/11 qui', 'Bastidor técnico', 'Sem mudança (sai a etiqueta PAUTA)', 'story-04 caixinha'),
    ('06/11 sex', 'Bom dia da ED', 'Abrindo a porta · 1º cliente · resultado do 1º corte · antes e depois do dia', 'story-03 + link'),
    ('11/11 qua', 'Último dia do 50% + V2', '“Só até hoje nesta semana” · bastidor da gravação · cliente que veio pelo 50% em 10 s', 'Contagem até 19h + link'),
    ('13/11 sex', 'Resultado do dia', 'Antes e depois de um cliente · resultado do dia · “sábado ainda tem horário”', 'story-03 + link'),
    ('18/11 qua', 'Ensaio + último dia do 50%', 'Bastidor das fotos · cada barbeiro se apresenta · “último dia do 50% nesta semana”', 'Enquete: qual barbeiro tu já conhece? + contagem'),
    ('19/11 qui', 'Espaço kids + R4', 'Criança na cadeira (autorização dos pais) · resultado com pai ou mãe · compartilhar R4', 'Link de agendar'),
]
trs = ''.join(f'<tr><td class="d">{a}</td><td><b>{b}</b><br><span class="nota">{c}</span><br><span class="am" style="font-size:11px">{d}</span></td></tr>' for a, b, c, d in st)
pg('Stories trocados', f'''
<h2>Stories que <span class="am">mudaram de dia.</span></h2>
<p class="sub">Os outros dias continuam iguais ao plano. O 25/11 já era quarta.</p>
<table><thead><tr><th>Dia</th><th>Tema · o que gravar · adesivo</th></tr></thead><tbody>{trs}</tbody></table>
''')

# ---------- 13. pendências ----------
pg('Pendências · fechar com o Ed hoje', '''
<h2>Antes de sair <span>da ED hoje.</span></h2>
<p class="sub" style="color:#3a3210">Leva 10 minutos e evita retrabalho no mês todo.</p>
''' + lst([
    '<b>Aprovar a pauta</b> com as visitas na quarta.',
    '<b>Feriado 20/11:</b> a ED abre ou fecha?',
    '<b>Quem posta os stories</b> em cada dia.',
    '<b>Como conferir o 50%</b> no app (é 1º corte mesmo?).',
    '<b>Paleta:</b> amarelo das artes atuais ou dourado seco do estudo novo? Decidir até 09/11.',
    '<b>Clientes de 11/11:</b> 1 de contorno na navalha (R4) e 1 cliente novo pelo 50% (R5). O R3 só precisa do Ed.',
    '<b>Modelos do ensaio de 18/11:</b> textured crop, degradê + barba e crop com fade (as fotos da A4).',
    '<b>Clientes de 25/11:</b> 1 de barba cheia (R6) e pai e filho (R7), com autorização.',
], ordered=True), 'y')

n = len(pages)
html = ''.join(
    f'<section class="pg {c}"><div class="ey">{e}</div>{b}<div class="foot"><span>ED BARBEARIA × HOUSE DO CREATOR</span><span>{i + 1:02d} / {n:02d}</span></div></section>'
    for i, (e, b, c) in enumerate(pages))
open('revisao.html', 'w').write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>ED Barbearia · Revisão do plano de novembro</title>
<link rel="stylesheet" href="../../fonte/fonts.css"><style>{CSS}</style></head><body>{html}</body></html>''')
print(n, 'páginas')
