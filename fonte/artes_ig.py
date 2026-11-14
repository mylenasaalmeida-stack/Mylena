"""Artes do Instagram v2 · Mylena | Cozinha Estratégica (PNG 1080 px) · conceito: o restaurante como linguagem."""
INK, G, LIME, OW, PAPER = '#0c0e0d', '#2f8a4e', '#b6e07a', '#f3efe6', '#fbf8f1'
AT = '@mylena.cozinhaestrategica'
P = 'img/mylena/'

GRAIN = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/></filter>"
         "<rect width='100%25' height='100%25' filter='url(%23n)' opacity='.55'/></svg>\")")

ICON = (f'<svg width="{{s}}" height="{{s}}" viewBox="0 0 64 64"><circle cx="32" cy="32" r="29" fill="none" stroke="{{c}}" stroke-width="3"/>'
        f'<circle cx="32" cy="32" r="19" fill="none" stroke="{{c}}" stroke-width="2" opacity=".55"/>'
        f'<path d="M20 40 L29 31 L35 36 L45 24" fill="none" stroke="{{a}}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<path d="M38 24 H45 V31" fill="none" stroke="{{a}}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def icon(s=56, c='#fff', a=LIME):
    return ICON.format(s=s, c=c, a=a)


CSS = f'''<style>
@import url('fonts.css');@import url('fonts2.css');
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#777;font-family:'Poppins',sans-serif;-webkit-font-smoothing:antialiased}}
.a{{position:relative;overflow:hidden;margin:20px;display:block}}
.sq{{width:1080px;height:1080px}}.p{{width:1080px;height:1350px}}.st{{width:1080px;height:1920px}}
.ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.grain:after{{content:'';position:absolute;inset:0;background:{GRAIN};mix-blend-mode:overlay;opacity:.35;pointer-events:none}}
.C{{font-family:'Roboto Condensed';font-weight:800;text-transform:uppercase;letter-spacing:-1px;line-height:.86}}
.S{{font-family:'Playfair Display';font-style:italic;font-weight:800;text-transform:none;letter-spacing:-1px}}
.Hn{{font-family:'Caveat';font-weight:700}}
.k{{font-size:21px;font-weight:600;letter-spacing:7px;text-transform:uppercase}}
.top{{position:absolute;left:70px;right:70px;top:56px;display:flex;justify-content:space-between;align-items:center;font-size:21px;font-weight:600;letter-spacing:5px;text-transform:uppercase}}
.bot{{position:absolute;left:70px;right:70px;bottom:52px;display:flex;justify-content:space-between;align-items:center;font-size:23px;font-weight:500}}
.hl{{background:linear-gradient(transparent 58%,{LIME} 58%,{LIME} 92%,transparent 92%);padding:0 6px}}
.mono{{font-family:'Courier New',monospace;font-weight:700}}
</style>'''


def top(left, right, color='#fff'):
    return f'<div class="top" style="color:{color}"><span style="display:flex;align-items:center;gap:16px">{icon(44, color)}{left}</span><span>{right}</span></div>'


def bot(right='', color='#fff'):
    return f'<div class="bot" style="color:{color}"><span>{AT}</span><span>{right}</span></div>'


arts = []

# 00 · Foto de perfil
arts.append(('00_foto_perfil', 'sq', f'''<img class="ph" src="{P}close-sorrindo_ed.jpg" style="object-position:53% 18%;transform:scale(1.55);transform-origin:53% 22%">'''))

# 01 · POST FIXADO · conceito revista + cardápio + reserva
arts.append(('01_fixado_1_capa', 'p grain', f'''<img class="ph" src="{P}feira-sorrindo_ed.jpg" style="object-position:60% 22%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,14,13,.75) 0,rgba(12,14,13,0) 26%,rgba(12,14,13,0) 52%,rgba(12,14,13,.96) 84%)"></div>
<div style="position:absolute;left:62px;right:62px;top:48px;color:#fff;display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid rgba(255,255,255,.5);padding-bottom:18px">
<div class="C" style="font-size:86px;letter-spacing:0">Cozinha<br><span style="color:{LIME}">estratégica</span></div>
<div style="text-align:right;font-size:20px;letter-spacing:4px;font-weight:600;line-height:1.7">EDIÇÃO Nº 01<br>RECIFE · PE</div></div>
<div style="position:absolute;left:62px;top:300px;color:#fff;width:300px">
<div class="Hn" style="font-size:46px;color:{LIME};transform:rotate(-4deg)">nesta edição ↓</div>
<div style="font-size:24px;line-height:1.5;margin-top:16px;font-weight:500">Custo certo<br>Cardápio que vende<br>Marca que atrai</div></div>
<div style="position:absolute;left:62px;right:62px;bottom:120px;color:#fff">
<div class="S" style="font-size:150px;line-height:.9">Prazer,</div>
<div class="C" style="font-size:150px;margin-top:-6px">sou a <span style="color:{LIME}">Mylena</span></div>
<div style="font-size:30px;margin-top:22px;max-width:760px;color:#e7ebe5;line-height:1.4">e ajudo restaurantes, bares e delivery a <b style="color:#fff">lucrar com o que já vendem.</b></div></div>
{bot("arraste →")}'''))

menu = [('Custo certo', 'quanto custa cada prato e quanto sobra de verdade'),
        ('Cardápio que vende', 'organização, preço e destaque para o que dá lucro'),
        ('Marca que atrai', 'identidade visual e Instagram que trazem cliente')]
arts.append(('01_fixado_2_cardapio', 'p grain', f'''<div style="position:absolute;inset:0;background:{PAPER}"></div>
<div style="position:absolute;inset:40px;border:3px solid {INK}"></div><div style="position:absolute;inset:52px;border:1px solid {INK}"></div>
<div style="position:absolute;left:110px;right:110px;top:120px;color:{INK};text-align:center">
{icon(84, INK, G)}
<div class="k" style="margin-top:22px;color:{G}">Cozinha estratégica</div>
<div class="S" style="font-size:120px;line-height:1;margin-top:10px">Menu</div>
<div class="C" style="font-size:60px;letter-spacing:6px">da casa</div>
<div style="width:120px;height:3px;background:{INK};margin:36px auto 30px"></div></div>
<div style="position:absolute;left:120px;right:120px;top:560px;color:{INK}">''' + ''.join(
    f'''<div style="margin-bottom:58px"><div style="display:flex;align-items:baseline;gap:18px"><span class="C" style="font-size:58px;letter-spacing:0">{t}</span>
<span style="flex:1;border-bottom:4px dotted {INK};transform:translateY(-14px)"></span><span class="S" style="font-size:52px;color:{G}">+ lucro</span></div>
<div style="font-size:28px;color:#4a4f4b;margin-top:10px;font-style:italic">{d}</div></div>''' for t, d in menu) + f'''</div>
<div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;color:{INK};font-size:22px;letter-spacing:5px;font-weight:600">SERVIDO EM RECIFE E REGIÃO METROPOLITANA</div>'''))

arts.append(('01_fixado_3_reserva', 'p grain', f'''<div style="position:absolute;inset:0;background:{G}"></div>
<div class="Hn" style="position:absolute;left:80px;top:80px;font-size:64px;color:#fff;transform:rotate(-3deg)">primeira vez aqui?</div>
<div style="position:absolute;left:80px;right:80px;top:210px;background:{PAPER};border-radius:6px;box-shadow:0 30px 60px rgba(0,0,0,.35);color:{INK};transform:rotate(1.2deg)">
<div style="padding:60px 64px 40px">
<div style="display:flex;justify-content:space-between;align-items:center">{icon(60, INK, G)}<span class="k" style="color:{G};font-size:20px">Reserva confirmada</span></div>
<div class="C" style="font-size:118px;margin-top:34px">Diagnóstico<br>de <span class="hl">lucro</span></div>
<div style="font-size:30px;color:#4a4f4b;margin-top:18px">Em 30 minutos, calculamos juntos o custo e a margem de 1 produto do seu cardápio.</div></div>
<div style="border-top:4px dashed #c9c3b6;margin:0 30px"></div>
<div style="padding:34px 64px 50px;display:grid;grid-template-columns:1fr 1fr;gap:26px 40px;font-size:24px">''' + ''.join(
    f'<div><div class="k" style="font-size:17px;color:#8a8f8b">{k}</div><div class="mono" style="font-size:34px;margin-top:6px">{v}</div></div>' for k, v in [
        ('Mesa para', 'Seu restaurante'), ('Duração', '30 min'), ('Valor', 'R$ 0,00'), ('Onde', 'WhatsApp')]) + f'''</div></div>
<div style="position:absolute;left:80px;right:80px;bottom:120px;color:#fff;display:flex;align-items:center;gap:22px">
<div class="C" style="font-size:52px">Link na bio</div><div class="Hn" style="font-size:54px;color:{LIME}">→ é só chamar</div></div>
{bot("", "#fff")}'''))

# 02 · CARROSSEL · conceito comanda com carimbo
arts.append(('02_carrossel_1_capa', 'p grain', f'''<img class="ph" src="{P}feira-seria_ed.jpg" style="object-position:58% 20%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,14,13,.0) 30%,rgba(12,14,13,.97) 70%)"></div>
{top("Cozinha estratégica", "01 / 05")}
<div style="position:absolute;left:70px;right:70px;bottom:130px;color:#fff">
<div style="display:flex;gap:20px;align-items:center;margin-bottom:26px">
<span class="C" style="font-size:64px;background:#fff;color:{INK};padding:6px 18px 2px">Vende muito.</span></div>
<div style="display:flex;gap:20px;align-items:center;margin-bottom:34px">
<span class="C" style="font-size:64px;color:#fff;padding:6px 18px 2px;border:3px solid #fff;text-decoration:line-through;text-decoration-color:{LIME};text-decoration-thickness:8px">Lucra muito.</span></div>
<div class="C" style="font-size:118px"><span style="color:{LIME}">3 erros</span> que<br>explicam isso</div>
<div class="Hn" style="font-size:46px;color:{LIME};margin-top:18px">o nº 3 é o mais comum →</div></div>
{bot("")}'''))

erros = [('Preço copiado do concorrente', [('Custo do prato', 'não calculado'), ('Preço de venda', 'igual ao do vizinho'), ('Margem', '???')], 'Calcule o custo de cada item antes de definir o preço.'),
         ('Porção sem padrão', [('Pizza A', 'mais queijo'), ('Pizza B', 'menos queijo'), ('Custo por pizza', 'muda todo dia')], 'Ficha de custo com a quantidade de cada ingrediente.'),
         ('Olhar só o faturamento', [('Caixa do mês', 'cheio'), ('CMV', 'não acompanhado'), ('Lucro', '???')], 'Acompanhe o CMV todo mês, não só o caixa.')]
for i, (t, linhas, sol) in enumerate(erros, 1):
    rows = ''.join(f'<div style="display:flex;justify-content:space-between;padding:16px 0;border-bottom:2px dotted #cfc8ba"><span>{a}</span><span>{b}</span></div>' for a, b in linhas)
    arts.append((f'02_carrossel_{i + 1}_erro{i}', 'p grain', f'''<div style="position:absolute;inset:0;background:{INK}"></div>
{top("Erro " + str(i) + " de 3", f"0{i + 1} / 05")}
<div class="C" style="position:absolute;right:40px;top:110px;font-size:420px;color:#1b201d;line-height:1">{i}</div>
<div style="position:absolute;left:90px;right:90px;top:180px;background:{PAPER};color:{INK};padding:54px 56px 60px;transform:rotate(-1.5deg);box-shadow:0 30px 60px rgba(0,0,0,.6)">
<div style="display:flex;justify-content:space-between" class="mono"><span style="font-size:26px">COMANDA Nº 00{i}</span><span style="font-size:26px">MESA: SEU RESTAURANTE</span></div>
<div style="border-top:3px solid {INK};margin:22px 0 28px"></div>
<div class="C" style="font-size:84px;line-height:.92">{t}</div>
<div class="mono" style="font-size:30px;margin-top:30px">{rows}</div>
<div class="mono" style="display:flex;justify-content:space-between;font-size:38px;margin-top:26px"><span>LUCRO</span><span style="color:#c8361f">EM RISCO</span></div>
<div style="position:absolute;left:0;right:0;bottom:-16px;height:32px;background:radial-gradient(circle at 16px 0,{INK} 15px,transparent 16px) 0 0/32px 32px repeat-x"></div></div>
<div style="position:absolute;left:110px;right:110px;bottom:120px;color:#fff;transform:rotate(-2deg)">
<div style="border:5px solid {LIME};border-radius:10px;padding:26px 34px;display:inline-block">
<div class="k" style="color:{LIME};font-size:20px">Como resolver</div>
<div class="C" style="font-size:52px;margin-top:10px;color:#fff">{sol}</div></div></div>
{bot("")}'''))

arts.append(('02_carrossel_5_cta', 'p grain', f'''<div style="position:absolute;inset:0;background:{G}"></div>
{top("Cozinha estratégica", "05 / 05")}
<div style="position:absolute;left:80px;right:80px;top:200px;color:#fff">
<div class="Hn" style="font-size:60px;color:{LIME};transform:rotate(-3deg)">se identificou?</div>
<div class="C" style="font-size:150px;margin-top:20px">Comente</div>
<div style="display:flex;align-items:center;gap:26px;margin-top:20px">
<div style="background:#fff;border-radius:60px 60px 60px 8px;padding:24px 56px 18px;box-shadow:0 20px 40px rgba(0,0,0,.25)"><span class="C" style="font-size:150px;color:{INK}">CMV</span></div></div>
<div style="font-size:36px;line-height:1.45;margin-top:56px;max-width:820px">e eu te mando o <b>passo a passo de 1 página</b> para calcular o CMV de um produto do seu cardápio.</div>
<div style="display:flex;gap:22px;margin-top:60px;font-size:26px;font-weight:600">
<span style="border:2px solid #fff;border-radius:40px;padding:12px 26px">🔖 Salve</span><span style="border:2px solid #fff;border-radius:40px;padding:12px 26px">↗ Mande para o sócio</span></div></div>
{bot("")}'''))

# 03 · BASTIDOR · polaroid + anotação à mão
arts.append(('03_bastidor_feira', 'p grain', f'''<div style="position:absolute;inset:0;background:#1a1e1b"></div>
<div style="position:absolute;inset:0;background:radial-gradient(circle at 30% 20%,#25302a 0,{INK} 70%)"></div>
{top("Bastidores", "Recife · PE")}
<div style="position:absolute;left:170px;top:150px;width:740px;background:{PAPER};padding:28px 28px 110px;transform:rotate(-3deg);box-shadow:0 40px 70px rgba(0,0,0,.6)">
<div style="height:620px;overflow:hidden"><img src="{P}close-sorrindo_ed.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 30%"></div>
<div class="Hn" style="position:absolute;left:36px;right:36px;bottom:28px;font-size:52px;color:{INK};white-space:nowrap">feira de food service ✔</div></div>
<div style="position:absolute;left:480px;top:122px;width:150px;height:46px;background:rgba(182,224,122,.85);transform:rotate(4deg)"></div>
<div style="position:absolute;left:70px;right:70px;bottom:120px;color:#fff">
<div class="C" style="font-size:76px">O que eu vi na feira</div><div class="C" style="font-size:76px;margin-top:6px"><span class="S" style="color:{LIME};font-size:80px">e o que</span> vale para</div><div class="C" style="font-size:76px;margin-top:6px">o seu restaurante</div></div>
{bot("3 aprendizados →")}'''))

# 04 · CAPA DE REELS
arts.append(('04_capa_reels', 'st grain', f'''<img class="ph" src="{P}selfie-preta_ed.jpg" style="object-position:50% 25%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,14,13,0) 38%,rgba(12,14,13,.95) 70%)"></div>
<div style="position:absolute;left:70px;top:100px;color:#fff;display:flex;align-items:center;gap:16px">{icon(54)}<span class="k" style="font-size:22px">Cozinha estratégica</span></div>
<div style="position:absolute;left:70px;right:70px;bottom:300px;color:#fff">
<div class="Hn" style="font-size:66px;color:{LIME};transform:rotate(-3deg)">seu restaurante...</div>
<div style="margin-top:24px"><span class="C" style="font-size:128px;background:#fff;color:{INK};padding:14px 24px 4px;display:inline-block;white-space:nowrap">vende muito</span></div>
<div style="margin-top:16px"><span class="C" style="font-size:128px;background:{G};color:#fff;padding:14px 24px 4px;display:inline-block;white-space:nowrap">e lucra pouco?</span></div>
<div style="font-size:36px;margin-top:40px;color:#e6e9e4">Os 3 erros que fazem o dinheiro escapar.</div></div>
<div style="position:absolute;left:70px;bottom:130px;color:#fff;font-size:28px">{AT}</div>'''))

html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">{CSS}</head><body>' + ''.join(
    f'<div class="a {c}" id="{n}">{b}</div>' for n, c, b in arts) + '</body></html>'
open('artes_ig.html', 'w').write(html)
open('artes_ig.list', 'w').write('\n'.join(n for n, _, _ in arts))
