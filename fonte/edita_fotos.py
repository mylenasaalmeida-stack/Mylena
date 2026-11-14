"""Tratamento de fotos: fundo escurecido, dessaturado e desfocado; pele valorizada; vinheta."""
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageChops

P = 'img/mylena/'
# arquivo: (centro x, centro y, raio x, raio y) da elipse que cobre a pessoa
FOTOS = {
    'feira-sorrindo': (1000, 1180, 400, 940),
    'feira-seria': (950, 1180, 400, 940),
    'close-sorrindo': (800, 1000, 450, 980),
    'selfie-preta': (725, 1350, 700, 1350),
}


def warm(im, r=1.03, b=0.96):
    ch = im.split()
    return Image.merge('RGB', (ch[0].point(lambda v: min(255, int(v * r))), ch[1], ch[2].point(lambda v: int(v * b))))


def tint_shadows(im, color=(14, 30, 20), amount=0.45):
    lay = Image.new('RGB', im.size, color)
    lum = im.convert('L').point(lambda v: int((255 - v) * amount))
    return Image.composite(lay, im, lum)


for nome, (cx, cy, rx, ry) in FOTOS.items():
    im = Image.open(P + nome + '.jpg').convert('RGB')
    w, h = im.size
    sub = ImageEnhance.Contrast(im).enhance(1.1)
    sub = ImageEnhance.Color(sub).enhance(0.86)
    sub = ImageEnhance.Brightness(sub).enhance(1.04)
    sub = warm(sub).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=3))
    bg = im.filter(ImageFilter.GaussianBlur(16))
    bg = ImageEnhance.Color(bg).enhance(0.22)
    bg = ImageEnhance.Brightness(bg).enhance(0.55)
    bg = tint_shadows(bg)
    mask = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mask).ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(110))
    out = Image.composite(sub, bg, mask)
    # vinheta
    vig = Image.new('L', (w, h), 0)
    ImageDraw.Draw(vig).ellipse((-w * .25, -h * .15, w * 1.25, h * 1.15), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(220))
    out = Image.composite(out, Image.new('RGB', (w, h), (8, 10, 9)), vig)
    out.save(P + nome + '_ed.jpg', quality=93)
    print(nome, 'ok')
