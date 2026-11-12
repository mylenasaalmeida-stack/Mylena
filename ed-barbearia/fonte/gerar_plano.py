# Plano de conteúdo de novembro/2026 da ED Barbearia, versão revisada (visitas na quarta + roteiros novos).
# Gerar: python3 gerar_plano.py && node render_plano.js
Y = '#f5cf4a'

CSS = '''
@page{size:1389px 781px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0b0b0b;color:#f4f2ec;font-family:Poppins,sans-serif;font-size:14px;line-height:1.45}
.s{width:1389px;height:781px;padding:46px 82px 0;position:relative;overflow:hidden;page-break-after:always;background:#0b0b0b}
.s.y{background:#f5cf4a;color:#111}
.ey{font-size:11px;letter-spacing:.24em;font-weight:700;color:#f5cf4a;text-transform:uppercase}
.s.y .ey{color:#111}
.hc{position:absolute;right:82px;top:38px;width:50px}
h1{font-size:46px;line-height:1.08;font-weight:700;letter-spacing:-.03em;margin:22px 0 10px}
h1.sm{font-size:36px;margin:16px 0 8px}
.am{color:#f5cf4a}
.sub{color:#9c9a93;font-size:15.5px;max-width:760px;margin-bottom:26px}
.foot{position:absolute;left:82px;right:82px;bottom:22px;border-top:1px solid #222;padding-top:12px;display:flex;justify-content:space-between;font-size:9.5px;letter-spacing:.2em;font-weight:700;color:#666}
.s.y .foot{border-color:#d9b53a;color:#5d4c0d}
.grid{display:grid;gap:14px}
.c2{grid-template-columns:1fr 1fr}.c3{grid-template-columns:1fr 1fr 1fr}.c4{grid-template-columns:repeat(4,1fr)}
.card{background:#181818;border-radius:16px;padding:18px 22px}
.s.y .hc{filter:invert(1)}
.s.y .card{background:#0b0b0b;color:#f4f2ec}
.card h4{font-size:15px;font-weight:700;margin-bottom:4px}
.card p{color:#9c9a93;font-size:13px}
.k{font-size:10px;letter-spacing:.2em;font-weight:700;color:#f5cf4a;text-transform:uppercase;margin-bottom:10px;display:block}
ul.ck{list-style:none}
ul.ck li{padding-left:26px;position:relative;margin-bottom:7px;font-size:14px}
ul.ck li:before{content:'';position:absolute;left:3px;top:4px;width:11px;height:6px;border-left:2.5px solid #f5cf4a;border-bottom:2.5px solid #f5cf4a;transform:rotate(-45deg)}
.tag{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;padding:4px 10px;border-radius:20px;background:#262626;color:#cfccc4;margin:3px 4px 0 0}
.tag.y{background:#f5cf4a;color:#111}.tag.b{background:#3b6ff5;color:#fff}.tag.r{background:#e8604c;color:#fff}.tag.g{background:#333;color:#aaa}
table{width:100%;border-collapse:collapse}
td,th{text-align:left;vertical-align:top;padding:9px 8px;border-bottom:1px solid #222;font-size:13px}
th{font-size:10px;letter-spacing:.2em;color:#888;text-transform:uppercase;font-weight:700}
td.d{font-weight:700;font-size:15px;white-space:nowrap}
td.d small{display:block;font-weight:400;font-size:11px;color:#888}
td.t{font-weight:700;width:210px}
td.a{color:#f5cf4a;width:240px}
td.w{color:#c9c6be}
.thumbs{display:flex;gap:12px;align-items:flex-end}
.thumbs img{border-radius:10px;display:block}
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:7px}
.cal .h{font-size:10px;letter-spacing:.2em;color:#888;font-weight:700}
.cal .d{background:#181818;border-radius:10px;height:84px;padding:8px 10px;font-size:11px;line-height:1.3}
.cal .d.o{background:#121212;color:#555}
.cal .d b.n{font-size:13px;display:block;margin-bottom:3px}
.cal .d .tag{font-size:8px;padding:3px 8px;margin-top:4px}
.cal .d .p{font-weight:600}
.cal .d .p i{font-style:normal;color:#f5cf4a}
.tl{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;border-top:2px solid #262626;margin-top:16px;padding-top:0}
.tl>div{position:relative;padding-top:24px}
.tl>div:before{content:'';position:absolute;top:-10px;left:0;width:12px;height:12px;border-radius:50%;border:3px solid #f5cf4a;background:#0b0b0b}
.tl .dt{font-size:10.5px;letter-spacing:.18em;font-weight:700;color:#f5cf4a}
.tl h4{font-size:16px;margin:6px 0 4px;line-height:1.2}
.tl p{font-size:12.5px;color:#9c9a93}
.tl .new .dt:after{content:' · NOVO';color:#7fb3ff}
.r-meta{font-size:12px;color:#888;margin-bottom:2px}
.gh{background:#181818;border-radius:12px;padding:11px 15px;margin-bottom:8px;font-size:13.5px}
.gh.best{border:1.5px solid #f5cf4a}
.gh b.l{color:#f5cf4a;font-size:10px;letter-spacing:.16em;margin-right:6px}
.sc{display:grid;grid-template-columns:62px 1fr;gap:5px 10px;font-size:13px}
.sc .t{color:#f5cf4a;font-weight:700;font-size:12px}
.leg{background:#181818;border-left:3px solid #f5cf4a;border-radius:0 12px 12px 0;padding:11px 15px;font-size:13px;white-space:pre-line}
.note{font-size:12.5px;color:#9c9a93}
.ord td{font-size:14px;padding:10px 8px}
.badge{display:inline-block;font-size:10px;font-weight:700;padding:3px 9px;border-radius:12px;background:#2a2a2a;color:#ddd}
.badge.y{background:#f5cf4a;color:#111}
.fix{color:#f5cf4a;font-weight:700;font-size:11px;letter-spacing:.1em;text-align:right}
'''

slides = []
HC = '<img class="hc" src="img/logo-hc.png">'


def S(ey, body, cls='', hc=True):
    slides.append((ey, body, cls, hc))


def ck(items):
    return '<ul class="ck">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def img(n, w):
    return f'<img src="img/{n}.jpg" style="width:{w}px">'


# 1 capa ---------------------------------------------------------------
S('', f'''
<img src="img/capa.jpg" style="position:absolute;right:0;top:0;height:781px;width:722px;object-fit:cover">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,#0b0b0b 48%,rgba(11,11,11,.0) 75%)"></div>
<div style="position:relative">
<img src="img/logo-hc.png" style="width:82px;margin-top:20px">
<div class="ey" style="margin-top:62px">Plano de conteúdo · Novembro 2026 · versão revisada</div>
<h1 style="font-size:64px;margin-top:26px;line-height:1.06">Novembro é o mês<br>de <span class="am">encher a<br>cadeira.</span></h1>
<p class="sub" style="margin-top:50px;max-width:540px">Calendário do mês, visitas toda quarta, stories de todo dia pra equipe, roteiros dos 7 Reels com gancho, as 4 artes do feed, campanha Seg a Qua e perfil novo. Plano Essencial + campanha de bônus.</p>
<div style="border-top:1px solid #2a2a2a;width:540px;padding-top:16px;margin-top:30px"><b style="font-size:15px">Ryan Coimbra &amp; Fontenele</b><br><span class="note">CEOs · House do Creator</span></div>
</div>
<img src="img/logo-ed.png" style="position:absolute;right:82px;bottom:60px;width:160px">
''', hc=False)

# 2 o que mudou --------------------------------------------------------
S('O que mudou nesta versão', '''
<h1>Visitas na quarta. <span class="am">Reels com gancho.</span></h1>
<p class="sub">Revisão feita em 04/11, dia da primeira visita. Escopo, ordem do feed e artes continuam iguais.</p>
<div class="grid c3">
<div class="card"><span class="k">Agenda</span>''' + ck([
    'Visitas em <b>04, 11, 18 e 25/11</b>, todas na quarta',
    'Pauta aprovada com o Ed em 04/11, antes de gravar',
    'Ensaio de fotos passa pra 18/11',
    'Stories dos dias de visita trocados de lugar',
]) + '''</div>
<div class="card"><span class="k">Reels</span>''' + ck([
    'Todo Reels abre com fala ou ação, não só texto',
    '3 aberturas gravadas por Reels (A, B e C)',
    'Legenda pede comentário antes do “agende”',
    'Voz do Ed em primeiro plano quando ele fala',
    'Collab com o cliente no R2 e no R7',
]) + '''</div>
<div class="card"><span class="k">Por que quarta</span>''' + ck([
    'É dia vazio: a gravação não toma horário de cliente pagante',
    'É dia de campanha: dá pra gravar quem veio pelo 50%',
    '6 dias entre gravar e postar os Reels de terça',
    'Ensaio 1 dia antes: mais tempo pra trocar as fotos provisórias',
]) + '</div></div>')

# 3 escopo -------------------------------------------------------------
esc = [('4 visitas no mês (1 por semana)', '04/11, 11/11, 18/11 e 25/11 · todas na quarta'),
       ('3 diárias de Reels: 7 Reels', 'Visitas 1, 2 e 4 · R1 a R7 publicados de 10 a 30/11'),
       ('1 diária de fotos pro feed', 'Visita 3, 18/11 · fotos de A1, A4 e dos meses seguintes'),
       ('4 artes ou carrosséis', 'A1 a A4, prontas neste material'),
       ('Legendas, calendário e Stories', 'Calendário de 11 posts, legendas e pauta de stories de 04 a 30/11'),
       ('Bio e capas de destaques novas', 'No ar em 09/11, com 8 capas no padrão novo'),
       ('Relatório mensal', 'Entregue em 30/11, com o que vira pauta de dezembro'),
       ('Bônus: 1 campanha de vendas', 'Seg a Qua Cheia · 50% no 1º corte, de 09 a 30/11')]
S('Escopo · Plano Essencial', '<h1>Tudo que foi contratado, <span class="am">com data marcada.</span></h1>'
  '<p class="sub">Plano Essencial (R$ 1.000/mês) + uma campanha de vendas de bônus. Cada item do contrato tem dia e responsável neste material.</p>'
  '<div class="grid c2">' + ''.join(f'<div class="card"><h4>{a}</h4><p>{b}</p></div>' for a, b in esc) + '</div>')

# 4 campanha -----------------------------------------------------------
S('Campanha do mês · bônus', '''<h1>Seg a Qua Cheia: <span class="am">50% no 1º corte.</span></h1>
<p class="sub">Segunda a quarta são os dias mais vazios. A promoção que a ED já tem vira campanha do mês, com peça no feed, stories em todo dia de campanha e Reels apontando pro app.</p>
<div class="grid c3">
<div class="card"><span class="k">Mecânica</span>''' + ck([
    '50% no primeiro corte, agendando pelo app', 'Vale de segunda a quarta',
    'Período: 09 a 30/11 (10 dias de campanha)', 'Pedir ao cliente: “como conheceu a ED?”',
    'Combinar com o Ed como o app mostra que é o 1º corte']) + '''</div>
<div class="card"><span class="k">Peças</span>''' + ck([
    'A1 no feed, fixada em 09/11', 'Story-01 e story-02 em todo dia de campanha',
    'R1, R2 e R5 com a oferta na legenda e na tela', 'Bio e destaque AGENDAR com a oferta']) + '''</div>
<div class="card"><span class="k">O que medir</span>''' + ck([
    'Agendamentos de seg a qua no app, antes x depois', 'Quantos usaram o 50%',
    'Cliques no link da bio', 'Quanto desses clientes voltou em 20 dias']) + f'''</div></div>
<div class="thumbs" style="margin-top:18px">{img("feed-01-campanha", 128)}{img("story-01-campanha", 90)}{img("story-02-horarios-hoje", 90)}
<p class="note" style="max-width:460px;margin-left:12px">Em 27/11 (Black Friday) a gente não cria desconto novo: a mensagem é “a Black da ED é toda semana, de segunda a quarta”. Em 30/11 a campanha passa o bastão pra agenda de dezembro.</p></div>''')

# 5 cronograma ---------------------------------------------------------
tl = [('04/11 · QUA', 'Visita 1 · Diária de Reels', 'Pauta aprovada com o Ed + grava R1 e R2 + stories', True),
      ('09/11 · SEG', 'Perfil novo no ar', 'Bio, 8 destaques e A1 fixada', False),
      ('11/11 · QUA', 'Visita 2 · Diária de Reels', 'Grava R3, R4 e R5 + stories', True),
      ('18/11 · QUA', 'Visita 3 · Diária de fotos', 'Ensaio: cortes, ambiente, equipe e o Ed (fotos de A1 e A4)', True),
      ('25/11 · QUA', 'Visita 4 · Diária de Reels', 'Grava R6 e R7 + stories', False),
      ('30/11 · SEG', 'Relatório', 'Alcance, seguidores, agendamentos e pauta de dezembro', False)]
S('Cronograma de produção', '<h1>Quando a House <span class="am">vai na ED.</span></h1>'
  '<p class="sub">Uma visita por semana, sempre na quarta. Em toda visita a gente grava stories de bastidor, além do que está na pauta.</p>'
  '<div class="tl">' + ''.join(f'<div class="{"new" if n else ""}"><div class="dt">{a}</div><h4>{b}</h4><p>{c}</p></div>' for a, b, c, n in tl) + '</div>'
  '''<div class="card" style="margin-top:40px;display:grid;grid-template-columns:200px 1fr;gap:20px"><span class="k" style="margin:4px 0 0">Antes de cada visita</span>
<p style="color:#ddd;font-size:14px">Agendar no app os clientes de cada Reels (lista em “Próximos passos”) e avisar que vão aparecer no Instagram. Pedir autorização de imagem, principalmente de crianças. Gravar todos os “antes” antes do primeiro corte.</p></div>''')

# 6 calendário ---------------------------------------------------------
V = lambda n: f'<span class="tag b">Visita {n}</span>'
C = '<span class="tag y">Seg a Qua 50%</span>'
cal = {1: '', 2: None, 3: None, 4: V(1), 5: '', 6: '', 7: '', 8: '',
       9: '<div class="p"><i>A1</i> Campanha Seg a Qua: 50% no 1º corte</div>' + C,
       10: '<div class="p">R1 Degradê sem marca</div>' + C, 11: V(2) + C,
       12: '<div class="p"><i>A2</i> Agendar na ED leva 3 toques + tabela</div>', 13: '',
       14: '<div class="p">R2 Chegou pedindo socorro</div>', 15: '', 16: C,
       17: '<div class="p">R3 O Ed responde: qual corte pro teu rosto</div>' + C, 18: V(3) + C,
       19: '<div class="p">R4 Movimentos da navalha, parte 2</div>', 20: '<span class="tag r">Feriado</span>',
       21: '<div class="p"><i>A3</i> Quem senta na cadeira da ED, volta (o Ed)</div>', 22: '', 23: C,
       24: '<div class="p">R5 Agendou pelo app, sentou na hora</div>' + C, 25: V(4) + C,
       26: '<div class="p"><i>A4</i> Qual corte é o seu?</div>', 27: '<span class="tag r">Black Friday</span>',
       28: '<div class="p">R6 Barba completa: o ritual</div>', 29: '',
       30: '<div class="p">R7 Pai e filho na mesma cadeira</div>' + C}
cells = ''.join(f'<div class="h">{d}</div>' for d in ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM'])
cells += '<div></div>' * 6
for d in range(1, 31):
    v = cal[d]
    cells += f'<div class="d{" o" if v is None or d == 1 else ""}"><b class="n">{d}</b>{v or ""}</div>'
S('Calendário · Novembro 2026', '<h1 class="sm" style="display:flex;justify-content:space-between;align-items:flex-end">'
  '<span>Feed do mês: <span class="am">11 posts.</span></span><span class="note" style="font-size:12px;font-weight:400;text-align:right;letter-spacing:0">'
  'Branco: Reels · Amarelo: arte/carrossel · Postar às 18h30<br>Stories todos os dias (próximas páginas)</span></h1>'
  f'<div class="cal" style="margin-top:6px">{cells}</div>')

# 7 ordem --------------------------------------------------------------
ordem = [('09/11', 'seg', 'A1', 'Arte', 'Campanha Seg a Qua: 50% no 1º corte', 1),
         ('10/11', 'ter', 'R1', 'Reels', 'Degradê sem marca', 0),
         ('12/11', 'qui', 'A2', 'Carrossel', 'Agendar na ED leva 3 toques + tabela', 1),
         ('14/11', 'sáb', 'R2', 'Reels', 'Chegou pedindo socorro', 0),
         ('17/11', 'ter', 'R3', 'Reels', 'O Ed responde: qual corte pro teu rosto', 0),
         ('19/11', 'qui', 'R4', 'Reels', 'Movimentos da navalha, parte 2', 0),
         ('21/11', 'sáb', 'A3', 'Carrossel', 'Quem senta na cadeira da ED, volta (o Ed)', 1),
         ('24/11', 'ter', 'R5', 'Reels', 'Agendou pelo app, sentou na hora', 0),
         ('26/11', 'qui', 'A4', 'Carrossel', 'Qual corte é o seu?', 0),
         ('28/11', 'sáb', 'R6', 'Reels', 'Barba completa: o ritual', 0),
         ('30/11', 'seg', 'R7', 'Reels', 'Pai e filho na mesma cadeira', 0)]
S('Feed · ordem de postagem', '<h1 class="sm">7 Reels e 4 artes, <span class="am">três por semana.</span></h1>'
  '<p class="sub" style="margin-bottom:10px">Terça, quinta e sábado às 18h30, com segunda nos dias de estreia. Os 3 fixados ficam: campanha, como agendar e o Ed.</p>'
  '<table class="ord">' + ''.join(
      f'<tr><td class="d">{a}</td><td style="color:#888">{b}</td><td><span class="badge {"y" if c[0] == "A" else ""}">{c}</span></td>'
      f'<td style="color:#888">{d}</td><td><b>{e}</b></td><td class="fix">{"FIXAR" if f else ""}</td></tr>' for a, b, c, d, e, f in ordem) + '</table>')

# 8 stories regras -----------------------------------------------------
S('Stories · regras da equipe', '<h1>Stories todo dia, <span class="am">feitos pela equipe da ED.</span></h1>'
  '<p class="sub">As próximas páginas têm o que postar em cada dia. Leva 5 minutos e quem estiver livre entre um cliente e outro pode fazer.</p>'
  '<div class="grid c2" style="gap:0 60px">' + ck([
      'Sempre vertical e na luz da janela ou do espelho', 'Todo story de oferta com o adesivo de link do agendamento',
      'Pedir autorização antes de filmar o cliente (e dos pais, no kids)', 'Usar as artes story-01 a story-04 que estão na pasta de artes']) + ck([
      'Nada de marca d’água de app de edição', 'Marcar @edbarbearia e o barbeiro do corte',
      '3 a 5 stories por dia: melhor pouco e todo dia do que muito num dia só', 'Repostar todo cliente que marcar a ED']) + '</div>'
  f'<div class="thumbs" style="margin-top:22px">{img("story-01-campanha", 100)}{img("story-02-horarios-hoje", 100)}{img("story-03-antes-depois", 100)}{img("story-04-caixinha", 100)}'
  '<p class="note" style="max-width:360px;margin-left:12px">Os modelos de story já têm o espaço marcado para o adesivo de link, a caixinha ou as fotos. É só abrir no Instagram e completar.</p></div>')

# 9-12 stories por semana ----------------------------------------------
TAGS = {'V1': '<span class="tag b">Visita 1</span>', 'V2': '<span class="tag b">Visita 2</span>',
        'V3': '<span class="tag b">Visita 3</span>', 'V4': '<span class="tag b">Visita 4</span>',
        'C': '<span class="tag y">Campanha</span>', 'F': '<span class="tag g">Fechado</span>',
        'H': '<span class="tag r">Feriado</span>', 'BF': '<span class="tag r">Black Friday</span>'}


def semana(titulo, rows):
    tr = ''.join(f'<tr><td class="d">{d}<small>{w}</small></td><td class="t">{t}<br>{"".join(TAGS[x] for x in tg)}</td>'
                 f'<td class="w">{o}</td><td class="a">{a}</td></tr>' for d, w, t, tg, o, a in rows)
    S(f'Stories · {titulo}', f'<h1 class="sm">Stories do dia <span class="am">{titulo.replace(" A ", " a ")}</span></h1>'
      f'<table><thead><tr><th>Dia</th><th>Tema</th><th>O que gravar</th><th>Adesivo / chamada</th></tr></thead><tbody>{tr}</tbody></table>')


semana('04/11 a 10/11', [
    ('04/11', 'qua', 'Dia de gravação', ['V1'], '1. Bastidor da House gravando (luz, celular, cadeira) · 2. Cliente do Reels antes de começar · 3. “Tem novidade chegando no perfil dia 9”', 'Enquete: degradê ou social? + link de agendar'),
    ('05/11', 'qui', 'Bastidor técnico', [], '1. Close de 10 s da máquina ou navalha trabalhando · 2. Mão do barbeiro fazendo o contorno · 3. Resultado final no espelho', 'Arte story-04 com caixinha: qual corte você quer?'),
    ('06/11', 'sex', 'Bom dia da ED', [], '1. Abrindo a porta e a primeira cadeira do dia · 2. Primeiro cliente sentando (pedir autorização) · 3. Resultado do primeiro corte, de perfil', 'Arte story-03 (antes/depois) do cliente do dia'),
    ('07/11', 'sáb', 'Casa cheia', [], '1. Timelapse de 15 s do movimento · 2. 3 resultados do dia em sequência · 3. Barbeiro mostrando a agenda de segunda', 'Link de agendar: “segunda já tem horário”'),
    ('08/11', 'dom', 'Repost de clientes', ['F'], '1. Repostar stories em que clientes marcaram a @edbarbearia · 2. Story de texto: “Amanhã começa a semana do 50%”', 'Lembrete de evento: 09/11'),
    ('09/11', 'seg', 'Estreia da campanha e do perfil novo', ['C'], '1. Arte story-01 (Seg a Qua · 50%) · 2. Tela do perfil novo mostrando os destaques · 3. Arte story-02 com os horários livres de hoje', 'Link de agendar em todos'),
    ('10/11', 'ter', 'Horários livres + R1', ['C'], '1. Arte story-02 com horários de hoje · 2. Compartilhar o Reels R1 · 3. Cliente em 10 s: “como ficou?”', 'Link de agendar')])
semana('11/11 a 17/11', [
    ('11/11', 'qua', 'Último dia da semana do 50%', ['C', 'V2'], '1. Story de texto: “só até hoje nesta semana” · 2. Bastidor da gravação · 3. Cliente que veio pelo 50% em 10 s: “como ficou?”', 'Contagem regressiva até 19h + link'),
    ('12/11', 'qui', 'Como agendar (A2)', [], '1. Repostar o carrossel A2 · 2. Gravar a tela do celular agendando de verdade no app (20 s) · 3. “Pronto, marcado”', 'Link de agendar'),
    ('13/11', 'sex', 'Antes e depois do dia', [], '1. Antes de um cliente do dia · 2. Depois, de perfil · 3. “Sábado ainda tem horário”', 'Arte story-03 + link'),
    ('14/11', 'sáb', 'Casa cheia + R2', [], '1. Compartilhar o Reels R2 · 2. Timelapse do sábado · 3. Enquete: barba cheia ou só o contorno?', 'Link de agendar'),
    ('15/11', 'dom', 'Pergunte ao Ed', ['F'], '1. Story de texto: “Manda tua dúvida pro Ed”', 'Caixinha de perguntas (respostas na segunda)'),
    ('16/11', 'seg', 'O Ed responde', ['C'], '1. Ed respondendo 3 perguntas da caixinha em vídeo selfie (até 30 s cada) · 2. Arte story-01', 'Link de agendar'),
    ('17/11', 'ter', 'Horários livres + R3', ['C'], '1. Arte story-02 com horários · 2. Compartilhar o Reels R3 · 3. Resultado do dia', 'Link de agendar')])
semana('18/11 a 24/11', [
    ('18/11', 'qua', 'Dia do ensaio', ['C', 'V3'], '1. Bastidor das fotos · 2. Cada barbeiro se apresenta: nome e corte favorito (1 story cada) · 3. “Último dia do 50% nesta semana”', 'Enquete: qual barbeiro você já conhece? + contagem regressiva'),
    ('19/11', 'qui', 'Espaço kids + R4', [], '1. Criança na cadeira (só com autorização dos pais) · 2. Resultado com o pai ou a mãe · 3. Compartilhar o Reels R4', 'Link de agendar'),
    ('20/11', 'sex', 'Consciência Negra', ['H'], '1. Se abrir: “aberto no feriado” + horários livres · 2. Se fechar: aviso e link para agendar sábado', 'Confirmar com o Ed até 18/11'),
    ('21/11', 'sáb', 'Um dia com o Ed (A3)', [], '1. Repostar o carrossel A3 · 2. Ed chegando e preparando a bancada · 3. Ed revisando um acabamento', 'Link de agendar'),
    ('22/11', 'dom', 'Repost + teaser', ['F'], '1. Repostar clientes que marcaram a ED · 2. “Amanhã volta o 50% no 1º corte”', 'Lembrete de evento: 23/11'),
    ('23/11', 'seg', 'Abertura da semana', ['C'], '1. Arte story-01 · 2. Arte story-02 com horários · 3. Bastidor da manhã', 'Link de agendar'),
    ('24/11', 'ter', 'Prova real + R5', ['C'], '1. Compartilhar o Reels R5 · 2. Depoimento de quem usou o 50% (10 a 15 s) · 3. Resultado do dia', 'Link de agendar')])
semana('25/11 a 30/11', [
    ('25/11', 'qua', 'Última quarta do 50% no mês', ['C', 'V4'], '1. Bastidor da gravação · 2. “Última quarta do mês com 50%” · 3. Antes e depois do dia', 'Contagem regressiva + link'),
    ('26/11', 'qui', 'Qual corte é o seu (A4)', [], '1. Repostar o carrossel A4 · 2. Enquete com os 3 cortes · 3. Caixinha: manda o print do corte que você quer', 'Arte story-04 + link'),
    ('27/11', 'sex', 'A nossa Black é toda semana', ['BF'], '1. Story de texto: “A Black da ED é de segunda a quarta: 50% no 1º corte” · 2. Horários livres de sábado · 3. Resultado do dia', 'Link de agendar'),
    ('28/11', 'sáb', 'Casa cheia + R6', [], '1. Compartilhar o Reels R6 · 2. Timelapse do sábado · 3. “Dezembro lota: já dá pra marcar”', 'Link de agendar'),
    ('29/11', 'dom', 'Retrospectiva do mês', ['F'], '1. Os 3 melhores cortes de novembro · 2. Agradecimento aos clientes', 'Caixinha: o que você quer ver em dezembro?'),
    ('30/11', 'seg', 'Agenda de dezembro aberta', ['C'], '1. Compartilhar o Reels R7 · 2. Arte story-01 · 3. “A agenda de dezembro já está aberta no app”', 'Link de agendar')])

# 13 regra dos reels ---------------------------------------------------
S('Roteiros de Reels · como gravar', '<h1>Roteiros: <span class="am">gancho nos 3 primeiros segundos.</span></h1>'
  '<p class="sub">Regra dos Reels da ED: abrir com fala ou ação, mostrar a técnica, terminar no resultado e chamar pro app.</p>'
  '<div class="grid c3">'
  '<div class="card"><span class="k">No set</span>' + ck([
      'Gravar os 3 ganchos (A, B e C). A gente escolhe na edição.', 'Gravar o “antes” antes do primeiro corte: não tem segunda chance',
      'Marcar com fita o lugar da cadeira e do tripé (antes e depois iguais)', 'Logo da parede no fundo em pelo menos 1 plano']) + '</div>'
  '<div class="card"><span class="k">Celular</span>' + ck([
      '4K 30 fps. Câmera lenta da navalha: 1080p 60 fps', 'Lente 1x, nunca 0,5 (deforma o rosto)',
      'Travar foco e luz segurando o dedo na tela', 'Lente limpa e modo avião']) + '</div>'
  '<div class="card"><span class="k">Edição e post</span>' + ck([
      'Texto na tela o vídeo inteiro (muita gente vê sem som)', 'Quando o Ed fala, a voz dele vem na frente da música',
      'Legenda pede um comentário antes do “agende”', 'Convidar o cliente como colaborador nos antes e depois',
      'Testar a abertura B como Reels de teste quando der']) + '</div></div>')


# 14-20 roteiros -------------------------------------------------------
def reel(cod, titulo, grava, posta, dur, tipo, mudou, gs, cenas, audio, capa, leg, extra=None):
    g = ''.join(f'<div class="gh{" best" if i == 0 else ""}"><b class="l">{"ABC"[i]}{" · RECOMENDADO" if i == 0 else ""}</b>{t}</div>' for i, t in enumerate(gs))
    sc = ''.join(f'<span class="t">{t}</span><span>{d}</span>' for t, d in cenas)
    ex = f'<span class="k" style="margin-top:12px">Não esquecer</span>{ck(extra)}' if extra else ''
    S(f'Roteiro de Reels · {cod}', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:18px">
<div>
<div style="font-size:40px;font-weight:700;color:{Y};line-height:1">{cod}</div>
<h1 class="sm" style="margin:8px 0 4px;font-size:30px">{titulo}</h1>
<div class="r-meta">{tipo} · {dur}</div>
<div><span class="tag y">grava {grava}</span><span class="tag">posta {posta}</span></div>
<p class="note" style="margin:12px 0 14px">{mudou}</p>
<span class="k">Gancho (0 a 3 s) · gravar as 3 aberturas</span>{g}
</div>
<div>
<span class="k">Cenas</span><div class="sc">{sc}</div>
<span class="k" style="margin-top:14px">Áudio e capa</span><p style="font-size:13px">{audio}<br><b>Capa:</b> {capa}</p>
<span class="k" style="margin-top:14px">Legenda</span><div class="leg">{leg}</div>{ex}
</div></div>''')


reel('R1', 'Degradê sem marca', '04/11 (qua)', '10/11 (ter)', '25 a 30 s', 'Técnica (o que mais roda no perfil)',
     'Antes: “Do zero ao degradê em 30 segundos”. Dizia o formato, mas não dava motivo pra ficar. A abertura nova começa no resultado e volta pro início.',
     ['Abre no resultado: close da nuca pronta, Ed passando a escova. Texto: <b>“Nenhuma linha marcada. Volta comigo do zero.”</b> Corte seco pro antes.',
      'Ed pra câmera, máquina ligada na mão: <b>“Degradê que marca linha é degradê mal feito. Olha.”</b>',
      'Máquina encostando na nuca, som alto. Texto: <b>“40 minutos de cadeira em 30 segundos.”</b> (trocar pelo tempo real)'],
     [('0–2 s', 'Gancho'), ('2–4 s', 'Cliente de perfil, antes. Texto: ANTES'),
      ('4–12 s', 'Máquina abrindo o degradê: 4 cortes de 2 s (lateral, pente, esfumado, nuca). Tripé na altura da orelha'),
      ('12–16 s', 'Dica do Ed em 1 frase, com a voz dele: o que ele faz pra não marcar linha'),
      ('16–20 s', 'Tesoura no topo'), ('20–24 s', 'Contorno na navalha, bem de perto'),
      ('24–30 s', 'Giro da cadeira até o espelho, cliente passa a mão. Último quadro igual ao primeiro. Texto: <b>Seg a qua: 50% no 1º corte pelo app</b>')],
     'Som real da máquina alto, música em alta bem baixa. Na dica, a voz do Ed na frente.', 'nuca pronta + “DEGRADÊ SEM MARCA”.',
     'Degradê sem marca, do zero ao acabamento. ✂️\nNa lateral tu vai de pente 0 ou 1? Comenta que o Ed responde.\n\nPrimeiro corte na ED? De segunda a quarta sai com 50% agendando pelo app. Link na bio.\n📍 Rua Paula Batista, 604 · Casa Amarela')

reel('R2', 'Chegou pedindo socorro', '04/11 (qua)', '14/11 (sáb)', '25 a 35 s', 'Antes e depois',
     'Antes: “Ele chegou assim...”. Todo antes e depois começa assim. Agora quem abre é o cliente, falando de verdade.',
     ['Cliente na cadeira, fala pra câmera (sem decorar): <b>“Faz [X] meses que eu não corto.”</b> Ed, de fundo: <b>“Deixa comigo.”</b>',
      'Texto sobre o antes: <b>“Ele pediu: faz o que tu achar melhor.”</b> Só se ele disse isso mesmo.',
      'Antes e depois lado a lado por 1 s. Texto: <b>“Mesmo cara. Mesmo dia.”</b> Volta pro antes.'],
     [('0–3 s', 'Gancho'), ('3–7 s', 'Antes em 3 ângulos: frente, perfil, nuca. Cadeira e tripé na marca'),
      ('7–10 s', 'Ed diz o plano em 1 frase (“baixar a lateral, tirar volume e desenhar a barba”)'),
      ('10–20 s', 'Corte acelerado: timelapse de 3 s + 4 cortes de 1,5 s (máquina, tesoura, barba, navalha)'),
      ('20–21 s', 'Transição: Ed sacode a capa na frente da lente'),
      ('21–28 s', 'Depois nos mesmos 3 ângulos, mesma luz'),
      ('28–32 s', 'Reação no espelho de mão, sem ensaiar. Texto: <b>Teu amigo precisa? 1º corte com 50%, seg a qua</b>')],
     'Música em alta + voz do cliente no gancho e na reação.', 'antes e depois em tela dividida + “CHEGOU PEDINDO SOCORRO”.',
     'Chegou pedindo socorro, saiu pronto pra foto.\nMarca aquele amigo que tá precisando 👇 O primeiro corte dele na ED sai com 50% de segunda a quarta, agendando pelo app. Link na bio.',
     ['Anotar o @ do cliente e convidar como colaborador no post', 'Plano B: se o cliente não vier com cabelo e barba grandes, grava o R3 e o R2 vai pra 11/11'])

reel('R3', 'O Ed responde: qual corte pro teu rosto', '11/11 (qua)', '17/11 (ter)', '30 a 45 s', 'O Ed como rosto da marca',
     'O gancho já era bom. Agora fecha pedindo comentário e direct, e as perguntas viram pauta do “Pergunte ao Ed”.',
     ['Ed pra câmera, apontando: <b>“Rosto redondo? Para de pedir esse corte.”</b> Foto do corte aparece na tela.',
      'Ed: <b>“Teu corte pode estar errado pro teu rosto. Em 30 segundos tu descobre.”</b>',
      'Ed segurando 3 fotos: <b>“Qual desses é tu?”</b>'],
     [('0–3 s', 'Gancho'),
      ('3–30 s', 'Para cada formato (redondo, quadrado, alongado): nome grande na tela, cliente real ou foto ao lado, e o Ed diz o que fazer e o que evitar, com as palavras dele'),
      ('30–35 s', 'Ed: <b>“Não sabe o teu? Comenta ROSTO que eu te digo.”</b>')],
     'Voz do Ed com microfone de lapela, música bem baixa ou nenhuma. Legenda na tela o tempo todo.', 'Ed apontando + “QUAL CORTE PRO TEU ROSTO?”.',
     'Qual é o formato do teu rosto? Comenta ROSTO e manda uma selfie de frente no direct que o Ed diz o corte. ✂️\nAgende pelo link da bio.',
     ['Só precisa do Ed: dá pra gravar entre um cliente e outro'])

reel('R4', 'Movimentos da navalha, parte 2', '11/11 (qua)', '19/11 (qui)', '20 a 35 s', 'Continuação do Reels de 16,6 mil views',
     'Antes: “Parte 2, porque vocês pediram”. Só funciona pra quem viu a parte 1. Esse conteúdo atrai muito barbeiro: serve pra alcance e pro curso.',
     ['Navalha abrindo, bem de perto. Texto: <b>“O vídeo da navalha passou de 16 mil views. Faltaram esses 3.”</b>',
      'Ed: <b>“O movimento que mais me pedem pra ensinar é esse aqui.”</b>',
      'Texto: <b>“3 movimentos de navalha que separam contorno bom de contorno perfeito.”</b>'],
     [('0–3 s', 'Gancho'), ('3–5 s', 'Navalha sendo montada, lâmina nova'),
      ('5–25 s', '3 movimentos bem de perto, em câmera lenta. Nome de cada um na tela, Ed narrando'),
      ('25–30 s', 'Resultado do contorno'), ('30–33 s', 'Ed: <b>“Quer aprender de verdade? Destaque CURSO.”</b>')],
     'Voz do Ed + som real da navalha, música bem baixa.', 'navalha de perto + “NAVALHA · PARTE 2”.',
     'Movimentos da navalha, parte 2. A parte 1 tá no perfil.\nSalva pra treinar depois. Quer aprender com o Ed? Destaque CURSO no perfil.')

reel('R5', 'Agendou pelo app, sentou na hora', '11/11 (qua)', '24/11 (ter)', '20 a 30 s', 'Conversão (app + campanha)',
     'Grava numa quarta de campanha, com um cliente que agendou pelo 50% de verdade. O POV vira prova.',
     ['Tela do app com cronômetro na tela. Texto: <b>“Agendei em 10 segundos. Sentei na hora marcada.”</b>',
      'Texto: <b>“POV: tu chegou na barbearia e não tinha ninguém na tua frente.”</b>',
      'Cliente na porta: <b>“Tem horário?”</b> Ed: <b>“Tem no app.”</b>'],
     [('0–3 s', 'Gancho'), ('3–10 s', 'Tela gravada: link da bio → serviço → horário → confirmar. Cronômetro na tela. Esconder dados pessoais'),
      ('10–14 s', 'Cliente entra pela porta, celular mostrando a hora, e senta direto'),
      ('14–24 s', 'Corte rápido: 4 cortes de 2 s'), ('24–28 s', 'Resultado. Texto: <b>Seg a qua: 50% no 1º corte pelo app</b>')],
     'Música em alta. Som de notificação no “confirmar”.', 'celular com o app + “SEM FILA”.',
     'Sem fila e sem esperar resposta no WhatsApp: 3 toques no app e a cadeira é tua.\nDe segunda a quarta, o primeiro corte sai com 50%. Link na bio.')

reel('R6', 'Barba completa: o ritual', '25/11 (qua)', '28/11 (sáb)', '20 a 30 s', 'Técnica e experiência',
     'Antes não tinha texto nem fala no gancho, só a imagem. Agora tem frase, e o som entra como atração.',
     ['Toalha quente saindo do rosto com vapor, bem de perto. Texto: <b>“Isso aqui não é só fazer a barba.”</b>',
      'Som da navalha, sem música. Texto: <b>“Liga o som.”</b>',
      'Ed: <b>“Barba de 5 minutos na máquina, ou isso aqui?”</b>'],
     [('0–3 s', 'Gancho'), ('3–8 s', 'Toalha quente, luz de lado pro vapor aparecer'), ('8–12 s', 'Espuma ou óleo'),
      ('12–20 s', 'Navalha desenhando a linha, bem de perto'), ('20–25 s', 'Acabamento e finalização'),
      ('25–28 s', 'Cliente passa a mão na barba. Texto: <b>Cabelo + barba R$ 80</b>')],
     'Som real (toalha, espuma, navalha) na frente, música bem baixa.', 'toalha com vapor + “O RITUAL DA BARBA”.',
     'O ritual da barba na ED: toalha quente, navalha e acabamento sem pressa.\nBarba R$ 40. Cabelo + barba R$ 80 (tu economiza R$ 10). Agende pelo link da bio.')

reel('R7', 'Pai e filho na mesma cadeira', '25/11 (qua)', '30/11 (seg)', '25 a 35 s', 'Espaço kids e família (com autorização)',
     'O gancho já era bom. Agora pede voto nos comentários e fecha com a agenda de dezembro.',
     ['Pai e filho lado a lado, cortes prontos. Texto: <b>“Quem ficou melhor? Vota: 1 ou 2.”</b>',
      'Filho: <b>“Pai, agora a gente tá igual.”</b> Só se sair natural.',
      'Texto: <b>“O programa deles de pai e filho é aqui.”</b>'],
     [('0–3 s', 'Gancho'), ('3–6 s', 'Os dois chegando juntos'), ('6–15 s', 'Filho no espaço kids'),
      ('15–24 s', 'Pai na cadeira'), ('24–30 s', 'Os dois no espelho. Texto: <b>A agenda de dezembro já tá aberta</b>')],
     'Música em alta, leve.', 'os dois no espelho + “PAI E FILHO”.',
     'Pai e filho, mesma cadeira. Quem ficou melhor: 1 ou 2? 👇\nDezembro lota rápido e a agenda já tá aberta no app. Link na bio.',
     ['Agendar pai e filho até 18/11', 'Autorização dos pais por escrito', 'Convidar o pai como colaborador no post'])


# 21-24 artes ----------------------------------------------------------
def arte(cod, data, titulo, imgs, leg, nota=''):
    th = ''.join(img(i, 270) for i in imgs)
    S(f'Feed · {cod} · {data}', f'<h1 class="sm">{cod} · <span class="am">{titulo}</span></h1>'
      f'<div class="thumbs" style="margin:14px 0 20px">{th}</div>'
      f'<div class="card"><span class="k">Legenda</span><p style="color:#f4f2ec;font-size:14.5px">{leg}</p>'
      f'<p class="note" style="margin-top:6px">1080 × 1350 px · arquivos na pasta artes. <b class="am">{nota}</b></p></div>')


arte('A1', '09/11', 'Campanha Seg a Qua', ['feed-01-campanha'],
     'Segunda a quarta a ED tem 50% no seu primeiro corte. É só agendar pelo app, escolher o horário e sentar na cadeira. Link na bio. 📍 Rua Paula Batista, 604, Casa Amarela.',
     'As fotos dos cortes são provisórias: trocar pelas do ensaio de 18/11.')
arte('A2', '12/11', 'Agendar em 3 toques', ['feed-02a-agendar-capa', 'feed-02b-agendar-passos', 'feed-02c-agendar-precos'],
     'Agendar na ED leva 3 toques: link da bio, serviço e hora, confirmar. Arrasta pra ver a tabela. Cabelo R$ 50, barba R$ 40, cabelo + barba R$ 80.')
arte('A3', '21/11', 'Quem é o Ed', ['feed-03a-ed-capa', 'feed-03b-ed-frase', 'feed-03c-ed-agendar'],
     'Quem senta na cadeira da ED, volta. O Ed está na casa de segunda a sábado e revisa cada acabamento antes de você levantar. Sua vez: link na bio.')
arte('A4', '26/11', 'Qual corte é o seu', ['feed-04a-cortes-capa', 'feed-04b-corte-textured', 'feed-04c-corte-barba', 'feed-04d-corte-crop'],
     'Qual corte é o seu? Textured crop, degradê com barba ou crop com fade. Comenta o número e manda o print do seu corte no direct. Agende pelo link da bio.',
     'As fotos dos cortes são provisórias: trocar pelas do ensaio de 18/11.')

# 25 perfil ------------------------------------------------------------
dest = [('agendar', 'AGENDAR'), ('cortes', 'CORTES'), ('precos', 'PREÇOS'), ('kids', 'KIDS'),
        ('salao', 'SALÃO'), ('acao-social', 'AÇÃO SOCIAL'), ('curso', 'CURSO'), ('onde', 'ONDE')]
dh = ''.join(f'<div style="text-align:center"><img src="img/destaque-{a}.jpg" style="width:84px;border-radius:50%"><div class="note" style="font-size:11px;margin-top:6px">{b}</div></div>' for a, b in dest)
S('Perfil · bio e destaques', '<h1>Perfil novo <span class="am">no ar em 09/11.</span></h1>'
  '<div class="grid c2"><div class="card"><span class="k">Bio nova (até 150 caracteres)</span>'
  '<p style="color:#f4f2ec;font-size:17px;line-height:1.7">ED BARBEARIA | Casa Amarela, Recife<br>✂️ Degradê, barba, kids e salão<br>🗓️ Seg a sáb, 9h às 19h<br>🎟️ 50% no 1º corte: seg a qua, pelo app<br>👇 Agende em 1 toque</p>'
  '<p class="note" style="margin-top:10px">Link da bio: landing page da ED (agendar, WhatsApp e mapa num lugar só).</p></div>'
  f'<div class="card"><span class="k">8 destaques, sem repetir</span><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px 6px">{dh}</div>'
  '<p class="note" style="margin-top:12px">Sai o destaque duplicado “Curso / CURSO”. O conteúdo de aluno vai só pro destaque CURSO, e o feed fala com o cliente.</p></div></div>'
  '<div class="card" style="margin-top:14px"><span class="k" style="display:inline;margin-right:14px">Fixados</span>A1 (campanha), A2 (como agendar) e A3 (o Ed). O post “Estamos contratando” sai dos fixados e vai pro destaque.</div>')

# 26 relatório ---------------------------------------------------------
rel = [('Alcance do mês', 'Contas alcançadas e de onde vieram'), ('Seguidores', 'Ganhos no mês, partindo de 3.199'),
       ('Reels', 'Views de R1 a R7, comparando com a média de 600 a 2,6 mil, e qual abertura funcionou melhor'),
       ('Link da bio', 'Cliques no link e no WhatsApp'),
       ('Agendamentos', 'Total do mês no app e só de seg a qua (pedir o número ao Ed)'),
       ('Campanha', 'Quantos clientes usaram os 50% no 1º corte e quantos comentaram as palavras-chave (ROSTO, 1 ou 2)')]
S('Relatório · 30/11', '<h1>O que a gente <span class="am">vai medir.</span></h1>'
  '<p class="sub">No dia 30 sai o relatório. O que funcionou vira pauta de dezembro, o mês mais cheio do ano.</p>'
  '<div class="grid c3">' + ''.join(f'<div class="card" style="min-height:120px"><span class="k">{a}</span><p style="color:#f4f2ec;font-size:14.5px">{b}</p></div>' for a, b in rel) + '</div>')

# 27 próximos passos ---------------------------------------------------
pp = [('01', 'Aprovar a pauta', 'Ed aprova este plano hoje, 04/11, antes da primeira gravação.'),
      ('02', 'Confirmar feriado', 'Se a ED abre em 20/11 (Consciência Negra). Até 18/11.'),
      ('03', 'Clientes da gravação', '11/11: 1 de contorno (R4) e 1 cliente novo do 50% (R5). 18/11: modelos dos 3 cortes da A4. 25/11: 1 de barba cheia (R6) e pai e filho (R7).'),
      ('04', 'Equipe e campanha', 'Definir quem posta os stories de cada dia e como o app mostra que é o 1º corte.')]
S('Próximos passos', '<h1>Aprovou, a gente grava.</h1><div class="grid c4" style="margin-top:20px">' +
  ''.join(f'<div class="card" style="min-height:200px"><div style="font-size:34px;font-weight:700;color:{Y}">{a}</div><h4 style="margin:10px 0 6px;font-size:16px">{b}</h4><p>{c}</p></div>' for a, b, c in pp) +
  '</div><p style="margin-top:22px;font-size:14px">Todo conteúdo é aprovado antes de ir ao ar. Dúvidas e ajustes: WhatsApp (81) 98355-4583 · @housedocreator</p>', 'y')

# monta ----------------------------------------------------------------
out = ''
for i, (ey, body, cls, hc) in enumerate(slides):
    logo = (HC.replace('logo-hc', 'logo-hc') if hc else '')
    foot = '' if i == 0 else f'<div class="foot"><span>ED BARBEARIA × HOUSE DO CREATOR</span><span>{i + 1:02d}</span></div>'
    out += f'<section class="s {cls}">{logo}<div class="ey">{ey}</div>{body}{foot}</section>'
open('plano.html', 'w').write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>ED Barbearia · Plano de conteúdo · Novembro 2026 (revisado)</title>
<link rel="stylesheet" href="../../fonte/fonts.css"><style>{CSS}</style></head><body>{out}</body></html>''')
print(len(slides), 'slides')
