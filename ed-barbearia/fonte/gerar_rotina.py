# Planilha da rotina na ED (gravação de 13/11). Horários calculados a partir da célula de chegada.
# Gerar: python3 gerar_rotina.py
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from datetime import time

AM, PR, BR, CZ = 'FFC629', '111111', 'FFFFFF', 'F2F0EA'
fino = Side(style='thin', color='D9D6CE')
borda = Border(top=fino, bottom=fino, left=fino, right=fino)
wrap = Alignment(wrap_text=True, vertical='top')
centro = Alignment(horizontal='center', vertical='top', wrap_text=True)

ATIV = [  # (minutos, atividade, como fazer, material, com quem, se atrasar)
    (15, 'Chegar e montar o set',
     'Cumprimenta a equipe. Escolhe o canto com luz de lado: a fachada é de vidro, então a janela nunca fica atrás do Ed. Tripé, lapela no Ed e um teste de 5 s pra ouvir o áudio. Celular no modo avião.',
     'Tripé, lapela, power bank', 'Sozinha', 'Não corta'),
    (15, 'Conversa com o Ed',
     'V1: há quantos anos corta, onde começou, um corte que deu errado e o que mudou depois. V2: se os 3 erros batem com o que ele vê. V3: explica o esquete e escolhe quem da equipe faz os clientes. Pede autorização de imagem.',
     'PDF dos roteiros', 'Ed', 'Não corta'),
    (30, 'Gravar V1 · O corte que eu errei',
     'Ed na cadeira vazia. Grava os 3 ganchos e cada fala 2 ou 3 vezes (roteiro, pág. 3 e 4). Chega mais perto na parte do erro. O trecho do espelho de mão fica pra fazer com o cliente do V2.',
     'Tripé, lapela', 'Ed', 'Grava só o gancho A'),
    (10, 'Stories de bastidor',
     '3 stories: a gravação acontecendo, o Ed se preparando e o story-02 com os horários livres de hoje + link.',
     'Celular, story-02', 'Alguém da equipe pode postar', 'Corta: a equipe posta depois'),
    (40, 'Gravar V2 + final do V1',
     'Cliente de degradê (pede autorização). Close da nuca pronta pro gancho, os 3 erros com o número na tela e a fala final. Com o mesmo cliente, grava o trecho do V1: Ed revisando a nuca com o espelho de mão e o cliente sorrindo.',
     'Tripé, lapela, aparelho de barbear e pomada (pra mostrar)', 'Ed + 1 cliente', 'Não corta'),
    (10, 'Backup e conferência',
     'Passa tudo pro Drive ou pro computador. Assiste os ganchos: se algum ficou ruim, refaz agora, enquanto ainda está lá.',
     'Cabo ou Drive', 'Sozinha', 'Não corta (é rápido)'),
    (30, 'Gravar V3 · Os 4 clientes',
     'Quando a equipe tiver um respiro. 4 cenas de até 6 s, trocando boné e camisa entre elas. O Ed não ri. Celular extra com “CARECA” escrito na tela.',
     'Boné, 2 camisas, celular extra', 'Ed + 2 ou 3 da equipe', 'Faz só 3 tipos (corta o que dorme)'),
    (15, 'Fotos extras',
     'Fachada inteira com o letreiro (pro story Onde estamos), espaço kids (arte F1), salão feminino (arte F2) e um retrato do Ed com o logo da parede atrás.',
     'Celular', 'Sozinha', 'Faz só a fachada'),
    (20, 'Aprovações e pendências com o Ed',
     'Mostra o mockup do perfil e a logo amarela. Faz as perguntas da aba “Perguntas pro Ed”.',
     'Mockup e logo no celular', 'Ed', 'Manda as perguntas no WhatsApp'),
    (10, 'Fechar o dia',
     'Story de fechamento com o resultado do dia. Recolhe o equipamento. Confirma a próxima visita: quarta, 18/11, ensaio de fotos.',
     'Celular', 'Ed', 'Não corta'),
]

LEVAR = ['Tripé', 'Microfone de lapela', 'Power bank e cabo', 'Celular com espaço livre (pelo menos 10 GB)',
         'Celular extra com “CARECA” escrito na tela (V3)', 'Boné e 2 camisas diferentes (V3)',
         'Aparelho de barbear e um pote de pomada (V2)', 'Ring light, se tiver',
         'PDF dos 3 roteiros aberto no celular', 'Mockup do perfil e logo amarela no celular, pra mostrar ao Ed']

PERGUNTAS = [
    ('Gravação', 'Há quantos anos ele corta cabelo e onde começou? (V1)'),
    ('Gravação', 'Um corte que deu errado e o que ele aprendeu (V1)'),
    ('Gravação', 'Os 3 erros do V2 são os que ele mais vê? Se não, quais são?'),
    ('Aprovação', 'Aprova a logo nova em amarelo e preto pra foto de perfil?'),
    ('Aprovação', 'Aprova as 5 artes extras do feed (kids, salão, tempo de corte, Black, dezembro)?'),
    ('Conferir', 'Os prazos da arte “De quanto em quanto tempo cortar” estão certos? (degradê 15 dias, social 30, barba 7 a 15)'),
    ('Conferir', 'O espaço kids é mesmo uma sala de super-heróis?'),
    ('Conferir', 'Quais serviços e valores do salão feminino podem entrar nas artes?'),
    ('Operação', 'A ED abre no feriado de 20/11 (Consciência Negra)?'),
    ('Operação', 'Quem da equipe posta os stories em cada dia?'),
    ('Operação', 'Como o app mostra que é o 1º corte do cliente (pra conferir o 50%)?'),
    ('Operação', 'O que são os destaques G10 e Barberdy? (pra ajustar a capa)'),
    ('Vaga', 'A vaga de barbeiro é seg a sáb, 9h às 19h? Quer divulgar salário ou comissão?'),
    ('Perfil', 'Corrigir na bio: “9h ás 19h” → “9h às 19h”'),
    ('Perfil', 'Dá pra trocar o link fabulous-smakager…netlify.app por um nome da ED?'),
]

wb = Workbook()

# ---------------- aba Rotina ----------------
ws = wb.active
ws.title = 'Rotina'
ws.sheet_view.showGridLines = False
larg = {'A': 5, 'B': 9, 'C': 9, 'D': 8, 'E': 28, 'F': 62, 'G': 24, 'H': 18, 'I': 24, 'J': 13}
for c, w in larg.items():
    ws.column_dimensions[c].width = w

ws['A1'] = 'MINHA TARDE NA ED · SEXTA, 13/11'
ws['A1'].font = Font(bold=True, size=16, color=PR)
ws['A2'] = 'Gravação dos 3 vídeos virais + fotos + pendências com o Ed'
ws['A2'].font = Font(size=10, color='666666')

ws['E3'] = 'Horário que eu cheguei →'
ws['E3'].font = Font(bold=True)
ws['E3'].alignment = Alignment(horizontal='right', vertical='center')
ws['F3'] = time(13, 0)
ws['F3'].number_format = 'hh:mm'
ws['F3'].font = Font(bold=True, size=14, color=PR)
ws['F3'].fill = PatternFill('solid', fgColor=AM)
ws['F3'].alignment = Alignment(horizontal='left', vertical='center')
ws['F3'].border = borda
ws['G3'] = 'Muda só essa célula: os horários se ajustam sozinhos.'
ws['G3'].font = Font(italic=True, size=9, color='666666')
ws.merge_cells('G3:J3')

cab = ['#', 'Início', 'Fim', 'Min', 'Atividade', 'Como fazer', 'Material', 'Com quem', 'Se atrasar', 'Status']
H = 5
for i, t in enumerate(cab, 1):
    c = ws.cell(row=H, column=i, value=t)
    c.font = Font(bold=True, color=AM)
    c.fill = PatternFill('solid', fgColor=PR)
    c.alignment = centro
    c.border = borda
ws.row_dimensions[H].height = 22

for k, (mins, ativ, como, mat, quem, atraso) in enumerate(ATIV, 1):
    r = H + k
    ws.cell(row=r, column=1, value=k)
    ws.cell(row=r, column=2, value='=$F$3' if k == 1 else f'=C{r - 1}')
    ws.cell(row=r, column=3, value=f'=B{r}+D{r}/1440')
    ws.cell(row=r, column=4, value=mins)
    for col, v in zip(range(5, 11), [ativ, como, mat, quem, atraso, 'A fazer']):
        ws.cell(row=r, column=col, value=v)
    for col in range(1, 11):
        c = ws.cell(row=r, column=col)
        c.border = borda
        c.alignment = centro if col in (1, 2, 3, 4, 10) else wrap
        if k % 2 == 0:
            c.fill = PatternFill('solid', fgColor=CZ)
    ws.cell(row=r, column=2).number_format = 'hh:mm'
    ws.cell(row=r, column=3).number_format = 'hh:mm'
    ws.cell(row=r, column=5).font = Font(bold=True)
    ws.row_dimensions[r].height = 62

fim = H + len(ATIV)
T = fim + 1
ws.cell(row=T, column=5, value='Total').font = Font(bold=True)
ws.cell(row=T, column=4, value=f'=SUM(D{H + 1}:D{fim})').font = Font(bold=True)
ws.cell(row=T, column=4).alignment = centro
ws.cell(row=T, column=6, value=f'="Tempo total: "&INT(D{T}/60)&"h"&TEXT(MOD(D{T},60),"00")&" · saio por volta de "&TEXT(C{fim},"hh:mm")').font = Font(bold=True)
for col in range(1, 11):
    ws.cell(row=T, column=col).fill = PatternFill('solid', fgColor=AM)

ws.cell(row=T + 2, column=5, value='Regra de ouro').font = Font(bold=True)
ws.cell(row=T + 2, column=6, value='Grava os 3 ganchos de cada vídeo e cada fala 2 ou 3 vezes. Se atrasar, olha a coluna “Se atrasar” e corta dali, nunca da gravação do V2.')
ws.cell(row=T + 2, column=6).alignment = wrap
ws.row_dimensions[T + 2].height = 32

dv = DataValidation(type='list', formula1='"A fazer,Feito,Pulei"', allow_blank=False)
ws.add_data_validation(dv)
dv.add(f'J{H + 1}:J{fim}')
verde = PatternFill('solid', fgColor='C8E6C9')
cinza = PatternFill('solid', fgColor='E0E0E0')
ws.conditional_formatting.add(f'A{H + 1}:J{fim}', FormulaRule(formula=[f'$J{H + 1}="Feito"'], fill=verde))
ws.conditional_formatting.add(f'A{H + 1}:J{fim}', FormulaRule(formula=[f'$J{H + 1}="Pulei"'], fill=cinza, font=Font(color='888888', strike=True)))
ws.freeze_panes = f'A{H + 1}'
ws.page_setup.orientation = 'landscape'
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0
ws.sheet_properties.pageSetUpPr.fitToPage = True


def lista(nome, titulo, linhas, cols):
    s = wb.create_sheet(nome)
    s.sheet_view.showGridLines = False
    s['A1'] = titulo
    s['A1'].font = Font(bold=True, size=14)
    for i, (t, w) in enumerate(cols, 1):
        c = s.cell(row=3, column=i, value=t)
        c.font = Font(bold=True, color=AM)
        c.fill = PatternFill('solid', fgColor=PR)
        c.border = borda
        s.column_dimensions[chr(64 + i)].width = w
    for r, linha in enumerate(linhas, 4):
        for i, v in enumerate(linha, 1):
            c = s.cell(row=r, column=i, value=v)
            c.border = borda
            c.alignment = wrap
        s.row_dimensions[r].height = 30
    ultima = chr(64 + len(cols))
    d = DataValidation(type='list', formula1='"Pendente,OK"', allow_blank=False)
    s.add_data_validation(d)
    d.add(f'{ultima}4:{ultima}{3 + len(linhas)}')
    s.conditional_formatting.add(f'A4:{ultima}{3 + len(linhas)}', FormulaRule(formula=[f'${ultima}4="OK"'], fill=verde))


lista('Levar', 'O QUE LEVAR', [(x, 'Pendente') for x in LEVAR], [('Item', 60), ('Separei?', 12)])
lista('Perguntas pro Ed', 'PERGUNTAS E APROVAÇÕES COM O ED', [(a, b, '', 'Pendente') for a, b in PERGUNTAS],
      [('Tipo', 12), ('Pergunta', 70), ('Resposta', 40), ('Status', 12)])

wb.save('../ED-Barbearia-Rotina-13nov.xlsx')
print('ok')
