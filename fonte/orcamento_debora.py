"""Orçamento de produção · Débora Brasil Beauty · porta e bandeira vela (padrão House do Creator, 2 páginas)."""
src = open('proposta_debora.py', encoding='utf-8').read()
exec(src[:src.index('# 1 · capa')])          # CSS e helpers (rays, title, page, brl) da proposta
CLIENTE = 'Orçamento de produção · Débora Brasil Beauty'

CSS += '''<style>
.dupla{display:grid;grid-template-columns:44mm 1fr;gap:6mm;width:100%;margin-top:6mm;align-items:start}
.dupla+.dupla{border-top:1px solid var(--line);padding-top:6mm}
.prev{background:#1a1a1a;border-radius:3mm;padding:3mm;display:flex;justify-content:center}
.prev img{max-width:100%;max-height:74mm;display:block}
.dupla h3{font-size:14pt;font-weight:700;letter-spacing:-.3px}
.dupla h3 span{color:var(--y)}
.dupla .ds{font-size:7.8pt;color:var(--soft);margin-top:1mm}
.dupla table{margin-top:2mm}
.dupla td.v{text-align:right;white-space:nowrap;font-weight:600}
.dupla tr.sum td{color:var(--y)}
.tot2{width:100%;margin-top:6mm;background:var(--y);color:var(--ink);border-radius:4mm;padding:5mm 6mm;display:grid;grid-template-columns:1fr auto;align-items:center;gap:4mm}
.tot2 small{display:block;font-size:7.4pt}
.tot2 b{font-size:10.5pt}
.tot2 .v{font-size:19pt;font-weight:700;white-space:nowrap;text-align:right}
.tot2 .v small{font-size:7pt;font-weight:500}
.obs{font-size:7pt;color:var(--soft);margin-top:3mm;width:100%}
.am .chk small{color:var(--soft)}
.dica{width:100%;background:var(--ink);color:var(--w);border-radius:4mm;padding:5mm 6mm;margin-top:5mm;font-size:8pt}
.dica b{color:var(--y)}
</style>'''

IMG = '../debora-brasil/impressao/'

p1 = page(1, f'''<span class="pill">Orçamento de produção</span>
{title('Do Instagram <span>pra rua.</span>')}
<p class="lead">A arte da porta já está no pacote. Aqui estão a arte da bandeira vela e uma estimativa do que a gráfica deve cobrar para imprimir e instalar as duas peças.</p>
<div class="dupla"><div class="prev"><img src="{IMG}porta-previa.png"></div><div>
<h3>Painel da porta · <span>60 × 90 cm</span></h3>
<p class="ds">Adesivo de vinil impresso e laminado, aplicado no vidro da porta da sala 7. Logo, serviços, horário, @ e WhatsApp.</p>
<table><thead><tr><th>Item</th><th class="r">Valor</th></tr></thead><tbody>
<tr><td>Arte da porta (House do Creator)</td><td class="v">incluída no pacote</td></tr>
<tr><td>Impressão em vinil + laminação (0,54 m²)</td><td class="v">R$ 60 a R$ 110</td></tr>
<tr><td>Instalação no vidro</td><td class="v">R$ 50 a R$ 100</td></tr>
<tr class="sum"><td>Total da porta</td><td class="v">R$ 110 a R$ 210</td></tr>
</tbody></table>
<p class="ds" style="margin-top:2mm">Porta inteira adesivada (até 0,90 × 2,10 m), se ela preferir: R$ 200 a R$ 380 instalado.</p></div></div>
<div class="dupla"><div class="prev"><img src="{IMG}vela-previa.png"></div><div>
<h3>Bandeira vela · <span>2,5 m</span></h3>
<p class="ds">Também chamada de wind banner ou bandeira de vento: tecido sublimado preso numa haste flexível, com base no chão, para ficar na calçada da galeria.</p>
<table><thead><tr><th>Item</th><th class="r">Valor</th></tr></thead><tbody>
<tr><td>Arte da bandeira vela (House do Creator)</td><td class="v">R$ 90</td></tr>
<tr><td>Kit completo dupla face: tecido + haste + base</td><td class="v">R$ 220 a R$ 350</td></tr>
<tr><td>Só o tecido, se já tiver haste e base</td><td class="v">R$ 100 a R$ 160</td></tr>
<tr class="sum"><td>Total da bandeira (arte + kit)</td><td class="v">R$ 310 a R$ 440</td></tr>
</tbody></table></div></div>
<div class="tot2"><div><small>Investimento total estimado</small><b>Porta + bandeira vela, arte e produção</b></div>
<div class="v">R$ 420 a R$ 650<small><br>R$ 90 da arte + gráfica</small></div></div>
<p class="obs">Valores de produção são estimativas de mercado (novembro/2026) para orientar a decisão. O preço final é o da gráfica escolhida: vale pedir 2 ou 3 orçamentos com os arquivos prontos.</p>''')

p2 = page(2, f'''<span class="pill">Como seguir</span>
{title('Pronto pra <span>imprimir.</span>', True)}
<p class="lead">Os arquivos já saem no tamanho real, em PDF com a logo vetorizada. Falta só confirmar quatro coisas e levar na gráfica.</p>
<div class="chk">
<div><i></i><span><b>Medir a porta</b><small>Largura e altura do vidro. O painel foi feito em 60 × 90 cm e a gente ajusta à medida real.</small></span></div>
<div><i></i><span><b>Confirmar o WhatsApp</b><small>O número entra na porta, na bandeira e nos botões da landing page.</small></span></div>
<div><i></i><span><b>Pedir o gabarito da gráfica</b><small>Cada fornecedor tem um molde de vela. A arte foi feita em 75 × 250 cm e encaixa no gabarito deles.</small></span></div>
<div><i></i><span><b>Aprovar a prova</b><small>Pedir a prova de cor antes de imprimir, para o malva sair igual ao da marca.</small></span></div>
</div>
<div class="dica"><b>Dicas pra gráfica:</b> bandeira dupla face (a frente se lê dos dois lados da rua); base de água ou cruzeta para a calçada; vinil da porta impresso e laminado, com corte reto. Prazo comum: 3 a 7 dias úteis.</div>
<div class="sig"><div>Débora Brasil · aprovação e data</div><div>House do Creator · assinatura e data</div></div>
<div class="cta"><small>WhatsApp</small><b>(81) 98355-4583</b></div>
<div class="who"><span><small>Instagram</small>@housedocreator</span><span><small>CEOs</small>Ryan Coimbra &amp; Fontenele</span></div>''', am=True)

open('orcamento_debora.html', 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Orçamento · Débora Brasil Beauty</title>{CSS}</head><body>{p1}{p2}</body></html>')
