from PIL import Image
U='/root/.claude/uploads/453f19b0-bdfe-5782-89ab-8aabf0bb1013/'
S=1640/1390
C={
 'arretado':('e035f228',221,217,1169,1401),
 'pork':('093caf7b',221,217,1169,1383),
 'naquele':('d9137331',221,217,1169,1401),
 'cremoso':('a6fb3061',221,217,1169,1401),
 'frango':('e9514149',221,217,1169,1401),
 'coalho':('bbd35d7e',221,217,1169,1392),
 'dois':('4ac2bc42',221,217,1169,1392),
 'mes':('5e5d0ce0',221,217,1169,1401),
 'shake_ninho':('860e95f5',221,300,1169,1401),
 'shake_ovo':('a27c1a8c',221,300,1169,1401),
 'shake_pacoca':('18153631',221,290,1169,1387),
 'shake_morango':('1548399f',221,290,1169,1387),
 'mural':('4b4620b5',221,727,1169,1672),
 'cliente1':('d665a33d',221,300,1169,1401),
 'cliente2':('af42acc6',221,357,1169,1532),
 'acai':('17fe23a1',221,217,1169,1401),
}
for n,(f,*b) in C.items():
    im=Image.open(U+f+'-image.png').convert('RGB').crop(tuple(round(v*S) for v in b))
    if im.width>1000: im=im.resize((1000,round(im.height*1000/im.width)),Image.LANCZOS)
    im.save(f'img/{n}.jpg',quality=82,optimize=True,progressive=True)
