"""Renderiza o vídeo retrospectiva quadro a quadro (PIL + numpy) e envia ao ffmpeg."""
import sys, os, math, json, random, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance
import assets as A
from timeline import SCENES, TRANS_DUR

W, H, FPS = 1920, 1080, 30
HERE = os.path.dirname(os.path.abspath(__file__))
PH = os.path.join(HERE, 'photos')

# ---------------------------------------------------------------- utilidades
def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))

def ease_out_cubic(x):
    x = clamp(x); return 1 - (1 - x) ** 3

def ease_in_out(x):
    x = clamp(x); return x * x * (3 - 2 * x)

def ease_out_back(x, s=1.70158):
    x = clamp(x); x -= 1; return x * x * ((s + 1) * x + s) + 1

def ease_out_bounce(x):
    x = clamp(x)
    n1, d1 = 7.5625, 2.75
    if x < 1 / d1: return n1 * x * x
    if x < 2 / d1: x -= 1.5 / d1; return n1 * x * x + .75
    if x < 2.5 / d1: x -= 2.25 / d1; return n1 * x * x + .9375
    x -= 2.625 / d1; return n1 * x * x + .984375

def paste(dst, src, x, y, alpha=1.0):
    """alpha_composite com recorte nas bordas; x,y = canto superior esquerdo."""
    x, y = int(round(x)), int(round(y))
    sw, sh = src.size
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(dst.width, x + sw), min(dst.height, y + sh)
    if x1 <= x0 or y1 <= y0:
        return
    s = src.crop((x0 - x, y0 - y, x1 - x, y1 - y))
    if alpha < 0.999:
        a = s.getchannel('A').point(lambda v: int(v * alpha))
        s = s.copy(); s.putalpha(a)
    dst.alpha_composite(s, (x0, y0))

def paste_c(dst, src, cx, cy, scale=1.0, alpha=1.0):
    if scale <= 0.01 or alpha <= 0.01:
        return
    if abs(scale - 1) > 0.003:
        src = src.resize((max(1, int(src.width * scale)), max(1, int(src.height * scale))), Image.BILINEAR)
    paste(dst, src, cx - src.width / 2, cy - src.height / 2, alpha)

def gradient(c1, c2, w=W, h=H, diag=True):
    a = np.array(c1, np.float32); b = np.array(c2, np.float32)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    t = (yy / h * 0.75 + xx / w * 0.25) if diag else yy / h
    img = a[None, None, :] * (1 - t[..., None]) + b[None, None, :] * t[..., None]
    return Image.fromarray(img.clip(0, 255).astype(np.uint8), 'RGB').convert('RGBA')

def load_photo(name):
    im = Image.open(os.path.join(PH, name))
    im = ImageOps.exif_transpose(im).convert('RGB')
    return im

_VIGN = None
def vignette():
    global _VIGN
    if _VIGN is None:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
        a = (np.clip(r - 0.55, 0, 1) * 200).clip(0, 170).astype(np.uint8)
        v = np.zeros((H, W, 4), np.uint8); v[..., 3] = a
        _VIGN = Image.fromarray(v, 'RGBA')
    return _VIGN

# fontes
F_TITLE = lambda s: A.font('pacifico.woff', s)
F_BOLD = lambda s: A.font('fredoka700.woff', s)
F_MED = lambda s: A.font('fredoka500.woff', s)
F_SCRIPT = lambda s: A.font('vibes.woff', s)

# ---------------------------------------------------------------- partículas
class Particles:
    def __init__(self, kind, seed, n=18, colors=None):
        rnd = random.Random(seed)
        colors = colors or [(255, 255, 255, 200), (255, 170, 200, 220), (255, 120, 170, 200)]
        self.items = []
        for i in range(n):
            size = rnd.randint(18, 60)
            col = rnd.choice(colors)
            if kind == 'hearts':
                spr = A.heart(size, col)
            elif kind == 'stars':
                spr = A.star(size, (255, 245, 190, 230))
            else:  # bolhas
                spr = Image.new('RGBA', (size, size)); ImageDraw.Draw(spr).ellipse([0, 0, size - 1, size - 1], outline=(255, 255, 255, 160), width=3)
            self.items.append(dict(spr=spr, x=rnd.uniform(0, W), sp=rnd.uniform(60, 160), ph=rnd.uniform(0, 1),
                                   amp=rnd.uniform(15, 50), fr=rnd.uniform(0.3, 0.9), tw=rnd.uniform(0, 6.28)))
        self.kind = kind

    def draw(self, img, t, alpha=1.0):
        span = H + 200
        for p in self.items:
            y = H + 100 - ((p['ph'] * span + p['sp'] * t) % span)
            x = p['x'] + math.sin(t * p['fr'] * 2 + p['tw']) * p['amp']
            a = alpha
            if self.kind == 'stars':
                a *= 0.45 + 0.55 * abs(math.sin(t * 2.5 + p['tw']))
            paste(img, p['spr'], x, y, a)

# ---------------------------------------------------------------- card polaroid
def make_card(photo, max_w, max_h, caption=None, rot=0.0, border=22, cap_h=86):
    pw, ph = photo.size
    s = min(max_w / pw, max_h / ph)
    pw2, ph2 = int(pw * s), int(ph * s)
    ph_img = photo.resize((pw2, ph2), Image.LANCZOS)
    bottom = cap_h if caption else border
    cw, ch = pw2 + 2 * border, ph2 + border + bottom
    card = Image.new('RGBA', (cw, ch), (253, 252, 248, 255))
    card.paste(ph_img, (border, border))
    if caption:
        d = ImageDraw.Draw(card)
        size = 40
        f = F_TITLE(size)
        while f.getlength(caption) > cw - 40 and size > 20:
            size -= 2; f = F_TITLE(size)
        tw = f.getlength(caption)
        d.text(((cw - tw) / 2, ph2 + border + (bottom - size * 1.5) / 2 - 2), caption, font=f, fill=(90, 70, 90))
    # sombra
    pad = 50
    full = Image.new('RGBA', (cw + 2 * pad, ch + 2 * pad), (0, 0, 0, 0))
    sh = Image.new('RGBA', full.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([pad + 8, pad + 14, pad + cw + 8, pad + ch + 14], fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    full.alpha_composite(sh)
    full.alpha_composite(card, (pad, pad))
    if abs(rot) > 0.05:
        full = full.rotate(rot, resample=Image.BICUBIC, expand=True)
    return full

def photo_bg(photo, accent):
    """Fundo: a própria foto desfocada, escurecida e tingida."""
    pw, ph = photo.size
    sw, sh = int(W * 1.12), int(H * 1.12)
    s = max(sw / pw, sh / ph)
    small = photo.resize((max(1, int(pw * s / 8)), max(1, int(ph * s / 8))), Image.BILINEAR)
    small = small.filter(ImageFilter.GaussianBlur(5))
    big = small.resize((int(pw * s), int(ph * s)), Image.BILINEAR)
    l, t = (big.width - sw) // 2, (big.height - sh) // 2
    big = big.crop((l, t, l + sw, t + sh))
    big = ImageEnhance.Brightness(big).enhance(0.62)
    tint = Image.new('RGB', big.size, accent)
    big = Image.blend(big, tint, 0.22)
    return big.convert('RGBA')

def entry_offset(kind, u):
    """retorna (dx, dy, scale_mult, extra_rot) para a animação de entrada, u em 0..1"""
    if kind == 'pop':
        return 0, 0, 0.55 + 0.45 * ease_out_back(u, 2.2), 0
    if kind == 'left':
        return -1500 * (1 - ease_out_back(u, 1.2)), 0, 1, 0
    if kind == 'right':
        return 1500 * (1 - ease_out_back(u, 1.2)), 0, 1, 0
    if kind == 'drop':
        return 0, -1200 * (1 - ease_out_bounce(u)), 1, 0
    if kind == 'up':
        return 0, 1200 * (1 - ease_out_cubic(u)), 1, 0
    return 0, 0, 1, 0

# ---------------------------------------------------------------- cenas
class Scene:
    def __init__(self, spec, idx):
        self.s = spec; self.idx = idx; self.ready = False
    def prep(self): pass
    def frame(self, t): raise NotImplementedError

class PhotoScene(Scene):
    def prep(self):
        s = self.s
        rnd = random.Random(self.idx * 7 + 3)
        rot = s['rot'] if s['rot'] is not None else rnd.choice([-4, -3, -2, 2, 3, 4])
        ph = load_photo(s['file'])
        land = ph.width > ph.height * 1.1
        mw, mh = (1300, 800) if land else (900, 820)
        if not s['cap']:
            mh += 40
        self.card = make_card(ph, mw, mh, s['cap'], rot)
        self.bg = photo_bg(ph, s['accent'])
        self.parts = Particles('hearts', self.idx, n=10)
        self.drift = rnd.choice([(-1, -1), (1, -1), (-1, 1), (1, 1)])
        self.ready = True
    def frame(self, t):
        d = self.s['dur']
        u = clamp(t / max(d, 0.1))
        ox = int((W * 0.12) / 2 * (1 + self.drift[0] * (u - 0.5) * 0.8))
        oy = int((H * 0.12) / 2 * (1 + self.drift[1] * (u - 0.5) * 0.8))
        img = self.bg.crop((ox, oy, ox + W, oy + H))
        self.parts.draw(img, t + self.idx, 0.55)
        dx, dy, sm, _ = entry_offset(self.s['entry'], t / 0.7)
        scale = (0.97 + 0.05 * u) * sm
        paste_c(img, self.card, W / 2 + dx, H / 2 + dy + 6, scale)
        img.alpha_composite(vignette())
        return img

class TrioScene(Scene):
    def prep(self):
        s = self.s
        self.cards = []
        rots = [-6, 3, -2]
        for i, f in enumerate(s['files']):
            ph = load_photo(f)
            self.cards.append(make_card(ph, 500, 640, None, rots[i], border=16))
        self.bg = photo_bg(load_photo(s['files'][1]), s['accent'])
        self.parts = Particles('hearts', self.idx, n=12)
        self.cap = A.text_sprite(s['cap'], F_TITLE(64), (255, 255, 255), stroke=3, stroke_fill=s['accent']) if s.get('cap') else None
        self.ready = True
    def frame(self, t):
        u = clamp(t / self.s['dur'])
        ox, oy = int(W * 0.06 * (0.5 + 0.4 * (u - .5))), int(H * 0.06)
        img = self.bg.crop((ox, oy, ox + W, oy + H))
        self.parts.draw(img, t + self.idx, 0.5)
        xs = [W / 2 - 560, W / 2, W / 2 + 560]
        ys = [H / 2 + 40, H / 2 + 10, H / 2 + 50]
        kinds = ['left', 'drop', 'right']
        for i in range(3):
            dx, dy, sm, _ = entry_offset(kinds[i], (t - i * 0.22) / 0.75)
            if t - i * 0.22 < 0:
                continue
            paste_c(img, self.cards[i], xs[i] + dx, ys[i] + dy, (0.98 + 0.04 * u) * sm)
        if self.cap is not None:
            k = ease_out_back((t - 0.8) / 0.5, 2.5)
            if k > 0:
                paste_c(img, self.cap, W / 2, 105, k)
        img.alpha_composite(vignette())
        return img

class TitleScene(Scene):
    def prep(self):
        s = self.s
        self.bg = gradient(s['colors'][0], s['colors'][1])
        self.parts = Particles(s['deco'], self.idx + 100, n=26)
        c2 = tuple(int(v * 0.75) for v in s['colors'][1])
        self.chap = A.text_sprite(s['chap'].upper(), F_BOLD(46), (255, 255, 255), stroke=0, shadow=False, pad=10)
        pill = Image.new('RGBA', (self.chap.width + 50, self.chap.height + 16), (0, 0, 0, 0))
        ImageDraw.Draw(pill).rounded_rectangle([0, 0, pill.width - 1, pill.height - 1], radius=pill.height // 2, fill=c2 + (230,))
        pill.alpha_composite(self.chap, (25, 8)); self.chap = pill
        size = 150
        while F_TITLE(size).getlength(s['title']) > W - 200: size -= 6
        self.title = A.text_sprite(s['title'], F_TITLE(size), (255, 255, 255), stroke=7, stroke_fill=c2)
        self.sub = A.text_sprite(s['sub'], F_MED(52), (255, 255, 255), stroke=3, stroke_fill=c2)
        self.hl = A.heart(90, (255, 255, 255, 235)); self.hr = A.heart(70, c2 + (255,))
        self.ready = True
    def frame(self, t):
        img = self.bg.copy()
        # raios girando suaves
        self.parts.draw(img, t + 3, 0.9)
        k1 = ease_out_back(t / 0.5, 2.0)
        paste_c(img, self.chap, W / 2, H / 2 - 190, k1)
        k2 = ease_out_back((t - 0.2) / 0.6, 2.6)
        wob = 1 + 0.015 * math.sin(t * 5)
        paste_c(img, self.title, W / 2, H / 2 - 30, k2 * wob)
        a3 = clamp((t - 0.6) / 0.5)
        paste_c(img, self.sub, W / 2, H / 2 + 120 + 30 * (1 - ease_out_cubic(a3)), 1, a3)
        kh = ease_out_back((t - 0.4) / 0.5, 3)
        bob = 10 * math.sin(t * 4)
        paste_c(img, self.hl, W / 2 - self.title.width / 2 - 30, H / 2 - 110 + bob, kh)
        paste_c(img, self.hr, W / 2 + self.title.width / 2 + 20, H / 2 + 40 - bob, kh)
        return img

class CountdownScene(Scene):
    def prep(self):
        rnd = np.random.default_rng(1)
        self.noise = [Image.fromarray(np.dstack([np.zeros((H // 2, W // 2, 3), np.uint8),
                      (rnd.random((H // 2, W // 2)) < 0.012).astype(np.uint8) * 140]), 'RGBA').resize((W, H)) for _ in range(5)]
        self.bg = gradient((60, 45, 70), (25, 20, 35))
        self.pre = A.text_sprite('Prontos pra uma viagem no tempo?', F_BOLD(78), (255, 255, 255), stroke=0)
        self.hearts = Particles('hearts', 5, n=14)
        self.nums = {n: A.text_sprite(str(n), F_BOLD(420), (255, 255, 255), stroke=0, shadow=True) for n in (3, 2, 1)}
        self.go = A.text_sprite('VAI!', F_BOLD(300), (255, 220, 90), stroke=12, stroke_fill=(255, 80, 150))
        self.ready = True
    def frame(self, t):
        img = self.bg.copy()
        self.hearts.draw(img, t, 0.35)
        if t < 2.0:
            k = ease_out_back(t / 0.6, 2)
            a = 1 - clamp((t - 1.7) / 0.3)
            paste_c(img, self.pre, W / 2, H / 2, k, a)
        elif t < 5.0:
            n = 3 - int(t - 2.0); u = (t - 2.0) % 1.0
            d = ImageDraw.Draw(img)
            cx, cy, R = W / 2, H / 2, 330
            # círculo do "filme antigo" e varredura
            d.pieslice([cx - 900, cy - 900, cx + 900, cy + 900], -90, -90 + 360 * u, fill=(255, 110, 165, 90))
            d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=(255, 255, 255, 220), width=10)
            d.ellipse([cx - R + 40, cy - R + 40, cx + R - 40, cy + R - 40], outline=(255, 255, 255, 120), width=5)
            d.line([0, cy, W, cy], fill=(255, 255, 255, 70), width=4)
            d.line([cx, 0, cx, H], fill=(255, 255, 255, 70), width=4)
            k = 1.25 - 0.25 * ease_out_cubic(u / 0.3)
            paste_c(img, self.nums[n], cx, cy, k)
        else:
            u = t - 5.0
            k = ease_out_back(u / 0.35, 3)
            paste_c(img, self.go, W / 2, H / 2, k * (1 + 0.6 * clamp((u - 0.7) / 0.3)), 1 - clamp((u - 0.75) / 0.25))
        img.alpha_composite(self.noise[int(t * FPS) % 5])
        img.alpha_composite(vignette())
        return img

class OpeningScene(Scene):
    def prep(self):
        self.bg = gradient((255, 170, 205), (190, 140, 255))
        self.parts = Particles('stars', 77, n=30)
        self.l1 = A.text_sprite('RETROSPECTIVA', F_BOLD(64), (255, 255, 255), stroke=0)
        self.l2 = A.text_sprite('Maria Eloá', F_TITLE(210), (255, 255, 255), stroke=9, stroke_fill=(230, 70, 140))
        self.l3 = A.text_sprite('a história de amor que trouxe você', F_MED(54), (255, 255, 255), stroke=3, stroke_fill=(200, 90, 170))
        files = [('u_kiss.jpg', -9), ('u_wedding.jpg', 7), ('087.jpg', -6), ('091.jpg', 8)]
        self.cards = [make_card(load_photo(f), 330, 330, None, r, border=12) for f, r in files]
        self.pos = [(260, 300), (W - 270, 290), (270, H - 270), (W - 260, H - 280)]
        cols = [(255, 120, 170, 255), (255, 210, 90, 255), (140, 200, 255, 255), (190, 140, 255, 255), (255, 255, 255, 255)]
        self.balloons = [(A.balloon(random.Random(i).randint(80, 120), cols[i % 5]), random.Random(i + 50).uniform(0, W), random.Random(i + 9).uniform(0, 2)) for i in range(10)]
        self.ready = True
    def frame(self, t):
        img = self.bg.copy()
        self.parts.draw(img, t, 1)
        for (b, x, ph) in self.balloons:
            y = H + 50 - ((t + ph) * 230) % (H + 500)
            paste(img, b, x + 30 * math.sin(t * 2 + ph * 3), y)
        for i, c in enumerate(self.cards):
            k = ease_out_back((t - 0.9 - i * 0.18) / 0.5, 2)
            paste_c(img, c, self.pos[i][0], self.pos[i][1] + 10 * math.sin(t * 2 + i), k * 0.95)
        paste_c(img, self.l1, W / 2, H / 2 - 190, ease_out_back(t / 0.5, 2))
        paste_c(img, self.l2, W / 2, H / 2 - 20, ease_out_back((t - 0.25) / 0.7, 2.6) * (1 + 0.02 * math.sin(t * 4)))
        a = clamp((t - 0.9) / 0.5)
        paste_c(img, self.l3, W / 2, H / 2 + 150 + 30 * (1 - a), 1, a)
        return img

class StorkScene(Scene):
    def prep(self):
        self.bg = gradient((140, 200, 250), (255, 200, 225), diag=False)
        self.frames = [A.stork(560, i / 8) for i in range(8)]
        rnd = random.Random(4)
        self.clouds = [(A.cloud(rnd.randint(220, 420)), rnd.uniform(0, W), rnd.uniform(60, H - 200), rnd.uniform(40, 120)) for _ in range(7)]
        self.txt1 = A.text_sprite('E então...', F_TITLE(110), (255, 255, 255), stroke=6, stroke_fill=(120, 150, 230))
        self.txt2 = A.text_sprite('a cegonha recebeu um pedido muito especial!', F_BOLD(62), (255, 255, 255), stroke=4, stroke_fill=(230, 100, 160))
        self.heart = A.heart(40, (255, 120, 170, 255))
        self.ready = True
    def stork_pos(self, t):
        x = -400 + (W + 800) * (t / 4.6)
        y = H * 0.5 + 60 * math.sin(t * 2.2) - 80
        return x, y
    def frame(self, t):
        img = self.bg.copy()
        for c, x, y, sp in self.clouds:
            paste(img, c, (x - sp * t) % (W + 500) - 400, y)
        # rastro de corações
        for i in range(12):
            tt = t - 0.12 * (i + 1)
            if tt < 0: break
            x, y = self.stork_pos(tt)
            paste_c(img, self.heart, x - 220, y + 40, 1 - i / 12, 1 - i / 12)
        x, y = self.stork_pos(t)
        fr = self.frames[int(t * 12) % 8]
        paste_c(img, fr, x, y)
        paste_c(img, self.txt1, W / 2, 160, ease_out_back((t - 0.3) / 0.5, 2.5))
        a = clamp((t - 1.0) / 0.5)
        paste_c(img, self.txt2, W / 2, H - 150 + 30 * (1 - a), ease_out_back((t - 1.0) / 0.5, 2), a)
        return img

class BirthCard(Scene):
    def prep(self):
        self.bg = gradient((60, 40, 90), (240, 140, 180), diag=False)
        self.parts = Particles('stars', 31, n=40)
        self.t1 = A.text_sprite('17 de novembro de 2024', F_TITLE(120), (255, 255, 255), stroke=6, stroke_fill=(200, 80, 150))
        self.t2 = A.text_sprite('08:35', F_BOLD(170), (255, 230, 240), stroke=6, stroke_fill=(200, 80, 150))
        self.t3 = A.text_sprite('o dia em que o nosso mundo ficou cor-de-rosa', F_MED(56), (255, 255, 255), stroke=3, stroke_fill=(170, 70, 140))
        self.ready = True
    def frame(self, t):
        img = self.bg.copy()
        self.parts.draw(img, t, 1)
        # linha de batimento cardíaco
        d = ImageDraw.Draw(img)
        y0 = H / 2 + 40
        pts = []
        prog = clamp(t / 2.2)
        for x in range(0, int(W * prog), 6):
            ph = (x % 480) / 480
            y = y0
            if 0.40 < ph < 0.44: y = y0 - (ph - 0.40) / 0.04 * 140
            elif 0.44 <= ph < 0.48: y = y0 - 140 + (ph - 0.44) / 0.04 * 230
            elif 0.48 <= ph < 0.52: y = y0 + 90 - (ph - 0.48) / 0.04 * 90
            pts.append((x, y))
        if len(pts) > 1:
            d.line(pts, fill=(255, 255, 255, 150), width=6, joint='curve')
        paste_c(img, self.t1, W / 2, H / 2 - 230, ease_out_back((t - 0.2) / 0.6, 2))
        beat = 1 + 0.06 * max(0, math.sin(t * 2 * math.pi * 1.2)) ** 8
        paste_c(img, self.t2, W / 2, H / 2 + 20, ease_out_back((t - 0.7) / 0.6, 2.5) * beat)
        a = clamp((t - 1.5) / 0.6)
        paste_c(img, self.t3, W / 2, H / 2 + 230, 1, a)
        return img

class InfoCard(Scene):
    def prep(self):
        self.bg = gradient((255, 200, 225), (255, 150, 190))
        self.parts = Particles('hearts', 88, n=24)
        self.name1 = A.text_sprite('Maria Eloá Sophia', F_TITLE(130), (255, 255, 255), stroke=7, stroke_fill=(220, 70, 140))
        self.name2 = A.text_sprite('Oliveira Xavier', F_TITLE(90), (255, 255, 255), stroke=5, stroke_fill=(220, 70, 140))
        self.welcome = A.text_sprite('Bem-vinda, princesa!', F_BOLD(64), (255, 255, 255), stroke=4, stroke_fill=(230, 90, 150))
        items = [('PESO', '3,210 kg'), ('ALTURA', '48 cm'), ('HORA', '08:35'), ('NASCEU NO', 'HGMI Unimed Recife')]
        self.pills = []
        for lab, val in items:
            fv = F_BOLD(54); fl = F_MED(28)
            w = int(max(fv.getlength(val), fl.getlength(lab))) + 70
            p = Image.new('RGBA', (w, 140), (0, 0, 0, 0))
            d = ImageDraw.Draw(p)
            d.rounded_rectangle([0, 0, w - 1, 139], radius=36, fill=(255, 255, 255, 240))
            d.text(((w - fl.getlength(lab)) / 2, 16), lab, font=fl, fill=(230, 100, 160))
            d.text(((w - fv.getlength(val)) / 2, 54), val, font=fv, fill=(110, 60, 100))
            self.pills.append(p)
        self.ready = True
    def frame(self, t):
        img = self.bg.copy()
        self.parts.draw(img, t, 0.8)
        paste_c(img, self.name1, W / 2, 230, ease_out_back((t - 0.1) / 0.6, 2.3))
        paste_c(img, self.name2, W / 2, 380, ease_out_back((t - 0.4) / 0.6, 2.3))
        total = sum(p.width for p in self.pills) + 40 * 3
        x = W / 2 - total / 2
        for i, p in enumerate(self.pills):
            k = ease_out_back((t - 1.0 - i * 0.35) / 0.5, 2.8)
            paste_c(img, p, x + p.width / 2, 620, k)
            x += p.width + 40
        a = clamp((t - 2.8) / 0.5)
        paste_c(img, self.welcome, W / 2, 860, ease_out_back((t - 2.8) / 0.5, 2.5) * (1 + 0.03 * math.sin(t * 5)), a)
        return img

class Confetti:
    def __init__(self, seed, n=140):
        rnd = random.Random(seed)
        cols = [(255, 90, 150), (255, 210, 80), (120, 200, 255), (170, 120, 240), (255, 255, 255), (110, 220, 160)]
        self.p = [dict(x=rnd.uniform(0, W), y0=rnd.uniform(-H, 0), vy=rnd.uniform(180, 380), w=rnd.randint(10, 20), h=rnd.randint(18, 30),
                       c=rnd.choice(cols), sw=rnd.uniform(1, 4), ph=rnd.uniform(0, 6.3)) for _ in range(n)]
    def draw(self, img, t):
        d = ImageDraw.Draw(img)
        for p in self.p:
            y = (p['y0'] + p['vy'] * t) % (H + 100) - 50
            x = p['x'] + 40 * math.sin(t * p['sw'] + p['ph'])
            k = abs(math.cos(t * p['sw'] * 1.7 + p['ph']))
            hw, hh = p['w'] / 2, p['h'] / 2 * k + 2
            d.rectangle([x - hw, y - hh, x + hw, y + hh], fill=p['c'] + (255,))

class BigTwo(Scene):
    def prep(self):
        self.bg = gradient((255, 160, 200), (255, 220, 150))
        self.conf = Confetti(9)
        self.two = A.text_sprite('2', F_BOLD(620), (255, 255, 255), stroke=18, stroke_fill=(240, 80, 150))
        self.txt = A.text_sprite('aninhos!', F_TITLE(150), (255, 255, 255), stroke=8, stroke_fill=(240, 80, 150))
        self.date = A.text_sprite('17 . 11 . 2026', F_BOLD(60), (255, 255, 255), stroke=3, stroke_fill=(220, 90, 150))
        cols = [(255, 120, 170, 255), (255, 255, 255, 255), (255, 200, 90, 255), (200, 150, 255, 255)]
        self.balloons = [(A.balloon(random.Random(i).randint(110, 160), cols[i % 4]), random.Random(i + 3).choice([random.Random(i + 7).uniform(40, 420), random.Random(i + 7).uniform(W - 560, W - 140)]), random.Random(i + 1).uniform(0, 2)) for i in range(12)]
        self.ready = True
    def frame(self, t):
        img = self.bg.copy()
        for b, x, ph in self.balloons:
            paste(img, b, x + 25 * math.sin(t * 2 + ph * 4), H - ((t + ph) * 260) % (H + 500) + 100)
        self.conf.draw(img, t)
        k = ease_out_back(t / 0.6, 3)
        paste_c(img, self.two, W / 2 - 230, H / 2, k * (1 + 0.04 * math.sin(t * 6)))
        paste_c(img, self.txt, W / 2 + 230, H / 2 - 20, ease_out_back((t - 0.4) / 0.5, 2.5))
        paste_c(img, self.date, W / 2 + 230, H / 2 + 140, 1, clamp((t - 0.9) / 0.4))
        return img

class EndScene(Scene):
    def prep(self):
        self.bg = gradient((255, 170, 205), (200, 150, 255))
        self.conf = Confetti(21, 110)
        self.parts = Particles('hearts', 50, n=16)
        self.card = make_card(load_photo('041.jpg'), 560, 700, 'Maria Eloá', -5)
        self.l1 = A.text_sprite('Parabéns,', F_TITLE(120), (255, 255, 255), stroke=6, stroke_fill=(230, 70, 140))
        self.l2 = A.text_sprite('Maria Eloá!', F_TITLE(150), (255, 255, 255), stroke=7, stroke_fill=(230, 70, 140))
        self.l3 = A.text_sprite('2 aninhos de muito amor', F_BOLD(64), (255, 255, 255), stroke=3, stroke_fill=(200, 80, 160))
        self.l4 = A.text_sprite('Com amor, papai e mamãe', F_SCRIPT(96), (255, 255, 255), stroke=2, stroke_fill=(200, 80, 160))
        self.ready = True
    def frame(self, t):
        img = self.bg.copy()
        self.parts.draw(img, t, 0.8)
        self.conf.draw(img, t)
        dx = -1400 * (1 - ease_out_back(t / 0.8, 1.2))
        paste_c(img, self.card, 520 + dx, H / 2 + 10 * math.sin(t * 1.5), 1)
        cx = 1300
        paste_c(img, self.l1, cx, 260, ease_out_back((t - 0.4) / 0.5, 2.5))
        paste_c(img, self.l2, cx, 420, ease_out_back((t - 0.7) / 0.6, 2.5) * (1 + 0.02 * math.sin(t * 4)))
        paste_c(img, self.l3, cx, 590, 1, clamp((t - 1.3) / 0.5))
        paste_c(img, self.l4, cx, 760, 1, clamp((t - 2.0) / 0.8))
        # fade final para preto
        f = clamp((t - (self.s['dur'] - 1.5)) / 1.5)
        if f > 0:
            img = Image.blend(img, Image.new('RGBA', img.size, (0, 0, 0, 255)), f)
        return img

TYPES = dict(photo=PhotoScene, trio=TrioScene, title=TitleScene, countdown=CountdownScene, opening=OpeningScene,
             stork=StorkScene, birthcard=BirthCard, info=InfoCard, bigtwo=BigTwo, end=EndScene)

# ---------------------------------------------------------------- transições
_BAL = None
def balloon_layer(u):
    global _BAL
    if _BAL is None:
        rnd = random.Random(99)
        cols = [(255, 120, 170, 255), (255, 255, 255, 255), (255, 200, 90, 255), (200, 150, 255, 255), (140, 200, 255, 255)]
        _BAL = [(A.balloon(rnd.randint(150, 230), rnd.choice(cols)), rnd.uniform(-100, W - 50), rnd.uniform(0, 0.5)) for _ in range(45)]
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    for b, x, off in _BAL:
        y = H + 50 - (u * 1.6 - off) * (H + 700)
        paste(lay, b, x, y)
    return lay

def transition(kind, a, b, u):
    if kind == 'cut' or u >= 1:
        return b
    e = ease_in_out(u)
    if kind == 'fade':
        return Image.blend(a, b, e)
    if kind == 'flash':
        white = Image.new('RGBA', (W, H), (255, 255, 255, 255))
        return Image.blend(a, white, u * 2) if u < 0.5 else Image.blend(white, b, (u - 0.5) * 2)
    if kind == 'heart':
        m = A.heart_mask(W, H, W / 2, H / 2 + 40, 2900 * e ** 1.3)
        out = a.copy(); out.paste(b, (0, 0), m); return out
    if kind == 'circle':
        m = Image.new('L', (W, H), 0)
        r = 1150 * e
        ImageDraw.Draw(m).ellipse([W / 2 - r, H / 2 - r, W / 2 + r, H / 2 + r], fill=255)
        out = a.copy(); out.paste(b, (0, 0), m); return out
    if kind == 'slide':
        x = int(W * e)
        out = Image.new('RGBA', (W, H))
        out.paste(a.crop((x, 0, W, H)), (0, 0))
        out.paste(b.crop((0, 0, x, H)), (W - x, 0))
        return out
    if kind == 'zoom':
        s = 1 + 0.35 * e
        aw, ah = int(W * s), int(H * s)
        az = a.resize((aw, ah), Image.BILINEAR).crop(((aw - W) // 2, (ah - H) // 2, (aw - W) // 2 + W, (ah - H) // 2 + H))
        return Image.blend(az, b, e)
    if kind == 'balloons':
        base = a if u < 0.5 else b
        base = base.copy(); base.alpha_composite(balloon_layer(u)); return base
    return Image.blend(a, b, e)

# ---------------------------------------------------------------- linha do tempo
def build():
    scenes, t = [], 0.0
    for i, s in enumerate(SCENES):
        sc = TYPES[s['type']](s, i)
        sc.start = t
        sc.td = TRANS_DUR.get(s['trans'], 0.5) if i > 0 else 0
        scenes.append(sc)
        t += s['dur']
    return scenes, t

def render_frame(scenes, t):
    i = 0
    while i + 1 < len(scenes) and scenes[i + 1].start <= t + 1e-9:
        i += 1
    sc = scenes[i]
    if not sc.ready: sc.prep()
    lt = t - sc.start
    b = sc.frame(lt)
    if sc.td > 0 and lt < sc.td and i > 0:
        pv = scenes[i - 1]
        if not pv.ready: pv.prep()
        a = pv.frame(t - pv.start)
        return transition(sc.s['trans'], a, b, lt / sc.td)
    return b

def main():
    scenes, total = build()
    if sys.argv[1] == 'info':
        out = dict(total=total, scenes=[dict(start=sc.start, dur=sc.s['dur'], type=sc.s['type'], trans=sc.s['trans'],
                                             section=sc.s.get('section'), entry=sc.s.get('entry'), cap=sc.s.get('cap')) for sc in scenes])
        json.dump(out, open(os.path.join(HERE, 'timeline.json'), 'w'), indent=1)
        print('total', total, 'scenes', len(scenes))
        return
    if sys.argv[1] == 'still':
        for ts in sys.argv[2:]:
            render_frame(scenes, float(ts)).convert('RGB').save(os.path.join(HERE, f'still_{float(ts):07.2f}.jpg'), quality=85)
        return
    # segmento: render f0 f1 out.mp4
    f0, f1, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                          '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for f in range(f0, f1):
        t = f / FPS
        img = render_frame(scenes, t)
        p.stdin.write(img.convert('RGB').tobytes())
        # libera memória de cenas antigas
        for sc in scenes:
            if sc.ready and sc.start + sc.s['dur'] + 2 < t:
                sc.__dict__ = {k: v for k, v in sc.__dict__.items() if k in ('s', 'idx', 'start', 'td')}; sc.ready = False
        if f % 150 == 0:
            print(out, f, flush=True)
    p.stdin.close(); p.wait()

if __name__ == '__main__':
    main()
