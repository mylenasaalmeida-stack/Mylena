"""Sprites desenhados por código: corações, estrelas, cegonha, balões, confete."""
import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

FD = __file__.rsplit('/', 1)[0] + '/fonts/'
def font(name, size):
    return ImageFont.truetype(FD + name, size)

SS = 3  # supersampling para bordas suaves

def _down(im, w, h):
    return im.resize((w, h), Image.LANCZOS)

def heart_path(cx, cy, s, n=120):
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((cx + x * s / 34, cy - y * s / 34))
    return pts

def heart(size, color, outline=None):
    S = size * SS
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.polygon(heart_path(S / 2, S / 2 + S * 0.04, S * 0.98), fill=color)
    # brilho
    d.ellipse([S * 0.22, S * 0.2, S * 0.36, S * 0.34], fill=(255, 255, 255, 120))
    return _down(im, size, size)

def heart_mask(W, H, cx, cy, s):
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).polygon(heart_path(cx, cy, s), fill=255)
    return m

def star(size, color, points=4):
    S = size * SS
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = S / 2
    pts = []
    for i in range(points * 2):
        r = c if i % 2 == 0 else c * 0.28
        a = math.pi * i / points - math.pi / 2
        pts.append((c + r * math.cos(a), c + r * math.sin(a)))
    d.polygon(pts, fill=color)
    im = _down(im, size, size)
    p = size // 3
    big = Image.new('RGBA', (size + 2 * p, size + 2 * p), (0, 0, 0, 0))
    big.paste(im, (p, p))
    glow = big.filter(ImageFilter.GaussianBlur(size / 8))
    return Image.alpha_composite(glow, big)

def balloon(w, color):
    h = int(w * 2.1)
    S = SS
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    bw, bh = w * S, int(w * 1.2 * S)
    d.ellipse([0, 0, bw - 1, bh], fill=color)
    d.polygon([(bw / 2 - 10 * S / 3, bh - 4), (bw / 2 + 10 * S / 3, bh - 4), (bw / 2, bh + 14 * S / 3)], fill=color)
    d.ellipse([bw * 0.2, bh * 0.12, bw * 0.38, bh * 0.38], fill=(255, 255, 255, 110))
    # cordinha ondulada
    pts = [(bw / 2 + math.sin(i / 6) * 6 * S / 3, bh + 14 * S / 3 + i * S) for i in range(int(h * 0.85 * 1) - int(bh / S) - 14)]
    if len(pts) > 1:
        d.line(pts, fill=(255, 255, 255, 200), width=max(2, S))
    return _down(im, w, h)

def stork(width, phase):
    """Cegonha cartoon voando para a direita carregando um embrulho rosa.
    phase 0..1 controla o bater de asas."""
    S = SS
    W, H = 640, 520
    im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    k = S
    def P(pts):
        return [(x * k, y * k) for x, y in pts]
    white = (255, 255, 255, 255)
    grey = (225, 228, 236, 255)
    black = (40, 40, 52, 255)
    orange = (255, 140, 50, 255)
    pink = (255, 150, 190, 255)
    flap = math.sin(phase * 2 * math.pi)
    # asa de trás
    wy = -110 * flap
    d.polygon(P([(250, 200), (330, 195), (300 + 30, 200 + wy - 40), (220, 200 + wy - 10)]), fill=grey)
    d.polygon(P([(220, 200 + wy - 10), (300 + 30, 200 + wy - 40), (250, 200 + wy - 80), (150, 200 + wy - 40)]), fill=black)
    # pernas (pra trás)
    d.line(P([(200, 250), (60, 285)]), fill=orange, width=8 * k)
    d.line(P([(205, 262), (70, 305)]), fill=orange, width=8 * k)
    # rabo
    d.polygon(P([(170, 215), (110, 205), (120, 240), (180, 250)]), fill=black)
    # corpo
    d.ellipse(P([(160, 185), (360, 280)]), fill=white)
    # pescoço
    d.polygon(P([(320, 205), (400, 120), (430, 140), (355, 245)]), fill=white)
    # cabeça
    d.ellipse(P([(385, 85), (465, 155)]), fill=white)
    # olho
    d.ellipse(P([(430, 105), (446, 121)]), fill=black)
    d.ellipse(P([(437, 108), (442, 113)]), fill=white)
    # bochecha
    d.ellipse(P([(420, 125), (440, 140)]), fill=(255, 180, 200, 200))
    # bico longo
    d.polygon(P([(455, 112), (590, 140), (590, 146), (455, 140)]), fill=orange)
    d.line(P([(458, 127), (588, 143)]), fill=(210, 100, 30, 255), width=2 * k)
    # trouxinha pendurada no bico
    d.line(P([(560, 142), (545, 230)]), fill=(255, 255, 255, 255), width=5 * k)
    d.line(P([(560, 142), (585, 230)]), fill=(255, 255, 255, 255), width=5 * k)
    d.ellipse(P([(505, 215), (625, 330)]), fill=pink)
    d.polygon(P([(520, 230), (610, 230), (565, 190)]), fill=pink)
    d.ellipse(P([(540, 238), (590, 288)]), fill=(255, 224, 200, 255))  # rostinho do bebê
    d.ellipse(P([(552, 256), (558, 262)]), fill=black)
    d.ellipse(P([(572, 256), (578, 262)]), fill=black)
    d.arc(P([(557, 262), (573, 276)]), 20, 160, fill=(200, 80, 100, 255), width=2 * k)
    d.polygon(P([(520, 290), (610, 290), (600, 325), (530, 325)]), fill=(255, 120, 170, 255))
    # coração no embrulho
    d.polygon([(x, y) for x, y in heart_path(565 * k, 305 * k, 22 * k)], fill=(255, 255, 255, 230))
    # asa da frente
    wy2 = -130 * flap
    d.polygon(P([(230, 215), (340, 210), (330, 215 + wy2 * 0.6 + 40), (200, 225 + wy2 * 0.5 + 40)]), fill=white)
    d.polygon(P([(200, 225 + wy2 * 0.5 + 40), (330, 215 + wy2 * 0.6 + 40), (280, 225 + wy2 + 90), (120, 230 + wy2 * 0.8 + 80)]), fill=black)
    im = _down(im, W, H)
    if width != W:
        im = im.resize((width, int(H * width / W)), Image.LANCZOS)
    return im

def cloud(w):
    h = int(w * 0.55)
    S = SS
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    W, H = w * S, h * S
    for (x, y, r) in [(0.25, 0.65, 0.22), (0.45, 0.45, 0.3), (0.68, 0.55, 0.25), (0.82, 0.7, 0.17), (0.5, 0.72, 0.25)]:
        d.ellipse([W * (x - r * 0.9), H * (y - r * 1.6), W * (x + r * 0.9), H * (y + r * 1.6)], fill=(255, 255, 255, 235))
    return _down(im, w, h)

def text_sprite(txt, fnt, fill, stroke=0, stroke_fill=(0, 0, 0), shadow=True, pad=30):
    bb = fnt.getbbox(txt, stroke_width=stroke)
    w, h = bb[2] - bb[0] + pad * 2, bb[3] - bb[1] + pad * 2
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if shadow:
        sh = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((pad - bb[0] + 4, pad - bb[1] + 7), txt, font=fnt, fill=(0, 0, 0, 120), stroke_width=stroke, stroke_fill=(0, 0, 0, 120))
        sh = sh.filter(ImageFilter.GaussianBlur(6))
        im = Image.alpha_composite(im, sh)
        d = ImageDraw.Draw(im)
    d.text((pad - bb[0], pad - bb[1]), txt, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return im
