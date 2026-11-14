"""Artes do Instagram · Mylena | Cozinha Estratégica (PNG 1080 px)."""
INK, G, G2, OW = '#0e100f', '#2f8a4e', '#9fd18b', '#f4f1ea'
AT = '@mylena.cozinhaestrategica'
P = 'img/mylena/'

CSS = f'''<style>
@import url('fonts.css');
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#777;font-family:'Poppins',sans-serif;-webkit-font-smoothing:antialiased}}
.a{{position:relative;overflow:hidden;margin:20px;display:block}}
.sq{{width:1080px;height:1080px}}.p{{width:1080px;height:1350px}}.st{{width:1080px;height:1920px}}
.ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.H{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;line-height:.95;letter-spacing:-.5px}}
.ov{{font-weight:600;letter-spacing:6px;text-transform:uppercase;font-size:24px}}
.tag{{display:inline-block;background:{G};color:#fff;font-weight:600;font-size:26px;padding:10px 26px;border-radius:40px}}
.foot{{position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:500}}
.dots span{{display:inline-block;width:14px;height:14px;border-radius:50%;background:currentColor;opacity:.35;margin-left:10px}}
.dots span.on{{opacity:1}}
.n{{font-family:'Roboto Condensed';font-weight:800;font-size:220px;line-height:.8;color:{G2}}}
.bd{{font-size:36px;line-height:1.45}}
</style>'''


def dots(i, n):
    return '<span class="dots">' + ''.join(f'<span class="{"on" if k == i else ""}"></span>' for k in range(n)) + '</span>'


def foot(i, n, color='#fff', swipe=True):
    right = dots(i, n) if n > 1 else ''
    left = AT
    return f'<div class="foot" style="color:{color}"><span>{left}</span><span>{"Arraste →  " if swipe and i == 0 and n > 1 else ""}{right}</span></div>'


arts = []

# 0. Foto de perfil
arts.append(('00_foto_perfil', 'sq', f'''<img class="ph" src="{P}perfil-recorte.jpg">'''))

# 1. Post fixado · carrossel "Prazer, sou a Mylena" (3 slides)
N = 3
arts.append(('01_fixado_1_capa', 'p', f'''<img class="ph" src="{P}feira-sorrindo.jpg" style="object-position:62% 30%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,16,15,0) 40%,rgba(14,16,15,.92) 78%)"></div>
<div style="position:absolute;left:80px;right:80px;bottom:170px;color:#fff">
<div class="ov" style="color:{G2}">Cozinha estratégica</div>
<div class="H" style="font-size:132px;margin-top:18px">Prazer,<br>sou a <span style="color:{G2}">Mylena</span></div>
<div class="bd" style="margin-top:26px;color:#e6e9e4">Eu ajudo restaurantes, bares e delivery a lucrar com o que já vendem.</div></div>{foot(0, N)}'''))
pil = [('Custo certo', 'Quanto custa cada prato e quanto sobra de verdade.'),
       ('Cardápio que vende', 'Organização, preço e destaque para o que dá lucro.'),
       ('Marca que atrai', 'Identidade visual e Instagram que trazem cliente.')]
arts.append(('01_fixado_2_o_que_faco', 'p', f'''<div style="position:absolute;inset:0;background:{INK}"></div>
<div style="position:absolute;left:80px;right:80px;top:110px;color:#fff">
<div class="ov" style="color:{G2}">O que eu faço</div>
<div class="H" style="font-size:96px;margin:18px 0 60px">Restaurante<br>que <span style="color:{G2}">lucra</span></div>''' + ''.join(
    f'''<div style="display:grid;grid-template-columns:120px 1fr;gap:20px;align-items:start;padding:34px 0;border-top:2px solid #2a2e2b">
<div class="H" style="font-size:90px;color:{G}">{i}</div><div><div class="H" style="font-size:52px">{t}</div><div class="bd" style="color:#b9bfb8;margin-top:10px">{d}</div></div></div>''' for i, (t, d) in enumerate(pil, 1)) +
    f'</div>{foot(1, N)}'))
arts.append(('01_fixado_3_comece', 'p', f'''<div style="position:absolute;inset:0;background:{G}"></div>
<div style="position:absolute;left:80px;right:80px;top:130px;color:#fff">
<div class="ov" style="color:#dff0d6">Como começar</div>
<div class="H" style="font-size:112px;margin:20px 0 46px">Diagnóstico<br>de lucro<br>gratuito</div>
<div class="bd" style="font-size:40px">Em 30 minutos, a gente calcula juntos o custo e a margem de 1 produto do seu cardápio. Você sai com um número real na mão.</div>
<div style="margin-top:60px;background:{INK};border-radius:24px;padding:42px 46px">
<div class="H" style="font-size:54px;color:{G2}">Me chama no WhatsApp</div><div class="bd" style="margin-top:12px">Link na bio · Recife e Região Metropolitana</div></div></div>{foot(2, N)}'''))

# 2. Carrossel de autoridade "3 erros" (5 slides)
N = 5
erros = [('Copiar o preço do concorrente', 'Se você não sabe quanto custa o seu prato, o preço do vizinho pode estar te dando prejuízo a cada venda.', 'Calcule o custo de cada item antes de definir o preço.'),
         ('Porção sem padrão', 'Cada pessoa da equipe serve de um jeito. A mesma pizza sai com pesos diferentes, e o lucro some sem ninguém ver.', 'Ficha de custo com a quantidade de cada ingrediente.'),
         ('Olhar só o faturamento', 'Caixa cheio não é lucro. O que importa é quanto sobra depois de pagar os ingredientes e as despesas.', 'Acompanhe o CMV todo mês.')]
arts.append(('02_carrossel_1_capa', 'p', f'''<img class="ph" src="{P}feira-seria.jpg" style="object-position:58% 28%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,16,15,0) 40%,rgba(14,16,15,.93) 74%)"></div>
<div style="position:absolute;left:80px;right:80px;bottom:150px;color:#fff">
<div class="ov" style="color:{G2}">Restaurante sem lucro</div>
<div class="H" style="font-size:100px;margin-top:20px"><span style="color:{G2}">3 erros</span> que fazem<br>o restaurante vender<br>e não lucrar</div></div>{foot(0, N)}'''))
for i, (t, d, f) in enumerate(erros, 1):
    arts.append((f'02_carrossel_{i + 1}_erro{i}', 'p', f'''<div style="position:absolute;inset:0;background:{INK if i != 2 else OW}"></div>
<div style="position:absolute;left:80px;right:80px;top:110px;color:{"#fff" if i != 2 else INK}">
<div class="n" style="{"" if i != 2 else f"color:{G}"}">{i}</div>
<div class="ov" style="color:{G2 if i != 2 else G};margin-top:40px">Erro {i}</div>
<div class="H" style="font-size:96px;margin:16px 0 40px">{t}</div>
<div class="bd" style="font-size:40px;color:{"#c9cec8" if i != 2 else "#3c403d"}">{d}</div>
<div style="margin-top:60px;border-left:10px solid {G};padding:10px 0 10px 34px">
<div class="ov" style="color:{G2 if i != 2 else G};font-size:22px">Como resolver</div>
<div class="H" style="font-size:52px;margin-top:10px">{f}</div></div></div>{foot(i, N, "#fff" if i != 2 else INK)}'''))
arts.append(('02_carrossel_5_cta', 'p', f'''<div style="position:absolute;inset:0;background:{G}"></div>
<div style="position:absolute;left:80px;right:80px;top:150px;color:#fff">
<div class="ov" style="color:#dff0d6">Se identificou?</div>
<div class="H" style="font-size:118px;margin:22px 0 46px">Comente<br><span style="background:{INK};padding:0 24px">CMV</span></div>
<div class="bd" style="font-size:42px">e eu te mando o passo a passo para calcular o CMV de 1 produto do seu cardápio.</div>
<div class="bd" style="margin-top:56px;font-size:36px;color:#e8f5e0">Salve este post para revisar com a sua equipe.</div></div>{foot(4, N)}'''))

# 3. Post de bastidor (feira)
arts.append(('03_bastidor_feira', 'p', f'''<img class="ph" src="{P}close-sorrindo.jpg" style="object-position:50% 40%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,16,15,0) 52%,rgba(14,16,15,.9) 82%)"></div>
<div style="position:absolute;left:80px;right:80px;bottom:160px;color:#fff">
<span class="tag">Bastidores</span>
<div class="H" style="font-size:96px;margin-top:26px">Onde o food service<br>vai buscar <span style="color:{G2}">solução</span></div>
<div class="bd" style="margin-top:20px;color:#e6e9e4">O que eu vi na [nome da feira] e o que dá para levar para o seu restaurante.</div></div>{foot(0, 1)}'''))

# 4. Capa de Reels / story
arts.append(('04_capa_reels', 'st', f'''<img class="ph" src="{P}selfie-preta.jpg" style="object-position:50% 30%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,16,15,.0) 45%,rgba(14,16,15,.92) 75%)"></div>
<div style="position:absolute;left:80px;right:80px;bottom:300px;color:#fff">
<span class="tag">Cozinha estratégica</span>
<div class="H" style="font-size:132px;margin-top:30px">Seu restaurante<br>vende muito e<br><span style="color:{G2}">lucra pouco?</span></div>
<div class="bd" style="margin-top:26px;font-size:40px;color:#e6e9e4">Assista até o fim: é aqui que o dinheiro escapa.</div></div>
<div class="foot" style="color:#fff;bottom:120px"><span>{AT}</span></div>'''))

html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{CSS}</head><body>' + ''.join(
    f'<div class="a {c}" id="{n}">{b}</div>' for n, c, b in arts) + '</body></html>'
open('artes_ig.html', 'w').write(html)
open('artes_ig.list', 'w').write('\n'.join(n for n, _, _ in arts))
