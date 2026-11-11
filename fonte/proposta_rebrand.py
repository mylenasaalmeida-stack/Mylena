"""Proposta comercial · Identidade visual, rebrand e cardápio · Speciale Pizzas Artesanais."""

CSS = '''<style>
@import url('fonts.css');
:root{--ink:#1f1a17;--muted:#6f6560;--line:#e7ddd2;--paper:#faf6f0;--accent:#c8361f;--accent2:#e07a2e;--soft:#f3ebe1}
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Poppins',sans-serif;color:var(--ink);font-size:8.8pt;line-height:1.5;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.C{font-family:'Roboto Condensed',sans-serif;font-weight:800}
.top{position:absolute;left:18mm;right:18mm;top:11mm;display:flex;justify-content:space-between;font-size:6.8pt;color:var(--muted);letter-spacing:.6px;text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:2.5mm}
.top b{color:var(--ink);font-weight:600}
.bd{position:absolute;left:18mm;right:18mm;top:24mm;bottom:18mm}
.ft{position:absolute;left:18mm;right:18mm;bottom:9mm;display:flex;justify-content:space-between;font-size:6.6pt;color:var(--muted)}
.kick{font-size:7.2pt;font-weight:600;color:var(--accent);letter-spacing:1.6px;text-transform:uppercase}
h2{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:25pt;line-height:1;text-transform:uppercase;margin:1.5mm 0 4mm}
h3{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:12pt;text-transform:uppercase;margin:5mm 0 2mm}
p.lead{font-size:10pt;color:#3d3531;max-width:160mm;margin-bottom:4mm}
ul.d{padding-left:4.5mm}ul.d li{margin:1.3mm 0}ul.d li::marker{color:var(--accent)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.card{background:var(--paper);border-radius:6px;padding:4.5mm 5mm;border:1px solid var(--line)}
.card h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:11pt;text-transform:uppercase;margin-bottom:1.5mm}
.card .n{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:22pt;color:var(--accent);line-height:1}
.card p{font-size:8.2pt;color:#3d3531}
.card.hl{border:1.5px solid var(--accent);background:#fff}
.tag{display:inline-block;font-size:6.6pt;font-weight:700;letter-spacing:.6px;padding:1px 7px;border-radius:3px;background:var(--accent);color:#fff;text-transform:uppercase;vertical-align:2px;margin-left:4px}
table{width:100%;border-collapse:collapse;font-size:8.3pt}
th{background:var(--ink);color:#fff;font-family:'Roboto Condensed',sans-serif;font-weight:700;font-size:7.8pt;text-transform:uppercase;letter-spacing:.3px;text-align:left;padding:6px 8px}
td{padding:5.5px 8px;border-bottom:1px solid var(--line);vertical-align:top}
tbody tr:nth-child(even) td{background:var(--paper)}
td.r,th.r{text-align:right;white-space:nowrap}
td b{font-weight:600}
.price{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:12pt}
.old{text-decoration:line-through;color:var(--muted);font-size:8pt;margin-right:4px}
.q{counter-reset:q}
.q li{list-style:none;position:relative;padding:1.4mm 0 1.4mm 8mm;border-bottom:1px dotted #d8ccbf;font-size:8.3pt}
.q li:before{counter-increment:q;content:counter(q);position:absolute;left:0;top:1.4mm;font-family:'Roboto Condensed',sans-serif;font-weight:800;color:var(--accent)}
.sw{display:flex;gap:2mm;margin:2.5mm 0}
.sw span{flex:1;height:13mm;border-radius:4px;position:relative}
.sw span i{position:absolute;left:1.5mm;bottom:1mm;font-style:normal;font-size:5.8pt;font-weight:600}
.note{font-size:7.2pt;color:var(--muted);margin-top:2mm}
.box{border-left:3px solid var(--accent);background:var(--soft);padding:3.5mm 5mm;border-radius:0 6px 6px 0;margin-top:4mm;font-size:8.5pt}
.box b{color:var(--accent)}
.steps{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm;margin:2mm 0 3mm}
.steps div{background:var(--ink);color:#fff;border-radius:5px;padding:3mm;font-size:7.4pt;line-height:1.35}
.steps b{display:block;font-family:'Roboto Condensed',sans-serif;font-size:9.5pt;color:#ffb98a;margin-bottom:1mm}
.sign{display:grid;grid-template-columns:1fr 1fr;gap:14mm;margin-top:14mm;text-align:center;font-size:7.4pt;color:var(--muted)}
.sign div{border-top:1px solid var(--ink);padding-top:2mm}
/* capa */
.cover{background:var(--ink);color:#fff}
.cover .chk{position:absolute;left:0;right:0;height:10px;background:repeating-conic-gradient(var(--accent) 0 25%,transparent 0 50%) 0 0/10px 10px;opacity:.9}
.cover .in{position:absolute;left:20mm;right:20mm;top:26mm;bottom:22mm}
.cover .k{font-size:8pt;letter-spacing:3px;color:#ffb98a;font-weight:600;text-transform:uppercase}
.cover h1{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:44pt;line-height:.95;text-transform:uppercase;margin-top:38mm}
.cover h1 span{display:block;color:var(--accent2)}
.cover .sub{font-size:11pt;margin-top:8mm;max-width:140mm;color:#e9e0d7}
.cover .meta{position:absolute;left:0;right:0;bottom:0;display:grid;grid-template-columns:repeat(3,1fr);gap:6mm;font-size:8pt;color:#cfc4ba;border-top:1px solid #4a403b;padding-top:5mm}
.cover .meta b{display:block;color:#fff;font-size:9.5pt;font-weight:600}
.logo{display:flex;align-items:center;gap:8px}
.logo .w b{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:16pt;display:block;line-height:1}
.logo .w i{font-style:normal;font-size:5pt;letter-spacing:2.6px;font-weight:600}
</style>'''

PROV = '[Seu nome ou estúdio]'
DATA = '11 de novembro de 2026'
T = 10
LOGO = ('<svg width="40" height="30" viewBox="0 0 46 34"><ellipse cx="9" cy="15" rx="8.5" ry="7" fill="#fff"/>'
        '<ellipse cx="18" cy="27" rx="8" ry="6.5" fill="#fff"/><path d="M18 13 C21 4 33 1 45 2 C42 10 31 15 18 13Z" fill="#3aa63a"/></svg>')


def page(n, sec, body):
    return (f'<section class="page"><div class="top"><span><b>Speciale Pizzas Artesanais</b> · Proposta de identidade visual e cardápio</span><span>{sec}</span></div>'
            f'<div class="bd">{body}</div><div class="ft"><span>{PROV} · Proposta válida por 15 dias a partir de {DATA}</span><span>{n} / {T}</span></div></section>')


def tbl(head, rows, widths=None, right=()):
    cg = '<colgroup>' + ''.join(f'<col style="width:{w}">' for w in widths) + '</colgroup>' if widths else ''
    th = ''.join(f'<th class="{"r" if i in right else ""}">{h}</th>' for i, h in enumerate(head))
    tr = ''.join('<tr>' + ''.join(f'<td class="{"r" if i in right else ""}">{c}</td>' for i, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<table>{cg}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def ul(items, cls='d'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


cover = f'''<section class="page cover"><div class="chk" style="top:0"></div>
<div class="in"><div class="logo">{LOGO}<div class="w"><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i></div></div>
<h1>Nova fase,<span>nova marca</span></h1>
<p class="sub">Proposta de identidade visual, rebrand e novo cardápio para acompanhar a mudança de cores e a nova infraestrutura da Speciale Pizzas Artesanais.</p>
<div class="meta"><div><b>Cliente</b>Speciale Pizzas Artesanais · Recife</div><div><b>Preparado por</b>{PROV}</div><div><b>Data</b>{DATA}</div></div>
</div><div class="chk" style="bottom:0"></div></section>'''

p2 = page(2, 'Contexto', '''<div class="kick">01 · Contexto</div><h2>Onde a Speciale está hoje</h2>
<p class="lead">A Speciale vive um momento de mudança: novas cores, reforma do espaço e uma operação que já está sendo padronizada por dentro. A marca e o cardápio precisam acompanhar esse passo.</p>
<div class="grid2"><div class="card"><h4>O que a casa já tem de forte</h4>''' + ul([
    'Pizza artesanal, com <b>massa própria</b> e <b>forno a lenha</b>.',
    'Operação em padronização: fichas técnicas, receitas de produção e guias já prontos para a equipe.',
    'Três tamanhos definidos (Broto, Média e Grande) e sabores clássicos com receita fechada.',
    'Uma marca reconhecida pelo nome <b>Speciale</b>.']) + '''</div>
<div class="card"><h4>O que está mudando</h4>''' + ul([
    '<b>Cores da marca:</b> a paleta atual (vermelho, laranja e creme) vai mudar.',
    '<b>Infraestrutura do local:</b> reforma do espaço, com impacto em ambiente, mobiliário e sinalização.',
    '<b>Padrão de produto:</b> porções e tamanhos sendo medidos e documentados.',
    '<b>Decisão em aberto:</b> manter, ajustar ou trocar a logo.']) + '''</div></div>
<h3>Objetivos desta proposta</h3>''' + ul([
    'Criar uma <b>identidade visual coerente</b> com as novas cores e o novo espaço, aplicável em todos os pontos de contato (fachada, salão, caixas, uniformes, redes e delivery).',
    'Construir um <b>novo cardápio</b>, físico e digital, alinhado à nova marca e ao padrão de produto da casa.',
    'Dar à Speciale <b>opções claras de investimento</b>: identidade visual, cardápio ou os dois em combo.']) +
    '<div class="box"><b>Como ler esta proposta:</b> as páginas 3 a 5 explicam o porquê das mudanças e trazem as decisões que precisamos tomar juntos. As páginas 6 a 8 detalham o que será entregue. As páginas 9 e 10 trazem investimento, prazos e próximos passos.</div>')

p3 = page(3, 'Por que o cardápio vai mudar', '''<div class="kick">02 · Cardápio</div><h2>Por que o cardápio vai ter que mudar</h2>
<p class="lead">O cardápio é a peça da marca que o cliente mais segura na mão. Quando cores, espaço e produto mudam, ele precisa mudar junto, ou passa a contradizer o resto da casa.</p>''' + tbl(
    ['Motivo', 'O que acontece se o cardápio não mudar', 'O que o novo cardápio resolve'], [
        ['<b>Novas cores da marca</b>', 'O cardápio antigo fica com a paleta velha e destoa da fachada, do salão, das caixas e das redes.', 'Cardápio na nova paleta, com a mesma tipografia e os mesmos elementos da marca.'],
        ['<b>Nova infraestrutura</b>', 'Formato, tamanho e material pensados para o espaço antigo: podem não funcionar com as novas mesas, a nova iluminação ou o novo balcão.', 'Formato escolhido para o novo espaço: mesa, parede, balcão ou display, com material resistente ao uso.'],
        ['<b>Produto padronizado</b>', 'Descrições, tamanhos e porções desatualizados em relação às fichas técnicas.', 'Descrições fiéis às receitas, tamanhos com número de fatias e informação de alérgenos.'],
        ['<b>Leitura e venda</b>', 'Sabores organizados sem estratégia: o cliente demora para escolher e os carros-chefe não aparecem.', 'Engenharia de cardápio: destaque para os sabores mais pedidos e mais rentáveis, leitura rápida.'],
        ['<b>Canais digitais</b>', 'Versões diferentes no salão, no WhatsApp e nos aplicativos de delivery.', 'Uma versão-mãe, adaptada para impresso, PDF, QR Code e aplicativos.'],
        ['<b>Fotos e imagem</b>', 'Fotos antigas ou de banco de imagem, que não mostram a pizza real.', 'Plano de fotos reais da casa, no novo estilo visual.'],
    ], widths=['20%', '40%', '40%']) +
    '<div class="box"><b>Resumo:</b> trocar só as cores do cardápio antigo resolve a aparência por pouco tempo. O ganho real vem de reconstruir o cardápio junto com a nova marca, usando o padrão de produto que a casa já está criando.</div>')

p4 = page(4, 'A logo', '''<div class="kick">03 · Decisão</div><h2>A logo: manter, ajustar ou mudar?</h2>
<p class="lead">Antes de começar, precisamos decidir o que acontece com a logo atual (“SPECIALE · Pizzas Artesanais”). Com as cores mudando, ela vai mudar pelo menos de cor. A pergunta é até onde ir.</p>
<div class="grid3">
<div class="card"><div class="n">A</div><h4>Manter</h4><p>A logo fica como está e só ganha as novas cores. A identidade nova é construída em volta dela.</p><p style="margin-top:2mm"><b>A favor:</b> menor custo e menor risco; o cliente reconhece na hora.<br><b>Contra:</b> pode parecer “velha” no espaço novo.</p></div>
<div class="card hl"><div class="n">B</div><h4>Ajustar <span class="tag">sugerido</span></h4><p>Redesenho da logo atual: melhora letras, proporções e símbolo, mantendo o reconhecimento.</p><p style="margin-top:2mm"><b>A favor:</b> marca atualizada sem perder quem já conhece a casa.<br><b>Contra:</b> exige trocar a logo em todos os materiais.</p></div>
<div class="card"><div class="n">C</div><h4>Mudar</h4><p>Logo nova, do zero, para marcar uma nova fase.</p><p style="margin-top:2mm"><b>A favor:</b> maior impacto e liberdade criativa.<br><b>Contra:</b> maior investimento; precisa comunicar a mudança aos clientes.</p></div>
</div>
<h3>Perguntas para decidir</h3><ol class="q">''' + ''.join(f'<li>{x}</li>' for x in [
    'O que vocês gostam e o que não gostam na logo atual?',
    'Os clientes reconhecem a Speciale pela logo, pelo nome ou pelo produto?',
    'A expressão “Pizzas Artesanais” continua fazendo parte da marca?',
    'Onde a logo aparece hoje (fachada, caixas, uniformes, sacolas, redes, aplicativos)? Há estoque de caixas ou materiais impressos?',
    'A marca e a logo estão registradas no INPI? Se a logo mudar, vale pedir um novo registro.',
    'A reforma inclui fachada nova? Ela já tem projeto ou prazo?',
    'Quem toma a decisão final sobre a logo?']) + '</ol>')

dirs = [
    ('Forno & Brasa', 'Calor do forno a lenha: tons queimados, terrosos e um laranja de brasa. Ar artesanal e acolhedor.', [('#2b211d', 'Carvão', '#fff'), ('#b5482a', 'Terracota', '#fff'), ('#e08a3c', 'Brasa', '#fff'), ('#efe3d0', 'Farinha', '#2b211d')]),
    ('Italiana contemporânea', 'Clássico italiano com leitura moderna: vinho, verde-oliva e muito espaço em branco. Ar mais sofisticado.', [('#5c1f2a', 'Vinho', '#fff'), ('#6b7442', 'Oliva', '#fff'), ('#d9c7a5', 'Trigo', '#2b211d'), ('#fbf8f2', 'Off-white', '#2b211d')]),
    ('Recife artesanal', 'Raiz local com cores vivas do Nordeste: tomate, verde de folha e azul de azulejo. Ar alegre e próximo.', [('#d23b2a', 'Tomate', '#fff'), ('#2f7a4f', 'Manjericão', '#fff'), ('#2d5b8a', 'Azulejo', '#fff'), ('#f4ecdc', 'Areia', '#2b211d')]),
]
dcards = ''.join(f'''<div class="card"><h4>{t}</h4><div class="sw">{"".join(f'<span style="background:{c}"><i style="color:{fc}">{n}</i></span>' for c, n, fc in sw)}</div><p>{d}</p></div>''' for t, d, sw in dirs)
p5 = page(5, 'Direções criativas', f'''<div class="kick">04 · Ponto de partida</div><h2>Direções criativas iniciais</h2>
<p class="lead">Três caminhos para começar a conversa. São hipóteses, não a proposta final: a direção escolhida será desenvolvida depois do briefing e precisa conversar com as cores e os materiais da reforma.</p>
<div class="grid3">{dcards}</div>
<h3>Perguntas sobre a nova fase</h3><ol class="q">''' + ''.join(f'<li>{x}</li>' for x in [
    'As novas cores já foram definidas (por exemplo, pelo arquiteto da reforma)? Se sim, quais?',
    'Qual sensação o cliente deve ter ao entrar na nova Speciale: acolhedora, sofisticada, descontraída, familiar?',
    'Quem é o cliente principal: famílias, casais, jovens, delivery? Mudou com a reforma?',
    'Quais pizzarias ou marcas vocês admiram (em Recife ou fora)? E quais não querem parecer?',
    'O forno a lenha e a massa artesanal devem ser o centro da comunicação?',
    'A reforma muda o modelo de atendimento (mais salão, mais delivery, balcão, retirada)?',
    'Há data de reabertura ou de inauguração do novo espaço?']) + '</ol>')

p6 = page(6, 'Escopo · Identidade visual', '''<div class="kick">05 · Escopo</div><h2>Identidade visual e rebrand</h2>
<div class="steps"><div><b>1. Imersão</b>Briefing, visita ao espaço e conversa com a equipe.</div><div><b>2. Pesquisa</b>Concorrência em Recife e referências.</div><div><b>3. Conceito</b>Painel de referências e direção escolhida.</div><div><b>4. Criação</b>Logo, cores, fontes e elementos.</div><div><b>5. Entrega</b>Manual da marca e arquivos finais.</div></div>''' + tbl(
    ['Entregável', 'Manter (A)', 'Ajustar (B)', 'Mudar (C)'], [
        ['Imersão, pesquisa e direção criativa', '✓', '✓', '✓'],
        ['Logo', 'Nova versão de cor', 'Redesenho da atual', 'Logo nova (2 propostas)'],
        ['Versões da logo (horizontal, vertical, símbolo, uma cor)', 'Só cor', '✓', '✓'],
        ['Paleta de cores com códigos para gráfica, tela e tinta', '✓', '✓', '✓'],
        ['Tipografia (fontes de títulos e textos)', '✓', '✓', '✓'],
        ['Elementos gráficos (padrões, ícones, texturas)', '✓', '✓', '✓'],
        ['Aplicações: caixa de pizza, sacola, uniforme, cartão, adesivo', '3 peças', '5 peças', '5 peças'],
        ['Kit digital: avatar, capa e modelos de post para redes', '✓', '✓', '✓'],
        ['Orientação de cores e sinalização para a reforma (fachada e salão)', '—', '✓', '✓'],
        ['Manual da marca (PDF)', 'Guia resumido', 'Manual completo', 'Manual completo'],
        ['Rodadas de ajuste', '2', '2 por etapa', '2 por etapa'],
    ], widths=['46%', '18%', '18%', '18%']) +
    '<p class="note">A orientação de fachada e salão é visual (cores, logo, posição e tamanho). O projeto e a execução de obra, placas e letreiros ficam com o arquiteto e os fornecedores.</p>')

p7 = page(7, 'Escopo · Cardápio', '''<div class="kick">06 · Escopo</div><h2>Novo cardápio</h2>
<div class="steps"><div><b>1. Conteúdo</b>Sabores, preços, tamanhos e regras da casa.</div><div><b>2. Estrutura</b>Engenharia de cardápio: ordem e destaques.</div><div><b>3. Textos</b>Nomes e descrições no tom da marca.</div><div><b>4. Layout</b>Versão impressa e digital.</div><div><b>5. Arquivos</b>Arquivos para gráfica, PDF e QR Code.</div></div>''' + tbl(
    ['Entregável', 'Incluso'], [
        ['Organização do conteúdo: categorias, sabores, tamanhos (Broto, Média e Grande) e fatias', '✓'],
        ['Engenharia de cardápio: posição e destaque dos carros-chefe e dos sabores mais rentáveis', '✓'],
        ['Descrições dos sabores revisadas a partir das fichas técnicas, com alérgenos', '✓'],
        ['Layout do cardápio de mesa (até 4 páginas ou 2 lâminas frente e verso)', '✓'],
        ['Versão digital: PDF leve para WhatsApp e página com QR Code para as mesas', '✓'],
        ['Arquivos prontos para a gráfica, com acompanhamento da prova de impressão', '✓'],
        ['Indicação de material e acabamento para o novo espaço', '✓'],
        ['Rodadas de ajuste', '2'],
    ], widths=['85%', '15%'], right=(1,)) + '''<h3>Adicionais opcionais</h3>''' + tbl(
    ['Adicional', 'Para que serve'], [
        ['Cardápio de parede, lousa ou display de balcão', 'Para o novo espaço, se houver venda no balcão'],
        ['Adaptação para aplicativos de delivery', 'Fotos e textos no padrão de cada aplicativo'],
        ['Direção de fotografia', 'Roteiro e acompanhamento das fotos das pizzas com fotógrafo contratado pela casa'],
        ['Atualização dos documentos internos', 'Fichas técnicas, receitas de produção e guias na nova identidade'],
    ], widths=['40%', '60%']) +
    '<p class="note">Os valores dos adicionais estão na página 9.</p>')

qs = [
    ('Formato e uso', ['O cardápio será usado no salão, no delivery ou nos dois?', 'Quantos cardápios físicos serão necessários (mesas, balcão)?', 'Qual formato combina com o novo espaço: cardápio de mesa, lâmina, parede ou display?', 'Preferência de material: papel plastificado, PVC, MDF, couro sintético?', 'Haverá QR Code nas mesas? Vocês usam algum sistema de cardápio digital ou de pedidos?']),
    ('Conteúdo', ['Quantos sabores salgados e doces vão entrar? Algum sabor vai sair ou entrar?', 'Quais são os carros-chefe e quais dão mais lucro?', 'Há entradas, bebidas, sobremesas, combos ou promoções fixas?', 'A casa aceita meio a meio, borda recheada ou adicionais? Como é a regra de preço?', 'Há opções vegetarianas, sem lactose ou outras restrições que precisam aparecer?']),
    ('Preços e tamanhos', ['Os preços serão revisados junto com o novo cardápio?', 'O preço é o mesmo no salão, na retirada e no delivery?', 'Os diâmetros de Média e Broto já foram medidos? O cardápio vai mostrar centímetros ou só fatias?']),
    ('Imagem e tom', ['O cardápio terá fotos? Vocês têm fotógrafo ou querem indicação?', 'Qual tom de voz combina com a casa: clássico, descontraído, regional?', 'A história da casa (forno a lenha, massa própria) deve aparecer no cardápio?']),
    ('Informações e aprovação', ['Quais informações fixas entram: horário, telefone, WhatsApp, redes, formas de pagamento, Wi-Fi?', 'Quem aprova o conteúdo e o layout? Até quando o cardápio precisa estar pronto?', 'Há orçamento reservado para a impressão?']),
]
qhtml = ''.join(f'<div><h3 style="margin-top:3mm">{t}</h3><ol class="q">' + ''.join(f'<li>{x}</li>' for x in items) + '</ol></div>' for t, items in qs)
p8 = page(8, 'Perguntas para o cardápio', f'''<div class="kick">07 · Briefing</div><h2>Perguntas para fechar o cardápio</h2>
<p class="lead" style="margin-bottom:1mm">As respostas definem o tamanho do trabalho e evitam retrabalho. Podemos fazer juntos em uma reunião de cerca de uma hora.</p>
<div class="grid2" style="gap:2mm 7mm">{qhtml}</div>''')

pkg = tbl(['Pacote', 'O que inclui', 'Prazo', 'Investimento'], [
    ['<b>Só o cardápio</b>', 'Escopo da página 7, usando cores e fontes já definidas pela casa', '3 semanas', '<span class="price">R$ 1.500</span>'],
    ['<b>Identidade A · Manter a logo</b>', 'Logo nas novas cores + identidade + guia resumido', '3 semanas', '<span class="price">R$ 2.500</span>'],
    ['<b>Identidade B · Ajustar a logo</b>', 'Redesenho da logo + identidade + manual completo', '5 semanas', '<span class="price">R$ 3.800</span>'],
    ['<b>Identidade C · Logo nova</b>', 'Logo nova + identidade + manual completo', '6 semanas', '<span class="price">R$ 5.500</span>'],
], widths=['26%', '46%', '12%', '16%'], right=(3,))
combo = tbl(['Combo (identidade + cardápio)', 'Separado', 'No combo', 'Economia'], [
    ['<b>Combo A</b> · Manter a logo + cardápio', 'R$ 4.000', '<span class="price">R$ 3.500</span>', 'R$ 500'],
    ['<b>Combo B</b> · Ajustar a logo + cardápio <span class="tag">recomendado</span>', 'R$ 5.300', '<span class="price">R$ 4.600</span>', 'R$ 700'],
    ['<b>Combo C</b> · Logo nova + cardápio', 'R$ 7.000', '<span class="price">R$ 6.000</span>', 'R$ 1.000'],
], widths=['46%', '16%', '20%', '18%'], right=(1, 2, 3))
extras = tbl(['Adicional', 'Investimento'], [
    ['Definição de cores e fontes só para o cardápio (se a casa não tiver identidade definida)', 'R$ 500'],
    ['Cardápio de parede, lousa ou display de balcão', 'R$ 400'],
    ['Adaptação para aplicativos de delivery', 'R$ 350'],
    ['Direção de fotografia (o fotógrafo é contratado à parte)', 'R$ 600'],
    ['Atualização dos documentos internos (fichas, receitas e guias)', 'R$ 400'],
], widths=['80%', '20%'], right=(1,))
p9 = page(9, 'Investimento', f'''<div class="kick">08 · Investimento</div><h2>Pacotes e combos</h2>
<h3 style="margin-top:0">Serviços separados</h3>{pkg}<h3>Combos com desconto</h3>{combo}<h3>Adicionais</h3>{extras}
<div class="box"><b>Recomendação:</b> o Combo B (ajustar a logo + cardápio) atualiza a marca para a nova fase sem perder o reconhecimento que a Speciale já tem, e entrega o cardápio pronto para a reabertura.</div>''')

p10 = page(10, 'Condições e próximos passos', '''<div class="kick">09 · Condições</div><h2>Prazos, condições e próximos passos</h2>
<div class="grid2"><div><h3 style="margin-top:0">Condições comerciais</h3>''' + ul([
    '<b>Pagamento:</b> 50% na aprovação da proposta e 50% na entrega dos arquivos finais. Pix ou transferência; parcelamento a combinar.',
    '<b>Prazos:</b> contam a partir do pagamento da entrada e do envio das informações do briefing. No combo, o cardápio é feito logo depois da identidade aprovada.',
    '<b>Ajustes:</b> as rodadas de ajuste estão descritas em cada escopo. Ajustes extras ou mudança de direção depois da aprovação são orçados à parte.',
    '<b>Arquivos:</b> ao final, a Speciale recebe os arquivos abertos e finais, com direito de uso da marca.',
    '<b>Validade:</b> 15 dias a partir da data desta proposta.']) + '''</div><div><h3 style="margin-top:0">Não incluso</h3>''' + ul([
    'Impressão do cardápio, caixas, sacolas, uniformes e adesivos (indicamos fornecedores e acompanhamos a prova).',
    'Fotografia profissional (cachê do fotógrafo).',
    'Projeto e execução de fachada, placas, letreiros e obra.',
    'Gestão de redes sociais e anúncios.',
    'Taxas de registro de marca no INPI.']) + '''</div></div>
<h3>Próximos passos</h3><div class="steps"><div><b>1</b>Escolher o pacote ou combo.</div><div><b>2</b>Decidir o caminho da logo (A, B ou C).</div><div><b>3</b>Reunião de briefing com as perguntas das páginas 4, 5 e 8.</div><div><b>4</b>Pagamento da entrada.</div><div><b>5</b>Início da imersão e do cronograma.</div></div>
<h3>Aceite</h3><p>Pacote escolhido: ☐ Só cardápio &nbsp; ☐ Identidade A &nbsp; ☐ Identidade B &nbsp; ☐ Identidade C &nbsp; ☐ Combo A &nbsp; ☐ Combo B &nbsp; ☐ Combo C</p>
<p style="margin-top:2mm">Adicionais: ________________________________________________</p>
<div class="sign"><div>Speciale Pizzas Artesanais · nome e data</div><div>''' + PROV + ''' · nome e data</div></div>''')

open('proposta_rebrand.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Proposta · Identidade visual e cardápio · Speciale</title>{CSS}</head><body>{cover}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}</body></html>')
