import re,base64,sys
src=open('src.html').read()
svg=open('logo/logo-la-no-morro.svg').read()
vb=re.search(r'viewBox="([^"]+)"',svg).group(1); d=re.search(r' d="([^"]+)"',svg).group(1)
src=src.replace('{{LOGO_VB}}',vb).replace('{{LOGO_D}}',d)
def img(m):
    b=open(f'img/{m.group(1)}.webp','rb').read()
    return 'data:image/webp;base64,'+base64.b64encode(b).decode()
seen=set()
def rep(m):
    k=m.group(1)
    if k in seen: return '" data-same="'+k
    seen.add(k); return img(m)+'" data-key="'+k
src=re.sub(r'\{\{IMG:([\w-]+)\}\}',rep,src)
src=re.sub(r'src="" data-same=','data-same=',src)
assert '{{' not in src
open(sys.argv[1],'w').write(src); print(len(src))
