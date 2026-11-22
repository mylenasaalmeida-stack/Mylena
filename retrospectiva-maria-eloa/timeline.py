"""Roteiro do vídeo: cenas em ordem, com duração (s), transição de entrada e animação."""

ROSA = (255, 105, 160)
LILAS = (170, 120, 230)
AZUL = (90, 160, 240)
DOURADO = (240, 180, 70)
VERDE = (80, 190, 150)
CORAL = (255, 130, 100)

def P(f, cap=None, dur=2.0, trans='fade', entry='pop', rot=None, accent=ROSA):
    return dict(type='photo', file=f, cap=cap, dur=dur, trans=trans, entry=entry, rot=rot, accent=accent)

def T(chap, title, sub, colors, dur=3.0, trans='circle', deco='hearts', section=None):
    return dict(type='title', chap=chap, title=title, sub=sub, colors=colors, dur=dur, trans=trans, deco=deco, section=section)

def TRIO(files, dur=4.0, trans='slide', accent=ROSA, cap=None):
    return dict(type='trio', files=files, dur=dur, trans=trans, accent=accent, cap=cap)

def quick(files, accent, trans='flash'):
    ent = ['pop', 'left', 'right', 'drop']
    return [P(f, dur=1.0, trans=trans, entry=ent[i % 4], accent=accent) for i, f in enumerate(files)]

SCENES = []
A = SCENES.append

# ---------------- ABERTURA (seção intro: 6 s exatos) ----------------
A(dict(type='countdown', dur=6.0, trans='cut', section='intro'))
A(dict(type='opening', dur=6.0, trans='flash', section='popA'))

# ---------------- CAP 1: onde tudo começou ----------------
A(T('Capítulo 1', 'Onde tudo começou', 'dois jovens, um olhar... e muita história pela frente',
    [(255, 182, 193), (186, 140, 255)], trans='heart'))
A(P('u_luana.jpg', 'Lá no comecinho...', entry='drop', accent=AZUL))
A(P('u_black.jpg', 'Pose de casal', trans='slide', entry='left', accent=LILAS))
A(P('u_selfie.jpg', 'Grudadinhos', trans='zoom', entry='pop', accent=ROSA))
A(P('u_mirror.jpg', 'Selfie no espelho, clássico!', trans='heart', entry='right', accent=CORAL))
A(P('u_olinda.jpg', 'Carnaval em Olinda!', dur=2.0, trans='flash', entry='drop', accent=AZUL))

# ---------------- CAP 2: o amor só cresceu ----------------
A(T('Capítulo 2', 'O amor só cresceu', 'passeios, risadas e muito companheirismo',
    [(255, 200, 150), (255, 120, 170)], trans='circle'))
A(P('u_piggy.jpg', 'Parceria pra toda hora', entry='drop', accent=CORAL))
A(P('069.jpg', 'A vida é da cor que a gente pinta', trans='slide', entry='left', accent=VERDE))
A(TRIO(['070.jpg', '071.jpg', '072.jpg'], trans='zoom', accent=VERDE, cap='Aventuras a dois'))
A(P('073.jpg', 'Noites especiais', trans='heart', entry='pop', accent=DOURADO))
A(P('u_party.jpg', 'Noivado!', trans='flash', entry='right', accent=DOURADO))
A(P('u_kiss.jpg', 'Um beijo, um sim', dur=3.0, trans='heart', entry='pop', accent=ROSA))

# ---------------- CAP 3: casamento ----------------
A(T('Capítulo 3', 'Sim, pra sempre!', 'diante de Deus, um só coração',
    [(255, 240, 220), (235, 190, 120)], trans='flash', deco='stars'))
A(P('u_wedding.jpg', 'O grande dia', dur=4.0, trans='heart', entry='pop', rot=0, accent=DOURADO))

# ---------------- CEGONHA ----------------
A(dict(type='stork', dur=5.0, trans='fade'))

# ---------------- CAP 4: gravidez ----------------
A(T('Capítulo 4', 'Esperando você', 'a família ia crescer!',
    [(255, 210, 230), (200, 170, 255)], trans='circle'))
A(P('178.jpg', 'Barriguinha crescendo', entry='drop', accent=LILAS))
A(TRIO(['074.jpg', '075.jpg', '076.jpg'], trans='slide', accent=DOURADO, cap='Chá revelação'))
A(P('080.jpg', 'Torcedora desde a barriga!', trans='zoom', entry='left', accent=CORAL))
A(P('078.jpg', None, dur=1.0, trans='flash', entry='right', accent=CORAL))
A(P('079.jpg', None, dur=1.0, trans='flash', entry='pop', accent=CORAL))
A(P('081.jpg', 'Linda de vermelho', trans='heart', entry='drop', accent=ROSA))
A(P('083.jpg', None, dur=1.0, trans='flash', entry='left', accent=ROSA))
A(P('084.jpg', None, dur=1.0, trans='flash', entry='right', accent=ROSA))
A(P('086.jpg', 'Contando os dias', trans='zoom', entry='pop', accent=LILAS))
A(P('087.jpg', 'Só falta você chegar', dur=2.0, trans='heart', entry='pop', accent=LILAS))

# ---------------- CAP 5: nascimento (música de caixinha) ----------------
A(dict(type='birthcard', dur=5.0, trans='fade', section='lullaby'))
A(P('088.jpg', 'O primeiro chorinho', dur=3.0, trans='fade', entry='pop', accent=ROSA))
A(P('091.jpg', 'Amor à primeira vista', dur=3.0, trans='fade', entry='pop', accent=ROSA))
A(P('094.jpg', None, dur=2.0, trans='fade', entry='pop', accent=ROSA))
A(P('097.jpg', 'Bem-vinda ao mundo!', dur=3.0, trans='heart', entry='pop', accent=ROSA))
A(P('096.jpg', 'Emoção que não cabe no peito', dur=3.0, trans='fade', entry='pop', accent=ROSA))
A(dict(type='info', dur=7.0, trans='circle'))

# ---------------- CAP 6: primeiro ano ----------------
A(T('Capítulo 5', 'O primeiro aninho', 'cada dia uma descoberta nova',
    [(255, 190, 215), (255, 225, 150)], trans='heart', deco='stars', section='popB'))
A(P('197.jpg', 'Soninho de anjo', entry='drop', accent=ROSA))
A(P('171.jpg', 'Colinho do papai', trans='slide', entry='left', accent=AZUL))
SCENES += quick(['160.jpg', '166.jpg', '164.jpg', '170.jpg'], ROSA)
A(P('172.jpg', 'Hora do banho!', trans='zoom', entry='pop', accent=AZUL))
A(P('186.jpg', 'Primeiro Natal!', trans='heart', entry='drop', accent=(220, 60, 70)))
A(TRIO(['043.jpg', '135.jpg', '057.jpg'], trans='slide', accent=(220, 60, 70), cap='Princesa de vermelho'))
SCENES += quick(['056.jpg', '138.jpg', '144.jpg', '141.jpg'], ROSA)
A(P('139.jpg', 'Banho de piscina com o papai', trans='zoom', entry='left', accent=AZUL))
A(P('133.jpg', 'Nos ombros do papai', trans='slide', entry='right', accent=AZUL))
A(P('147.jpg', '10 meses', trans='flash', entry='drop', accent=CORAL))
A(P('150.jpg', '11 meses', trans='slide', entry='pop', accent=ROSA))
A(P('202.jpg', '1 aninho!', dur=3.0, trans='heart', entry='pop', accent=DOURADO))
A(P('061.jpg', 'Festa da princesa', trans='zoom', entry='left', accent=DOURADO))

# ---------------- CAP 7: crescendo ----------------
A(T('Capítulo 6', 'Crescendo cheia de charme', 'sorrisos, poses e muita personalidade',
    [(200, 235, 255), (255, 180, 220)], trans='circle'))
A(P('008.jpg', 'Sorriso que ilumina tudo', entry='drop', accent=CORAL))
A(P('105.jpg', 'Diva de óculos', trans='slide', entry='left', accent=ROSA))
SCENES += quick(['106.jpg', '022.jpg', '016.jpg', '109.jpg'], ROSA)
A(P('115.jpg', 'Dia dos Pais', trans='heart', entry='pop', accent=AZUL))
A(P('124.jpg', 'Dia das Mães', trans='heart', entry='pop', accent=ROSA))
A(P('125.jpg', 'Feliz Páscoa!', trans='zoom', entry='drop', accent=VERDE))
A(TRIO(['117.jpg', '121.jpg', '119.jpg'], trans='slide', accent=VERDE, cap='Torcedora do Brasil!'))
SCENES += quick(['113.jpg', '122.jpg', '199.jpg', '205.jpg'], LILAS)
A(P('009.jpg', 'Nossa família', trans='zoom', entry='pop', accent=DOURADO))
A(P('014.jpg', 'Passeio em família', trans='slide', entry='right', accent=CORAL))
A(P('211.jpg', 'Quase 2...', dur=3.0, trans='flash', entry='drop', accent=ROSA))

# ---------------- FINAL: 2 aninhos (Parabéns pra você) ----------------
A(dict(type='bigtwo', dur=3.0, trans='balloons', section='finale'))
A(P('023.jpg', None, trans='flash', entry='pop', accent=ROSA))
A(P('026.jpg', None, trans='heart', entry='left', accent=ROSA))
A(P('027.jpg', None, trans='slide', entry='drop', accent=ROSA))
A(P('031.jpg', None, trans='zoom', entry='pop', accent=ROSA))
A(P('040.jpg', None, trans='heart', entry='right', accent=ROSA))
A(P('034.jpg', None, trans='slide', entry='drop', accent=ROSA))
A(P('214.jpg', 'Papai, mamãe e a princesa', dur=3.0, trans='heart', entry='pop', accent=ROSA))
A(dict(type='end', dur=9.0, trans='flash'))

TRANS_DUR = {'fade': 0.5, 'heart': 0.7, 'circle': 0.7, 'slide': 0.5, 'flash': 0.35,
             'zoom': 0.5, 'balloons': 1.2, 'cut': 0.0}
