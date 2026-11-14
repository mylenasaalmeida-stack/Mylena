"""Gera os PDFs finais em CMYK (FOGRA39), um arquivo por face.

uso: python3 cmyk.py      (depois de `node render.js cartao panfleto`)

1. separa as páginas dos PDFs RGB gerados pelo Chromium;
2. converte para CMYK com Ghostscript usando o perfil Coated FOGRA39;
3. preto puro (#000: logo, QR, título) -> 100% K, para não borrar;
   fundo preto (#141414) -> preto rico C60 M40 Y40 K100;
4. define TrimBox/BleedBox (3 mm de sangria) e embute o perfil como OutputIntent.
"""
import os, subprocess, tempfile, pypdf
from pypdf.generic import (NameObject, ArrayObject, DictionaryObject, FloatObject,
                           TextStringObject, StreamObject, NumberObject)

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, '..', 'impressao_CMYK')
ICC = os.path.join(AQUI, 'CoatedFOGRA39.icc')
SANGRIA = 3 / 25.4 * 72  # 3 mm em pt

# valores que o Ghostscript gera para cada RGB com este perfil -> valor final
TROCAS = {
    '0.722 0.675 0.671 0.882': '0 0 0 1',      # #000000 -> 100K
    '0.706 0.671 0.667 0.808': '0.6 0.4 0.4 1', # #141414 -> preto rico
}

PECAS = [('cartao_grafica.pdf', ['Cartao_FRENTE', 'Cartao_VERSO']),
         ('panfleto_grafica.pdf', ['Panfleto_A5_FRENTE', 'Panfleto_A5_VERSO'])]

os.makedirs(SAIDA, exist_ok=True)
icc_bytes = open(ICC, 'rb').read()
tmp = tempfile.mkdtemp()

for origem, nomes in PECAS:
    leitor = pypdf.PdfReader(os.path.join(AQUI, '..', origem))
    for i, nome in enumerate(nomes):
        rgb = os.path.join(tmp, nome + '_rgb.pdf')
        w = pypdf.PdfWriter(); w.add_page(leitor.pages[i]); w.write(rgb)
        cmyk = os.path.join(tmp, nome + '_cmyk.pdf')
        subprocess.run(['gs', '-q', '-o', cmyk, '-sDEVICE=pdfwrite', '-dCompressPages=false',
                        '-sColorConversionStrategy=CMYK', '-sProcessColorModel=DeviceCMYK',
                        f'-sOutputICCProfile={ICC}', '-sDefaultRGBProfile=/usr/share/color/icc/sRGB.icc',
                        '-dRenderIntent=1', rgb], check=True)

        r = pypdf.PdfReader(cmyk); w = pypdf.PdfWriter()
        pg = w.add_page(r.pages[0])
        conteudo = pg.get_contents().get_data().decode('latin1')
        for a, b in TROCAS.items():
            conteudo = conteudo.replace(a + ' k', b + ' k').replace(a + ' K', b + ' K')
        novo = StreamObject(); novo.set_data(conteudo.encode('latin1'))
        pg[NameObject('/Contents')] = w._add_object(novo)
        # Form XObjects (ex.: brilho do espelho) também podem conter cores
        for xo in (pg['/Resources'].get('/XObject') or {}).values():
            xo = xo.get_object()
            if xo.get('/Subtype') == '/Form':
                d = xo.get_data().decode('latin1')
                for a, b in TROCAS.items():
                    d = d.replace(a + ' k', b + ' k').replace(a + ' K', b + ' K')
                xo.set_data(d.encode('latin1'))

        x0, y0, x1, y1 = [float(v) for v in pg.mediabox]
        pg.bleedbox = pypdf.generic.RectangleObject([x0, y0, x1, y1])
        pg.trimbox = pypdf.generic.RectangleObject([x0 + SANGRIA, y0 + SANGRIA, x1 - SANGRIA, y1 - SANGRIA])
        pg.compress_content_streams()

        perfil = StreamObject(); perfil.set_data(icc_bytes)
        perfil[NameObject('/N')] = NumberObject(4)
        intent = DictionaryObject({
            NameObject('/Type'): NameObject('/OutputIntent'),
            NameObject('/S'): NameObject('/GTS_PDFX'),
            NameObject('/OutputConditionIdentifier'): TextStringObject('FOGRA39'),
            NameObject('/Info'): TextStringObject('Coated FOGRA39 (ISO 12647-2:2004)'),
            NameObject('/RegistryName'): TextStringObject('http://www.color.org'),
            NameObject('/DestOutputProfile'): w._add_object(perfil)})
        w._root_object[NameObject('/OutputIntents')] = ArrayObject([w._add_object(intent)])
        w.add_metadata({'/Title': f'Santino Barber Studio - {nome}', '/Creator': 'Santino Barber Studio'})
        w.write(os.path.join(SAIDA, f'Santino_{nome}_CMYK.pdf'))
        print('ok', nome)
