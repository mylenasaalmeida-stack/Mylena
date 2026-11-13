# Kit de SEO local: Moda Nostra (Candeias)

Objetivo: fazer a Moda Nostra aparecer no topo das buscas "pizzaria em Candeias", "pizza perto de mim", "pizza delivery Candeias" no Google e no Google Maps.

> Campos entre [colchetes] precisam ser preenchidos com os dados reais da pizzaria.

---

## 1. Como o Google decide quem fica em 1º no Maps

São três fatores:

1. **Relevância**: o perfil diz claramente que é uma pizzaria e o que vende?
2. **Distância**: a pessoa que busca está perto? Isso não dá para mudar.
3. **Proeminência**: quantidade e nota das avaliações, frequência de fotos e postagens, menções em outros sites.

Ninguém consegue "colocar" uma empresa em 1º. Dá para trabalhar os itens 1 e 3 melhor que os concorrentes.

---

## 2. Checklist do Perfil da Empresa no Google (faça com o login do dono)

Acesse business.google.com com a conta do dono.

- [ ] Perfil **verificado**
- [ ] Nome **exatamente** igual à fachada: `Moda Nostra Pizzaria`. Não acrescente palavras-chave, porque o Google pode suspender o perfil.
- [ ] Categoria principal: **Pizzaria**
- [ ] Categorias secundárias que sejam verdadeiras: *Restaurante de entrega de pizza*, *Restaurante italiano*, *Restaurante de comida para viagem*
- [ ] Endereço igual ao do iFood, Instagram e site
- [ ] Telefone/WhatsApp: [(81) XXXXX-XXXX]
- [ ] Horário completo, com **horários especiais** em feriados
- [ ] Link do site ou cardápio digital, e link de pedido (iFood/WhatsApp)
- [ ] Atributos marcados: entrega, retirada, consumo no local, Pix, cartão, acessibilidade, Wi-Fi etc.
- [ ] **Cardápio** cadastrado item por item, com preço e foto
- [ ] **Produtos**: as 6 pizzas mais vendidas, com foto e descrição
- [ ] **Perguntas e respostas** já preenchidas (veja a seção 5)

---

## 3. Descrição do perfil (até 750 caracteres, pronta para colar)

> A Moda Nostra é a pizzaria de Candeias para quem não abre mão de uma pizza bem feita. Massa de fermentação lenta, molho de tomate da casa e ingredientes selecionados, assados em [forno a lenha / forno de pedra] até a borda ficar no ponto. No cardápio: pizzas tradicionais, especiais da casa, doces e opções de [calzone / esfiha / bebidas]. Fazemos delivery em Candeias, Piedade e região, retirada no balcão e atendimento no salão. Peça pelo WhatsApp [número] ou pelo iFood. Aberto de [dia] a [dia], das [hora] às [hora]. Moda Nostra: pizza de verdade, feita aqui em Candeias.

As palavras **pizzaria, pizza, Candeias, delivery, Piedade** aparecem de forma natural. É isso que ajuda na relevância.

---

## 4. Avaliações (o fator que mais pesa)

**O que fazer:**
- Gerar o link curto de avaliação (Perfil → "Pedir avaliações") e transformar em **QR code**.
- Colocar o QR code no **lacre da caixa**, no **balcão** e na **mensagem de pós-venda do WhatsApp**.
- Responder **todas** as avaliações em até 48h.

**Mensagem de pós-venda (WhatsApp):**
> Oi, [nome]! Aqui é da Moda Nostra 🍕 Chegou tudo certinho? Se gostou, sua avaliação no Google ajuda muito a gente: [link]. Obrigado!

**Resposta para avaliação positiva:**
> Obrigado, [nome]! Ficamos felizes que a [pizza citada] agradou. Volte sempre à Moda Nostra, aqui em Candeias!

**Resposta para avaliação negativa:**
> [Nome], sentimos muito pela experiência. Não é o padrão da Moda Nostra. Queremos entender o que aconteceu: fale com a gente no WhatsApp [número] para resolvermos.

**Proibido** (o Google detecta e pode derrubar o perfil, além de ser ilegal pelo CDC): comprar avaliações, pedir para funcionários e parentes avaliarem, oferecer brinde **em troca de nota 5** e denunciar concorrentes sem motivo.

---

## 5. Perguntas e respostas para cadastrar

| Pergunta | Resposta |
|---|---|
| Vocês entregam em Piedade? | Sim! Entregamos em Candeias, Piedade e [bairros]. |
| Tem pizza meio a meio? | Sim, em todos os tamanhos [confirmar]. |
| Aceitam Pix? | Sim: Pix, cartão e dinheiro. |
| Tem opção sem lactose/vegetariana? | [preencher] |
| Qual o tempo médio de entrega? | Em média [X] minutos. |

---

## 6. Calendário de postagens no Perfil (1 a 2 por semana)

| Semana | Tipo | Ideia |
|---|---|---|
| 1 | Novidade | Foto da pizza mais vendida: "A favorita de Candeias" |
| 2 | Oferta | Promoção de terça/quarta (dias fracos) |
| 3 | Bastidor | Vídeo curto da massa sendo aberta ou da pizza saindo do forno |
| 4 | Evento | Combo para jogo de futebol / fim de semana |

E mais **5 fotos novas por semana**: fachada, salão, equipe e pizzas com boa luz. Perfis com fotos recentes recebem mais cliques.

---

## 7. Fora do Google (proeminência)

- **Mesmo nome, endereço e telefone** em iFood, 99Food, Instagram, Facebook, TripAdvisor e Apple Maps.
- Instagram com localização marcada "Candeias, Jaboatão dos Guararapes" em todos os posts.
- Parcerias com perfis locais (páginas de Candeias/Piedade, influenciadores do bairro).
- Se houver site: página com a palavra "Pizzaria em Candeias" no título e o código abaixo.

### Código para o site (Schema.org)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Moda Nostra Pizzaria",
  "servesCuisine": ["Pizza", "Italiana"],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Rua, número]",
    "addressLocality": "Jaboatão dos Guararapes",
    "addressRegion": "PE",
    "postalCode": "[CEP]",
    "addressCountry": "BR"
  },
  "telephone": "[+55 81 XXXXX-XXXX]",
  "url": "[https://site]",
  "menu": "[https://link-do-cardapio]",
  "hasMap": "[link do Google Maps]",
  "openingHours": "[Tu-Su 18:00-23:30]",
  "priceRange": "$$"
}
</script>
```

---

## 8. Como medir

No painel do Perfil, acompanhe todo mês: **pesquisas**, **visualizações**, **cliques em "Como chegar"**, **ligações** e **cliques no site**. Meta para 90 dias: +30 avaliações novas, nota ≥ 4,7 e crescimento das buscas por "pizzaria".

Resultados aparecem em **4 a 12 semanas** de trabalho constante.
