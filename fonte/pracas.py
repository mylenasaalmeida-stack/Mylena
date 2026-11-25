"""Divisão da equipe por praça e termo de responsabilidade · Speciale."""
from common import *

D, F, T = 'EQUIPE · DIVISÃO POR PRAÇA', 'Speciale Pizzas Artesanais · Divisão por praça e responsabilidades · RDC ANVISA 216/2004', 6
B = '<span class="blank" style="min-width:34mm"></span>'
EXTRA = '''<style>
.fill td{height:8.5mm}
.pc{display:grid;grid-template-columns:repeat(2,1fr);gap:4mm}
.pc .c{border:1px solid var(--cream-ln);border-radius:6px;overflow:hidden;break-inside:avoid}
.pc .h{background:var(--red);color:#fff;padding:2mm 3.5mm;display:flex;justify-content:space-between;align-items:center}
.pc .h b{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:10.5pt}
.pc .h span{font-size:6.8pt;opacity:.9}
.pc .b{padding:2.5mm 3.5mm;font-size:7.6pt;line-height:1.45;background:#fff}
.pc .b ul{padding-left:3.6mm;margin:1mm 0}
.pc .r{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin-top:2mm;font-size:7pt;color:#555}
.pc .r div{border-bottom:1px solid #999;padding-bottom:4mm}
.org{display:flex;flex-direction:column;align-items:center;gap:3mm}
.org .lv{display:flex;gap:3mm;justify-content:center;flex-wrap:wrap}
.org .bx{border:1.5px solid var(--red);border-radius:5px;padding:2mm 3mm;text-align:center;font-size:7.6pt;min-width:30mm;background:#fff}
.org .bx b{display:block;font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:9pt}
.org .bx.top{background:var(--red);color:#fff}
.org .bx.sup{background:var(--cream)}
.org .ln{width:1.5px;height:4mm;background:var(--red)}
.term{font-size:8.6pt;line-height:1.6;text-align:justify}
</style>'''

PR = [
    ('Massa', 'Produção', 'Masseira, balança, bandejas', ['Pesar e bater a massa conforme a receita de produção.', 'Dividir, bolear, etiquetar e armazenar.', 'Higienizar masseira e balança após o uso.'], 'POP 01 · Receita da massa'),
    ('Pré-preparo', 'Produção', 'Facas, tábuas, potes, geladeira', ['Preparar molho, frango, cortes e queijos.', 'Porcionar e etiquetar (produto, data, validade).', 'Manter crus separados dos prontos.'], 'POP 01 · Fichas técnicas'),
    ('Montagem', 'Produção', 'Bancada, bisnagas, balança', ['Abrir a massa e montar conforme a ficha técnica.', 'Bancada só com o que vai para a pizza.', 'Higienizar bancada, bisnaga e bico.'], 'Fichas técnicas · POP 04'),
    ('Forno', 'Produção', 'Forno a lenha, pá, cortador', ['Manter o forno no ponto (340 a 380 °C).', 'Assar 3 a 4 min e conferir o ponto.', 'Limpar pá, cortador e cinzas com o forno frio.'], 'POP 01'),
    ('Expedição', 'Saída', 'Caixas, bag térmica', ['Cortar, embalar e fechar a caixa na hora.', 'Conferir pedido, tamanho e sabor.', 'Manter a bag térmica limpa por dentro.'], 'POP 04'),
    ('Atendimento e caixa', 'Salão', 'Caixa, salão, cardápio', ['Receber pedidos e cobrar.', 'Não tocar em alimentos depois de manusear dinheiro sem lavar as mãos.', 'Limpar mesas e cardápios.'], 'POP 01 · POP 04'),
    ('Estoque e recebimento', 'Apoio', 'Estoque seco, geladeiras, freezer', ['Conferir entregas: validade, temperatura, embalagem.', 'Organizar por PVPS, nada no chão.', 'Anotar temperaturas 2 vezes ao dia.'], 'Planilha de temperatura'),
    ('Higienização', 'Apoio', 'Pia de louça, piso, lixeiras', ['Lavar louças e utensílios.', 'Limpeza diária de piso, ralos e lixeiras.', 'Retirar o lixo e registrar na planilha.'], 'POP 01 · POP 02'),
]

cover = f'''<section class="page cover"><div class="chk top"></div><div class="in">{logo()}
<div class="tag">Organização da equipe</div><h1>Cada um<span>na sua praça</span></h1>
<p class="lead">Divisão da equipe por praça, supervisores por turno e termo de responsabilidade assinado por quem responde por cada etapa, da massa à higienização.</p>
<div class="stats"><div class="st"><b>8 praças</b><small>da produção da massa ao lixo</small></div>
<div class="st"><b>1 supervisor</b><small>por turno, que confere as planilhas</small></div>
<div class="st"><b>Assinado</b><small>cada responsável assina a sua etapa</small></div></div>
<div class="ver">Versão 1.0 · Novembro/2026</div></div><div class="chk bot"></div></section>'''

org = '''<div class="org">
<div class="lv"><div class="bx top"><b>Proprietária</b>Speciale</div></div><div class="ln"></div>
<div class="lv"><div class="bx sup"><b>Responsável pelas boas práticas</b>RDC 216 · item 4.12</div></div><div class="ln"></div>
<div class="lv"><div class="bx sup"><b>Supervisor · turno 1</b>______________</div><div class="bx sup"><b>Supervisor · turno 2</b>______________</div></div><div class="ln"></div>
<div class="lv">''' + ''.join(f'<div class="bx"><b>{n}</b>{a}</div>' for n, a, *_ in PR) + '</div></div>'
p1 = sec('01', 'Organograma') + org + sec('02', 'Papéis') + table(['Papel', 'O que faz', 'Quem'], [
    ['<b>Responsável pelas boas práticas</b>', 'Responde pela aplicação das boas práticas (RDC 216, item 4.12): treinamento, POPs, planilhas. Deve ser capacitado em Boas Práticas.', B],
    ['<b>Supervisor de turno</b>', 'Confere a entrada da equipe (uniforme, saúde), as planilhas do turno e corrige na hora o que estiver fora do padrão.', B],
    ['<b>Responsável da praça</b>', 'Executa e registra as tarefas da sua praça; avisa o supervisor de qualquer problema.', 'Ver página 3'],
    ['<b>Substituto</b>', 'Assume a praça na folga ou falta do titular, com o mesmo treinamento.', 'Ver página 3'],
], widths=['26%', '54%', '20%'])

cards = ''.join(f'''<div class="c"><div class="h"><b>{n}</b><span>{a} · {eq}</span></div><div class="b">
<ul>{''.join(f'<li>{x}</li>' for x in tarefas)}</ul><div style="color:#666">Segue: {ref}</div>
<div class="r"><div>Responsável</div><div>Substituto</div></div></div></div>''' for n, a, eq, tarefas, ref in PR)
p2 = sec('03', 'Praças, tarefas e responsáveis') + f'<div class="pc">{cards}</div>'

p3 = sec('04', 'Quadro de responsáveis') + '<div class="fill">' + table(['Praça', 'Responsável', 'Substituto', 'Turno', 'Supervisor'], [[f'<b>{n}</b>', '', '', '', ''] for n, *_ in PR], widths=['24%', '22%', '22%', '12%', '20%']) + '</div>' + \
    sec('05', 'Equipamentos: quem higieniza') + '<div class="fill">' + table(['Equipamento', 'Frequência', 'Responsável', 'Registro'], [
        ['<b>Masseira</b>', 'Após cada uso', '', 'Planilha de higienização'],
        ['<b>Balança</b>', 'Após cada uso', '', 'Planilha de higienização'],
        ['<b>Geladeiras e freezer</b>', 'Semanal (externa diária)', '', 'Planilha de higienização'],
        ['<b>Forno a lenha e pá</b>', 'Diária', '', 'Planilha de higienização'],
        ['<b>Bancadas</b>', 'Entre tarefas e fim do turno', '', 'Planilha de higienização'],
        ['<b>Bisnagas e bicos</b>', 'Fim do turno', '', 'Planilha de higienização'],
        ['<b>Coifa e luminárias</b>', 'Mensal', '', 'Planilha de higienização'],
        ['<b>Caixa d\'água e filtro</b>', 'A cada 6 meses / fabricante', '', 'Planilha do reservatório'],
    ], widths=['26%', '26%', '24%', '24%']) + '</div>'

rot = ''.join(f'<th style="text-align:center">{d}</th>' for d in ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'])
p4 = sec('06', 'Escala semanal') + '<p class="note" style="margin:-1mm 0 2mm">Escrever o nome de quem fica em cada praça no dia. Semana de ___/___ a ___/___.</p><table class="fill"><thead><tr><th>Praça</th>' + rot + '</tr></thead><tbody>' + \
    ''.join(f'<tr><td style="font-size:8pt"><b>{n}</b></td>' + '<td></td>' * 7 + '</tr>' for n, *_ in PR) + '<tr><td style="font-size:8pt"><b>Supervisor</b></td>' + '<td></td>' * 7 + '</tr></tbody></table>' + \
    sec('07', 'Rotina do supervisor') + table(['Quando', 'O que conferir'], [
        ['<b>Abertura</b>', 'Equipe com uniforme, touca, sem adornos e sem sintomas · temperatura de geladeira e freezer · bancadas higienizadas · massa e insumos dentro da validade.'],
        ['<b>Durante o turno</b>', 'Lavagem das mãos nas trocas de tarefa · crus separados dos prontos · porções conforme ficha técnica · lixeiras tampadas.'],
        ['<b>Fechamento</b>', 'Higienização das praças e equipamentos · temperatura · lixo retirado · planilhas preenchidas e rubricadas.'],
        ['<b>Semanal</b>', 'Revisar planilhas com o responsável pelas boas práticas e registrar ocorrências.']], widths=['18%', '82%'])

term = '''<div class="term"><p>Eu, ______________________________________, função ____________________, declaro que recebi o treinamento em Boas Práticas de Manipulação de Alimentos (RDC ANVISA 216/2004) e os POPs da Speciale Pizzas Artesanais, e que assumo a responsabilidade pela execução e pelo registro das tarefas da(s) praça(s) abaixo, seguindo os procedimentos da casa e comunicando ao supervisor qualquer problema.</p></div>'''
p5 = sec('08', 'Termo de responsabilidade por praça') + term + '<div class="fill">' + table(['Praça', 'Desde', 'Assinatura do responsável', 'Assinatura do supervisor'], [[f'<b>{n}</b>', '___/___/___', '', ''] for n, *_ in PR], widths=['24%', '14%', '31%', '31%']) + '</div>' + \
    '<p class="note">Uma folha por funcionário, ou uma linha por praça para cada responsável. Arquivar junto com os registros de treinamento. Revisar quando houver troca de função.</p>' + \
    '<div class="sign" style="margin-top:10mm"><div>Responsável pelas boas práticas</div><div>Supervisor(es)</div><div>Proprietária (Speciale)</div></div>'

subs = ['Organograma e papéis', 'Praças e tarefas', 'Responsáveis e equipamentos', 'Escala e supervisão', 'Termo de responsabilidade']
pages = [cover] + [page(D, s, i + 2, T, F, c) for i, (s, c) in enumerate(zip(subs, [p1, p2, p3, p4, p5]))]
open('pracas.html', 'w').write(html('Speciale · Divisão por praça', pages).replace('</head>', EXTRA + '</head>'))
