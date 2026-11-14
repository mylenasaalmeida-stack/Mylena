"""Proposta · Débora Brasil Beauty · padrão House do Creator (7 páginas, preto + amarelo)."""

CSS = '''<style>
@import url('fonts.css');
:root{--ink:#0b0b0b;--card:#1a1a1a;--y:#f5cf47;--w:#fff;--soft:#bdbdbd;--line:#2c2c2c}
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Poppins',sans-serif;font-size:9pt;line-height:1.45;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:var(--ink);color:var(--w)}
.page:last-child{page-break-after:auto}
.page.am{background:var(--y);color:var(--ink)}
.in{position:absolute;left:16mm;right:16mm;top:13mm;bottom:20mm;display:flex;flex-direction:column;align-items:center}
.ft{position:absolute;left:16mm;right:16mm;bottom:9mm;display:flex;justify-content:space-between;font-size:6.2pt}
.ft b{font-weight:700;letter-spacing:.3px}
.logo{height:13mm}
.pill{display:inline-block;background:var(--y);color:var(--ink);font-weight:700;font-size:6.4pt;letter-spacing:.4px;text-transform:uppercase;padding:1.4mm 4.5mm;border-radius:20px;margin-top:3mm}
.am .pill{background:var(--ink);color:var(--y)}
h1,h2{font-weight:700;letter-spacing:-.4px;text-align:center;line-height:1.08}
h2{font-size:21pt;margin-top:3mm;position:relative;display:inline-block}
h1 span,h2 span{color:var(--y)}
.am h2 span{color:var(--ink)}
.ray{position:absolute;width:12mm;height:12mm}
.ray.l{left:-15mm;top:-4mm}.ray.r{right:-15mm;bottom:-6mm}
.lead{font-size:8.6pt;color:var(--soft);text-align:center;max-width:150mm;margin-top:3mm}
.am .lead{color:#2a2a2a}
/* capa */
.cover .in{justify-content:flex-start}
.cover .logo{height:24mm;margin-top:14mm}
.cover h1{font-size:32pt;margin-top:24mm;position:relative}
.cover .lead{font-size:9.4pt;margin-top:6mm;max-width:140mm}
.cover .chips{display:flex;gap:2.5mm;margin-top:8mm;flex-wrap:wrap;justify-content:center}
.cover .chips span{border:1px solid var(--y);color:var(--y);border-radius:20px;padding:1.3mm 4mm;font-size:7.4pt;font-weight:500}
.cover .bot{position:absolute;bottom:0;left:0;right:0;text-align:center;font-size:7pt;color:var(--soft)}
.cover .bot b{display:block;color:var(--y);font-weight:700;margin-top:1mm}
.cover .for{margin-top:auto;margin-bottom:22mm;background:var(--card);border-radius:4mm;padding:4mm 8mm;text-align:center}
.cover .for b{display:block;font-size:10pt}
.cover .for small{font-size:7pt;color:var(--soft)}
/* cenário */
.x{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:7mm;width:100%}
.x div{background:var(--ink);color:var(--w);border-radius:4mm;padding:5mm}
.x b{display:flex;align-items:center;gap:2.5mm;font-size:9.6pt}
.x b i{width:5.5mm;height:5.5mm;border-radius:50%;border:1.6px solid var(--w);display:inline-flex;align-items:center;justify-content:center;font-style:normal;font-size:7pt;flex:none}
.x p{font-size:7.8pt;color:var(--soft);margin-top:2mm}
.res{display:grid;grid-template-columns:24mm 1fr;gap:5mm;align-items:center;background:var(--ink);color:var(--w);border-radius:4mm;padding:6mm 7mm;margin-top:4mm;width:100%}
.res img{width:24mm}
.res b{color:var(--y);font-size:11pt;display:block;line-height:1.25}
.res p{font-size:7.9pt;color:var(--soft);margin-top:2mm}
.nums{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;width:100%;margin-top:6mm}
.nums div{border:1.6px solid var(--ink);border-radius:4mm;padding:3.5mm;text-align:center}
.nums b{display:block;font-size:17pt;line-height:1}
.nums small{font-size:6.8pt}
/* serviços */
.svc{width:100%;margin-top:6mm}
.svc+.svc{border-top:1px solid var(--line);padding-top:6mm}
.sh{display:grid;grid-template-columns:15mm 1fr auto;align-items:baseline}
.sh .n{color:var(--y);font-weight:700;font-size:24pt;line-height:1}
.sh h3{font-size:16pt;font-weight:700;letter-spacing:-.3px}
.sh .v{font-size:7.4pt;color:var(--soft);text-align:right}
.sh .v b{display:block;color:var(--w);font-size:11pt}
.svc .ds{margin-left:15mm;color:var(--soft);font-size:8.6pt;margin-top:1.5mm}
.svc .k{margin-left:15mm;color:var(--y);font-weight:700;font-size:6.4pt;text-transform:uppercase;margin-top:2.5mm}
.rc{margin-left:15mm;display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;margin-top:2.5mm}
.rc div{background:var(--card);border-radius:3mm;padding:3mm 4mm 3mm 9mm;position:relative;font-size:7.8pt;min-height:12mm;display:flex;align-items:center}
.rc div:before{content:'';position:absolute;left:4mm;top:50%;width:2mm;height:2mm;border-radius:50%;background:var(--y);transform:translateY(-50%)}
.dif{margin-left:15mm;background:var(--y);color:var(--ink);border-radius:3.5mm;padding:4mm 6mm;font-size:8pt;margin-top:4mm}
/* pacotes */
.pk{display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm;margin-top:7mm;width:100%;align-items:stretch}
.p{background:var(--ink);color:var(--w);border-radius:4mm;padding:6mm 4.5mm 5mm;display:flex;flex-direction:column;position:relative}
.p.best{outline:2.2px solid var(--ink);outline-offset:2mm}
.p .tg{position:absolute;top:-3.4mm;left:50%;transform:translateX(-50%);background:var(--w);color:var(--ink);font-size:6.2pt;font-weight:700;text-transform:uppercase;padding:1mm 3.5mm;border-radius:20px;white-space:nowrap}
.p .ph{color:var(--y);font-weight:700;font-size:6.6pt;text-transform:uppercase;letter-spacing:.4px}
.p h4{font-size:12.5pt;line-height:1.1;margin-top:1mm}
.p .fr{font-size:7.2pt;color:var(--soft);margin-top:1.5mm;min-height:10mm}
.p .old{font-size:7.2pt;color:var(--soft);text-decoration:line-through;margin-top:2mm}
.p .pr{font-size:22pt;font-weight:700;color:var(--y);line-height:1.05;white-space:nowrap}
.p .sv{font-size:7pt;font-weight:600;margin-top:.5mm}
.p ul{list-style:none;margin-top:3.5mm;font-size:7.6pt}
.p li{padding:1.5mm 0 1.5mm 4.5mm;border-top:1px solid var(--line);position:relative}
.p li:before{content:'';position:absolute;left:0;top:2.9mm;width:1.8mm;height:1.8mm;border-radius:50%;background:var(--y)}
.p li.pl{color:var(--y);font-weight:600}
.note{background:var(--ink);color:var(--w);border-radius:3.5mm;padding:4mm 6mm;font-size:8pt;margin-top:6mm;width:100%}
.am .steps p{color:#2a2a2a}.am .steps i{background:var(--ink);color:var(--y)}
.note b{color:var(--y)}
/* tabela */
table{width:100%;border-collapse:separate;border-spacing:0 1.3mm;font-size:7.8pt;margin-top:4mm}
th{font-size:6.2pt;color:var(--y);text-transform:uppercase;font-weight:700;text-align:left;padding:0 3mm}
td{background:var(--card);padding:2.2mm 3mm}
td:first-child{border-radius:2.5mm 0 0 2.5mm}td:last-child{border-radius:0 2.5mm 2.5mm 0}
.r{text-align:right}.c{text-align:center}
.ok{color:var(--y);font-weight:700}.no{color:#555}
tr.sum td{background:transparent;border-top:1px solid var(--line);font-weight:600}
tr.fin td{background:var(--y);color:var(--ink);font-weight:700;font-size:9pt}
/* como funciona */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;width:100%;margin-top:5mm;text-align:center}
.steps i{display:inline-flex;width:8mm;height:8mm;border-radius:50%;background:var(--y);color:var(--ink);font-style:normal;font-weight:700;align-items:center;justify-content:center;font-size:9pt}
.steps b{display:block;font-size:9pt;margin-top:2mm}
.steps p{font-size:7pt;color:var(--soft)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:4mm;width:100%;margin-top:7mm}
.bx{border-left:2px solid var(--y);background:var(--card);border-radius:0 3mm 3mm 0;padding:4mm 5mm}
.bx b{color:var(--y);font-size:8.6pt}
.bx ul{list-style:none;font-size:7.4pt;color:#ddd;margin-top:1.5mm}
.bx li{margin:1mm 0}
/* próximos passos */
.chk{width:100%;display:flex;flex-direction:column;gap:2.5mm;margin-top:6mm}
.chk div{background:var(--ink);color:var(--w);border-radius:3.5mm;padding:3.5mm 5mm;display:grid;grid-template-columns:9mm 1fr;align-items:center}
.chk i{width:5mm;height:5mm;border:1.6px solid var(--y);border-radius:1.3mm}
.chk b{font-size:9pt;display:block}
.chk small{font-size:7.2pt;color:var(--soft)}
.sig{display:grid;grid-template-columns:1fr 1fr;gap:12mm;width:100%;margin-top:14mm;text-align:center;font-size:7pt}
.sig div{border-top:1.4px solid var(--ink);padding-top:2mm}
.cta{background:var(--ink);color:var(--w);border-radius:20mm;padding:4mm 14mm;text-align:center;margin-top:auto}
.cta small{display:block;color:var(--y);font-size:6pt;font-weight:700;text-transform:uppercase}
.cta b{font-size:14pt;color:var(--y)}
.who{display:flex;gap:30mm;margin-top:5mm;font-size:7.4pt;text-align:center}
.who small{display:block;font-weight:700;font-size:6pt;text-transform:uppercase}
</style>'''

CLIENTE = 'Proposta · Débora Brasil Beauty'
TOTAL = 7
RAY = ('<svg class="ray {s}" viewBox="0 0 40 40"><g stroke="{c}" stroke-width="4.5" stroke-linecap="round">'
       '<line x1="{a}" y1="6" x2="{b}" y2="18"/><line x1="{d}" y1="22" x2="{e}" y2="28"/></g></svg>')


def rays(c='#f5cf47'):
    return (RAY.format(s='l', c=c, a=22, b=30, d=6, e=20) + RAY.format(s='r', c=c, a=10, b=18, d=20, e=34))


def title(txt, dark=False):
    return f'<h2>{rays("#0b0b0b" if dark else "#f5cf47")}{txt}</h2>'


def page(n, body, am=False):
    logo = 'img/house/hc-escuro.png' if am else 'img/house/hc-claro.png'
    return (f'<section class="page{" am" if am else ""}"><div class="in"><img class="logo" src="{logo}">{body}</div>'
            f'<div class="ft"><b>HOUSE DO CREATOR</b><span>{CLIENTE}</span><b>{n:02d}</b></div></section>')


def brl(v): return f'R$ {v:,}'.replace(',', '.')


# 1 · capa
p1 = f'''<section class="page cover"><div class="in">
<img class="logo" src="img/house/hc-claro.png">
<span class="pill" style="margin-top:6mm">Proposta para Débora Brasil Beauty</span>
<h1>{rays()}Teu trabalho já é lindo.<br>Agora o perfil <span>também.</span></h1>
<p class="lead">Landing page, bio, destaques, os 6 primeiros posts e a arte da porta do estúdio, tudo no mesmo padrão, pra quem procura sobrancelha em Piedade e Candeias te achar e agendar.</p>
<div class="chips"><span>Landing page</span><span>Bio + destaques</span><span>6 primeiros posts</span><span>Arte da porta</span></div>
<div class="for"><b>Débora Brasil · @deborabrasilbeauty</b><small>Micropigmentação · Brow lamination · Lash lifting · Maquiagem</small></div>
<div class="bot">Recife · Pernambuco · 14/11/2026<b>@housedocreator · (81) 98355-4583</b></div>
</div></section>'''

# 2 · cenário
p2 = page(2, f'''<span class="pill">O que a gente viu</span>
{title('O resultado é bonito.<br>O perfil não <span>mostra.</span>', True)}
<p class="lead">Teus antes e depois mostram técnica e capricho. O problema é como o perfil apresenta isso pra quem chega pela primeira vez e decide em segundos.</p>
<div class="nums"><div><b>491</b><small>posts no feed</small></div><div><b>2.582</b><small>seguidoras</small></div>
<div><b>5</b><small>destaques sem padrão</small></div><div><b>0</b><small>página com serviços</small></div></div>
<div class="x">
<div><b><i>✕</i>Feed sem identidade</b><p>Resultado, recado, Natal, show e café se misturam. A logo DB quase não aparece.</p></div>
<div><b><i>✕</i>Bio cortada</b><p>Os serviços somem no "mais" e o endereço ocupa três linhas.</p></div>
<div><b><i>✕</i>Destaques bagunçados</b><p>Cada capa de um jeito e nomes cortados: "Novo ender…", "Brow la…".</p></div>
<div><b><i>✕</i>Porta que não fala</b><p>Quem passa na galeria não sabe que ali tem um estúdio de beleza do olhar.</p></div>
</div>
<div class="res"><img src="img/house/hc-claro.png"><div><b>A House do Creator organiza<br>tua vitrine de ponta a ponta.</b>
<p>Do primeiro post à porta do estúdio, tudo com a cara da marca DB: quem chega pelo Instagram, pelo link ou pela galeria entende o que tu faz e já sabe como agendar.</p></div></div>''', am=True)

ITENS = {
    'lp': ('01', 'Landing page', 400, 'Um link só, bonito e rápido, que apresenta teus serviços e transforma visita em agendamento.',
           ['Página com serviços, fotos de resultados e diferenciais', 'Endereço com mapa e horário de atendimento',
            'Botão direto pro teu WhatsApp', 'Feita pra abrir perfeita no celular'],
           'Diferencial: vira o link da tua bio. A cliente chega no WhatsApp já sabendo o que quer.'),
    'bio': ('02', 'Bio + destaques', 150, 'A primeira coisa que a cliente lê. Bio curta e clara, e destaques que organizam teu trabalho.',
            ['Bio reescrita: o que tu faz, onde fica e como agendar', 'Capas dos destaques no tom da marca DB',
             'Destaques organizados: Micro fio a fio, Brow, Lash, Maquiagem', 'Destaques "Onde estamos" e "Agende"'],
            'Diferencial: tudo legível no celular, sem nome cortado e sem "mais" escondendo teus serviços.'),
    'posts': ('03', 'Os 6 primeiros posts', 300, 'O topo do feed é o teu cartão de visita. Seis posts que apresentam tu, teus serviços e teus resultados.',
              ['6 artes no mesmo padrão visual', 'Legendas prontas, com chamada pra agendar',
               'Quem é a Débora, serviços, antes e depois, onde fica', '3 posts pra fixar no topo do perfil'],
              'Diferencial: quem entra no perfil entende em segundos quem tu é e por que agendar contigo.'),
    'porta': ('04', 'Arte da porta', 90, 'A porta é vitrine também. Quem passa na Galeria Ponto Certo precisa saber que ali tem estúdio.',
              ['Logo DB, serviços e horário de atendimento', '@ do Instagram e WhatsApp pra agendar',
               'Arte no tamanho real da tua porta', 'Arquivo pronto pra gráfica (adesivo ou vinil)'],
              'Diferencial: a mesma identidade do Instagram na rua. Impressão não inclusa, a gente indica a gráfica.'),
}


def svc(key):
    n, t, v, d, rec, dif = ITENS[key]
    cards = ''.join(f'<div>{r}</div>' for r in rec)
    return (f'<div class="svc"><div class="sh"><span class="n">{n}</span><h3>{t}</h3><span class="v">avulso<b>{brl(v)}</b></span></div>'
            f'<p class="ds">{d}</p><div class="k">O que tu recebe</div><div class="rc">{cards}</div><div class="dif">{dif}</div></div>')


p3 = page(3, f'<span class="pill">O que entra</span>{title("Um link que <span>agenda.</span>")}{svc("lp")}{svc("bio")}')
p4 = page(4, f'<span class="pill">O que entra</span>{title("Uma vitrine que <span>vende.</span>")}{svc("posts")}{svc("porta")}')

# 5 · pacotes
PK = [
    ('Proposta para ti', 'Vitrine', 'Perfil, link e porta trabalhando por ti.', 940, 500, True,
     [('Landing page', 0), ('Bio + capas dos destaques', 0), ('6 primeiros posts com legenda', 0), ('Arte da porta para impressão', 0)]),
    ('Mais conteúdo', 'Vitrine + Conteúdo', 'Pra manter o feed bonito no primeiro mês.', 1400, 700, False,
     [('Tudo do pacote Vitrine', 0), ('+ 6 posts (12 no total)', 1), ('+ 4 modelos de stories editáveis: promoção, agenda, antes e depois, depoimento', 1)]),
    ('Mais alcance', 'Presença Completa', 'Pra ser achada no Google e no Instagram.', 2110, 1100, False,
     [('Tudo do Vitrine + Conteúdo', 0), ('+ 6 posts (18 no total)', 1), ('+ Perfil no Google Meu Negócio otimizado', 1),
      ('+ Tabela de serviços e valores (digital e impressa)', 1), ('+ Plaquinha de balcão com QR Code', 1)]),
]


def card(ph, nome, fr, av, pr, best, itens):
    lis = ''.join(f'<li class="{"pl" if p else ""}">{t}</li>' for t, p in itens)
    tg = '<span class="tg">Recomendado</span>' if best else ''
    return (f'<div class="p{" best" if best else ""}">{tg}<span class="ph">{ph}</span><h4>{nome}</h4><p class="fr">{fr}</p>'
            f'<div class="old">avulso {brl(av)}</div><div class="pr">{brl(pr)}</div><div class="sv">economia de {brl(av - pr)}</div><ul>{lis}</ul></div>')


p5 = page(5, f'''<span class="pill">Investimento</span>
{title('Junto sai <span>mais barato.</span>', True)}
<p class="lead">Cada serviço pode ser contratado sozinho. No pacote, tudo é criado junto, com a mesma identidade, e o valor cai.</p>
<div class="pk">{"".join(card(*x) for x in PK)}</div>
<div class="note">Avulso, landing page + bio e destaques + 6 posts + arte da porta somam <b>R$ 940</b>. No pacote Vitrine, tu leva tudo por <b>R$ 500</b>.</div>
<span class="pill" style="margin-top:8mm">Como funciona</span>
<div class="steps am-steps">
<div><i>1</i><b>Conversa</b><p>Entendemos teus serviços, valores e a cliente que tu quer atrair.</p></div>
<div><i>2</i><b>Material</b><p>Tu manda as melhores fotos de resultado. A gente escolhe e trata.</p></div>
<div><i>3</i><b>Criação</b><p>Montamos página, bio, destaques, posts e a arte da porta.</p></div>
<div><i>4</i><b>Entrega e ajuste</b><p>Tu revisa com a gente, ajusta e começa a usar.</p></div>
</div>
''', am=True)

# 6 · tabela + como funciona
ROWS = [('Landing page', 400, 1, 1, 1), ('Bio + capas dos destaques', 150, 1, 1, 1), ('6 primeiros posts', 300, 1, 1, 1),
        ('Arte da porta', 90, 1, 1, 1), ('+ 6 posts', 300, 0, 1, 1), ('4 modelos de stories', 160, 0, 1, 1),
        ('+ 6 posts', 300, 0, 0, 1), ('Google Meu Negócio', 200, 0, 0, 1), ('Tabela de serviços e valores', 120, 0, 0, 1),
        ('Plaquinha com QR Code', 90, 0, 0, 1)]


def mk(x): return '<span class="ok">●</span>' if x else '<span class="no">–</span>'


trs = ''.join(f'<tr><td>{n}</td><td class="r">{brl(v)}</td><td class="c">{mk(a)}</td><td class="c">{mk(b)}</td><td class="c">{mk(c)}</td></tr>'
              for n, v, a, b, c in ROWS)
trs += '<tr class="sum"><td>Soma avulsa</td><td></td><td class="c">R$ 940</td><td class="c">R$ 1.400</td><td class="c">R$ 2.110</td></tr>'
trs += '<tr class="fin"><td>No pacote</td><td></td><td class="c">R$ 500</td><td class="c">R$ 700</td><td class="c">R$ 1.100</td></tr>'

p6 = page(6, f'''<span class="pill">Valores e condições</span>
{title('Monta do teu <span>jeito.</span>')}
<table><thead><tr><th>Serviço</th><th class="r">Avulso</th><th class="c">Vitrine</th><th class="c">+ Conteúdo</th><th class="c">Completa</th></tr></thead><tbody>{trs}</tbody></table>
<div class="two">
<div class="bx"><b>Condições</b><ul><li>50% pra começar e 50% na entrega, no Pix.</li><li>Pacotes de R$ 700 e R$ 1.100 em até 3x sem acréscimo.</li>
<li>2 rodadas de ajuste incluídas.</li><li>Prazo: 15 dias úteis após receber as fotos.</li><li>Proposta válida por 15 dias.</li></ul></div>
<div class="bx"><b>Não incluso</b><ul><li>Impressão e instalação da arte da porta.</li><li>Domínio próprio (.com.br), se tu quiser: cerca de R$ 40/ano.</li>
<li>Ensaio fotográfico (sob consulta com a nossa equipe).</li><li>Gestão mensal e tráfego pago.</li></ul></div>
</div>''')

# 7 · próximos passos
p7 = page(7, f'''<span class="pill">Próximo passo</span>
{title('Bora deixar teu perfil<br>à altura do teu <span>trabalho?</span>', True)}
<p class="lead">Marca o pacote, assina e manda pra gente no WhatsApp. Começamos na semana seguinte.</p>
<div class="chk">
<div><i></i><span><b>Vitrine · R$ 500</b><small>Landing page, bio, destaques, 6 primeiros posts e arte da porta.</small></span></div>
<div><i></i><span><b>Vitrine + Conteúdo · R$ 700</b><small>Tudo do Vitrine + 6 posts e 4 modelos de stories.</small></span></div>
<div><i></i><span><b>Presença Completa · R$ 1.100</b><small>Tudo acima + 6 posts, Google Meu Negócio, tabela de valores e plaquinha QR Code.</small></span></div>
<div><i></i><span><b>Pra começar, a gente precisa de</b><small>Lista de serviços com valores, medidas da porta e 10 a 20 fotos de antes e depois.</small></span></div>
</div>
<div class="sig"><div>Débora Brasil · assinatura e data</div><div>House do Creator · assinatura e data</div></div>
<div class="cta"><small>WhatsApp</small><b>(81) 98355-4583</b></div>
<div class="who"><span><small>Instagram</small>@housedocreator</span><span><small>CEOs</small>Ryan Coimbra &amp; Fontenele</span></div>''', am=True)

open('proposta_debora.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Proposta · Débora Brasil Beauty</title>{CSS}</head>'
    f'<body>{p1}{p2}{p3}{p4}{p5}{p6}{p7}</body></html>')
