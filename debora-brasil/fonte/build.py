"""Gera as versões finais (arquivo único, imagens e fontes embutidas) da landing e do mockup do perfil."""
import base64, io, os, re
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.dirname(AQUI)
MIME = {'.jpg': 'image/jpeg', '.png': 'image/png', '.woff': 'font/woff'}
cache = {}


def data_uri(rel):
    if rel in cache:
        return cache[rel]
    p = os.path.join(AQUI, rel)
    ext = os.path.splitext(p)[1]
    if ext == '.jpg':
        im = Image.open(p).convert('RGB')
        im.thumbnail((1100, 1100))
        b = io.BytesIO(); im.save(b, 'JPEG', quality=78, optimize=True, progressive=True); raw = b.getvalue()
    else:
        raw = open(p, 'rb').read()
    cache[rel] = f'data:{MIME[ext]};base64,' + base64.b64encode(raw).decode()
    return cache[rel]


def embutir(src, dst):
    s = open(os.path.join(AQUI, src), encoding='utf-8').read()
    s = re.sub(r'(src|href)="((?:img|fonts)/[^"]+)"', lambda m: f'{m.group(1)}="{data_uri(m.group(2))}"', s)
    s = re.sub(r'url\(((?:img|fonts)/[^)]+)\)', lambda m: f'url({data_uri(m.group(1))})', s)
    os.makedirs(os.path.dirname(os.path.join(SAIDA, dst)), exist_ok=True)
    open(os.path.join(SAIDA, dst), 'w', encoding='utf-8').write(s)
    print(dst, round(len(s) / 1024), 'KB')


embutir('landing.html', 'landing/index.html')
embutir('perfil.html', 'perfil-instagram-debora.html')
