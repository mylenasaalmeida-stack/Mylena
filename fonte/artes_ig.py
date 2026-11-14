"""Artes do Instagram v4 · direção "Bastidor com autoridade" (inspirada nos feeds de referência)."""
INK, OW, G, LG = '#0C0E0D', '#F4F1EA', '#2F8A4E', '#A9DB8C'
AT = '@mylena.cozinhaestrategica'
P = 'img/mylena/'
I = 'img/'

CSS = f'''<style>
@import url('fonts.css');@import url('fonts2.css');@import url('fonts3.css');
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#888;font-family:'Poppins',sans-serif;-webkit-font-smoothing:antialiased}}
.a{{position:relative;overflow:hidden;margin:20px;display:block;background:{OW};color:{INK}}}
.sq{{width:1080px;height:1080px}}.p{{width:1080px;height:1350px}}.st{{width:1080px;height:1920px}}
.ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,14,13,0) 45%,rgba(12,14,13,.88) 82%)}}
.shadeT{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,14,13,.8) 0,rgba(12,14,13,0) 34%)}}
.hook{{font-family:'Poppins';font-weight:700;color:#fff;letter-spacing:-1.5px;line-height:1.08}}
.it{{font-family:'Playfair Display';font-style:italic;font-weight:700;color:{LG};letter-spacing:-1px}}
.box{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;line-height:1;letter-spacing:-.5px;background:#fff;color:{INK};padding:14px 26px 8px;display:inline-block}}
.sm{{font-size:30px;font-weight:500;color:#e8ebe6}}
.tw{{font-size:46px;line-height:1.35;font-weight:500;letter-spacing:-.5px}}
</style>'''


def avatar(name='Mylena'):
    return f'''<div style="display:flex;align-items:center;gap:22px"><div style="width:96px;height:96px;border-radius:50%;overflow:hidden"><img src="artes_tmp_perfil.jpg" style="width:100%;height:100%;object-fit:cover"></div>
<div><div style="font-size:34px;font-weight:700">{name}</div><div style="font-size:26px;color:#6c716d">{AT}</div></div></div>'''


arts = []

# Foto de perfil
arts.append(('00_foto_perfil', 'sq', f'<img class="ph" src="{P}close-sorrindo_ed.jpg" style="object-position:52% 20%;transform:scale(1.45);transform-origin:52% 24%">'))

# FIXADO 1 · quem sou (foto + gancho)
arts.append(('01_fixado_1_quem_sou', 'p', f'''<img class="ph" src="{P}feira-nova.jpg" style="object-position:50% 20%"><div class="shade"></div>
<div style="position:absolute;left:80px;right:80px;bottom:110px">
<div class="sm" style="margin-bottom:22px">Prazer, sou a Mylena.</div>
<div class="hook" style="font-size:66px">Seu restaurante não<br>precisa vender mais.</div>
<div class="hook" style="font-size:66px;margin-top:14px">Precisa <span class="it" style="font-size:74px">lucrar</span> com<br>o que já vende.</div></div>'''))

# FIXADO 2 · case (cliente real · usar só com autorização)
arts.append(('01_fixado_2_case', 'p', f'''<img class="ph" src="{I}lombo-foto1.jpg" style="object-position:50% 50%"><div class="shadeT"></div><div class="shade"></div>
<div style="position:absolute;left:80px;top:80px"><span class="box" style="font-size:30px;background:{G};color:#fff">Case · Recife</span></div>
<div style="position:absolute;left:80px;right:80px;bottom:110px">
<div class="hook" style="font-size:80px">Como uma pizzaria<br>passou a servir <span class="it" style="font-size:88px">igual</span><br>todos os dias.</div>
<div class="sm" style="margin-top:22px">Fichas de custo, cardápio novo e marca.</div></div>'''))

# FIXADO 3 · oferta em formato "nota/tweet"
arts.append(('01_fixado_3_diagnostico', 'p', f'''<div style="position:absolute;left:90px;right:90px;top:200px">{avatar()}
<div class="tw" style="margin-top:56px">Em 30 minutos eu calculo com você o custo e o lucro real de 1 produto do seu cardápio.</div>
<div class="tw" style="margin-top:40px">Sem planilha complicada. Sem custo.</div>
<div style="margin-top:70px;font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:64px;color:{G}">Diagnóstico de lucro gratuito.</div>
<div style="margin-top:20px;font-size:30px;color:#6c716d">Agende pelo link na bio.</div></div>'''))

# CARROSSEL · capa com gancho na foto
arts.append(('02_carrossel_1_capa', 'p', f'''<img class="ph" src="{P}feira-seria_ed.jpg" style="object-position:58% 24%"><div class="shade"></div>
<div style="position:absolute;left:80px;right:80px;bottom:110px">
<div class="hook" style="font-size:82px">3 erros que fazem o restaurante vender e <span class="it" style="font-size:90px">não lucrar.</span></div>
<div class="sm" style="margin-top:22px">O terceiro é o mais comum →</div></div>'''))
erros = [('Copiar o preço do concorrente.', 'Sem saber o custo do prato, o preço do vizinho pode dar prejuízo a cada venda.', 'Calcule o custo de cada item antes de definir o preço.'),
         ('Servir sem porção padrão.', 'Cada pessoa da equipe serve de um jeito, e o lucro muda a cada prato.', 'Defina a quantidade de cada ingrediente numa ficha de custo.'),
         ('Olhar só o faturamento.', 'Caixa cheio não é lucro. O que importa é quanto sobra no fim do mês.', 'Acompanhe o CMV todo mês, não só o caixa.')]
for i, (t, d, f) in enumerate(erros, 1):
    arts.append((f'02_carrossel_{i + 1}_erro{i}', 'p', f'''<div style="position:absolute;left:90px;right:90px;top:200px">
<div style="font-size:30px;font-weight:600;color:{G}">Erro {i} de 3</div>
<div style="font-size:88px;font-weight:700;letter-spacing:-2px;line-height:1.08;margin-top:24px">{t}</div>
<div class="tw" style="margin-top:44px;color:#4b504c">{d}</div>
<div style="margin-top:80px;padding-left:34px;border-left:8px solid {G}">
<div style="font-size:28px;font-weight:600;color:{G}">Como resolver</div>
<div style="font-family:'Playfair Display';font-style:italic;font-weight:700;font-size:54px;line-height:1.2;margin-top:8px">{f}</div></div></div>
<div style="position:absolute;left:90px;bottom:80px;font-size:24px;color:#8a8f8b">{AT}</div>'''))
arts.append(('02_carrossel_5_cta', 'p', f'''<img class="ph" src="{P}close-sorrindo_ed.jpg" style="object-position:50% 25%"><div class="shade"></div>
<div style="position:absolute;left:80px;right:80px;bottom:110px">
<div class="hook" style="font-size:96px">Comente <span class="it" style="font-size:104px">CMV</span></div>
<div class="sm" style="margin-top:24px;font-size:34px">e eu te mando o passo a passo para calcular o custo de 1 produto.</div></div>'''))

# POST · frase em card branco (estilo "nota")
arts.append(('05_frase_mais_vende', 'p', f'''<div style="position:absolute;left:90px;right:90px;top:420px">
<div style="font-size:86px;font-weight:700;letter-spacing:-2px;line-height:1.12">O prato que você mais vende pode ser o que <span style="font-family:'Playfair Display';font-style:italic;color:{G}">menos te dá lucro.</span></div>
<div class="tw" style="margin-top:50px;color:#6c716d;font-size:38px">E você só descobre fazendo a conta.</div></div>
<div style="position:absolute;left:90px;bottom:80px;font-size:24px;color:#8a8f8b">{AT}</div>'''))

# POST · tweet com comparação visual (sem números inventados)
bars = ''.join(f'''<div style="flex:1"><div style="font-size:26px;font-weight:600;color:#6c716d;margin-bottom:14px">{m}</div>
<div style="display:flex;gap:16px;align-items:flex-end;height:330px">
<div style="flex:1;height:100%;background:#d8d3c7;border-radius:12px 12px 0 0;display:flex;align-items:flex-end;justify-content:center;padding-bottom:14px;font-size:22px;font-weight:600">Vendas</div>
<div style="flex:1;height:{h}%;background:{c};border-radius:12px 12px 0 0;display:flex;align-items:flex-end;justify-content:center;padding-bottom:14px;font-size:22px;font-weight:600;color:#fff">Lucro</div></div></div>''' for m, h, c in [('Mês 1', 62, G), ('Mês 2', 22, '#c8361f')])
arts.append(('06_tweet_mesmas_vendas', 'p', f'''<div style="position:absolute;left:90px;right:90px;top:150px">{avatar()}
<div class="tw" style="margin-top:50px">Você pode vender a mesma quantidade em dois meses e ter lucros <b>completamente diferentes.</b></div>
<div style="display:flex;gap:60px;margin-top:70px;background:#fff;border-radius:24px;padding:44px">{bars}</div>
<div style="font-size:24px;color:#8a8f8b;margin-top:18px">Ilustração. A diferença costuma estar no custo e na porção.</div></div>'''))

# BASTIDOR
arts.append(('03_bastidor_feira', 'p', f'''<img class="ph" src="{P}close-sorrindo_ed.jpg" style="object-position:50% 20%"><div class="shade"></div>
<div style="position:absolute;left:80px;right:80px;bottom:110px">
<div class="hook" style="font-size:70px">Fui à feira de food service e trouxe <span class="it" style="font-size:78px">3 ideias</span> para o seu restaurante.</div></div>'''))

# CAPA DE REELS · caixas condensadas (estilo Joel Jota), fora do rosto
arts.append(('04_capa_reels', 'st', f'''<img class="ph" src="{P}selfie-preta_ed.jpg" style="object-position:50% 22%">
<div style="position:absolute;left:0;right:0;top:1180px;text-align:center">
<div><span class="box" style="font-size:104px">Vende muito</span></div>
<div style="margin-top:12px"><span class="box" style="font-size:104px">e lucra pouco?</span></div></div>'''))

html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{CSS}</head><body>' + ''.join(
    f'<div class="a {c}" id="{n}">{b}</div>' for n, c, b in arts) + '</body></html>'
open('artes_ig.html', 'w').write(html)
open('artes_ig.list', 'w').write('\n'.join(n for n, _, _ in arts))
