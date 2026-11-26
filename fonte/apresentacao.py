"""Apresentação · acompanhamento da Speciale (slides 16:9 em PDF)."""
from common import logo

RED, OR, CR, INK = '#d7141a', '#f07f1e', '#fcf3e8', '#231a18'
DATA = '[data a confirmar]'
CSS = f'''<style>
@import url('fonts.css');
@page{{size:338.67mm 190.5mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Poppins',sans-serif;color:{INK};-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.s{{width:338.67mm;height:190.5mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}}
.s:last-child{{page-break-after:auto}}
.chk{{position:absolute;left:0;right:0;height:9px;background:repeating-conic-gradient({RED} 0 25%,#fff 0 50%) 0 0/9px 9px}}
.in{{position:absolute;left:20mm;right:20mm;top:16mm;bottom:16mm}}
.k{{font-size:9pt;font-weight:600;letter-spacing:3px;color:{RED};text-transform:uppercase}}
h2{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:30pt;line-height:1;margin:2mm 0 6mm}}
h2 span{{color:{RED}}}
.n{{position:absolute;right:20mm;bottom:8mm;font-size:8pt;color:#999}}
.ft{{position:absolute;left:20mm;bottom:8mm;font-size:8pt;color:#999}}
.cols{{display:grid;gap:7mm;min-width:0}}.cols>*{{min-width:0}}
.card{{background:{CR};border-radius:6px;padding:6mm;border-top:4px solid {RED}}}
.card h4{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:14pt;margin-bottom:2.5mm}}
.card ul{{padding-left:5mm;font-size:12.5pt;line-height:1.5}}.card li{{margin:1mm 0}}.card li::marker{{color:{RED}}}
.big{{font-family:'Roboto Condensed';font-weight:800;color:{RED};font-size:34pt;line-height:1}}
.th{{display:flex;gap:4mm;align-items:flex-end;flex-wrap:wrap;justify-content:center}}
.th figure{{text-align:center;font-size:8pt;color:#555}}
.th img{{display:block;border-radius:3px;box-shadow:0 2mm 4mm rgba(0,0,0,.18);margin-bottom:2mm}}
.tl{{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:8mm}}
.tl .v{{border-radius:8px;padding:7mm;position:relative}}
.tl .v .d{{position:absolute;top:-6mm;left:7mm;width:12mm;height:12mm;border-radius:50%;background:{RED};color:#fff;font-family:'Roboto Condensed';font-weight:800;font-size:16pt;display:flex;align-items:center;justify-content:center}}
.tl h4{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:16pt;margin-top:3mm}}
.tl small{{font-size:9pt;color:#777}}
.tl ul{{padding-left:5mm;font-size:12.5pt;line-height:1.5;margin-top:3mm}}
.tag{{display:inline-block;font-size:8.5pt;font-weight:700;padding:1mm 3.5mm;border-radius:20mm;margin-top:2mm}}
table{{width:100%;border-collapse:collapse;font-size:12pt}}
th{{background:{INK};color:#fff;font-family:'Roboto Condensed';text-transform:uppercase;font-size:9.5pt;text-align:left;padding:2.5mm 3mm}}
td{{padding:3.6mm 3mm;border-bottom:1px solid #eadfd2}}
</style>'''

T = 10


def sl(n, k, title, body, dark=False):
    bg = f'background:{INK};color:#fff' if dark else ''
    return f'<section class="s" style="{bg}"><div class="chk" style="top:0"></div><div class="in"><div class="k">{k}</div><h2>{title}</h2>{body}</div><div class="ft">Speciale Pizzas Artesanais · Relatório de acompanhamento</div><div class="n">{n} / {T}</div></section>'


def th(items, h=62):
    return '<div class="th">' + ''.join(f'<figure><img src="thumbs/{f}.png" style="height:{h}mm">{c}</figure>' for f, c in items) + '</div>'


def ul(xs):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'


capa = f'''<section class="s" style="background:{RED};color:#fff"><div class="chk" style="top:0;background:repeating-conic-gradient(#fff 0 25%,{RED} 0 50%) 0 0/9px 9px"></div>
<div class="in"><div style="display:flex;align-items:center;gap:10px"><svg width="60" height="44" viewBox="0 0 46 34"><ellipse cx="9" cy="15" rx="8.5" ry="7" fill="#fff"/><ellipse cx="18" cy="27" rx="8" ry="6.5" fill="#fff"/><path d="M18 13 C21 4 33 1 45 2 C42 10 31 15 18 13Z" fill="#3aa63a"/></svg><div><div style="font-family:'Roboto Condensed';font-weight:800;font-size:24pt;line-height:1">SPECIALE</div><div style="font-size:7pt;letter-spacing:3px;font-weight:600">PIZZAS ARTESANAIS</div></div></div>
<div style="position:absolute;top:48mm;left:0;right:0">
<div style="font-size:11pt;font-weight:600;letter-spacing:4px;color:#ffd2ae">RELATÓRIO DE ACOMPANHAMENTO</div>
<div style="font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:56pt;line-height:.95;margin-top:4mm">O que fizemos<br><span style="color:#ffd2ae">na Speciale</span></div>
<p style="font-size:13pt;margin-top:6mm;max-width:190mm;opacity:.95">Diagnóstico, melhorias propostas e materiais entregues para organizar a operação, a marca e as boas práticas.</p></div>
<div style="position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;font-size:9.5pt;border-top:1px solid rgba(255,255,255,.4);padding-top:4mm"><span>Speciale Pizzas Artesanais · Recife</span><span>Novembro de 2026</span></div></div>
<div class="chk" style="bottom:0;background:repeating-conic-gradient(#fff 0 25%,{RED} 0 50%) 0 0/9px 9px"></div></section>'''

s2 = sl(2, 'Visão geral', 'Três visitas, <span>um plano</span>', f'''<div class="tl">
<div class="v" style="background:{CR}"><div class="d">1</div><h4>Diagnóstico</h4><small>1ª visita · {DATA}</small>
{ul(['Conversa com o proprietário', 'Diagnóstico do local e da operação', 'Questionários entregues à equipe'])}<span class="tag" style="background:#2f8a4e;color:#fff">Concluída</span></div>
<div class="v" style="background:{CR}"><div class="d">2</div><h4>Retorno e melhorias</h4><small>2ª visita · {DATA}</small>
{ul(['Retorno do diagnóstico', 'Melhorias propostas para a operação', 'Materiais de padronização, marca e boas práticas'])}<span class="tag" style="background:#2f8a4e;color:#fff">Concluída</span></div>
<div class="v" style="background:#fff;border:2px dashed {RED}"><div class="d">3</div><h4>Implantação</h4><small>3ª visita · a agendar</small>
{ul(['Treinamento da equipe por setor', 'Definição de responsáveis e supervisores', 'Aprovação e afixação dos POPs'])}<span class="tag" style="background:{OR};color:#fff">Próxima etapa</span></div></div>''')

s3 = sl(3, '1ª visita', 'Conhecer a casa <span>por dentro</span>', f'''<div class="cols" style="grid-template-columns:1fr 1fr 1fr">
<div class="card"><div class="big">01</div><h4 style="margin-top:3mm">Conversa com o dono</h4>{ul(['Objetivos do negócio e momento da casa', 'Mudança de cores e reforma do espaço', 'Principais dores na operação'])}</div>
<div class="card"><div class="big">02</div><h4 style="margin-top:3mm">Diagnóstico do local</h4>{ul(['Visita à cozinha, estoque, salão e área do forno', 'Acompanhamento da produção da massa e da montagem', 'Registro fotográfico da operação'])}</div>
<div class="card"><div class="big">03</div><h4 style="margin-top:3mm">Questionários à equipe</h4>{ul(['Questionários entregues aos funcionários', 'Rotina, dificuldades e sugestões de quem está na operação', 'Base para as melhorias propostas'])}</div></div>''')

s4 = sl(4, 'Diagnóstico', 'O que <span>observamos</span>', '<table><thead><tr><th style="width:28%">Ponto observado</th><th>Impacto</th><th style="width:30%">Melhoria proposta</th></tr></thead><tbody>' + ''.join(
    f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in [
        ('Tamanho da pizza definido “no olho”', 'Pizzas com tamanhos e custos diferentes; sobra de massa aparada', 'Peso da bolinha, gabarito e marcação na bancada'),
        ('Catupiry sem medida padrão', 'Quantidade varia por pizzaiolo; custo sem controle', 'Teste de pesagem e bico padrão'),
        ('Bisnaga com ponta cortada', 'Abertura muda a cada bisnaga', 'Saco descartável + adaptador + bico'),
        ('Procedimentos não documentados', 'Risco na fiscalização e treinamento difícil', '8 POPs, cartilha e sinalização'),
        ('Responsabilidades informais', 'Tarefas sem dono; ninguém confere', 'Divisão por praça e supervisores'),
        ('Nova fase: cores e reforma', 'Marca e cardápio desatualizados', 'Proposta de identidade e cardápio')]) + '</tbody></table>')

s5 = sl(5, '2ª visita · operação', 'Padronizar <span>para economizar</span>', '<div class="cols" style="grid-template-columns:1.1fr 1fr">' +
        f'<div class="card"><h4>Entregues</h4>{ul(["<b>Guia “Como medir o catupiry”</b>: comparação de métodos, teste de pesagem, formulários e conferência semanal.", "<b>Guia “Bico no catupiry”</b>: marcas, opções sem trocar o fornecedor e lista de compras.", "<b>Materiais e sugestão de compras</b>: gabarito, balança, termômetro e plano de compras."])}</div>' +
        th([('cat', 'Como medir o catupiry'), ('bico', 'Bico no catupiry')], 92) + '</div>')

s6 = sl(6, '2ª visita · marca', 'Uma marca para a <span>nova fase</span>', '<div class="cols" style="grid-template-columns:1fr 1.25fr">' +
        f'<div class="card"><h4>Propostas</h4>{ul(["<b>Proposta comercial</b> de identidade visual e cardápio, com pacotes e combos.", "<b>Cardápio em preto e verde</b>: tríptico de mesa e cardápio redondo, com preços (Média R$ 45).", "<b>Cardápio digital</b> no site, com pedido pelo WhatsApp.", "<b>Questionário de briefing</b> para fechar marca e cardápio."])}</div>' +
        th([('prop', 'Proposta'), ('dig', 'Cardápio digital'), ('quest', 'Briefing')], 62) + th([('card3', 'Cardápio em tamanho real')], 44) + '</div>')

s7 = sl(7, '2ª visita · boas práticas', 'Segurança dos alimentos <span>no papel e na parede</span>', '<div class="cols" style="grid-template-columns:1fr 1.45fr">' +
        f'<div class="card"><h4>Conforme a RDC ANVISA 216/2004</h4>{ul(["<b>8 POPs</b>: os 4 obrigatórios + recebimento, hortifrútis, forno a lenha e delivery/salão.", "<b>Duas versões</b>: manual completo (gestão) e guia da equipe.", "<b>Treinamento</b>: roteiro de 2 h, dinâmicas, avaliação e lista de presença.", "<b>Cartilha</b> para cada funcionário.", "<b>Sinalização</b>: cartazes dos POPs, lavagem das mãos, 16 adesivos e etiquetas."])}</div>' +
        th([('popg', 'Manual (gestão)'), ('pope', 'Guia da equipe'), ('sin2', 'Cartaz de POP'), ('cart', 'Cartilha')], 52) + '</div>')

s8 = sl(8, '2ª visita · equipe', 'Cada um <span>na sua praça</span>', '<div class="cols" style="grid-template-columns:1fr 1.1fr">' +
        f'<div class="card"><h4>Organização da equipe</h4>{ul(["<b>8 praças</b>: massa, pré-preparo, montagem, forno, expedição, atendimento e caixa, estoque e higienização.", "<b>Supervisor por turno</b>, com rotina de abertura, turno e fechamento.", "<b>Quem higieniza cada equipamento</b>: masseira, balança, forno, geladeiras, bisnagas.", "<b>Termo de responsabilidade</b> assinado por praça."])}</div>' +
        th([('prac', 'Divisão por praça'), ('trein', 'Treinamento')], 78) + '</div>')

s9 = sl(9, '3ª visita', 'Próximos <span>passos</span>', '<div class="cols" style="grid-template-columns:1fr 1fr">' +
        f'<div class="card"><h4>Na 3ª visita</h4>{ul(["Reunião com a gestão para definir responsáveis por setor e supervisores.", "Treinamento de higienização por equipe (setor de cima e pizzaiolos).", "Aprovação, assinatura e afixação dos POPs e cartazes.", "Início das planilhas de registro (temperatura, higienização, higiene pessoal).", "Teste de pesagem do catupiry com o bico padrão."])}</div>' +
        f'<div class="card" style="border-top-color:{OR}"><h4>Decisões da casa</h4>{ul(["Validade e armazenamento da massa (geladeira ou freezer).", "Empresa de controle de pragas e data da última limpeza da caixa d\'água.", "Produtos de limpeza e de hortifrútis em uso.", "Pacote de marca e cardápio e paleta de cores.", "Lista completa de sabores, bebidas e preços."])}</div></div>')

s10 = f'''<section class="s" style="background:{INK};color:#fff"><div class="chk" style="top:0"></div><div class="in">
<div style="position:absolute;top:40mm;left:0;right:0"><div class="k" style="color:#ffb98a">Resumo</div>
<div style="font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;font-size:44pt;line-height:1;margin-top:3mm">Diagnóstico feito.<br>Melhorias entregues.<br><span style="color:{OR}">Agora, implantar.</span></div>
<div style="display:flex;gap:12mm;margin-top:10mm">''' + ''.join(f'<div><div class="big" style="color:{OR}">{a}</div><div style="font-size:10pt;opacity:.85;margin-top:1mm">{b}</div></div>' for a, b in [('2', 'visitas realizadas'), ('8', 'POPs elaborados'), ('8', 'praças organizadas'), ('1', 'visita de implantação')]) + '''</div></div></div>
<div class="chk" style="bottom:0"></div></section>'''

open('apresentacao.html', 'w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Speciale · Relatório de acompanhamento</title>{CSS}</head><body>{capa}{s2}{s3}{s4}{s5}{s6}{s7}{s8}{s9}{s10}</body></html>')
