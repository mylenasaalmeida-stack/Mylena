"""Cardápio digital no site · briefing do projeto e simulação (A4 retrato, formato da proposta)."""
from proposta_v2 import CSS as PCSS, LOGO

G, G2, BK, OW = '#2f8a4e', '#9fd18b', '#0e100f', '#f4f1ea'
PROV = '[Seu nome ou estúdio]'
IG = '@perfildacasa'
SAB = [
    ('Portuguesa', 'Molho de tomate artesanal, muçarela, presunto, ovo cozido, cebola, azeitona preta e orégano.', 'port-foto6', 'Glúten · Leite · Ovo'),
    ('4 Queijos', 'Muçarela, gorgonzola, provolone ralado, catupiry e orégano.', 'q4-foto3', 'Glúten · Leite'),
    ('Frango com Catupiry', 'Frango desfiado, muçarela, catupiry, azeitona preta e orégano.', 'frango-foto1', 'Glúten · Leite'),
    ('Lombinho', 'Lombo fatiado, muçarela, catupiry, azeitona preta e orégano.', 'lombo-foto2', 'Glúten · Leite'),
]

EXTRA = f'''<style>
.phone{{width:62mm;height:128mm;border-radius:8mm;background:#1a1a1a;padding:2.2mm;box-shadow:0 4mm 9mm rgba(0,0,0,.28);flex:none}}
.scr{{width:100%;height:100%;border-radius:6mm;overflow:hidden;background:{BK};color:#fff;position:relative;font-size:5.6pt;line-height:1.35}}
.nt{{position:absolute;top:1.6mm;left:50%;transform:translateX(-50%);width:16mm;height:3.4mm;border-radius:2mm;background:#000;z-index:3}}
.bar{{padding:6.5mm 3.5mm 2.5mm;display:flex;justify-content:space-between;align-items:center;background:{BK};border-bottom:.3mm solid #222}}
.lg{{display:flex;align-items:center;gap:1.4mm}}.lg b{{font-family:'Roboto Condensed';font-weight:800;font-size:8pt;line-height:1;display:block}}.lg i{{font-style:normal;font-size:3pt;letter-spacing:1.2px}}
.tabs{{display:flex;gap:1.5mm;padding:2.2mm 3mm;overflow:hidden;background:{BK}}}
.tabs span{{padding:1mm 2.6mm;border-radius:5mm;border:.25mm solid #333;font-size:5pt;white-space:nowrap}}
.tabs span.on{{background:{G};border-color:{G}}}
.chips{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4mm;padding:0 3mm 2mm}}
.chips div{{border:.3mm solid #2f3a33;border-radius:2mm;text-align:center;padding:1.2mm 0}}
.chips div.on{{border-color:{G2};background:#16271c}}
.chips b{{display:block;font-family:'Roboto Condensed';font-size:7.5pt}}
.it{{display:grid;grid-template-columns:14mm 1fr;gap:2.2mm;padding:2.2mm 3mm;border-bottom:.25mm solid #1f2421;align-items:center}}
.it .pf{{width:14mm;height:14mm;border-radius:2mm;overflow:hidden}}.it .pf img,.hero img{{width:100%;height:100%;object-fit:cover;display:block}}
.it h6{{font-family:'Roboto Condensed';font-weight:700;font-size:7pt;text-transform:uppercase;margin:0}}
.it p{{color:#aab1ab;font-size:4.6pt;margin:.4mm 0 .8mm}}
.it .row{{display:flex;justify-content:space-between;align-items:center}}
.add{{background:{G};color:#fff;border-radius:3mm;width:5mm;height:5mm;display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:7pt}}
.cta{{position:absolute;left:3mm;right:3mm;bottom:3mm;background:{G};border-radius:3mm;padding:2.4mm 3mm;display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:5.8pt}}
.btn{{display:block;border-radius:3mm;padding:2.3mm;text-align:center;font-weight:600;margin-top:1.8mm;font-size:5.8pt}}
.cap2{{font-size:7.4pt;color:#3d3531;text-align:center;margin-top:2.5mm;max-width:62mm}}
.cap2 b{{display:block;font-family:'Roboto Condensed';font-size:10pt;text-transform:uppercase;color:var(--ink)}}
.flow{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-top:5mm}}
.flow div{{background:var(--paper);border-radius:6px;padding:4mm;position:relative}}
.flow b{{font-family:'Roboto Condensed';font-weight:800;font-size:20pt;color:var(--acc);display:block;line-height:1}}
.flow h4{{font-family:'Roboto Condensed';font-weight:800;font-size:10.5pt;text-transform:uppercase;margin:1.5mm 0 1mm}}
.flow p{{font-size:8pt;color:#3d3531}}
.tb{{width:100%;border-collapse:collapse;font-size:8.6pt;margin-top:3mm}}
.tb th{{background:var(--ink);color:#fff;font-family:'Roboto Condensed';text-transform:uppercase;font-size:7.8pt;text-align:left;padding:5px 7px}}
.tb td{{padding:5px 7px;border-bottom:1px solid var(--line);vertical-align:top}}
.tb tr:nth-child(even) td{{background:var(--paper)}}
.two2{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}}
.list{{padding-left:4.5mm;font-size:8.6pt}}.list li{{margin:1.2mm 0}}.list li::marker{{color:var(--acc)}}
h3s{{display:block}}
.h3x{{font-family:'Roboto Condensed';font-weight:800;font-size:12pt;text-transform:uppercase;margin:6mm 0 2mm}}
</style>'''

T = 6


def page(n, body):
    return (f'<section class="page"><div class="in">{body}</div><div class="ft"><span>Speciale Pizzas Artesanais · Cardápio digital no site · briefing e simulação</span>'
            f'<span>{n} / {T}</span></div></section>')


def logo_s():
    return ('<div class="lg"><svg width="6mm" height="4.4mm" viewBox="0 0 46 34"><ellipse cx="9" cy="15" rx="8.5" ry="7" fill="#fff"/><ellipse cx="18" cy="27" rx="8" ry="6.5" fill="#fff"/>'
            f'<path d="M18 13 C21 4 33 1 45 2 C42 10 31 15 18 13Z" fill="{G}"/></svg><div><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i></div></div>')


def phone(inner):
    return f'<div class="phone"><div class="scr"><div class="nt"></div>{inner}</div></div>'


def chips(on=1):
    return '<div class="chips">' + ''.join(f'<div class="{"on" if i == on else ""}"><span style="font-size:4.4pt;color:#aab1ab">{n} · {f} fatias</span><b>R$ {p}</b></div>' for i, (n, f, p) in enumerate([('Broto', 4, 38), ('Média', 5, 45), ('Grande', 8, 68)])) + '</div>'


s_inicio = phone(f'''<div class="hero" style="height:60mm;position:relative"><img src="img/lombo-foto2.jpg">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,16,15,.2),rgba(14,16,15,.95) 92%)"></div>
<div style="position:absolute;left:3.5mm;top:6.5mm">{logo_s()}</div>
<div style="position:absolute;left:3.5mm;right:3.5mm;bottom:3mm"><div style="font-size:4.4pt;letter-spacing:1.4px;color:{G2};font-weight:700">FORNO A LENHA · RECIFE</div>
<div style="font-family:'Roboto Condensed';font-weight:800;font-size:15pt;line-height:.95;text-transform:uppercase;margin-top:1mm">Saiu do<br>forno agora.</div></div></div>
<div style="padding:2mm 3.5mm">
<div style="display:flex;align-items:center;gap:1.4mm;font-size:5pt;color:#cfd3cc"><span style="width:1.8mm;height:1.8mm;border-radius:50%;background:#4cd17a;display:inline-block"></span>Aberto agora · horário a confirmar</div>
<span class="btn" style="background:{G}">Ver cardápio</span>
<span class="btn" style="background:#fff;color:{BK}">Pedir pelo WhatsApp</span>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.8mm"><span class="btn" style="border:.3mm solid #333">Instagram</span><span class="btn" style="border:.3mm solid #333">Como chegar</span></div>
<div style="margin-top:3mm;background:#16271c;border-radius:2.5mm;padding:2mm 2.5mm;font-size:5pt"><b style="color:{G2}">Está na Speciale?</b> Poste e marque {IG}.</div></div>''')

items = ''.join(f'''<div class="it"><div class="pf"><img src="img/{f}.jpg"></div><div><h6>{t}</h6><p>{d}</p>
<div class="row"><span style="font-size:4.4pt;color:{G2}">{a}</span><span class="add">+</span></div></div></div>''' for t, d, f, a in SAB)
s_lista = phone(f'''<div class="bar">{logo_s()}<span style="font-size:5pt;color:#aab1ab">Buscar</span></div>
<div class="tabs"><span class="on">Pizzas</span><span>Bebidas</span><span>Sobremesas</span></div>
<div style="padding:.5mm 3mm 1.5mm;font-size:5pt;color:#aab1ab">1. Escolha o tamanho</div>{chips(1)}
<div style="padding:0 3mm 1mm;font-size:5pt;color:#aab1ab">2. Escolha o sabor</div>{items}
<div class="cta"><span>2 itens · ver pedido</span><span>R$ 113</span></div>''')

t, d, f, a = SAB[1]
s_det = phone(f'''<div class="hero" style="height:52mm;position:relative"><img src="img/{f}.jpg">
<div style="position:absolute;left:3mm;top:6.5mm;width:6mm;height:6mm;border-radius:50%;background:rgba(14,16,15,.75);display:flex;align-items:center;justify-content:center">‹</div></div>
<div style="padding:3mm 3.5mm">
<div style="font-family:'Roboto Condensed';font-weight:800;font-size:12pt;text-transform:uppercase">{t}</div>
<div style="color:#aab1ab;font-size:5.2pt;margin:1mm 0 1.5mm">{d}</div>
<div style="font-size:4.6pt;color:{G2};margin-bottom:2.5mm">Contém: {a}</div>
<div style="font-size:5pt;color:#aab1ab;margin-bottom:1.2mm">Tamanho</div></div>{chips(1)}
<div style="padding:1.5mm 3.5mm"><div style="display:flex;justify-content:space-between;align-items:center;border:.3mm solid #2f3a33;border-radius:2mm;padding:2mm 2.5mm">
<span><b>Meio a meio</b><br><span style="color:#aab1ab;font-size:4.6pt">Escolher o outro sabor</span></span><span style="width:7mm;height:4mm;border-radius:2mm;background:{G};position:relative"><i style="position:absolute;right:.5mm;top:.5mm;width:3mm;height:3mm;border-radius:50%;background:#fff"></i></span></div>
<div style="margin-top:1.8mm;border:.3mm solid #2f3a33;border-radius:2mm;padding:2mm 2.5mm;font-size:5pt;color:#cfd3cc">Outro sabor: <b style="color:#fff">Frango com Catupiry</b></div></div>
<div class="cta"><span>Adicionar ao pedido</span><span>R$ 45</span></div>''')

s_pedido = phone(f'''<div class="bar"><span style="font-size:7pt">‹</span><b style="font-family:'Roboto Condensed';font-size:8pt">SEU PEDIDO</b><span></span></div>
<div style="padding:3mm 3.5mm">
<div style="display:flex;justify-content:space-between;padding:2mm 0;border-bottom:.25mm solid #1f2421"><span><b>Grande · Portuguesa</b><br><span style="color:#aab1ab;font-size:4.6pt">8 fatias</span></span><span>R$ 68</span></div>
<div style="display:flex;justify-content:space-between;padding:2mm 0;border-bottom:.25mm solid #1f2421"><span><b>Média · meio a meio</b><br><span style="color:#aab1ab;font-size:4.6pt">4 Queijos + Frango com Catupiry</span></span><span>R$ 45</span></div>
<div style="display:flex;justify-content:space-between;padding:2.5mm 0;font-weight:700;font-size:7pt"><span>Total</span><span>R$ 113</span></div>
<div style="font-size:5pt;color:#aab1ab;margin:1mm 0">Entrega ou retirada?</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm"><span class="btn" style="background:#16271c;border:.3mm solid {G2};margin:0">Retirada</span><span class="btn" style="border:.3mm solid #333;margin:0">Entrega</span></div>
<div style="margin-top:3mm;background:#e8f5e0;color:#123;border-radius:2.5mm;padding:2.2mm 2.5mm;font-size:4.8pt;line-height:1.45">
<b style="color:{G}">Mensagem pronta no WhatsApp:</b><br>Olá, Speciale! Quero pedir:<br>• 1 Grande Portuguesa · R$ 68<br>• 1 Média meio a meio 4 Queijos + Frango com Catupiry · R$ 45<br>Total: R$ 113 · Retirada</div></div>
<div class="cta" style="background:#25a35a"><span>Enviar pelo WhatsApp</span><span>→</span></div>''')

desk_items = ''.join(f'''<div style="background:#141716;border-radius:2mm;overflow:hidden"><div style="height:20mm"><img src="img/{f}.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div style="padding:2mm"><div style="font-family:'Roboto Condensed';font-weight:700;font-size:6.4pt;text-transform:uppercase">{t}</div><div style="font-size:4.4pt;color:#aab1ab;margin-top:.6mm;line-height:1.35">{d}</div></div></div>''' for t, d, f, a in SAB)
desktop = f'''<div style="width:170mm;margin:0 auto"><div style="background:#1a1a1a;border-radius:4mm 4mm 0 0;padding:2.5mm 2.5mm 0">
<div style="background:{BK};color:#fff;height:74mm;border-radius:2mm 2mm 0 0;overflow:hidden;font-size:5.4pt">
<div style="display:flex;justify-content:space-between;align-items:center;padding:3mm 5mm;border-bottom:.25mm solid #222">{logo_s()}<span style="color:#aab1ab">Cardápio · Sobre · Como chegar · <b style="color:#fff;background:{G};padding:1mm 2.5mm;border-radius:2mm">Pedir pelo WhatsApp</b></span></div>
<div style="display:grid;grid-template-columns:52mm 1fr;gap:5mm;padding:4mm 5mm">
<div><div style="font-size:4.4pt;letter-spacing:1.4px;color:{G2};font-weight:700">PASSO 1 · TAMANHO</div><div style="margin:2mm -3mm 0">{chips(1)}</div>
<div style="font-size:4.4pt;letter-spacing:1.4px;color:{G2};font-weight:700;margin-top:3mm">MEIO A MEIO</div><div style="color:#aab1ab;margin-top:1mm">Escolha dois sabores na mesma pizza.</div>
<div style="font-size:4.4pt;letter-spacing:1.4px;color:{G2};font-weight:700;margin-top:3mm">ALÉRGENOS</div><div style="color:#aab1ab;margin-top:1mm">Indicados em cada sabor.</div></div>
<div><div style="font-size:4.4pt;letter-spacing:1.4px;color:{G2};font-weight:700;margin-bottom:2mm">PASSO 2 · SABOR</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2.5mm">{desk_items}</div></div></div></div></div>
<div style="height:4mm;background:#2a2a2a;border-radius:0 0 3mm 3mm"></div><div style="width:40mm;height:3mm;background:#3a3a3a;margin:0 auto;border-radius:0 0 3mm 3mm"></div></div>'''

capa = f'''<section class="page cover"><div class="chk" style="top:0"></div><div class="in">
<div class="logo">{LOGO}<div><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i></div></div>
<h1>Cardápio<span>no celular</span></h1>
<p class="sub">Briefing e simulação do cardápio digital da Speciale: uma página no site, aberta pelo QR Code da mesa, pelo Instagram ou pelo Google, com o pedido saindo pronto no WhatsApp.</p>
<div class="meta"><span>Para: <b>Speciale Pizzas Artesanais</b></span><span>Por: <b>{PROV}</b></span><span>11/11/2026</span></div>
</div><div class="chk" style="bottom:0"></div></section>'''

p2 = page(2, f'''<div class="k">Como funciona</div><h2>Do QR Code<br><span>ao WhatsApp</span></h2>
<p class="lead">O cardápio físico continua na mesa. O digital é a mesma marca e o mesmo conteúdo, no celular do cliente, sempre com o preço certo.</p>
<div class="flow">
<div><b>1</b><h4>Abre</h4><p>Pelo QR Code da mesa, pelo link na bio do Instagram ou pelo Google.</p></div>
<div><b>2</b><h4>Escolhe</h4><p>Tamanho, sabor e meio a meio, com foto e ingredientes de cada pizza.</p></div>
<div><b>3</b><h4>Confere</h4><p>O pedido soma sozinho e mostra o total antes de enviar.</p></div>
<div><b>4</b><h4>Pede</h4><p>A mensagem chega pronta no WhatsApp da casa. Sem aplicativo e sem taxa por pedido.</p></div></div>
<div class="h3x">Físico e digital, juntos</div>
<table class="tb"><thead><tr><th></th><th>Cardápio físico</th><th>Cardápio digital no site</th></tr></thead><tbody>
<tr><td><b>Onde</b></td><td>Mesa e balcão</td><td>Celular do cliente, na mesa, em casa ou no Instagram</td></tr>
<tr><td><b>Mudar preço ou sabor</b></td><td>Reimprimir</td><td>Atualiza na hora</td></tr>
<tr><td><b>Fotos</b></td><td>Algumas, por espaço</td><td>Uma por sabor, em tamanho grande</td></tr>
<tr><td><b>Pedido</b></td><td>Com o garçom</td><td>Mensagem pronta no WhatsApp</td></tr>
<tr><td><b>Instagram e Google</b></td><td>QR Code impresso</td><td>Link na bio e no perfil do Google</td></tr></tbody></table>
<div class="quote" style="margin-top:7mm">O digital não substitui o físico: <b>os dois usam a mesma marca, os mesmos preços e as mesmas fotos</b>, e o QR Code liga um ao outro.</div>''')

p3 = page(3, f'''<div class="k">Simulação · celular</div><h2>Como o cliente <span>vê</span></h2>
<p class="lead" style="margin-bottom:6mm">Telas ilustrativas com o conteúdo real da casa e os preços definidos (Broto R$ 38 · Média R$ 45 · Grande R$ 68).</p>
<div style="display:flex;justify-content:space-around">
<div>{s_inicio}<div class="cap2"><b>Início</b>Horário, botão de pedido, Instagram e como chegar.</div></div>
<div>{s_lista}<div class="cap2"><b>Cardápio</b>Tamanho primeiro, depois o sabor, com foto e alérgenos.</div></div></div>''')

p4 = page(4, f'''<div class="k">Simulação · pedido e computador</div><h2>Escolher e <span>pedir</span></h2>
<div style="display:flex;justify-content:space-around;margin-top:3mm">
<div>{s_det}<div class="cap2"><b>Sabor</b>Ingredientes, alérgenos, tamanho e meio a meio.</div></div>
<div>{s_pedido}<div class="cap2"><b>Pedido</b>Total somado e mensagem pronta para o WhatsApp.</div></div></div>
<div style="margin-top:5mm">{desktop}<div class="cap2" style="max-width:none">Versão para computador: o mesmo conteúdo, em colunas.</div></div>''')

p5 = page(5, f'''<div class="k">Briefing do projeto</div><h2>O que será <span>feito</span></h2>
<div class="two2">
<div><div class="h3x" style="margin-top:2mm">Objetivo</div><p style="font-size:8.8pt">Ter um cardápio no celular, com a nova marca, que facilite a escolha, leve o pedido pronto ao WhatsApp e funcione como vitrine no Instagram e no Google.</p>
<div class="h3x">Público</div><p style="font-size:8.8pt">Clientes no salão (pelo QR Code), clientes de retirada e delivery (pelo WhatsApp e Instagram) e quem procura pizzaria no Google.</p>
<div class="h3x">Incluso</div><ul class="list">
<li>Página única no site, que funciona no celular e no computador.</li>
<li>Início com horário, WhatsApp, Instagram e localização.</li>
<li>Cardápio por categorias, com foto, ingredientes, alérgenos e preço por tamanho.</li>
<li>Escolha de meio a meio e soma automática do pedido.</li>
<li>Pedido enviado como mensagem pronta no WhatsApp.</li>
<li>QR Code para as mesas e link para a bio do Instagram.</li>
<li>Publicação e 1 rodada de ajustes.</li></ul></div>
<div><div class="h3x" style="margin-top:2mm">A casa envia</div><ul class="list">
<li>Lista de sabores, bebidas e sobremesas, com preços.</li>
<li>Número do WhatsApp de pedidos e perfil do Instagram.</li>
<li>Horário, endereço e área de entrega.</li>
<li>Regra do meio a meio e taxa de entrega, se houver.</li>
<li>Fotos (as atuais já servem para começar).</li></ul>
<div class="h3x">Não incluso</div><ul class="list">
<li>Domínio (endereço do site) e hospedagem: cotar. Um site simples pode usar hospedagem gratuita.</li>
<li>Pagamento online e integração com aplicativos de delivery.</li>
<li>Atualizações depois da entrega (orçadas à parte ou em plano mensal, a combinar).</li></ul>
<div class="h3x">Prazo</div><p style="font-size:8.8pt">2 semanas a partir do recebimento do conteúdo.</p></div></div>''')

p6 = page(6, f'''<div class="k">Investimento</div><h2>Cardápio digital <span>no site</span></h2>
<table class="tb" style="font-size:9.4pt;margin-top:4mm"><thead><tr><th>Opção</th><th style="text-align:right">Investimento</th></tr></thead><tbody>
<tr><td><b>Cardápio digital avulso</b><br><span style="color:var(--muted);font-size:8pt">Usando cores e fontes já definidas pela casa</span></td><td style="text-align:right;font-family:Roboto Condensed;font-weight:800;font-size:14pt">R$ 500</td></tr>
<tr><td><b>Junto com o cardápio físico</b> <span class="tag">recomendado</span><br><span style="color:var(--muted);font-size:8pt">Mesmo conteúdo, fotos e preços: físico R$ 600 + digital R$ 400</span></td><td style="text-align:right;font-family:Roboto Condensed;font-weight:800;font-size:14pt">R$ 1.000</td></tr>
<tr><td><b>Junto com um combo de identidade + cardápio</b><br><span style="color:var(--muted);font-size:8pt">Acrescenta o digital a qualquer combo da proposta</span></td><td style="text-align:right;font-family:Roboto Condensed;font-weight:800;font-size:14pt">+ R$ 400</td></tr></tbody></table>
<p class="note">Pagamento: 50% para começar e 50% na publicação, por Pix. Proposta válida por 15 dias.</p>
<div class="box" style="margin-top:7mm"><h4>Próximos passos</h4><ul>
<li>Escolher a opção e responder o questionário de briefing (documento à parte).</li>
<li>Enviar o conteúdo: preços, bebidas, sobremesas, WhatsApp e Instagram.</li>
<li>Aprovar a primeira versão no celular e publicar.</li></ul></div>
<div class="ok"><h4>Aceite</h4><div class="opts"><span>☐ Digital avulso · R$ 500</span><span>☐ Físico + digital · R$ 1.000</span><span>☐ Digital junto com combo · + R$ 400</span></div>
<div class="sg"><div>Speciale Pizzas Artesanais · assinatura e data</div><div>{PROV} · assinatura e data</div></div></div>''')

open('digital.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Cardápio digital · Speciale</title>{PCSS}{EXTRA}</head><body>{capa}{p2}{p3}{p4}{p5}{p6}</body></html>')
