from common import *

DOC = 'FICHA TÉCNICA · PIZZA PORTUGUESA'
FOOT = 'Speciale Pizzas Artesanais · Ficha técnica de montagem · Versão 1.3'
T = 7
VER = 'Versão 1.3 · Novembro/2026'

cover = f'''<section class="page cover"><div class="chk top"></div>
<div class="in">{logo()}
<div class="tag">Ficha técnica de montagem</div>
<h1>Pizza<span>Portuguesa</span></h1>
<p class="lead">Muçarela, presunto, ovo cozido, cebola e azeitona preta sobre molho de tomate artesanal, finalizada com orégano e assada em forno a lenha.</p>
<div class="stats">
<div class="st"><b>280 g</b><small>de muçarela ralada por pizza Grande</small></div>
<div class="st"><b>150 ml</b><small>de molho de tomate, com colher funda, por toda a massa</small></div>
<div class="st"><b>3 a 4 min</b><small>no forno a lenha, a 340 a 380 °C</small></div>
</div>
<div class="ver">{VER}</div>
</div><div class="chk bot"></div></section>'''

p2 = sec('01', 'Identificação geral') + table(['Campo', 'Informação'], [
    ['Nome do produto', 'Pizza Portuguesa'],
    ['Código interno / SKU', '<span class="blank"></span>'],
    ['Categoria', 'Pizza salgada · montagem sobre a massa artesanal da casa'],
    ['Tamanho de referência', f'Grande · 8 fatias · bolinha de 320 g · ≈35 cm {EST} (Média e Broto na seção 07)'],
    ['Base', 'Massa de pizza artesanal (ficha própria) + molho de tomate artesanal (150 ml)'],
    ['Forno', 'A lenha · 340 a 380 °C (ponto ideal) · 3 a 4 min'],
    ['Alérgenos', 'CONTÉM GLÚTEN (trigo), LEITE (muçarela), OVO e SOJA (óleo da massa). Conferir também o rótulo do presunto.'],
    ['Responsável técnico', '<span class="blank" style="min-width:80mm"></span>'],
    ['Data de elaboração', 'Novembro de 2026 · versão 1.3'],
], widths=['31%', '69%']) + '''<p class="note"><b>Descrição:</b> pizza tradicional montada em camadas sobre a massa aberta na hora: molho de tomate, muçarela ralada, presunto fatiado em tiras, ovo cozido em rodelas, cebola e azeitona preta, finalizada com orégano.</p>''' \
    + sec('02', 'Ingredientes por pizza') + table(['Ingrediente', 'Quantidade', 'Forma de uso', 'Função'], [
        ['Massa de pizza (bolinha)', '1 un · 320 g', 'Aberta na hora e aparada com o cortador', 'Base'],
        ['Molho de tomate artesanal', '150 ml', 'Colher funda (padrão), por toda a massa', 'Sabor e umidade'],
        ['Muçarela', '280 g', 'Ralada, distribuída sobre o molho', 'Recheio principal'],
        ['Presunto', '70 g', 'Fatiado, em tiras a partir do centro', 'Sabor e sal'],
        ['Ovo cozido', '2 un', 'Em rodelas, entre as tiras', 'Complemento clássico'],
        ['Cebola', '100 g', f'Corte {AC}', 'Doçura e aroma'],
        ['Azeitona preta', '9 g', 'Em pedaços, espalhada', 'Finalização'],
        ['Orégano', 'a olho', 'Salpicado por cima, antes do forno', 'Aroma'],
    ], num_cols=(1,), widths=['27%', '15%', '36%', '22%']) \
    + '<p class="note">Quantidades por pizza Grande. Orégano vai a olho, sem peso definido (ver Melhorias). O corte e a etapa da cebola estão a confirmar.</p>' \
    + sec('03', 'Equipamentos e utensílios') + table(['Item', 'Uso'], [
        ['Mesa / bancada higienizada', 'Abrir a massa e montar a pizza'],
        ['Cortador de pizza (carretilha)', 'Aparar a borda da massa aberta e cortar as fatias'],
        ['Colher funda (padrão)', 'Aplicar e espalhar o molho (150 ml na Grande)'],
        ['Balança', 'Conferir bolinha, muçarela, presunto, cebola e azeitona'],
        ['Pá de pizza e forno a lenha', 'Levar a pizza ao forno, girar e retirar'],
        ['Caixa de pizza', 'Embalar a pizza pronta para entrega'],
    ], widths=['40%', '60%'])

steps = [
    ('Preparar o posto:', ' mesa higienizada, ingredientes porcionados e refrigerados até o uso, colher funda e balança à mão.' + pcc(1)),
    ('Abrir a bolinha', ' de massa (320 g) na mesa enfarinhada e <b>aparar a borda com o cortador</b> até o tamanho da pizza.' + foto(1) + foto(2)),
    ('Aplicar 150 ml de molho', ' com a colher funda e espalhar por toda a massa, deixando só a borda livre.' + pcc(2)),
    ('Distribuir a muçarela ralada', ' (280 g) sobre o molho, por igual.' + foto(3) + pcc(2)),
    ('Dispor o presunto', ' (70 g) fatiado em tiras, partindo do centro, sobre a muçarela.' + pcc(2)),
    ('Incluir o ovo cozido', ' em rodelas (2 ovos) entre as tiras de presunto.'),
    ('Distribuir a cebola', f' (100 g).' + ac('ETAPA E CORTE A CONFIRMAR')),
    ('Espalhar a azeitona preta', ' em pedaços (9 g) e finalizar com <b>orégano</b> a olho, por cima de tudo.' + foto(4)),
    ('Assar no forno a lenha', ' a 340 a 380 °C, por 3 a 4 min, até a muçarela derreter e a borda dourar.' + foto(5) + pcc(3)),
    ('Retirar, cortar', ' em 8 fatias (Grande) e embalar na caixa ou servir na hora.' + foto(6)),
]
st = ''.join(f'<div class="s"><span class="i">{i:02d}</span><p><b>{a}</b>{b}</p></div>' for i, (a, b) in enumerate(steps, 1))
flow = '<div class="flow">' + ''.join(f'<div><b>{a}</b><small>{b}</small></div>' for a, b in [
    ('Abrir', 'e aparar'), ('Molho', '150 ml'), ('Muçarela', '280 g'), ('Presunto', '70 g'), ('Ovo · cebola', 'azeitona'), ('Orégano', 'e forno')]) + '</div>'
p3 = sec('04', 'Modo de montagem') + flow + f'<div class="steps">{st}</div>' + '<h3 class="sub">Pontos críticos de controle (PCC)</h3>' + table(
    ['PCC', 'O que controlar', 'Limite / referência'], [
        ['1 · Higienização', 'Mesa, utensílios e mãos limpos; ovo cozido, presunto, muçarela e cebola cortada refrigerados até o uso', 'Conforme RDC 216/2004 e rótulo dos fabricantes'],
        ['2 · Porções', 'Medida e peso de cada ingrediente por pizza', 'Grande: molho 150 ml · muçarela 280 g · presunto 70 g · cebola 100 g · azeitona 9 g · ovo 2 un'],
        ['3 · Forno', 'Temperatura e tempo de forno', '340 a 380 °C · 3 a 4 min · muçarela derretida, borda dourada'],
    ], widths=['18%', '44%', '38%'])

fotos = [
    (1, 'Massa aberta e aparada', 'Etapa 2', 'Pizzaiolo aparando a borda da massa aberta com o cortador, na mesa enfarinhada. A tira que sobra é massa perdida (ver material de padronização).'),
    (2, 'Massas abertas na bancada', 'Etapa 2', 'Várias massas já abertas, enfileiradas na bancada, redondas e de espessura uniforme, prontas para receber o molho.'),
    (3, 'Muçarela sobre o molho', 'Etapa 4', 'Muçarela ralada sendo distribuída à mão sobre o molho, cobrindo a massa por igual e deixando a borda livre.'),
    (4, 'Montada, pronta para o forno', 'Etapa 8', 'Presunto em tiras a partir do centro, rodelas de ovo, azeitona preta em pedaços e orégano por cima. A cebola não aparece na foto.'),
    (5, 'Ponto de saída do forno', 'Etapa 9', 'Close da pizza assada: muçarela derretida e dourada, ovo e presunto no ponto, azeitona e orégano visíveis.'),
    (6, 'Pizza pronta na caixa', 'Etapa 10', 'Pizza inteira já embalada na caixa: borda dourada, muçarela derretida e ingredientes bem distribuídos.'),
]
gal = ''.join(f'''<div class="ph"><div class="im"><img src="img/port-foto{ {5:6,6:5}.get(n,n) }.jpg"><span class="lb">FOTO {n}</span></div>
<h4>{t}</h4><p><b>{e}</b> · {d}</p></div>''' for n, t, e, d in fotos)
p4 = sec('05', 'Guia visual de fotos') + '<p class="note" style="margin:-1mm 0 4mm">Registro fotográfico da montagem acompanhada na visita. Cada foto aparece uma única vez e corresponde à etapa indicada. Use como referência para conferir o ponto antes de seguir.</p>' + f'<div class="gal">{gal}</div>'

dot = lambda c: f'<span class="dot-size" style="background:{c}"></span>'
p5 = sec('06', 'Características do produto') + table(['Atributo', 'Padrão esperado'], [
    ['Aparência', 'Muçarela derretida e uniforme; tiras de presunto a partir do centro; rodelas de ovo, cebola e azeitona bem distribuídas; borda dourada'],
    ['Massa', 'Borda dourada e levantada, sem partes cruas no centro'],
    ['Molho', 'Cobrindo toda a massa, sem encharcar nem deixar áreas secas'],
    ['Aroma / sabor', 'Tomate, queijo e presunto equilibrados; orégano presente, sem queimar'],
], widths=['20%', '80%']) + sec('07', 'Padrão por tamanho') + \
    f'<p class="note" style="margin:-1mm 0 3mm">Grande: quantidades definidas. Média e Broto {EST}: proporcionais ao número de fatias (Média 5/8 · Broto 4/8 da Grande, arredondado). Hoje o tamanho é definido no olho; os diâmetros reais de Média e Broto ainda precisam ser medidos. Validar na prática e ajustar.</p>' + table(
    ['Item', 'Grande · 8 fatias', f'Média · 5 fatias (est.)', f'Broto · 4 fatias (est.)'], [
        ['Diâmetro', '≈35 cm (est.)', '≈28 cm', '≈25 cm'],
        ['Massa (bolinha)', '320 g', '≈200 g', '≈160 g'],
        ['Etiqueta (sugerida)', dot('#d7141a') + 'Vermelha', dot('#f2b705') + 'Amarela', dot('#3aa63a') + 'Verde'],
        ['Molho de tomate', '150 ml', '≈95 ml', '≈75 ml'],
        ['Muçarela', '280 g', '≈175 g', '≈140 g'],
        ['Presunto', '70 g', '≈45 g', '≈35 g'],
        ['Cebola', '100 g', '≈60 g', '≈50 g'],
        ['Ovo cozido', '2 un', '1 un', '1 un'],
        ['Azeitona preta', '9 g', '≈6 g', '≈5 g'],
        ['Orégano', 'a olho', 'a olho', 'a olho'],
    ], num_cols=(1, 2, 3), widths=['28%', '24%', '24%', '24%']) + \
    '<p class="note">Atenção: 320 g é o <b>peso</b> da bolinha da Grande, não o diâmetro. Como padronizar o tamanho e reduzir o desperdício: ver o material “Materiais e sugestão de compras” (gabarito, marcação na bancada, etiqueta por cor e conferência na pá).</p>' \
    + sec('08', 'Condições do forno') + table(['Item', 'Resposta'], [
        ['Tipo de forno', 'A lenha'],
        ['Temperatura', '340 a 380 °C é o ponto ideal (forno sem marcador de temperatura)'],
        ['Tempo médio de forno', '3 a 4 min'],
    ], widths=['32%', '68%'])

p6 = sec('09', 'Controle de qualidade e falhas comuns') + '<h3 class="sub" style="margin-top:0">Critérios de aprovação da pizza</h3><ul class="chk-l">' + ''.join(f'<li>{x}</li>' for x in [
    'Todas as porções conforme a seção 07 (molho, muçarela, presunto, cebola, ovo e azeitona).',
    'Molho espalhado por toda a massa e ingredientes distribuídos por igual.',
    'Muçarela derretida, borda dourada e massa assada por inteiro.',
    'Orégano presente e sem queimar; sem corpos estranhos.',
    'Tamanho conferido na pá (diâmetro e número de fatias do pedido).']) + '</ul><h3 class="sub">Falhas mais comuns</h3>' + table(
    ['Falha', 'Causa provável', 'Correção'], [
        ['Centro cru ou mole', 'Excesso de molho ou de ingredientes; forno frio', 'Respeitar 150 ml e as porções; manter o forno em 340 a 380 °C'],
        ['Pizza encharcada', 'Molho demais ou cebola/ovo úmidos', 'Medir o molho com a colher funda; escorrer a cebola cortada'],
        ['Borda queimada ou pálida', 'Forno quente ou frio demais; tempo errado', 'Conferir o ponto do forno e o tempo de 3 a 4 min'],
        ['Muçarela sem derreter', 'Pouco tempo de forno ou camada irregular', 'Distribuir os 280 g por igual e manter o tempo'],
        ['Sabor salgado demais', 'Presunto ou azeitona acima da porção', 'Pesar presunto (70 g) e azeitona (9 g)'],
        ['Pizza maior ou menor que o padrão', 'Bolinha sem peso e abertura no olho', 'Pesar a bolinha e usar gabarito'],
    ], widths=['26%', '34%', '40%']) + sec('10', 'Armazenamento dos ingredientes') + table(
    ['Ingrediente', 'Condição', 'Prazo'], [
        ['Muçarela e presunto', 'Refrigerados, na embalagem ou em recipiente tampado', 'Conforme rótulo'],
        ['Ovo cozido', 'Cozido por completo, resfriado e refrigerado em recipiente tampado e etiquetado', AC],
        ['Cebola cortada', 'Refrigerada, em recipiente tampado e identificado', AC],
        ['Azeitona e orégano', 'Azeitona em recipiente tampado e refrigerado após aberta; orégano em pote fechado, em local seco', 'Conforme rótulo'],
        ['Etiqueta', 'Produto · data de preparo · validade · responsável · usar primeiro o que vence primeiro (PVPS)', 'Obrigatória'],
    ], widths=['22%', '58%', '20%'])

reg = table(['Data', 'Responsável', 'Tamanho', 'Peso bolinha', 'Tempo forno', 'Ponto OK?', 'Visto'], [[''] * 7 for _ in range(7)], widths=['12%', '22%', '13%', '14%', '13%', '13%', '13%'])
p7 = sec('11', 'Registro de montagem') + f'<div class="reg">{reg}</div><p class="note">Registro para conferir a padronização: tamanho, peso da bolinha e tempo de forno de algumas pizzas por turno.</p>' \
    + sec('12', 'Melhorias recomendadas') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        '<b>Pré-porcionar os ingredientes:</b> deixar muçarela (280 g), presunto (70 g), cebola (100 g) e azeitona (9 g) já pesados em porções, para a montagem sair sempre igual.',
        '<b>Padronizar a colher funda:</b> conferir uma vez que a colher entrega os 150 ml de molho e marcar essa colher para a Grande.',
        '<b>Peso da bolinha e gabarito:</b> hoje o tamanho é definido no olho e a borda é aparada com o cortador. Pesar a bolinha e abrir até o gabarito reduz a apara e o desperdício.',
        '<b>Validar Média e Broto:</b> medir os diâmetros reais e testar as porções estimadas da seção 07 com o pizzaiolo.',
        '<b>Padronizar o orégano:</b> definir uma medida fixa (por exemplo, uma colher-medida) no lugar do “a olho”.']) + '</ul>' \
    + '<div class="box"><h5>A confirmar com a equipe</h5><ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        'Em que etapa a cebola entra e qual é o corte (está na receita, mas não aparece nas fotos).',
        'Se aparar a borda com o cortador fica como padrão da Portuguesa (aparece na Foto 1).',
        'Validade do ovo cozido e da cebola cortada.',
        'Marca do presunto e da muçarela.',
        'Diâmetros reais de Média e Broto e teste das porções estimadas.']) + '</ul></div>' \
    + '<div class="sign"><div>Elaborado por</div><div>Responsável técnico</div><div>Aprovado por (Speciale)</div></div>'

subs = ['Identificação e ingredientes', 'Modo de montagem', 'Guia visual de fotos', 'Produto e padrão', 'Qualidade e armazenamento', 'Registro e melhorias']
pages = [cover] + [page(DOC, s, i + 2, T, FOOT, c) for i, (s, c) in enumerate(zip(subs, [p2, p3, p4, p5, p6, p7]))]
open('ficha_portuguesa.html', 'w').write(html('Speciale · Ficha Técnica Pizza Portuguesa', pages))
