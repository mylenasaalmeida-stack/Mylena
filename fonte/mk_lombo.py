s = open('ficha_frango.py').read()
R = [
    ("PIZZA FRANGO COM CATUPIRY", "PIZZA DE LOMBINHO"),
    ('<h1 style="font-size:42pt">Pizza Frango<span>com Catupiry</span></h1>', '<h1>Pizza de<span>Lombinho</span></h1>'),
    ("Frango pré-preparado, muçarela e listras de catupiry", "Lombo fatiado, muçarela e listras de catupiry"),
    ("<b>140 g</b><small>de frango pré-preparado por pizza Grande</small>", "<b>105 g</b><small>de lombo fatiado por pizza Grande</small>"),
    ("'Pizza Frango com Catupiry'", "'Pizza de Lombinho'"),
    ("Alérgenos do tempero do frango: ver Orientações finais (seção 13).'", "Conferir também o rótulo do lombo.'"),
    ("muçarela, frango pré-preparado e listras", "muçarela, lombo fatiado e listras"),
    ("['Frango', '140 g', 'Pré-preparado e porcionado (ver Orientações finais)', 'Recheio principal']", "['Lombo', '105 g', 'Fatiado, distribuído sobre a muçarela', 'Recheio principal']"),
    ("'Conferir bolinha, muçarela, frango e azeitona'", "'Conferir bolinha, muçarela, lombo e azeitona'"),
    ("muçarela e frango porcionados", "muçarela e lombo porcionados"),
    ("('Distribuir o frango', ' (140 g) logo depois da muçarela, por toda a pizza, até perto da borda.' + pcc(2))",
     "('Distribuir o lombo', ' fatiado (105 g) logo depois da muçarela, por toda a pizza, até perto da borda.' + pcc(2) + ac('ETAPA A CONFIRMAR'))"),
    ("('Frango', '140 g')", "('Lombo', '105 g')"),
    ("frango pré-preparado, muçarela e catupiry refrigerados", "lombo, muçarela e catupiry refrigerados"),
    ("frango 140 g · azeitona", "lombo 105 g · azeitona"),
    ("['Frango', '140 g', '≈88 g', '≈70 g']", "['Lombo', '105 g', '≈66 g', '≈53 g']"),
    ("(molho, muçarela, frango, catupiry e azeitona)", "(molho, muçarela, lombo, catupiry e azeitona)"),
    ("e frango distribuído por igual", "e lombo distribuído por igual"),
    ("['Frango ressecado ou queimado', 'Frango por cima sem proteção ou forno quente demais', 'Distribuir o frango sobre a muçarela e conferir o tempo de 3 a 4 min']",
     "['Lombo ressecado ou queimado', 'Fatias soltas por cima ou forno quente demais', 'Distribuir o lombo sobre a muçarela e conferir o tempo de 3 a 4 min']"),
    ("['Frango concentrado no centro', 'Distribuição apressada', 'Espalhar os 140 g por toda a pizza, até perto da borda']",
     "['Lombo concentrado no centro', 'Distribuição apressada', 'Espalhar os 105 g por toda a pizza, até perto da borda'],\n        ['Sabor salgado demais', 'Lombo acima da porção', 'Pesar o lombo (105 g)']"),
    ("['Pizza encharcada', 'Molho demais ou frango muito úmido', 'Medir o molho com a colher funda e escorrer o frango antes de usar']",
     "['Pizza encharcada', 'Molho demais', 'Medir o molho com a colher funda']"),
    ("['Frango pré-preparado', 'Refrigerado, porcionado em recipiente tampado e etiquetado', 'Conforme ficha do frango']",
     "['Lombo fatiado', 'Refrigerado, na embalagem ou porcionado em recipiente tampado e etiquetado', 'Conforme rótulo']"),
    ("muçarela (280 g) e frango (140 g) já pesados", "muçarela (280 g) e lombo (105 g) já pesados"),
    ("'Aparência', 'Frango distribuído por toda a pizza;", "'Aparência', 'Fatias de lombo distribuídas por toda a pizza;"),
    ("'Frango temperado e úmido, sem ressecar; catupiry cremoso; orégano sem queimar'", "'Lombo macio, sem ressecar nem queimar nas bordas; catupiry cremoso; orégano sem queimar'"),
    ("'<b>Fotos da Grande:</b> fotografar a montagem de uma pizza Grande para completar o guia visual.'", "'<b>Fotos da montagem:</b> fotografar uma pizza Grande nas etapas da seção 05 para completar o guia visual.'"),
    ("        'Quantidade de listras de catupiry por tamanho.',\n",
     "        'Quantidade de listras de catupiry por tamanho.',\n        'Se o lombo entra logo depois da muçarela, como na Frango com Catupiry.',\n        'Tipo de lombo (defumado/canadense ou preparado na casa) e marca.',\n        'Fotos reais da montagem e da pizza pronta.',\n"),
    ("open('ficha_frango.html'", "open('ficha_lombinho.html'"),
    ("Ficha Técnica Pizza Frango com Catupiry", "Ficha Técnica Pizza de Lombinho"),
]
for a, b in R:
    assert a in s, a
    s = s.replace(a, b)
i = s.index("p4 = sec('05'"); j = s.index("dot = lambda", i)
s = s[:i] + open('p4_lombo.txt').read() + s[j:]
i = s.index("'<b>Fazer a ficha técnica do frango pré-preparado.</b>"); j = s.index("'<b>Média e Broto são estimativas.</b>")
s = s[:i] + ("'<b>Lombo fatiado:</b> esta ficha considera o lombo comprado já fatiado, com validade e alérgenos conforme o rótulo. "
             "Se o lombo for preparado ou temperado na casa, ele precisa de ficha técnica própria (preparo, resfriamento, armazenamento, "
             "validade e alérgenos), como pede a RDC 216/2004.',\n        ") + s[j:]
s = s.replace("' (140 g) por toda", "' (105 g) por toda")
open('ficha_lombinho.py', 'w').write(s)

# receita simplificada
o = open('op_frango.py').read()
O = [
    ("NOME = 'Pizza Frango com Catupiry'", "NOME = 'Pizza de Lombinho'"),
    ("('Frango', 'pré-preparado e porcionado', '140 g')", "('Lombo', 'fatiado', '105 g')"),
    ("<th>Frango</th>", "<th>Lombo</th>"),
    ("'280 g', '140 g', '≈9 g'", "'280 g', '105 g', '≈9 g'"),
    ("'≈175 g', '≈88 g', '≈6 g'", "'≈175 g', '≈66 g', '≈6 g'"),
    ("'≈140 g', '≈70 g', '≈5 g'", "'≈140 g', '≈53 g', '≈5 g'"),
    ("header('Frango com Catupiry', 'Receita da produção', 1)", "header('Pizza de Lombinho', 'Receita da produção', 1)"),
    ("<b>140 g</b><small>de frango</small>", "<b>105 g</b><small>de lombo fatiado</small>"),
    ("<li>Frango e muçarela porcionados e na geladeira</li>", "<li>Lombo e muçarela porcionados e na geladeira</li>"),
    ("'Molho, muçarela e frango'", "'Molho, muçarela e lombo'"),
    ("distribua os <b>140 g de frango</b> por toda a pizza", "distribua os <b>105 g de lombo fatiado</b> por toda a pizza"),
    ("'<div class=\"al\"><b>Frango sempre sobre a muçarela.</b> Assim ele não resseca no forno.</div>'",
     "'<div class=\"al\"><b>Atenção:</b> a etapa do lombo segue a Frango com Catupiry e está <span class=\"tbc\">a confirmar</span>.</div>'"),
    ("tip('Frango espalhado por igual, sem montes no centro')", "tip('Lombo espalhado por igual, sem montes no centro')"),
    ("<b>Frango ressecado?</b>", "<b>Lombo ressecado?</b>"),
    ("'<div class=\"pic t\" style=\"height:62mm\"><img src=\"img/frango-foto1.jpg\" style=\"object-position:50% 45%\"><em>FOTO 1</em><span>Ponto de saída (foto de uma Broto)</span></div>'",
     "tip('Foto a enviar · ponto: muçarela derretida, catupiry levemente dourado, borda assada')"),
    ("frango bem distribuído, listras", "lombo bem distribuído, listras"),
    ("<h4>Frango pré-preparado</h4><b>Ver ficha</b><p>Geladeira, porcionado e etiquetado. Validade conforme a ficha do frango.</p>",
     "<h4>Lombo fatiado</h4><b>Rótulo</b><p>Geladeira, na embalagem ou em pote tampado e etiquetado.</p>"),
    ("<li>Pese: muçarela 280 g e frango 140 g.</li>", "<li>Pese: muçarela 280 g e lombo 105 g.</li>"),
    ("<li>Frango na geladeira até a hora de montar.</li>", "<li>Lombo na geladeira até a hora de montar.</li>"),
    ("<li>Frango com cheiro azedo, pegajoso ou com cor estranha.</li>", "<li>Lombo pegajoso, com limo, cheiro azedo ou cor estranha.</li>"),
    ("deixe o frango ou a muçarela", "deixe o lombo ou a muçarela"),
    ("<li><b>Ficha do frango:</b> ainda precisa ser feita. O frango é preparado antes e guardado; sem ficha não há padrão de tempero, validade nem lista de alérgenos dos temperos.</li>",
     "<li><b>Lombo:</b> considerado comprado já fatiado (validade do rótulo). Se for preparado na casa, precisa de ficha própria.</li>"),
    ("receita_op_frango.html", "receita_op_lombinho.html"),
    ("Receita de Produção Pizza Frango com Catupiry", "Receita de Produção Pizza de Lombinho"),
]
for a, b in O:
    assert a in o, a
    o = o.replace(a, b)
open('op_lombinho.py', 'w').write(o)
