"""Proposta · Débora Brasil Beauty · landing page, Instagram e arte da porta (5 páginas)."""

CSS = '''<style>
@import url('fonts.css');@import url('fonts2.css');@import url('fonts3.css');
:root{--ink:#2b2220;--muted:#7a6a64;--line:#eadfd8;--paper:#f7f0ea;--acc:#8c5a57;--acc2:#c99a8f;--soft:#f3e4de}
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Poppins',sans-serif;color:var(--ink);font-size:9.5pt;line-height:1.45;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.in{position:absolute;left:20mm;right:20mm;top:18mm;bottom:16mm}
.ft{position:absolute;left:20mm;right:20mm;bottom:8mm;display:flex;justify-content:space-between;font-size:6.8pt;color:var(--muted)}
.k{font-size:7.5pt;font-weight:600;color:var(--acc);letter-spacing:2px;text-transform:uppercase}
h2{font-family:'Playfair Display',serif;font-weight:700;font-size:28pt;line-height:1.02;margin:2mm 0 3mm}
h2 span{color:var(--acc);font-style:italic}
.lead{font-size:10.5pt;color:#4a3f3b;max-width:162mm}
.band{position:absolute;left:0;right:0;height:3mm;background:linear-gradient(90deg,var(--acc),var(--acc2))}
.tag{display:inline-block;font-size:6.6pt;font-weight:700;letter-spacing:.6px;padding:1px 7px;border-radius:3px;background:var(--acc);color:#fff;text-transform:uppercase}
/* capa */
.cover{background:var(--paper)}
.cover .in{top:24mm;bottom:22mm}
.mono{width:30mm;height:30mm;border-radius:50%;border:1px solid var(--acc);display:flex;align-items:center;justify-content:center;font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:24pt;color:var(--acc)}
.cover h1{font-family:'Playfair Display',serif;font-weight:700;font-size:40pt;line-height:1;margin-top:36mm}
.cover h1 span{display:block;color:var(--acc);font-style:italic}
.cover .sub{font-size:12pt;margin-top:8mm;max-width:150mm;color:#4a3f3b;line-height:1.55}
.cover .chips{display:flex;flex-wrap:wrap;gap:2.5mm;margin-top:9mm}
.cover .chips span{border:1px solid var(--acc2);border-radius:20px;padding:1.5mm 4mm;font-size:8.4pt;color:var(--acc);font-weight:500;background:#fff}
.cover .meta{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;font-size:8.5pt;color:var(--muted);border-top:1px solid var(--line);padding-top:5mm}
.cover .meta b{color:var(--ink);font-weight:600}
/* diagnóstico */
.diag{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:6mm}
.col h4{font-family:'Playfair Display';font-weight:700;font-size:13pt;margin-bottom:2mm}
.col ul{list-style:none}
.col li{padding:2.2mm 0 2.2mm 6mm;border-top:1px solid var(--line);position:relative;font-size:8.8pt;color:#3d3431}
.col li:before{position:absolute;left:0;top:2.1mm;font-weight:700}
.col.bad li:before{content:'–';color:#b06a5e}
.col.good li:before{content:'✓';color:var(--acc)}
.col li b{color:var(--ink)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-top:6mm}
.stats div{background:var(--paper);border-radius:6px;padding:4mm;text-align:center}
.stats b{font-family:'Playfair Display';font-size:19pt;display:block;line-height:1;color:var(--acc)}
.stats small{font-size:7.4pt;color:var(--muted)}
.quote{margin-top:7mm;background:var(--ink);color:#fff;border-radius:8px;padding:6mm 8mm;font-size:11.5pt;line-height:1.5}
.quote b{color:#f0c9bd}
/* entregas */
.ent{display:grid;grid-template-columns:1fr 62mm;gap:7mm;margin-top:5mm}
.it{display:grid;grid-template-columns:9mm 1fr auto;gap:3mm;padding:3.4mm 0;border-top:1px solid var(--line);align-items:start}
.it .n{font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:15pt;color:var(--acc);line-height:1}
.it b{font-family:'Playfair Display';font-weight:700;font-size:11.5pt;display:block;line-height:1.15}
.it p{font-size:8.3pt;color:#4a3f3b;margin-top:.8mm}
.it .v{font-size:8.6pt;color:var(--muted);text-decoration:line-through;white-space:nowrap;padding-top:1mm}
.tot{display:flex;justify-content:space-between;align-items:center;background:var(--ink);color:#fff;border-radius:8px;padding:5mm 6mm;margin-top:3mm}
.tot small{display:block;font-size:7.8pt;color:#d8cbc5}
.tot .old{font-size:10pt;color:#d8cbc5;text-decoration:line-through;margin-right:3mm}
.tot .pr{font-family:'Playfair Display';font-weight:700;font-size:26pt;white-space:nowrap}
.tot .save{font-size:8pt;color:#f0c9bd;font-weight:600;text-align:right}
/* porta (mockup) */
.door{height:178mm;border-radius:3mm;background:linear-gradient(180deg,#d9dfe2,#c5ccd0);padding:5mm;position:relative;box-shadow:inset 0 0 0 2.2mm #4a4442}
.glass{position:absolute;inset:5mm;border-radius:1mm;background:linear-gradient(160deg,rgba(255,255,255,.55),rgba(255,255,255,.1) 45%,rgba(255,255,255,.35));display:flex;flex-direction:column;align-items:center;padding:12mm 4mm 6mm;text-align:center;color:var(--acc)}
.glass .mono{width:24mm;height:24mm;font-size:18pt;background:rgba(255,255,255,.65)}
.glass .nm{font-family:'Playfair Display';font-weight:600;font-size:13pt;color:var(--ink);margin-top:4mm;letter-spacing:.5px}
.glass .bt{font-size:6.4pt;letter-spacing:3px;text-transform:uppercase;color:var(--acc)}
.glass ul{list-style:none;margin-top:7mm;font-size:7pt;color:var(--ink);line-height:1.9}
.glass .hr{margin-top:auto;font-size:6.6pt;color:var(--ink);line-height:1.6;border-top:1px solid var(--acc2);padding-top:3mm;width:100%}
.glass .hr b{color:var(--acc)}
.handle{position:absolute;right:8mm;top:50%;width:2mm;height:24mm;background:#4a4442;border-radius:1mm}
.cap{font-size:7.4pt;color:var(--muted);margin-top:2mm;text-align:center}
/* pacotes */
.pk{display:grid;grid-template-columns:1.1fr 1fr 1fr;gap:4mm;margin-top:6mm;align-items:stretch}
.p{border:1.5px solid var(--line);border-radius:8px;padding:6mm 5mm;display:flex;flex-direction:column;position:relative}
.p.best{border:2.5px solid var(--acc);box-shadow:0 0 0 4px var(--soft)}
.p.best .tag{position:absolute;top:-3mm;left:50%;transform:translateX(-50%);font-size:7.2pt;padding:2px 10px;white-space:nowrap}
.p h4{font-family:'Playfair Display';font-weight:700;font-size:15pt;line-height:1.05}
.p .for{font-size:8pt;color:var(--muted);margin:1.5mm 0 3mm;min-height:9mm}
.p .pr{font-family:'Playfair Display';font-weight:700;font-size:26pt;line-height:1;white-space:nowrap}
.p .pr small{display:block;font-size:7.6pt;font-family:'Poppins';font-weight:500;color:var(--muted);margin-bottom:1mm;text-decoration:line-through}
.p .save{font-size:8pt;color:var(--acc);font-weight:600;margin-top:1.2mm}
.p ul{list-style:none;margin-top:4mm;font-size:8.3pt}
.p li{padding:1.3mm 0 1.3mm 5mm;position:relative;border-top:1px solid var(--line)}
.p li:before{content:'✓';position:absolute;left:0;color:var(--acc);font-weight:700}
.p li.plus{color:var(--acc);font-weight:600}
.p li.plus:before{content:'+'}
table{width:100%;border-collapse:collapse;font-size:8.8pt;margin-top:3mm}
th{font-weight:600;text-transform:uppercase;letter-spacing:.8px;font-size:7pt;text-align:left;padding:5px 8px;background:var(--ink);color:#fff}
td{padding:5px 8px;border-bottom:1px solid var(--line)}
td.r,th.r{text-align:right;white-space:nowrap}
td.c,th.c{text-align:center}
.y{color:var(--acc);font-weight:700}
.no{color:#cbbdb6}
tr.sum td{font-weight:600;background:var(--paper)}
tr.fin td{font-weight:700;font-family:'Playfair Display';font-size:11pt;color:var(--acc)}
.note{font-size:7.6pt;color:var(--muted);margin-top:2mm}
/* como funciona */
.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-top:6mm}
.tl div{position:relative;padding-top:9mm}
.tl div:before{content:attr(data-n);position:absolute;top:0;left:0;width:7mm;height:7mm;border-radius:50%;background:var(--acc);color:#fff;font-family:'Playfair Display';font-weight:700;display:flex;align-items:center;justify-content:center;font-size:10pt}
.tl b{font-family:'Playfair Display';font-weight:700;font-size:11pt;display:block}
.tl p{font-size:8.3pt;color:#4a3f3b}
.two{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:7mm}
.box{background:var(--paper);border-radius:8px;padding:5mm 6mm}
.box h4{font-family:'Playfair Display';font-weight:700;font-size:12pt;margin-bottom:2mm}
.box ul{padding-left:4.5mm;font-size:8.6pt}.box li{margin:1.2mm 0}.box li::marker{color:var(--acc)}
.ok{margin-top:7mm;border:1.5px dashed var(--acc);border-radius:8px;padding:6mm}
.ok h4{font-family:'Playfair Display';font-weight:700;font-size:14pt}
.ok .opts{display:flex;flex-direction:column;gap:2mm;margin:3mm 0 12mm;font-size:9.5pt}
.ok .sg{display:grid;grid-template-columns:1fr 1fr;gap:12mm;text-align:center;font-size:7.6pt;color:var(--muted)}
.ok .sg div{border-top:1px solid var(--ink);padding-top:2mm}
</style>'''

PROV = 'House do Creator'
DATA = '14/11/2026'
TOTAL = 5


def page(n, body):
    return (f'<section class="page"><div class="band" style="top:0"></div><div class="in">{body}</div>'
            f'<div class="ft"><span>Débora Brasil Beauty · Proposta de landing page, Instagram e arte da porta</span>'
            f'<span>{n} / {TOTAL}</span></div></section>')


cover = f'''<section class="page cover"><div class="band" style="top:0"></div><div class="in">
<div class="mono">DB</div>
<h1>O seu trabalho já é lindo.<span>Agora o perfil também.</span></h1>
<p class="sub">Uma proposta para a Débora Brasil Beauty chegar mais organizada a quem procura sobrancelha, micropigmentação e lash lifting em Piedade e Candeias: do Instagram ao WhatsApp, até a porta do estúdio.</p>
<div class="chips"><span>Landing page</span><span>Bio + destaques</span><span>6 primeiros posts</span><span>Arte da porta</span></div>
<div class="meta"><span>Para: <b>Débora Brasil · @deborabrasilbeauty</b></span><span>Por: <b>{PROV}</b></span><span>{DATA}</span></div>
</div><div class="band" style="bottom:0"></div></section>'''

p2 = page(2, '''<div class="k">O que vimos no seu perfil</div><h2>Resultado de sobra.<br><span>Falta a vitrine.</span></h2>
<p class="lead">As fotos de antes e depois mostram técnica e capricho. O que atrapalha é a forma como o perfil apresenta esse trabalho para quem chega pela primeira vez.</p>
<div class="stats">
<div><b>491</b><small>posts publicados</small></div>
<div><b>2.582</b><small>seguidoras</small></div>
<div><b>5</b><small>destaques sem padrão</small></div>
<div><b>0</b><small>página com serviços e preços</small></div>
</div>
<div class="diag">
<div class="col bad"><h4>Hoje</h4><ul>
<li><b>Feed sem identidade:</b> resultados, recados, Natal, show e café se misturam, e a logo DB quase não aparece.</li>
<li><b>Bio cortada:</b> os serviços somem no "mais" e o endereço ocupa três linhas.</li>
<li><b>Destaques com capas de foto,</b> cada uma de um jeito, e nomes cortados ("Novo ender…", "Brow la…").</li>
<li><b>Link direto para o WhatsApp:</b> a cliente chega sem saber serviços, valores ou como funciona.</li>
<li><b>Porta sem comunicação:</b> quem passa na galeria não sabe que ali tem um estúdio de beleza do olhar.</li></ul></div>
<div class="col good"><h4>Depois</h4><ul>
<li><b>6 primeiros posts</b> que apresentam você, os serviços e os resultados com a mesma cara.</li>
<li><b>Bio curta e clara:</b> o que você faz, onde fica e um botão para agendar.</li>
<li><b>Destaques organizados</b> com capas no tom nude e rosé da marca DB.</li>
<li><b>Landing page</b> com serviços, fotos, endereço e agendamento pelo WhatsApp num só link.</li>
<li><b>Arte da porta</b> com logo, serviços, horário e @ para quem passa na galeria virar cliente.</li></ul></div>
</div>
<div class="quote">Quem procura sobrancelha decide pelo perfil em poucos segundos. <b>Um perfil organizado transforma visita em agendamento, sem precisar postar mais.</b></div>''')

ITENS = [
    ('Landing page', 'Página com seus serviços, fotos de resultados, endereço com mapa, horário e botão de agendar no WhatsApp. Vira o link da bio.', 400),
    ('Bio + destaques', 'Bio reescrita e capas para os destaques (Micro fio a fio, Brow lamination, Lash lifting, Maquiagem, Onde estamos, Agende) no tom da marca.', 150),
    ('6 primeiros posts', 'Seis artes para o topo do feed, com legenda: quem é a Débora, serviços, antes e depois, onde fica e como agendar. Três ficam fixados.', 300),
    ('Arte da porta', 'Arte em tamanho real para impressão (adesivo ou vinil): logo DB, serviços, horário, @ e WhatsApp. Arquivo pronto para a gráfica.', 90),
]

itens_html = ''.join(
    f'<div class="it"><span class="n">0{i + 1}</span><div><b>{t}</b><p>{d}</p></div><span class="v">R$ {v}</span></div>'
    for i, (t, d, v) in enumerate(ITENS))

p3 = page(3, f'''<div class="k">A proposta</div><h2>Tudo junto <span>por R$ 500</span></h2>
<p class="lead">Separados, os quatro serviços somam R$ 940. No pacote eles saem por R$ 500, porque são criados juntos, com a mesma identidade.</p>
<div class="ent"><div>{itens_html}
<div class="tot"><div><small>Pacote Vitrine · tudo acima</small><span class="old">R$ 940</span></div>
<div><div class="pr">R$ 500</div><div class="save">economia de R$ 440</div></div></div>
<p class="note">Prazo: 15 dias úteis após o briefing e o envio das fotos. Impressão da porta não inclusa.</p></div>
<div><div class="door"><div class="glass">
<div class="mono">DB</div><div class="nm">Débora Brasil</div><div class="bt">Beauty</div>
<ul><li>Design de sobrancelhas</li><li>Micropigmentação fio a fio</li><li>Brow lamination</li><li>Lash lifting</li><li>Maquiagem</li></ul>
<div class="hr">Seg a sáb · <b>9h às 18h</b><br>@deborabrasilbeauty<br>Agende pelo WhatsApp</div>
</div><div class="handle"></div></div>
<p class="cap">Ideia da arte da porta. Medidas e horários a confirmar.</p></div>
</div>''')

PK = [
    ('Vitrine', 'O essencial para o perfil e o estúdio venderem por você.', 940, 500, True, [
        ('Landing page', 0), ('Bio + capas dos destaques', 0), ('6 primeiros posts com legenda', 0), ('Arte da porta para impressão', 0)]),
    ('Vitrine + Conteúdo', 'Para manter o feed bonito no primeiro mês.', 1400, 700, False, [
        ('Tudo do pacote Vitrine', 0), ('+ 6 posts (12 no total)', 1), ('+ 4 modelos de stories editáveis: promoção, agenda, antes e depois, depoimento', 1)]),
    ('Presença Completa', 'Para ser achada no Google e no Instagram.', 2110, 1100, False, [
        ('Tudo do Vitrine + Conteúdo', 0), ('+ 6 posts (18 no total)', 1), ('+ Perfil no Google Meu Negócio otimizado', 1),
        ('+ Tabela de serviços e valores (digital e impressa)', 1), ('+ Plaquinha de balcão com QR Code', 1)]),
]


def card(nome, para, avulso, preco, best, itens):
    lis = ''.join(f'<li class="{"plus" if p else ""}">{t.lstrip("+ ") if p else t}</li>' for t, p in itens)
    tag = '<span class="tag">Proposta para você</span>' if best else ''
    return (f'<div class="p{" best" if best else ""}">{tag}<h4>{nome}</h4><div class="for">{para}</div>'
            f'<div class="pr"><small>avulso {brl(avulso)}</small>{brl(preco)}</div>'
            f'<div class="save">economia de {brl(avulso - preco)}</div><ul>{lis}</ul></div>')


ROWS = [
    ('Landing page', 400, 1, 1, 1),
    ('Bio + capas dos destaques', 150, 1, 1, 1),
    ('6 primeiros posts', 300, 1, 1, 1),
    ('Arte da porta', 90, 1, 1, 1),
    ('+ 6 posts', 300, 0, 1, 1),
    ('4 modelos de stories', 160, 0, 1, 1),
    ('+ 6 posts', 300, 0, 0, 1),
    ('Google Meu Negócio', 200, 0, 0, 1),
    ('Tabela de serviços e valores', 120, 0, 0, 1),
    ('Plaquinha QR Code', 90, 0, 0, 1),
]


def brl(v): return f'R$ {v:,}'.replace(',', '.')


def mark(x): return '<span class="y">✓</span>' if x else '<span class="no">–</span>'


trs = ''.join(f'<tr><td>{n}</td><td class="r">{brl(v)}</td><td class="c">{mark(a)}</td><td class="c">{mark(b)}</td><td class="c">{mark(c)}</td></tr>'
              for n, v, a, b, c in ROWS)
trs += '<tr class="sum"><td>Soma avulsa</td><td></td><td class="c">R$ 940</td><td class="c">R$ 1.400</td><td class="c">R$ 2.110</td></tr>'
trs += '<tr class="fin"><td>No pacote</td><td></td><td class="c">R$ 500</td><td class="c">R$ 700</td><td class="c">R$ 1.100</td></tr>'

p4 = page(4, f'''<div class="k">Investimento</div><h2>Escolha o <span>seu pacote</span></h2>
<p class="lead">Cada serviço pode ser contratado sozinho, mas no pacote tudo sai mais barato.</p>
<div class="pk">{"".join(card(*x) for x in PK)}</div>
<table><thead><tr><th>Serviço</th><th class="r">Avulso</th><th class="c">Vitrine</th><th class="c">+ Conteúdo</th><th class="c">Completa</th></tr></thead>
<tbody>{trs}</tbody></table>''')

p5 = page(5, f'''<div class="k">Como funciona</div><h2>Simples e <span>no seu ritmo</span></h2>
<div class="tl">
<div data-n="1"><b>Conversa</b><p>30 minutos para entender serviços, valores, público e o que você quer destacar.</p></div>
<div data-n="2"><b>Fotos e textos</b><p>Você envia as melhores fotos de resultados. A gente escolhe, trata e escreve.</p></div>
<div data-n="3"><b>Aprovação</b><p>Você vê tudo antes de publicar e pede os ajustes que quiser.</p></div>
<div data-n="4"><b>Entrega</b><p>Página no ar, perfil atualizado, posts prontos e arte da porta para a gráfica.</p></div>
</div>
<div class="two">
<div class="box"><h4>Condições</h4><ul>
<li>50% para começar e 50% na entrega, por Pix.</li>
<li>Pacotes de R$ 700 e R$ 1.100 em até 3x sem acréscimo.</li>
<li>2 rodadas de ajuste incluídas.</li>
<li>Arquivos finais e direito de uso ficam com você.</li>
<li>Proposta válida por 15 dias.</li></ul></div>
<div class="box"><h4>Não incluso</h4><ul>
<li>Impressão e instalação da arte da porta (indicamos a gráfica).</li>
<li>Domínio próprio (.com.br), se desejar: cerca de R$ 40 por ano.</li>
<li>Ensaio fotográfico profissional.</li>
<li>Gestão mensal das redes e anúncios pagos.</li></ul></div>
</div>
<div class="box" style="margin-top:6mm"><h4>Para começar, só precisamos de</h4><ul>
<li>Lista de serviços com valores e duração.</li>
<li>Medidas da porta (largura e altura da área a adesivar).</li>
<li>10 a 20 fotos de antes e depois de que você mais gosta.</li></ul></div>
<div class="ok"><h4>Vamos começar?</h4><div class="opts">
<span>☐ Vitrine · landing page, bio, destaques, 6 posts e arte da porta · <b>R$ 500</b></span>
<span>☐ Vitrine + Conteúdo · <b>R$ 700</b></span>
<span>☐ Presença Completa · <b>R$ 1.100</b></span>
<span>☐ Avulso: _______________________________</span></div>
<div class="sg"><div>Débora Brasil · assinatura e data</div><div>{PROV} · assinatura e data</div></div></div>''')

open('proposta_debora.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Proposta · Débora Brasil Beauty</title>{CSS}</head>'
    f'<body>{cover}{p2}{p3}{p4}{p5}</body></html>')
