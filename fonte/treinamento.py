"""Pacote de treinamento em Boas Práticas · Speciale (RDC ANVISA 216/2004)."""
from common import *

AC_ = '<span class="tbc">a confirmar</span>'
LN = '<span class="blank" style="min-width:60mm"></span>'
EXTRA = '''<style>
.ag td{font-size:8.2pt}
.q{counter-reset:q}.q li{list-style:none;position:relative;padding:2mm 0 2mm 8mm;border-bottom:1px dotted #cbbfb3;font-size:8.6pt}
.q li:before{counter-increment:q;content:counter(q);position:absolute;left:0;top:2mm;font-family:'Roboto Condensed';font-weight:800;color:var(--red)}
.q .o{display:flex;gap:6mm;margin-top:1mm;font-size:8.2pt;color:#444}
.fill td{height:8mm}
.big{font-family:'Roboto Condensed';font-weight:800;color:var(--red);font-size:20pt;line-height:1}
.two{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.card{background:var(--cream);border-radius:6px;padding:3.5mm 4mm;border-top:3px solid var(--red)}
.card h4{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:10pt;margin-bottom:1.5mm}
.card ul{padding-left:4mm;font-size:8pt;line-height:1.5}
</style>'''


def doc(fname, title, pages):
    open(fname, 'w').write(html(title, pages).replace('</head>', EXTRA + '</head>'))


def cover(tag, t1, t2, lead, stats, ver='Versão 1.0 · Novembro/2026'):
    st = ''.join(f'<div class="st"><b>{a}</b><small>{b}</small></div>' for a, b in stats)
    return f'''<section class="page cover"><div class="chk top"></div><div class="in">{logo()}
<div class="tag">{tag}</div><h1>{t1}<span>{t2}</span></h1><p class="lead">{lead}</p>
<div class="stats">{st}</div><div class="ver">{ver}</div></div><div class="chk bot"></div></section>'''


def ul(xs, cls='dot'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'


# =================== 1. ROTEIRO DO TREINAMENTO ===================
D1, F1, T1 = 'TREINAMENTO · BOAS PRÁTICAS', 'Speciale Pizzas Artesanais · Capacitação interna em Boas Práticas · RDC 216/2004', 6
r1 = cover('Capacitação da equipe', 'Boas práticas', 'na Speciale',
           'Roteiro do treinamento da equipe operacional: o que abordar, como conduzir, dinâmicas, avaliação e registro de presença.',
           [('2 h', 'duração sugerida, com prática na cozinha'), ('8 temas', 'do uniforme ao forno, ligados à rotina da casa'), ('RDC 216', 'ANVISA · Boas Práticas para Serviços de Alimentação')])

agenda = [('0:00', '10 min', 'Abertura', 'Por que boas práticas: segurança do cliente, qualidade da pizza e fiscalização da Vigilância Sanitária.', 'Conversa'),
          ('0:10', '15 min', '1. Higiene pessoal', 'Uniforme, touca, sem adornos, unhas, saúde e afastamento.', 'Checagem em dupla'),
          ('0:25', '15 min', '2. Lavagem das mãos', 'Quando e como lavar (passo a passo de 40 a 60 s).', 'Prática com tinta guache'),
          ('0:40', '15 min', '3. Contaminação cruzada', 'Cru x pronto, tábuas e utensílios, bancada, pano, bisnaga e sacos.', 'Caça aos erros (fotos)'),
          ('0:55', '15 min', '4. Temperaturas', 'Geladeira até 5 °C, freezer −18 °C, descongelar na geladeira, cocção 70 °C, forno.', 'Leitura do termômetro'),
          ('1:10', '10 min', '5. Armazenamento e validade', 'Etiqueta, PVPS, nada no chão, validade após aberto e preparado.', 'Etiquetar 3 produtos'),
          ('1:20', '15 min', '6. Higienização', 'Limpeza x desinfecção, diluição, frequência, panos e escovas.', 'Diluir e aplicar'),
          ('1:35', '10 min', '7. Lixo, pragas e água', 'Lixeira com tampa e pedal, retirada, sinais de pragas, filtro e caixa d\'água.', 'Ronda pela área'),
          ('1:45', '15 min', 'Fechamento', 'Avaliação, dúvidas, combinados da casa e assinatura da lista de presença.', 'Avaliação escrita')]
p1 = sec('01', 'Objetivo e formato') + ul([
    '<b>Objetivo:</b> garantir que toda a equipe saiba manipular, armazenar e servir os alimentos com segurança, conforme a RDC ANVISA 216/2004, e conheça os POPs da casa.',
    '<b>Público:</b> pizzaiolos, auxiliares de cozinha, atendentes e entregadores que tocam em alimentos.',
    '<b>Formato:</b> conversa curta + demonstração na cozinha + prática. Usar os exemplos da Speciale (massa, molho, catupiry, forno a lenha).',
    '<b>Materiais:</b> cartilha impressa (1 por pessoa), adesivos, termômetro, guache ou tinta lavável, venda para os olhos, etiquetas, produtos de limpeza, lista de presença.',
    '<b>Periodicidade:</b> repetir a cada 6 meses e sempre que entrar alguém novo (a RDC exige capacitação periódica e registrada).']) + \
    sec('02', 'Agenda (2 horas)') + '<div class="ag">' + table(['Início', 'Tempo', 'Tema', 'O que abordar', 'Dinâmica'], agenda, widths=['9%', '9%', '20%', '44%', '18%']) + '</div>'

temas = [('Higiene pessoal', ['Uniforme limpo, trocado todo dia e usado só no trabalho.', 'Cabelo preso e com touca; barba feita.', 'Sem anel, aliança, brinco, relógio, pulseira, piercing; unhas curtas, limpas, sem esmalte.', 'Não fumar, comer, mascar chiclete, tossir ou espirrar sobre os alimentos; não mexer no celular na bancada.', 'Com diarreia, febre, vômito, ferida ou corte infeccionado: avisar e não manipular alimentos.']),
         ('Lavagem das mãos', ['Ao chegar, ao voltar do banheiro, ao trocar de tarefa, depois de tocar em cru, lixo, dinheiro, celular, rosto ou cabelo, depois de tossir ou espirrar.', 'Lavatório exclusivo, sabonete líquido, papel toalha e lixeira com pedal.', 'Passo a passo de 40 a 60 segundos (adesivo na pia).', 'Luva não substitui a lavagem: lavar antes de calçar e trocar a cada tarefa.']),
         ('Contaminação cruzada', ['Separar cru (frango, ovo, carnes) de pronto (queijos, presunto, molho).', 'Tábuas, facas e potes separados ou higienizados entre usos.', 'Pano de prato não serve para tudo: usar papel toalha ou pano exclusivo e trocado.', 'Bisnaga e bico de catupiry higienizados; saco de confeitar descartado no fim do turno.', 'Na bancada, só o que vai para a pizza agora.']),
         ('Temperaturas', ['Geladeira até 5 °C; freezer a −18 °C ou menos (conferir e anotar 2 vezes ao dia).', 'Descongelar dentro da geladeira, nunca na bancada ou na pia; não recongelar.', 'Alimento cozido (como o frango) atinge pelo menos 70 °C em todas as partes.', 'Alimento quente mantido a 60 °C ou mais por até 6 h; alimento preparado e refrigerado até 5 °C dura no máximo 5 dias.', 'Resfriar rápido: de 60 °C a 10 °C em até 2 h, em recipientes rasos.']),
         ('Armazenamento e validade', ['Nada direto no chão: estrados ou prateleiras a 25 cm do piso.', 'Etiqueta em tudo que é aberto, porcionado ou preparado: produto, data, validade, responsável.', 'PVPS: primeiro que vence, primeiro que sai.', 'Crus embaixo, prontos em cima na geladeira; tudo tampado.', 'Produtos de limpeza longe dos alimentos.']),
         ('Higienização', ['Limpar (tirar a sujeira) e depois desinfetar (matar os micróbios).', 'Usar só produtos regularizados na ANVISA e diluir conforme o rótulo.', 'Bancada e utensílios: a cada troca de tarefa e no fim do turno.', 'Escovas e esponjas trocadas com frequência; panos de limpeza separados por área.', 'Seguir o POP 01 e anotar na planilha.'])]
p2 = sec('03', 'Pontos a abordar em cada tema') + '<div class="two">' + ''.join(
    f'<div class="card"><h4>{t}</h4>{ul(xs)}</div>' for t, xs in temas) + '</div>'

din = [('Tinta nas mãos (guache)', 'Com olhos vendados, a pessoa “lava” as mãos com guache. Ao abrir, todos veem onde a lavagem falhou (entre os dedos, polegar, unhas). Depois, lavar de verdade seguindo o adesivo.'),
       ('Caça aos erros', 'Mostrar a bancada montada com 6 erros de propósito: pano sujo, pote sem etiqueta, cru ao lado de pronto, celular na bancada, bisnaga aberta, lixeira destampada. Quem achar mais, ganha.'),
       ('Leitura do termômetro', 'Cada um mede a geladeira e o freezer e anota na planilha. Combinar o que fazer se estiver acima de 5 °C.'),
       ('Etiquetar 3 produtos', 'Molho, catupiry aberto e queijo picado: cada pessoa preenche uma etiqueta completa.'),
       ('Diluir e aplicar', 'Preparar a solução de limpeza seguindo o rótulo e higienizar uma bancada na sequência certa.')]
p3 = sec('04', 'Dinâmicas') + table(['Dinâmica', 'Como fazer'], din, widths=['26%', '74%']) + \
    sec('05', 'Combinados da Speciale (fechamento)') + ul([
        'Massa: etiquetada, coberta e dentro da validade definida pela casa (validade e local a confirmar: geladeira ou freezer).',
        'Molho e catupiry: sempre com concha ou bisnaga limpa; sobra nunca volta para a embalagem original.',
        'Geladeira e freezer conferidos e anotados na abertura e no fechamento.',
        'Bancada limpa a cada pizza montada e higienizada no fim do turno.',
        'Pá e cortador limpos; caixa de pizza fechada na hora.',
        'Quem estiver doente avisa antes de entrar na cozinha.']) + \
    '<div class="box"><h5>Documentos da casa que a equipe precisa conhecer</h5>' + ul([
        'Manual de Boas Práticas (a elaborar ou confirmar se existe).',
        'Os 4 POPs obrigatórios (entregues neste pacote): higienização, pragas, caixa d\'água e higiene dos manipuladores.',
        'Fichas técnicas e receitas de produção das pizzas.',
        'Planilhas de registro: temperatura, higienização e treinamento.']) + '</div>'

quiz = [('Qual é a temperatura máxima da geladeira?', ['5 °C', '10 °C', '15 °C']),
        ('Onde a massa congelada deve ser descongelada?', ['Na bancada', 'Na pia com água', 'Dentro da geladeira']),
        ('Por quanto tempo, no mínimo, devemos lavar as mãos?', ['10 segundos', '40 a 60 segundos', '2 minutos']),
        ('Usar luva dispensa lavar as mãos?', ['Sim', 'Não']),
        ('O que a etiqueta de um produto aberto precisa ter?', ['Só o nome', 'Produto, data, validade e responsável', 'Só a validade']),
        ('O que significa PVPS?', ['Primeiro que vence, primeiro que sai', 'Pedido vem, pizza sai', 'Pesar, validar, porcionar, servir']),
        ('Com diarreia ou febre, o que fazer?', ['Trabalhar de luva', 'Avisar e não manipular alimentos', 'Tomar remédio e seguir']),
        ('Qual a ordem certa da higienização?', ['Desinfetar e depois limpar', 'Limpar e depois desinfetar', 'Só passar pano']),
        ('A sobra do catupiry do saco pode voltar para a embalagem?', ['Sim', 'Não']),
        ('Qual a temperatura mínima para cozinhar o frango por completo?', ['50 °C', '60 °C', '70 °C'])]
qhtml = '<ol class="q">' + ''.join(f'<li><b>{t}</b><div class="o">' + ''.join(f'<span>☐ {o}</span>' for o in os_) + '</div></li>' for t, os_ in quiz) + '</ol>'
p4 = sec('06', 'Avaliação rápida') + '<p class="note" style="margin:-1mm 0 2mm">Nome: ______________________________ Função: ______________ Data: ___/___/____</p>' + qhtml + \
    '<p class="note">Gabarito (para o instrutor): 1-5 °C · 2-geladeira · 3-40 a 60 s · 4-não · 5-produto, data, validade e responsável · 6-primeiro que vence · 7-avisar · 8-limpar e depois desinfetar · 9-não · 10-70 °C. Acerto mínimo sugerido: 8 de 10; abaixo disso, repassar o tema com a pessoa.</p>'

pres = table(['Nº', 'Nome completo', 'Função', 'Nota', 'Assinatura'], [[str(i), '', '', '', ''] for i in range(1, 13)], widths=['6%', '38%', '18%', '8%', '30%'])
p5 = sec('07', 'Registro de capacitação') + table(['Campo', 'Informação'], [
    ['Tema', 'Boas Práticas de Manipulação de Alimentos (RDC ANVISA 216/2004) e POPs da casa'],
    ['Data e horário', '___/___/____ · das ____ às ____'], ['Carga horária', '2 horas'],
    ['Local', 'Speciale Pizzas Artesanais · Recife'], ['Instrutor(a)', LN], ['Conteúdo', 'Higiene pessoal, lavagem das mãos, contaminação cruzada, temperaturas, armazenamento e validade, higienização, lixo, pragas e água']],
    widths=['22%', '78%']) + '<h3 class="sub">Lista de presença</h3><div class="fill">' + pres + '</div>' + \
    '<div class="sign" style="margin-top:12mm"><div>Instrutor(a)</div><div>Responsável pelas atividades de manipulação</div><div>Proprietária (Speciale)</div></div>'

subs1 = ['Objetivo e agenda', 'Pontos a abordar', 'Dinâmicas e combinados', 'Avaliação', 'Registro e presença']
doc('trein_roteiro.html', 'Speciale · Treinamento em Boas Práticas', [r1] + [page(D1, s, i + 2, T1, F1, c) for i, (s, c) in enumerate(zip(subs1, [p1, p2, p3, p4, p5]))])

# =================== 2. POPs ===================
D2, F2, T2 = 'POPs · PROCEDIMENTOS OPERACIONAIS PADRONIZADOS', 'Speciale Pizzas Artesanais · POPs exigidos pela RDC ANVISA 216/2004 (item 4.11)', 8
r2 = cover('Procedimentos Operacionais Padronizados', 'Os 4 POPs', 'da Speciale',
           'Os quatro POPs exigidos pela RDC 216/2004 para serviços de alimentação, já adaptados à pizzaria, com as planilhas de registro.',
           [('4 POPs', 'obrigatórios pela RDC 216/2004'), ('Registro', 'planilhas para monitorar e verificar'), ('Revisar', 'a cada ano ou quando algo mudar')])


def pop(num, titulo, campos, procedimento, monit, acao, verif):
    head = table(['Campo', 'Informação'], [['POP nº', f'{num:02d}'], ['Título', titulo]] + campos + [
        ['Elaborado em', 'Novembro/2026 · versão 1.0'], ['Responsável', LN]], widths=['24%', '76%'])
    return (sec(f'{num:02d}', titulo) + head + '<h3 class="sub">Procedimento</h3>' + procedimento +
            '<h3 class="sub">Monitoramento, ação corretiva e verificação</h3>' +
            table(['Etapa', 'Como fazer'], [['Monitoramento', monit], ['Ação corretiva', acao], ['Verificação', verif]], widths=['22%', '78%']))


pop1 = pop(1, 'Higienização de instalações, equipamentos e móveis',
           [['Objetivo', 'Manter piso, paredes, bancadas, equipamentos e utensílios limpos e desinfetados, evitando contaminação dos alimentos.'],
            ['Aplica-se a', 'Toda a área de produção, estoque, salão e banheiros.']],
           table(['O quê', 'Frequência', 'Como', 'Produto'], [
               ['Bancadas e mesa de abrir massa', 'Entre tarefas e no fim do turno', 'Retirar resíduos → lavar com detergente → enxaguar → desinfetar → secar ao natural', 'Detergente neutro + desinfetante (solução clorada ou álcool 70%)'],
               ['Utensílios (facas, tábuas, colheres, bisnagas, bicos, potes)', 'Após cada uso', 'Lavar, enxaguar, desinfetar, secar e guardar protegidos', 'Detergente + desinfetante'],
               ['Masseira e balança', 'Após cada uso', 'Desligar da tomada, retirar resíduos, lavar partes removíveis, desinfetar', 'Detergente + álcool 70%'],
               ['Geladeiras e freezer', 'Semanal (externa diária)', 'Esvaziar, lavar com detergente, enxaguar, desinfetar, secar', 'Detergente + desinfetante'],
               ['Forno a lenha (boca e pá)', 'Diária', 'Retirar cinzas com o forno frio; escovar a pá; limpar a área em volta', 'Escova própria'],
               ['Piso e ralos', 'Diária e quando sujar', 'Varrer úmido, lavar com detergente, desinfetar, puxar com rodo', 'Detergente + solução clorada'],
               ['Paredes, portas e janelas', 'Semanal', 'Lavar com detergente, enxaguar e desinfetar', 'Detergente + desinfetante'],
               ['Lixeiras', 'Diária', 'Esvaziar, lavar, desinfetar e trocar o saco', 'Detergente + solução clorada'],
               ['Teto, luminárias e coifa', 'Mensal', 'Retirar pó e gordura', 'Desengordurante'],
           ], widths=['22%', '16%', '38%', '24%']) +
           '<p class="note">Usar somente produtos regularizados na ANVISA, diluídos conforme o rótulo do fabricante (referência usual: solução clorada a 200 ppm por 10 minutos de contato, ou álcool 70%; confirmar no rótulo). Produtos guardados longe dos alimentos. Panos e escovas exclusivos por área. Não usar escova de aço nem varrer a seco na produção.</p>',
           'Quem faz a limpeza anota na Planilha de Higienização (data, área, horário, rubrica).',
           'Área ou equipamento sujo: refazer a higienização na hora e reorientar o responsável.',
           'O responsável pelas atividades de manipulação confere a planilha toda semana e assina.')

pop2 = pop(2, 'Controle integrado de vetores e pragas urbanas',
           [['Objetivo', 'Impedir a entrada, o abrigo e a proliferação de baratas, ratos, moscas e formigas.'],
            ['Aplica-se a', 'Todo o estabelecimento, incluindo área externa e depósito.']],
           '<h3 class="sub" style="margin-top:0">Medidas preventivas (equipe)</h3>' + ul([
               'Portas e janelas com tela milimétrica; ralos sifonados e fechados; portas com vedação na parte de baixo.',
               'Alimentos tampados, fora do chão e sem restos sobre as bancadas.',
               'Lixo em lixeira com tampa e pedal, retirado sempre que necessário e no fim do expediente.',
               'Caixas de papelão do fornecedor retiradas e descartadas antes de entrar no estoque.',
               'Não deixar água parada, nem materiais sem uso acumulados.']) +
           '<h3 class="sub">Controle químico (empresa especializada)</h3>' + ul([
               f'Feito somente por empresa especializada e licenciada. Empresa: {AC_}. Frequência: {AC_} (definida pela empresa).',
               'No dia da aplicação, retirar ou proteger alimentos e utensílios e seguir as orientações da empresa.',
               'Guardar o comprovante de execução do serviço (com produtos usados) junto a este POP.']),
           'Equipe registra qualquer sinal de praga (fezes, roedura, insetos) no caderno de ocorrências.',
           'Sinal de praga: avisar o responsável, reforçar a limpeza e acionar a empresa fora do cronograma.',
           'Responsável confere os comprovantes da empresa e a validade do serviço a cada visita.')

pop3 = pop(3, 'Higienização do reservatório de água',
           [['Objetivo', 'Garantir água potável para preparo dos alimentos, gelo e higienização.'],
            ['Aplica-se a', f'Caixa d\'água / reservatório e filtro da cozinha. Capacidade: {AC_}.']],
           ul([
               '<b>Frequência:</b> no máximo a cada 6 meses (exigência da RDC 216/2004), e sempre que houver acidente que possa contaminar a água.',
               f'<b>Quem faz:</b> empresa especializada ou funcionário treinado. Responsável: {AC_}.',
               '<b>Passo a passo (referência):</b> fechar a entrada de água → esvaziar, guardando um palmo de água → esfregar paredes e fundo com escova (sem sabão) → retirar a sujeira → encher com água e desinfetante clorado conforme orientação do fabricante e deixar agir → esvaziar pelas torneiras → encher de novo e tampar bem.',
               '<b>Durante a limpeza:</b> não usar a água para preparar alimentos.',
               '<b>Filtro da cozinha:</b> trocar o elemento filtrante conforme o fabricante e registrar a troca.',
               '<b>Caixa d\'água:</b> sempre tampada, sem rachaduras e com acesso fácil.']),
           'Registrar data, responsável e próxima limpeza na Planilha do Reservatório; guardar o comprovante da empresa, se houver.',
           'Água com cor, cheiro ou gosto estranho: não usar, avisar o responsável e higienizar o reservatório.',
           'Responsável confere as datas a cada mês; laudo de potabilidade quando solicitado pela Vigilância Sanitária.')

pop4 = pop(4, 'Higiene e saúde dos manipuladores',
           [['Objetivo', 'Garantir que quem manipula alimentos esteja saudável, com higiene adequada e capacitado.'],
            ['Aplica-se a', 'Todos os funcionários que tocam em alimentos, inclusive substitutos e diaristas.']],
           table(['Tema', 'Regra da casa'], [
               ['Saúde', 'Com diarreia, vômito, febre, tosse, feridas ou cortes infeccionados: avisar o responsável e não manipular alimentos. Controle de saúde conforme a legislação trabalhista (exames admissionais e periódicos).'],
               ['Uniforme', 'Limpo, trocado todo dia, usado só dentro do estabelecimento; sapato fechado; touca cobrindo todo o cabelo.'],
               ['Adornos', 'Proibido anel, aliança, brinco, colar, relógio, pulseira, piercing e unhas postiças. Unhas curtas, limpas e sem esmalte. Sem perfume forte e sem maquiagem pesada.'],
               ['Mãos', 'Lavar conforme o adesivo (40 a 60 s): ao chegar, ao trocar de tarefa, após banheiro, lixo, cru, dinheiro, celular, tossir ou espirrar.'],
               ['Comportamento', 'Não fumar, comer, mascar chiclete, falar, cantar, tossir ou espirrar sobre os alimentos; não mexer no celular, no cabelo ou no rosto durante a manipulação; não manusear dinheiro durante a montagem.'],
               ['Visitantes', 'Só entram na produção com touca e seguindo as mesmas regras.'],
               ['Capacitação', 'Treinamento em Boas Práticas ao entrar e periodicamente (sugerido: a cada 6 meses), com lista de presença arquivada.'],
           ], widths=['20%', '80%']),
           'Checagem diária na entrada do turno (uniforme, touca, adornos, saúde), com rubrica na Planilha de Higiene Pessoal.',
           'Fora do padrão: corrigir antes de entrar na cozinha. Doente: afastar da manipulação e orientar a procurar atendimento.',
           'Responsável confere a planilha semanalmente e mantém os registros de treinamento e de saúde arquivados.')

days = ''.join(f'<th style="text-align:center;padding:4px 2px">{d}</th>' for d in range(1, 16))
def grade(rows, first='Item'):
    body = ''.join(f'<tr><td style="font-size:7.6pt">{r}</td>' + '<td></td>' * 15 + '</tr>' for r in rows)
    return f'<table class="fill"><thead><tr><th>{first}</th>{days}</tr></thead><tbody>{body}</tbody></table>'


plan1 = sec('05', 'Planilha · temperatura de geladeira e freezer') + '<p class="note" style="margin:-1mm 0 2mm">Medir na abertura (A) e no fechamento (F). Geladeira: até 5 °C · Freezer: −18 °C ou menos. Fora do limite: ajustar, conferir de novo em 30 min e avisar o responsável. Mês: ________ (dias 1 a 15; usar outra folha para 16 a 31).</p>' + \
    grade(['Geladeira 1 · A', 'Geladeira 1 · F', 'Geladeira 2 · A', 'Geladeira 2 · F', 'Freezer · A', 'Freezer · F', 'Rubrica'], 'Equipamento')
plan2 = sec('06', 'Planilha · higienização (POP 01)') + '<p class="note" style="margin:-1mm 0 2mm">Marcar ✓ e rubricar quando feito. Mês: ________</p>' + \
    grade(['Bancadas (fim do turno)', 'Utensílios e bisnagas', 'Masseira e balança', 'Piso e ralos', 'Lixeiras', 'Geladeiras (semanal)', 'Paredes e portas (semanal)', 'Teto e coifa (mensal)'], 'Área')
plan3 = sec('07', 'Planilha · higiene pessoal (POP 04)') + '<p class="note" style="margin:-1mm 0 2mm">Na entrada do turno: uniforme, touca, sem adornos, unhas e saúde OK = ✓. Mês: ________</p>' + \
    grade([f'Funcionário {i}: __________' for i in range(1, 8)], 'Nome') + \
    sec('08', 'Planilha · reservatório e pragas (POP 02 e 03)') + table(['Data', 'Serviço', 'Empresa / responsável', 'Próxima data', 'Comprovante?', 'Visto'],
                                                                         [['', 'Limpeza da caixa d\'água', '', '', '☐', ''], ['', 'Troca do filtro', '', '', '☐', ''], ['', 'Controle de pragas', '', '', '☐', ''], ['', 'Controle de pragas', '', '', '☐', ''], ['', '', '', '', '☐', '']], widths=['12%', '24%', '26%', '14%', '12%', '12%']).replace('<table', '<table class="fill"')
subs2 = ['POP 01 · Higienização', 'POP 02 · Pragas', 'POP 03 · Reservatório de água', 'POP 04 · Manipuladores', 'Planilha de temperatura', 'Planilha de higienização', 'Higiene pessoal, água e pragas']
doc('trein_pops.html', 'Speciale · POPs', [r2] + [page(D2, s, i + 2, T2, F2, c) for i, (s, c) in enumerate(zip(subs2, [pop1, pop2, pop3, pop4, plan1, plan2, plan3]))])

# =================== 3. CARTILHA ===================
D3, F3, T3 = 'CARTILHA · BOAS PRÁTICAS', 'Speciale Pizzas Artesanais · Cartilha da equipe · RDC ANVISA 216/2004', 3
r3 = cover('Cartilha da equipe', 'Resumo das', 'boas práticas',
           'O essencial para quem trabalha na cozinha da Speciale, em uma leitura de 5 minutos. Guarde e consulte sempre.',
           [('5 °C', 'temperatura máxima da geladeira'), ('40 a 60 s', 'para lavar as mãos'), ('PVPS', 'primeiro que vence, primeiro que sai')])
c1 = '<div class="two">' + ''.join(f'<div class="card"><h4>{t}</h4>{ul(xs)}</div>' for t, xs in [
    ('1 · Eu, antes de entrar', ['Uniforme limpo e touca cobrindo o cabelo.', 'Sem anel, brinco, relógio, pulseira ou piercing.', 'Unhas curtas, limpas e sem esmalte.', 'Doente? Avise antes de entrar.']),
    ('2 · Minhas mãos', ['Lavo ao chegar e a cada troca de tarefa.', 'Lavo depois do banheiro, do lixo, do cru, do dinheiro e do celular.', '40 a 60 segundos, seguindo o adesivo.', 'Luva não substitui a lavagem.']),
    ('3 · Cru longe do pronto', ['Frango, ovo e carnes separados de queijos, presunto e molho.', 'Tábua e faca limpas entre um e outro.', 'Pano de prato não é para tudo.', 'Sobra nunca volta para a embalagem.']),
    ('4 · Frio é frio, quente é quente', ['Geladeira até 5 °C; freezer −18 °C.', 'Descongelar dentro da geladeira; nunca recongelar.', 'Cozinhar até 70 °C no centro.', 'Preparado e refrigerado: no máximo 5 dias.']),
    ('5 · Tudo etiquetado', ['Produto, data de preparo ou abertura, validade e responsável.', 'Primeiro que vence, primeiro que sai.', 'Nada no chão; tudo tampado.', 'Venceu ou está estranho? Descarte e avise.']),
    ('6 · Limpo e desinfetado', ['Primeiro limpar, depois desinfetar.', 'Bancada limpa a cada pizza e no fim do turno.', 'Produto de limpeza só diluído como no rótulo e longe dos alimentos.', 'Lixeira tampada, com pedal, esvaziada sempre.'])]) + '</div>'
c2 = sec('', 'Na Speciale, é assim').replace('<span class="num"></span>', '') + table(['Situação', 'O que fazer'], [
    ['Massa', 'Etiquetada, coberta e dentro da validade da casa; descongelar na geladeira.'],
    ['Molho', 'Pegar com concha ou colher limpa; balde sempre tampado.'],
    ['Catupiry', 'Bico e bisnaga limpos; saco descartável trocado no fim do turno; sobra não volta.'],
    ['Montagem', 'Na bancada só o que vai para a pizza agora; ingredientes voltam para a geladeira.'],
    ['Forno e pá', 'Pá limpa; ao redor do forno sem acúmulo de cinza e restos.'],
    ['Entrega', 'Caixa fechada na hora; bag térmica limpa por dentro.'],
    ['Viu algo errado?', 'Avise o responsável na hora. Segurança do cliente vem primeiro.']], widths=['22%', '78%']) + \
    '<div class="box"><h5>Quem é o responsável pelas boas práticas?</h5><p>Nome: ______________________________ · Telefone: __________________</p></div>' + \
    '<div class="sign" style="grid-template-columns:1fr 1fr;margin-top:12mm"><div>Li e entendi · nome</div><div>Data e assinatura</div></div>'
doc('trein_cartilha.html', 'Speciale · Cartilha de Boas Práticas', [r3] + [page(D3, s, i + 2, T3, F3, c) for i, (s, c) in enumerate(zip(['O essencial', 'Na Speciale'], [c1, c2]))])

# =================== 4. ADESIVOS ===================
SCSS = '''<style>
.stk{position:relative;border:2px dashed #bbb;border-radius:4mm;overflow:hidden;display:flex;flex-direction:column}
.stk .hd{background:var(--red);color:#fff;padding:3mm 5mm;font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:15pt;line-height:1}
.stk .bd{padding:4mm 5mm;flex:1;background:#fff}
.n{font-family:'Roboto Condensed';font-weight:800;color:var(--red);font-size:22pt;line-height:1}
.hw{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.hw div{background:var(--cream);border-radius:3mm;padding:4mm;text-align:center}
.hw p{font-size:10pt;font-weight:600;margin-top:2mm;line-height:1.3}
.hw svg{display:block;margin:2mm auto 0}
.lbl{font-size:8.5pt;line-height:2.1}
.big{font-family:'Roboto Condensed';font-weight:800;color:var(--red);line-height:1}
</style>'''


def hand(kind):
    # ícones simples, só traço
    c = '#d7141a'
    base = '<svg width="34mm" height="20mm" viewBox="0 0 68 40" fill="none" stroke="' + c + '" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
    pal = 'M10 32 C6 24 8 14 16 12 L30 10 C34 10 34 15 30 16 L22 17'
    pal2 = 'M58 32 C62 24 60 14 52 12 L38 10 C34 10 34 15 38 16 L46 17'
    art = {
        'agua': '<path d="M34 4 C28 14 26 18 26 22 a8 8 0 0 0 16 0 C42 18 40 14 34 4Z"/><path d="M30 24 a4 4 0 0 0 4 4"/>',
        'sabao': '<rect x="24" y="14" width="20" height="22" rx="3"/><path d="M30 14 V8 H40"/><circle cx="50" cy="10" r="2"/><circle cx="54" cy="16" r="1.6"/>',
        'palmas': f'<path d="{pal}"/><path d="{pal2}"/><path d="M16 12 L18 4 M22 11 L24 3 M46 11 L44 3 M52 12 L50 4"/>',
        'dorso': f'<path d="{pal}"/><path d="M20 22 L44 18 M24 28 L48 24"/><path d="M40 14 C50 10 58 16 56 26"/>',
        'dedos': '<path d="M12 34 L22 8 M20 34 L30 8 M28 34 L38 8"/><path d="M56 34 L46 8 M48 34 L38 8 M40 34 L30 8"/>',
        'polegar': '<path d="M20 34 C14 26 16 14 26 12 L34 12"/><path d="M34 12 C40 6 48 8 46 16 C44 22 38 22 34 20"/><path d="M28 20 C36 26 44 24 50 30"/>',
        'unhas': '<path d="M14 32 C12 22 20 16 30 18 L38 20"/><circle cx="44" cy="20" r="6"/><path d="M40 16 L44 12 L48 16 M44 26 V30"/>',
        'punhos': '<rect x="18" y="20" width="12" height="16" rx="3"/><path d="M30 20 C30 10 40 6 48 10 L54 16"/><path d="M14 24 C22 20 30 26 38 24"/>',
        'enxague': '<path d="M14 6 H40 V14"/><path d="M40 16 V20 M36 24 V28 M44 24 V28"/><path d="M16 36 C20 28 34 28 40 32 C46 28 56 30 58 36"/>',
        'seca': '<rect x="14" y="6" width="40" height="12" rx="2"/><path d="M22 18 V30 H46 V18"/><path d="M26 22 H42 M26 26 H42"/>',
    }[kind]
    return base + art + '</svg>'


steps = [('agua', 'Molhe as mãos'), ('sabao', 'Aplique sabonete líquido'), ('palmas', 'Esfregue as palmas'),
         ('dorso', 'Esfregue o dorso das mãos'), ('dedos', 'Esfregue entre os dedos'), ('polegar', 'Esfregue o polegar'),
         ('unhas', 'Esfregue pontas dos dedos e unhas'), ('punhos', 'Esfregue os punhos'), ('seca', 'Enxágue e seque com papel toalha')]
hw = '<div class="hw">' + ''.join(f'<div><div class="n">{i}</div>{hand(k)}<p>{t}</p></div>' for i, (k, t) in enumerate(steps, 1)) + '</div>'


def spage(inner):
    return f'<section class="page" style="padding:12mm 14mm">{inner}<div class="foot" style="left:14mm;right:14mm;bottom:5mm"><span>Speciale Pizzas Artesanais · Adesivos e cartazes · imprimir em papel adesivo e recortar na linha tracejada</span><span>RDC ANVISA 216/2004</span></div></section>'


s1 = spage(f'''<div class="stk" style="height:270mm"><div class="hd" style="font-size:30pt;padding:6mm 8mm;display:flex;justify-content:space-between;align-items:center">Lave as mãos assim<span style="font-size:12pt;font-family:Poppins;font-weight:600;text-transform:none">40 a 60 segundos</span></div>
<div class="bd" style="padding:7mm 8mm">{hw}
<div style="margin-top:7mm;display:grid;grid-template-columns:1fr 1fr;gap:5mm;font-size:10.5pt">
<div style="background:var(--red);color:#fff;border-radius:3mm;padding:4mm 5mm"><b style="font-family:Roboto Condensed;font-size:13pt">QUANDO LAVAR</b><br>Ao chegar · ao trocar de tarefa · depois do banheiro, do lixo, do alimento cru, do dinheiro, do celular · depois de tossir ou espirrar</div>
<div style="background:var(--cream);border-radius:3mm;padding:4mm 5mm"><b style="font-family:Roboto Condensed;font-size:13pt;color:var(--red)">ATENÇÃO</b><br>Feche a torneira com o papel toalha. Luva não substitui a lavagem. Mãos sem anel, relógio e pulseira.</div></div>
<div style="margin-top:6mm;display:flex;justify-content:space-between;align-items:center">{logo()}<span style="font-size:8pt;color:#666">Lavatório exclusivo para as mãos · sabonete líquido · papel toalha · lixeira com pedal</span></div></div></div>''').replace('<div class="logo">', '<div class="logo" style="color:#231a18">').replace('fill="#fff"', 'fill="#231a18"')


def sticker(hd, body, h='62mm', color='var(--red)'):
    return f'<div class="stk" style="height:{h}"><div class="hd" style="background:{color}">{hd}</div><div class="bd">{body}</div></div>'


s2 = spage('<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm">' + ''.join([
    sticker('Geladeira', '<div class="big" style="font-size:44pt">até 5 °C</div><p style="font-size:9.5pt;margin-top:2mm">Confira e anote na abertura e no fechamento. Crus embaixo, prontos em cima, tudo tampado e etiquetado.</p>'),
    sticker('Freezer', '<div class="big" style="font-size:44pt">−18 °C</div><p style="font-size:9.5pt;margin-top:2mm">ou menos. Descongele dentro da geladeira. Nunca recongele.</p>', color='#1f4f8a'),
    sticker('Sem adornos', '<p style="font-size:11pt;font-weight:600;line-height:1.5">Anel · aliança · brinco · relógio · pulseira · colar · piercing</p><p style="font-size:9.5pt;margin-top:2mm">Tire antes de entrar na cozinha. Unhas curtas e sem esmalte.</p>'),
    sticker('Touca sempre', '<p style="font-size:11pt;font-weight:600;line-height:1.5">Cabelo preso e totalmente coberto.</p><p style="font-size:9.5pt;margin-top:2mm">Área de produção: entrada só com touca e uniforme limpo.</p>'),
    sticker('PVPS', '<div class="big" style="font-size:24pt">Primeiro que vence,<br>primeiro que sai</div><p style="font-size:9.5pt;margin-top:2mm">Use antes o que vence antes. Venceu? Descarte e avise.</p>', color='#2f8a4e'),
    sticker('Lixeira', '<p style="font-size:11pt;font-weight:600;line-height:1.5">Mantenha tampada.<br>Abra só pelo pedal.</p><p style="font-size:9.5pt;margin-top:2mm">Lave as mãos depois de mexer no lixo.</p>', color='#555'),
    sticker('Área de produção', '<p style="font-size:11pt;font-weight:600;line-height:1.5">Proibido celular, comer, fumar e mascar chiclete.</p><p style="font-size:9.5pt;margin-top:2mm">Não tussa nem espirre sobre os alimentos.</p>'),
    sticker('Produtos de limpeza', '<p style="font-size:11pt;font-weight:600;line-height:1.5">Guardar longe dos alimentos.</p><p style="font-size:9.5pt;margin-top:2mm">Diluir só como indica o rótulo. Nunca misturar produtos.</p>', color='#555')]) + '</div>')

lbl = '<div class="lbl"><b>Produto:</b> ____________________<br><b>Preparo/abertura:</b> ___/___ · ___h<br><b>Validade:</b> ___/___<br><b>Responsável:</b> ______________<br>☐ Geladeira ☐ Freezer ☐ Seco</div>'
s3 = spage('<div style="font-family:Roboto Condensed;font-weight:800;font-size:16pt;text-transform:uppercase;margin-bottom:4mm">Etiquetas de validade <span style="font-family:Poppins;font-weight:400;font-size:9pt;text-transform:none;color:#666">· imprimir em papel adesivo · 12 por folha</span></div>'
           '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4mm">' + ''.join(
               sticker('Speciale · etiqueta', lbl, h='60mm', color=['var(--red)', '#2f8a4e', '#1f4f8a'][i % 3]) for i in range(12)) + '</div>')
s4 = spage('<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm">' + ''.join([
    sticker('Só para lavar as mãos', '<p style="font-size:12pt;font-weight:600">Pia exclusiva para higiene das mãos.</p><p style="font-size:9.5pt;margin-top:2mm">Não lavar utensílios nem alimentos aqui.</p>', h='58mm'),
    sticker('Descongelamento', '<p style="font-size:12pt;font-weight:600">Só dentro da geladeira.</p><p style="font-size:9.5pt;margin-top:2mm">Massa: cerca de 12 h na geladeira (a confirmar pela casa). Nunca na bancada ou na pia.</p>', h='58mm', color='#1f4f8a'),
    sticker('Alimentos prontos', '<p style="font-size:12pt;font-weight:600">Queijos, presunto, molho, catupiry.</p><p style="font-size:9.5pt;margin-top:2mm">Prateleiras de cima. Separados dos crus.</p>', h='58mm', color='#2f8a4e'),
    sticker('Alimentos crus', '<p style="font-size:12pt;font-weight:600">Frango, ovos, carnes.</p><p style="font-size:9.5pt;margin-top:2mm">Prateleira de baixo, tampados.</p>', h='58mm'),
    sticker('Catupiry', '<p style="font-size:12pt;font-weight:600">Bico e bisnaga limpos.</p><p style="font-size:9.5pt;margin-top:2mm">Saco descartável trocado no fim do turno. A sobra não volta para a embalagem.</p>', h='58mm', color='#2f8a4e'),
    sticker('Bancada limpa', '<p style="font-size:12pt;font-weight:600">A cada pizza: só o que vai para ela.</p><p style="font-size:9.5pt;margin-top:2mm">No fim do turno: limpar e depois desinfetar.</p>', h='58mm', color='#555'),
    sticker('Está doente?', '<p style="font-size:12pt;font-weight:600">Diarreia, febre, vômito, ferida?</p><p style="font-size:9.5pt;margin-top:2mm">Avise o responsável antes de entrar na cozinha.</p>', h='58mm'),
    sticker('Termômetro', '<p style="font-size:12pt;font-weight:600">Anote a temperatura 2 vezes ao dia.</p><p style="font-size:9.5pt;margin-top:2mm">Fora do limite? Ajuste, confira em 30 min e avise.</p>', h='58mm', color='#1f4f8a')]) + '</div>')
open('trein_adesivos.html', 'w').write(html('Speciale · Adesivos e cartazes', [s1, s2, s4, s3]).replace('</head>', SCSS + '</head>'))
