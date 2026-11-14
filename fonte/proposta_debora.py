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

/* capa com foto */
.cover .hero{width:100%;height:66mm;border-radius:5mm;margin-top:9mm;position:relative;overflow:hidden;background:#ccc}
.cover .hero img.f{width:100%;height:100%;object-fit:cover;object-position:50% 42%;display:block}
.cover .hero .lg{position:absolute;right:5mm;top:50%;transform:translateY(-50%);height:17mm}
.cover .for{display:flex;align-items:center;gap:5mm;text-align:left}
.cover .for img{height:11mm}
/* prévia */
.pv{display:grid;grid-template-columns:76mm 1fr;gap:7mm;width:100%;margin-top:6mm;align-items:start}
.cap2{font-size:6.6pt;color:var(--soft);margin-top:2mm;text-align:center}
.cap2 b{color:var(--y)}
.ph2{background:#000;border-radius:7mm;padding:2.2mm;border:1px solid #333}
.sc{background:#fff;border-radius:5mm;overflow:hidden;color:#111;font-size:5.6pt;line-height:1.35}
.igt{display:flex;justify-content:space-between;padding:2.5mm 3mm 1mm;font-weight:700;font-size:7pt}
.igh{display:flex;align-items:center;gap:3mm;padding:1mm 3mm}
.av{width:13mm;height:13mm;border-radius:50%;padding:.6mm;background:linear-gradient(45deg,#d8bcbc,#9a7070);flex:none}
.av img{width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:60% 25%;border:.6mm solid #fff;display:block}
.st{display:flex;flex:1;justify-content:space-around;text-align:center}
.st b{display:block;font-size:6.6pt}
.bio2{padding:1.2mm 3mm 0}
.bio2 b{font-size:6pt}
.bio2 .ct{color:#888}
.bio2 .lk{color:#9a7070;font-weight:600}
.btn2{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1mm;padding:2mm 3mm}
.btn2 span{background:#efefef;border-radius:1.2mm;text-align:center;padding:1mm 0;font-weight:600}
.btn2 span.on{background:#9a7070;color:#fff}
.hl2{display:flex;justify-content:space-between;padding:1mm 3mm 2.5mm}
.hl2 div{display:flex;flex-direction:column;align-items:center;gap:.8mm;width:10mm}
.hl2 i{width:10mm;height:10mm;border-radius:50%;border:.35mm solid #d8bcbc;padding:.6mm;display:block}
.hl2 i span{display:flex;width:100%;height:100%;border-radius:50%;background:#f5efe8;align-items:center;justify-content:center;font-family:'Playfair Display';font-style:italic;font-weight:700;color:#9a7070;font-size:6.5pt}
.hl2 small{font-size:4.6pt;white-space:nowrap}
.gr{display:grid;grid-template-columns:repeat(3,1fr);gap:.4mm;border-top:.3mm solid #eee}
.t{aspect-ratio:4/5;position:relative;overflow:hidden;background:#f5efe8;font-family:'Playfair Display'}
.t img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.t .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(60,35,35,0) 45%,rgba(60,35,35,.75))}
.t .tx{position:absolute;left:2mm;right:2mm;bottom:2mm;color:#fff;font-size:7pt;line-height:1.05;font-weight:600}
.t .tx small{display:block;font-family:'Poppins';font-size:4pt;letter-spacing:.6px;text-transform:uppercase;font-weight:500;margin-bottom:.6mm;color:#f5efe8}
.t.m{background:#9a7070;color:#fff;padding:2.5mm;display:flex;flex-direction:column;justify-content:center}
.t.m b{font-size:7.5pt;line-height:1.05}
.t.m ul{list-style:none;font-family:'Poppins';font-size:4.4pt;margin-top:1.5mm}
.t.m li{border-top:.2mm solid rgba(255,255,255,.4);padding:.6mm 0}
.t.c{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#9a7070;padding:2mm}
.t.c img{position:static;width:13mm;height:auto}
.t.c b{font-size:6.6pt;margin-top:1mm}
.t.c small{font-family:'Poppins';font-size:4pt;color:#6d5050}
.pin2{position:absolute;top:1mm;right:1mm;width:2.4mm;height:2.4mm;z-index:3}
/* porta */
.door2{height:118mm;border-radius:2.5mm;background:#3b3533;padding:2.2mm;position:relative}
.gl{height:100%;border-radius:1mm;background:linear-gradient(160deg,#8e9aa0,#5d686e 55%,#79858b);position:relative;overflow:hidden}
.gl:after{content:'';position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.22) 0 18%,transparent 18% 40%,rgba(255,255,255,.12) 40% 47%,transparent 47%)}
.vin{position:absolute;left:7mm;right:7mm;top:13mm;bottom:12mm;background:rgba(245,239,232,.93);border-radius:1mm;display:flex;flex-direction:column;align-items:center;padding:7mm 4mm 5mm;text-align:center;color:#9a7070;z-index:1}
.vin img{width:46mm}
.vin ul{list-style:none;font-size:5.8pt;letter-spacing:1.4px;text-transform:uppercase;margin-top:5mm;line-height:2;color:#6d5050}
.vin .rd{margin-top:auto;border-top:.3mm solid #d8bcbc;padding-top:2.5mm;width:100%;font-size:5.8pt;color:#6d5050;line-height:1.6}
.vin .rd b{color:#9a7070}
.hd2{position:absolute;right:3.5mm;top:48%;width:1.5mm;height:18mm;background:#cfcfcf;border-radius:1mm;z-index:2}
/* landing */
.lp2{margin-top:5mm;background:#fff;border-radius:3mm;overflow:hidden;color:#3d2a2a}
.lp2 .bar{background:#eee;height:4.5mm;display:flex;align-items:center;gap:1mm;padding:0 2mm;font-size:4.6pt;color:#888}
.lp2 .bar i{width:1.4mm;height:1.4mm;border-radius:50%;background:#ccc;display:block}
.lp2 .hr2{display:grid;grid-template-columns:1fr 38mm;background:#f5efe8;height:42mm}
.lp2 .hr2 div{padding:4mm;display:flex;flex-direction:column;justify-content:center}
.lp2 .hr2 img.lg{height:7mm;align-self:flex-start}
.lp2 .hr2 b{font-family:'Playfair Display';font-size:10pt;line-height:1.08;margin-top:2.5mm;color:#6d4848}
.lp2 .hr2 span{margin-top:2.5mm;background:#9a7070;color:#fff;font-size:5.2pt;font-weight:600;border-radius:5mm;padding:1.2mm 3mm;align-self:flex-start}
.lp2 .hr2 img.f{width:100%;height:100%;object-fit:cover;object-position:60% 30%}
.pal{display:flex;gap:2mm;margin-top:4mm;align-items:center;font-size:6.4pt;color:var(--soft)}
.pal i{width:5mm;height:5mm;border-radius:1.4mm;display:block;border:.3mm solid #333}
</style>'''

CLIENTE = 'Proposta · Débora Brasil Beauty'
TOTAL = 8
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
<div class="hero"><img class="f" src="img/debora/pinca.jpg"><img class="lg" src="img/debora/logo-horizontal.png"></div>
<div class="for"><img src="img/debora/logo-circulo-branco.png"><div><b>Débora Brasil · @deborabrasilbeauty</b><small>Micropigmentação · Brow lamination · Lash lifting · Maquiagem</small></div></div>
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

PIN = '<svg class="pin2" viewBox="0 0 24 24" fill="#fff"><path d="M16 3l5 5-3 1-4 4 1 5-2 2-4-4-5 5-1-1 5-5-4-4 2-2 5 1 4-4z"/></svg>'
p5 = page(5, f'''<span class="pill">Uma prévia</span>
{title('Tua marca, do feed <span>à porta.</span>')}
<p class="lead">Um esboço com a tua identidade, a paleta da marca e as fotos do teu ensaio, só pra tu visualizar. O material final é criado junto contigo depois da conversa.</p>
<div class="pv">
<div><div class="ph2"><div class="sc">
<div class="igt"><span>deborabrasilbeauty</span><span>···</span></div>
<div class="igh"><div class="av"><img src="img/debora/pinca.jpg"></div>
<div class="st"><div><b>497</b>posts</div><div><b>2.582</b>seguidores</div><div><b>4.621</b>seguindo</div></div></div>
<div class="bio2"><b>Débora Brasil Beauty</b><br><span class="ct">Estúdio de beleza</span><br>
Sobrancelhas, micropigmentação e lash lifting<br>que valorizam o teu olhar.<br>
Galeria Ponto Certo · Piedade, Jaboatão<br>Agende pelo link abaixo<br><span class="lk">deborabrasilbeauty.com.br</span></div>
<div class="btn2"><span class="on">Seguir</span><span>Mensagem</span><span>WhatsApp</span></div>
<div class="hl2">
<div><i><span>Ag</span></i><small>Agende</small></div><div><i><span>Mf</span></i><small>Micro fio</small></div>
<div><i><span>Bl</span></i><small>Brow</small></div><div><i><span>Ll</span></i><small>Lash</small></div>
<div><i><span>Mq</span></i><small>Make</small></div><div><i><span>On</span></i><small>Onde</small></div></div>
<div class="gr">
<div class="t">{PIN}<img src="img/debora/sentada.jpg" style="object-position:50% 20%"><div class="sh"></div><div class="tx"><small>Prazer</small>Eu sou a Débora</div></div>
<div class="t m">{PIN}<b>O que eu faço por você</b><ul><li>Design de sobrancelhas</li><li>Micro fio a fio</li><li>Brow lamination</li><li>Lash lifting</li><li>Maquiagem</li></ul></div>
<div class="t">{PIN}<img src="img/debora/paquimetro.jpg" style="object-position:50% 25%"><div class="sh"></div><div class="tx"><small>Design</small>Medido pro teu rosto</div></div>
<div class="t"><img src="img/debora/caneta.jpg" style="object-position:30% 50%"><div class="sh"></div><div class="tx"><small>Micropigmentação</small>Fio a fio natural</div></div>
<div class="t c"><img src="img/debora/logo-circulo.png"><b>Onde estamos</b><small>Galeria Ponto Certo<br>Piedade · Jaboatão</small></div>
<div class="t"><img src="img/debora/celular.jpg" style="object-position:55% 30%"><div class="sh"></div><div class="tx"><small>Agenda aberta</small>Chama no WhatsApp</div></div>
</div></div></div>
<p class="cap2"><b>Bio, destaques e os 6 primeiros posts</b> · 3 fixados no topo</p></div>
<div><div class="door2"><div class="gl"><div class="vin"><img src="img/debora/logo-horizontal.png">
<ul><li>Design de sobrancelhas</li><li>Micropigmentação</li><li>Brow lamination</li><li>Lash lifting</li><li>Maquiagem</li></ul>
<div class="rd">Atendimento com hora marcada · <b>9h às 18h</b><br>@deborabrasilbeauty · Agende pelo WhatsApp</div></div></div><div class="hd2"></div></div>
<p class="cap2"><b>Arte da porta</b> · medidas e informações a confirmar</p>
<div class="lp2"><div class="bar"><i></i><i></i><i></i>&nbsp;deborabrasilbeauty.com.br</div>
<div class="hr2"><div><img class="lg" src="img/debora/logo-horizontal.png"><b>Sobrancelhas que valorizam o teu olhar.</b><span>Agendar no WhatsApp</span></div><img class="f" src="img/debora/sentada-h.jpg"></div></div>
<p class="cap2"><b>Landing page</b> · abertura da página no computador e no celular</p>
<div class="pal">Paleta da marca: <i style="background:#f5efe8"></i>#F5EFE8 <i style="background:#9a7070"></i>#9A7070 <i style="background:#d8bcbc"></i>#D8BCBC</div>
</div></div>''')

# 6 · pacotes
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


p6 = page(6, f'''<span class="pill">Investimento</span>
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

p7 = page(7, f'''<span class="pill">Valores e condições</span>
{title('Monta do teu <span>jeito.</span>')}
<table><thead><tr><th>Serviço</th><th class="r">Avulso</th><th class="c">Vitrine</th><th class="c">+ Conteúdo</th><th class="c">Completa</th></tr></thead><tbody>{trs}</tbody></table>
<div class="two">
<div class="bx"><b>Condições</b><ul><li>50% pra começar e 50% na entrega, no Pix.</li><li>Pacotes de R$ 700 e R$ 1.100 em até 3x sem acréscimo.</li>
<li>2 rodadas de ajuste incluídas.</li><li>Prazo: 15 dias úteis após receber as fotos.</li><li>Proposta válida por 15 dias.</li></ul></div>
<div class="bx"><b>Não incluso</b><ul><li>Impressão e instalação da arte da porta.</li><li>Domínio próprio (.com.br), se tu quiser: cerca de R$ 40/ano.</li>
<li>Ensaio fotográfico (sob consulta com a nossa equipe).</li><li>Gestão mensal e tráfego pago.</li></ul></div>
</div>''')

# 7 · próximos passos
p8 = page(8, f'''<span class="pill">Próximo passo</span>
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
    f'<body>{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}</body></html>')
