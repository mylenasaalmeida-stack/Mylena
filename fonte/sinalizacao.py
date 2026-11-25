"""Sinalização profissional · cartazes dos 8 POPs + adesivos (A4) · pictogramas Lucide (licença ISC)."""
import re
from treinamento import hand  # pictogramas da lavagem das mãos

ICDIR = '../icons/node_modules/lucide-static/icons/'
RED, BLUE, GREEN, AMBER, INK, CREAM = '#C8161D', '#1F5FA8', '#1E8A4C', '#E8A317', '#1D1D1F', '#FBF6EE'


def ic(name, size=40, color='#fff', sw=2):
    svg = open(ICDIR + name + '.svg').read()
    svg = re.sub(r'<!--.*?-->', '', svg, flags=re.S)
    svg = re.sub(r'width="\d+"', f'width="{size}"', svg, count=1)
    svg = re.sub(r'height="\d+"', f'height="{size}"', svg, count=1)
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"').replace('stroke-width="2"', f'stroke-width="{sw}"')
    return svg.replace('class="lucide', 'style="display:block" class="lucide')


def ban(name, size=40):
    """pictograma de proibição: ícone + círculo cortado."""
    inner = ic(name, size * .62, INK, 2)
    return (f'<div style="position:relative;width:{size}px;height:{size}px;border-radius:50%;border:{size * .1:.0f}px solid {RED};background:#fff;display:flex;align-items:center;justify-content:center">'
            f'{inner}<div style="position:absolute;left:50%;top:50%;width:{size * .95:.0f}px;height:{size * .1:.0f}px;background:{RED};transform:translate(-50%,-50%) rotate(-45deg)"></div></div>')


CSS = f'''<style>
@import url('fonts.css');
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Poppins',sans-serif;color:{INK};-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}}
.page:last-child{{page-break-after:auto}}
.C{{font-family:'Roboto Condensed',sans-serif;font-weight:800;text-transform:uppercase;letter-spacing:.2px}}
/* cartaz */
.pst{{position:absolute;inset:8mm;border-radius:6mm;overflow:hidden;display:flex;flex-direction:column;border:1.2mm solid var(--c)}}
.top{{background:var(--c);color:#fff;padding:9mm 10mm 8mm;display:grid;grid-template-columns:1fr 34mm;align-items:center;gap:6mm}}
.top .tg{{display:inline-block;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.5);border-radius:20mm;padding:1mm 4mm;font-size:9pt;font-weight:600;letter-spacing:1px}}
.top h1{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:34pt;line-height:.95;margin-top:3mm}}
.top p{{font-size:10pt;opacity:.92;margin-top:2.5mm;line-height:1.35}}
.top .ico{{width:34mm;height:34mm;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center}}
.steps{{display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:5mm;padding:8mm 10mm 0;flex:1}}
.stp{{display:grid;grid-template-columns:26mm 1fr;gap:5mm;align-items:center;background:{CREAM};border-radius:4mm;padding:5mm}}
.stp .ci{{width:26mm;height:26mm;border-radius:50%;background:var(--c);display:flex;align-items:center;justify-content:center;position:relative}}
.stp .ci b{{position:absolute;right:-1.5mm;top:-1.5mm;width:7mm;height:7mm;border-radius:50%;background:{INK};color:#fff;font-family:'Roboto Condensed';font-size:10pt;display:flex;align-items:center;justify-content:center}}
.stp h4{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:16pt;line-height:1.05}}
.stp p{{font-size:10.5pt;line-height:1.35;margin-top:1.5mm;color:#3a3a3c}}
.freq{{margin:6mm 10mm 0;display:flex;gap:3mm;flex-wrap:wrap}}
.freq span{{border:1.5px solid var(--c);border-radius:20mm;padding:2mm 4.5mm;font-size:9.5pt}}
.freq span b{{color:var(--c)}}
.warn{{margin:5mm 10mm 0;font-size:10pt;display:grid;grid-template-columns:14mm 1fr;gap:4mm;align-items:center;background:#FFF6DC;border-left:2mm solid {AMBER};border-radius:2mm;padding:3mm 4mm;font-size:9pt;line-height:1.35}}
.foot{{margin-top:6mm;display:flex;justify-content:space-between;align-items:flex-end;padding:0 10mm 7mm;font-size:7.6pt;color:#666}}
.foot .sg{{display:grid;grid-template-columns:1fr 1fr;gap:8mm;width:115mm}}
.foot .sg div{{border-top:1px solid {INK};padding-top:1mm}}
.brand{{font-family:'Roboto Condensed';font-weight:800;font-size:14pt;color:{RED};line-height:1;text-align:right}}
.brand small{{display:block;font-family:Poppins;font-weight:600;font-size:5.5pt;letter-spacing:2px;color:{INK}}}
/* adesivos */
.sheet{{padding:10mm;display:grid;grid-template-columns:1fr 1fr;gap:5mm}}
.stk{{height:64mm;border:1px dashed #b5b5b5;border-radius:5mm;padding:2mm}}
.stk .in{{height:100%;border-radius:4mm;overflow:hidden;display:grid;grid-template-columns:30mm 1fr;border:1mm solid var(--c)}}
.stk .l{{background:var(--c);display:flex;align-items:center;justify-content:center}}
.stk .r{{padding:4mm 4.5mm;display:flex;flex-direction:column;justify-content:center}}
.stk .k{{font-size:7pt;font-weight:700;letter-spacing:1.5px;color:var(--c);text-transform:uppercase}}
.stk h3{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:19pt;line-height:.95;margin-top:1mm}}
.stk .big{{font-family:'Roboto Condensed';font-weight:800;font-size:30pt;line-height:1;color:var(--c);margin-top:1mm}}
.stk p{{font-size:8pt;line-height:1.35;margin-top:1.5mm;color:#3a3a3c}}
.cap{{position:absolute;left:10mm;right:10mm;bottom:4mm;display:flex;justify-content:space-between;font-size:6.6pt;color:#888}}
.leg{{grid-column:1/-1;display:flex;gap:6mm;font-size:7.5pt;color:#555;align-items:center}}
.leg i{{display:inline-block;width:3.5mm;height:3.5mm;border-radius:1mm;vertical-align:-.6mm;margin-right:1.5mm}}
</style>'''

BRAND = '<div class="brand">SPECIALE<small>PIZZAS ARTESANAIS</small></div>'


def poster(num, title, sub, color, icon, steps, freq, warn):
    st = ''.join(f'''<div class="stp"><div class="ci">{ic(i, 52, '#fff', 2)}<b>{k}</b></div><div><h4>{t}</h4><p>{d}</p></div></div>''' for k, (i, t, d) in enumerate(steps, 1))
    fr = ''.join(f'<span><b>{a}</b> · {b}</span>' for a, b in freq)
    return f'''<section class="page" style="--c:{color}"><div class="pst">
<div class="top"><div><span class="tg">POP {num:02d} · PROCEDIMENTO OPERACIONAL PADRONIZADO</span><h1>{title}</h1><p>{sub}</p></div>
<div class="ico">{ic(icon, 74, color, 1.8)}</div></div>
<div class="steps">{st}</div>
<div class="freq">{fr}</div>
<div class="warn">{ic("circle-alert", 40, "#9a6a00", 2)}<div>{warn}</div></div>
<div class="foot"><div class="sg"><div>Responsável · nome e função</div><div>Aprovado por · data ___/___/____</div></div>{BRAND}</div>
</div><div class="cap" style="bottom:2mm"><span>Cartaz para afixar · documento completo na pasta de Boas Práticas</span><span>RDC ANVISA 216/2004</span></div></section>'''


POPS = [
    (1, 'Higienização', 'Instalações, equipamentos, móveis e utensílios', RED, 'spray-can', [
        ('trash-2', 'Retire os resíduos', 'Tire restos de massa, queijo e sujeira maior.'),
        ('droplets', 'Lave com detergente', 'Esfregue com esponja ou escova da área.'),
        ('waves', 'Enxágue', 'Água corrente até sair todo o produto.'),
        ('sparkles', 'Desinfete', 'Produto da casa diluído como no rótulo; respeite o tempo.'),
        ('wind', 'Seque', 'Ao natural ou com papel toalha. Nunca pano de prato.'),
        ('clipboard-check', 'Registre', 'Marque e rubrique na planilha de higienização.')],
     [('Bancadas', 'entre tarefas e fim do turno'), ('Utensílios e bisnagas', 'após o uso'), ('Masseira e balança', 'após o uso'), ('Piso e lixeiras', 'diária'), ('Geladeiras', 'semanal'), ('Coifa', 'mensal')],
     '<b>Nunca misture produtos de limpeza</b> e guarde-os longe dos alimentos. Use só produtos regularizados na ANVISA.'),
    (2, 'Controle de pragas', 'Prevenção e controle integrado de vetores e pragas', '#3A3A3C', 'bug', [
        ('package', 'Tudo tampado', 'Alimentos fechados e fora do chão.'),
        ('trash-2', 'Lixo controlado', 'Lixeira com tampa e pedal; retirada diária.'),
        ('door-closed', 'Entradas vedadas', 'Telas, ralos fechados e portas vedadas.'),
        ('archive', 'Sem papelão', 'Caixas do fornecedor fora do estoque.'),
        ('bell-ring', 'Viu sinal? Avise', 'Fezes, roedura ou inseto: avise na hora.'),
        ('shield-check', 'Só empresa licenciada', 'Veneno só pela empresa. Guarde o comprovante.')],
     [('Ronda de sinais', 'diária'), ('Retirada do lixo', 'diária'), ('Empresa especializada', 'conforme contrato')],
     '<b>Ninguém da equipe aplica veneno.</b> No dia da aplicação, proteja alimentos e utensílios conforme a empresa orientar.'),
    (3, 'Caixa d\'água', 'Higienização do reservatório e potabilidade da água', BLUE, 'glass-water', [
        ('shield-check', 'Sempre tampada', 'Sem rachaduras e com acesso fácil.'),
        ('calendar-check', 'A cada 6 meses', 'Higienização no máximo a cada 6 meses.'),
        ('ban', 'Durante a limpeza', 'Não use a água para preparar alimentos.'),
        ('filter', 'Troque o filtro', 'Conforme o fabricante; anote a data.'),
        ('circle-alert', 'Água estranha?', 'Cor, cheiro ou gosto diferente: não use.'),
        ('clipboard-check', 'Registre', 'Data, responsável e próxima limpeza.')],
     [('Reservatório', 'a cada 6 meses (máximo)'), ('Filtro', 'conforme fabricante'), ('Conferência visual', 'diária')],
     'Guarde o <b>comprovante da empresa</b> que higienizou o reservatório na pasta de Boas Práticas.'),
    (4, 'Higiene do manipulador', 'Saúde, uniforme e conduta de quem toca nos alimentos', GREEN, 'chef-hat', [
        ('shirt', 'Uniforme limpo', 'Trocado todo dia; sapato fechado.'),
        ('chef-hat', 'Touca sempre', 'Todo o cabelo preso e coberto.'),
        ('watch', 'Sem adornos', 'Sem anel, brinco, relógio, pulseira ou piercing.'),
        ('hand', 'Mãos lavadas', 'Ao chegar e a cada troca de tarefa.'),
        ('smartphone', 'Sem celular', 'Nada de celular, comida ou chiclete na produção.'),
        ('heart-pulse', 'Doente? Avise', 'Diarreia, febre, vômito ou ferida: não manipule.')],
     [('Checagem do supervisor', 'entrada de cada turno'), ('Lavagem das mãos', 'a cada troca de tarefa'), ('Treinamento', 'admissão e a cada 6 meses')],
     '<b>Luva não substitui a lavagem das mãos.</b> Unhas curtas, limpas e sem esmalte.'),
    (5, 'Recebimento', 'Recebimento e armazenamento de mercadorias', '#6B3FA0', 'truck', [
        ('truck', 'Confira a entrega', 'Veículo limpo; refrigerados chegando frios.'),
        ('package-check', 'Confira o produto', 'Embalagem íntegra, rótulo, lote e validade.'),
        ('thermometer', 'Meça a temperatura', 'Compare com o indicado no rótulo.'),
        ('ban', 'Reprove se preciso', 'Fora do padrão: devolva e anote o motivo.'),
        ('refrigerator', 'Guarde o frio primeiro', 'Congelados e refrigerados antes dos secos.'),
        ('tags', 'PVPS e etiqueta', 'Primeiro que vence sai primeiro; nada no chão.')],
     [('Conferência', 'toda entrega'), ('Planilha de recebimento', 'toda entrega'), ('Organização do estoque', 'semanal')],
     '<b>Caixa de papelão não entra no estoque.</b> Transfira os produtos para recipientes limpos e identificados.'),
    (6, 'Hortifrútis', 'Higienização de frutas, verduras e legumes', '#2E7D32', 'leaf', [
        ('trash-2', 'Selecione', 'Retire partes estragadas, folhas feias e mofo.'),
        ('droplets', 'Lave um a um', 'Em água corrente potável, esfregando.'),
        ('timer', 'Desinfete', 'Solução própria para alimentos, no tempo do rótulo.'),
        ('waves', 'Enxágue', 'Em água corrente potável.'),
        ('refrigerator', 'Guarde frio', 'Recipiente limpo, tampado e etiquetado.'),
        ('clipboard-check', 'Registre', 'Data, hora, produto e diluição usados.')],
     [('Tomate e manjericão do molho', 'a cada preparo'), ('Cebola e outros', 'antes do corte')],
     'Use só produto <b>registrado na ANVISA para hortifrútis</b>. Bacia e utensílios exclusivos para esta etapa.'),
    (7, 'Forno a lenha', 'Operação segura do forno, da lenha e das cinzas', '#D2541A', 'flame', [
        ('trees', 'Lenha certa', 'Seca, sem tinta, verniz ou cola; longe dos alimentos.'),
        ('ban', 'Sem inflamáveis', 'Nunca acenda com álcool ou gasolina.'),
        ('thermometer-sun', 'Ponto do forno', '340 a 380 °C; pizza por 3 a 4 min.'),
        ('hand', 'Luva térmica', 'Cano longo; área livre de papel e caixas.'),
        ('fire-extinguisher', 'Extintor pronto', 'Próximo, sinalizado e na validade.'),
        ('archive', 'Cinzas frias', 'Retire com o forno frio, em lata metálica com tampa.')],
     [('Conferência da área', 'abertura'), ('Pá e cortador', 'a cada turno'), ('Extintor', 'semanal')],
     '<b>Nunca deixe caixas, papel ou embalagens perto da boca do forno.</b>'),
    (8, 'Delivery e salão', 'Expedição, entrega e atendimento ao cliente', '#0E7C86', 'bike', [
        ('pizza', 'Embale na hora', 'Cortou, embalou, fechou a caixa.'),
        ('list-checks', 'Confira o pedido', 'Sabor, tamanho e extras antes de sair.'),
        ('shopping-bag', 'Bag só para comida', 'Higienizada no fim do turno; nada pessoal dentro.'),
        ('bike', 'Entrega rápida', 'Entregador não toca na pizza nem abre a caixa.'),
        ('utensils', 'Salão limpo', 'Mesa e cardápio higienizados a cada cliente.'),
        ('banknote', 'Dinheiro x comida', 'Pegou dinheiro? Lave as mãos antes de servir.')],
     [('Bags térmicas', 'fim de cada turno'), ('Mesas e cardápios', 'a cada cliente'), ('Caixas guardadas', 'protegidas de pó')],
     '<b>Pizza que esfriou ou caixa amassada não sai.</b> Troque antes de entregar.'),
]
posters = [poster(*p) for p in POPS]

# --- cartaz lavagem das mãos (novo visual)
hw = [('agua', 'Molhe as mãos'), ('sabao', 'Sabonete líquido'), ('palmas', 'Palma com palma'), ('dorso', 'Dorso das mãos'), ('dedos', 'Entre os dedos'),
      ('polegar', 'Polegares'), ('unhas', 'Pontas e unhas'), ('punhos', 'Punhos'), ('seca', 'Enxágue e seque')]
hcells = ''.join(f'''<div style="background:{CREAM};border-radius:4mm;padding:4mm;text-align:center;position:relative">
<div style="position:absolute;left:3mm;top:3mm;width:8mm;height:8mm;border-radius:50%;background:{BLUE};color:#fff;font-family:Roboto Condensed;font-weight:800;font-size:12pt;display:flex;align-items:center;justify-content:center">{i}</div>
<div style="width:30mm;height:30mm;border-radius:50%;background:#fff;margin:2mm auto 0;display:flex;align-items:center;justify-content:center">{hand(k).replace('#d7141a', BLUE).replace('width="34mm" height="20mm"', 'width="26mm" height="16mm"')}</div>
<div class="C" style="font-size:12pt;margin-top:3mm">{t}</div></div>''' for i, (k, t) in enumerate(hw, 1))
maos = f'''<section class="page" style="--c:{BLUE}"><div class="pst">
<div class="top"><div><span class="tg">OBRIGATÓRIO · LAVATÓRIO DE MÃOS</span><h1>Lave as mãos</h1><p>40 a 60 segundos · sabonete líquido · papel toalha · lixeira com pedal</p></div>
<div class="ico">{ic('hand', 74, BLUE, 1.8)}</div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;padding:7mm 10mm 0">{hcells}</div>
<div class="freq"><span><b>Ao chegar</b></span><span><b>Ao trocar de tarefa</b></span><span><b>Após o banheiro</b></span><span><b>Após lixo e alimento cru</b></span><span><b>Após dinheiro e celular</b></span><span><b>Após tossir ou espirrar</b></span></div>
<div class="warn">{ic("circle-alert", 40, "#9a6a00", 2)}<div><b>Feche a torneira com o papel toalha.</b> Luva não substitui a lavagem.</div></div>
<div class="foot"><div style="font-size:7.6pt">RDC ANVISA 216/2004</div>{BRAND}</div></div></section>'''

# --- adesivos (cores pela lógica da sinalização de segurança)
def stk(color, kind, icon, k, title, text, big=None):
    left = ban(icon, 86) if kind == 'ban' else ic(icon, 62, '#fff', 1.9)
    lbg = '#fff' if kind == 'ban' else color
    body = f'<div class="big">{big}</div>' if big else ''
    return f'''<div class="stk" style="--c:{color}"><div class="in"><div class="l" style="background:{lbg};{'border-right:1mm solid ' + color if kind == 'ban' else ''}">{left}</div>
<div class="r"><div class="k">{k}</div><h3>{title}</h3>{body}<p>{text}</p></div></div></div>'''


A1 = [stk(BLUE, 'ok', 'refrigerator', 'Obrigatório', 'Geladeira', 'Confira e anote na abertura e no fechamento.', 'até 5 °C'),
      stk(BLUE, 'ok', 'snowflake', 'Obrigatório', 'Freezer', 'Descongele dentro da geladeira. Não recongele.', '−18 °C'),
      stk(RED, 'ban', 'watch', 'Proibido', 'Adornos', 'Sem anel, brinco, relógio, pulseira, colar ou piercing.'),
      stk(BLUE, 'ok', 'chef-hat', 'Obrigatório', 'Touca e uniforme', 'Cabelo totalmente coberto. Uniforme limpo.'),
      stk(RED, 'ban', 'smartphone', 'Proibido', 'Celular na produção', 'Nem celular, comida, chiclete ou cigarro.'),
      stk(GREEN, 'ok', 'tags', 'Boa prática', 'PVPS', 'Primeiro que vence, primeiro que sai. Tudo etiquetado.'),
      stk(AMBER, 'ok', 'flame', 'Atenção', 'Forno quente', 'Use luva térmica de cano longo. Nada de papel por perto.'),
      stk(BLUE, 'ok', 'hand', 'Obrigatório', 'Só para as mãos', 'Pia exclusiva para lavar as mãos. Não lave utensílios aqui.')]
A2 = [stk(GREEN, 'ok', 'pizza', 'Geladeira · em cima', 'Prontos', 'Queijos, presunto, molho, catupiry. Tampados e etiquetados.'),
      stk(AMBER, 'ok', 'drumstick', 'Geladeira · embaixo', 'Crus', 'Frango, ovos e carnes. Sempre na prateleira de baixo.'),
      stk(BLUE, 'ok', 'clock', 'Obrigatório', 'Descongelamento', 'Só dentro da geladeira. Nunca na bancada ou na pia.'),
      stk('#3A3A3C', 'ok', 'trash-2', 'Obrigatório', 'Lixeira', 'Mantenha tampada e abra só pelo pedal.'),
      stk(RED, 'ban', 'spray-can', 'Proibido', 'Limpeza perto de alimento', 'Produtos de limpeza guardados longe dos alimentos.'),
      stk(GREEN, 'ok', 'shopping-bag', 'Delivery', 'Bag só para comida', 'Higienizada no fim do turno. Nada pessoal dentro.'),
      stk(AMBER, 'ok', 'heart-pulse', 'Atenção', 'Está doente?', 'Diarreia, febre, vômito ou ferida: avise antes de entrar.'),
      stk(BLUE, 'ok', 'thermometer', 'Obrigatório', 'Termômetro', 'Anote 2 vezes ao dia. Fora do limite? Avise.')]
leg = f'<div class="leg"><span><i style="background:{BLUE}"></i>Obrigação</span><span><i style="background:{RED}"></i>Proibição</span><span><i style="background:{AMBER}"></i>Atenção</span><span><i style="background:{GREEN}"></i>Boa prática</span><span style="margin-left:auto">Imprimir em papel adesivo e recortar na linha tracejada</span></div>'
sheets = [f'<section class="page"><div class="sheet">{leg}{"".join(a)}</div><div class="cap"><span>Speciale · adesivos de sinalização · folha {i}</span><span>RDC ANVISA 216/2004</span></div></section>' for i, a in enumerate([A1, A2], 1)]

# --- etiquetas de validade
lab = ''.join(f'''<div style="border:1px dashed #b5b5b5;border-radius:4mm;padding:1.5mm"><div style="border:.8mm solid {c};border-radius:3mm;overflow:hidden">
<div style="background:{c};color:#fff;padding:1.5mm 3mm;display:flex;justify-content:space-between;align-items:center"><span class="C" style="font-size:10pt">Identificação</span>{ic('tag', 16, '#fff', 2)}</div>
<div style="padding:2.5mm 3mm;font-size:8pt;line-height:2.05"><b>Produto</b> ________________<br><b>Preparo/abertura</b> ___/___ · ___h<br><b>Validade</b> ___/___<br><b>Responsável</b> ____________<br>☐ Refrig. ☐ Cong. ☐ Seco</div></div></div>''' for c in [RED, BLUE, GREEN] * 5)
etiq = f'<section class="page"><div style="padding:10mm"><div class="C" style="font-size:15pt;margin-bottom:4mm">Etiquetas de validade <span style="font-family:Poppins;font-weight:400;text-transform:none;font-size:8.5pt;color:#666">· 15 por folha · papel adesivo</span></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm">{lab}</div></div></section>'

open('sinalizacao.html', 'w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Speciale · Sinalização</title>{CSS}</head><body>{maos}{"".join(posters)}{"".join(sheets)}{etiq}</body></html>')
