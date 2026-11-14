"""Plano de ação Instagram v2 · posicionamento seguro (sem CRN) + crescimento do zero (A4 retrato)."""
from proposta_v2 import CSS as PCSS
from digital import EXTRA as DEXTRA

NOME = '[Seu nome] | Lucro e Marca para Restaurantes'
BIO = ['Restaurantes, bares e delivery com mais lucro', 'Custos • CMV • Cardápio • Marca', 'Do preço ao Instagram, tudo pronto', '📍 Recife · 👇 Análise gratuita']
BIO_LEN = len('\n'.join(BIO))
T = 10

EXTRA = '''<style>
.tb td,.tb th{font-size:7.9pt}
.grid2{display:grid;grid-template-columns:1fr 1fr}.grid3{display:grid;grid-template-columns:repeat(3,1fr)}
.card{background:var(--paper);border:1px solid var(--line);border-radius:6px;padding:4mm 4.5mm}
.card h4{font-family:'Roboto Condensed';font-weight:800;font-size:11pt;text-transform:uppercase;margin-bottom:1.5mm}
.card p,.card li{font-size:8pt;color:#3d3531;line-height:1.45}
.card ul{padding-left:4mm}
.card .n{font-family:'Roboto Condensed';font-weight:800;font-size:20pt;color:var(--acc);line-height:1}
.card.hl{border:1.5px solid var(--acc);background:#fff}
.g{border-top:4px solid #2f8a4e}.y{border-top:4px solid #e0a52e}.r{border-top:4px solid #c8361f}
.small{font-size:7.6pt;color:var(--muted)}
.src{font-size:7.4pt;line-height:1.5}.src li{margin:1.2mm 0;word-break:break-all}
.warn{border:1.5px solid var(--acc);border-radius:6px;padding:3.5mm 4.5mm;font-size:8pt;background:#fff}
.warn b{color:var(--acc)}
.phase{display:grid;grid-template-columns:28mm 1fr;gap:4mm;padding:3.5mm 0;border-bottom:1px solid var(--line)}
.phase .w{font-family:'Roboto Condensed';font-weight:800;font-size:12pt;text-transform:uppercase;color:var(--acc);line-height:1.05}
.phase .w small{display:block;font-family:Poppins;font-weight:500;font-size:7pt;color:var(--muted);text-transform:none;margin-top:1mm}
.phase ul{padding-left:4mm;font-size:8.2pt;line-height:1.45}.phase li{margin:.6mm 0}
</style>'''


def page(n, body):
    return (f'<section class="page"><div class="in" style="top:15mm">{body}</div><div class="ft"><span>Plano de ação · Instagram do zero · gestão de custos, cardápio e marca para restaurantes · Recife</span>'
            f'<span>{n} / {T}</span></div></section>')


def tbl(head, rows, widths):
    cg = '<colgroup>' + ''.join(f'<col style="width:{w}">' for w in widths) + '</colgroup>'
    return '<table class="tb">' + cg + '<thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>' + ''.join(
        '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>'


def ul(xs):
    return '<ul class="list">' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'


capa = '''<section class="page cover"><div class="chk" style="top:0"></div><div class="in">
<div style="font-size:8pt;letter-spacing:3px;color:#ffb98a;font-weight:600">PLANO DE AÇÃO · 90 DIAS · VERSÃO 2</div>
<h1 style="margin-top:38mm">Do zero ao<span>primeiro cliente</span></h1>
<p class="sub">Posicionamento seguro diante do conselho (sem CRN), palavras-chave revisadas e um plano semana a semana para crescer o perfil e fechar clientes em Recife.</p>
<div class="meta"><span>Para: <b>[Seu nome]</b></span><span>Foco: <b>Recife e RMR</b></span><span>14/11/2026</span></div>
</div><div class="chk" style="bottom:0"></div></section>'''

p2 = page(2, '''<div class="k">01 · O que diz a regra</div><h2>O conselho e <span>o seu trabalho</span></h2>
<div class="warn" style="margin-bottom:4mm"><b>Importante:</b> esta é uma análise informativa a partir das normas públicas, não um parecer jurídico. Antes de lançar o perfil, confirme por escrito com o CRN-6 (a fiscalização tem caráter orientador) ou com um advogado.</div>''' +
          tbl(['Norma', 'O que diz', 'O que significa para você'], [
              ['<b>Lei 8.234/1991, art. 3º</b>', 'São privativas do nutricionista, entre outras: planejamento, organização, direção, supervisão e avaliação de serviços de alimentação e nutrição; e assistência, consultoria e assessoria em nutrição.', 'O risco não está na palavra “consultoria” sozinha, e sim em oferecer serviço de <b>nutrição</b> ou de <b>planejamento e supervisão do serviço de alimentação</b>.'],
              ['<b>STF · ADI 803 (2017)</b>', 'Manteve as atividades como privativas.', 'A regra está em vigor e é aplicada.'],
              ['<b>Resolução CFN 596/2017</b>', 'Exercer atividade privativa sem habilitação é infração penal; bacharel atuando sem inscrição no CRN também é infração.', 'Nunca se apresentar como nutricionista nem prometer serviço de nutrição.'],
              ['<b>Resolução CFN 600/2018</b>', 'Inclui o “serviço comercial de alimentação” (restaurantes) entre as áreas do nutricionista.', 'Restaurante é área do conselho: a comunicação precisa deixar claro que o seu serviço é de <b>negócio</b> (custos, vendas e marca).'],
              ['<b>Resolução CFN 605/2018</b>', 'Define a ficha técnica de preparação com receita, componentes, valor nutritivo, per capita e custo.', 'Fale em <b>ficha de custo</b> e <b>receita padronizada</b>, sem valor nutricional.'],
          ], ['22%', '40%', '38%']) +
          '<div class="h3x">A leitura estratégica</div>' + ul([
              'O espaço livre é o <b>lado de negócio</b> do restaurante: custo, preço, margem, cardápio como ferramenta de venda, compras, marca e Instagram. Não existe profissão regulamentada exclusiva para isso.',
              'A zona de risco é tudo que soa como <b>nutrição</b> ou como <b>comando técnico da cozinha</b> (planejar, supervisionar ou responder tecnicamente pelo serviço de alimentação).',
              'Por isso, o posicionamento muda de “consultoria de gestão” para <b>“lucro e marca para restaurantes”</b>: mais seguro e, para o dono, mais atraente.']))

p3 = page(3, '''<div class="k">02 · Mapa de risco</div><h2>O que dizer e <span>o que evitar</span></h2>
<div class="grid3" style="gap:3mm">
<div class="card g"><h4>Livre</h4><ul><li>Custos, CMV, margem e lucro</li><li>Precificação e preço de venda</li><li>Cardápio como ferramenta de venda (design, organização, engenharia de cardápio)</li><li>Identidade visual, marca e Instagram</li><li>Compras e negociação com fornecedores</li><li>Processos administrativos e atendimento</li></ul></div>
<div class="card y"><h4>Com cuidado</h4><ul><li>Ficha técnica → dizer <b>ficha de custo</b> ou <b>receita padronizada</b></li><li>Padronização de porções → pelo lado do <b>custo e da margem</b></li><li>Organização da rotina → pelo lado do <b>tempo e do desperdício</b></li><li>Fotos de cozinha → mostrar o negócio, não orientar sobre higiene ou segurança dos alimentos</li></ul></div>
<div class="card r"><h4>Evitar</h4><ul><li>Nutrição, nutricionista, “nutri”</li><li>Consultoria ou assessoria em nutrição ou alimentação</li><li>Valor nutricional, cardápio saudável, dieta</li><li>Responsável técnico, assinar documentos técnicos</li><li>“Planejo, organizo e supervisiono a sua cozinha”</li><li>Boas práticas e segurança dos alimentos como serviço seu</li></ul></div></div>
<div class="h3x">Troca de vocabulário</div>''' + tbl(['Em vez de', 'Use'], [
    ['Consultora / consultoria de gestão', '“Trabalho com custos, cardápio e marca para restaurantes”'],
    ['Ficha técnica de preparação', 'Ficha de custo · receita padronizada'],
    ['Diagnóstico', 'Análise de lucro · análise de cardápio'],
    ['Organizo e supervisiono a sua cozinha', 'Coloco o seu custo e o seu cardápio em ordem'],
    ['Planejamento de cardápio', 'Cardápio que vende · organização do cardápio'],
    ['Padronização da produção', 'Mesma porção, mesmo custo, todo dia'],
], ['45%', '55%']) +
    '<div class="h3x">Proteções práticas</div>' + ul([
        '<b>Contrato:</b> descrever o objeto como “análise de custos, precificação, organização do cardápio, identidade visual e marketing”.',
        '<b>Documentos entregues:</b> sem campo de responsável técnico assinado por você e sem informação nutricional (as fichas da Speciale já seguem isso).',
        '<b>Parceria:</b> quando o cliente precisar de algo privativo (rotulagem nutricional, cardápio para dietas, responsável técnico), indicar uma nutricionista registrada parceira.',
        '<b>Quando tiver o CRN:</b> o posicionamento pode crescer; até lá, nada de “nutri” em nome, @, bio ou legenda.']))

prof_bio = '<br>'.join(BIO)
p4 = page(4, f'''<div class="k">03 · Posicionamento</div><h2>Nome, bio <span>e perfil</span></h2>
<div class="grid2" style="gap:6mm">
<div><div class="h3x" style="margin-top:0">Nome do perfil (campo de busca)</div>
<div class="box" style="margin:0"><b style="font-family:'Roboto Condensed';font-size:12.5pt">{NOME}</b></div>
<p class="small" style="margin-top:1.5mm">Junta “restaurantes” (o termo que o dono usa) com o resultado que ele quer (lucro) e o seu diferencial (marca). Sem “consultoria” e sem “nutri”. O campo aceita até 64 caracteres.</p>
<div class="h3x">Alternativas</div>{ul(['[Seu nome] | Custos e Cardápio para Restaurantes', '[Seu nome] · Restaurante com Lucro · Recife'])}
<div class="h3x">Bio · {BIO_LEN} caracteres</div><div class="box" style="margin:0;font-size:9.6pt;line-height:1.6">{prof_bio}</div>
<p class="small" style="margin-top:1.5mm">Limite: 150 caracteres (cada emoji pode contar 2).</p></div>
<div><div class="h3x" style="margin-top:0">Por que funciona</div>{ul(['<b>Linha 1:</b> para quem e o resultado (lucro).', '<b>Linha 2:</b> os 4 assuntos, todos da zona livre.', '<b>Linha 3:</b> o diferencial: do preço ao Instagram, entregue pronto.', '<b>Linha 4:</b> cidade e oferta de entrada (análise gratuita).'])}
<div class="h3x">Complementos</div>{ul(['<b>@:</b> curto, sem números e sem “nutri”, ex.: [seunome].restaurantes', '<b>Categoria:</b> uma categoria de negócios ou de marketing, sem “nutrição” e sem “consultor”.', '<b>Link:</b> WhatsApp com a mensagem pronta “Quero minha análise de lucro”.', '<b>Destaques:</b> Comece aqui · Custos · Cardápio · Marca · Antes e depois · Como funciona', '<b>Foto:</b> você, rosto visível, fundo neutro ou cozinha. Perfil de pessoa cresce mais rápido que logotipo.'])}</div></div>''')

A = [('CMV / como calcular CMV', 'Aprender', 'Alta', 'Legenda, capa de Reels'),
     ('Preço de venda / precificação', 'Aprender', 'Alta', 'Legenda, capa de Reels'),
     ('Restaurante sem lucro / vende mas não lucra', 'Aprender', 'Alta', 'Gancho da legenda'),
     ('Gestão de restaurante / lucro restaurante', 'Comparar', 'Alta', 'Nome (variação), legenda'),
     ('Cardápio que vende / engenharia de cardápio', 'Comparar', 'Alta', 'Legenda, capa'),
     ('Ficha de custo / receita padronizada', 'Aprender', 'Média', 'Legenda, texto alternativo'),
     ('Marketing para restaurantes / Instagram de restaurante', 'Contratar', 'Média', 'Legenda, hashtag'),
     ('Identidade visual para restaurante', 'Contratar', 'Média', 'Legenda, hashtag'),
     ('Taxa do iFood / lucro no delivery', 'Aprender', 'Média', 'Legenda'),
     ('Compras / desperdício / estoque', 'Aprender', 'Média', 'Legenda')]
p5 = page(5, '''<div class="k">04 · Palavras-chave revisadas</div><h2>O que usar <span>agora</span></h2>
<p class="lead" style="margin-bottom:2mm">Somente termos da zona livre. Prioridades são hipóteses até a validação (contagem de posts e sugestões da busca).</p>''' +
          tbl(['Termo (grupo A · dor do dono)', 'Intenção', 'Prioridade', 'Onde usar'], A, ['44%', '14%', '12%', '30%']) +
          '<div class="h3x">Grupo B · local</div><p style="font-size:8.6pt">Recife, Pernambuco, Olinda, Jaboatão, Paulista, Camaragibe e os bairros: Boa Viagem, Pina, Casa Forte, Graças, Espinheiro, Aflitos, Parnamirim, Madalena, Torre e Recife Antigo. Usar na localização do post e nas legendas de bastidores.</p>' +
          '<div class="h3x">Grupo C · hashtags</div>' + tbl(['Uso', 'Hashtags', 'Situação'], [
              ['Prospecção (onde os negócios postam)', '#gastronomiarecife · #recifefood · #restaurantesrecife · #deliveryrecife · #pizzariarecife · #hamburgueriarecife · #cafeteriarecife', 'Validar o total de posts'],
              ['Seus posts (tema)', '#gestaoderestaurantes · #cmv · #precificacao · #cardapio · #marketingpararestaurantes · #foodservice', 'Validar o total de posts'],
              ['Retiradas por segurança', '#consultoriarestaurante · #consultoriafoodservice · #nutri…', 'Não usar até ter o CRN'],
              ['Descartada', '#gestãocozinha', 'Menos de 100 posts'],
          ], ['30%', '50%', '20%']))

phases = [('Semana 0', 'Montar a base', ['Nome, @, bio, foto e link do WhatsApp (página 4).', 'Criar os 6 destaques, cada um com 1 a 3 stories.', 'Publicar 6 posts de base: “quem sou e o que faço”, “como funciona a análise de lucro”, 2 carrosséis de custo (CMV e preço de venda), 1 antes e depois da Speciale (com autorização) e 1 Reels de bastidor.', 'Preparar as 3 iscas (página 8).', 'Seguir 100 perfis do grupo C: restaurantes de Recife, Abrasel-PE, Sebrae PE e distribuidoras.']),
          ('Semanas 1 a 4', 'Ser vista', ['Frequência: 3 Reels + 2 carrosséis + stories todos os dias.', 'Reels de até 30 segundos, com gancho nos 2 primeiros segundos e a palavra-chave escrita na tela.', 'Usar os Reels de teste do Instagram (quando disponíveis na sua conta) para mostrar o vídeo primeiro a quem não te segue.', 'Rotina de prospecção da página 9 todos os dias úteis.', 'Meta: 10 conversas iniciadas e 4 análises gratuitas (hipótese).']),
          ('Semanas 5 a 8', 'Pegar emprestada a audiência', ['Fazer 2 posts em colaboração (recurso “Collab”) com restaurantes ou fornecedores de Recife: o post aparece para os seguidores dos dois.', 'Gravar “um dia na cozinha de [restaurante]” mostrando custo e cardápio, nunca orientação de higiene ou nutrição.', 'Comentar todo dia em perfis grandes do setor (Abrasel-PE, perfis de gastronomia de Recife) com comentários de valor.', 'Lançar a isca CMV em Reels.', 'Meta: 8 análises e 2 propostas (hipótese).']),
          ('Semanas 9 a 12', 'Converter', ['Publicar resultados reais (antes e depois, depoimentos) de quem fez a análise ou contratou.', 'Uma semana temática: “Semana do cardápio que vende”, com stories diários e caixinha de perguntas.', 'Oferta com prazo: “5 análises de lucro gratuitas este mês”.', 'Recalcular a rotina com as taxas reais de resposta e de fechamento.', 'Meta: 30 análises no total e 5 clientes (hipótese da meta).'])]
p6 = page(6, '<div class="k">05 · Plano de ação</div><h2>Do zero em <span>90 dias</span></h2>' + ''.join(
    f'<div class="phase"><div class="w">{w}<small>{t}</small></div><ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul></div>' for w, t, xs in phases) +
    '<p class="small" style="margin-top:2.5mm">Metas são hipóteses derivadas da meta de 30 análises e 5 clientes. Ajuste após a semana 4 com os números reais.</p>')

pil = [('Lucro e custos', ['CMV alto? Os 3 erros que mais vejo em restaurantes de Recife.', 'Como calcular o CMV de um produto em 5 passos.', 'Vende bem e não sobra dinheiro? Olhe o CMV, não o faturamento.', 'Preço de venda: por que copiar o concorrente dá prejuízo.', 'Taxa do iFood: a conta do lucro no delivery.']),
       ('Cardápio que vende', ['Onde o cliente olha primeiro no cardápio.', 'Preço repetido em cada sabor atrasa o pedido.', 'Cardápio digital: o pedido chega pronto no WhatsApp.', 'Reforma ou cores novas? O cardápio muda junto.', 'Antes e depois: cardápio de uma pizzaria em Recife.*']),
       ('Mesma porção, mesmo lucro', ['Ficha de custo: o que precisa ter.', 'A mesma pizza com 3 pesos diferentes custa caro.', 'Receita padronizada: a equipe faz igual sem você na cozinha.', 'Desperdício começa na porção que ninguém pesa.', 'Bastidor: fichas de custo de uma pizzaria, do zero ao PDF.*']),
       ('Marca e Instagram', ['O cliente decide pelo Instagram antes de entrar.', 'Foto do prato: 3 ajustes que dão vontade de pedir.', 'Mesa “instagramável”: o cliente divulga por você.', 'Identidade visual: quando a marca precisa mudar.', 'Um dia em [bairro]: custo, cardápio e marca de um negócio real.'])]
pil_html = ''.join(f'<div class="card"><h4>{t}</h4><ol style="padding-left:4.5mm;font-size:7.9pt;line-height:1.45">' + ''.join(f'<li style="margin:1mm 0">{x}</li>' for x in xs) + '</ol></div>' for t, xs in pil)
p7 = page(7, f'''<div class="k">06 · Conteúdo</div><h2>4 pilares, <span>20 posts</span></h2>
<div class="grid2" style="gap:4mm">{pil_html}</div>
<p class="small" style="margin-top:2mm">Palavra-chave nas 2 primeiras linhas da legenda, repetida na capa e no texto alternativo. *Usar o case só com autorização da casa. Todos os temas estão na zona livre.</p>
<div class="h3x">Formatos que fazem um perfil novo crescer</div>''' + tbl(['Formato', 'Para quê', 'Frequência'], [
    ['Reels curto (até 30 s) com gancho', 'Alcançar quem não te segue', '3 por semana'],
    ['Carrossel com passo a passo', 'Ser salvo e compartilhado (mostra autoridade)', '2 por semana'],
    ['Stories com enquete e caixinha', 'Criar conversa com quem já segue', 'Todos os dias'],
    ['Post em colaboração (Collab)', 'Aparecer para a audiência de outro perfil', '2 por mês, a partir da semana 5'],
], ['36%', '44%', '20%']))

p8 = page(8, '''<div class="k">07 · Iscas e oferta de entrada</div><h2>Como transformar <span>seguidor em conversa</span></h2>
<div class="grid3" style="gap:3mm">
<div class="card"><h4>Comente CUSTO</h4><p>Modelo de ficha de custo pronto para preencher (sem informação nutricional).</p></div>
<div class="card"><h4>Comente CMV</h4><p>Passo a passo de 1 página para calcular o CMV de 1 produto.</p></div>
<div class="card"><h4>Comente CARDÁPIO</h4><p>Checklist dos erros que fazem o cliente demorar a pedir.</p></div></div>
<div class="h3x">Oferta de entrada: análise de lucro gratuita</div>''' + ul([
    '<b>O que é:</b> 30 minutos, presencial ou online, para calcular com o dono o custo real e a margem de 1 produto e apontar 3 melhorias no cardápio.',
    '<b>Por que funciona:</b> o dono sai com um número concreto; você mostra o seu método sem prometer nada técnico de nutrição.',
    '<b>Como fechar:</b> no fim, apresentar a proposta curta (4 páginas) com o próximo passo: ficha de custo do cardápio inteiro, cardápio novo ou marca.']) +
    '<div class="h3x">Prova social desde o primeiro mês</div>' + ul([
        'Antes e depois do cardápio e das fichas da Speciale (com autorização).',
        'Print (com permissão) de mensagens de quem fez a análise.',
        'Números reais: “o CMV da pizza X caiu de __% para __%” só depois de medido.']))

p9 = page(9, '''<div class="k">08 · Prospecção</div><h2>Rotina de <span>30 minutos</span></h2>
<div class="grid3" style="gap:3mm">
<div class="card"><div class="n">1</div><h4>Aproximação</h4><p><b>Dia 1.</b> Seguir e fazer 1 comentário útil num post recente. Ex.: “Esse combo ficou bom. Vale mostrar o preço por pessoa, ajuda quem está decidindo.”</p></div>
<div class="card"><div class="n">2</div><h4>Mensagem de valor</h4><p><b>2 a 3 dias depois.</b> “Oi, [nome]! Trabalho com custos, cardápio e marca para restaurantes aqui em Recife. Reparei em [observação]. Vocês sabem quanto sobra de lucro na [produto mais vendido]?”</p></div>
<div class="card hl"><div class="n">3</div><h4>Convite</h4><p><b>Se responder.</b> “Faço uma análise gratuita de 30 min: calculo com vocês o custo e a margem de 1 produto. Posso te chamar no WhatsApp?”</p></div></div>
<p class="small" style="margin-top:2mm">Sem resposta: no máximo 1 lembrete após 5 dias.</p>
<div class="h3x">Semana tipo</div>''' + tbl(['Dia', 'Conteúdo', 'Prospecção (30 min)'], [
    ['<b>Seg</b>', 'Reels (pilar lucro e custos)', '10 comentários em 1 hashtag do grupo C'],
    ['<b>Ter</b>', 'Carrossel (cardápio)', '10 comentários em 1 localização · mensagens da etapa 2'],
    ['<b>Qua</b>', 'Reels com isca', 'Responder DMs e comentários da isca'],
    ['<b>Qui</b>', 'Carrossel (porção e custo)', '10 perfis entre seguidores de Abrasel-PE ou fornecedor · convites da etapa 3'],
    ['<b>Sex</b>', 'Reels (marca ou bastidor)', 'Planilha de métricas (10 min)'],
    ['<b>Todos</b>', 'Stories', 'Responder em até 1 hora quem chamar'],
], ['10%', '38%', '52%']) +
    '<div class="h3x">Métricas (toda sexta)</div>' + tbl(['Métrica', 'Onde ver', 'Referência (hipótese)'], [
        ['Alcance de não seguidores', 'Painel profissional', 'Crescer semana a semana'],
        ['Salvamentos e compartilhamentos', 'Painel profissional', 'Mostram quais temas dão autoridade'],
        ['Perfis abordados / conversas iniciadas', 'Planilha', '50 / acompanhar a taxa de resposta'],
        ['Análises gratuitas feitas', 'Agenda', '2 a 3 por semana (30 em 90 dias)'],
        ['Propostas e clientes', 'Planilha', '5 clientes em 90 dias'],
    ], ['40%', '24%', '36%']))

p10 = page(10, '''<div class="k">09 · Antes de lançar</div><h2>Checklist <span>e fontes</span></h2>
<ul class="chk-l" style="list-style:none;font-size:9pt;line-height:1.9">
<li>☐ Confirmar por escrito com o CRN-6 (ou com um advogado) que o posicionamento “lucro e marca para restaurantes” não configura atividade privativa.</li>
<li>☐ Revisar nome, @, bio, destaques e legendas: sem “nutri”, “nutrição”, “consultoria em nutrição” e “responsável técnico”.</li>
<li>☐ Ajustar contrato e proposta: objeto = custos, precificação, cardápio, identidade visual e marketing.</li>
<li>☐ Combinar com uma nutricionista registrada as indicações para demandas privativas.</li>
<li>☐ Pedir autorização da Speciale para usar o case.</li>
<li>☐ Validar as hashtags do grupo C e de tema (total de posts) e anotar na planilha.</li>
<li>☐ Preparar as 3 iscas antes do primeiro Reels com “comente”.</li></ul>
<div class="h3x">Fontes consultadas (14/11/2026)</div><ul class="src">
<li>Lei nº 8.234/1991 (regulamenta a profissão de nutricionista): www2.camara.leg.br/legin/fed/lei/1991/lei-8234-17-setembro-1991-363145</li>
<li>STF · ADI 803 (2017), atividades privativas de nutricionista: migalhas.com.br/quentes/266284</li>
<li>Resolução CFN 596/2017 (infrações de pessoa física): cfn.org.br/wp-content/uploads/resolucoes/Res_596_2017.htm</li>
<li>Resolução CFN 600/2018 (áreas de atuação, inclui serviço comercial de alimentação): cfn.org.br/wp-content/uploads/resolucoes/Res_600_2018.htm</li>
<li>Resolução CFN 605/2018 (definição de ficha técnica de preparação): cfn.org.br/wp-content/uploads/resolucoes/resolucoes_old/Res_605_2018.htm</li>
<li>Código de Ética e de Conduta do Nutricionista (Res. CFN 599/2018; verificar se há norma mais recente): cfn.org.br/wp-content/uploads/resolucoes/Res_599_2018.html</li>
<li>Folder de fiscalização do CFN (caráter orientador): cfn.org.br/wp-content/uploads/2024/08/Folder.pdf</li>
<li>Busca no Instagram (prints de 14/11/2026): #consultoriarestaurante 5.000+, #consultoriafoodservice 1.000+, #gestãocozinha &lt;100.</li></ul>
<p class="small" style="margin-top:3mm">Documento informativo. Não substitui orientação do CRN-6 nem parecer de advogado.</p>''')

open('plano_v2.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano de ação · Instagram</title>{PCSS}{DEXTRA}{EXTRA}</head><body>{capa}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}</body></html>')
print('bio', BIO_LEN)
