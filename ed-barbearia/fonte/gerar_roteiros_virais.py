# 3 roteiros virais (Ed, barbearia, engraçado) com falas prontas. Formato celular 540x960.
# Gerar: python3 gerar_roteiros_virais.py && node render_celular.js roteiros_virais
from gerar_roteiros_simples import CSS

EXTRA = '''
.card{background:#1a1a1a;border-radius:12px;padding:10px 13px;margin-bottom:7px;font-size:13px}
.card.dest{border:1.5px solid #f5cf4a}
.k{color:#f5cf4a;font-size:9.5px;letter-spacing:.14em;font-weight:700;text-transform:uppercase}
.kv{display:grid;grid-template-columns:78px 1fr;gap:4px 8px;font-size:12.5px}
.kv b{color:#f5cf4a;font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;padding-top:2px}
.st .t{font-size:9px;color:#8a877f;font-weight:700;letter-spacing:.06em;display:block;margin-top:2px}
.src{font-size:10px;color:#8a877f;line-height:1.5}
'''

pages = []


def P(ey, body):
    pages.append((ey, body))


def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def passos(lista):
    out = ''
    for i, (cena, fala, quem) in enumerate(lista, 1):
        if fala and not quem:  # ação sem fala: vai no corpo do passo
            cena, fala = f'{cena}<br>{fala}', None
        fl = f'<div class="fala"><small>{quem}</small>{fala}</div>' if fala else ''
        out += f'<div class="st"><div class="n">{i}</div><div><div class="faz">{cena}</div>{fl}</div></div>'
    return out


def ganchos(g):
    return ''.join(f'<div class="card{" dest" if i == 0 else ""}"><span class="k">{"ABC"[i]}{" · recomendado" if i == 0 else ""}</span><br>{t}</div>'
                   for i, t in enumerate(g))


ED, CL, TX = 'ED FALA', 'CLIENTE FALA', 'TEXTO NA TELA'

# ---------- capa ----------
P('ED Barbearia × House do Creator · gravação de 13/11', '''
<div style="height:100px"></div>
<h1>3 vídeos<br><span class="am">pra viralizar.</span></h1>
<p class="sub" style="font-size:15px">Um pra fortalecer o Ed, um pra trazer cliente pra barbearia e um engraçado pra puxar gente nova pro perfil. Cada um com gancho, estrutura e as falas prontas.</p>
<div style="height:30px"></div>
<div class="card"><b class="am">V1 · O Ed</b><br>“O corte que eu errei”: confissão que vira autoridade</div>
<div class="card"><b class="am">V2 · A barbearia</b><br>“3 coisas que estragam teu corte em 3 dias”: dica que a pessoa salva e manda pro amigo</div>
<div class="card"><b class="am">V3 · Engraçado</b><br>“Os 4 clientes que todo barbeiro já atendeu”: esquete pra marcar o amigo</div>
''')

# ---------- pesquisa ----------
P('O que está funcionando agora', '''
<h2>O que está dando certo <span class="am">no nicho.</span></h2>
<p class="sub">Pesquisa de novembro/2026 em guias de Reels, bancos de ganchos de barbeiro e no que está circulando no TikTok e no Instagram.</p>
<h3>Ganchos</h3>''' + ul([
    '<b>Confissão pessoal</b> e momento específico vencem frase pronta. O público já reconhece gancho genérico.',
    '<b>Conselho disfarçado:</b> “3 coisas que tu faz depois do corte que estragam ele em 3 dias”. A pessoa salva e compartilha.',
    '<b>Tempo real e começo imperfeito</b> passam mais confiança que transformação perfeita demais.',
]) + '''<h3>Formatos</h3>''' + ul([
    'Antes e depois, processo acelerado e ASMR de máquina e navalha continuam fortes.',
    '<b>Esquete de tipos de cliente</b> e situações da cadeira: “só tira as pontas”, o cliente que nunca tá satisfeito, o que dorme.',
    '<b>História real e emocional</b>: o vídeo da esposa apoiando o barbeiro na inauguração vazia passou de 29 milhões de views em 2026.',
]) + '''<h3>Estrutura que segura</h3>''' + ul([
    'Gancho em até 3 s, com no máximo 15 palavras.',
    'Algo novo na tela a cada 5 a 7 s: texto, ângulo ou corte.',
    'Final que emenda no começo (loop) e uma chamada só.',
]) + '''
<h3>Fontes</h3><p class="src">reelry.app/hooks/barbers · medium.com/@viralboris (Reel hooks 2026) · flowshorts.app · jamilefernandes.com.br (Reels 2026) · tryvolume.app (tendências nov/2026) · TikTok Discover: barbershop viral, barber trends · sonoticiaboa.com.br (caso 29 milhões). Números de blog são indicativos, não pesquisa.</p>''')

# ---------- V1 ----------
P('V1 · O Ed · preparação', '''
<h2><span class="am">V1</span> · O corte que eu errei</h2>
<div class="card kv" style="margin-top:8px">
<b>Objetivo</b><span>Fortalecer o Ed como o rosto e a autoridade da ED.</span>
<b>Formato</b><span>Confissão pra câmera + cenas dele trabalhando.</span>
<b>Duração</b><span>35 a 45 s</span>
<b>Por que</b><span>História pessoal e real é o gancho que mais segura agora. E termina na frase da marca.</span></div>
<h3>Antes de gravar, pergunta pro Ed</h3>''' + ul([
    'Há quantos anos ele corta cabelo? Onde começou?',
    'Um corte que deu errado e ensinou alguma coisa. O que aconteceu? O que o cliente disse?',
    'O que ele faz diferente desde aquele dia?',
    'Tem foto antiga dele cortando? (o destaque Trajetória pode ter)',
]) + '''<p class="nota" style="font-size:12px;color:#a9a69e;margin-top:6px">A história tem que ser dele e verdadeira. As falas abaixo são a estrutura: ele conta do jeito dele.</p>
<h3>Gancho (0 a 3 s) · grava os 3</h3>''' + ganchos([
    'Ed sentado na cadeira vazia, olhando pra lente: <b>“Eu corto cabelo há [X] anos. E o corte que mais me ensinou foi um que eu errei.”</b>',
    'Ed segurando a primeira máquina ou tesoura (só se tiver): <b>“Essa aqui foi a primeira máquina que eu comprei.”</b>',
    'Ed de costas arrumando a bancada, vira pra câmera: <b>“Todo cliente que senta aqui passa por uma coisa que nem percebe.”</b>',
]))

P('V1 · O Ed · passo a passo', '<h2><span class="am">V1</span> · falas</h2>' + passos([
    ('0–3 s · cadeira vazia, Ed olha pra lente', '“Eu corto cabelo há [X] anos. E o corte que mais me ensinou foi um que eu errei.”', ED),
    ('3–10 s · fotos antigas da Trajetória por cima da fala', '“Eu comecei em [lugar], com [idade] anos. Achava que cortar bem era só não errar a máquina.”', ED),
    ('10–18 s · Ed falando, mais perto da câmera', '“Um dia um cliente levantou da cadeira, se olhou no espelho e não disse nada. Não voltou mais.” (a história real dele)', ED),
    ('18–26 s · Ed pega o espelho de mão', '“Desde aquele dia, ninguém levanta da minha cadeira sem eu revisar o acabamento com ele.”', ED),
    ('26–34 s · close dele revisando a nuca de um cliente, cliente sorrindo no espelho', None, ''),
    ('34–38 s · Ed volta pra lente', '“Por isso quem senta na cadeira da ED, volta.”', ED),
]) + '''<div class="card" style="margin-top:8px"><span class="k">Edição</span><br>Legenda na tela o tempo todo. Música baixa e emotiva. O último quadro (Ed na cadeira) igual ao primeiro, pra o vídeo emendar.</div>
<div class="card"><span class="k">Legenda</span><br>[X] anos de cadeira e o corte que mais me ensinou foi um que eu errei. Desde então, ninguém levanta sem eu revisar o acabamento. ✂️<br>Qual foi o pior corte que tu já levou? 👇<br>Agenda pelo link da bio.</div>''')

# ---------- V2 ----------
P('V2 · A barbearia · preparação', '''
<h2><span class="am">V2</span> · 3 coisas que estragam teu corte em 3 dias</h2>
<div class="card kv" style="margin-top:8px">
<b>Objetivo</b><span>Mostrar que a ED entende do assunto e trazer cliente. Vídeo pra salvar e mandar pro amigo.</span>
<b>Formato</b><span>Conselho disfarçado: lista de 3 erros, com demonstração.</span>
<b>Duração</b><span>30 a 40 s</span>
<b>Quem fala</b><span>O Ed ou um barbeiro da casa. Precisa de 1 cliente de degradê pra demonstrar.</span></div>
<h3>Confere com o Ed</h3><p style="font-size:12.5px">Os 3 erros são os mais comuns em barbearia. Se ele vê outro erro mais vezes no dia a dia, troca: o vídeo fica mais forte com o que ele realmente vê.</p>
<h3>Gancho (0 a 3 s) · grava os 3</h3>''' + ganchos([
    'Close da nuca recém-cortada. Ed: <b>“Tu saiu daqui com o corte assim. Três dias depois tá estragado. A culpa é de 3 coisas.”</b>',
    'Ed apontando pra câmera: <b>“Para de fazer isso depois de cortar o cabelo.”</b>',
    'Texto na tela sobre o resultado: <b>“POV: teu degradê durou 3 dias e tu não sabe por quê.”</b>',
]))

P('V2 · A barbearia · passo a passo', '<h2><span class="am">V2</span> · falas</h2>' + passos([
    ('0–3 s · close da nuca pronta', '“Tu saiu daqui com o corte assim. Três dias depois tá estragado. A culpa é de 3 coisas.”', ED),
    ('3–11 s · número 1 na tela, aparelho de barbear na mão', '“Um: tirar o pezinho em casa com aparelho. A linha sobe e o degradê perde o desenho.”', ED),
    ('11–19 s · número 2, cliente passando a mão no cabelo molhado', '“Dois: dormir com o cabelo molhado. Tu acorda com a marca do travesseiro e o topo perde a forma.”', ED),
    ('19–27 s · número 3, pote de pomada', '“Três: produto demais. Pomada pesada deixa o fio grudado e o corte parece mais velho.”', ED),
    ('27–34 s · Ed com a máquina na mão, sorrindo', '“E passou de 15 dias? Aí não tem dica. Tem que voltar pra cadeira.”', ED),
    ('34–36 s · texto final', 'Salva pra não esquecer. Agenda pelo link da bio.', TX),
]) + '''<div class="card" style="margin-top:8px"><span class="k">Edição</span><br>Número grande (1, 2, 3) na tela em cada erro: segura até o fim. Corte rápido entre os itens. Um “x” vermelho em cima de cada erro.</div>
<div class="card"><span class="k">Legenda</span><br>3 coisas que estragam teu corte em 3 dias. Tu faz qual delas? 👇<br>Salva e manda pro amigo que tira o pezinho em casa.<br>De segunda a quarta, o 1º corte na ED sai com 50% pelo app. Link na bio.</div>''')

# ---------- V3 ----------
P('V3 · Engraçado · preparação', '''
<h2><span class="am">V3</span> · Os 4 clientes que todo barbeiro já atendeu</h2>
<div class="card kv" style="margin-top:8px">
<b>Objetivo</b><span>Puxar gente nova pro perfil. Vídeo que a pessoa manda e marca o amigo.</span>
<b>Formato</b><span>Esquete de tipos de cliente. Cenas curtas, sem fala longa.</span>
<b>Duração</b><span>25 a 35 s</span>
<b>Elenco</b><span>O Ed como o barbeiro de cara séria. 2 ou 3 da equipe fazem os clientes, trocando boné e camisa entre as cenas.</span></div>
<h3>Regras do esquete</h3>''' + ul([
    'O Ed não ri. A graça é a cara séria dele.',
    'Cada cena tem no máximo 6 s.',
    'Nada de foto de famoso na tela do celular: o texto na tela resolve.',
]) + '''<h3>Gancho (0 a 3 s) · grava os 3</h3>''' + ganchos([
    'Ed olhando pra lente, cara de cansado, braços cruzados. Texto: <b>“Os 4 clientes que todo barbeiro já atendeu. O 3º é tu.”</b>',
    'Cliente na cadeira: <b>“Ed, só tira as pontinhas.”</b> Mostra o celular. Corta pra cara do Ed.',
    'Cliente conversando animado. A máquina liga. Silêncio total. Texto: <b>“Todo cliente quando a máquina liga:”</b>',
]))

P('V3 · Engraçado · passo a passo', '<h2><span class="am">V3</span> · cenas</h2>' + passos([
    ('0–3 s · Ed de braços cruzados, olhando pra lente', 'Os 4 clientes que todo barbeiro já atendeu. O 3º é tu.', TX),
    ('3–9 s · cliente 1 de boné, apontando o celular', '“Ed, só tira as pontinhas. Quero assim, ó.” (o celular mostra o texto “CARECA” na tela)', CL),
    ('· Ed olha a tela, olha o cliente, desliga a máquina devagar', None, ''),
    ('9–15 s · cliente 2 vira a cabeça toda hora pra ver o celular', 'Ed segura a cabeça dele com as duas mãos e endireita. Sem falar nada. Repete 2 vezes.', ''),
    ('15–23 s · cliente 3 olhando o espelho de mão', '“Tá bom… mas tira mais um pouquinho.” (3 vezes, cortes rápidos)', CL),
    ('· na terceira vez, Ed mostra a máquina sem pente', None, ''),
    ('23–29 s · cliente 4 dormindo de boca aberta', 'Ed olha pra câmera, faz “shhh” e continua o corte na ponta dos pés.', ''),
    ('29–32 s · Ed volta pra lente', '“E tu? Qual desses é tu?”', ED),
]) + '''<div class="card" style="margin-top:8px"><span class="k">Edição</span><br>Nome de cada tipo na tela (“O das pontinhas”, “O inquieto”, “O nunca satisfeito”, “O que dorme”). Áudio de comédia em alta nas viradas. Corte seco.</div>
<div class="card"><span class="k">Legenda</span><br>Os 4 clientes que todo barbeiro já atendeu 😂<br>Marca o amigo que é o nº 3 👇<br>(Na ED tem lugar pra todos os 4. Agenda pelo link da bio.)</div>''')

# ---------- dia de gravação ----------
P('Amanhã à tarde · plano de gravação', '''
<h2>Ordem do dia, <span class="am">umas 2h.</span></h2>
<table style="width:100%;border-collapse:collapse;font-size:12.5px;margin-top:6px">
<tr><td style="padding:6px 4px;color:#f5cf4a;font-weight:700;white-space:nowrap">15 min</td><td style="padding:6px 4px">Conversa com o Ed: a história do V1 e se os 3 erros do V2 batem com o que ele vê</td></tr>
<tr><td style="padding:6px 4px;color:#f5cf4a;font-weight:700">30 min</td><td style="padding:6px 4px"><b>V1</b> primeiro, com a casa mais calma. O Ed descansado fala melhor.</td></tr>
<tr><td style="padding:6px 4px;color:#f5cf4a;font-weight:700">40 min</td><td style="padding:6px 4px"><b>V2</b> com um cliente de degradê (pedir autorização)</td></tr>
<tr><td style="padding:6px 4px;color:#f5cf4a;font-weight:700">30 min</td><td style="padding:6px 4px"><b>V3</b> no fim, quando a equipe tiver um respiro</td></tr>
<tr><td style="padding:6px 4px;color:#f5cf4a;font-weight:700">10 min</td><td style="padding:6px 4px">Stories de bastidor</td></tr></table>
<h3>Luz</h3>''' + ul([
    'Usa a iluminação da ED, sem montar nada. Ela já é boa.',
    'A fachada é de vidro: à tarde o sol pode entrar forte. Nunca grava com a janela atrás do Ed (ele fica escuro).',
]) + '''<h3>Levar</h3>''' + ul([
    'Tripé, microfone de lapela e power bank',
    'Celular com espaço livre e no modo avião',
    'Boné e 2 camisas diferentes pra troca no V3',
    'Celular extra pra mostrar o “CARECA” na tela (V3)',
]) + '''<h3>Regra de ouro</h3><p style="font-size:13px">Grava os 3 ganchos de cada vídeo e cada fala 2 ou 3 vezes. A gente escolhe na edição.</p>''')

n = len(pages)
html = ''.join(
    f'<section class="pg"><div class="ey">{e}</div>{b}<div class="foot"><span>ED BARBEARIA × HOUSE DO CREATOR</span><span>{i + 1:02d} / {n:02d}</span></div></section>'
    for i, (e, b) in enumerate(pages))
open('roteiros_virais.html', 'w').write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>ED Barbearia · 3 roteiros virais</title>
<link rel="stylesheet" href="../../fonte/fonts.css"><style>{CSS}{EXTRA}</style></head><body>{html}</body></html>''')
print(n, 'páginas')
