# Recorta pessoa de foto com fundo liso de estúdio (preenchimento a partir das bordas).
# Uso: python3 -I fonte/recorta_fundo.py entrada.jpg saida.png [tolerancia]
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageChops
src, dst = sys.argv[1], sys.argv[2]
tol = int(sys.argv[3]) if len(sys.argv) > 3 else 28
im = Image.open(src).convert('RGB')
W, H = im.size
px = im.load()
# cor de fundo: mediana das bordas
bord = [px[x, 0] for x in range(0, W, 8)] + [px[0, y] for y in range(0, H, 8)] + [px[W-1, y] for y in range(0, H, 8)]
bg = tuple(sorted(c[i] for c in bord)[len(bord)//2] for i in range(3))
# imagem binária: 255 = parecido com o fundo
diff = ImageChops.difference(im, Image.new('RGB', im.size, bg)).convert('L')
near = diff.point(lambda v: 255 if v < tol else 0)
# preenche o fundo conectado às bordas (topo e laterais)
for (x, y) in [(0, 0), (W-1, 0), (W//2, 0), (0, H//2), (W-1, H//2), (0, H-1), (W-1, H-1)]:
    if near.getpixel((x, y)) == 255:
        ImageDraw.floodfill(near, (x, y), 128)
mask = near.point(lambda v: 0 if v == 128 else 255)
mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.6))
out = im.convert('RGBA'); out.putalpha(mask)
out = out.crop(mask.getbbox())
out.save(dst)
print(dst, out.size, 'fundo', bg)
