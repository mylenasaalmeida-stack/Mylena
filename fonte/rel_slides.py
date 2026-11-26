from apresentacao import sl, ul, RED, OR, CR, INK
AC = '<span style="color:#f07f1e;font-weight:600">[a preencher]</span>'

def tab(rows, w='30%'):
    return '<table><tbody>' + ''.join(f'<tr><td style="width:{w}"><b>{a}</b></td><td>{b}</td></tr>' for a, b in rows) + '</tbody></table>'

r1 = sl(0, 'Relatório de extensão · 1', 'Identificação <span>da iniciativa</span>', tab([
    ('Título', 'Boas Práticas de Manipulação de Alimentos em uma pizzaria de Recife: diagnóstico, padronização e capacitação da equipe'),
    ('Tipo de iniciativa', AC), ('Carga horária total', AC), ('Curso', AC), ('Escola', AC), ('Disciplina', AC), ('Professor(a)', AC), ('Programa Unicap', AC),
    ('Público parceiro', 'Speciale Pizzas Artesanais · Recife (forno a lenha, salão e delivery)'),
    ('Base normativa', 'RDC ANVISA nº 216/2004 · Boas Práticas para Serviços de Alimentação')]))

r2 = sl(0, 'Relatório de extensão · 4', 'Objetivos <span>da iniciativa</span>', f'''<div class="cols" style="grid-template-columns:1fr 1.25fr">
<div class="card"><h4>Objetivo principal</h4><p style="font-size:12.5pt;line-height:1.5">Promover a adequação da pizzaria às Boas Práticas de Manipulação de Alimentos (RDC ANVISA 216/2004), ensinando a equipe e entregando documentos e materiais de apoio.</p></div>
<div><table><thead><tr><th>Objetivo específico</th><th>Como foi alcançado</th></tr></thead><tbody>
<tr><td><b>1.</b> Diagnosticar as condições higiênico-sanitárias e a organização do local</td><td>1ª visita: conversa com o proprietário, observação da cozinha, estoque e salão, registro fotográfico e questionários à equipe</td></tr>
<tr><td><b>2.</b> Elaborar documentos e materiais conforme a RDC 216</td><td>8 POPs (4 obrigatórios), planilhas de registro, cartilha, cartazes, adesivos e etiquetas</td></tr>
<tr><td><b>3.</b> Capacitar a equipe e organizar as responsabilidades</td><td>Roteiro de treinamento, avaliação e divisão por praça; treinamento por setor na 3ª visita</td></tr>
</tbody></table></div></div>''')

r3 = sl(0, 'Relatório de extensão · 2', 'Aprendizagem <span>e competências</span>', f'''<div class="cols" style="grid-template-columns:1fr 1fr">
<div class="card"><h4>Objetivos de aprendizagem</h4>{ul(['Aplicar a RDC 216/2004 à realidade de um serviço de alimentação.', 'Elaborar documentos técnicos de boas práticas (POPs, planilhas de registro).', 'Planejar e conduzir uma ação educativa para manipuladores de alimentos.'])}
<p style="font-size:10pt;color:#555;margin-top:3mm"><b>Como a extensão contribuiu:</b> a norma estudada em sala foi aplicada a uma cozinha real, com limitações de espaço, tempo e equipe.</p></div>
<div class="card" style="border-top-color:{OR}"><h4>Competências transversais</h4>{ul(['Comunicação com públicos diversos (proprietário, gestor e equipe operacional).', 'Trabalho em equipe, planejamento e organização.', 'Pensamento crítico e resolução de problemas.'])}
<p style="font-size:10pt;color:#555;margin-top:3mm"><b>Para as próximas edições:</b> mais tempo de acompanhamento na rotina e devolutiva com indicadores.</p></div></div>''')

r4 = sl(0, 'Relatório de extensão · 3', 'Interação com o <span>público parceiro</span>', f'''<div class="cols" style="grid-template-columns:1fr 1fr">
<div class="card"><h4>Como foi</h4>{ul(['Conversa inicial com o proprietário sobre objetivos e dificuldades.', 'Questionários aplicados à equipe operacional.', 'Alinhamento com o gestor para definir responsáveis por setor.', 'Treinamento organizado por equipe, para não parar a operação.'])}</div>
<div class="card" style="border-top-color:{OR}"><h4>O que aprendemos com a realidade</h4>{ul(['Distância entre a norma e a rotina de uma pizzaria com delivery e forno a lenha.', 'Estrutura (estoque, freezer, banheiro) influencia tanto quanto o comportamento.', 'Materiais simples e visuais funcionam melhor para a equipe.'])}
<p style="font-size:10pt;color:#555;margin-top:3mm"><b>Melhoria futura:</b> mais visitas em horários de produção e escuta contínua da equipe.</p></div></div>''')

r5 = sl(0, 'Relatório de extensão · 5', 'ODS <span>e metas</span>', f'''<div class="cols" style="grid-template-columns:.8fr 1.2fr">
<div class="card" style="background:#2f8a4e;color:#fff;border-top-color:#1e5f33"><div class="big" style="color:#fff">ODS 3</div><h4 style="margin-top:2mm">Saúde e bem-estar</h4>
<p style="font-size:11pt;line-height:1.5">Boas práticas previnem doenças transmitidas por alimentos e protegem clientes e trabalhadores.</p>
<p style="font-size:9pt;margin-top:3mm;opacity:.9">Confirmar a ODS escolhida no Plano de Trabalho. Relação também com a ODS 8 (trabalho decente).</p></div>
<div><table><thead><tr><th>Meta</th><th style="width:26%">Situação</th></tr></thead><tbody>
<tr><td><b>1.</b> Realizar o diagnóstico do estabelecimento com registro fotográfico e questionários</td><td><span style="color:#2f8a4e;font-weight:700">Atingida</span></td></tr>
<tr><td><b>2.</b> Elaborar os POPs exigidos pela RDC 216 e os materiais de sinalização</td><td><span style="color:#2f8a4e;font-weight:700">Atingida</span> (8 POPs)</td></tr>
<tr><td><b>3.</b> Capacitar a equipe operacional e definir responsáveis por setor</td><td><span style="color:{OR};font-weight:700">Em andamento</span> (3ª visita)</td></tr>
</tbody></table><p style="font-size:9.5pt;color:#555;margin-top:3mm">Ajustar o texto das metas ao Plano de Trabalho de Extensão.</p></div></div>''')

r6 = sl(0, 'Relatório de extensão · 6', 'Reflexões <span>e avaliação</span>', f'''<div class="cols" style="grid-template-columns:1fr 1fr 1fr 1fr">
<div class="card"><h4>Antes</h4><p style="font-size:10.5pt;line-height:1.45">Estudo da RDC 216 e preparação da visita.<br><b style="color:{RED}">Melhorar:</b> levar um checklist padrão de inspeção.</p></div>
<div class="card"><h4>Durante</h4><p style="font-size:10.5pt;line-height:1.45">Rotina intensa limitou o tempo com a equipe.<br><b style="color:{RED}">Melhorar:</b> visitar fora do horário de pico.</p></div>
<div class="card"><h4>Depois</h4><p style="font-size:10.5pt;line-height:1.45">Materiais entregues; implantação depende da casa.<br><b style="color:{RED}">Melhorar:</b> acompanhar com indicadores.</p></div>
<div class="card" style="border-top-color:{OR}"><h4>Avaliação</h4>{ul(['Avaliação escrita (10 questões)', 'Lista de presença', 'Planilhas de registro', 'Checklist na 3ª visita'])}</div></div>
<p style="font-size:9pt;color:#777;margin-top:4mm">Reflexões em rascunho: revisar com a percepção de cada estudante.</p>''')

r7 = sl(0, 'Relatório de extensão · 7, 8 e 9', 'Sugestões <span>e equipe</span>', f'''<div class="cols" style="grid-template-columns:1.2fr 1fr">
<div class="card"><h4>Sugestões para a iniciativa</h4>{ul(['Prever ao menos 4 visitas, com uma de acompanhamento após a implantação.', 'Usar checklist de verificação antes e depois para medir a evolução.', 'Treinar toda a equipe, em turnos, incluindo entregadores.', 'Manter parceria com o estabelecimento para revisão anual dos POPs.'])}</div>
<div><div class="card" style="border-top-color:{OR}"><h4>Estudantes (ordem alfabética)</h4>{ul(['[nome da estudante]', 'Mylena Almeida'])}</div>
<div class="card" style="margin-top:5mm;border-top-color:#555"><h4>Registros</h4><p style="font-size:11pt">Fotos e documentos: {AC} (link da pasta no Google Drive)</p></div></div></div>''')
