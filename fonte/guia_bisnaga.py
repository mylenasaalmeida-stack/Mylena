from common import *

DOC = 'GUIA DE PADRONIZAÇÃO · BICO NO CATUPIRY'
FOOT = 'Speciale Pizzas Artesanais · Bico no catupiry: opções · Versão 1.0'
T = 5
DATA = '03/11/2026'

extra = '''<style>
.opt{border:1.5px solid var(--cream-ln);border-radius:6px;padding:3.5mm 4.5mm;margin-bottom:3.5mm;display:grid;grid-template-columns:13mm 1fr;gap:3mm}
.opt.best{border-color:var(--red);background:#fffaf6}
.opt .l{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:22pt;color:var(--red);line-height:1}
.opt h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:11pt}
.opt h4 em{font-style:normal;background:var(--red);color:#fff;font-size:7pt;padding:1px 6px;border-radius:3px;margin-left:6px;vertical-align:2px}
.opt p{font-size:8.3pt;margin-top:1mm}
.pc{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:1.5mm;font-size:7.9pt}
.pc b{display:block;font-family:'Roboto Condensed',sans-serif;font-size:8.5pt;text-transform:uppercase}
.pc .p b{color:#2b8a3e}.pc .c b{color:var(--red)}
.src{font-size:6.8pt;color:var(--muted);word-break:break-all;line-height:1.5}
.src li{margin:1mm 0}
</style>'''

cover = f'''<section class="page cover"><div class="chk top"></div>
<div class="in">{logo()}
<div class="tag">Guia de padronização</div>
<h1>Bico no<span>catupiry</span></h1>
<p class="lead">A bisnaga usada hoje é de ponta cortada, sem rosca para bico. Este guia mostra o que foi encontrado sobre marcas com bico de rosca e as opções para usar bico sem trocar a marca do catupiry.</p>
<div class="stats">
<div class="st"><b>Hoje</b><small>bisnaga de ponta cortada: a abertura muda a cada bisnaga</small></div>
<div class="st"><b>Objetivo</b><small>listra sempre igual, com o bico pitanga aberto de 8 a 10 mm</small></div>
<div class="st"><b>Recomendação</b><small>manter a marca e passar para saco descartável com adaptador e bico</small></div>
</div>
<div class="ver">Versão 1.0 · Novembro/2026</div>
</div><div class="chk bot"></div></section>'''

p2 = sec('01', 'Situação atual') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
    '<b>A casa usa a bisnaga do próprio fabricante</b>, aquela em que se corta a ponta para abrir. Ela não tem rosca nem encaixe para bico.',
    '<b>Cada corte sai diferente:</b> se a ponta é cortada mais alta ou mais baixa, a abertura muda, a listra muda e a quantidade de catupiry por pizza muda junto.',
    '<b>Para padronizar</b> (ver o guia “Como medir o catupiry”), a casa precisa aplicar sempre com o <b>mesmo bico</b>: o recomendado é o pitanga aberto, de 8 a 10 mm, em inox.',
]) + '</ul>' + sec('02', 'Marcas com bico de rosca: o que foi encontrado') + \
    f'<p style="margin-bottom:2.5mm"><b>Resultado da pesquisa ({DATA}):</b> não foi encontrada nenhuma fonte que confirme uma marca de catupiry ou requeijão em bisnaga de 1,5 kg com bico de rosca para encaixar bico de confeitar. Os anúncios de food service não informam o tipo de ponta. As marcas abaixo têm bisnaga de 1,5 kg para food service e são as que vale consultar com o distribuidor.</p>' + table(
    ['Marca', 'Produto encontrado', 'Bico com rosca?'], [
        ['Catupiry', 'Requeijão Tradicional e linha Profissional · bisnaga 1,5 kg', 'Não (ponta para cortar, conforme anúncio de atacado)'],
        ['Tirolez', 'Requeijão cremoso tradicional · bisnaga 1,5 kg', 'Não informado'],
        ['Scala', 'Requeijão cremoso Profissional · bisnaga 1,5 kg', 'Não informado'],
        ['Vigor', 'Requeijão cremoso culinário · bisnaga 1,5 kg', 'Não informado'],
        ['Select', 'Requeijão cremoso · bisnaga 1,5 kg', 'Não informado'],
        ['Hebrom', 'Requeijão cremoso uso culinário · bisnaga 1,5 kg', 'Não informado'],
        ['Ipanema · Valelac', 'Requeijão culinário · bisnaga 1,5 kg', 'Não informado'],
    ], widths=['18%', '50%', '32%']) + \
    '<p class="note">Trocar de marca muda o sabor, a textura no forno e o custo da pizza. Qualquer troca deve passar por teste de forno e aprovação da gerência.</p>' \
    + '<h3 class="sub">Perguntas para fazer ao distribuidor</h3><ul class="chk-l">' + ''.join(f'<li>{x}</li>' for x in [
        'A bisnaga tem bico com rosca? Aceita bico de confeitar ou adaptador?',
        'Qual é o diâmetro da saída da bisnaga?',
        'Validade fechada e depois de aberta, e temperatura de conservação.',
        'O produto resiste ao forno a lenha (340 a 380 °C) sem escorrer?',
        'Preço por bisnaga e por caixa, prazo de entrega em Recife.']) + '</ul>'

opts = [
    ('A', 'Saco de confeitar descartável + adaptador + bico', True,
     'Passar o catupiry da bisnaga para um saco de confeitar descartável com adaptador e o bico pitanga aberto. A bisnaga da marca atual continua sendo comprada; só muda a forma de aplicar.',
     'Mantém a marca · bico sempre igual · baixo custo · saco novo a cada abastecimento (mais higiênico)',
     'Uma etapa a mais (transferir) · o calor da mão amolece o catupiry no pico · gasto contínuo com sacos'),
    ('B', 'Bisnaga reutilizável com bico de rosca', False,
     'Comprar bisnagas plásticas vazias que aceitem bico de rosca e abastecer com o catupiry da marca atual.',
     'Mantém a marca · parecida com a bisnaga de hoje · não esquenta tanto na mão',
     'Não encontramos modelo confirmado para catupiry · precisa lavar e higienizar todo dia · difícil esvaziar por completo'),
    ('C', 'Aplicador de catupiry (equipamento com gatilho)', False,
     'Equipamento próprio para pizzaria, com gatilho e bico, vendido nas versões 1,8 kg e 0,9 kg, com refil em saquinhos.',
     'Feito para pizzaria · dose mais regular · menos desperdício, segundo o fabricante',
     'Investimento maior · o site não informa se aceita a bisnaga do catupiry atual · confirmar peças e assistência'),
    ('D', 'Cortar a ponta sempre no mesmo ponto (provisório)', False,
     'Enquanto não há bico, cortar a ponta da bisnaga sempre na mesma altura, com tesoura própria e uma marca de referência.',
     'Custo zero · pode começar hoje',
     'Não é bico: a listra continua lisa e a abertura ainda varia · serve só até a compra da opção A, B ou C'),
]
p3 = sec('03', 'Opções sem trocar a marca do catupiry') + ''.join(
    f'''<div class="opt{" best" if b else ""}"><span class="l">{l}</span><div><h4>{t}{"<em>RECOMENDADA</em>" if b else ""}</h4><p>{d}</p>
<div class="pc"><div class="p"><b>A favor</b>{pr}</div><div class="c"><b>Contra</b>{co}</div></div></div></div>''' for l, t, b, d, pr, co in opts)

p4 = sec('04', 'Recomendação e como fazer') + '<p style="margin-bottom:2mm"><b>Opção A: manter a marca atual e aplicar com saco descartável, adaptador e bico pitanga aberto.</b> É a forma mais barata e rápida de ter o bico padrão sem mudar o catupiry. Se depois de algumas semanas a equipe achar o saco pouco prático no pico, vale avaliar o aplicador (opção C).</p>' \
    + '<div class="steps">' + ''.join(f'<div class="s"><span class="i">{i:02d}</span><p>{t}</p></div>' for i, t in enumerate([
        '<b>Lavar as mãos</b> e higienizar a bancada, o adaptador e o bico.',
        '<b>Montar o saco:</b> cortar a ponta do saco descartável, encaixar o adaptador por dentro e rosquear o bico por fora.',
        '<b>Abrir a bisnaga do catupiry</b> e passar para o saco só a quantidade do turno (ou parte dele), sem encher demais.',
        '<b>Fechar o saco</b> torcendo a parte de cima e <b>etiquetar</b>: produto, data e hora, validade e responsável.',
        '<b>Guardar na geladeira</b> entre os usos; na bancada, só durante a montagem.',
        '<b>No fim do turno</b>, descartar o saco com a sobra (não devolver para a bisnaga) e lavar adaptador e bico.',
        '<b>Fazer o teste de pesagem</b> do guia “Como medir o catupiry” já com o bico escolhido.',
    ], 1)) + '</div>' \
    + sec('05', 'Cuidados de higiene') + '<ul class="dot">' + ''.join(f'<li>{x}</li>' for x in [
        'Passar o catupiry de uma embalagem para outra é manipulação: mãos limpas, utensílios higienizados e etiqueta no saco (RDC 216/2004).',
        'Usar sacos descartáveis próprios para alimentos; não reaproveitar o saco de um dia para o outro.',
        'Ter 2 ou 3 adaptadores e bicos iguais, para trocar enquanto os outros estão na lavagem.',
        'Bisnaga aberta: manter a ponta limpa e fechada e seguir a validade depois de aberta indicada no rótulo.']) + '</ul>'

p5 = sec('06', 'Lista de compras') + table(['Item', 'Quantidade sugerida', 'Preço encontrado', 'Observação'], [
    ['Bico pitanga aberto, 8 a 10 mm, inox', '2 a 3 iguais', 'cotar', 'Comprar pelo desenho e pela abertura em mm'],
    ['Adaptador para bico de confeitar', '2 a 3', 'cotar', 'Confirmar se o bico escolhido encaixa no adaptador'],
    ['Saco de confeitar descartável', 'Para 1 a 2 meses de uso', 'cotar', 'Próprio para alimentos; tamanho médio ou grande'],
    ['Kit Mago (3 adaptadores + 2 sacos)', 'Opcional', f'R$ 39,90 (R$ 28,05 no Pix) · Magazine Luiza · {DATA}', 'Não vem bico; os sacos do kit parecem reutilizáveis'],
    ['Aplicador de catupiry 1,8 kg (opção C)', 'Se escolhida', f'R$ 780,00 · site do fabricante · {DATA}', 'Confirmar se aceita a bisnaga atual'],
    ['Aplicador de catupiry 0,9 kg (opção C)', 'Se escolhida', f'R$ 635,00 · site do fabricante · {DATA}', 'Versão menor'],
], widths=['28%', '16%', '28%', '28%']) + \
    f'<p class="note">Preços consultados na internet em {DATA}, sem confirmação de estoque ou frete; podem mudar. Itens sem preço confirmado ficam como “cotar”.</p>' \
    + sec('07', 'Decisão da gerência') + '<div class="std" style="display:grid;grid-template-columns:repeat(3,1fr);gap:4mm">' + ''.join(
        f'<div style="border:1.5px solid var(--red);border-radius:6px;padding:3mm 4mm;font-size:8.4pt"><b>{t}</b><p style="margin-top:2mm">☐ Sim &nbsp; ☐ Não</p></div>' for t in [
            'Manter a marca atual do catupiry?', 'Adotar a opção A (saco + adaptador + bico)?', 'Avaliar o aplicador (opção C)?']) + '</div>' \
    + '<h3 class="sub">Fontes consultadas</h3><ul class="src">' + ''.join(f'<li>{x}</li>' for x in [
        'Catupiry Tradicional bisnaga 1,5 kg (ponta para cortar): tendaatacado.com.br/produto/requeijao-cremoso-catupiry-tradicional-1-5kg-8772',
        'Tirolez bisnaga 1,5 kg: tendaatacado.com.br/produto/requeijao-crem-tirolez-trad-bisnag-1-5kg',
        'Scala Profissional bisnaga 1,5 kg: kurodaemcasa.com.br/p/Requeijao-Cremoso-Scala-Profissional-Bisnaga-1-5kg',
        'Vigor culinário bisnaga 1,5 kg: praso.com.br/products/requeijao-culinario-vigor-1-5kg',
        'Select bisnaga 1,5 kg: tendaatacado.com.br/produto/requeijao-cremoso-select-1-5kg-24115',
        'Hebrom bisnaga 1,5 kg: mma-distribuidora.dooca.store/requeijao-cremoso-uso-culinario-15kg-bisnaga-hebrom-food-service',
        'Kit Mago 3 adaptadores + 2 sacos: magazineluiza.com.br/marcas/mago',
        'Aplicador de catupiry: aplicadordecatupiry.com.br']) + '</ul>' \
    + '<div class="sign" style="margin-top:8mm"><div>Elaborado por</div><div>Gerente</div><div>Aprovado por (Speciale)</div></div>'

subs = ['Situação e marcas', 'Opções sem trocar a marca', 'Recomendação e higiene', 'Compras e decisão']
pages = [cover] + [page(DOC, s, i + 2, T, FOOT, c) for i, (s, c) in enumerate(zip(subs, [p2, p3, p4, p5]))]
open('guia_bisnaga.html', 'w').write(html('Speciale · Bico no catupiry', pages).replace('</head>', extra + '</head>'))
