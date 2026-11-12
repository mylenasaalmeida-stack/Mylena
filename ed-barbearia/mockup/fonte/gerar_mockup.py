# Mockup do perfil completo da ED no Instagram + capas de Reels (R1 a R7) no padrão.
# Gerar: python3 gerar_mockup.py && node render_mockup.js
Y, K, W = '#FFC629', '#111111', '#F5F3EE'
ED = '../../'  # raiz de ed-barbearia
FONTS = f'''
@font-face{{font-family:Anton;src:url('{ED}marca/fonte/fonts/Anton.ttf')}}
@font-face{{font-family:Inter;font-weight:400;src:url('{ED}marca/fonte/fonts/Inter-400.ttf')}}
@font-face{{font-family:Inter;font-weight:600;src:url('{ED}marca/fonte/fonts/Inter-600.ttf')}}
@font-face{{font-family:Inter;font-weight:700;src:url('{ED}marca/fonte/fonts/Inter-700.ttf')}}
@font-face{{font-family:Poppins;font-weight:600;src:url('{ED}../fonte/fonts/Poppins-600.woff2')}}
@font-face{{font-family:Poppins;font-weight:700;src:url('{ED}../fonte/fonts/Poppins-700.woff2')}}
'''

# ---------------- capas de Reels (1080x1920; o essencial fica no miolo 3:4 que a grade mostra) ----------------
REELS = [
    ('R1', 'Degradê<br>sem marca', W, K, None),
    ('R2', 'Chegou<br>pedindo<br>socorro', W, K, None),
    ('R3', 'Qual corte<br>pro teu<br>rosto?', K, Y, 'ed-retrato'),
    ('R4', 'Navalha<br>parte 2', Y, K, None),
    ('R5', 'Sem<br>fila.', Y, K, None),
    ('R6', 'O ritual<br>da barba', Y, K, None),
    ('R7', 'Pai<br>e filho', W, K, None),
]
CAPA_CSS = FONTS + f'''
*{{margin:0;padding:0;box-sizing:border-box}}
.c{{width:1080px;height:1920px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:0 100px}}
.c .t{{font-family:Anton;text-transform:uppercase;font-size:200px;line-height:.92;position:relative;z-index:2}}
.c .l{{font-family:Poppins;font-weight:700;font-size:34px;letter-spacing:.24em;position:relative;z-index:2;margin-bottom:30px}}
.c .nv{{position:relative;z-index:2;margin-top:50px}}
'''


def navalha(cor, fundo, w):
    return f'''<svg viewBox="-100 -20 200 40" style="width:{w}px;display:block"><g transform="scale(1.15)">
<rect x="-92" y="-8" width="96" height="16" rx="8" fill="{cor}"/><circle cx="-78" cy="0" r="2.6" fill="{fundo}"/><circle cx="-12" cy="0" r="2.6" fill="{fundo}"/>
<path d="M2 -9 L74 -9 Q84 -9 84 1 Q84 13 70 15 Q40 17 6 9 Z" fill="{cor}"/><circle cx="2" cy="0" r="6" fill="{cor}" stroke="{fundo}" stroke-width="2.5"/></g></svg>'''


for cod, tit, bg, fg, foto in REELS:
    ph = ''
    if foto:
        ph = (f'<img src="{ED}fixados/fonte/img/{foto}.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:62% 0">'
              f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.1) 20%,{K} 72%)"></div>')
    just = 'justify-content:flex-end;padding-bottom:330px' if foto else ''
    acc = Y if bg != Y else K
    html = (f'<section class="c" style="background:{bg};color:{fg};{just}">{ph}<div class="l" style="color:{acc if bg == K else fg}">ED BARBEARIA</div>'
            f'<div class="t">{tit}</div><div class="nv">{navalha(fg if bg != K else Y, bg, 420)}</div></section>')
    open(f'capa-reels-{cod}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CAPA_CSS}</style></head><body>{html}</body></html>')

# ---------------- mockup ----------------
OLD = f'{ED}fonte/img/'          # capas de destaque antigas (recortadas 240 px)
NEW = f'{ED}stories/destaques/'  # capas novas 1080x1920
DESTAQUES = [('Agendar', OLD + 'destaque-agendar.jpg', 0), ('Onde', OLD + 'destaque-onde.jpg', 0), ('Preços', OLD + 'destaque-precos.jpg', 0),
             ('Cortes', OLD + 'destaque-cortes.jpg', 0), ('Kids', NEW + 'destaque-kids.png', 1), ('Salão', NEW + 'destaque-salao-feminino.png', 1),
             ('Ação social', NEW + 'destaque-acao-social.png', 1), ('Trajetória', NEW + 'destaque-trajetoria.png', 1), ('Estúdio', NEW + 'destaque-estudio.png', 1),
             ('Construção', NEW + 'destaque-construcao.png', 1), ('Curso', OLD + 'destaque-curso.jpg', 0), ('Vagas', NEW + 'destaque-vagas.png', 1)]

GRADE = [  # (imagem, tipo) na ordem da grade: fixados, depois o mais recente primeiro
    (f'{ED}fixados/fixado-1-agenda.png', 'fix'), (f'{ED}fixados/fixado-2-senta.png', 'fix'), (f'{ED}fixados/fixado-3-volta.png', 'fix'),
    (f'{ED}feed/feed-estamos-contratando.png', ''), ('capa-reels-R7.png', 'reel'), ('capa-reels-R6.png', 'reel'),
    (f'{ED}fonte/img/feed-04a-cortes-capa.jpg', 'car'), ('capa-reels-R5.png', 'reel'), (f'{ED}fonte/img/feed-03a-ed-capa.jpg', 'car'),
    ('capa-reels-R4.png', 'reel'), ('capa-reels-R3.png', 'reel'), ('capa-reels-R2.png', 'reel'),
    (f'{ED}fonte/img/feed-02a-agendar-capa.jpg', 'car'), ('capa-reels-R1.png', 'reel'), (f'{ED}fonte/img/feed-01-campanha.jpg', ''),
]

IC = {
    'fix': '<svg viewBox="0 0 24 24" fill="#fff"><path d="M16 3H8v2l1 1v5l-3 3v2h5v5l1 1 1-1v-5h5v-2l-3-3V6l1-1z"/></svg>',
    'reel': '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M3 8h18M8 3l3 5M14 3l3 5" /><path d="M10 11.5v5l4-2.5z" fill="#fff"/></svg>',
    'car': '<svg viewBox="0 0 24 24" fill="#fff"><rect x="7" y="3" width="14" height="14" rx="2"/><path d="M4 7v12a2 2 0 0 0 2 2h12" fill="none" stroke="#fff" stroke-width="2"/></svg>',
}

CSS = FONTS + f'''
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#e9e6df;font-family:Inter,sans-serif;padding:50px;display:flex;gap:50px;align-items:flex-start;width:max-content}}
.phone{{width:430px;background:#fff;border-radius:44px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.25);border:10px solid #111;color:#000}}
.sb{{display:flex;justify-content:space-between;align-items:center;padding:14px 26px 6px;font-weight:600;font-size:15px}}
.top{{display:flex;justify-content:space-between;align-items:center;padding:6px 16px 10px}}
.top b{{font-size:21px;font-weight:700;display:flex;align-items:center;gap:4px}}
.top .ic{{display:flex;gap:20px}} .top svg{{width:26px;height:26px}}
.hd{{display:flex;align-items:center;gap:22px;padding:4px 16px 10px}}
.av{{width:92px;height:92px;border-radius:50%;padding:3px;background:conic-gradient(#f9ce34,#ee2a7b,#6228d7,#f9ce34);flex:none}}
.av div{{width:100%;height:100%;border-radius:50%;border:3px solid #fff;background:#fff url('{ED}stories/fonte/img/logo-antigo.png') center/88% no-repeat;box-shadow:inset 0 0 0 3px #111}}
.st{{display:flex;flex:1;justify-content:space-around;text-align:center;font-size:14px}}
.st b{{display:block;font-size:17px;font-weight:700}}
.bio{{padding:0 16px;font-size:14px;line-height:1.38}}
.bio .n{{font-weight:600}} .bio .cat{{color:#737373}} .bio a{{color:#00376b;font-weight:600;text-decoration:none}}
.btn{{display:flex;gap:6px;padding:12px 16px 4px}}
.btn div{{flex:1;background:#efefef;border-radius:9px;text-align:center;font-weight:600;font-size:14px;padding:8px 0}}
.btn div.az{{background:#0095f6;color:#fff}}
.hl{{display:flex;gap:14px;padding:14px 16px 12px;overflow:hidden}}
.hl div{{text-align:center;font-size:12px;width:66px;flex:none}}
.hl i{{display:block;width:66px;height:66px;border-radius:50%;border:1px solid #dbdbdb;padding:3px;margin-bottom:5px}}
.hl i span{{display:block;width:100%;height:100%;border-radius:50%;background-position:center;background-repeat:no-repeat}}
.tabs{{display:flex;border-top:1px solid #dbdbdb}}
.tabs div{{flex:1;display:flex;justify-content:center;padding:10px 0}}
.tabs div.on{{border-bottom:1.5px solid #000}} .tabs svg{{width:24px;height:24px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px}}
.grid div{{aspect-ratio:3/4;background-size:cover;background-position:center;position:relative}}
.grid svg{{position:absolute;top:7px;right:7px;width:18px;height:18px;filter:drop-shadow(0 0 2px rgba(0,0,0,.6))}}
.nav{{display:flex;justify-content:space-around;padding:12px 0 26px;border-top:1px solid #efefef}} .nav svg{{width:26px;height:26px}}
.notes{{width:420px;font-family:Poppins,sans-serif;color:#111}}
.notes h1{{font-family:Anton;font-weight:400;font-size:58px;line-height:1;text-transform:uppercase;margin:6px 0 14px}}
.notes .k{{font-size:11px;letter-spacing:.22em;font-weight:700;text-transform:uppercase;color:#7a6a20;margin:22px 0 8px}}
.notes .card{{background:#fff;border-radius:16px;padding:16px 18px;font-size:13.5px;line-height:1.45;margin-bottom:10px}}
.notes ol{{padding-left:20px}} .notes li{{margin-bottom:3px}}
.notes .tag{{display:inline-block;background:{Y};font-weight:700;font-size:11px;letter-spacing:.14em;padding:5px 10px;border-radius:20px}}
'''


def hl_html():
    out = ''
    for nome, src, novo in DESTAQUES:
        size = '138% auto' if novo else 'cover'
        out += f'<div><i><span style="background-image:url(\'{src}\');background-size:{size}"></span></i>{nome}</div>'
    return out


grid = ''.join(f'<div style="background-image:url(\'{src}\')">{IC.get(t, "")}</div>' for src, t in GRADE)

ICON = lambda d, sw=2, fill='none': f'<svg viewBox="0 0 24 24" fill="{fill}" stroke="#000" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'

phone = f'''<div class="phone">
<div class="sb"><span>9:41</span><span>●●● ▲ ▮</span></div>
<div class="top"><b>edbarbearia <span style="font-size:14px">⌄</span></b><div class="ic">{ICON('<rect x="3" y="3" width="18" height="18" rx="5"/><path d="M12 8v8M8 12h8"/>')}{ICON('<path d="M4 6h16M4 12h16M4 18h16"/>')}</div></div>
<div class="hd"><div class="av"><div></div></div>
<div class="st"><div><b>308</b>posts</div><div><b>3.199</b>seguidores</div><div><b>812</b>seguindo</div></div></div>
<div class="bio"><div class="n">ED Barbearia | Casa Amarela, Recife</div><div class="cat">Barbearia</div>
✂️ Degradê, barba, kids e salão feminino<br>🗓️ Seg a sáb, 9h às 19h<br>🎟️ 50% no 1º corte de seg a qua, pelo app<br>👇 Agende pelo link<br>
<a>🔗 Agendamento da ED</a><br><span class="cat">Rua Paula Batista, 604, Recife</span></div>
<div class="btn"><div class="az">Seguir</div><div>Mensagem</div><div>Reservar</div></div>
<div class="hl">{hl_html()}</div>
<div class="tabs"><div class="on">{ICON('<rect x="3" y="3" width="18" height="18"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/>', 1.6)}</div>
<div>{ICON('<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M10 9.5v5l4-2.5z"/>', 1.6)}</div><div>{ICON('<path d="M4 4h16v16H4z"/><circle cx="12" cy="10" r="3"/><path d="M7 20c1-3 3-4 5-4s4 1 5 4"/>', 1.6)}</div></div>
<div class="grid">{grid}</div>
<div class="nav">{ICON('<path d="M3 10l9-7 9 7v10a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>')}{ICON('<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>')}{ICON('<rect x="3" y="3" width="18" height="18" rx="5"/><path d="M12 8v8M8 12h8"/>')}{ICON('<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M10 9.5v5l4-2.5z"/>')}<div style="width:28px;height:28px;border-radius:50%;background:#fff url('{ED}stories/fonte/img/logo-antigo.png') center/cover;border:2px solid #000"></div></div>
</div>'''

notes = f'''<div class="notes"><span class="tag">MOCKUP · PERFIL COMPLETO</span>
<h1>O perfil da ED <span style="color:#b8860b">no fim de novembro.</span></h1>
<p style="font-size:14px;line-height:1.5">Como o perfil fica com tudo no ar: bio nova, destaques no padrão, os 3 fixados e o feed do mês.</p>
<div class="k">Topo</div><div class="card">Nome com o bairro (aparece na busca), bio de 4 linhas, link do agendamento, endereço e o botão <b>Reservar</b> ligado ao app, se o app tiver essa integração.</div>
<div class="k">Destaques, nessa ordem</div><div class="card"><ol>{''.join(f'<li>{n}</li>' for n, _, _ in DESTAQUES)}</ol>
<p style="margin-top:6px;color:#666">No celular aparecem os 5 primeiros. Os de venda vêm antes.</p></div>
<div class="k">Grade</div><div class="card"><b>Linha 1:</b> os 3 fixados (Agenda, Senta, Volta).<br><b>Depois:</b> os posts do mês, do mais recente pro mais antigo. Preto, amarelo e branco se alternam pra a grade não ficar pesada.<br><br>
<b>Reels:</b> as capas são ilustrativas, com o título de cada Reels. Na postagem, a capa fica igual, só que com o melhor frame do vídeo no fundo.</div>
<div class="k">Números</div><div class="card" style="color:#666">Seguidores e seguindo são os de hoje. Posts = 296 + os 12 de novembro. É ilustração, não meta.</div>
</div>'''

open('mockup.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{phone}{notes}</body></html>')
print('ok')
