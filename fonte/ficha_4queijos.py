from common import *

DOC = 'FICHA TÉCNICA · PIZZA 4 QUEIJOS'
FOOT = 'Speciale Pizzas Artesanais · Ficha técnica de montagem · Versão 1.1'
T = 7
VER = 'Versão 1.1 · Novembro/2026'

cover = f'''<section class="page cover"><div class="chk top"></div>
<div class="in">{logo()}
<div class="tag">Ficha técnica de montagem</div>
<h1>Pizza<span>4 Queijos</span></h1>
<p class="lead">Muçarela, gorgonzola, provolone e listras de catupiry sobre molho de tomate artesanal, finalizada com orégano e assada em forno a lenha.</p>
<div class="stats">
<div class="st"><b>280 g</b><small>de muçarela por pizza Grande</small></div>
<div class="st"><b>4 listras</b><small>de catupiry por cima dos queijos (a confirmar)</small></div>
<div class="st"><b>3 a 4 min</b><small>no forno a lenha, a 340 a 380 °C</small></div>
</div>
<div class="ver">{VER}</div>
</div><div class="chk bot"></div></section>'''

p2 = sec('01', 'Identificação geral') + table(['Campo', 'Informação'], [
    ['Nome do produto', 'Pizza 4 Queijos'],
    ['Código interno / SKU', '<span class="blank"></span>'],
    ['Categoria', 'Pizza salgada · montagem sobre a massa artesanal da casa'],
    ['Tamanho de referência', f'Grande · 8 fatias · bolinha de 320 g · ≈35 cm {EST} (Média e Broto na seção 07)'],
    ['Base', 'Massa de pizza artesanal (ficha própria) + molho de tomate artesanal (150 ml)'],
    ['Forno', 'A lenha · 340 a 380 °C (ponto ideal) · 3 a 4 min'],
    ['Alérgenos', 'CONTÉM GLÚTEN (trigo), LEITE (muçarela, gorgonzola, provolone e catupiry) e SOJA (óleo da massa).'],
    ['Responsável técnico', '<span class="blank" style="min-width:80mm"></span>'],
    ['Data de elaboração', 'Novembro de 2026 · versão 1.1'],
], widths=['31%', '69%']) + '''<p class="note"><b>Descrição:</b> pizza de quatro queijos montada em camadas sobre a massa aberta na hora: molho de tomate, muçarela, gorgonzola e provolone picados e listras de catupiry por cima, finalizada com orégano.</p>''' \
    + sec('02', 'Ingredientes por pizza') + table(['Ingrediente', 'Quantidade', 'Forma de uso', 'Função'], [
        ['Massa de pizza (bolinha)', '1 un · 320 g', 'Aberta na hora e aparada com o cortador', 'Base'],
        ['Molho de tomate artesanal', '150 ml', 'Colher funda (padrão), por toda a massa', 'Sabor e umidade'],
        ['Muçarela', '280 g', 'Por toda a massa, sobre o molho', 'Base de queijo'],
        ['Gorgonzola', f'24 g', f'Picado, sobre a muçarela · peso {AC}', 'Sabor forte'],
        ['Provolone', '150 g', f'Picado · ralado ou em pedaços {AC}', 'Sabor defumado'],
        ['Catupiry', '4 listras', f'Em listras por cima dos queijos · peso e espessura {AC}', 'Cremosidade'],
        ['Orégano', 'a olho', 'Salpicado por cima, antes do forno', 'Aroma'],
    ], num_cols=(1,), widths=['27%', '12%', '44%', '17%']) \
    + '<p class="note">Quantidades por pizza Grande. O catupiry é medido em listras (sem peso informado) e o orégano vai a olho; ver Melhorias.</p>' \
    + sec('03', 'Equipamentos e utensílios') + table(['Item', 'Uso'], [
        ['Mesa / bancada higienizada', 'Abrir a massa e montar a pizza'],
        ['Cortador de pizza (carretilha)', 'Aparar a borda da massa aberta e cortar as fatias'],
        ['Colher funda (padrão)', 'Aplicar e espalhar o molho (150 ml na Grande)'],
        ['Balança', 'Conferir bolinha, muçarela, gorgonzola e provolone'],
        ['Faca e tábua dos queijos', 'Picar gorgonzola e provolone'],
        ['Bisnaga ou colher para catupiry', 'Aplicar as listras de catupiry'],
        ['Pá de pizza, forno a lenha e caixa', 'Assar a pizza (girar e retirar) e embalar para entrega'],
    ], widths=['40%', '60%'])

steps = [
    ('Preparar o posto:', ' mesa higienizada, queijos porcionados e refrigerados até o uso, colher funda, balança e catupiry à mão.' + pcc(1)),
    ('Abrir a bolinha', ' de massa (320 g) na mesa enfarinhada e <b>aparar o excesso da borda com o cortador</b>, deixando a massa redonda e uniforme.' + foto(1)),
    ('Aplicar 150 ml de molho', ' com a colher funda (padrão) e espalhar por toda a massa.' + pcc(2)),
    ('Espalhar a muçarela', ' (280 g) sobre o molho, distribuindo por igual.' + pcc(2)),
    ('Distribuir o gorgonzola', ' (24 g) e o <b>provolone</b> (150 g), picados, por cima da muçarela.' + pcc(2)),
    ('Aplicar o catupiry', ' em <b>4 listras</b> por cima dos queijos.' + pcc(2) + ac('Nº DE LISTRAS A CONFIRMAR')),
    ('Finalizar com orégano', ' a olho, por cima de tudo, antes de ir ao forno.' + foto(2)),
    ('Assar no forno a lenha', ' a 340 a 380 °C, por 3 a 4 min, até os queijos derreterem e a borda dourar.' + pcc(3)),
    ('Retirar, cortar', ' em 8 fatias (Grande) e embalar na caixa ou servir na hora.' + foto(3)),
]
st = ''.join(f'<div class="s"><span class="i">{i:02d}</span><p><b>{a}</b>{b}</p></div>' for i, (a, b) in enumerate(steps, 1))
flow = '<div class="flow">' + ''.join(f'<div><b>{a}</b><small>{b}</small></div>' for a, b in [
    ('Abrir', 'e aparar'), ('Molho', '150 ml'), ('Muçarela', '280 g'), ('Gorgonzola', 'e provolone'), ('Catupiry', '4 listras'), ('Orégano', 'e forno')]) + '</div>'
p3 = sec('04', 'Modo de montagem') + flow + f'<div class="steps">{st}</div>' + '<h3 class="sub">Pontos críticos de controle (PCC)</h3>' + table(
    ['PCC', 'O que controlar', 'Limite / referência'], [
        ['1 · Higienização', 'Mesa, utensílios e mãos limpos; queijos picados e porcionados refrigerados até o uso', 'Conforme RDC 216/2004 e rótulo dos fabricantes'],
        ['2 · Porções', 'Medida e peso de cada ingrediente por pizza', 'Grande: molho 150 ml · muçarela 280 g · gorgonzola 24 g · provolone 150 g · catupiry 4 listras'],
        ['3 · Forno', 'Temperatura e tempo de forno', '340 a 380 °C · 3 a 4 min · queijos derretidos, borda dourada'],
    ], widths=['18%', '44%', '38%'])

fotos = [
    (1, 'Massa aberta e aparada', 'Etapa 2', 'Pizzaiolo aparando o excesso da borda com o cortador de pizza, na mesa enfarinhada, deixando a massa redonda.', ''),
    (2, 'Pronta para o forno', 'Etapas 3 a 7', 'Molho por toda a massa, muçarela, pedaços de gorgonzola e provolone, listras onduladas de catupiry e orégano por cima. Na foto aparecem cerca de 6 listras, não 4 (a confirmar).', ''),
    (3, 'Pizza pronta na caixa', 'Etapas 8 e 9', 'Pizza assada já na caixa: muçarela dourada, gorgonzola derretido, listras de catupiry levemente douradas, orégano visível e borda assada.', ' wide'),
]
gal = ''.join(f'''<div class="ph{w}"><div class="im"><img src="img/q4-foto{n}.jpg"><span class="lb">FOTO {n}</span></div>
<h4>{t}</h4><p><b>{e}</b> · {d}</p></div>''' for n, t, e, d, w in fotos)
p4 = sec('05', 'Guia visual de fotos') + '<p class="note" style="margin:-1mm 0 4mm">Registro fotográfico da montagem acompanhada. Cada foto aparece uma única vez e corresponde à etapa indicada. Use como referência para conferir o ponto antes de seguir.</p>' \
    + '<style>.ph.wide{grid-column:span 2}.ph.wide .im{height:92mm}.gal .ph:not(.wide) .im{height:66mm}</style>' + f'<div class="gal">{gal}</div>'

dot = lambda c: f'<span class="dot-size" style="background:{c}"></span>'
p5 = sec('06', 'Características do produto') + table(['Atributo', 'Padrão esperado'], [
    ['Aparência', 'Queijos derretidos e uniformes; pedaços de gorgonzola e provolone distribuídos; listras de catupiry e orégano visíveis; borda dourada'],
    ['Massa', 'Borda dourada e levantada, sem partes cruas no centro'],
    ['Molho', 'Cobrindo toda a massa, sem encharcar nem deixar áreas secas'],
    ['Aroma / sabor', 'Queijos equilibrados: gorgonzola presente sem dominar; provolone defumado; catupiry cremoso; orégano sem queimar'],
], widths=['20%', '80%']) + sec('07', 'Padrão por tamanho') + \
    f'<p class="note" style="margin:-1mm 0 3mm">Grande: quantidades definidas. Média e Broto {EST}: proporcionais ao número de fatias (Média 5/8 · Broto 4/8 da Grande), com as listras de catupiry arredondadas. Hoje o tamanho é definido no olho; os diâmetros reais de Média e Broto ainda precisam ser medidos.</p>' + table(
    ['Item', 'Grande · 8 fatias', 'Média · 5 fatias (est.)', 'Broto · 4 fatias (est.)'], [
        ['Diâmetro', '≈35 cm (est.)', '≈28 cm', '≈25 cm'],
        ['Massa (bolinha)', '320 g', '≈200 g', '≈160 g'],
        ['Etiqueta (sugerida)', dot('#d7141a') + 'Vermelha', dot('#f2b705') + 'Amarela', dot('#3aa63a') + 'Verde'],
        ['Molho de tomate', '150 ml', '≈95 ml', '≈75 ml'],
        ['Muçarela', '280 g', '≈175 g', '≈140 g'],
        ['Gorgonzola', '24 g', '≈15 g', '≈12 g'],
        ['Provolone', '150 g', '≈95 g', '≈75 g'],
        ['Catupiry', '4 listras', '≈3 listras', '≈2 listras'],
        ['Orégano', 'a olho', 'a olho', 'a olho'],
    ], num_cols=(1, 2, 3), widths=['28%', '24%', '24%', '24%']) + \
    '<p class="note">Atenção: 320 g é o <b>peso</b> da bolinha da Grande, não o diâmetro. Como padronizar o tamanho: ver o material “Materiais e sugestão de compras” (gabarito, marcação na bancada, etiqueta por cor e conferência na pá).</p>' \
    + sec('08', 'Condições do forno') + table(['Item', 'Resposta'], [
        ['Tipo de forno', 'A lenha'],
        ['Temperatura', '340 a 380 °C é o ponto ideal (forno sem marcador de temperatura)'],
        ['Tempo médio de forno', '3 a 4 min'],
    ], widths=['32%', '68%'])

p6 = sec('09', 'Controle de qualidade e falhas comuns') + '<h3 class="sub" style="margin-top:0">Critérios de aprovação da pizza</h3><ul class="chk-l">' + ''.join(f'<li>{x}</li>' for x in [
    'Todas as porções conforme a seção 07 (molho, muçarela, gorgonzola, provolone e catupiry).',
    'Molho espalhado por toda a massa e queijos distribuídos por igual.',
    'Queijos derretidos, borda dourada e massa assada por inteiro.',
    'Listras de catupiry visíveis e orégano presente, sem queimar; sem corpos estranhos.',
    'Tamanho conferido na pá (diâmetro e número de fatias do pedido).']) + '</ul><h3 class="sub">Falhas mais comuns</h3>' + table(
    ['Falha', 'Causa provável', 'Correção'], [
        ['Centro cru ou mole', 'Excesso de molho ou de queijo; forno frio', 'Respeitar 150 ml e as porções; manter o forno em 340 a 380 °C'],
        ['Pizza oleosa ou encharcada', 'Muito queijo ou molho demais', 'Pesar os queijos e medir o molho com a colher funda'],
        ['Borda queimada ou pálida', 'Forno quente ou frio demais; tempo errado', 'Conferir o ponto do forno e o tempo de 3 a 4 min'],
        ['Gorgonzola dominante ou ausente', 'Peso fora dos 24 g ou mal distribuído', 'Pesar o gorgonzola e espalhar em pedaços pequenos'],
        ['Catupiry queimado ou escorrido', 'Listras grossas ou forno muito quente', 'Padronizar a espessura das listras e o tempo de forno'],
        ['Queijo sem derreter', 'Pouco tempo de forno ou pedaços grandes', 'Picar os queijos menores e manter o tempo de forno'],
        ['Pizza maior ou menor que o padrão', 'Bolinha sem peso e abertura no olho', 'Pesar a bolinha e usar gabarito'],
    ], widths=['26%', '34%', '40%']) + sec('10', 'Armazenamento dos ingredientes') + table(
    ['Ingrediente', 'Condição', 'Prazo'], [
        ['Muçarela e provolone', 'Refrigerados, na embalagem ou em recipiente tampado', 'Conforme rótulo'],
        ['Gorgonzola', 'Refrigerado, bem embalado, longe de outros alimentos para não passar aroma', 'Conforme rótulo'],
        ['Catupiry', 'Refrigerado após aberto, em recipiente tampado e identificado com a data de abertura', 'Conforme rótulo'],
        ['Queijos picados', 'Porcionados em recipiente tampado e identificado, sob refrigeração', AC],
        ['Etiqueta', 'Produto · data de preparo · validade · responsável · usar primeiro o que vence primeiro (PVPS)', 'Obrigatória'],
    ], widths=['22%', '58%', '20%'])

reg = table(['Data', 'Responsável', 'Tamanho', 'Peso bolinha', 'Tempo forno', 'Ponto OK?', 'Visto'], [[''] * 7 for _ in range(7)], widths=['12%', '22%', '13%', '14%', '13%', '13%', '13%'])
p7 = sec('11', 'Registro de montagem') + f'<div class="reg">{reg}</div><p class="note">Registro para conferir a padronização: tamanho, peso da bolinha e tempo de forno de algumas pizzas por turno.</p>' \
    + sec('12', 'Melhorias recomendadas') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        '<b>Pré-porcionar os queijos:</b> deixar muçarela (280 g), gorgonzola (24 g) e provolone (150 g) já pesados em porções, para a montagem sair sempre igual.',
        '<b>Padronizar a colher funda:</b> conferir uma vez que a colher entrega os 150 ml de molho e marcar essa colher para a Grande.',
        '<b>Padronizar a listra de catupiry:</b> definir espessura e comprimento (ou usar bisnaga com bico fixo) e pesar uma vez o catupiry de uma pizza para ter um peso de referência.',
        '<b>Peso da bolinha e gabarito:</b> hoje o tamanho é definido no olho e a borda é aparada com o cortador. Pesar a bolinha e abrir até o gabarito reduz a apara e o desperdício.',
        '<b>Validar Média e Broto:</b> medir os diâmetros reais e testar as porções estimadas da seção 07 com o pizzaiolo.',
        '<b>Padronizar o orégano:</b> definir uma medida fixa (por exemplo, uma colher-medida) no lugar do “a olho”.']) + '</ul>' \
    + '<div class="box"><h5>A confirmar com a equipe</h5><ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        'Se o gorgonzola é mesmo 24 g (bem menos que os 150 g de provolone).',
        'Se são 4 listras de catupiry: a foto da pizza crua mostra cerca de 6 listras mais curtas.',
        'Peso e espessura da listra de catupiry.',
        'Se o provolone vai ralado ou em pedaços.',
        'Validade dos queijos picados e marca dos queijos.',
        'Diâmetros reais de Média e Broto e teste das porções estimadas.']) + '</ul></div>' \
    + '<div class="sign"><div>Elaborado por</div><div>Responsável técnico</div><div>Aprovado por (Speciale)</div></div>'

subs = ['Identificação e ingredientes', 'Modo de montagem', 'Guia visual de fotos', 'Produto e padrão', 'Qualidade e armazenamento', 'Registro e melhorias']
pages = [cover] + [page(DOC, s, i + 2, T, FOOT, c) for i, (s, c) in enumerate(zip(subs, [p2, p3, p4, p5, p6, p7]))]
open('ficha_4queijos.html', 'w').write(html('Speciale · Ficha Técnica Pizza 4 Queijos', pages))
