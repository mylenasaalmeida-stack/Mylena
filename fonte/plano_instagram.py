"""Plano de Instagram · consultoria food service Recife (A4 retrato, formato da proposta)."""
from proposta_v2 import CSS as PCSS
from digital import EXTRA as DEXTRA

NOME = '[Seu nome] | Consultoria Food Service Recife'
BIO = ['Consultoria em gestão para Food Service', 'CMV • Ficha técnica • Cardápio', 'Vou à sua cozinha e entrego tudo pronto', '📍 Recife · 👇 Diagnóstico gratuito']
BIO_LEN = len('\n'.join(BIO))
T = 8

EXTRA = '''<style>
.pill{display:inline-block;font-size:6.6pt;font-weight:700;padding:1px 6px;border-radius:3px;white-space:nowrap}
.hi{background:#c8361f;color:#fff}.me{background:#f3d7c6;color:#7a2a17}.lo{background:#e7ddd2;color:#555}
.tb td,.tb th{font-size:7.9pt}
.prof{width:76mm;border-radius:9mm;background:#1a1a1a;padding:2.4mm;box-shadow:0 4mm 9mm rgba(0,0,0,.25)}
.prof .s{background:#fff;border-radius:7mm;overflow:hidden;padding:8mm 4.5mm 5mm;font-size:6.6pt;line-height:1.4;color:#111}
.av{width:17mm;height:17mm;border-radius:50%;background:#0e100f;display:flex;align-items:center;justify-content:center;color:#9fd18b;font-family:'Roboto Condensed';font-weight:800;font-size:12pt;border:.7mm solid #2f8a4e}
.st{display:grid;grid-template-columns:repeat(3,1fr);text-align:center;font-size:6pt;flex:1}
.st b{display:block;font-size:8pt}
.hls{display:flex;gap:2.5mm;margin-top:3mm}
.hls div{text-align:center;font-size:5.2pt;width:12mm}
.hls span{display:flex;width:11mm;height:11mm;border-radius:50%;border:.4mm solid #ccc;margin:0 auto 1mm;align-items:center;justify-content:center;background:#0e100f;color:#9fd18b;font-family:'Roboto Condensed';font-weight:800;font-size:6pt}
.grid9{display:grid;grid-template-columns:repeat(3,1fr);gap:.6mm;margin-top:3mm}
.grid9 div{aspect-ratio:1;background:#0e100f;color:#fff;font-family:'Roboto Condensed';font-weight:800;font-size:5.2pt;text-transform:uppercase;display:flex;align-items:flex-end;padding:1.2mm;line-height:1.05}
.grid9 div:nth-child(even){background:#2f8a4e}
.grid2{display:grid;grid-template-columns:1fr 1fr}.grid3{display:grid;grid-template-columns:repeat(3,1fr)}
.card{background:var(--paper);border:1px solid var(--line);border-radius:6px;padding:4mm 4.5mm}
.card h4{font-family:'Roboto Condensed';font-weight:800;font-size:11pt;text-transform:uppercase;margin-bottom:1.5mm}
.card p{font-size:8pt;color:#3d3531;line-height:1.45}
.card .n{font-family:'Roboto Condensed';font-weight:800;font-size:20pt;color:var(--acc);line-height:1}
.card.hl{border:1.5px solid var(--acc);background:#fff}
.src{font-size:7.6pt;line-height:1.55}.src li{margin:1.4mm 0;word-break:break-all}
.small{font-size:7.6pt;color:var(--muted)}
</style>'''


def page(n, body):
    return (f'<section class="page"><div class="in" style="top:16mm">{body}</div><div class="ft"><span>Plano de Instagram · consultoria em gestão para food service · Recife</span>'
            f'<span>{n} / {T}</span></div></section>')


def pr(p):
    return {'A': '<span class="pill hi">Alta</span>', 'M': '<span class="pill me">Média</span>', 'B': '<span class="pill lo">Baixa</span>'}[p]


def tbl(head, rows, widths):
    cg = '<colgroup>' + ''.join(f'<col style="width:{w}">' for w in widths) + '</colgroup>'
    return '<table class="tb">' + cg + '<thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>' + ''.join(
        '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>'


capa = '''<section class="page cover"><div class="chk" style="top:0"></div><div class="in">
<div style="font-size:8pt;letter-spacing:3px;color:#ffb98a;font-weight:600">ESTUDO E PLANO · 90 DIAS</div>
<h1 style="margin-top:40mm">Instagram que<span>fecha clientes</span></h1>
<p class="sub">Palavras-chave, perfil, conteúdo e rotina de prospecção para uma consultoria de gestão em food service em Recife e Região Metropolitana.</p>
<div class="meta"><span>Para: <b>[Seu nome]</b></span><span>Foco: <b>Recife e RMR</b></span><span>14/11/2026</span></div>
</div><div class="chk" style="bottom:0"></div></section>'''

p2 = page(2, '''<div class="k">01 · Diagnóstico</div><h2>O mercado e <span>a busca</span></h2>
<div class="flow" style="grid-template-columns:repeat(3,1fr)">
<div><b>~100 mil</b><h4>Estabelecimentos</h4><p>de food service em Pernambuco (dados da Abrasel-PE citados pelo Diario de Pernambuco, 2026).</p></div>
<div><b>~metade</b><h4>No azul</h4><p>Só cerca de metade do setor no estado fechou julho de 2025 com lucro (pesquisa Abrasel). A dor do cliente ideal é real.</p></div>
<div><b>Instagram</b><h4>Canal do setor</h4><p>Estudo da UFRPE mostra restaurante do Recife que usa o Instagram como única divulgação.</p></div></div>
<div class="h3x">Leitura</div><ul class="list">
<li>O dono do negócio está no Instagram, divulgando o próprio estabelecimento. É lá que ele pode ser encontrado e abordado.</li>
<li>Não foi encontrada consultoria local com posicionamento forte em ficha técnica, CMV e cardápio juntos: <b>há espaço para ocupar essa posição</b> (hipótese a confirmar na busca do Instagram).</li></ul>
<div class="h3x">Como a busca do Instagram funciona hoje</div>''' + tbl(['Campo', 'Peso na busca', 'Como usar'], [
    ['<b>Nome do perfil</b>', 'O maior', 'Palavra principal + Recife'],
    ['<b>Legenda</b>', 'Alto', 'Palavra-chave nas 2 primeiras linhas, antes do “mais”'],
    ['<b>Texto alternativo e capa de Reels</b>', 'Médio', 'Repetir o termo do post'],
    ['<b>Hashtags</b>', 'Reforço', '3 a 5 na legenda (nos comentários não são indexadas)'],
    ['<b>Bio</b>', 'Divergente entre fontes', 'Escrever para pessoas: entender em 3 segundos'],
], ['30%', '22%', '48%']) + '<p class="small" style="margin-top:2mm">Fontes de mercado (não oficiais da Meta). Lista completa na página 8. Perfis profissionais públicos também podem aparecer no Google.</p>')

A = [('CMV / como calcular CMV', 'Aprender', 'A', 'Legenda, capa de Reels, #cmv'),
     ('Ficha técnica (pizza, hambúrguer, prato)', 'Aprender', 'A', 'Nome, legenda, capa, texto alternativo'),
     ('Preço de venda / precificação de cardápio', 'Aprender', 'A', 'Legenda, capa de Reels'),
     ('Restaurante sem lucro / vendo mas não lucro', 'Aprender', 'A', 'Gancho da legenda, capa'),
     ('Consultoria para restaurantes / gastronômica', 'Contratar', 'A', 'Nome, bio, legenda'),
     ('Gestão de restaurante / food service', 'Comparar', 'A', 'Nome, bio, hashtag'),
     ('Custo do prato / custo da pizza', 'Aprender', 'M', 'Legenda, texto alternativo'),
     ('Padronização / receita padrão', 'Aprender', 'M', 'Legenda, capa de Reels'),
     ('Controle de estoque / compras', 'Aprender', 'M', 'Legenda'),
     ('Desperdício na cozinha', 'Aprender', 'M', 'Legenda, capa de Reels'),
     ('Cardápio que vende / engenharia de cardápio', 'Comparar', 'M', 'Legenda, capa de Reels'),
     ('Cardápio digital / pedido no WhatsApp', 'Comparar', 'M', 'Legenda, hashtag'),
     ('Taxa do iFood / lucro no delivery', 'Aprender', 'M', 'Legenda'),
     ('Abrir restaurante, hamburgueria, pizzaria', 'Aprender', 'B', 'Legenda pontual')]
p3 = page(3, '''<div class="k">02 · Palavras-chave</div><h2>Grupo A · <span>a dor do dono</span></h2>
<p class="lead" style="margin-bottom:2mm">O que o dono pesquisa quando sente o problema. Prioridades são hipóteses até a validação da página 5.</p>''' +
          tbl(['Termo', 'Intenção', 'Prioridade', 'Onde usar'], [(f'<b>{t}</b>', i, pr(p), u) for t, i, p, u in A], ['40%', '14%', '13%', '33%']))

B = [('Recife', 'Contratar (com “consultoria”)', 'A', 'Nome, bio, legenda, localização'),
     ('“food service Recife”, “restaurantes em Recife”', 'Comparar', 'A', 'Legenda, texto alternativo'),
     ('Pernambuco / PE', 'Comparar', 'M', 'Legenda, hashtag'),
     ('RMR: Olinda, Jaboatão, Paulista, Camaragibe', 'Contratar', 'M', 'Legenda, localização'),
     ('Bairros: Boa Viagem, Pina, Casa Forte, Graças, Espinheiro, Aflitos, Parnamirim, Madalena, Torre, Recife Antigo', 'Contratar', 'M', 'Localização e legenda de bastidores')]
C = [('#gastronomiarecife · #recifefood · #restaurantesrecife · #comidarecife', 'Divulgar o negócio', 'A', 'Prospecção e posts de bastidores'),
     ('#deliveryrecife', 'Delivery com margem apertada', 'A', 'Prospecção'),
     ('#pizzariarecife · #hamburgueriarecife · #cafeteriarecife · #barrecife', 'Nichos do cliente ideal', 'A', 'Prospecção e posts de nicho'),
     ('Localizações dos bairros do grupo B', 'Negócio físico ativo', 'A', 'Prospecção por bairro'),
     ('Seguidores de Abrasel-PE, Sebrae PE, distribuidoras e eventos (Arena Gastronômica, Recife Love Burger)', 'Donos e gestores', 'A', 'Prospecção mais qualificada'),
     ('#ondecomeremrecife', 'Mais usada por clientes finais', 'B', 'Só para descobrir negócios'),
     ('#recife (cerca de 12,7 milhões de posts)', 'Concorrência altíssima', 'B', 'Evitar sozinha')]
p4 = page(4, '''<div class="k">02 · Palavras-chave</div><h2>Grupos B e C · <span>Recife</span></h2>
<div class="h3x" style="margin-top:2mm">Grupo B · termos locais (sempre junto com um termo do grupo A)</div>''' +
          tbl(['Termo', 'Intenção', 'Prioridade', 'Onde usar'], [(f'<b>{t}</b>', i, pr(p), u) for t, i, p, u in B], ['40%', '22%', '12%', '26%']) +
          '<div class="h3x">Grupo C · onde os estabelecimentos postam (para prospectar)</div>' +
          tbl(['Onde', 'Quem você encontra', 'Prioridade', 'Uso'], [(f'<b>{t}</b>', i, pr(p), u) for t, i, p, u in C], ['42%', '22%', '12%', '24%']))

bio_html = '<br>'.join(BIO)
prof = f'''<div class="prof"><div class="s">
<div style="font-weight:700;font-size:7.4pt;text-align:center;margin-bottom:3mm">[seunome].foodservice</div>
<div style="display:flex;align-items:center;gap:3mm"><div class="av">CF</div><div class="st"><div><b>—</b>posts</div><div><b>—</b>seguidores</div><div><b>—</b>seguindo</div></div></div>
<div style="font-weight:700;margin-top:2.5mm">{NOME}</div>
<div style="color:#666;font-size:6pt">Consultor(a) empresarial</div>
<div style="margin-top:1mm">{bio_html}</div>
<div style="color:#1f5fa8;font-weight:600;margin-top:1mm">wa.me/55819… · Quero meu diagnóstico</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;margin-top:2.5mm"><span style="background:#efefef;border-radius:2mm;text-align:center;padding:1.3mm;font-weight:600">Seguir</span><span style="background:#efefef;border-radius:2mm;text-align:center;padding:1.3mm;font-weight:600">Mensagem</span></div>
<div class="hls"><div><span>CMV</span>CMV</div><div><span>FICHA</span>Ficha</div><div><span>MENU</span>Cardápio</div><div><span>CASE</span>Cases</div><div><span>?</span>Como funciona</div></div>
<div class="grid9"><div>CMV alto? 3 erros</div><div>Ficha técnica sem erro</div><div>Cardápio que vende</div><div>Um dia na cozinha</div><div>Preço de venda</div><div>Antes e depois</div></div></div></div>'''
p5 = page(5, f'''<div class="k">03 · Perfil</div><h2>Nome e bio <span>finais</span></h2>
<div style="display:grid;grid-template-columns:1fr 78mm;gap:7mm;margin-top:3mm">
<div><div class="h3x" style="margin-top:0">Nome do perfil (campo de busca)</div>
<div class="box" style="margin:0"><b style="font-family:'Roboto Condensed';font-size:12.5pt">{NOME}</b></div>
<p class="small" style="margin-top:1.5mm">Junta as 3 palavras que mais pesam: consultoria, food service e Recife. Alternativas: “[Seu nome] • Gestão de Restaurantes Recife” ou “[Seu nome] | CMV e Ficha Técnica”.</p>
<div class="h3x">Bio (para pessoas, em 3 segundos)</div>
<div class="box" style="margin:0;font-size:9.6pt;line-height:1.6">{bio_html}</div>
<p class="small" style="margin-top:1.5mm">{BIO_LEN} caracteres com quebras de linha (limite: 150; cada emoji pode contar 2).</p>
<ul class="list" style="margin-top:2mm">
<li><b>Linha 1:</b> o que faz e para quem.</li>
<li><b>Linha 2:</b> os 3 termos de maior prioridade do grupo A.</li>
<li><b>Linha 3:</b> o diferencial que nenhum concorrente local mostra.</li>
<li><b>Linha 4:</b> cidade e ação.</li></ul>
<div class="h3x">Complementos</div><ul class="list">
<li><b>@:</b> curto, sem números, ex.: [seunome].foodservice</li>
<li><b>Link:</b> WhatsApp com mensagem pronta “Quero meu diagnóstico”.</li>
<li><b>Categoria:</b> Consultor(a) empresarial.</li>
<li><b>Destaques:</b> CMV · Ficha · Cardápio · Cases · Como funciona.</li></ul></div>
<div>{prof}<p class="small" style="text-align:center;margin-top:2mm">Simulação ilustrativa do perfil.</p></div></div>''')

pil = [('Custos e CMV', ['CMV alto? Os 3 erros que mais vejo em restaurantes de Recife.', 'Como calcular o CMV da sua pizza em 5 passos, sem planilha complicada.', 'Vende bem e não sobra dinheiro? Comece olhando o CMV, não o faturamento.', 'Preço de venda: por que copiar o preço do concorrente dá prejuízo.', 'Taxa do iFood e lucro no delivery: a conta que pouca gente faz.']),
       ('Padronização e ficha técnica', ['Ficha técnica: o que ela precisa ter para a equipe seguir sem errar.', 'A mesma pizza com 3 pesos diferentes? Isso é falta de padronização.', 'Receita de produção: a versão da ficha técnica que a cozinha usa.', 'Bastidor: fichas técnicas de uma pizzaria em Recife, do zero ao PDF.*', 'Desperdício na cozinha começa na porção que ninguém pesa.']),
       ('Cardápio e marca', ['Cardápio que vende: onde o cliente olha primeiro.', 'Preço repetido em cada sabor? Isso atrasa a escolha do cliente.', 'Cardápio digital no WhatsApp: o pedido chega pronto, sem aplicativo.', 'Reforma ou cores novas? O cardápio precisa mudar junto.', 'Antes e depois: o cardápio de uma pizzaria em Recife.*']),
       ('Bastidores e gestão em Recife', ['Um dia numa cozinha em [bairro]: o que vejo primeiro na consultoria.', 'Gestão de restaurante: as 5 perguntas do meu diagnóstico.', 'Compras: por que comprar mais barato nem sempre é economia.', 'Food service em Pernambuco: o que os donos mais me perguntam.', 'Como funciona a consultoria: vou à cozinha e entrego tudo pronto.'])]
pil_html = ''.join(f'<div class="card"><h4>{t}</h4><ol style="padding-left:4.5mm;font-size:7.9pt;line-height:1.45">' + ''.join(f'<li style="margin:1mm 0">{x}</li>' for x in xs) + '</ol></div>' for t, xs in pil)
p6 = page(6, f'''<div class="k">04 · Conteúdo</div><h2>4 pilares, <span>20 posts</span></h2>
<div class="grid2" style="gap:4mm">{pil_html}</div>
<p class="small" style="margin-top:2mm">Palavra-chave nas 2 primeiras linhas da legenda, repetida na capa do Reels e no texto alternativo. *Usar o case só com autorização da casa.</p>
<div class="h3x">Iscas para DM (preparar o material antes de publicar)</div>
<div class="grid3" style="gap:3mm">
<div class="card"><h4>Comente FICHA</h4><p>Modelo de ficha técnica pronto para preencher (versão genérica).</p></div>
<div class="card"><h4>Comente CMV</h4><p>Passo a passo de 1 página para calcular o CMV de 1 produto.</p></div>
<div class="card"><h4>Comente CARDÁPIO</h4><p>Checklist dos erros que fazem o cliente demorar a pedir.</p></div></div>''')

p7 = page(7, '''<div class="k">05 · Prospecção</div><h2>Da DM ao <span>diagnóstico</span></h2>
<div class="grid3" style="gap:3mm">
<div class="card"><div class="n">1</div><h4>Aproximação</h4><p><b>Dia 1.</b> Seguir e fazer 1 comentário útil num post recente. Ex.: “Esse combo ficou bom. Vale destacar o preço por pessoa, ajuda quem está decidindo.”</p></div>
<div class="card"><div class="n">2</div><h4>Mensagem de valor</h4><p><b>2 a 3 dias depois.</b> “Oi, [nome]! Sou consultora de gestão para food service aqui em Recife. Reparei em [observação]. Vocês sabem o CMV real da [produto mais vendido]?”</p></div>
<div class="card hl"><div class="n">3</div><h4>Convite</h4><p><b>Se responder.</b> “Faço um diagnóstico gratuito de 30 min: calculo com vocês o custo real e a margem de 1 produto. Posso te chamar no WhatsApp?”</p></div></div>
<p class="small" style="margin-top:2mm">Sem resposta: no máximo 1 lembrete após 5 dias; depois, só interagir nos posts.</p>
<div class="h3x">Rotina semanal (até 30 min por dia)</div>''' + tbl(['Dia', 'O que fazer'], [
    ['<b>Segunda</b>', 'Post do pilar 1 ou 2 · 10 comentários úteis em 1 hashtag do grupo C'],
    ['<b>Terça</b>', '10 comentários em 1 localização de bairro · mensagens da etapa 2'],
    ['<b>Quarta</b>', 'Reels com isca (“comente FICHA”) · responder todas as DMs'],
    ['<b>Quinta</b>', '10 perfis entre seguidores de Abrasel-PE ou distribuidora · convites da etapa 3'],
    ['<b>Sexta</b>', 'Post do pilar 3 ou 4 com localização · preencher a planilha de métricas']], ['18%', '82%']) +
    '<div class="h3x">Métricas (toda sexta)</div>' + tbl(['Métrica', 'Onde ver', 'Referência (hipótese)'], [
        ['Alcance vindo de busca e hashtags', 'Painel profissional', 'Crescer mês a mês'],
        ['Perfis abordados', 'Planilha', '50 por semana'],
        ['DMs iniciadas', 'Instagram', 'Acompanhar a taxa de resposta'],
        ['Diagnósticos marcados', 'Agenda', '2 a 3 por semana (30 em 90 dias)'],
        ['Propostas e clientes fechados', 'Planilha', '5 clientes em 90 dias']], ['40%', '22%', '38%']) +
    '<p class="small" style="margin-top:2mm">Referências derivadas da meta assumida, não de dados de mercado. Após 4 semanas, recalcular com as taxas reais.</p>')

p8 = page(8, '''<div class="k">06 · Validação e fontes</div><h2>Como validar em <span>15 minutos</span></h2>
<ul class="list">
<li><b>Grupo A, na busca do Instagram:</b> digitar o início de cada termo e anotar as sugestões de complemento; ver se os perfis que aparecem são poucos ou fracos.</li>
<li><b>Grupo A, no Google Trends:</b> comparar até 5 termos com filtro Pernambuco e período de 12 meses; manter os de interesse constante.</li>
<li><b>Grupo B:</b> buscar “[termo] Recife” e ver quanto conteúdo local existe.</li>
<li><b>Grupo C:</b> abrir cada hashtag e ver o total de posts e se as publicações recentes são de estabelecimentos.</li>
<li><b>Depois de 30 dias:</b> no painel profissional, ver o alcance vindo de busca e hashtags; manter os termos dos 3 melhores posts.</li></ul>
<div class="h3x">Fontes consultadas (14/11/2026)</div><ul class="src">
<li>Diario de Pernambuco · Food service em PE inclui cerca de 100 mil estabelecimentos (2026): diariodepernambuco.com.br/economia/2026/03/11710315</li>
<li>Movimento Econômico · Setor de alimentação fora do lar comemora volta do crescimento (dez/2025): movimentoeconomico.com.br/estados/pernambuco/2025/12/02</li>
<li>UFRPE · TCC sobre restaurante do Recife e uso do Instagram: repository.ufrpe.br/bitstream/123456789/6283</li>
<li>Folha de Pernambuco · Estabelecimentos de comida apostam em cenários instagramáveis: folhape.com.br/sabores</li>
<li>Folha de Pernambuco · Arena Gastronômica do Carnaval do Recife: folhape.com.br/noticias/abrasel-anuncia-participacao</li>
<li>Conversion · SEO no Instagram: conversion.com.br/blog/seo-no-instagram</li>
<li>Reportei · Social SEO no Instagram: reportei.com/social-seo-no-instagram</li>
<li>Agência Gram · Instagram SEO e buscas 2026: agenciagram.com.br/blog/instagram-seo-buscas-2026</li>
<li>IQ Hashtags · Análise de #recife: iqhashtags.com/hashtags/hashtag/recife</li></ul>
<div class="box" style="margin-top:6mm"><h4>Antes de publicar</h4><ul>
<li>Trocar [Seu nome] e [seunome] pelo nome real.</li>
<li>Confirmar se o diagnóstico será mesmo gratuito e o atendimento online.</li>
<li>Pedir autorização da Speciale para usar o case.</li></ul></div>''')

open('plano_instagram.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano de Instagram</title>{PCSS}{DEXTRA}{EXTRA}</head><body>{capa}{p2}{p3}{p4}{p5}{p6}{p7}{p8}</body></html>')
print('bio chars:', BIO_LEN)
