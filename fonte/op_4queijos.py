"""Receita de produção (operacional) · Pizza 4 Queijos — mesmo layout do modelo do molho."""
from op_portuguesa import CSS, sec, st, blk

NOME = 'Pizza 4 Queijos'
EXTRA = '''<style>.tip{background:var(--cream);border-radius:6px;height:100%;min-height:36mm;display:flex;align-items:center;justify-content:center;text-align:center;padding:4mm;
font-family:'Roboto Condensed',sans-serif;font-weight:800;color:var(--red);font-size:12.5pt;line-height:1.25;text-transform:uppercase}
.pic.t{height:58mm}</style>'''


def header(t1, t2, pg):
    t = f'{t1}<span>{t2}</span>' if t2 else t1
    return (f'<div class="hd"><h1>{t}</h1><div class="lg"><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i>'
            f'<small>Página {pg} de 3</small></div></div><div class="chk"></div>')


def foot(right):
    return f'<div class="ft"><span>Ficha de produção · {NOME}</span><span>{right}</span></div><div class="chk bot"></div>'


def pic(f, cap, cls=''):
    return f'<div class="pic {cls}"><img src="img/q4-foto{f}.jpg"><em>FOTO {f}</em><span>{cap}</span></div>'


def tip(t): return f'<div class="tip">{t}</div>'


ings = [
    ('Massa de pizza (bolinha)', 'aberta na hora', '320 g'),
    ('Molho de tomate', 'colher funda (padrão)', '150 ml'),
    ('Muçarela', 'por toda a massa', '280 g'),
    ('Gorgonzola', 'picado · peso a confirmar', '24 g'),
    ('Provolone', 'picado · ralado ou pedaços a confirmar', '150 g'),
    ('Catupiry', 'em listras · nº de listras a confirmar', '4 listras'),
    ('Orégano', 'por cima, antes do forno', 'a olho'),
]
rows = ''.join(f'<div class="r"><span class="bx"></span><div class="t">{a}<small>{b}</small></div>'
               f'<div class="q{" o" if q == "a olho" else ""}">{q}</div></div>' for a, b, q in ings)
dot = lambda c: f'<span class="dt" style="background:{c}"></span>'
sizes = '<table><thead><tr><th>Tamanho</th><th>Fatias</th><th>Bolinha</th><th>Molho</th><th>Muçarela</th><th>Gorgonzola</th><th>Provolone</th><th>Catupiry</th></tr></thead><tbody>' + ''.join(
    f'<tr><td>{d}{t}</td>' + ''.join(f'<td>{x}</td>' for x in v) + '</tr>' for d, t, v in [
        (dot('#d7141a'), '<b>Grande</b>', ['8', '320 g', '150 ml', '280 g', '24 g', '150 g', '4 listras']),
        (dot('#f2b705'), 'Média <span class="est">(est.)</span>', ['5', '≈200 g', '≈95 ml', '≈175 g', '≈15 g', '≈95 g', '≈3 listras']),
        (dot('#3aa63a'), 'Broto <span class="est">(est.)</span>', ['4', '≈160 g', '≈75 ml', '≈140 g', '≈12 g', '≈75 g', '≈2 listras']),
    ]) + '</tbody></table>'

p1 = f'''<section class="page">{header(NOME, 'Receita da produção', 1)}<div class="in">
<div class="stats"><div><b>320 g</b><small>bolinha da Grande</small></div><div><b>150 ml</b><small>de molho por pizza</small></div>
<div><b>280 g</b><small>de muçarela</small></div><div><b>3 a 4 min</b><small>forno a 340–380 °C</small></div></div>
{sec(1, 'Separe os ingredientes')}<p class="note" style="margin:-1mm 0 2mm">Quantidades para 1 pizza Grande (8 fatias).</p><div class="ing">{rows}</div>
{sec(2, 'Por tamanho')}{sizes}
<p class="note">Média e Broto são estimativas <span class="est">(est.)</span>, em teste. Etiqueta da bolinha: vermelha (Grande), amarela (Média), verde (Broto). Na dúvida, pese.</p>
<div class="dark"><h3>Antes de começar</h3><ul>
<li>Mãos lavadas, touca e avental</li><li>Queijos picados, porcionados e na geladeira</li>
<li>Bancada limpa e salpicada de farinha</li><li>Cortador de pizza e colher funda</li>
<li>Balança conferida</li><li>Bisnaga ou colher do catupiry</li>
<li>Forno a lenha no ponto (340–380 °C)</li><li>Pá de pizza e caixas</li></ul></div>
</div>{foot('Grande: 8 fatias · Média: 5 · Broto: 4')}</section>'''

A = blk('A', 'Abrir e aparar',
        st(1, 'Pegue <b>1 bolinha</b> (Grande: <b>320 g</b>) e abra na <b>mesa enfarinhada</b>.')
        + st(2, '<b>Apare o excesso da borda com o cortador</b>, deixando a massa redonda e uniforme.')
        + '<div class="al"><b>Tamanho:</b> Grande ≈35 cm · Média ≈28 cm · Broto ≈25 cm <span class="est">(est.)</span>.</div>',
        pic(1, 'Borda aparada com o cortador'))
B = blk('B', 'Molho e queijos',
        st(3, 'Coloque <b>150 ml de molho</b> com a <b>colher funda</b> e espalhe por toda a massa.')
        + st(4, 'Espalhe os <b>280 g de muçarela</b> por igual sobre o molho.')
        + st(5, 'Distribua o <b>gorgonzola (24 g)</b> e o <b>provolone (150 g)</b>, picados, por cima da muçarela.')
        + '<div class="al"><b>Pese os queijos.</b> Gorgonzola demais domina o sabor; queijo demais deixa a pizza oleosa.</div>',
        tip('Gorgonzola em pedaços pequenos e espalhados por toda a pizza'))
C = blk('C', 'Catupiry e orégano',
        st(6, 'Aplique o <b>catupiry em 4 listras</b> por cima dos queijos.')
        + st(7, 'Finalize com <b>orégano a olho</b> por cima de tudo.')
        + '<div class="al"><b>Atenção:</b> o número de listras ainda está <span class="tbc">a confirmar</span>. A foto mostra cerca de 6 listras mais curtas.</div>',
        pic(2, 'Pronta para o forno', 't'))
D = blk('D', 'Assar',
        st(8, 'Leve ao <b>forno a lenha</b> com a pá, a <b>340–380 °C</b>, por <b>3 a 4 minutos</b>. Gire para assar por igual.')
        + st(9, 'Tire quando os <b>queijos derreterem</b> e a <b>borda dourar</b>, sem centro cru.')
        + '<div class="al"><b>Catupiry queimado?</b> Listra grossa demais ou forno muito quente. <b>Borda pálida?</b> Espere o forno voltar ao ponto.</div>',
        tip('Ponto: queijos derretidos, catupiry levemente dourado, borda assada'))

p2 = f'''<section class="page">{header('Modo de montagem', '', 2)}<div class="in" style="padding-top:5mm">{A}{B}{C}{D}</div>{foot('Dúvida no ponto? Compare com a foto.')}</section>'''

E = blk('E', 'Cortar e embalar',
        st(10, 'Corte em <b>8 fatias</b> (Grande), <b>5</b> (Média) ou <b>4</b> (Broto).')
        + st(11, 'Coloque na <b>caixa</b> e feche na hora. Confira o tamanho do pedido antes de entregar.')
        + '<div class="al"><b>Confira:</b> queijos derretidos e bem distribuídos, listras visíveis, orégano sem queimar.</div>',
        pic(3, 'Pronta na caixa'))

p3 = f'''<section class="page">{header('Servir e guardar', '', 3)}<div class="in" style="padding-top:5mm">{E}
{sec('!', 'Validade dos ingredientes')}
<div class="vcards">
<div class="vc" style="background:var(--blue)"><h4>Muçarela e provolone</h4><b>Rótulo</b><p>Geladeira, na embalagem ou em pote tampado.</p></div>
<div class="vc" style="background:var(--blue)"><h4>Gorgonzola e catupiry</h4><b>Rótulo</b><p>Geladeira. Gorgonzola bem embalado; catupiry com a data de abertura.</p></div>
<div class="vc" style="background:var(--navy)"><h4>Queijos picados</h4><b>A confirmar</b><p>Geladeira, pote tampado e etiquetado.</p></div>
</div>
<div class="two">
<div class="fs"><h4>Faça sempre</h4><ul><li>Use primeiro o que vence primeiro.</li><li>Pese os queijos: 280 g, 24 g, 150 g.</li><li>Molho sempre com a colher funda: 150 ml.</li><li>Guarde o gorgonzola separado, para não passar cheiro.</li><li>Etiquete todo pote aberto ou porcionado.</li></ul></div>
<div class="jf"><h4>Jogue fora se</h4><ul><li>Passou da validade da etiqueta.</li><li>Cheiro azedo ou cor estranha.</li><li>Mofo diferente do normal do gorgonzola.</li><li>Catupiry com água separada ou azedo.</li><li>Ficou fora da geladeira por muito tempo.</li></ul></div>
</div>
<div class="bar"><b>Nunca</b> deixe os queijos na bancada fora do uso. Volte para a geladeira assim que terminar.</div>
<div class="et"><div class="tt">Modelo de<br>etiqueta</div>
<div>Produto: <span class="ln"></span></div><div>Lote: <span class="ln"></span></div>
<div>Preparo: <span class="ln"></span></div><div>Validade: <span class="ln"></span></div>
<div>Responsável: <span class="ln" style="width:24mm"></span></div><div>☐ Geladeira</div></div>
</div>{foot('Boas Práticas · RDC ANVISA 216/2004')}</section>'''

open('receita_op_4queijos.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Speciale · Receita de Produção Pizza 4 Queijos</title>{CSS}{EXTRA}</head><body>{p1}{p2}{p3}</body></html>')
