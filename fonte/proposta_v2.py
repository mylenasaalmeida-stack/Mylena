"""Proposta curta · Identidade visual + cardápio · Speciale (4 páginas)."""

CSS = '''<style>
@import url('fonts.css');
:root{--ink:#1f1a17;--muted:#6f6560;--line:#e7ddd2;--paper:#faf6f0;--acc:#c8361f;--acc2:#e07a2e}
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Poppins',sans-serif;color:var(--ink);font-size:9.5pt;line-height:1.45;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.in{position:absolute;left:20mm;right:20mm;top:18mm;bottom:16mm}
.ft{position:absolute;left:20mm;right:20mm;bottom:8mm;display:flex;justify-content:space-between;font-size:6.8pt;color:var(--muted)}
.k{font-size:7.5pt;font-weight:600;color:var(--acc);letter-spacing:2px;text-transform:uppercase}
h2{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:30pt;line-height:.98;text-transform:uppercase;margin:2mm 0 3mm}
h2 span{color:var(--acc)}
.lead{font-size:11pt;color:#3d3531;max-width:160mm}
.chk{position:absolute;left:0;right:0;height:10px;background:repeating-conic-gradient(var(--acc) 0 25%,transparent 0 50%) 0 0/10px 10px}
/* capa */
.cover{background:var(--ink);color:#fff}
.cover .in{top:24mm;bottom:22mm}
.cover h1{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:52pt;line-height:.92;text-transform:uppercase;margin-top:44mm}
.cover h1 span{display:block;color:var(--acc2)}
.cover .sub{font-size:13pt;margin-top:8mm;max-width:145mm;color:#eee4da;line-height:1.5}
.cover .meta{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;font-size:8.5pt;color:#cfc4ba;border-top:1px solid #4a403b;padding-top:5mm}
.cover .meta b{color:#fff;font-weight:600}
.logo{display:flex;align-items:center;gap:9px}
.logo b{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:18pt;display:block;line-height:1}
.logo i{font-style:normal;font-size:5.4pt;letter-spacing:2.8px;font-weight:600}
/* razões */
.why{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm;margin-top:7mm}
.why div{border-top:4px solid var(--acc);background:var(--paper);border-radius:0 0 6px 6px;padding:5mm}
.why .n{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:28pt;color:var(--acc);line-height:1}
.why h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:13pt;text-transform:uppercase;margin:2mm 0 1.5mm;line-height:1.05}
.why p{font-size:8.8pt;color:#3d3531}
.quote{margin-top:8mm;background:var(--ink);color:#fff;border-radius:8px;padding:7mm 8mm;font-size:12.5pt;line-height:1.45}
.quote b{color:#ffb98a}
.logo3{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:4mm}
.logo3 div{border:1.5px solid var(--line);border-radius:6px;padding:4mm;text-align:center}
.logo3 div.hl{border-color:var(--acc)}
.logo3 b{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:12pt;text-transform:uppercase;display:block}
.logo3 small{font-size:8pt;color:var(--muted)}
.tag{display:inline-block;font-size:6.6pt;font-weight:700;letter-spacing:.6px;padding:1px 7px;border-radius:3px;background:var(--acc);color:#fff;text-transform:uppercase}
/* pacotes */
.pk{display:grid;grid-template-columns:1fr 1.12fr 1fr;gap:4mm;margin-top:6mm;align-items:stretch}
.p{border:1.5px solid var(--line);border-radius:8px;padding:6mm 5mm;display:flex;flex-direction:column}
.p.best{border:2.5px solid var(--acc);box-shadow:0 0 0 4px #fbe3dc;position:relative}
.p.best .tag{position:absolute;top:-3mm;left:50%;transform:translateX(-50%);font-size:7.2pt;padding:2px 10px}
.p h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:15pt;text-transform:uppercase;line-height:1}
.p .for{font-size:8pt;color:var(--muted);margin:1.5mm 0 3mm;min-height:9mm}
.p .pr{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:28pt;line-height:1}
.p .pr small{display:block;font-size:8pt;font-family:'Poppins';font-weight:500;color:var(--muted);margin-bottom:1mm}
.p.best .tag{white-space:nowrap}
.p .pr{white-space:nowrap}
.p .save{font-size:8pt;color:var(--acc);font-weight:600;margin-top:1mm;min-height:4mm}
.p ul{list-style:none;margin-top:4mm;font-size:8.6pt}
.p li{padding:1.3mm 0 1.3mm 5mm;position:relative;border-top:1px solid var(--line)}
.p li:before{content:'✓';position:absolute;left:0;color:var(--acc);font-weight:700}
.var{margin-top:6mm}
table{width:100%;border-collapse:collapse;font-size:9pt}
th{font-family:'Roboto Condensed',sans-serif;font-weight:700;text-transform:uppercase;font-size:8pt;text-align:left;padding:5px 8px;background:var(--ink);color:#fff}
td{padding:6px 8px;border-bottom:1px solid var(--line)}
td.r,th.r{text-align:right}
td b{font-family:'Roboto Condensed',sans-serif;font-size:11pt}
.note{font-size:7.6pt;color:var(--muted);margin-top:2mm}
/* como funciona */
.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-top:6mm}
.tl div{position:relative;padding-top:9mm}
.tl div:before{content:attr(data-n);position:absolute;top:0;left:0;width:7mm;height:7mm;border-radius:50%;background:var(--acc);color:#fff;font-family:'Roboto Condensed',sans-serif;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:10pt}
.tl b{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:11pt;text-transform:uppercase;display:block}
.tl p{font-size:8.4pt;color:#3d3531}
.two{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:7mm}
.box{background:var(--paper);border-radius:8px;padding:5mm 6mm}
.box h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:12pt;text-transform:uppercase;margin-bottom:2mm}
.box ul{padding-left:4.5mm;font-size:8.7pt}.box li{margin:1.2mm 0}.box li::marker{color:var(--acc)}
.ok{margin-top:7mm;border:2px dashed var(--ink);border-radius:8px;padding:6mm}
.ok h4{font-family:'Roboto Condensed',sans-serif;font-weight:800;font-size:13pt;text-transform:uppercase}
.ok .opts{display:flex;flex-wrap:wrap;gap:3mm 7mm;margin:3mm 0 9mm;font-size:9.5pt}
.ok .sg{display:grid;grid-template-columns:1fr 1fr;gap:12mm;text-align:center;font-size:7.6pt;color:var(--muted)}
.ok .sg div{border-top:1px solid var(--ink);padding-top:2mm}
</style>'''

PROV = '[Seu nome ou estúdio]'
DATA = '11/11/2026'
LOGO = ('<svg width="44" height="32" viewBox="0 0 46 34"><ellipse cx="9" cy="15" rx="8.5" ry="7" fill="#fff"/>'
        '<ellipse cx="18" cy="27" rx="8" ry="6.5" fill="#fff"/><path d="M18 13 C21 4 33 1 45 2 C42 10 31 15 18 13Z" fill="#3aa63a"/></svg>')


def page(n, body):
    return f'<section class="page"><div class="in">{body}</div><div class="ft"><span>Speciale Pizzas Artesanais · Proposta de identidade visual e cardápio</span><span>{n} / 4</span></div></section>'


cover = f'''<section class="page cover"><div class="chk" style="top:0"></div><div class="in">
<div class="logo">{LOGO}<div><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i></div></div>
<h1>Casa nova,<span>marca à altura</span></h1>
<p class="sub">Uma identidade visual e um cardápio pensados para a nova fase da Speciale: novas cores, novo espaço e a mesma pizza artesanal de forno a lenha.</p>
<div class="meta"><span>Para: <b>Speciale Pizzas Artesanais</b></span><span>Por: <b>{PROV}</b></span><span>{DATA}</span></div>
</div><div class="chk" style="bottom:0"></div></section>'''

p2 = page(2, '''<div class="k">Por que agora</div><h2>O espaço vai mudar.<br><span>A marca precisa acompanhar.</span></h2>
<p class="lead">Quando o cliente entrar na nova Speciale, tudo precisa contar a mesma história: a fachada, o salão, a caixa da pizza e o cardápio.</p>
<div class="why">
<div><span class="n">01</span><h4>Cores novas</h4><p>Com a nova paleta, o material antigo (cardápio, caixas, redes) passa a destoar do espaço. A marca precisa ser refeita nas novas cores.</p></div>
<div><span class="n">02</span><h4>Espaço novo</h4><p>A reforma muda mesas, balcão e iluminação. O cardápio precisa de formato e material pensados para esse novo ambiente.</p></div>
<div><span class="n">03</span><h4>Cardápio que vende</h4><p>Um cardápio organizado destaca os carros-chefe, deixa a escolha mais rápida e mostra tamanhos e sabores de forma clara, no salão e no WhatsApp.</p></div>
</div>
<div class="quote">A reabertura é a melhor hora para mudar: o cliente já espera novidade. <b>Fazer marca e cardápio juntos sai mais barato e deixa tudo pronto para o primeiro dia.</b></div>
<div class="k" style="margin-top:9mm">Uma decisão para começar</div>
<p style="margin-top:1.5mm;font-size:10pt"><b>E a logo?</b> Com as novas cores, ela muda pelo menos de cor. Vocês escolhem até onde ir:</p>
<div class="logo3">
<div><b>Manter</b><small>Mesma logo, nas novas cores. Menor custo.</small></div>
<div class="hl"><span class="tag">sugerido</span><b>Ajustar</b><small>Redesenho da logo atual. Moderniza sem perder o reconhecimento.</small></div>
<div><b>Logo nova</b><small>Criada do zero, para marcar a nova fase.</small></div>
</div>''')

p3 = page(3, '''<div class="k">Investimento</div><h2>Escolha o <span>seu pacote</span></h2>
<div class="pk">
<div class="p"><h4>Cardápio</h4><div class="for">Para quem já tem a nova identidade definida.</div>
<div class="pr"><small>&nbsp;</small>R$ 600</div><div class="save"></div><ul>
<li>Cardápio de mesa nas novas cores</li><li>Sabores organizados para vender mais</li><li>Descrições claras, tamanhos e fatias</li><li>Versão digital para WhatsApp e QR Code</li><li>Arquivo pronto para a gráfica</li></ul></div>
<div class="p best"><span class="tag">Recomendado</span><h4>Combo marca + cardápio</h4><div class="for">Tudo pronto e combinando para a reabertura.</div>
<div class="pr"><small>a partir de</small> R$ 1.300</div><div class="save">Economia de até R$ 400</div><ul>
<li><b>Tudo do pacote Cardápio</b></li><li>Logo nas novas cores, ajustada ou nova</li><li>Paleta de cores e fontes da marca</li><li>Caixa de pizza, uniforme e outras peças</li><li>Perfil e destaques das redes sociais</li><li>Guia da marca para usar no dia a dia</li></ul></div>
<div class="p"><h4>Identidade visual</h4><div class="for">Para renovar a marca agora e o cardápio depois.</div>
<div class="pr"><small>a partir de</small> R$ 900</div><div class="save"></div><ul>
<li>Logo nas novas cores, ajustada ou nova</li><li>Paleta de cores e fontes da marca</li><li>Caixa de pizza, uniforme e outras peças</li><li>Perfil e destaques das redes sociais</li><li>Guia da marca para usar no dia a dia</li></ul></div>
</div>
<div class="var"><table><thead><tr><th>A logo vai…</th><th class="r">Só identidade</th><th class="r">Combo + cardápio</th><th class="r">Prazo do combo</th></tr></thead><tbody>
<tr><td>Manter (mudar só a cor)</td><td class="r"><b>R$ 900</b></td><td class="r"><b>R$ 1.300</b></td><td class="r">4 semanas</td></tr>
<tr><td>Ser ajustada <span class="tag">sugerido</span></td><td class="r"><b>R$ 1.400</b></td><td class="r"><b>R$ 1.700</b></td><td class="r">5 semanas</td></tr>
<tr><td>Ser nova</td><td class="r"><b>R$ 2.000</b></td><td class="r"><b>R$ 2.200</b></td><td class="r">6 semanas</td></tr>
</tbody></table>
<p class="note">Opcionais: cardápio de parede ou balcão (R$ 150) · adaptação para aplicativos de delivery (R$ 150) · direção das fotos das pizzas (R$ 250, fotógrafo à parte).</p></div>''')

p4 = page(4, '''<div class="k">Como funciona</div><h2>Simples, rápido e <span>no seu ritmo</span></h2>
<div class="tl">
<div data-n="1"><b>Conversa</b><p>Uma reunião de 1 hora para entender a casa, o espaço novo e o cardápio.</p></div>
<div data-n="2"><b>Proposta visual</b><p>Apresentamos a direção da marca com as novas cores.</p></div>
<div data-n="3"><b>Ajustes</b><p>Vocês opinam e ajustamos até ficar do jeito certo.</p></div>
<div data-n="4"><b>Entrega</b><p>Arquivos prontos para a gráfica, as redes e o WhatsApp.</p></div>
</div>
<div class="two">
<div class="box"><h4>Condições</h4><ul>
<li>50% para começar e 50% na entrega, por Pix.</li>
<li>Combos em até 3x sem acréscimo.</li>
<li>2 rodadas de ajuste incluídas.</li>
<li>Arquivos finais e direito de uso ficam com a Speciale.</li>
<li>Proposta válida por 15 dias.</li></ul></div>
<div class="box"><h4>Não incluso</h4><ul>
<li>Impressão (indicamos gráficas e acompanhamos a prova).</li>
<li>Cachê de fotógrafo.</li>
<li>Obra, fachada e placas.</li>
<li>Gestão de redes sociais.</li>
<li>Registro da marca no INPI.</li></ul></div>
</div>
<div class="box" style="margin-top:6mm"><h4>Para começar, só precisamos saber</h4><ul>
<li>As novas cores já foram definidas? Quais?</li>
<li>A logo vai ser mantida, ajustada ou trocada?</li>
<li>Qual é a data da reabertura?</li></ul>
<p class="note">As demais perguntas ficam para a reunião, com o questionário de briefing.</p></div>
<div class="ok"><h4>Vamos começar?</h4><div class="opts">
<span>☐ Cardápio · R$ 600</span><span>☐ Combo · logo mantida · R$ 1.300</span><span>☐ Combo · logo ajustada · R$ 1.700</span><span>☐ Combo · logo nova · R$ 2.200</span>
<span>☐ Identidade · logo mantida · R$ 900</span><span>☐ Identidade · logo ajustada · R$ 1.400</span><span>☐ Identidade · logo nova · R$ 2.000</span></div>
<div class="sg"><div>Speciale Pizzas Artesanais · assinatura e data</div><div>''' + PROV + ''' · assinatura e data</div></div></div>''')

open('proposta_v2.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Proposta · Speciale</title>{CSS}</head><body>{cover}{p2}{p3}{p4}</body></html>')
