"""Kit de lançamento do Instagram · Mylena | Cozinha Estratégica (A4 retrato)."""
from proposta_v2 import CSS as PCSS

AT = '@mylena.cozinhaestrategica'
NOME = 'Mylena | Cozinha Estratégica para Restaurantes'
BIO = ['Cozinha estratégica: restaurante que lucra', '✔ Custo certo', '✔ Cardápio que vende', '✔ Marca que atrai', '👇 Diagnóstico de lucro gratuito']
T = 8
A = 'web/artes/'
P = 'web/mylena/'

EXTRA = '''<style>
.grid2{display:grid;grid-template-columns:1fr 1fr}.grid3{display:grid;grid-template-columns:repeat(3,1fr)}
.card{background:var(--paper);border:1px solid var(--line);border-radius:6px}.card h4{font-family:'Roboto Condensed';font-weight:800;font-size:11pt;text-transform:uppercase;margin-bottom:1.5mm}.card p{font-size:7.8pt;color:#3d3531;line-height:1.45}.card.hl{border:1.5px solid var(--acc);background:#fff}
.th{border-radius:4px;overflow:hidden;position:relative;background:#ddd}
.th img{width:100%;height:100%;object-fit:cover;display:block}
.bad{position:absolute;left:2mm;top:2mm;font-size:6.6pt;font-weight:700;padding:1px 6px;border-radius:3px;color:#fff}
.ok{background:#2f8a4e}.no{background:#c8361f}.mid{background:#b07d12}
.cap{font-size:7.4pt;color:#3d3531;margin-top:1.4mm;line-height:1.4}
.cap b{display:block;font-family:'Roboto Condensed';font-size:9pt;text-transform:uppercase;color:var(--ink)}
.lg{background:var(--paper);border-radius:6px;padding:3.5mm 4.5mm;font-size:7.8pt;line-height:1.5;white-space:pre-line;border-left:3px solid var(--acc)}
.lg b{font-family:'Roboto Condensed';font-size:9pt;text-transform:uppercase;display:block;margin-bottom:1mm;white-space:normal}
.small{font-size:7.6pt;color:var(--muted)}
.h3x{font-family:'Roboto Condensed';font-weight:800;font-size:12pt;text-transform:uppercase;margin:5mm 0 2mm}
.list{padding-left:4.5mm;font-size:8.6pt}.list li{margin:1.2mm 0}.list li::marker{color:var(--acc)}
.warn{border:1.5px solid var(--acc);border-radius:6px;padding:3.5mm 4.5mm;font-size:8.2pt;background:#fff}.warn b{color:var(--acc)}
.prof{width:74mm;border-radius:9mm;background:#1a1a1a;padding:2.4mm;box-shadow:0 4mm 9mm rgba(0,0,0,.25)}
.prof .s{background:#fff;border-radius:7mm;overflow:hidden;padding:7mm 4.5mm 4mm;font-size:6.5pt;line-height:1.4;color:#111}
.g9{display:grid;grid-template-columns:repeat(3,1fr);gap:.5mm;margin-top:3mm}.g9 img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block}
</style>'''


def page(n, body):
    return (f'<section class="page"><div class="in" style="top:15mm">{body}</div><div class="ft"><span>Kit de lançamento do Instagram · {AT}</span>'
            f'<span>{n} / {T}</span></div></section>')


def th(src, h, label='', cls='ok', cap=''):
    lb = f'<span class="bad {cls}">{label}</span>' if label else ''
    return f'<div><div class="th" style="height:{h}mm"><img src="{src}">{lb}</div>{cap}</div>'



def tbl_spec():
    rows = [('Margens', '80 px em todos os lados'), ('Linha superior (y 80)', 'Rótulo da seção à esquerda (20 px, caixa alta, 55% de opacidade) · contador à direita'),
            ('Título', 'Playfair Display 600, 72 a 92 px, preto ou off-white; números de destaque 150 a 620 px em verde'),
            ('Apoio', 'Poppins 400, 28 a 32 px, até 2 linhas, 70% de opacidade'),
            ('Rodapé (y 1270)', '@mylena.cozinhaestrategica, 20 px, sempre à esquerda'),
            ('Foto', 'Bloco de 920 × 700 a 760 px a partir de y 150, sem texto sobre o rosto')]
    return '<table class="tb" style="font-size:8pt"><tbody>' + ''.join(f'<tr><td style="width:30%"><b>{a}</b></td><td>{b}</td></tr>' for a, b in rows) + '</tbody></table>'
capa = f'''<section class="page cover"><div class="chk" style="top:0"></div><div class="in">
<div style="font-size:8pt;letter-spacing:3px;color:#ffb98a;font-weight:600">KIT DE LANÇAMENTO · INSTAGRAM</div>
<h1 style="margin-top:38mm">Cozinha<span>estratégica</span></h1>
<p class="sub">Perfil final, escolha das fotos e as primeiras artes prontas para publicar, com legendas e ordem de lançamento.</p>
<div class="meta"><span>Perfil: <b>{AT}</b></span><span>Para: <b>Mylena</b></span><span>15/11/2026</span></div>
</div><div class="chk" style="bottom:0"></div></section>'''

bio_html = '<br>'.join(BIO)
p2 = page(2, f'''<div class="k">01 · Perfil</div><h2>O perfil <span>pronto</span></h2>
<div style="display:grid;grid-template-columns:1fr 76mm;gap:7mm;margin-top:3mm">
<div><div class="h3x" style="margin-top:0">Foto do perfil</div>
<div style="display:flex;gap:5mm;align-items:center"><div style="width:34mm;height:34mm;border-radius:50%;overflow:hidden;border:1mm solid #2f8a4e;flex:none"><img src="{A}00_foto_perfil.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<p style="font-size:8.4pt">Close sorrindo, blazer preto, fundo de feira de food service. No círculo pequeno, só rosto funciona: simpatia e confiança ao mesmo tempo.</p></div>
<div class="h3x">Usuário</div><div class="box" style="margin:0"><b style="font-family:'Roboto Condensed';font-size:12pt">{AT}</b></div>
<div class="h3x">Nome (campo de busca)</div><div class="box" style="margin:0"><b style="font-family:'Roboto Condensed';font-size:12pt">{NOME}</b></div>
<div class="h3x">Bio</div><div class="box" style="margin:0;font-size:9.4pt;line-height:1.6">{bio_html}</div>
<div class="h3x">Complementos</div><ul class="list">
<li><b>Link:</b> WhatsApp com a mensagem pronta “Quero meu diagnóstico”.</li>
<li><b>Destaques:</b> Comece aqui · Custos · Cardápio · Marca · Antes e depois.</li>
<li><b>Sem</b> “nutri”, “nutrição” ou “consultoria” até ter o CRN.</li></ul></div>
<div><div class="prof"><div class="s">
<div style="font-weight:700;font-size:7.2pt;text-align:center;margin-bottom:3mm">{AT[1:]}</div>
<div style="display:flex;align-items:center;gap:3mm"><div style="width:16mm;height:16mm;border-radius:50%;overflow:hidden;flex:none"><img src="{A}00_foto_perfil.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);text-align:center;font-size:5.8pt;flex:1"><div><b style="display:block;font-size:7.6pt">6</b>posts</div><div><b style="display:block;font-size:7.6pt">—</b>seguidores</div><div><b style="display:block;font-size:7.6pt">—</b>seguindo</div></div></div>
<div style="font-weight:700;margin-top:2.5mm">{NOME}</div><div style="margin-top:.8mm">{bio_html}</div>
<div style="color:#1f5fa8;font-weight:600;margin-top:1mm">wa.me/55… · Quero meu diagnóstico</div>
<div class="g9"><img src="{A}03_bastidor_feira.jpg"><img src="{A}02_carrossel_1_capa.jpg"><img src="{A}01_fixado_1_quem_sou.jpg">
<img src="{A}02_carrossel_2_erro1.jpg"><img src="{A}01_fixado_2_case.jpg"><img src="{A}02_carrossel_5_cta.jpg"></div></div></div>
<p class="small" style="text-align:center;margin-top:2mm">Simulação: como o perfil fica após os primeiros posts.</p></div></div>''')

fotos = [('close-sorrindo_ed', 'Perfil', 'ok', 'Foto 3 · close sorrindo', 'Foto do perfil e post de bastidor.'),
         ('feira-sorrindo_ed', 'Feed', 'ok', 'Foto 1 · feira, sorrindo', 'Capa do post fixado “Prazer, sou a Mylena”.'),
         ('feira-seria_ed', 'Feed', 'ok', 'Foto 2 · feira, séria', 'Capa de carrossel de autoridade.'),
         ('selfie-preta_ed', 'Stories', 'mid', 'Foto 9 · blusa preta', 'Capa de Reels e stories com texto.'),
         ('selfie-tatuagem', 'Stories', 'mid', 'Foto 7 · blusa preta, pose', 'Stories do dia a dia; tom mais pessoal.'),
         ('selfie-ai', 'Evitar', 'no', 'Foto 8 · editada por IA', 'Marca “Meta AI”: no começo, autenticidade pesa.'),
         ('jaleco-1', 'Não usar', 'no', 'Fotos 4 e 6 · jaleco', 'Bordado “Nutricionista” sem CRN: risco com o conselho.'),
         ('jaleco-ai', 'Não usar', 'no', 'Foto 5 · jaleco, IA', 'Mesmo risco, e editada por IA.')]
p3 = page(3, '''<div class="k">02 · Fotos</div><h2>Qual foto <span>usar onde</span></h2>
<div class="grid3" style="gap:4mm 5mm;grid-template-columns:repeat(4,1fr)">''' + ''.join(
    th(P + f + '.jpg', 52, l, c, f'<div class="cap"><b>{t}</b>{d}</div>') for f, l, c, t, d in fotos) + '''</div>
<div class="warn" style="margin-top:5mm"><b>Fotos de jaleco:</b> o bordado “Mylena Almeida · Nutricionista” apresenta uma profissão que ainda não pode ser exercida sem o CRN. Guarde para depois do registro.</div>
<div class="h3x">Fotos para produzir nas próximas semanas</div><ul class="list">
<li>Numa cozinha ou balcão, conversando com o dono ou o pizzaiolo.</li>
<li>Segurando o cardápio impresso ou a ficha de custo (com autorização do cliente).</li>
<li>No notebook, com a planilha de custos ou o cardápio na tela.</li>
<li>Detalhe das mãos: pesando ingrediente, marcando o cardápio, apontando um número.</li></ul>
<p class="small">Mesma roupa da feira (blazer preto e blusa clara) para manter a identidade com a paleta preta e verde.</p>''')

p4 = page(4, f'''<div class="k">03 · Posts fixados</div><h2>Três posts <span>fixados</span></h2>
<p class="lead" style="margin-bottom:3mm">Três posts fixados: quem sou (foto + gancho “Seu restaurante não precisa vender mais. Precisa lucrar com o que já vende.”), case da pizzaria (só com autorização da casa) e a oferta em formato de nota.</p>
<div class="grid3" style="gap:4mm">{th(A + "01_fixado_1_quem_sou.jpg", 70)}{th(A + "01_fixado_2_case.jpg", 70)}{th(A + "01_fixado_3_diagnostico.jpg", 70)}</div>
<div class="lg" style="margin-top:5mm"><b>Legenda · fixado 1</b>Lucro no restaurante: o problema quase nunca é vender pouco.
É não saber quanto sobra de cada venda.

Prazer, sou a Mylena 👋
Aqui em Recife, eu ajudo restaurantes, bares e delivery a lucrar com o que já vendem, em três frentes:

1. Custo certo: quanto custa cada prato e quanto sobra de verdade.
2. Cardápio que vende: preço e destaque para o que dá lucro.
3. Marca que atrai: imagem e Instagram que trazem cliente.

Antes de pensar em vender mais, vale descobrir quanto você já ganha.
Faço um diagnóstico de lucro gratuito de 30 minutos: calculamos juntos o custo e a margem de 1 produto do seu cardápio.

👉 Me chama no WhatsApp pelo link da bio.

#gestaoderestaurantes #lucro #cmv #gastronomiarecife #foodservice</div>''')

p5 = page(5, f'''<div class="k">04 · Carrossel de autoridade</div><h2>3 erros que fazem <span>vender e não lucrar</span></h2><p class="lead" style="margin-bottom:3mm">Capa com foto e gancho; um erro por slide em card claro; slide final com foto e “Comente CMV”.</p>
<div class="grid3" style="gap:3mm;grid-template-columns:repeat(5,1fr)">''' + ''.join(th(A + f + '.jpg', 42) for f in ['02_carrossel_1_capa', '02_carrossel_2_erro1', '02_carrossel_3_erro2', '02_carrossel_4_erro3', '02_carrossel_5_cta']) + '''</div>
<div class="lg" style="margin-top:5mm"><b>Legenda</b>Restaurante sem lucro: estes são os 3 erros que mais aparecem quando o caixa enche e o dinheiro não sobra.

1. Copiar o preço do concorrente sem saber o seu custo.
2. Porção sem padrão: cada um serve de um jeito.
3. Olhar só o faturamento e esquecer o CMV.

Qual desses acontece aí? Comente CMV que eu te mando o passo a passo para calcular o CMV de 1 produto do seu cardápio.

#cmv #precificacao #gestaoderestaurantes #restaurantesrecife #foodservice</div>
<p class="small" style="margin-top:2mm">Antes de publicar: preparar o material da isca “CMV” (1 página).</p>''')

p6 = page(6, f'''<div class="k">05 · Bastidor e Reels</div><h2>Mais duas <span>artes</span></h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm">
<div>{th(A + "03_bastidor_feira.jpg", 100)}<div class="lg" style="margin-top:3mm"><b>Legenda · post de bastidor</b>Food service em Recife: estive na [nome da feira] e trouxe o que dá para aplicar no seu restaurante.

[3 aprendizados em tópicos curtos]

Qual novidade você quer que eu traga na próxima?

#foodservice #gastronomiarecife #gestaoderestaurantes</div>
<p class="small" style="margin-top:1.5mm">Trocar [nome da feira] pelo nome real do evento.</p></div>
<div>{th(A + "04_capa_reels.jpg", 120)}<div class="lg" style="margin-top:3mm"><b>Capa de Reels · roteiro (até 30 s)</b>0–2 s: “Seu restaurante vende muito e lucra pouco?”
3–20 s: os 3 erros, um por frase.
21–30 s: “Comente CMV que eu te mando o passo a passo.”</div></div></div>''')

p7 = page(8, '''<div class="k">07 · Lançamento</div><h2>Ordem de <span>publicação</span></h2>''' + '''
<table class="tb" style="font-size:8.6pt"><thead><tr><th>Quando</th><th>O que publicar</th><th>Arte</th></tr></thead><tbody>
<tr><td><b>Dia 1</b></td><td>Trocar foto, nome, @, bio e link. Criar destaques.</td><td>Foto do perfil</td></tr>
<tr><td><b>Dia 1</b></td><td>Post de bastidor (abre o feed com você no mercado).</td><td>Bastidor</td></tr>
<tr><td><b>Dia 2</b></td><td>Carrossel “3 erros” com a isca CMV.</td><td>Carrossel</td></tr>
<tr><td><b>Dia 3</b></td><td>Os 3 posts fixados (quem sou, case, diagnóstico) e fixar no topo.</td><td>Fixado</td></tr>
<tr><td><b>Dia 4</b></td><td>Reels “vende muito e lucra pouco?”.</td><td>Capa de Reels</td></tr>
<tr><td><b>Dias 1 a 7</b></td><td>Stories todo dia: bastidores, enquete “qual o seu maior problema: custo, cardápio ou marca?”.</td><td>Fotos 7 e 9</td></tr>
</tbody></table>
<p class="small" style="margin-top:2mm">Publicar o fixado por último faz ele aparecer como o post mais recente e já fixado no topo. A partir da semana 2, seguir a rotina do plano de ação.</p>
<div class="h3x">Arquivos</div><ul class="list">
<li>As 14 artes e a prévia do grid estão em PNG, prontas para postar, na pasta <b>artes-instagram</b> do repositório.</li>
<li>Formato: posts 1080 × 1350 px (4:5), foto do perfil 1080 × 1080 px, capa de Reels 1080 × 1920 px.</li>
<li><b>Tratamento das fotos:</b> fundo da feira escurecido, dessaturado e desfocado para destacar você; pele com leve correção de contraste e temperatura. Sem alterar rosto ou corpo.</li>
<li><b>Identidade:</b> direção “Bastidor com autoridade”: foto com rosto e gancho em Poppins branco, 1 palavra em itálico verde (Playfair Display); cards de texto em off-white; capas de Reels com caixas brancas.</li></ul>
<div class="box" style="margin-top:5mm"><h4>Antes de publicar</h4><ul>
<li>Confirmar se o @ está disponível.</li>
<li>Preparar o material da isca CMV.</li>
<li>Trocar [nome da feira] e escrever os 3 aprendizados reais.</li></ul></div>''')


DIRS = [('Relatório', 'Recomendada', 'Off-white com tipografia serifada e números grandes, como um relatório anual. Fotos em blocos com margem, linhas finas separando as informações.', 'Off-white · preto · verde nos números', 'Playfair Display + Poppins', 'Número “3” verde ocupando o terço superior; abaixo, “erros que fazem o restaurante vender e não lucrar” em serifa preta; @ pequeno no rodapé.'),
        ('Preto editorial', '', 'Fundo preto, fotos com pouca cor e título em sans condensada clara. Visual premium e dramático.', 'Preto · off-white · verde mínimo', 'Roboto Condensed + Poppins', 'Foto em close ocupando 60% da altura; título “Prazer, sou a Mylena.” em off-white embaixo; nenhum outro elemento.'),
        ('Tabela de custos', '', 'Composições em grade, como uma planilha bonita: colunas, números alinhados e rótulos pequenos.', 'Off-white · preto · verde em um dado por arte', 'Roboto Condensed + Poppins', 'Tabela “Custo · Preço · Margem” com 1 linha preenchida e o rótulo “Margem: ?” em verde.')]
dcards = ''.join(f'''<div class="card{" hl" if r else ""}" style="padding:4mm"><h4>{n} {('<span class="tag">' + r + '</span>') if r else ''}</h4><p>{d}</p>
<p style="margin-top:1.5mm"><b>Paleta:</b> {pa}<br><b>Fontes:</b> {fo}<br><b>Exemplo de capa:</b> {ex}</p></div>''' for n, r, d, pa, fo, ex in DIRS)
pdir = page(3, f'''<div class="k">02 · Direção de arte</div><h2>Três caminhos, <span>uma escolha</span></h2>
<div class="grid3" style="gap:3mm">{dcards}</div>
<div class="h3x">Por que “Relatório”</div><ul class="list">
<li>É a direção que mais diz “entende de dinheiro”: números grandes e linhas de tabela lembram balanço e relatório, sem cara de marketing.</li>
<li>O off-white deixa o feed claro e calmo; o preto entra só nos slides de ação, criando ritmo.</li>
<li>Escala bem: qualquer post novo se monta com título, número, uma frase e uma linha.</li></ul>
<div class="h3x">Grade fixa (1080 × 1350 px)</div>''' + tbl_spec())

GRID = [('01_fixado_1_quem_sou', 'Fixado'), ('04_capa_reels', 'Reels'), ('02_carrossel_1_capa', 'Carrossel'),
        ('03_bastidor_feira', 'Bastidor'), (None, 'Carrossel tipográfico<br>“Como calcular o CMV”'), (None, 'Foto<br>na cozinha de um cliente'),
        (None, 'Preto · número grande<br>“1 produto, 30 min”'), (None, 'Foto<br>notebook com a planilha'), (None, 'Carrossel tipográfico<br>“Preço de venda”')]
def tile(src, lab):
    if src:
        pos = '50% 62%' if 'reels' in src else '50% 50%'
        return f'<div style="aspect-ratio:4/5;overflow:hidden"><img src="{A}{src}.jpg" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"></div>'
    dark = 'Preto' in lab
    return f'<div style="aspect-ratio:4/5;background:{"#0C0E0D" if dark else ("#d9d4c9" if "Foto" in lab else "#F4F1EA")};color:{"#F4F1EA" if dark else "#0C0E0D"};display:flex;align-items:center;justify-content:center;text-align:center;font-size:7pt;padding:3mm;border:1px dashed #b9b2a5">{lab}</div>'
pgrid = page(7, f'''<div class="k">06 · Feed</div><h2>Direção de arte <span>e grid</span></h2>
<div style="display:grid;grid-template-columns:92mm 1fr;gap:8mm;margin-top:3mm">
<div><img src="web/artes/99_previa_grid.jpg" style="width:100%;display:block"></div>
<div><div class="h3x" style="margin-top:0">O que os feeds de referência têm em comum</div><ul class="list">
<li><b>Rosto em quase todo post</b>, em contexto real (palco, evento, casa, cozinha).</li>
<li><b>Gancho escrito na foto</b>: frase curta que provoca, fora do rosto.</li>
<li><b>Cards de texto simples</b> (fundo claro, frase forte) intercalados com as fotos.</li>
<li><b>Prova de autoridade</b>: eventos, cases, parcerias.</li></ul>
<div class="h3x">Regras da direção</div><ol class="list">
<li>60% foto ou vídeo com rosto e gancho; 25% cards de texto; 15% prova (case, evento).</li>
<li>Gancho em até 12 palavras, com 1 palavra em itálico verde.</li>
<li>Gancho sempre no terço inferior, nunca sobre o rosto.</li>
<li>Nunca duas fotos iguais lado a lado.</li>
<li>Fotos reais da cozinha dos clientes são prioridade de produção.</li></ol></div></div>''')
open('kit_ig.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Kit de lançamento do Instagram</title>{PCSS}{EXTRA}</head><body>{capa}{p2}{p3}{p4}{p5}{p6}{pgrid}{p7}</body></html>')
