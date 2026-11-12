# Roteiros simplificados com as falas prontas, pra o Ed e a equipe gravarem. Formato celular 540x960.
# Gerar: python3 gerar_roteiros_simples.py && node render_celular.js roteiros_simples
CSS = '''
@page{size:540px 960px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0e0e0e;color:#f2f0ea;font-family:Poppins,sans-serif;font-size:14px;line-height:1.45}
.pg{width:540px;height:960px;padding:34px 30px 30px;position:relative;overflow:hidden;page-break-after:always;background:#0e0e0e}
.ey{font-size:9.5px;letter-spacing:.2em;font-weight:700;color:#f5cf4a;text-transform:uppercase;margin-bottom:8px}
h1{font-size:50px;line-height:1.04;font-weight:700;letter-spacing:-.02em;margin-bottom:14px}
h2{font-size:27px;line-height:1.1;font-weight:700;margin-bottom:4px}
h3{font-size:10px;letter-spacing:.18em;font-weight:700;color:#f5cf4a;text-transform:uppercase;margin:14px 0 7px}
.am{color:#f5cf4a}
.sub{color:#a9a69e;font-size:13px}
.tag{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:3px 9px;border-radius:20px;background:#222;color:#d9d6ce;margin:6px 4px 0 0}
.tag.am{background:#f5cf4a;color:#111}
ul{list-style:none}
li{padding-left:16px;position:relative;margin-bottom:4px;font-size:13px}
li:before{content:'';position:absolute;left:2px;top:7px;width:6px;height:6px;border-radius:50%;background:#f5cf4a}
.st{display:grid;grid-template-columns:26px 1fr;gap:0 10px;margin-bottom:9px}
.st .n{width:24px;height:24px;border-radius:50%;background:#f5cf4a;color:#111;font-weight:700;font-size:12px;text-align:center;line-height:24px}
.st .faz{font-size:13.5px}
.st .fala{margin-top:4px;background:#1a1a1a;border-left:3px solid #f5cf4a;border-radius:0 10px 10px 0;padding:7px 11px;font-size:14px;font-weight:600}
.st .fala small{display:block;font-size:9px;letter-spacing:.14em;color:#f5cf4a;font-weight:700;margin-bottom:1px}
.card{background:#1a1a1a;border-radius:12px;padding:10px 13px;margin-bottom:7px;font-size:13px}
.foot{position:absolute;left:30px;right:30px;bottom:16px;display:flex;justify-content:space-between;font-size:8.5px;letter-spacing:.16em;color:#666;font-weight:700}
'''

pages = []


def P(ey, body):
    pages.append((ey, body))


def ul(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


P('ED Barbearia · Reels de novembro', '''
<div style="height:120px"></div>
<h1>Roteiros<br><span class="am">com as falas.</span></h1>
<p class="sub" style="font-size:15px">Uma página por vídeo. É só seguir os passos e falar o que está no quadro amarelo. Pode falar do seu jeito: o importante é a ideia, não decorar palavra por palavra.</p>
<div style="height:36px"></div>
<div class="card"><b class="am">04/11 · quarta</b><br>R1 Degradê sem marca · R2 Chegou pedindo socorro</div>
<div class="card"><b class="am">11/11 · quarta</b><br>R3 Qual corte pro teu rosto · R4 Navalha, parte 2 · R5 Agendou pelo app</div>
<div class="card"><b class="am">25/11 · quarta</b><br>R6 Barba: o ritual · R7 Pai e filho</div>
''')

P('Antes de gravar qualquer vídeo', '''
<h2>5 regras <span class="am">que valem pra todos.</span></h2>
<div style="height:10px"></div>''' + ''.join(
    f'<div class="st"><div class="n">{i}</div><div class="faz">{t}</div></div>' for i, t in enumerate([
        '<b>Celular em pé</b>, lente normal (1x), lente limpa e no modo avião.',
        '<b>Luz de lado</b>, da janela ou do espelho. Nunca com a luz atrás da pessoa.',
        '<b>Pede autorização</b> pro cliente antes de filmar. Criança, só com o pai ou a mãe autorizando.',
        '<b>Filma o antes primeiro.</b> Depois que cortou, não tem como voltar.',
        '<b>Grava cada fala 2 ou 3 vezes.</b> Errou, respira e fala de novo. A gente corta na edição.',
    ], 1)) + '''
<h3>Na hora de falar</h3>''' + ul([
    'Olha pra lente do celular, não pra tela.',
    'Fala como fala com cliente na cadeira: tranquilo e direto.',
    'Antes de falar, conta 2 segundos em silêncio. Depois de falar, mais 2.',
]) + '''
<h3>Depois de gravar</h3>''' + ul([
    'Manda tudo pra House pelo WhatsApp ou pelo Drive, sem editar.',
    'Anota o @ do cliente que apareceu no vídeo.',
]))


def reel(cod, titulo, quando, precisa, passos):
    ps = ''
    for i, (faz, fala, quem) in enumerate(passos, 1):
        fl = f'<div class="fala"><small>{quem}</small>{fala}</div>' if fala else ''
        ps += f'<div class="st"><div class="n">{i}</div><div><div class="faz">{faz}</div>{fl}</div></div>'
    P(f'Roteiro {cod}', f'''<h2><span class="am">{cod}</span> · {titulo}</h2>
<div><span class="tag am">{quando}</span></div>
<h3>Precisa ter</h3>{ul(precisa)}
<h3>Passo a passo</h3>{ps}''')


ED = 'ED FALA'
CL = 'CLIENTE FALA'

reel('R1', 'Degradê sem marca', 'grava 04/11 · posta 10/11',
     ['Cliente com o cabelo das laterais crescido, que vai fazer degradê', 'Celular no tripé, na altura da orelha'],
     [('Antes de começar, o Ed fica em pé atrás do cliente, com a máquina ligada na mão, e olha pra câmera.',
       '“Degradê que marca linha é degradê mal feito. Olha só.”', ED),
      ('Filma o cliente de lado, ainda sem cortar, girando a cadeira devagar.', None, ''),
      ('Filma bem de perto: a máquina subindo na lateral, a troca de pente e a nuca. Uns 2 segundos de cada.', None, ''),
      ('No meio do corte, o Ed fala enquanto trabalha, sem parar o corte.',
       '“O segredo é não subir reto. Vou abrindo o pente aos poucos e esfumando em concha, até a linha sumir.”', ED),
      ('Filma a tesoura no topo e a navalha fazendo o contorno, bem de perto.', None, ''),
      ('No final, o Ed gira a cadeira pro espelho e o cliente passa a mão na nuca.', None, ''),
      ('Por último: a nuca pronta bem de perto, e o Ed passando a escova de baixo pra cima.',
       '“Nenhuma linha marcada. Seg a qua o primeiro corte é com 50% pelo app.”', ED)])

reel('R2', 'Chegou pedindo socorro', 'grava 04/11 · posta 14/11',
     ['Cliente com cabelo e barba bem grandes (de 2 meses ou mais)', 'Fita no chão marcando a cadeira: o depois tem que ser no mesmo lugar'],
     [('Cliente sentado, antes de cortar. Alguém pergunta de trás da câmera: “Faz quanto tempo que tu não corta?”',
       '“Faz uns [X] meses que eu não corto.” (resposta verdadeira, do jeito dele)', CL),
      ('O Ed responde de onde estiver.', '“Deixa comigo.”', ED),
      ('Filma o antes: de frente, de lado e de costas.', None, ''),
      ('O Ed põe a mão no cabelo e diz o que vai fazer.',
       '“Vou baixar a lateral, tirar esse volume e desenhar a barba.”', ED),
      ('Filma o corte: máquina, tesoura, barba e navalha, 2 segundos de cada.', None, ''),
      ('No fim, o Ed sacode a capa na frente da câmera, até tampar.', None, ''),
      ('Filma o depois: de frente, de lado e de costas, no mesmo lugar do antes.', None, ''),
      ('Dá o espelho de mão pro cliente e deixa ele falar o que quiser. Não pede pra ele reagir.', None, '')])

reel('R3', 'Qual corte pro teu rosto', 'grava 11/11 · posta 17/11',
     ['Só o Ed, com microfone de lapela', 'Logo da parede atrás', 'Gravar antes dos clientes chegarem'],
     [('Ed olha pra câmera e aponta.', '“Rosto redondo? Para de pedir esse corte.”', ED),
      ('Fala sobre o rosto redondo.',
       '“Rosto redondo pede altura em cima e lateral bem baixa. Foge de franja reta e de volume do lado, que arredonda mais.”', ED),
      ('Fala sobre o rosto quadrado.',
       '“Quadrado combina com quase tudo. Eu gosto de textura em cima pra quebrar o ângulo, e um degradê que acompanha o maxilar.”', ED),
      ('Fala sobre o rosto alongado.',
       '“Alongado é o contrário: nada de topete alto. Deixa um pouco de volume do lado, e uma franja ajuda a equilibrar.”', ED),
      ('Chega mais perto da câmera pra fechar.', '“Não sabe o teu? Comenta ROSTO que eu te digo.”', ED)])

reel('R4', 'Movimentos da navalha, parte 2', 'grava 11/11 · posta 19/11',
     ['Cliente pra contorno (barba ou cabelo)', 'Lâmina nova', 'Ed escolhe os 3 movimentos antes de gravar'],
     [('Filma bem de perto a navalha abrindo e a lâmina nova entrando.', None, ''),
      ('Ed segura a navalha e olha pra câmera.', '“O movimento que mais me pedem pra ensinar é esse aqui.”', ED),
      ('Primeiro movimento, bem de perto. O Ed fala o nome enquanto faz.', '“Um: a linha da testa. A navalha vai deitada, puxando a pele com a outra mão.”', ED),
      ('Segundo movimento.', '“Dois: o pezinho da nuca. Movimento curto, de baixo pra cima.”', ED),
      ('Terceiro movimento.', '“Três: a linha da barba na bochecha. Desenha primeiro com a ponta, depois limpa.”', ED),
      ('Filma o contorno pronto, com o dedo passando na linha.', None, ''),
      ('Ed olha pra câmera.', '“Quer aprender de verdade? Tá no destaque CURSO.”', ED)])

reel('R5', 'Agendou pelo app, sentou na hora', 'grava 11/11 · posta 24/11',
     ['Um cliente novo que marcou pelo 50% pra quarta', 'Gravar a tela do celular agendando no app (esconder nome e telefone)'],
     [('Grava a tela do celular: link da bio, escolher o serviço, o horário e confirmar.', None, ''),
      ('Filma de dentro o cliente chegando na porta.', '“Tem horário?”', CL),
      ('O Ed aponta pra cadeira.', '“Tem no app. Senta aí.”', ED),
      ('Filma o celular ou o relógio mostrando a hora certinha do agendamento.', None, ''),
      ('Filma o corte, 2 segundos de cada parte.', None, ''),
      ('Cliente se olhando no espelho no final.', None, ''),
      ('Depois do corte, um depoimento rápido do cliente, pros stories.', '“Marquei pelo app, cheguei e já sentei. E o primeiro corte saiu pela metade.”', CL)])

reel('R6', 'Barba completa: o ritual', 'grava 25/11 · posta 28/11',
     ['Cliente de barba cheia', 'Toalha quente com vapor (testar antes)', 'Fundo escuro atrás do rosto, pro vapor aparecer'],
     [('Ed segura a toalha quente e olha pra câmera.', '“Barba de 5 minutos na máquina, ou isso aqui?”', ED),
      ('Coloca a toalha no rosto do cliente. Filma de perto quando tirar, com o vapor subindo.', None, ''),
      ('Filma as mãos passando espuma ou óleo.', None, ''),
      ('Filma bem de perto a navalha desenhando a linha. Sem música e sem conversa: o som da navalha é o vídeo.', None, ''),
      ('Filma o acabamento com pente e tesoura.', None, ''),
      ('No final, o cliente passa a mão na barba.', None, ''),
      ('Ed fecha olhando pra câmera.', '“Cabelo e barba aqui é R$ 80. Marca pelo app.”', ED)])

reel('R7', 'Pai e filho na mesma cadeira', 'grava 25/11 · posta 30/11',
     ['Pai e filho agendados juntos', 'Autorização do pai por escrito', 'Espaço kids arrumado. Se a criança não quiser ser filmada, não grava'],
     [('Filma os dois chegando juntos pela porta.', None, ''),
      ('Filma o filho no espaço kids: sentando, o corte e a cara dele.', None, ''),
      ('Filma o corte do pai, 3 partes de 3 segundos.', None, ''),
      ('No final, os dois lado a lado no espelho.', None, ''),
      ('Se sair natural, o filho fala pro pai. Não força.', '“Pai, agora a gente tá igual.”', 'FILHO FALA'),
      ('O Ed fecha, ao lado deles.', '“Quem ficou melhor? Vota aí: 1 ou 2. E a agenda de dezembro já tá aberta.”', ED)])

n = len(pages)
html = ''.join(
    f'<section class="pg"><div class="ey">{e}</div>{b}<div class="foot"><span>ED BARBEARIA × HOUSE DO CREATOR</span><span>{i + 1:02d} / {n:02d}</span></div></section>'
    for i, (e, b) in enumerate(pages))
open('roteiros_simples.html', 'w').write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>ED Barbearia · Roteiros com as falas</title>
<link rel="stylesheet" href="../../fonte/fonts.css"><style>{CSS}</style></head><body>{html}</body></html>''')
print(n, 'páginas')
