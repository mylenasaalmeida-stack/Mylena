# Vetoriza o desenho da logo atual (barbudo) e gera versões nas cores da marca.
# Uso: python3 vetorizar.py <imagem-original-da-logo>
import sys
import numpy as np
from PIL import Image, ImageDraw
import potrace

Y, K = '#FFC629', '#111111'
src = Image.open(sys.argv[1]).convert('L')
cx, cy, r = 460, 477, 300                       # miolo branco da logo no print do perfil
im = src.crop((cx - r, cy - r, cx + r, cy + r)).resize((1800, 1800), Image.LANCZOS)
a = np.array(im)
yy, xx = np.mgrid[:1800, :1800]
dentro = (xx - 900) ** 2 + (yy - 900) ** 2 < (900 * 0.96) ** 2
tinta = (a < 120) & dentro
tinta[1540:, :] = False  # sobras da máquina cortada no print original
# o potracer preenche onde o bitmap é falso, por isso vai invertido
plist = potrace.Bitmap(~tinta).trace(turdsize=40, alphamax=1.0, opticurve=True, opttolerance=0.3)
d = []
for c in plist:
    d.append(f'M{c.start_point.x:.1f},{c.start_point.y:.1f}')
    for s in c.segments:
        if s.is_corner:
            d.append(f'L{s.c.x:.1f},{s.c.y:.1f}L{s.end_point.x:.1f},{s.end_point.y:.1f}')
        else:
            d.append(f'C{s.c1.x:.1f},{s.c1.y:.1f} {s.c2.x:.1f},{s.c2.y:.1f} {s.end_point.x:.1f},{s.end_point.y:.1f}')
    d.append('Z')
D = ''.join(d)
open('desenho.path', 'w').write(D)


def svg(fundo, tinta_cor, aro, transparente=False):
    # desenho ocupa 1800x1800; a logo inteira tem 2200x2200 (aro em volta)
    bg = '' if transparente else f'<circle cx="1100" cy="1100" r="1100" fill="{aro}"/><circle cx="1100" cy="1100" r="960" fill="{fundo}"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2200 2200" width="2200" height="2200">{bg}'
            f'<path transform="translate(1100 1060) scale(1.2) translate(-900 -900)" fill="{tinta_cor}" fill-rule="evenodd" d="{D}"/></svg>')


versoes = {
    'logo-ed-amarela': svg(Y, K, K),              # fundo amarelo, desenho preto, aro preto
    'logo-ed-preta': svg(K, Y, Y),                # fundo preto, desenho amarelo, aro amarelo
    'logo-ed-amarela-aro-amarelo': svg(Y, K, Y),  # só amarelo e preto, sem aro escuro
    'desenho-preto-transparente': svg(None, K, None, True),
    'desenho-amarelo-transparente': svg(None, Y, None, True),
}
for n, s in versoes.items():
    open(f'../{n}.svg', 'w').write(s)
print(len(plist), 'formas;', len(D) // 1000, 'kB de caminho')
