# Site Canal da Construção

Abra `index.html` no navegador. O site funciona sem servidor, mas para publicar basta subir a pasta inteira (`index.html`, `css/`, `js/`, `img/`) em qualquer hospedagem estática (Netlify, Vercel, Hostinger, GitHub Pages).

## Onde editar

| O que | Arquivo |
|---|---|
| WhatsApp, telefone, e-mail, CNPJ, endereços das lojas, data final da oferta, parcelamento | `js/catalogo.js` → `LOJA` |
| Departamentos (nome, foto, ícone) | `js/catalogo.js` → `CATS` |
| Produtos (nome, preço, preço antigo, foto) | `js/catalogo.js` → `RAW` |
| Visual (cores, fontes, espaçamentos) | `css/site.css` |
| Textos da home, rodapé | `index.html` |
| Páginas institucionais (quem somos, trocas, privacidade…) | `js/app.js` → `INST` |

### Formato de um produto

```js
["Nome do produto - Marca", 49.90, 59.90, "prod/foto.jpg"],
//   nome (a marca vem depois de " - ")  preço  preço antigo (ou null)  foto (ou null)
```

- Preço `null` = "Preço sob consulta" (entra na sacola como orçamento).
- Foto `null` = o site desenha um ícone do departamento no lugar.
- Opções extras no 5º item: `{ un: "m²" }`, `{ esgotado: true }`, `{ prebl: true }`, `{ desc: "texto" }`.
- Fotos de produto ficam em `img/prod/`.

## Páginas

- `#/` início · `#/c/eletricos` departamento · `#/c/ofertas` ofertas
- `#/p/<id-do-produto>` produto · `#/busca/<termo>` busca
- `#/i/quem-somos`, `lojas`, `contato`, `como-comprar`, `pagamento-e-entrega`, `trocas-e-devolucoes`, `privacidade`, `faq`

## Como funciona a compra

Sacola → finalizar compra (dados, endereço com busca de CEP, envio, pagamento) → o pedido completo abre no WhatsApp da loja. Não há cobrança online no site: o atendente confirma estoque e frete e envia o Pix ou o link do cartão. Conta, favoritos, endereços e pedidos ficam salvos no navegador do cliente.
