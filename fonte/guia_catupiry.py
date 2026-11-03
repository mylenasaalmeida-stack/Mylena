from common import *

DOC = 'GUIA DE PADRONIZAÇÃO · CATUPIRY'
FOOT = 'Speciale Pizzas Artesanais · Como medir o catupiry · Versão 1.0'
T = 5

extra = '''<style>
.rec{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:2mm}
.rec>div{background:var(--cream);border-top:3px solid var(--red);border-radius:5px;padding:4mm}
.rec b.k{font-family:'Roboto Condensed',sans-serif;font-weight:800;color:var(--red);font-size:20pt;display:block;line-height:1}
.rec h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:10.5pt;margin:1.5mm 0 1mm}
.rec p{font-size:8pt;line-height:1.45}
.lv{display:inline-block;width:46px;height:7px;border-radius:4px;background:#eee;position:relative;vertical-align:1px;margin-right:5px}
.lv i{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:var(--red)}
.ok{color:#2b8a3e;font-weight:700}.no{color:var(--red);font-weight:700}
.big-note{background:var(--red);color:#fff;border-radius:6px;padding:4mm 5mm;margin-top:4mm;font-size:9pt}
.big-note b{font-family:'Roboto Condensed',sans-serif;font-size:11.5pt;text-transform:uppercase;display:block;margin-bottom:1mm}
.fill td{height:7.5mm}
.std{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:2mm}
.std div{border:1.5px solid var(--red);border-radius:6px;padding:3mm 4mm;font-size:8.4pt}
.std h5{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:10pt;text-transform:uppercase;margin-bottom:1.5mm}
.std p{margin:1.4mm 0}
</style>'''


def lv(n):  # nível 1 a 5
    return f'<span class="lv"><i style="width:{n * 20}%"></i></span>'


cover = f'''<section class="page cover"><div class="chk top"></div>
<div class="in">{logo()}
<div class="tag">Guia de padronização</div>
<h1>Como medir<span>o catupiry</span></h1>
<p class="lead">Qual a melhor forma de medir o catupiry das pizzas, como fazer o teste para definir o padrão de cada tamanho e como conferir no dia a dia.</p>
<div class="stats">
<div class="st"><b>Pesar</b><small>uma vez, para descobrir quanto vai em cada pizza</small></div>
<div class="st"><b>Bico fixo</b><small>no dia a dia, com número e comprimento de listras definidos</small></div>
<div class="st"><b>Conferir</b><small>toda semana, por amostragem, na balança</small></div>
</div>
<div class="ver">Versão 1.0 · Novembro/2026</div>
</div><div class="chk bot"></div></section>'''

p2 = sec('01', 'Por que medir o catupiry') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
    '<b>Hoje o catupiry é medido em listras, sem peso.</b> A listra muda de tamanho conforme o pizzaiolo, a força na bisnaga e o bico usado. Duas pizzas com o mesmo número de listras podem levar quantidades bem diferentes.',
    '<b>As fotos já mostram essa variação:</b> na 4 Queijos a receita falava em 4 listras e a foto mostra cerca de 6; na Frango com Catupiry e na Lombinho a quantidade ainda está a confirmar com a equipe.',
    '<b>Catupiry demais</b> escorre, queima no forno a lenha e deixa a pizza pesada. <b>Catupiry de menos</b> é reclamação do cliente, porque é o ingrediente que dá nome ao sabor.',
    '<b>É um dos ingredientes que mais pesam no custo.</b> Sem medida, não há como saber quanto vai em cada pizza nem comparar o consumo com as vendas.',
]) + '</ul>' + sec('02', 'Formas de medir: comparação') + table(
    ['Forma de medir', 'Como funciona', 'Precisão', 'Praticidade', 'Melhor uso'], [
        ['Contar listras a olho (hoje)', 'O pizzaiolo faz o número de listras combinado, sem bico ou comprimento definido', lv(1) + 'Baixa', lv(5) + 'Alta', 'Não recomendado sozinho'],
        ['Tara na balança', 'Coloca a pizza montada (sem catupiry) sobre a balança, zera (tara), aplica o catupiry e lê o peso', lv(5) + 'Alta', lv(3) + 'Média', '<b>Definir o padrão</b> e conferir'],
        ['Pesar a bisnaga antes e depois', 'Pesa a bisnaga cheia, faz a pizza, pesa de novo; a diferença é o que foi usado', lv(5) + 'Alta', lv(3) + 'Média', 'Teste e conferência'],
        ['Bisnaga com bico fixo', 'Mesmo bico sempre, número de listras e comprimento definidos (de borda a borda)', lv(4) + 'Boa', lv(5) + 'Alta', '<b>Dia a dia</b>'],
        ['Porção pré-pesada', 'Separa antes do turno a porção de cada pizza em saco de confeitar descartável', lv(5) + 'Alta', lv(2) + 'Baixa', 'Só se a variação continuar'],
        ['Colher ou concha dosadora', 'Mede o volume com colher padrão', lv(3) + 'Média', lv(2) + 'Baixa', 'Não serve para fazer listras'],
    ], widths=['21%', '35%', '15%', '15%', '14%']) + \
    '<p class="note">Precisão: o quanto a medida se repete de uma pizza para outra. Praticidade: o quanto atrapalha a montagem no horário de pico.</p>'

p3 = sec('03', 'A melhor forma: recomendação') + '<p style="margin-bottom:2mm">Nenhuma forma sozinha resolve. A recomendação é combinar três passos: <b>pesar para definir</b>, <b>usar bico fixo no dia a dia</b> e <b>pesar de novo para conferir</b>.</p>' + '''<div class="rec">
<div><b class="k">1</b><h4>Definir o padrão</h4><p>Fazer o teste da seção 04 com a <b>tara na balança</b>: descobrir quantos gramas e quantas listras vão em cada tamanho (Grande, Média e Broto).</p></div>
<div><b class="k">2</b><h4>Usar no dia a dia</h4><p>Aplicar <b>sempre com o mesmo bico</b> (ver o guia “Bico no catupiry”), com o número de listras definido e cada listra de borda a borda. O pizzaiolo não precisa pesar.</p></div>
<div><b class="k">3</b><h4>Conferir</h4><p>Uma vez por semana, pesar o catupiry de 3 pizzas por tamanho (tara na balança). Se sair da faixa combinada, refazer o treino com o pizzaiolo.</p></div>
</div>
<div class="big-note"><b>Por que a tara na balança é a melhor forma de medir</b>A balança da casa já é usada para os outros ingredientes, a pizza já está sobre a bancada e a leitura é direta, em gramas, para a pizza inteira. Pesar a bisnaga antes e depois também funciona, mas exige duas pesagens e o resultado se perde se alguém usar a bisnaga no meio.</div>''' \
    + sec('04', 'Passo a passo do teste') + '<div class="steps">' + ''.join(
        f'<div class="s"><span class="i">{i:02d}</span><p>{t}</p></div>' for i, t in enumerate([
            '<b>Escolher o bico</b> que vai ser o padrão da casa e separar para uso só do catupiry.',
            '<b>Montar a pizza normalmente</b> até a etapa do catupiry (massa, molho, queijo e recheio).',
            '<b>Colocar a pizza sobre a balança</b> (em uma assadeira ou disco, se preciso) e <b>zerar a balança (tara)</b>.',
            '<b>Aplicar o catupiry</b> como o pizzaiolo faz hoje, contando as listras e fazendo cada uma de borda a borda.',
            '<b>Anotar no formulário</b> (seção 06): tamanho, número de listras e peso em gramas.',
            '<b>Repetir em 5 pizzas de cada tamanho</b>, de preferência com mais de um pizzaiolo.',
            '<b>Provar e olhar a pizza assada:</b> catupiry cremoso, sem escorrer nem queimar, e presente em todas as fatias.',
            '<b>Definir o padrão</b> de cada tamanho (peso de referência e número de listras), aprovar com a responsável e atualizar as fichas técnicas.',
        ], 1)) + '</div>' \
    + sec('05', 'Bico recomendado') + table(['Opção', 'Bico', 'Por que'], [
        ['<b>Recomendado</b>', '<b>Pitanga aberto (estrela aberta), médio</b><br>abertura de 8 a 10 mm, em inox', 'Faz a listra com frisos, igual à das fotos da casa (Lombinho). A listra fica com volume, não se espalha e é fácil ver se ficou igual às outras.'],
        ['Alternativa', 'Perlê liso (redondo), médio<br>abertura de 8 a 10 mm, em inox', 'Listra lisa e uniforme, mais fácil de lavar. Boa opção se a casa preferir o visual liso.'],
        ['Evitar', 'Bico fino (abaixo de 6 mm) ou ponta da bisnaga cortada a olho', 'Bico fino demora e a listra quebra; a ponta cortada muda de abertura a cada bisnaga e acaba com a padronização.'],
    ], widths=['16%', '34%', '50%']) + '<p class="note"><b>A bisnaga da casa é de ponta cortada e não aceita bico:</b> as opções estão no guia “Bico no catupiry” (recomendado: saco descartável com adaptador). A numeração dos bicos muda de fabricante para fabricante: compre pela <b>abertura em milímetros</b> e pelo desenho. Tenha 2 ou 3 bicos iguais, para trocar durante a limpeza, e faça o teste da seção 04 já com o bico escolhido.</p>'

reg = lambda t: f'<h3 class="sub">{t}</h3><div class="fill">' + table(['Nº', 'Data', 'Pizzaiolo', 'Pizza (sabor)', 'Nº de listras', 'Peso (g)', 'Pizza assada OK?'], [[str(i), '', '', '', '', '', ''] for i in range(1, 6)],
                                                                    widths=['6%', '13%', '20%', '21%', '13%', '12%', '15%']) + '</div>'
p4 = sec('06', 'Formulário do teste') + '<p class="note" style="margin:-1mm 0 1mm">Preencher durante o teste da seção 04, com o bico da seção 05. Peso lido na balança depois da tara, só do catupiry.</p>' \
    + reg('Grande · 8 fatias') + reg('Média · 5 fatias') + reg('Broto · 4 fatias') \
    + '<h3 class="sub">Padrão definido</h3><div class="std">' + ''.join(
        f'<div><h5>{t}</h5><p>Peso de referência: ______ g</p><p>Número de listras: ______</p><p>Bico: pitanga aberto ____ mm</p></div>' for t in ['Grande', 'Média', 'Broto']) + '</div>'

conf = table(['Semana', 'Tamanho', 'Pizza 1 (g)', 'Pizza 2 (g)', 'Pizza 3 (g)', 'Dentro do padrão?', 'Visto'], [[''] * 7 for _ in range(6)], widths=['14%', '14%', '13%', '13%', '13%', '19%', '14%'])
p5 = sec('07', 'Conferência semanal') + f'<div class="fill">{conf}</div>' + \
    '<p class="note">Sugestão de faixa aceitável: até 10% acima ou abaixo do peso de referência. Ajustar com a equipe depois das primeiras semanas.</p>' \
    + sec('08', 'Materiais') + table(['Item', 'Para que serve', 'Situação', 'Preço'], [
        ['Balança digital (1 g de precisão)', 'Tara e pesagem do catupiry', 'Já indicada no material de compras', 'cotar'],
        ['Bico pitanga aberto, 8 a 10 mm, inox (2 a 3 iguais)', 'Aplicar as listras sempre iguais', 'Comprar (ver seção 05)', 'cotar'],
        ['Saco descartável + adaptador', 'Usar o bico padrão com o catupiry da marca atual', 'A bisnaga atual não aceita bico: ver o guia “Bico no catupiry”', 'cotar'],
        ['Etiquetas', 'Identificar a bisnaga com a data de abertura do catupiry', 'Já em uso', '—'],
    ], widths=['30%', '32%', '26%', '12%']) + '<p class="note">Os preços não foram pesquisados: ficam em branco para cotação.</p>' \
    + sec('09', 'Cuidados de higiene') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        'Bisnaga e bico lavados e higienizados todo dia, e sempre que a bisnaga for reabastecida.',
        'Catupiry na geladeira; a bisnaga fica fora só durante a montagem.',
        'Não devolver a sobra da bisnaga para a embalagem original.',
        'Etiqueta na bisnaga com produto, data de abertura, validade e responsável (RDC 216/2004).']) + '</ul>' \
    + sec('10', 'Depois do teste') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        'Atualizar as fichas técnicas e as receitas de produção da <b>4 Queijos</b>, da <b>Frango com Catupiry</b> e da <b>Pizza de Lombinho</b> com o peso e o número de listras de cada tamanho.',
        'Treinar todos os pizzaiolos com o bico padrão e mostrar uma pizza modelo de cada tamanho.']) + '</ul>' \
    + '<div class="sign" style="margin-top:12mm"><div>Elaborado por</div><div>Responsável técnico</div><div>Aprovado por (Speciale)</div></div>'

subs = ['Por que medir e formas de medir', 'Recomendação e teste', 'Formulário do teste', 'Conferência, materiais e cuidados']
pages = [cover] + [page(DOC, s, i + 2, T, FOOT, c) for i, (s, c) in enumerate(zip(subs, [p2, p3, p4, p5]))]
open('guia_catupiry.html', 'w').write(html('Speciale · Como medir o catupiry', pages).replace('</head>', extra + '</head>'))
