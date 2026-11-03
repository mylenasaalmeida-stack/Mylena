from common import *

DOC = 'FICHA TÉCNICA · PIZZA DE LOMBINHO'
FOOT = 'Speciale Pizzas Artesanais · Ficha técnica de montagem · Versão 1.0'
T = 7
VER = 'Versão 1.0 · Novembro/2026'
P = 'quantidade de listras de catupiry a confirmar com a equipe'
TB = '<span class="tbc">a confirmar</span>'

cover = f'''<section class="page cover"><div class="chk top"></div>
<div class="in">{logo()}
<div class="tag">Ficha técnica de montagem</div>
<h1>Pizza de<span>Lombinho</span></h1>
<p class="lead">Lombo fatiado, muçarela e listras de catupiry sobre molho de tomate artesanal, com azeitona preta e orégano, assada em forno a lenha.</p>
<div class="stats">
<div class="st"><b>105 g</b><small>de lombo fatiado por pizza Grande</small></div>
<div class="st"><b>280 g</b><small>de muçarela por pizza Grande</small></div>
<div class="st"><b>3 a 4 min</b><small>no forno a lenha, a 340 a 380 °C</small></div>
</div>
<div class="ver">{VER}</div>
</div><div class="chk bot"></div></section>'''

p2 = sec('01', 'Identificação geral') + table(['Campo', 'Informação'], [
    ['Nome do produto', 'Pizza de Lombinho'],
    ['Código interno / SKU', '<span class="blank"></span>'],
    ['Categoria', 'Pizza salgada · montagem sobre a massa artesanal da casa'],
    ['Tamanho de referência', f'Grande · 8 fatias · bolinha de 320 g · ≈35 cm {EST} (Média e Broto na seção 07)'],
    ['Base', 'Massa de pizza artesanal (ficha própria) + molho de tomate artesanal (150 ml)'],
    ['Forno', 'A lenha · 340 a 380 °C (ponto ideal) · 3 a 4 min'],
    ['Alérgenos', f'CONTÉM GLÚTEN (trigo), LEITE (muçarela e catupiry) e SOJA (óleo da massa). Conferir também o rótulo do lombo.'],
    ['Responsável técnico', '<span class="blank" style="min-width:80mm"></span>'],
    ['Data de elaboração', 'Novembro de 2026 · versão 1.0'],
], widths=['31%', '69%']) + '''<p class="note"><b>Descrição:</b> pizza montada em camadas sobre a massa aberta na hora: molho de tomate, muçarela, lombo fatiado e listras de catupiry por cima, com azeitona e orégano.</p>''' \
    + sec('02', 'Ingredientes por pizza') + table(['Ingrediente', 'Quantidade', 'Forma de uso', 'Função'], [
        ['Massa de pizza (bolinha)', '1 un · 320 g', 'Aberta na hora e aparada com o cortador', 'Base'],
        ['Molho de tomate artesanal', '150 ml', 'Colher funda (padrão), por toda a massa', 'Sabor e umidade'],
        ['Muçarela', '280 g', 'Por toda a massa, sobre o molho', 'Base de queijo'],
        ['Lombo', '105 g', 'Fatiado, distribuído sobre a muçarela', 'Recheio principal'],
        ['Catupiry', TB, f'Em listras por cima · {P}', 'Cremosidade'],
        ['Azeitona preta', '≈9 g', 'Em pedaços, espalhada por cima', 'Finalização'],
        ['Orégano', 'a olho', 'Polvilhado por cima, antes do forno', 'Aroma'],
    ], num_cols=(1,), widths=['25%', '13%', '45%', '17%']) \
    + '<p class="note">Quantidades por pizza Grande. O catupiry é medido em listras e o orégano vai a olho.</p>' \
    + sec('03', 'Equipamentos e utensílios') + table(['Item', 'Uso'], [
        ['Mesa / bancada higienizada', 'Abrir a massa e montar a pizza'],
        ['Cortador de pizza (carretilha)', 'Aparar a borda da massa aberta e cortar as fatias'],
        ['Colher funda (padrão)', 'Aplicar e espalhar o molho (150 ml na Grande)'],
        ['Balança', 'Conferir bolinha, muçarela, lombo e azeitona'],
        ['Bisnaga ou colher para catupiry', 'Aplicar as listras de catupiry'],
        ['Pá de pizza, forno a lenha e caixa', 'Assar a pizza (girar e retirar) e embalar para entrega'],
    ], widths=['40%', '60%'])

steps = [
    ('Preparar o posto:', ' mesa higienizada, muçarela e lombo porcionados e refrigerados até o uso, colher funda, balança e catupiry à mão.' + pcc(1)),
    ('Abrir a bolinha', ' de massa (320 g) na mesa enfarinhada e <b>aparar o excesso da borda com o cortador</b>, deixando a massa redonda e uniforme.'),
    ('Aplicar 150 ml de molho', ' com a colher funda (padrão) e espalhar por toda a massa.' + pcc(2)),
    ('Espalhar a muçarela', ' (280 g) sobre o molho, distribuindo por igual.' + pcc(2)),
    ('Distribuir o lombo', ' fatiado (105 g) logo depois da muçarela, por toda a pizza, até perto da borda.' + pcc(2)),
    ('Aplicar o catupiry', f' em listras por cima de tudo (<span class="tbc">{P}</span>).' + pcc(2)),
    ('Espalhar a azeitona preta', ' em pedaços (≈9 g) e <b>polvilhar orégano</b> a olho, antes de ir ao forno.' + foto(1)),
    ('Assar no forno a lenha', ' a 340 a 380 °C, por 3 a 4 min, até a muçarela derreter, o catupiry dourar levemente e a borda assar.' + foto(2) + pcc(3)),
    ('Retirar, cortar', ' em 8 fatias (Grande) e embalar na caixa ou servir na hora.'),
]
st = ''.join(f'<div class="s"><span class="i">{i:02d}</span><p><b>{a}</b>{b}</p></div>' for i, (a, b) in enumerate(steps, 1))
flow = '<div class="flow">' + ''.join(f'<div><b>{a}</b><small>{b}</small></div>' for a, b in [
    ('Abrir', 'e aparar'), ('Molho', '150 ml'), ('Muçarela', '280 g'), ('Lombo', '105 g'), ('Catupiry', 'em listras'), ('Azeitona', 'orégano e forno')]) + '</div>'
p3 = sec('04', 'Modo de montagem') + flow + f'<div class="steps">{st}</div>' + '<h3 class="sub">Pontos críticos de controle (PCC)</h3>' + table(
    ['PCC', 'O que controlar', 'Limite / referência'], [
        ['1 · Higienização', 'Mesa, utensílios e mãos limpos; lombo, muçarela e catupiry refrigerados até o uso', 'Conforme RDC 216/2004 e rótulo dos fabricantes'],
        ['2 · Porções', 'Medida e peso de cada ingrediente por pizza', f'Grande: molho 150 ml · muçarela 280 g · lombo 105 g · azeitona ≈9 g · catupiry: {P}'],
        ['3 · Forno', 'Temperatura e tempo de forno', '340 a 380 °C · 3 a 4 min · muçarela derretida, borda dourada'],
    ], widths=['18%', '44%', '38%'])

fotos = [
    (1, 'lombo-foto1', 'Pronta para o forno', 'Etapa 7', 'Pizza crua sobre a pá, na boca do forno a lenha: fatias redondas de lombo sobrepostas cobrindo a pizza, muçarela aparecendo por baixo na borda, listras onduladas de catupiry em paralelo, azeitona preta em pedaços e orégano por cima.', '50% 88%'),
    (2, 'lombo-foto2', 'Pizza assada', 'Etapa 8', 'Detalhe da pizza saída do forno: lombo levemente dourado nas bordas das fatias, muçarela derretida, listras de catupiry inteiras e cremosas, azeitona preta em pedaços, orégano e borda dourada.', '50% 50%'),
]
def _ph(n, f, t, e, d, pos, h):
    return f'''<div class="ph"><div class="im" style="height:{h}"><img src="img/{f}.jpg" style="object-position:{pos}"><span class="lb">FOTO {n}</span></div>
<h4>{t}</h4><p><b>{e}</b> · {d}</p></div>'''
gal = _ph(*fotos[0][:5], '50% 50%', '84mm') + '<div style="display:grid;grid-template-columns:72mm 1fr;gap:7mm;margin-top:5mm">' + _ph(*fotos[1][:5], '50% 50%', '96mm') + '<div>BOXSLOT</div></div>'
p4 = sec('05', 'Guia visual de fotos') + '<p class="note" style="margin:-1mm 0 4mm">Registro fotográfico enviado pela casa. Cada foto aparece uma única vez e corresponde à etapa indicada. Use como referência de distribuição e de ponto.</p>' \
    + gal.replace('BOXSLOT', '<div class="box" style="margin-top:0"><h5>O que as fotos mostram</h5><ul class="dot">' \
    + '<li>O lombo aparece por cima da muçarela e por baixo do catupiry, o que reforça a ordem desta ficha.</li>' \
    + '<li>A azeitona preta vai em pedaços, espalhada por cima, junto com o orégano.</li>' \
    + '<li>Não há fotos da massa aberta nem da muçarela: vale fotografar essas etapas para completar o guia.</li></ul></div>')

dot = lambda c: f'<span class="dot-size" style="background:{c}"></span>'
p5 = sec('06', 'Características do produto') + table(['Atributo', 'Padrão esperado'], [
    ['Aparência', 'Fatias de lombo distribuídas por toda a pizza; listras de catupiry visíveis e levemente douradas; azeitona e orégano por cima; borda dourada'],
    ['Massa', 'Borda dourada e levantada, sem partes cruas no centro'],
    ['Molho', 'Cobrindo toda a massa, sem encharcar nem deixar áreas secas'],
    ['Aroma / sabor', 'Lombo macio, sem ressecar nem queimar nas bordas; catupiry cremoso; orégano sem queimar'],
], widths=['20%', '80%']) + sec('07', 'Padrão por tamanho') + \
    f'<p class="note" style="margin:-1mm 0 3mm">Grande: quantidades definidas. Média e Broto {EST}: proporcionais ao número de fatias (Média 5/8 · Broto 4/8 da Grande). Hoje o tamanho é definido no olho; os diâmetros reais de Média e Broto ainda precisam ser medidos.</p>' + table(
    ['Item', 'Grande · 8 fatias', 'Média · 5 fatias (est.)', 'Broto · 4 fatias (est.)'], [
        ['Diâmetro', '≈35 cm (est.)', '≈28 cm', '≈25 cm'],
        ['Massa (bolinha)', '320 g', '≈200 g', '≈160 g'],
        ['Etiqueta (sugerida)', dot('#d7141a') + 'Vermelha', dot('#f2b705') + 'Amarela', dot('#3aa63a') + 'Verde'],
        ['Molho de tomate', '150 ml', '≈95 ml', '≈75 ml'],
        ['Muçarela', '280 g', '≈175 g', '≈140 g'],
        ['Lombo', '105 g', '≈66 g', '≈53 g'],
        ['Catupiry', TB, TB, TB],
        ['Azeitona', '≈9 g', '≈6 g', '≈5 g'],
        ['Orégano', 'a olho', 'a olho', 'a olho'],
    ], num_cols=(1, 2, 3), widths=['28%', '24%', '24%', '24%']) + \
    '<p class="note">Atenção: 320 g é o <b>peso</b> da bolinha da Grande, não o diâmetro. Como padronizar o tamanho: ver o material “Materiais e sugestão de compras” (gabarito, marcação na bancada, etiqueta por cor e conferência na pá).</p>' \
    + sec('08', 'Condições do forno') + table(['Item', 'Resposta'], [
        ['Tipo de forno', 'A lenha'],
        ['Temperatura', '340 a 380 °C é o ponto ideal (forno sem marcador de temperatura)'],
        ['Tempo médio de forno', '3 a 4 min'],
    ], widths=['32%', '68%'])

p6 = sec('09', 'Controle de qualidade e falhas comuns') + '<h3 class="sub" style="margin-top:0">Critérios de aprovação da pizza</h3><ul class="chk-l">' + ''.join(f'<li>{x}</li>' for x in [
    'Todas as porções conforme a seção 07 (molho, muçarela, lombo, catupiry e azeitona).',
    'Molho espalhado por toda a massa e lombo distribuído por igual.',
    'Muçarela derretida, borda dourada e massa assada por inteiro.',
    'Listras de catupiry visíveis e orégano presente, sem queimar; sem corpos estranhos.',
    'Tamanho conferido na pá (diâmetro e número de fatias do pedido).']) + '</ul><h3 class="sub">Falhas mais comuns</h3>' + table(
    ['Falha', 'Causa provável', 'Correção'], [
        ['Centro cru ou mole', 'Excesso de molho ou de recheio; forno frio', 'Respeitar 150 ml e as porções; manter o forno em 340 a 380 °C'],
        ['Lombo ressecado ou queimado', 'Fatias soltas por cima ou forno quente demais', 'Distribuir o lombo sobre a muçarela e conferir o tempo de 3 a 4 min'],
        ['Lombo concentrado no centro', 'Distribuição apressada', 'Espalhar os 105 g por toda a pizza, até perto da borda'],
        ['Sabor salgado demais', 'Lombo acima da porção', 'Pesar o lombo (105 g)'],
        ['Pizza encharcada', 'Molho demais', 'Medir o molho com a colher funda'],
        ['Catupiry queimado ou escorrido', 'Listras grossas ou forno muito quente', 'Padronizar a bisnaga e o comprimento das listras'],
        ['Borda queimada ou pálida', 'Forno quente ou frio demais; tempo errado', 'Conferir o ponto do forno e o tempo de 3 a 4 min'],
        ['Pizza maior ou menor que o padrão', 'Bolinha sem peso e abertura no olho', 'Pesar a bolinha e usar gabarito'],
    ], widths=['26%', '34%', '40%']) + sec('10', 'Armazenamento dos ingredientes') + table(
    ['Ingrediente', 'Condição', 'Prazo'], [
        ['Lombo', 'Refrigerado, na embalagem ou fatiado e porcionado em recipiente tampado e etiquetado', 'Ver seção 13'],
        ['Muçarela', 'Refrigerada, na embalagem ou em recipiente tampado', 'Conforme rótulo'],
        ['Catupiry', 'Refrigerado após aberto, em recipiente tampado e identificado com a data de abertura', 'Conforme rótulo'],
        ['Azeitona preta e orégano', 'Azeitona tampada e refrigerada após aberta; orégano em pote fechado, em local seco', 'Conforme rótulo'],
        ['Etiqueta', 'Produto · data de preparo · validade · responsável · usar primeiro o que vence primeiro (PVPS)', 'Obrigatória'],
    ], widths=['22%', '58%', '20%'])

reg = table(['Data', 'Responsável', 'Tamanho', 'Peso bolinha', 'Tempo forno', 'Ponto OK?', 'Visto'], [[''] * 7 for _ in range(5)], widths=['12%', '22%', '13%', '14%', '13%', '13%', '13%'])
p7 = sec('11', 'Registro de montagem') + f'<div class="reg">{reg}</div><p class="note">Registro para conferir a padronização: tamanho, peso da bolinha e tempo de forno de algumas pizzas por turno.</p>' \
    + sec('12', 'Melhorias recomendadas') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        '<b>Pré-porcionar:</b> deixar muçarela (280 g) e lombo (105 g) já pesados em porções, para a montagem sair sempre igual.',
        '<b>Padronizar a colher funda:</b> conferir uma vez que a colher entrega os 150 ml de molho e marcar essa colher para a Grande.',
        '<b>Padronizar a listra de catupiry:</b> usar sempre a mesma bisnaga e o mesmo comprimento de listra.',
        '<b>Peso da bolinha e gabarito:</b> pesar a bolinha e abrir até o gabarito reduz a apara e o desperdício.',
        '<b>Fotos da montagem:</b> fotografar as etapas de massa aberta e muçarela para completar o guia visual.']) + '</ul>' \
    + sec('13', 'Orientações finais') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        '<b>Forma de compra do lombo: informação a ser apresentada pela equipe.</b> Não se sabe ainda se o lombo chega já fatiado ou se é fatiado na casa, e isso muda o controle. Se vier fatiado, valem a validade e os alérgenos do rótulo. Se for fatiado na casa, é preciso definir a espessura da fatia, a higienização do fatiador e a validade depois de aberto e fatiado, com etiqueta. Se for preparado ou temperado na casa, precisa de ficha técnica própria, como pede a RDC 216/2004.',
        '<b>Média e Broto são estimativas.</b> As quantidades da seção 07 foram calculadas a partir da Grande, na proporção das fatias (5/8 e 4/8). É preciso aferir os dados reais: medir o diâmetro, pesar a bolinha e as porções de algumas pizzas de cada tamanho, ajustar com o pizzaiolo e atualizar a ficha.']) + '</ul>' \
    + '<div class="box"><h5>A confirmar com a equipe</h5><ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        'Quantidade de listras de catupiry por tamanho.',
        'Se o lombo chega já fatiado ou é fatiado na casa, e a marca (ver seção 13).',
        'Marca da muçarela e do catupiry; diâmetros reais de Média e Broto.']) + '</ul></div>' \
    + '<div class="sign"><div>Elaborado por</div><div>Responsável técnico</div><div>Aprovado por (Speciale)</div></div>'

subs = ['Identificação e ingredientes', 'Modo de montagem', 'Guia visual de fotos', 'Produto e padrão', 'Qualidade e armazenamento', 'Registro e melhorias']
pages = [cover] + [page(DOC, s, i + 2, T, FOOT, c) for i, (s, c) in enumerate(zip(subs, [p2, p3, p4, p5, p6, p7]))]
open('ficha_lombinho.html', 'w').write(html('Speciale · Ficha Técnica Pizza de Lombinho', pages))
