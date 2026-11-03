s = open('ficha_lombinho.py').read()
s = s.replace("em pedaços (≈9 g) e <b>polvilhar orégano</b> a olho, antes de ir ao forno.'),",
              "em pedaços (≈9 g) e <b>polvilhar orégano</b> a olho, antes de ir ao forno.' + foto(1)),")
s = s.replace("e a borda assar.' + foto(1) + pcc(3))", "e a borda assar.' + foto(2) + pcc(3))")
i = s.index('FOTOS_PEND = ['); j = s.index('dot = lambda', i)
s = s[:i] + '''fotos = [
    (1, 'lombo-foto1', 'Pronta para o forno', 'Etapa 7', 'Pizza crua sobre a pá, na boca do forno a lenha: fatias redondas de lombo sobrepostas cobrindo a pizza, muçarela aparecendo por baixo na borda, listras onduladas de catupiry em paralelo, azeitona preta em pedaços e orégano por cima.', '50% 88%'),
    (2, 'lombo-foto2', 'Pizza assada', 'Etapa 8', 'Detalhe da pizza saída do forno: lombo levemente dourado nas bordas das fatias, muçarela derretida, listras de catupiry inteiras e cremosas, azeitona preta em pedaços, orégano e borda dourada.', '50% 50%'),
]
gal = ''.join(f\'\'\'<div class="ph"><div class="im" style="height:118mm"><img src="img/{f}.jpg" style="object-position:{pos}"><span class="lb">FOTO {n}</span></div>
<h4>{t}</h4><p><b>{e}</b> · {d}</p></div>\'\'\' for n, f, t, e, d, pos in fotos)
p4 = sec('05', 'Guia visual de fotos') + '<p class="note" style="margin:-1mm 0 4mm">Registro fotográfico enviado pela casa. Cada foto aparece uma única vez e corresponde à etapa indicada. Use como referência de distribuição e de ponto.</p>' \\
    + f'<div class="gal">{gal}</div>' \\
    + '<div class="box" style="margin-top:6mm"><h5>O que as fotos mostram</h5><ul class="dot">' \\
    + '<li>O lombo aparece por cima da muçarela e por baixo do catupiry, o que reforça a ordem desta ficha.</li>' \\
    + '<li>A azeitona preta vai em pedaços, espalhada por cima, junto com o orégano.</li>' \\
    + '<li>Não há fotos da massa aberta nem da muçarela: vale fotografar essas etapas para completar o guia.</li></ul></div>'

''' + s[j:]
s = s.replace("'<b>Fotos da montagem:</b> fotografar uma pizza Grande nas etapas da seção 05 para completar o guia visual.'",
              "'<b>Fotos da montagem:</b> fotografar as etapas de massa aberta e muçarela para completar o guia visual.'")
s = s.replace("        'Fotos reais da montagem e da pizza pronta.',\n", "")
s = s.replace("'Se o lombo entra logo depois da muçarela, como na Frango com Catupiry.'",
              "'Se o lombo entra logo depois da muçarela (as fotos indicam que sim).'")
open('ficha_lombinho.py', 'w').write(s)

o = open('op_lombinho.py').read()
o = o.replace("tip('Listras paralelas, de um lado ao outro da pizza'))",
              "'<div class=\"pic t\" style=\"height:58mm\"><img src=\"img/lombo-foto1.jpg\" style=\"object-position:50% 88%\"><em>FOTO 1</em><span>Pronta para o forno</span></div>')")
o = o.replace("tip('Foto a enviar · ponto: muçarela derretida, catupiry levemente dourado, borda assada'))",
              "'<div class=\"pic t\" style=\"height:58mm\"><img src=\"img/lombo-foto2.jpg\" style=\"object-position:50% 50%\"><em>FOTO 2</em><span>Ponto: catupiry cremoso, borda dourada</span></div>')")
o = o.replace("a etapa do lombo segue a Frango com Catupiry e está", "a etapa do lombo segue as fotos (sobre a muçarela) e está")
open('op_lombinho.py', 'w').write(o)
