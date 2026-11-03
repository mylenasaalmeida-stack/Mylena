"""Receita de produção (operacional) · Pizza Frango com Catupiry — layout do modelo do molho."""
from op_portuguesa import CSS, sec, st, blk
from op_4queijos import EXTRA, tip

NOME = 'Pizza Frango com Catupiry'
P = 'quantidade de listras de catupiry a confirmar com a equipe'


def header(t1, t2, pg):
    t = f'{t1}<span>{t2}</span>' if t2 else t1
    return (f'<div class="hd"><h1>{t}</h1><div class="lg"><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i>'
            f'<small>Página {pg} de 3</small></div></div><div class="chk"></div>')


def foot(right):
    return f'<div class="ft"><span>Ficha de produção · {NOME}</span><span>{right}</span></div><div class="chk bot"></div>'


ings = [
    ('Massa de pizza (bolinha)', 'aberta na hora', '320 g'),
    ('Molho de tomate', 'colher funda (padrão)', '150 ml'),
    ('Muçarela', 'por toda a massa', '280 g'),
    ('Frango', 'pré-preparado e porcionado', '140 g'),
    ('Catupiry', f'em listras · {P}', 'a confirmar'),
    ('Azeitona preta', 'em pedaços, espalhada por cima', '≈9 g'),
    ('Orégano', 'polvilhado, antes do forno', 'a olho'),
]
rows = ''.join(f'<div class="r"><span class="bx"></span><div class="t">{a}<small>{b}</small></div>'
               f'<div class="q{" o" if q in ("a olho", "a confirmar") else ""}">{q}</div></div>' for a, b, q in ings)
dot = lambda c: f'<span class="dt" style="background:{c}"></span>'
sizes = '<table><thead><tr><th>Tamanho</th><th>Fatias</th><th>Bolinha</th><th>Molho</th><th>Muçarela</th><th>Frango</th><th>Azeitona</th><th>Catupiry</th></tr></thead><tbody>' + ''.join(
    f'<tr><td>{d}{t}</td>' + ''.join(f'<td>{x}</td>' for x in v) + '</tr>' for d, t, v in [
        (dot('#d7141a'), '<b>Grande</b>', ['8', '320 g', '150 ml', '280 g', '140 g', '≈9 g', 'a confirmar']),
        (dot('#f2b705'), 'Média <span class="est">(est.)</span>', ['5', '≈200 g', '≈95 ml', '≈175 g', '≈88 g', '≈6 g', 'a confirmar']),
        (dot('#3aa63a'), 'Broto <span class="est">(est.)</span>', ['4', '≈160 g', '≈75 ml', '≈140 g', '≈70 g', '≈5 g', 'a confirmar']),
    ]) + '</tbody></table>'

p1 = f'''<section class="page">{header('Frango com Catupiry', 'Receita da produção', 1)}<div class="in">
<div class="stats"><div><b>320 g</b><small>bolinha da Grande</small></div><div><b>150 ml</b><small>de molho por pizza</small></div>
<div><b>140 g</b><small>de frango</small></div><div><b>3 a 4 min</b><small>forno a 340–380 °C</small></div></div>
{sec(1, 'Separe os ingredientes')}<p class="note" style="margin:-1mm 0 2mm">Quantidades para 1 pizza Grande (8 fatias).</p><div class="ing">{rows}</div>
{sec(2, 'Por tamanho')}{sizes}
<p class="note">Média e Broto são estimativas <span class="est">(est.)</span>, em teste. Etiqueta da bolinha: vermelha (Grande), amarela (Média), verde (Broto). Na dúvida, pese.</p>
<div class="dark"><h3>Antes de começar</h3><ul>
<li>Mãos lavadas, touca e avental</li><li>Frango e muçarela porcionados e na geladeira</li>
<li>Bancada limpa e salpicada de farinha</li><li>Cortador de pizza e colher funda</li>
<li>Balança conferida</li><li>Bisnaga ou colher do catupiry</li>
<li>Forno a lenha no ponto (340–380 °C)</li><li>Pá de pizza e caixas</li></ul></div>
</div>{foot('Grande: 8 fatias · Média: 5 · Broto: 4')}</section>'''

A = blk('A', 'Abrir e aparar',
        st(1, 'Pegue <b>1 bolinha</b> (Grande: <b>320 g</b>) e abra na <b>mesa enfarinhada</b>.')
        + st(2, '<b>Apare o excesso da borda com o cortador</b>, deixando a massa redonda e uniforme.')
        + '<div class="al"><b>Tamanho:</b> Grande ≈35 cm · Média ≈28 cm · Broto ≈25 cm <span class="est">(est.)</span>.</div>',
        tip('Massa redonda, espessura igual, borda aparada'))
B = blk('B', 'Molho, muçarela e frango',
        st(3, 'Coloque <b>150 ml de molho</b> com a <b>colher funda</b> e espalhe por toda a massa.')
        + st(4, 'Espalhe os <b>280 g de muçarela</b> por igual sobre o molho.')
        + st(5, '<b>Logo depois da muçarela</b>, distribua os <b>140 g de frango</b> por toda a pizza, até perto da borda.')
        + '<div class="al"><b>Frango sempre sobre a muçarela.</b> Assim ele não resseca no forno.</div>',
        tip('Frango espalhado por igual, sem montes no centro'))
C = blk('C', 'Catupiry, azeitona e orégano',
        st(6, 'Aplique o <b>catupiry em listras</b> por cima de tudo.')
        + st(7, 'Espalhe a <b>azeitona preta em pedaços (≈9 g)</b> e polvilhe <b>orégano a olho</b>.')
        + f'<div class="al"><b>Atenção:</b> <span class="tbc">{P}</span>.</div>',
        tip('Listras paralelas, de um lado ao outro da pizza'))
D = blk('D', 'Assar',
        st(8, 'Leve ao <b>forno a lenha</b> com a pá, a <b>340–380 °C</b>, por <b>3 a 4 minutos</b>. Gire para assar por igual.')
        + st(9, 'Tire quando a <b>muçarela derreter</b>, o <b>catupiry dourar levemente</b> e a <b>borda assar</b>.')
        + '<div class="al"><b>Frango ressecado?</b> Forno quente demais ou tempo longo. <b>Borda pálida?</b> Espere o forno voltar ao ponto.</div>',
        '<div class="pic t" style="height:62mm"><img src="img/frango-foto1.jpg" style="object-position:50% 45%"><em>FOTO 1</em><span>Ponto de saída (foto de uma Broto)</span></div>')

p2 = f'''<section class="page">{header('Modo de montagem', '', 2)}<div class="in" style="padding-top:5mm">{A}{B}{C}{D}</div>{foot('Dúvida no ponto? Compare com a foto.')}</section>'''

E = blk('E', 'Cortar e embalar',
        st(10, 'Corte em <b>8 fatias</b> (Grande), <b>5</b> (Média) ou <b>4</b> (Broto).')
        + st(11, 'Coloque na <b>caixa</b> e feche na hora. Confira o tamanho do pedido antes de entregar.')
        + '<div class="al"><b>Confira:</b> frango bem distribuído, listras visíveis, orégano sem queimar.</div>',
        tip('Porções certas para o tamanho do pedido'))

p3 = f'''<section class="page">{header('Servir e guardar', '', 3)}<div class="in" style="padding-top:5mm">{E}
{sec('!', 'Validade dos ingredientes')}
<div class="vcards">
<div class="vc" style="background:var(--navy)"><h4>Frango pré-preparado</h4><b>Ver ficha</b><p>Geladeira, porcionado e etiquetado. Validade conforme a ficha do frango.</p></div>
<div class="vc" style="background:var(--blue)"><h4>Muçarela e catupiry</h4><b>Rótulo</b><p>Geladeira. Catupiry com a data de abertura.</p></div>
<div class="vc" style="background:var(--blue)"><h4>Azeitona preta</h4><b>Rótulo</b><p>Tampada, na geladeira depois de aberta.</p></div>
</div>
<div class="two">
<div class="fs"><h4>Faça sempre</h4><ul><li>Use primeiro o que vence primeiro.</li><li>Pese: muçarela 280 g e frango 140 g.</li><li>Molho sempre com a colher funda: 150 ml.</li><li>Frango na geladeira até a hora de montar.</li><li>Etiquete todo pote aberto ou porcionado.</li></ul></div>
<div class="jf"><h4>Jogue fora se</h4><ul><li>Passou da validade da etiqueta.</li><li>Frango com cheiro azedo, pegajoso ou com cor estranha.</li><li>Catupiry com água separada ou azedo.</li><li>Mofo na muçarela ou na azeitona.</li><li>Ficou fora da geladeira por muito tempo.</li></ul></div>
</div>
<div class="bar"><b>Nunca</b> deixe o frango ou a muçarela na bancada fora do uso. Volte para a geladeira assim que terminar.</div>
<div class="et"><div class="tt">Modelo de<br>etiqueta</div>
<div>Produto: <span class="ln"></span></div><div>Lote: <span class="ln"></span></div>
<div>Preparo: <span class="ln"></span></div><div>Validade: <span class="ln"></span></div>
<div>Responsável: <span class="ln" style="width:24mm"></span></div><div>☐ Geladeira</div></div>
<div class="two" style="grid-template-columns:1fr"><div class="fs"><h4>Orientações finais</h4><ul>
<li><b>Ficha do frango:</b> ainda precisa ser feita. O frango é preparado antes e guardado; sem ficha não há padrão de tempero, validade nem lista de alérgenos dos temperos.</li>
<li><b>Média e Broto são estimativas</b> calculadas a partir da Grande. Meça e pese algumas pizzas reais e avise o responsável para ajustar.</li></ul></div></div>
</div>{foot('Boas Práticas · RDC ANVISA 216/2004')}</section>'''

open('receita_op_frango.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Speciale · Receita de Produção Pizza Frango com Catupiry</title>{CSS}{EXTRA}</head><body>{p1}{p2}{p3}</body></html>')
