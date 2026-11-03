from common import *

DOC = 'RECEITA DE PRODUÇÃO · PIZZA PORTUGUESA'
FOOT = 'Speciale Pizzas Artesanais · Receita de produção (operacional) · Versão 1.0'
T = 3

extra = '''<style>
.op{font-size:10pt}
.op h1{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:30pt;line-height:1;text-transform:uppercase}
.op h1 span{color:var(--red)}
.op .lead{color:var(--muted);font-size:9.5pt;margin-top:2mm}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;margin-top:5mm}
.cards div{background:var(--cream);border-top:3px solid var(--red);border-radius:4px;padding:3mm}
.cards b{font-family:'Roboto Condensed',sans-serif;font-size:17pt;display:block;line-height:1.1;color:var(--red)}
.cards small{font-size:7.6pt;color:var(--muted)}
.op table td{font-size:10pt;padding:6px 8px}
.op table th{font-size:8.6pt}
.big td.n{font-weight:600}
.tool{display:flex;flex-wrap:wrap;gap:2.5mm}
.tool span{border:1.5px solid var(--red);border-radius:20px;padding:3px 11px;font-size:8.6pt;font-weight:500}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:4mm 5mm}
.c{border:1px solid var(--cream-ln);border-radius:6px;overflow:hidden;display:flex;flex-direction:column}
.c .im{height:39mm;position:relative}
.c .im img{width:100%;height:100%;object-fit:cover;display:block}
.c .im .lb{position:absolute;right:6px;top:6px;background:var(--ink);color:#fff;font-weight:700;font-size:6.6pt;padding:2px 6px;border-radius:3px}
.c .noim{height:39mm;background:var(--cream);display:flex;align-items:center;justify-content:center;flex-direction:column;color:var(--red)}
.c .noim b{font-family:'Roboto Condensed',sans-serif;font-size:26pt;line-height:1}
.c .noim small{font-size:7.6pt;color:var(--muted)}
.c .tx{padding:2.5mm 3.5mm;display:grid;grid-template-columns:9mm 1fr;gap:1mm}
.c .tx .i{font-family:'Roboto Condensed',sans-serif;font-weight:800;color:var(--red);font-size:17pt;line-height:1}
.c .tx h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:10.5pt;line-height:1.1}
.c .tx p{font-size:8.2pt;line-height:1.4;margin-top:.5mm}
ul.chk-l.lg li{font-size:10pt;padding:4px 0 4px 20px}
ul.chk-l.lg li:before{top:8px;width:11px;height:11px}
.warn{background:var(--red);color:#fff;border-radius:6px;padding:4mm 5mm;margin-top:5mm;font-size:9.6pt}
.warn b{font-family:'Roboto Condensed',sans-serif;font-size:11.5pt;text-transform:uppercase;display:block;margin-bottom:1mm}
</style>'''

dot = lambda c: f'<span class="dot-size" style="background:{c}"></span>'
p1 = '<div class="op">' + '''<h1>Pizza <span>Portuguesa</span></h1>
<p class="lead">Versão simplificada para a bancada. Detalhes, PCCs e controle de qualidade estão na ficha técnica completa.</p>
<div class="cards"><div><b>340–380 °C</b><small>ponto do forno a lenha</small></div><div><b>3 a 4 min</b><small>tempo de forno</small></div>
<div><b>150 ml</b><small>de molho na Grande (colher funda)</small></div><div><b>8 fatias</b><small>Grande · Média 5 · Broto 4</small></div></div>''' \
    + sec('1', 'Separe antes de começar') + '<div class="big">' + table(
        ['Ingrediente', dot('#d7141a') + 'Grande', dot('#f2b705') + 'Média (est.)', dot('#3aa63a') + 'Broto (est.)'], [
            ['Massa (bolinha)', '320 g', '≈200 g', '≈160 g'],
            ['Molho de tomate', '150 ml', '≈95 ml', '≈75 ml'],
            ['Muçarela ralada', '280 g', '≈175 g', '≈140 g'],
            ['Presunto fatiado', '70 g', '≈45 g', '≈35 g'],
            ['Ovo cozido (rodelas)', '2 un', '1 un', '1 un'],
            ['Cebola', '100 g', '≈60 g', '≈50 g'],
            ['Azeitona preta (pedaços)', '9 g', '≈6 g', '≈5 g'],
            ['Orégano', 'a olho', 'a olho', 'a olho'],
        ], num_cols=(1, 2, 3), widths=['37%', '21%', '21%', '21%']) + '</div>' \
    + f'<p class="note">Média e Broto são estimativas {EST} e ainda serão testadas. Na dúvida, pese. Corte e etapa da cebola: {AC}.</p>' \
    + sec('2', 'Tenha à mão') + '<div class="tool">' + ''.join(f'<span>{x}</span>' for x in [
        'Bancada higienizada', 'Cortador de pizza', 'Colher funda', 'Balança', 'Pá de pizza', 'Caixa']) + '</div>' \
    + sec('3', 'Antes de montar') + '<ul class="chk-l lg">' + ''.join(f'<li>{x}</li>' for x in [
        'Mãos lavadas, bancada e utensílios limpos.',
        'Ingredientes porcionados e na geladeira até a hora de usar.',
        'Etiquetas conferidas: usar primeiro o que vence primeiro.',
        'Forno a lenha no ponto (340 a 380 °C).']) + '</ul></div>'

cards = [
    (1, 'Abrir e aparar', 'Abra a bolinha na mesa enfarinhada. Apare a borda com o cortador até o tamanho da pizza.', 1),
    (2, 'Conferir o tamanho', 'Massa redonda e com espessura igual. Grande ≈35 cm, Média ≈28 cm, Broto ≈25 cm (est.).', 2),
    (3, 'Molho', '150 ml (colher funda) espalhados por toda a massa. Deixe só a borda livre.', None),
    (4, 'Muçarela', 'Distribua os 280 g de muçarela ralada por igual sobre o molho.', 3),
    (5, 'Presunto e ovo', 'Presunto (70 g) em tiras, partindo do centro. Rodelas de 2 ovos cozidos entre as tiras.', None),
    (6, 'Cebola, azeitona e orégano', 'Cebola (100 g)*, azeitona preta em pedaços (9 g) e orégano a olho por cima. *Etapa e corte da cebola a confirmar.', 4),
    (7, 'Forno', '3 a 4 min a 340–380 °C. Gire com a pá. Tire quando a muçarela derreter e a borda dourar.', 5),
    (8, 'Cortar e embalar', 'Corte em 8 fatias (Grande), 5 (Média) ou 4 (Broto). Embale na caixa na hora.', 6),
]


def card(i, t, d, f):
    top = (f'<div class="im"><img src="img/port-foto{ {5:6,6:5}.get(f,f) }.jpg"><span class="lb">FOTO {f}</span></div>' if f
           else (lambda b, sm: f'<div class="noim"><b>{b}</b><small>{sm}</small></div>')(*{3: ('150 ml', 'colher funda · Grande'), 5: ('70 g · 2 ovos', 'presunto · ovo cozido · Grande')}[i]))
    return f'<div class="c">{top}<div class="tx"><span class="i">{i}</span><div><h4>{t}</h4><p>{d}</p></div></div></div>'


# ordem do grid: 1,2 / 3,4 / 5,6 / 7,8
p2 = '<div class="op">' + sec('4', 'Passo a passo') + '<div class="grid">' + ''.join(card(*c) for c in cards) + '</div></div>'

p3 = '<div class="op">' + sec('5', 'Confira antes de sair') + '<ul class="chk-l lg">' + ''.join(f'<li>{x}</li>' for x in [
    'Porções certas para o tamanho pedido.',
    'Molho por toda a massa, sem encharcar.',
    'Muçarela derretida e borda dourada, sem centro cru.',
    'Ingredientes bem distribuídos e orégano sem queimar.',
    'Número de fatias certo para o tamanho.']) + '</ul>' + sec('6', 'Se der errado') + table(
    ['Problema', 'O que fazer'], [
        ['Centro cru ou mole', 'Não passe de 150 ml de molho nem das porções. Espere o forno voltar ao ponto.'],
        ['Pizza encharcada', 'Meça o molho com a colher funda. Escorra a cebola cortada.'],
        ['Borda queimada', 'Forno quente demais: afaste da brasa e confira o tempo.'],
        ['Borda pálida', 'Forno frio: espere voltar ao ponto antes de assar.'],
        ['Salgada demais', 'Pese o presunto (70 g) e a azeitona (9 g).'],
        ['Tamanho errado', 'Pese a bolinha e abra até o gabarito.'],
    ], widths=['32%', '68%']) + sec('7', 'Guardar') + table(['Ingrediente', 'Como guardar'], [
        ['Muçarela e presunto', 'Geladeira, em recipiente tampado. Prazo conforme rótulo.'],
        ['Ovo cozido', f'Geladeira, tampado e etiquetado. Prazo {AC}.'],
        ['Cebola cortada', f'Geladeira, tampada e etiquetada. Prazo {AC}.'],
        ['Azeitona e orégano', 'Azeitona tampada na geladeira depois de aberta. Orégano em pote fechado e seco.'],
    ], widths=['32%', '68%']) + \
    '<div class="warn"><b>Regra da casa</b>Tudo etiquetado com produto, data, validade e responsável. Usar primeiro o que vence primeiro.</div>' \
    + '<div class="sign" style="margin-top:12mm"><div>Pizzaiolo</div><div>Data</div><div>Visto do responsável</div></div></div>'

subs = ['Ingredientes e preparo', 'Passo a passo', 'Conferência e cuidados']
pages = [page(DOC, s, i + 1, T, FOOT, c) for i, (s, c) in enumerate(zip(subs, [p1, p2, p3]))]
open('receita_op_portuguesa.html', 'w').write(html('Speciale · Receita de Produção Pizza Portuguesa', pages).replace('</head>', extra + '</head>'))
