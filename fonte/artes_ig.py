"""Artes do Instagram v3 · direção "Relatório" · minimalismo editorial (PNG 1080 px)."""
INK, OW, G = '#0C0E0D', '#F4F1EA', '#2F8A4E'
AT = '@mylena.cozinhaestrategica'
P = 'img/mylena/'

CSS = f'''<style>
@import url('fonts.css');@import url('fonts3.css');
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#888;font-family:'Poppins',sans-serif;-webkit-font-smoothing:antialiased}}
.a{{position:relative;overflow:hidden;margin:20px;display:block;background:{OW};color:{INK}}}
.sq{{width:1080px;height:1080px}}.p{{width:1080px;height:1350px}}.st{{width:1080px;height:1920px}}
.dark{{background:{INK};color:{OW}}}
.S{{font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1;font-family:'Playfair Display';font-weight:600;letter-spacing:-1.5px;line-height:1.04}}
.k{{position:absolute;left:80px;top:80px;font-size:20px;font-weight:600;letter-spacing:4px;text-transform:uppercase;opacity:.55}}
.cnt{{position:absolute;right:80px;top:80px;font-size:20px;font-weight:500;letter-spacing:2px;opacity:.55}}
.sig{{position:absolute;left:80px;bottom:72px;font-size:20px;font-weight:500;opacity:.6}}
.sup{{font-size:32px;line-height:1.45;font-weight:400}}
.rule{{height:1.5px;background:currentColor;opacity:.25}}
.img{{position:absolute;overflow:hidden}}.img img{{width:100%;height:100%;object-fit:cover;display:block}}
</style>'''


def frame(kicker, cnt=''):
    return f'<div class="k">{kicker}</div><div class="cnt">{cnt}</div><div class="sig">{AT}</div>'


arts = []

# e) Foto de perfil
arts.append(('00_foto_perfil', 'sq', f'''<div class="img" style="inset:0"><img src="{P}close-sorrindo_ed.jpg" style="object-position:52% 20%;transform:scale(1.45);transform-origin:52% 24%"></div>'''))

# a) Post fixado
arts.append(('01_fixado_1_capa', 'p', f'''{frame("Cozinha estratégica", "01 / 03")}
<div class="img" style="left:80px;right:80px;top:150px;height:700px"><img src="{P}feira-sorrindo_ed.jpg" style="object-position:62% 24%"></div>
<div class="S" style="position:absolute;left:80px;right:80px;top:910px;font-size:92px">Prazer, sou<br>a Mylena.</div>
<div class="sup" style="position:absolute;left:80px;right:220px;top:1130px">Ajudo restaurantes a lucrar com o que já vendem.</div>'''))

pil = [('Custo certo', 'Quanto custa cada prato e quanto sobra.'),
       ('Cardápio que vende', 'Preço e destaque para o que dá lucro.'),
       ('Marca que atrai', 'Imagem e Instagram que trazem cliente.')]
arts.append(('01_fixado_2_o_que_faco', 'p', f'''{frame("O que eu faço", "02 / 03")}
<div class="S" style="position:absolute;left:80px;top:180px;font-size:84px">Três frentes,<br>um resultado: lucro.</div>
<div style="position:absolute;left:80px;right:80px;top:520px">''' + ''.join(
    f'''<div class="rule"></div><div style="display:grid;grid-template-columns:140px 1fr;padding:44px 0">
<div class="S" style="font-size:64px;color:{G}">0{i}</div><div><div class="S" style="font-size:56px">{t}</div>
<div class="sup" style="font-size:28px;opacity:.7;margin-top:10px">{d}</div></div></div>''' for i, (t, d) in enumerate(pil, 1)) + '<div class="rule"></div></div>'))

arts.append(('01_fixado_3_diagnostico', 'p dark', f'''{frame("Para começar", "03 / 03")}
<div class="S" style="position:absolute;left:72px;top:240px;font-size:300px;letter-spacing:-8px;line-height:.9">30<span style="font-size:120px;letter-spacing:-2px;color:{G}"> min</span></div>
<div class="S" style="position:absolute;left:80px;right:80px;top:640px;font-size:76px">Diagnóstico de lucro gratuito.</div>
<div class="sup" style="position:absolute;left:80px;right:200px;top:860px;opacity:.8">Calculamos juntos o custo e a margem de 1 produto do seu cardápio.</div>
<div style="position:absolute;left:80px;right:80px;top:1110px" class="rule"></div>
<div style="position:absolute;left:80px;top:1140px;font-size:26px;font-weight:500">Agende pelo link na bio</div>'''))

# b) Carrossel
arts.append(('02_carrossel_1_capa', 'p', f'''{frame("Lucro em restaurante", "01 / 05")}
<div class="S" style="position:absolute;left:60px;top:150px;font-size:620px;letter-spacing:-20px;line-height:.85;color:{G}">3</div>
<div class="S" style="position:absolute;left:80px;right:80px;top:760px;font-size:84px">erros que fazem o restaurante vender e não lucrar.</div>
<div class="cnt" style="top:auto;bottom:72px">deslize</div>'''))
erros = [('Copiar o preço do concorrente.', 'Sem saber o custo do prato, o preço do vizinho pode dar prejuízo a cada venda.', 'Calcule o custo de cada item antes de definir o preço.'),
         ('Servir sem porção padrão.', 'Cada pessoa da equipe serve de um jeito, e o lucro muda a cada prato.', 'Defina a quantidade de cada ingrediente numa ficha de custo.'),
         ('Olhar só o faturamento.', 'Caixa cheio não é lucro. O que importa é quanto sobra no fim do mês.', 'Acompanhe o CMV todo mês, não só o caixa.')]
for i, (t, d, f) in enumerate(erros, 1):
    arts.append((f'02_carrossel_{i + 1}_erro{i}', 'p', f'''{frame(f"Erro {i} de 3", f"0{i + 1} / 05")}
<div class="S" style="position:absolute;left:80px;top:170px;font-size:150px;color:{G};letter-spacing:-4px">0{i}</div>
<div class="S" style="position:absolute;left:80px;right:80px;top:380px;font-size:82px">{t}</div>
<div class="sup" style="position:absolute;left:80px;right:180px;top:640px;opacity:.75">{d}</div>
<div style="position:absolute;left:80px;right:80px;top:930px" class="rule"></div>
<div style="position:absolute;left:80px;top:970px;font-size:20px;font-weight:600;letter-spacing:4px;text-transform:uppercase;color:{G}">Como resolver</div>
<div class="S" style="position:absolute;left:80px;right:160px;top:1020px;font-size:46px;letter-spacing:-.5px">{f}</div>'''))
arts.append(('02_carrossel_5_cta', 'p dark', f'''{frame("Próximo passo", "05 / 05")}
<div class="S" style="position:absolute;left:80px;right:80px;top:330px;font-size:110px">Comente <span style="color:{G}">CMV</span>.</div>
<div class="sup" style="position:absolute;left:80px;right:200px;top:520px;opacity:.8">Eu te mando o passo a passo para calcular o CMV de 1 produto do seu cardápio.</div>
<div style="position:absolute;left:80px;right:80px;top:1110px" class="rule"></div>
<div style="position:absolute;left:80px;top:1140px;font-size:26px;font-weight:500">Salve para revisar com a sua equipe</div>'''))

# c) Bastidor
arts.append(('03_bastidor_feira', 'p', f'''{frame("Bastidores · Recife", "")}
<div class="img" style="left:80px;right:80px;top:150px;height:760px"><img src="{P}close-sorrindo_ed.jpg" style="object-position:50% 28%"></div>
<div class="S" style="position:absolute;left:80px;right:80px;top:970px;font-size:72px">O que eu vi na feira de food service.</div>
<div class="sup" style="position:absolute;left:80px;right:200px;top:1150px;font-size:28px;opacity:.7">3 aprendizados para o seu restaurante, na legenda.</div>'''))

# d) Capa de Reels (área do grid: y 285–1635)
arts.append(('04_capa_reels', 'st', f'''<div class="img" style="left:0;right:0;top:0;height:1010px"><img src="{P}selfie-preta.jpg" style="object-position:50% 22%"></div>
<div style="position:absolute;left:80px;top:1060px;font-size:20px;font-weight:600;letter-spacing:4px;text-transform:uppercase;opacity:.55">Cozinha estratégica</div>
<div class="S" style="position:absolute;left:80px;right:80px;top:1120px;font-size:96px">Seu restaurante vende muito e lucra <span style="color:{G}">pouco?</span></div>
<div class="sig" style="bottom:330px">{AT}</div>'''))

html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{CSS}</head><body>' + ''.join(
    f'<div class="a {c}" id="{n}">{b}</div>' for n, c, b in arts) + '</body></html>'
open('artes_ig.html', 'w').write(html)
open('artes_ig.list', 'w').write('\n'.join(n for n, _, _ in arts))
