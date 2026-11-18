# Gera a versão do site com as fotos em arquivos separados (pasta img/), boa para hospedagem.
import re,sys,os,shutil
out=sys.argv[1]
src=open('src.html').read()
svg=open('logo/logo-la-no-morro.svg').read()
vb=re.search(r'viewBox="([^"]+)"',svg).group(1); d=re.search(r' d="([^"]+)"',svg).group(1)
src=src.replace('{{LOGO_VB}}',vb).replace('{{LOGO_D}}',d)
used=set(re.findall(r'\{\{IMG:([\w-]+)\}\}',src))
src=re.sub(r'\{\{IMG:([\w-]+)\}\}',lambda m:f'img/{m.group(1)}.webp',src)
os.makedirs(out+'/img',exist_ok=True)
for k in used: shutil.copy(f'img/{k}.webp',f'{out}/img/{k}.webp')
open(out+'/index.html','w').write(src); print(len(used),'fotos')
