"""Questionário de briefing · Speciale (A4 retrato, formato da proposta)."""
from proposta_v2 import CSS as PCSS, LOGO

PROV = '[Seu nome ou estúdio]'
EXTRA = '''<style>
.qs{counter-reset:q}
.qq{position:relative;padding:1.5mm 0 1.2mm 9mm;border-bottom:1px solid var(--line);break-inside:avoid}
.qq:before{counter-increment:q;content:counter(q);position:absolute;left:0;top:1.5mm;font-family:'Roboto Condensed';font-weight:800;color:var(--acc);font-size:10pt}
.qq b{font-weight:600;font-size:8.5pt}
.qq .o{display:flex;flex-wrap:wrap;gap:.8mm 5mm;margin-top:1mm;font-size:8pt;color:#3d3531}
.ln{border-bottom:1px solid #bfb4a8;height:4.6mm}
.sec{display:flex;align-items:center;gap:3mm;margin:4mm 0 .5mm}
.sec span{background:var(--ink);color:#fff;font-family:'Roboto Condensed';font-weight:800;width:8mm;height:8mm;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:11pt}
.sec h3{font-family:'Roboto Condensed';font-weight:800;font-size:14pt;text-transform:uppercase}
.hint{font-size:7.4pt;color:var(--muted);margin:0 0 1mm 11mm}
</style>'''


def q(text, opts=None, lines=1):
    o = ''
    if opts:
        o = '<div class="o">' + ''.join(f'<span>☐ {x}</span>' for x in opts) + '</div>'
    ls = ''.join('<div class="ln"></div>' for _ in range(lines))
    return f'<div class="qq"><b>{text}</b>{o}{ls}</div>'


def sec(n, t, hint=''):
    return f'<div class="sec"><span>{n}</span><h3>{t}</h3></div>' + (f'<div class="hint">{hint}</div>' if hint else '')


T = 5


def page(n, body):
    return (f'<section class="page"><div class="in" style="top:15mm">{body}</div><div class="ft"><span>Speciale Pizzas Artesanais · Questionário de briefing · '
            f'Nome de quem respondeu: ____________________ · Data: ___/___/____</span><span>{n} / {T}</span></div></section>')


capa = f'''<section class="page cover"><div class="chk" style="top:0"></div><div class="in">
<div class="logo">{LOGO}<div><b>SPECIALE</b><i>PIZZAS ARTESANAIS</i></div></div>
<h1>Questionário<span>de briefing</span></h1>
<p class="sub">Todas as perguntas para fechar a nova marca, o cardápio físico, o cardápio digital e a padronização da produção, num lugar só. Responda o que já souber; o restante vemos juntos na reunião.</p>
<div class="meta"><span>Para: <b>Speciale Pizzas Artesanais</b></span><span>Por: <b>{PROV}</b></span><span>Tempo estimado: 30 a 40 min</span></div>
</div><div class="chk" style="bottom:0"></div></section>'''

p2 = page(2, '<div class="qs">' + sec(1, 'A casa e a nova fase') +
          q('O que muda na reforma do espaço?', ['Fachada', 'Salão e mesas', 'Balcão', 'Iluminação', 'Cozinha', 'Outro']) +
          q('As novas cores já foram definidas (por exemplo, pelo arquiteto)? A paleta preto e verde da prévia está aprovada?', ['Sim, preto e verde', 'Sim, outras cores', 'Ainda não']) +
          q('Qual é a data prevista de reabertura?') +
          q('Que sensação o cliente deve ter ao entrar na nova Speciale?', ['Acolhedora', 'Sofisticada', 'Descontraída', 'Familiar', 'Outra']) +
          q('Quem é o cliente principal hoje? Isso muda com a reforma?', ['Famílias', 'Casais', 'Jovens', 'Delivery', 'Retirada']) +
          q('O atendimento muda depois da reforma?', ['Mais salão', 'Mais delivery', 'Balcão e retirada', 'Não muda']) +
          q('Quais pizzarias ou marcas vocês admiram? E com quais não querem parecer?', lines=2) +
          sec(2, 'Logo e marca') +
          q('O que acontece com a logo?', ['Manter (só as novas cores)', 'Ajustar', 'Criar uma nova']) +
          q('O que vocês gostam e o que não gostam na logo atual?', lines=2) +
          q('Os clientes reconhecem a casa mais pela logo, pelo nome ou pelo produto?', ['Logo', 'Nome', 'Produto']) +
          q('A expressão “Pizzas Artesanais” continua na marca?', ['Sim', 'Não']) +
          q('A marca está registrada no INPI?', ['Sim', 'Não', 'Não sei']) +
          q('Onde a logo aparece hoje? Há estoque de caixas ou impressos?', ['Fachada', 'Caixas', 'Uniformes', 'Sacolas', 'Redes', 'Aplicativos']) +
          q('Quem toma a decisão final sobre marca e cardápio?') + '</div>')

p3 = page(3, '<div class="qs" style="counter-reset:q 14">' + sec(3, 'Cardápio físico', 'Formatos da simulação: A = tríptico de mesa · B = cardápio redondo.') +
          q('Quais formatos a casa quer?', ['A · Tríptico', 'B · Redondo', 'Os dois', 'TV no balcão', 'Cardápio de parede']) +
          q('Quantos cardápios físicos serão necessários?', ['Até 10', '10 a 20', '20 a 40', 'Mais de 40']) +
          q('Preferência de material:', ['Papel com laminação fosca', 'PVC', 'MDF', 'Couro sintético', 'Sem preferência']) +
          q('Lista completa de sabores salgados e doces (algum entra ou sai?):', lines=3) +
          q('Quais são os carros-chefe? E os que dão mais lucro?', lines=1) +
          q('Há entradas, bebidas, sobremesas ou combos? Liste com os preços:', lines=3) +
          q('Os preços das pizzas estão aprovados (Broto R$ 38 · Média R$ 45 · Grande R$ 68, iguais para todos os sabores)?', ['Sim', 'Ajustar', 'Preço diferente por sabor']) +
          q('O preço é o mesmo no salão, na retirada e no delivery?', ['Sim', 'Não']) +
          q('Como é a regra do meio a meio?', ['Mesmo preço', 'Preço do sabor mais caro', 'Não fazemos']) +
          q('Há borda recheada, adicionais ou opções vegetarianas, sem lactose ou outras?', lines=1) +
          q('Tom de voz do cardápio:', ['Clássico', 'Descontraído', 'Regional', 'Sofisticado']) +
          q('A hashtag “#EuNaSpeciale” está aprovada? Se não, qual usar?', ['Aprovada', 'Outra: __________']) + '</div>')

p4 = page(4, '<div class="qs" style="counter-reset:q 26">' + sec(4, 'Cardápio digital, Instagram e contatos') +
          q('Número do WhatsApp que recebe os pedidos:') +
          q('Perfil do Instagram (@):') +
          q('A casa já tem site ou domínio (endereço na internet)? Qual?', ['Sim: __________', 'Não']) +
          q('A localização da casa está cadastrada no Google e no Instagram?', ['Google', 'Instagram', 'Nenhum']) +
          q('Endereço, horário de funcionamento e área de entrega:', lines=2) +
          q('Há taxa de entrega? Como é calculada?', lines=1) +
          q('Formas de pagamento aceitas:', ['Pix', 'Cartão', 'Dinheiro', 'Vale-refeição']) +
          q('A casa usa iFood ou outro aplicativo de delivery?', ['iFood', 'Outro: __________', 'Não']) +
          q('Quem vai atualizar preços e sabores no cardápio digital?', ['A própria casa', 'Contratar atualização']) +
          q('Haverá TV no balcão para o cardápio?', ['Sim', 'Não', 'Talvez']) +
          q('A casa tem fotógrafo ou quer indicação para fotos das pizzas?', ['Tem', 'Quer indicação', 'Usar as fotos atuais']) +
          q('Há orçamento reservado para a impressão dos cardápios?', ['Sim: R$ ______', 'Não']) + '</div>')

p5 = page(5, '<div class="qs" style="counter-reset:q 38">' + sec(5, 'Padronização da produção', 'Pendências das fichas técnicas e dos guias já entregues.') +
          q('Massa: a validade de 2 dias vale para geladeira ou freezer? Temperatura do freezer?', ['Geladeira', 'Freezer a ____ °C']) +
          q('Massa: tempo de descanso das bolinhas e se a bandeja fica coberta.', ['20 a 30 min', '30 a 40 min', 'Coberta', 'Descoberta']) +
          q('Peso da bolinha e diâmetro real (medido) de cada tamanho:', ['Broto ____ g · ____ cm', 'Média ____ g · ____ cm', 'Grande 320 g · ____ cm']) +
          q('Horário de produção da massa e marca do fermento:') +
          q('Quantas listras de catupiry vão em cada tamanho?', ['Broto ____', 'Média ____', 'Grande ____']) +
          q('Validade depois de preparados:', ['Ovo cozido ____', 'Cebola cortada ____', 'Gorgonzola picado ____', 'Provolone ralado ____']) +
          q('Portuguesa: em que etapa entra a cebola e qual é o corte?', ['Rodelas', 'Tiras', 'Cubos']) +
          q('Lombo: chega já fatiado ou é fatiado na casa? Marca?', ['Já fatiado', 'Fatiado na casa', 'Marca: __________']) +
          q('Marcas usadas:', ['Muçarela ______', 'Catupiry ______', 'Presunto ______', 'Gorgonzola ______', 'Provolone ______']) +
          q('A gerência quer manter a marca atual do catupiry?', ['Sim', 'Não']) +
          q('Como aplicar o catupiry com bico padrão?', ['Saco descartável + adaptador + bico', 'Bisnaga reutilizável', 'Aplicador', 'Ainda não decidido']) +
          q('Listra de catupiry com frisos (bico pitanga) ou lisa (bico perlê)? A balança da casa tem precisão de 1 g?', ['Com frisos', 'Lisa', 'Balança de 1 g: sim', 'Balança de 1 g: não']) + '</div>')

open('questionario.html', 'w').write(
    f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Questionário de briefing · Speciale</title>{PCSS}{EXTRA}</head><body>{capa}{p2}{p3}{p4}{p5}</body></html>')
