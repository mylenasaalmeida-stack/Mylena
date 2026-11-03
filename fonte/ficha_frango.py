from common import *

DOC = 'FICHA TÉCNICA · PIZZA FRANGO COM CATUPIRY'
FOOT = 'Speciale Pizzas Artesanais · Ficha técnica de montagem · Versão 1.0'
T = 7
VER = 'Versão 1.0 · Novembro/2026'
P = 'quantidade de listras de catupiry a confirmar com a equipe'
TB = '<span class="tbc">a confirmar</span>'

cover = f'''<section class="page cover"><div class="chk top"></div>
<div class="in">{logo()}
<div class="tag">Ficha técnica de montagem</div>
<h1 style="font-size:42pt">Pizza Frango<span>com Catupiry</span></h1>
<p class="lead">Frango pré-preparado, muçarela e listras de catupiry sobre molho de tomate artesanal, com azeitona preta e orégano, assada em forno a lenha.</p>
<div class="stats">
<div class="st"><b>140 g</b><small>de frango pré-preparado por pizza Grande</small></div>
<div class="st"><b>280 g</b><small>de muçarela por pizza Grande</small></div>
<div class="st"><b>3 a 4 min</b><small>no forno a lenha, a 340 a 380 °C</small></div>
</div>
<div class="ver">{VER}</div>
</div><div class="chk bot"></div></section>'''

p2 = sec('01', 'Identificação geral') + table(['Campo', 'Informação'], [
    ['Nome do produto', 'Pizza Frango com Catupiry'],
    ['Código interno / SKU', '<span class="blank"></span>'],
    ['Categoria', 'Pizza salgada · montagem sobre a massa artesanal da casa'],
    ['Tamanho de referência', f'Grande · 8 fatias · bolinha de 320 g · ≈35 cm {EST} (Média e Broto na seção 07)'],
    ['Base', 'Massa de pizza artesanal (ficha própria) + molho de tomate artesanal (150 ml)'],
    ['Forno', 'A lenha · 340 a 380 °C (ponto ideal) · 3 a 4 min'],
    ['Alérgenos', f'CONTÉM GLÚTEN (trigo), LEITE (muçarela e catupiry) e SOJA (óleo da massa). Alérgenos do tempero do frango: ver Orientações finais (seção 13).'],
    ['Responsável técnico', '<span class="blank" style="min-width:80mm"></span>'],
    ['Data de elaboração', 'Novembro de 2026 · versão 1.0'],
], widths=['31%', '69%']) + '''<p class="note"><b>Descrição:</b> pizza montada em camadas sobre a massa aberta na hora: molho de tomate, muçarela, frango pré-preparado e listras de catupiry por cima, com azeitona e orégano.</p>''' \
    + sec('02', 'Ingredientes por pizza') + table(['Ingrediente', 'Quantidade', 'Forma de uso', 'Função'], [
        ['Massa de pizza (bolinha)', '1 un · 320 g', 'Aberta na hora e aparada com o cortador', 'Base'],
        ['Molho de tomate artesanal', '150 ml', 'Colher funda (padrão), por toda a massa', 'Sabor e umidade'],
        ['Muçarela', '280 g', 'Por toda a massa, sobre o molho', 'Base de queijo'],
        ['Frango', '140 g', 'Pré-preparado e porcionado (ver Orientações finais)', 'Recheio principal'],
        ['Catupiry', TB, f'Em listras por cima · {P}', 'Cremosidade'],
        ['Azeitona preta', '≈9 g', 'Em pedaços, espalhada por cima', 'Finalização'],
        ['Orégano', 'a olho', 'Polvilhado por cima, antes do forno', 'Aroma'],
    ], num_cols=(1,), widths=['25%', '13%', '45%', '17%']) \
    + '<p class="note">Quantidades por pizza Grande. O catupiry é medido em listras e o orégano vai a olho.</p>' \
    + sec('03', 'Equipamentos e utensílios') + table(['Item', 'Uso'], [
        ['Mesa / bancada higienizada', 'Abrir a massa e montar a pizza'],
        ['Cortador de pizza (carretilha)', 'Aparar a borda da massa aberta e cortar as fatias'],
        ['Colher funda (padrão)', 'Aplicar e espalhar o molho (150 ml na Grande)'],
        ['Balança', 'Conferir bolinha, muçarela, frango e azeitona'],
        ['Bisnaga ou colher para catupiry', 'Aplicar as listras de catupiry'],
        ['Pá de pizza, forno a lenha e caixa', 'Assar a pizza (girar e retirar) e embalar para entrega'],
    ], widths=['40%', '60%'])

steps = [
    ('Preparar o posto:', ' mesa higienizada, muçarela e frango porcionados e refrigerados até o uso, colher funda, balança e catupiry à mão.' + pcc(1)),
    ('Abrir a bolinha', ' de massa (320 g) na mesa enfarinhada e <b>aparar o excesso da borda com o cortador</b>, deixando a massa redonda e uniforme.'),
    ('Aplicar 150 ml de molho', ' com a colher funda (padrão) e espalhar por toda a massa.' + pcc(2)),
    ('Espalhar a muçarela', ' (280 g) sobre o molho, distribuindo por igual.' + pcc(2)),
    ('Distribuir o frango', ' (140 g) logo depois da muçarela, por toda a pizza, até perto da borda.' + pcc(2)),
    ('Aplicar o catupiry', f' em listras por cima de tudo (<span class="tbc">{P}</span>).' + pcc(2)),
    ('Espalhar a azeitona preta', ' em pedaços (≈9 g) e <b>polvilhar orégano</b> a olho, antes de ir ao forno.'),
    ('Assar no forno a lenha', ' a 340 a 380 °C, por 3 a 4 min, até a muçarela derreter, o catupiry dourar levemente e a borda assar.' + foto(1) + pcc(3)),
    ('Retirar, cortar', ' em 8 fatias (Grande) e embalar na caixa ou servir na hora.'),
]
st = ''.join(f'<div class="s"><span class="i">{i:02d}</span><p><b>{a}</b>{b}</p></div>' for i, (a, b) in enumerate(steps, 1))
flow = '<div class="flow">' + ''.join(f'<div><b>{a}</b><small>{b}</small></div>' for a, b in [
    ('Abrir', 'e aparar'), ('Molho', '150 ml'), ('Muçarela', '280 g'), ('Frango', '140 g'), ('Catupiry', 'em listras'), ('Azeitona', 'orégano e forno')]) + '</div>'
p3 = sec('04', 'Modo de montagem') + flow + f'<div class="steps">{st}</div>' + '<h3 class="sub">Pontos críticos de controle (PCC)</h3>' + table(
    ['PCC', 'O que controlar', 'Limite / referência'], [
        ['1 · Higienização', 'Mesa, utensílios e mãos limpos; frango pré-preparado, muçarela e catupiry refrigerados até o uso', 'Conforme RDC 216/2004 e rótulo dos fabricantes'],
        ['2 · Porções', 'Medida e peso de cada ingrediente por pizza', f'Grande: molho 150 ml · muçarela 280 g · frango 140 g · azeitona ≈9 g · catupiry: {P}'],
        ['3 · Forno', 'Temperatura e tempo de forno', '340 a 380 °C · 3 a 4 min · muçarela derretida, borda dourada'],
    ], widths=['18%', '44%', '38%'])

p4 = sec('05', 'Guia visual de fotos') + '<p class="note" style="margin:-1mm 0 4mm">Registro fotográfico enviado pela casa. A foto é de uma pizza <b>Broto</b>; as quantidades desta ficha são da <b>Grande</b>. Use a foto como referência de distribuição e de ponto, não de quantidade.</p>' + '''
<div class="ph"><div class="im" style="height:122mm"><img src="img/frango-foto1.jpg" style="object-position:50% 45%"><span class="lb">FOTO 1</span></div>
<h4>Detalhe da pizza assada</h4><p><b>Etapa 8</b> · Close da pizza Broto saída do forno: frango desfiado e alaranjado cobrindo toda a pizza, muçarela derretida aparecendo entre o frango, listras onduladas de catupiry em paralelo, levemente douradas, orégano por cima e borda clara e assada.</p></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:7mm;margin-top:5mm">
<div><h3 class="sub" style="margin-top:0">O que observar na foto</h3><ul class="chk-l">
<li>Frango distribuído por toda a pizza, até perto da borda, sem montes.</li>
<li>Catupiry em listras paralelas por cima do frango, de um lado ao outro.</li>
<li>Orégano espalhado por cima das listras.</li>
<li>Borda clara e assada, sem queimar; muçarela derretida.</li></ul></div>
<div><div class="box" style="margin-top:0"><h5>Diferenças em relação à receita</h5><ul class="dot">
<li>A azeitona preta não aparece na foto, mas está na receita.</li>
<li>A foto é de uma Broto: as quantidades dela não valem para a Grande.</li>
<li>A quantidade de listras de catupiry ainda está a confirmar com a equipe.</li></ul></div></div></div>
<p class="note" style="margin-top:4mm">Para completar o guia visual, vale fotografar uma pizza Grande nas etapas: massa aberta e aparada, muçarela e frango, catupiry e azeitona (crua) e pizza pronta na caixa.</p>'''

dot = lambda c: f'<span class="dot-size" style="background:{c}"></span>'
p5 = sec('06', 'Características do produto') + table(['Atributo', 'Padrão esperado'], [
    ['Aparência', 'Frango distribuído por toda a pizza; listras de catupiry visíveis e levemente douradas; azeitona e orégano por cima; borda dourada'],
    ['Massa', 'Borda dourada e levantada, sem partes cruas no centro'],
    ['Molho', 'Cobrindo toda a massa, sem encharcar nem deixar áreas secas'],
    ['Aroma / sabor', 'Frango temperado e úmido, sem ressecar; catupiry cremoso; orégano sem queimar'],
], widths=['20%', '80%']) + sec('07', 'Padrão por tamanho') + \
    f'<p class="note" style="margin:-1mm 0 3mm">Grande: quantidades definidas. Média e Broto {EST}: proporcionais ao número de fatias (Média 5/8 · Broto 4/8 da Grande). Hoje o tamanho é definido no olho; os diâmetros reais de Média e Broto ainda precisam ser medidos.</p>' + table(
    ['Item', 'Grande · 8 fatias', 'Média · 5 fatias (est.)', 'Broto · 4 fatias (est.)'], [
        ['Diâmetro', '≈35 cm (est.)', '≈28 cm', '≈25 cm'],
        ['Massa (bolinha)', '320 g', '≈200 g', '≈160 g'],
        ['Etiqueta (sugerida)', dot('#d7141a') + 'Vermelha', dot('#f2b705') + 'Amarela', dot('#3aa63a') + 'Verde'],
        ['Molho de tomate', '150 ml', '≈95 ml', '≈75 ml'],
        ['Muçarela', '280 g', '≈175 g', '≈140 g'],
        ['Frango', '140 g', '≈88 g', '≈70 g'],
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
    'Todas as porções conforme a seção 07 (molho, muçarela, frango, catupiry e azeitona).',
    'Molho espalhado por toda a massa e frango distribuído por igual.',
    'Muçarela derretida, borda dourada e massa assada por inteiro.',
    'Listras de catupiry visíveis e orégano presente, sem queimar; sem corpos estranhos.',
    'Tamanho conferido na pá (diâmetro e número de fatias do pedido).']) + '</ul><h3 class="sub">Falhas mais comuns</h3>' + table(
    ['Falha', 'Causa provável', 'Correção'], [
        ['Centro cru ou mole', 'Excesso de molho ou de recheio; forno frio', 'Respeitar 150 ml e as porções; manter o forno em 340 a 380 °C'],
        ['Frango ressecado ou queimado', 'Frango por cima sem proteção ou forno quente demais', 'Distribuir o frango sobre a muçarela e conferir o tempo de 3 a 4 min'],
        ['Frango concentrado no centro', 'Distribuição apressada', 'Espalhar os 140 g por toda a pizza, até perto da borda'],
        ['Pizza encharcada', 'Molho demais ou frango muito úmido', 'Medir o molho com a colher funda e escorrer o frango antes de usar'],
        ['Catupiry queimado ou escorrido', 'Listras grossas ou forno muito quente', 'Padronizar a bisnaga e o comprimento das listras'],
        ['Borda queimada ou pálida', 'Forno quente ou frio demais; tempo errado', 'Conferir o ponto do forno e o tempo de 3 a 4 min'],
        ['Pizza maior ou menor que o padrão', 'Bolinha sem peso e abertura no olho', 'Pesar a bolinha e usar gabarito'],
    ], widths=['26%', '34%', '40%']) + sec('10', 'Armazenamento dos ingredientes') + table(
    ['Ingrediente', 'Condição', 'Prazo'], [
        ['Frango pré-preparado', 'Refrigerado, porcionado em recipiente tampado e etiquetado', 'Conforme ficha do frango'],
        ['Muçarela', 'Refrigerada, na embalagem ou em recipiente tampado', 'Conforme rótulo'],
        ['Catupiry', 'Refrigerado após aberto, em recipiente tampado e identificado com a data de abertura', 'Conforme rótulo'],
        ['Azeitona preta e orégano', 'Azeitona tampada e refrigerada após aberta; orégano em pote fechado, em local seco', 'Conforme rótulo'],
        ['Etiqueta', 'Produto · data de preparo · validade · responsável · usar primeiro o que vence primeiro (PVPS)', 'Obrigatória'],
    ], widths=['22%', '58%', '20%'])

reg = table(['Data', 'Responsável', 'Tamanho', 'Peso bolinha', 'Tempo forno', 'Ponto OK?', 'Visto'], [[''] * 7 for _ in range(5)], widths=['12%', '22%', '13%', '14%', '13%', '13%', '13%'])
p7 = sec('11', 'Registro de montagem') + f'<div class="reg">{reg}</div><p class="note">Registro para conferir a padronização: tamanho, peso da bolinha e tempo de forno de algumas pizzas por turno.</p>' \
    + sec('12', 'Melhorias recomendadas') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        '<b>Pré-porcionar:</b> deixar muçarela (280 g) e frango (140 g) já pesados em porções, para a montagem sair sempre igual.',
        '<b>Padronizar a colher funda:</b> conferir uma vez que a colher entrega os 150 ml de molho e marcar essa colher para a Grande.',
        '<b>Padronizar a listra de catupiry:</b> usar sempre a mesma bisnaga e o mesmo comprimento de listra.',
        '<b>Peso da bolinha e gabarito:</b> pesar a bolinha e abrir até o gabarito reduz a apara e o desperdício.',
        '<b>Fotos da Grande:</b> fotografar a montagem de uma pizza Grande para completar o guia visual.']) + '</ul>' \
    + sec('13', 'Orientações finais') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        '<b>Fazer a ficha técnica do frango pré-preparado.</b> Ela não faz parte deste trabalho, mas é necessária: o frango é preparado antes (cozido, desfiado e temperado), guardado e só depois usado na pizza. Sem ficha própria não há padrão de tempero, ponto e sabor, nem regra de resfriamento, armazenamento e validade, e não dá para listar os alérgenos dos temperos. Pela RDC 216/2004, todo alimento preparado e guardado precisa desse controle. Esta ficha considera só a porção de 140 g por pizza Grande.',
        '<b>Média e Broto são estimativas.</b> As quantidades da seção 07 foram calculadas a partir da Grande, na proporção das fatias (5/8 e 4/8). É preciso aferir os dados reais: medir o diâmetro, pesar a bolinha e as porções de algumas pizzas de cada tamanho, ajustar com o pizzaiolo e atualizar a ficha.']) + '</ul>' \
    + '<div class="box"><h5>A confirmar com a equipe</h5><ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        'Quantidade de listras de catupiry por tamanho.',
        'Marca da muçarela e do catupiry; diâmetros reais de Média e Broto.']) + '</ul></div>' \
    + '<div class="sign"><div>Elaborado por</div><div>Responsável técnico</div><div>Aprovado por (Speciale)</div></div>'

subs = ['Identificação e ingredientes', 'Modo de montagem', 'Guia visual de fotos', 'Produto e padrão', 'Qualidade e armazenamento', 'Registro e melhorias']
pages = [cover] + [page(DOC, s, i + 2, T, FOOT, c) for i, (s, c) in enumerate(zip(subs, [p2, p3, p4, p5, p6, p7]))]
open('ficha_frango.html', 'w').write(html('Speciale · Ficha Técnica Pizza Frango com Catupiry', pages))
