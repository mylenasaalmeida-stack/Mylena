"""Dois documentos de POPs: versão completa (gestão) e guia da equipe (operacional)."""
import treinamento as T
from common import *
from sinalizacao import POPS, ic, CREAM, INK, AMBER

# ============ VERSÃO COMPLETA (GESTÃO) ============
D, F = 'MANUAL DE POPs · VERSÃO DE GESTÃO', 'Speciale Pizzas Artesanais · Manual de POPs · Revisão 00 · RDC ANVISA 216/2004'
NOMES = ['Higienização de instalações, equipamentos e móveis', 'Controle integrado de vetores e pragas urbanas', 'Higienização do reservatório de água',
         'Higiene e saúde dos manipuladores', 'Recebimento e armazenamento de mercadorias', 'Higienização de hortifrútis', 'Operação do forno a lenha', 'Expedição, delivery e salão']
POPH = [T.pop1, T.pop2, T.pop3, T.pop4, T.pop5, T.pop6, T.pop7, T.pop8]
PLANS = [T.plan1, T.plan2, T.plan3]
NPAG = 1 + 4 + 8 + 3 + 1
pg = lambda n, sub, c: page(D, sub, n, NPAG, F, c)

capa = T.cover('Manual de POPs · versão completa', 'Procedimentos', 'operacionais',
               'Documento de gestão da Speciale com os 8 Procedimentos Operacionais Padronizados, responsabilidades, cronograma, registros e controle de revisão.',
               [('8 POPs', '4 exigidos pela RDC 216 + 4 da operação'), ('Rev. 00', 'novembro/2026 · revisar a cada 12 meses'), ('Para', 'direção e responsável pelas boas práticas')])

sumario = ''.join(f'<tr><td style="white-space:nowrap"><b>POP-SPC-{i:02d}</b></td><td>{n}</td><td>{"Obrigatório (RDC 216, item 4.11)" if i <= 4 else "Operacional da casa"}</td><td style="text-align:right">{4 + i}</td></tr>' for i, n in enumerate(NOMES, 1))
g1 = sec('01', 'Sumário') + f'<table><thead><tr><th>Código</th><th>Procedimento</th><th>Natureza</th><th style="text-align:right">Pág.</th></tr></thead><tbody>{sumario}' + \
    '<tr><td><b>Anexos</b></td><td>Planilhas de registro (temperatura, higienização, higiene pessoal, reservatório e pragas)</td><td>Registros</td><td style="text-align:right">14 a 16</td></tr>' + \
    '<tr><td><b>Aprovação</b></td><td>Termo de aprovação e implantação</td><td>Gestão</td><td style="text-align:right">17</td></tr></tbody></table>' + \
    sec('02', 'Objetivo e base legal') + T.ul([
        '<b>Objetivo:</b> padronizar as operações que garantem a segurança dos alimentos na Speciale, do recebimento à entrega, e servir de evidência para a Vigilância Sanitária.',
        '<b>RDC ANVISA 216/2004</b>, item 4.11: o serviço de alimentação deve ter Manual de Boas Práticas e POPs, acessíveis aos funcionários e disponíveis à autoridade sanitária.',
        '<b>Item 4.11.2:</b> os POPs devem ter instruções sequenciais, frequência, nome e cargo ou função dos responsáveis, e ser aprovados, datados e assinados pelo responsável do estabelecimento.',
        '<b>Item 4.11.4:</b> os POPs obrigatórios são: higienização de instalações, equipamentos e móveis; controle de vetores e pragas; higienização do reservatório; higiene e saúde dos manipuladores.',
        'Os POPs 05 a 08 foram criados para a realidade da casa (delivery, salão e forno a lenha).']) + \
    sec('03', 'Definições') + T.table(['Termo', 'Significado'], [
        ['Limpeza', 'Remoção de terra, resíduos de alimento, gordura e outras sujidades.'],
        ['Desinfecção', 'Redução, por produto químico ou método físico, dos micro-organismos a um nível que não comprometa a segurança do alimento.'],
        ['Higienização', 'Limpeza seguida de desinfecção.'],
        ['Manipulador', 'Qualquer pessoa que entra em contato direto ou indireto com o alimento.'],
        ['Monitoramento', 'Observação ou medição para saber se o procedimento está sendo seguido.'],
        ['Ação corretiva', 'O que fazer quando o monitoramento mostra um desvio.'],
        ['Verificação', 'Conferência, pelo responsável, de que o POP funciona e está registrado.'],
        ['PVPS', 'Primeiro que vence, primeiro que sai.']], widths=['24%', '76%'])

papeis = ['Proprietária', 'Resp. boas práticas', 'Supervisor turno', 'Resp. da praça', 'Empresa externa']
M = [['Higienização', 'A', 'V', 'M', 'E', '—'], ['Pragas', 'A', 'V', 'M', 'E (prevenção)', 'E (controle químico)'],
     ['Reservatório', 'A', 'V', '—', '—', 'E'], ['Manipuladores', 'A', 'V', 'M', 'E', '—'], ['Recebimento', 'A', 'V', 'M', 'E', '—'],
     ['Hortifrútis', 'A', 'V', 'M', 'E', '—'], ['Forno a lenha', 'A', 'V', 'M', 'E', '—'], ['Delivery e salão', 'A', 'V', 'M', 'E', '—']]
g2 = sec('04', 'Matriz de responsabilidades') + T.table(['POP'] + papeis, M, widths=['20%', '14%', '16%', '16%', '16%', '18%']) + \
    '<p class="note">A = aprova · V = verifica (confere os registros) · M = monitora no turno · E = executa. Nomes no documento “Divisão por praça e responsáveis”.</p>' + \
    sec('05', 'Cronograma de execução') + T.table(['Atividade', 'Diária', 'Semanal', 'Mensal', 'Semestral', 'POP'], [
        ['Temperatura de geladeira e freezer (2x)', '●', '', '', '', '05'], ['Checagem de higiene da equipe', '●', '', '', '', '04'],
        ['Bancadas, utensílios, piso, lixeiras', '●', '', '', '', '01'], ['Bags térmicas, mesas e cardápios', '●', '', '', '', '08'],
        ['Área do forno, pá, cinzas', '●', '', '', '', '07'], ['Geladeiras, paredes; extintor', '', '●', '', '', '01 · 07'],
        ['Revisão das planilhas', '', '●', '', '', 'Todos'], ['Teto, luminárias, coifa', '', '', '●', '', '01'],
        ['Controle de pragas (empresa)', '', '', 'contrato', '', '02'], ['Higienização do reservatório', '', '', '', '●', '03'],
        ['Treinamento da equipe', '', '', '', '●', '04'], ['Revisão do manual de POPs', '', '', '', 'anual', 'Todos']],
        widths=['40%', '10%', '11%', '11%', '12%', '16%']).replace('<td class="">●</td>', '<td style="text-align:center;color:#d7141a">●</td>')

g3 = sec('06', 'Registros e arquivamento') + T.table(['Registro', 'Quem preenche', 'Onde fica', 'Guardar por'], [
    ['Planilha de temperatura', 'Resp. estoque / supervisor', 'Na cozinha, perto das geladeiras', 'Mínimo 30 dias (sugerido 12 meses)'],
    ['Planilha de higienização', 'Resp. de cada praça', 'Na cozinha', 'Sugerido 12 meses'],
    ['Planilha de higiene pessoal', 'Supervisor do turno', 'Na cozinha', 'Sugerido 12 meses'],
    ['Planilha de recebimento', 'Resp. estoque', 'Estoque', 'Sugerido 12 meses'],
    ['Comprovantes de pragas e reservatório', 'Resp. boas práticas', 'Pasta de Boas Práticas', 'Até o próximo serviço + 12 meses'],
    ['Lista de presença dos treinamentos', 'Resp. boas práticas', 'Pasta de Boas Práticas', 'Enquanto o funcionário estiver na casa'],
], widths=['30%', '24%', '24%', '22%']) + '<p class="note">A RDC 216 exige manter os registros, mas não fixa prazo. Os prazos acima são sugestão de gestão; confirmar com a Vigilância Sanitária do Recife.</p>' + \
    sec('07', 'Controle de revisões') + T.table(['Rev.', 'Data', 'O que mudou', 'Aprovado por'], [['00', 'Nov/2026', 'Emissão inicial: 8 POPs', ''], ['01', '', '', ''], ['02', '', '', '']], widths=['10%', '16%', '50%', '24%']).replace('<table', '<table class="fill"') + \
    sec('08', 'Pendências para implantação') + T.ul([
        'Nomear o responsável pelas boas práticas e os supervisores de turno.', 'Definir a empresa de controle de pragas e anexar o contrato.',
        'Registrar a capacidade da caixa d\'água e a data da última higienização.', 'Definir os produtos de limpeza e de hortifrútis (marca e diluição do rótulo).',
        'Confirmar a validade e o armazenamento da massa (geladeira ou freezer).', 'Conferir a existência e a validade do extintor perto do forno.'])

aprov = sec('09', 'Termo de aprovação e implantação') + '<p style="font-size:9pt;line-height:1.6;text-align:justify">Declaro que os 8 Procedimentos Operacionais Padronizados deste manual (POP-SPC-01 a POP-SPC-08) foram elaborados para a Speciale Pizzas Artesanais, conforme a RDC ANVISA 216/2004, e ficam aprovados para implantação a partir de ___/___/______. Os funcionários envolvidos serão treinados e os registros serão mantidos à disposição da autoridade sanitária.</p>' + \
    T.table(['Função', 'Nome', 'Assinatura', 'Data'], [['Proprietária / responsável pelo estabelecimento', '', '', ''], ['Diretor', '', '', ''], ['Responsável pelas boas práticas', '', '', ''], ['Elaborado por', '', '', '']], widths=['32%', '26%', '26%', '16%']).replace('<table', '<table class="fill"')

pops_pages = [pg(5 + i, f'POP-SPC-{i:02d}', h.replace(f">{i:02d}</span><h2>", f">{i:02d}</span><h2>POP-SPC-{i:02d} · ").replace("<td class=\"k\">POP nº</td><td class=\"\">", "<td class=\"k\">Código</td><td class=\"\">POP-SPC-").replace("['Elaborado em'", "['Elaborado em'")) for i, h in enumerate(POPH, 1)]
pops_pages = [p.replace('<td class="k">Elaborado em</td><td class="">Novembro/2026 · versão 1.0</td>', '<td class="k">Revisão</td><td class="">00 · emitido em novembro/2026 · próxima revisão: novembro/2027</td>') for p in pops_pages]
plan_pages = [pg(14 + i, s, c) for i, (s, c) in enumerate(zip(['Anexo · temperatura', 'Anexo · higienização', 'Anexo · higiene, água e pragas'], PLANS))]
gest = [capa, pg(2, 'Sumário e base legal', g1), pg(3, 'Responsabilidades e cronograma', g2), pg(4, 'Registros e revisões', g3)] + [pg(5, 'Nota', '')][:0] + pops_pages + plan_pages + [pg(17, 'Aprovação', aprov)]
# corrige numeração: POPs nas págs. 5-12, anexos 13-15, aprovação 16
NPAG = 16
gest = [capa, page(D, 'Sumário e base legal', 2, NPAG, F, g1), page(D, 'Responsabilidades e cronograma', 3, NPAG, F, g2), page(D, 'Registros e revisões', 4, NPAG, F, g3)]
for i, h in enumerate(POPH, 1):
    h = h.replace(f'<span class="num">{i:02d}</span><h2>', f'<span class="num">{i:02d}</span><h2>POP-SPC-{i:02d} · ')
    h = h.replace('<td class="k">Elaborado em</td><td class="">Novembro/2026 · versão 1.0</td>', '<td class="k">Revisão</td><td class="">00 · novembro/2026 · próxima: novembro/2027</td>')
    gest.append(page(D, f'POP-SPC-{i:02d}', 4 + i, NPAG, F, h))
for i, (s, c) in enumerate(zip(['Anexo · temperatura', 'Anexo · higienização', 'Anexo · higiene, água e pragas'], PLANS)):
    gest.append(page(D, s, 13 + i, NPAG, F, c))
gest.append(page(D, 'Aprovação', 16, NPAG, F, aprov))
g1 = g1.replace('<td style="text-align:right">{4 + i}</td>', '')
open('pops_gestao.html', 'w').write(html('Speciale · Manual de POPs (gestão)', gest).replace('</head>', T.EXTRA + '</head>').replace('14 a 16</td>', '13 a 15</td>').replace('>17</td></tr></tbody>', '>16</td></tr></tbody>'))
for i in range(1, 9):
    pass

# ============ GUIA DA EQUIPE (OPERACIONAL) ============
NEVER = {1: ['Misturar produtos de limpeza', 'Usar pano de prato para tudo', 'Varrer a seco na produção'],
         2: ['Aplicar veneno por conta própria', 'Deixar comida aberta ou no chão', 'Guardar caixa de papelão no estoque'],
         3: ['Usar a água durante a limpeza da caixa', 'Deixar a caixa d\'água destampada', 'Usar água com cheiro ou cor estranha'],
         4: ['Trabalhar com anel, relógio ou brinco', 'Usar celular na produção', 'Manipular alimento doente'],
         5: ['Aceitar embalagem amassada ou furada', 'Deixar refrigerado fora da geladeira', 'Guardar produto sem etiqueta'],
         6: ['Usar água sanitária com perfume', 'Pular o enxágue', 'Usar a bacia para outra coisa'],
         7: ['Acender com álcool ou gasolina', 'Usar madeira pintada ou tratada', 'Deixar papel ou caixa perto do forno'],
         8: ['Colocar capacete ou objetos na bag', 'Abrir a caixa da pizza', 'Servir depois de pegar dinheiro sem lavar as mãos']}
WHERE = {1: 'Planilha de higienização', 2: 'Avisar o supervisor (caderno de ocorrências)', 3: 'Planilha do reservatório', 4: 'Planilha de higiene pessoal',
         5: 'Planilha de recebimento', 6: 'Registro de hortifrútis', 7: 'Planilha de higienização (área do forno)', 8: 'Planilha do salão / horário de saída'}
ECSS = f'''<style>
.op{{position:absolute;inset:0;display:flex;flex-direction:column}}
.oh{{background:var(--c);color:#fff;padding:9mm 12mm 7mm;display:flex;justify-content:space-between;align-items:center}}
.oh small{{font-size:8.5pt;font-weight:600;letter-spacing:1.5px;opacity:.9}}
.oh h1{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:30pt;line-height:1;margin-top:1.5mm}}
.oh .i{{width:26mm;height:26mm;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center}}
.ob{{padding:7mm 12mm 0;flex:1;display:flex;flex-direction:column}}
.lb{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:12pt;color:var(--c);margin:0 0 2.5mm}}
.ss .s{{display:grid;grid-template-columns:15mm 1fr;gap:4mm;align-items:center;padding:2.6mm 0;border-bottom:1px solid #eee3d6}}
.ss .c{{width:15mm;height:15mm;border-radius:50%;background:var(--c);display:flex;align-items:center;justify-content:center}}
.ss b{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:13pt;display:block;line-height:1.05}}
.ss span{{font-size:9.6pt;color:#444}}
.row{{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:6mm}}
.nv{{background:#FDECEC;border-radius:3mm;padding:4mm 5mm}}.nv li{{list-style:none;font-size:9.6pt;padding:1mm 0}}.nv li:before{{content:'✕  ';color:#C8161D;font-weight:800}}
.fq{{background:{CREAM};border-radius:3mm;padding:4mm 5mm;font-size:9.4pt;line-height:1.6}}
.wh{{margin-top:5mm;display:flex;align-items:center;gap:4mm;background:{INK};color:#fff;border-radius:3mm;padding:3.5mm 5mm;font-size:10pt}}
.of{{padding:4mm 12mm 6mm;display:flex;justify-content:space-between;font-size:7pt;color:#777}}
.ck td{{height:7.5mm;font-size:9pt}}
</style>'''


def op_page(n, title, sub, color, icon, steps, freq, warn):
    ss = ''.join(f'<div class="s"><div class="c">{ic(i, 30, "#fff", 2)}</div><div><b>{k}. {t}</b><span>{d}</span></div></div>' for k, (i, t, d) in enumerate(steps, 1))
    nv = ''.join(f'<li>{x}</li>' for x in NEVER[n])
    fq = '<br>'.join(f'<b>{a}:</b> {b}' for a, b in freq)
    return f'''<section class="page" style="--c:{color}"><div class="op">
<div class="oh"><div><small>GUIA DA EQUIPE · POP {n:02d}</small><h1>{title}</h1></div><div class="i">{ic(icon, 58, color, 1.8)}</div></div>
<div class="ob"><div class="lb">Como fazer</div><div class="ss">{ss}</div>
<div class="row"><div class="nv"><div class="lb" style="color:#C8161D">Nunca faça</div><ul>{nv}</ul></div><div class="fq"><div class="lb">Quando</div>{fq}</div></div>
<div class="wh">{ic("clipboard-check", 26, "#fff", 2)}<div><b>Anote em:</b> {WHERE[n]}</div></div>
<div class="wh" style="background:#FFF6DC;color:{INK}">{ic("circle-alert", 26, "#9a6a00", 2)}<div>{warn}</div></div></div>
<div class="of"><span>Speciale Pizzas Artesanais · Guia da equipe · versão simplificada do POP-SPC-{n:02d}</span><span>Dúvida? Fale com o supervisor do turno</span></div></div></section>'''


ecapa = T.cover('Guia da equipe', 'POPs', 'do dia a dia',
                'A versão simples dos 8 procedimentos da cozinha, do salão e do delivery: o que fazer, o que nunca fazer, quando e onde anotar.',
                [('1 página', 'por procedimento'), ('8 POPs', 'da lavagem ao delivery'), ('Na dúvida', 'fale com o supervisor')])
rot = '<section class="page" style="--c:#C8161D"><div class="op"><div class="oh"><div><small>GUIA DA EQUIPE · CHECKLIST</small><h1>Rotina do turno</h1></div><div class="i">' + ic('list-checks', 58, '#C8161D', 1.8) + '</div></div><div class="ob">' + ''.join(
    f'<div class="lb" style="margin-top:3mm">{t}</div><table class="ck"><tbody>' + ''.join(f'<tr><td style="width:8%;text-align:center">☐</td><td>{x}</td></tr>' for x in xs) + '</tbody></table>' for t, xs in [
        ('Abertura', ['Uniforme, touca, sem adornos, mãos lavadas', 'Temperatura da geladeira e do freezer anotada', 'Bancadas e utensílios higienizados', 'Lenha, extintor e área do forno conferidos', 'Massa e insumos dentro da validade']),
        ('Durante o turno', ['Mãos lavadas a cada troca de tarefa', 'Crus separados dos prontos; tudo tampado', 'Bancada limpa a cada pizza', 'Mesas e cardápios higienizados a cada cliente', 'Pizza embalada e conferida antes de sair']),
        ('Fechamento', ['Higienização das praças, masseira e balança', 'Bags térmicas limpas por dentro', 'Lixo retirado e lixeiras lavadas', 'Temperatura anotada de novo', 'Planilhas preenchidas e rubricadas'])]) + \
    '<div style="margin-top:5mm;font-size:9pt">Supervisor do turno: ______________________ · Data: ___/___/____</div></div><div class="of"><span>Speciale Pizzas Artesanais · Guia da equipe</span><span>RDC ANVISA 216/2004</span></div></div></section>'
eq = [ecapa] + [op_page(*p) for p in POPS] + [rot]
open('pops_equipe.html', 'w').write(html('Speciale · POPs · Guia da equipe', eq).replace('</head>', ECSS + '</head>'))
