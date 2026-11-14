# Santino Barber Studio · cartão de visita e panfleto

## Arquivos para a gráfica (CMYK): pasta `impressao_CMYK/`
| Arquivo | Formato final | Com sangria |
|---|---|---|
| `Santino_Cartao_FRENTE_CMYK.pdf` | 90×50 mm | 96×56 mm |
| `Santino_Cartao_VERSO_CMYK.pdf` | 90×50 mm | 96×56 mm |
| `Santino_Panfleto_A5_FRENTE_CMYK.pdf` | 148×210 mm | 154×216 mm |
| `Santino_Panfleto_A5_VERSO_CMYK.pdf` | 148×210 mm | 154×216 mm |

- Perfil de cor: Coated FOGRA39 (ISO 12647-2), embutido no PDF como OutputIntent.
- Sangria de 3 mm em todos os lados; TrimBox marca o corte final.
- Logo, QR code e título do panfleto em 100% K (preto puro, não borra em letra pequena).
- Fundo preto em preto rico C60 M40 Y40 K100.
- Carga máxima de tinta: 248% nos vetores, até 300% nas fotos (dentro do limite de couché).
- Fontes embutidas.

Os PDFs `cartao_grafica.pdf` e `panfleto_grafica.pdf` da raiz são as versões RGB (para tela).

## Prévias
- `previa/mockup_cartao.jpg`: mockup do cartão para apresentar ao cliente.
- `previa/cartao-1.png`, `previa/cartao-2.png`, `previa/panfleto-1.png`, `previa/panfleto-2.png`.

## Conceito
O espelho orgânico com LED do estúdio vira a assinatura visual da marca. No verso do cartão ele emoldura o QR code; na frente do panfleto, a foto do salão.
- Off-white quente `#F6F3EE` (o respiro), preto `#141414`, dourado `#B8935A` / `#E8BE78`.
- Tipografia: Cormorant Garamond (serifa, conversa com o logo) + Jost (caixa alta espaçada).

## Sugestão de impressão
- Cartão: couché fosco 350 g ou papel Markatto/Color Plus off-white, laminação fosca (soft touch) e, se der, hot stamping dourado no contorno do espelho.
- Panfleto: couché fosco 150–170 g, 4×4 cores.

## Conferir antes de imprimir
- O QR code leva para instagram.com/santinobarbearia. Se preferir o link do Booksy, é só trocar.
- Não tem telefone/WhatsApp. Se quiser incluir, é uma linha a mais no verso.
- As descrições dos serviços foram escritas a partir do feed. Confirme com o cliente.

## Editar
Os arquivos-fonte ficam em `fonte/` (HTML/CSS). Para gerar de novo: `cd fonte && node render.js cartao panfleto && python3 cmyk.py` (precisa de Ghostscript).
