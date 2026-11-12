# Gera landing/index.html embutindo as imagens de img/ no lugar de {{nome}}.
import base64, pathlib, re
raiz = pathlib.Path(__file__).parent
src = (raiz / "landing/index.src.html").read_text(encoding="utf-8")
def troca(m):
    p = raiz / "img" / (m.group(1) + ".jpg")
    return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
(raiz / "landing/index.html").write_text(re.sub(r"\{\{([\w-]+)\}\}", troca, src), encoding="utf-8")
print("ok")
