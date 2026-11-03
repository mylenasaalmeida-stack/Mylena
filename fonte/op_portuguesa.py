"""Receita de produção (operacional) · Pizza Portuguesa — layout do modelo do molho."""

CSS = '''<style>
@import url('fonts.css');
:root{--red:#d7141a;--orange:#f07f1e;--cream:#fdf4e7;--peach:#fde7dc;--ink:#231a18;--muted:#6b5f58;--line:#e8ddd1;--blue:#1f6fb5;--navy:#1b3a63}
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Poppins',sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always}
.page:last-child{page-break-after:auto}
.C{font-family:'Roboto Condensed','Arial Narrow',sans-serif;font-weight:800}
.hd{background:var(--red);color:#fff;padding:9mm 15mm 6mm;display:flex;justify-content:space-between;align-items:flex-end;position:relative}
.hd h1{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:29pt;line-height:.95;text-transform:uppercase}
.hd h1 span{display:block;color:#ffd2ae}
.hd .lg{text-align:right;line-height:1}
.hd .lg b{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:15pt;display:block}
.hd .lg i{font-style:normal;font-size:4.6pt;letter-spacing:2.6px;font-weight:600;display:block;margin-top:1px}
.hd .lg small{font-size:7.5pt;font-weight:600;display:block;margin-top:2.5mm}
.chk{height:12px;background:repeating-conic-gradient(var(--red) 0 25%,#fff 0 50%) 0 0/12px 12px}
.bot{position:absolute;left:0;right:0;bottom:0}
.ft{position:absolute;left:15mm;right:15mm;bottom:17px;display:flex;justify-content:space-between;font-size:6.6pt;color:var(--muted)}
.in{padding:6mm 15mm 0}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;margin-bottom:5mm}
.stats div{background:var(--cream);border-top:3px solid var(--red);border-radius:5px;text-align:center;padding:3mm 2mm}
.stats b{font-family:'Roboto Condensed',sans-serif;font-weight:800;color:var(--red);font-size:17pt;display:block;line-height:1.1}
.stats small{font-size:7.4pt}
.sec{display:flex;align-items:center;gap:3mm;margin:4mm 0 2.5mm}
.sec .n{background:var(--ink);color:#fff;width:8mm;height:8mm;border-radius:4px;display:flex;align-items:center;justify-content:center;font-family:'Roboto Condensed',sans-serif;font-weight:700;font-size:11pt}
.sec h2{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:16pt;text-transform:uppercase}
.ing{border-top:1.5px solid var(--line)}
.ing .r{display:grid;grid-template-columns:10mm 1fr auto;align-items:center;border-bottom:1.5px solid var(--line);padding:2mm 2mm 2mm 3mm;min-height:10.5mm}
.ing .bx{width:5.5mm;height:5.5mm;border:1.6px solid var(--ink);border-radius:3px}
.ing .t{font-size:10.5pt}
.ing .t small{display:block;font-size:7.3pt;color:var(--muted);margin-top:-.5mm}
.ing .q{font-family:'Roboto Condensed',sans-serif;font-weight:800;color:var(--red);font-size:15pt;text-align:right}
.ing .q.o{color:var(--orange);font-size:12pt}
table{width:100%;border-collapse:collapse;font-size:8.6pt}
th{background:var(--ink);color:#fff;font-family:'Roboto Condensed',sans-serif;font-weight:700;text-transform:uppercase;font-size:7.6pt;padding:5px 7px;text-align:right}
th:first-child,td:first-child{text-align:left}
td{padding:4px 7px;border-bottom:1px solid var(--line);text-align:right}
tbody tr:nth-child(even) td{background:var(--cream)}
.dt{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px}
.note{font-size:7.2pt;color:var(--muted);margin-top:1.5mm}
.est{color:var(--orange);font-weight:700}
.dark{background:var(--ink);color:#fff;border-radius:6px;padding:4mm 5mm;margin-top:4mm}
.dark h3{font-family:'Roboto Condensed',sans-serif;font-weight:800;color:#ffb56b;font-size:11pt;text-transform:uppercase;margin-bottom:2mm}
.dark ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:1.2mm 6mm;font-size:8.4pt}
.dark li:before{content:'';display:inline-block;width:3.2mm;height:3.2mm;border:1.4px solid #fff;border-radius:2px;margin-right:2mm;vertical-align:-.6mm}
.blk{display:grid;grid-template-columns:1fr 60mm;gap:6mm;padding-bottom:3.5mm;margin-bottom:3.5mm;border-bottom:1.5px dashed #efd9c5}
.blk:last-child{border-bottom:0}
.bh{display:flex;align-items:center;gap:2.5mm;margin-bottom:2mm}
.bh .l{background:var(--red);color:#fff;width:7mm;height:7mm;border-radius:3px;display:flex;align-items:center;justify-content:center;font-family:'Roboto Condensed',sans-serif;font-weight:700;font-size:10pt}
.bh h3{font-family:'Roboto Condensed',sans-serif;font-weight:800;color:var(--red);font-size:13pt;text-transform:uppercase}
.st{display:grid;grid-template-columns:8.5mm 1fr;align-items:start;margin:1.4mm 0;font-size:9.4pt;line-height:1.42}
.st .c{width:6.6mm;height:6.6mm;border:1.4px solid var(--red);border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--red);font-family:'Roboto Condensed',sans-serif;font-weight:700;font-size:9pt;background:#fff8f3}
.al{background:var(--peach);border-left:3px solid var(--orange);border-radius:0 5px 5px 0;padding:2mm 3mm;font-size:8pt;margin-top:2mm}
.al b{color:var(--red)}
.ph{display:flex;flex-direction:column;gap:2.5mm}
.pic{position:relative;border-radius:6px;overflow:hidden;height:43mm}
.pic.s{height:30mm}
.pic img{width:100%;height:100%;object-fit:cover;display:block}
.pic span{position:absolute;left:0;right:0;bottom:0;background:rgba(35,26,24,.82);color:#fff;font-size:6.8pt;font-weight:600;padding:1.4mm 2.5mm}
.pic em{position:absolute;right:2mm;top:2mm;background:var(--red);color:#fff;font-style:normal;font-size:6pt;font-weight:700;padding:1px 5px;border-radius:3px}
.vcards{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.vc{border-radius:6px;color:#fff;padding:4mm}
.vc h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:10.5pt;text-transform:uppercase}
.vc b{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:19pt;display:block;line-height:1.1;margin:1mm 0}
.vc p{font-size:7.6pt;line-height:1.4}
.two{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:4mm}
.two>div{border-radius:6px;padding:4mm 5mm}
.two h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:11pt;text-transform:uppercase;margin-bottom:1.5mm}
.two ul{padding-left:4mm;font-size:8.4pt;line-height:1.65}
.fs{background:var(--cream)}.fs h4{color:var(--red)}
.jf{background:var(--ink);color:#fff}.jf h4{color:#ffb56b}
.bar{background:var(--peach);border-left:3px solid var(--orange);padding:2mm 3mm;font-size:8pt;margin-top:4mm;border-radius:0 5px 5px 0}
.bar b{color:var(--red)}
.et{border:1.6px dashed var(--ink);border-radius:6px;margin-top:4mm;padding:4mm 5mm;display:grid;grid-template-columns:32mm 1fr 1fr;gap:1.6mm 5mm;font-size:8pt;align-items:center}
.et .tt{grid-row:span 3;font-family:'Roboto Condensed',sans-serif;font-weight:800;color:var(--red);font-size:12pt;text-transform:uppercase;line-height:1.05}
.ln{display:inline-block;border-bottom:1px solid var(--ink);width:28mm;height:3mm}
.tbc{color:var(--orange);font-weight:700}
</style>'''


def header(t1, t2, pg):
    t = f'{t1}<span>{t2}</span>' if t2 else t1
    return (f'<div class="hd"><h1>{t}</h1><div class="lg"><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i>'
            f'<small>Página {pg} de 3</small></div></div><div class="chk"></div>')


def foot(right):
    return f'<div class="ft"><span>Ficha de produção · Pizza Portuguesa</span><span>{right}</span></div><div class="chk bot"></div>'


def sec(n, t): return f'<div class="sec"><span class="n">{n}</span><h2>{t}</h2></div>'
def st(n, t): return f'<div class="st"><span class="c">{n}</span><div>{t}</div></div>'


def pic(f, cap, s=False):
    real = {5: 6, 6: 5}.get(f, f)  # foto 5 = close da pizza assada; foto 6 = pizza na caixa
    return f'<div class="pic{" s" if s else ""}"><img src="img/port-foto{real}.jpg"><em>FOTO {f}</em><span>{cap}</span></div>'


def blk(letter, title, body, photos):
    return (f'<div class="blk"><div><div class="bh"><span class="l">{letter}</span><h3>{title}</h3></div>{body}</div>'
            f'<div class="ph">{photos}</div></div>')


ings = [
    ('Massa de pizza (bolinha)', 'aberta na hora', '320 g'),
    ('Molho de tomate', 'colher funda (padrão)', '150 ml'),
    ('Muçarela', 'ralada', '280 g'),
    ('Presunto', 'fatiado, em tiras', '70 g'),
    ('Ovo cozido', 'em rodelas', '2 un'),
    ('Cebola', 'corte a confirmar', '100 g'),
    ('Azeitona preta', 'em pedaços', '9 g'),
    ('Orégano', 'por cima, antes do forno', 'a olho'),
]
rows = ''.join(f'<div class="r"><span class="bx"></span><div class="t">{a}<small>{b}</small></div>'
               f'<div class="q{" o" if q == "a olho" else ""}">{q}</div></div>' for a, b, q in ings)

dot = lambda c: f'<span class="dt" style="background:{c}"></span>'
sizes = '''<table><thead><tr><th>Tamanho</th><th>Fatias</th><th>Bolinha</th><th>Molho</th><th>Muçarela</th><th>Presunto</th><th>Cebola</th><th>Ovo</th><th>Azeitona</th></tr></thead><tbody>''' + ''.join(
    f'<tr><td>{d}{t}</td>' + ''.join(f'<td>{x}</td>' for x in v) + '</tr>' for d, t, v in [
        (dot('#d7141a'), '<b>Grande</b>', ['8', '320 g', '150 ml', '280 g', '70 g', '100 g', '2 un', '9 g']),
        (dot('#f2b705'), 'Média <span class="est">(est.)</span>', ['5', '≈200 g', '≈95 ml', '≈175 g', '≈45 g', '≈60 g', '1 un', '≈6 g']),
        (dot('#3aa63a'), 'Broto <span class="est">(est.)</span>', ['4', '≈160 g', '≈75 ml', '≈140 g', '≈35 g', '≈50 g', '1 un', '≈5 g']),
    ]) + '</tbody></table>'

p1 = f'''<section class="page">{header('Pizza Portuguesa', 'Receita da produção', 1)}<div class="in">
<div class="stats"><div><b>320 g</b><small>bolinha da Grande</small></div><div><b>150 ml</b><small>de molho por pizza</small></div>
<div><b>280 g</b><small>de muçarela ralada</small></div><div><b>3 a 4 min</b><small>forno a 340–380 °C</small></div></div>
{sec(1, 'Separe os ingredientes')}<p class="note" style="margin:-1mm 0 2mm">Quantidades para 1 pizza Grande (8 fatias).</p><div class="ing">{rows}</div>
{sec(2, 'Por tamanho')}{sizes}
<p class="note">Média e Broto são estimativas <span class="est">(est.)</span>, em teste. Etiqueta da bolinha: vermelha (Grande), amarela (Média), verde (Broto). Na dúvida, pese.</p>
<div class="dark"><h3>Antes de começar</h3><ul>
<li>Mãos lavadas, touca e avental</li><li>Ingredientes porcionados e na geladeira</li>
<li>Bancada limpa e salpicada de farinha</li><li>Cortador de pizza e colher funda</li>
<li>Balança conferida</li><li>Pá de pizza e caixas</li>
<li>Forno a lenha no ponto (340–380 °C)</li><li>Etiquetas conferidas (vence primeiro, usa primeiro)</li></ul></div>
</div>{foot('Grande: 8 fatias · Média: 5 · Broto: 4')}</section>'''

A = blk('A', 'Abrir e aparar',
        st(1, 'Pegue <b>1 bolinha</b> (Grande: <b>320 g</b>) e abra na <b>mesa enfarinhada</b>.')
        + st(2, '<b>Apare a borda com o cortador</b> até o tamanho da pizza. Massa redonda e com espessura igual.')
        + '<div class="al"><b>Tamanho:</b> Grande ≈35 cm · Média ≈28 cm · Broto ≈25 cm <span class="est">(est.)</span>.</div>',
        pic(1, 'Borda aparada com o cortador', True) + pic(2, 'Massas abertas, redondas e iguais', True))
B = blk('B', 'Molho e muçarela',
        st(3, 'Coloque <b>150 ml de molho</b> com a <b>colher funda</b> e espalhe por toda a massa. Deixe só a borda livre.')
        + st(4, 'Distribua os <b>280 g de muçarela ralada</b> por igual sobre o molho.')
        + '<div class="al"><b>Não passe de 150 ml.</b> Molho demais deixa o centro mole e a pizza encharcada.</div>',
        pic(3, 'Ponto: muçarela por igual, borda livre'))
C = blk('C', 'Cobertura',
        st(5, 'Disponha o <b>presunto (70 g)</b> em tiras, <b>partindo do centro</b>.')
        + st(6, 'Coloque <b>2 ovos cozidos em rodelas</b> entre as tiras.')
        + st(7, 'Distribua a <b>cebola (100 g)</b>.')
        + st(8, 'Espalhe a <b>azeitona preta em pedaços (9 g)</b> e finalize com <b>orégano a olho</b> por cima.')
        + '<div class="al"><b>Atenção:</b> a etapa e o corte da cebola ainda estão <span class="tbc">a confirmar</span> com a equipe.</div>',
        pic(4, 'Pronta para o forno'))
D = blk('D', 'Assar',
        st(9, 'Leve ao <b>forno a lenha</b> com a pá, a <b>340–380 °C</b>, por <b>3 a 4 minutos</b>. Gire para assar por igual.')
        + st(10, 'Tire quando a <b>muçarela derreter</b> e a <b>borda dourar</b>, sem centro cru.')
        + '<div class="al"><b>Borda escura?</b> Forno quente demais. <b>Borda pálida?</b> Espere o forno voltar ao ponto.</div>',
        pic(5, 'Ponto: muçarela derretida e dourada'))

p2 = f'''<section class="page">{header('Modo de montagem', '', 2)}<div class="in" style="padding-top:5mm">{A}{B}{C}{D}</div>{foot('Dúvida no ponto? Compare com a foto.')}</section>'''

E = blk('E', 'Cortar e embalar',
        st(11, 'Corte em <b>8 fatias</b> (Grande), <b>5</b> (Média) ou <b>4</b> (Broto).')
        + st(12, 'Coloque na <b>caixa</b> e feche na hora. Confira o tamanho do pedido antes de entregar.')
        + '<div class="al"><b>Confira:</b> porções certas, ingredientes bem distribuídos, orégano sem queimar.</div>',
        pic(6, 'Pronta na caixa'))

p3 = f'''<section class="page">{header('Servir e guardar', '', 3)}<div class="in" style="padding-top:5mm">{E}
{sec('!', 'Validade dos ingredientes')}
<div class="vcards">
<div class="vc" style="background:var(--blue)"><h4>Muçarela e presunto</h4><b>Rótulo</b><p>Geladeira, na embalagem ou em pote tampado.</p></div>
<div class="vc" style="background:var(--navy)"><h4>Ovo cozido</h4><b>A confirmar</b><p>Geladeira, pote tampado e etiquetado.</p></div>
<div class="vc" style="background:var(--navy)"><h4>Cebola cortada</h4><b>A confirmar</b><p>Geladeira, pote tampado e etiquetado.</p></div>
</div>
<div class="two">
<div class="fs"><h4>Faça sempre</h4><ul><li>Use primeiro o que vence primeiro.</li><li>Pese as porções: 280 g, 70 g, 100 g, 9 g.</li><li>Molho sempre com a colher funda: 150 ml.</li><li>Feche os potes logo depois de usar.</li><li>Etiquete todo pote aberto ou porcionado.</li></ul></div>
<div class="jf"><h4>Jogue fora se</h4><ul><li>Passou da validade da etiqueta.</li><li>Cheiro azedo ou cor estranha.</li><li>Presunto pegajoso ou com limo.</li><li>Mofo na muçarela ou na azeitona.</li><li>Ficou fora da geladeira por muito tempo.</li></ul></div>
</div>
<div class="bar"><b>Nunca</b> deixe ovo, presunto ou muçarela na bancada fora do uso. Volte para a geladeira assim que terminar.</div>
<div class="et"><div class="tt">Modelo de<br>etiqueta</div>
<div>Produto: <span class="ln"></span></div><div>Lote: <span class="ln"></span></div>
<div>Preparo: <span class="ln"></span></div><div>Validade: <span class="ln"></span></div>
<div>Responsável: <span class="ln" style="width:24mm"></span></div><div>☐ Geladeira</div></div>
</div>{foot('Boas Práticas · RDC ANVISA 216/2004')}</section>'''

open('receita_op_portuguesa.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Speciale · Receita de Produção Pizza Portuguesa</title>{CSS}</head><body>{p1}{p2}{p3}</body></html>')
