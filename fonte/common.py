LOGO_SVG = ('<svg width="{w}" height="{h}" viewBox="0 0 46 34">'
            '<ellipse cx="9" cy="15" rx="8.5" ry="7" fill="#fff"/>'
            '<ellipse cx="18" cy="27" rx="8" ry="6.5" fill="#fff"/>'
            '<path d="M18 13 C21 4 33 1 45 2 C42 10 31 15 18 13Z" fill="#3aa63a"/></svg>')


def logo(sm=False):
    w, h = (34, 25) if sm else (46, 34)
    svg = '' if sm else LOGO_SVG.format(w=w, h=h)
    return (f'<div class="logo{" sm" if sm else ""}">{svg}<div class="w"><span class="n">SPECIALE</span>'
            f'<span class="s">PIZZAS ARTESANAIS</span></div></div>')


def page(doc, sub, n, total, footer, content):
    return f'''<section class="page">
<div class="hdr">{logo(True)}<div class="r"><b>{doc}</b>{sub}</div></div>
<div class="body">{content}</div>
<div class="foot"><span>{footer}</span><span>{n} / {total}</span></div>
<div class="chk bot"></div>
</section>'''


def sec(num, title):
    return f'<div class="sec"><span class="num">{num}</span><h2>{title}</h2></div>'


def table(head, rows, num_cols=(), widths=None):
    cg = ''
    if widths:
        cg = '<colgroup>' + ''.join(f'<col style="width:{w}">' for w in widths) + '</colgroup>'
    th = ''.join(f'<th class="{"n" if i in num_cols else ""}">{h}</th>' for i, h in enumerate(head))
    trs = ''
    for r in rows:
        trs += '<tr>' + ''.join(
            f'<td class="{"n" if i in num_cols else ("k" if i == 0 else "")}">{c}</td>' for i, c in enumerate(r)) + '</tr>'
    return f'<table>{cg}<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'


def html(title, pages):
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="speciale.css"></head><body>{"".join(pages)}</body></html>'''


EST = '<span class="est">(est.)</span>'
AC = '<span class="tbc">a confirmar</span>'


def pcc(n): return f'<span class="pcc">PCC {n}</span>'
def foto(n): return f'<span class="foto">FOTO {n}</span>'
def ac(t='A CONFIRMAR'): return f'<span class="ac">{t}</span>'
