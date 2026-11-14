from PIL import Image
U='/root/.claude/uploads/453f19b0-bdfe-5782-89ab-8aabf0bb1013/'
S=1640/1390
C={ # nome: (arquivo, x0,y0,x1,y1) em coordenadas de exibição
 'iorgut':('9cc5c556',187,1535,1203,1765),
 'antarica':('2fbc8d0d',187,745,1203,978),
 'coxinha':('48c1606f',187,1155,1203,1390),
 'pepsi':('2fbc8d0d',187,978,1203,1445),
 'destaques':('19b2357f',187,655,1203,1115),
 'casal':('4166d33e',187,378,1203,568),
 'perfil':('7144d98d',180,120,1210,960),
 'site':('156d2194',188,115,1202,1600),
 'ig_mes':('5e5d0ce0',221,217,1169,1660),
 'ig_naquele':('5eada429',221,217,1169,1660),
 'ig_frango':('869919e6',221,217,1169,1620),
 'ig_cremoso':('eb7887e0',221,217,1169,1590),
 'ig_shake':('1548399f',221,203,1169,1387),
 'ig_convoc':('71172690',221,217,1169,1401),
 'burgers':('461f16a2',187,370,1203,1090),
}
for n,(f,*b) in C.items():
    im=Image.open(U+f+'-image.png').convert('RGB').crop(tuple(round(v*S) for v in b))
    im.save(f'prints/{n}.jpg',quality=86)
