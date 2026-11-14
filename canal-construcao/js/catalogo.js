/* =====================================================================
   CANAL DA CONSTRUÇÃO — DADOS DA LOJA E CATÁLOGO
   Edite este arquivo para trocar contatos, departamentos e produtos.
   ===================================================================== */

const LOJA = {
  nome: "Canal da Construção & Condomínios",
  razao: "Comercial Canal Ltda",
  cnpj: "12.806.642/0001-61",
  whatsapp: "5581992035561",          // só dígitos: DDI + DDD + número
  whatsappTxt: "(81) 99203-5561",
  telefone: "(81) 2102-0488",
  telefoneLink: "+558121020488",
  email: "contato@canalconstrucao.com.br",
  instagram: "https://www.instagram.com/canalconstrucao/",
  fimOferta: "2026-11-30T23:59:59-03:00",
  parcelasMax: 4,                    // até 4x sem juros
  parcelaMin: 50,                    // valor mínimo aproximado da parcela
  lojas: [
    { id: "arruda", nome: "Arruda", end: "Av. Beberibe, 1501 – Arruda, Recife – PE, 52120-000",
      mapa: "Av.+Beberibe,+1501+-+Arruda,+Recife+-+PE,+52120-000" },
    { id: "bv", nome: "Boa Viagem", end: "Av. Fernando Simões Barbosa, 1274 – Boa Viagem, Recife – PE",
      mapa: "Av.+Fernando+Sim%C3%B5es+Barbosa,+1274+-+Boa+Viagem,+Recife+-+PE" }
  ]
};

/* Departamentos (mesmos do site atual) — img = foto do card na home; ic = ícone */
const CATS = [
  { id: "basicos",      nome: "Básicos para Construção", img: "u-obra.jpg",        ic: "brick", sub: "Argamassa, rejunte, reboco" },
  { id: "eletricos",    nome: "Materiais Elétricos",     img: "p-lampadas.jpg",    ic: "bolt",  sub: "Tomadas, cabos, disjuntores" },
  { id: "pisos",        nome: "Pisos e Revestimentos",   img: "u-pisos.jpg",       ic: "tile",  sub: "Cerâmica e porcelanato" },
  { id: "tintas",       nome: "Tintas",                  img: "u-tintas.jpg",      ic: "paint", sub: "Coral, Suvinil, Sherwin-Williams" },
  { id: "portas",       nome: "Portas e Janelas",        img: "p-porta.jpg",       ic: "door",  sub: "Sanfonadas, alumínio, números" },
  { id: "fechaduras",   nome: "Fechaduras e Acessórios", img: "p-fechadura.jpg",   ic: "lock",  sub: "Correntes e acessórios" },
  { id: "cadeados",     nome: "Cadeados",                img: "prod/cadeado-40.jpg", ic: "lock", sub: "Linha Pado", light: true },
  { id: "epi",          nome: "EPI",                     img: "u-casa.jpg",        ic: "helmet",sub: "Botas, luvas, fitas" },
  { id: "hidraulica",   nome: "Hidráulica",              img: "prod/caixa-dagua-1000.jpg", ic: "pipe", sub: "Caixas d'água, grelhas, chuveiros", light: true },
  { id: "ferramentas",  nome: "Ferramentas",             img: "p-ferramentas.jpg", ic: "tool",  sub: "Atlas, Tramontina, Norton" },
  { id: "ferragem",     nome: "Ferragem",                img: "p-furadeira.jpg",   ic: "tool",  sub: "Parafusos, buchas, pregos" },
  { id: "metais",       nome: "Metais",                  img: "prod/torneira-cozinha-bica-alta.jpg", ic: "drop", sub: "Torneiras, registros, duchas", light: true },
  { id: "loucas",       nome: "Louças",                  img: "prod/bacia-ravena.jpg", ic: "drop", sub: "Bacias, caixas acopladas, cubas", light: true },
  { id: "banheiro",     nome: "Móveis para Banheiro",    img: "u-banheiro.jpg",    ic: "drop",  sub: "Gabinetes e espelhos" },
  { id: "pvc",          nome: "PVC",                     img: "u-obra.jpg",        ic: "pipe",  sub: "Forros e perfis" },
  { id: "iluminacao",   nome: "Iluminação",              img: "p-pendente.jpg",    ic: "bulb",  sub: "Lâmpadas, painéis, refletores" },
  { id: "automotivo",   nome: "Automotivo",              img: "prod/cera-pasta.jpg", ic: "car", sub: "Cera, graxa, odorizador", light: true },
  { id: "limpeza",      nome: "Limpeza",                 img: "p-limpeza.jpg",     ic: "spray", sub: "Desincrustantes, vaselina, pós-obra" },
  { id: "lar",          nome: "Utilidades do Lar",       img: "u-cozinha.jpg",     ic: "home",  sub: "Casa organizada" }
];

/* Produtos.
   Formato: [nome, preço (null = sob consulta), preço antigo (ou null), imagem (ou null), opções]
   opções: { un: "m²", esgotado: true, prebl: true, desc: "..." }
   Preços lidos do site canalconstrucao.com.br em 14/11/2026 — confira antes de publicar. */
const RAW = {
  loucas: [
    ["Pia de Cozinha Plus 30 em Aço Inox 100x53 cm", 249.90, null, null],
    ["Pia de Cozinha Plus 30 em Aço Inox 120x53 cm", 249.90, null, null],
    ["Pia de Cozinha Plus 30 em Aço Inox 140x53 cm", 329.90, null, null],
    ["Pia de Cozinha Plus 30 em Aço Inox 160x53 cm", 399.90, null, null],
    ["Pia de Cozinha em Aço Inox Bali 200x53 cm", 759.90, null, null],
    ["Caixa Para Acoplar 6 Litros Parati Branco - Logasa", 199.95, null, "prod/caixa-acoplar-parati.jpg"],
    ["Cuba Inox 560x350 mm Para Embutir - Ghelplus", 145.90, null, "prod/cuba-inox-560.jpg"],
    ["Bacia Para Caixa Acoplada Ravena Branco - Deca", 575.00, null, "prod/bacia-ravena.jpg"],
    ["Cuba de Embutir Quadrada Branco 350x350 mm", 112.90, null, "prod/cuba-embutir-quadrada.jpg"],
    ["Cuba de Sobrepor Redonda Branco 310x310 mm", 149.00, null, null],
    ["Assento Termofixo Com Slow Close e Easy Clean", 1099.90, null, null],
    ["Assento Plástico Com Microban Para Bacias", 329.90, null, null],
    ["Caixa Acoplada Duo Vogue Plus Conforto Branco", 999.90, null, null],
    ["Caixa Acoplada Branco Com Acionamento Duo", 1295.90, null, null],
    ["Kit Completo Bacia Com Caixa Acoplada Quadra", 1268.90, null, null],
    ["Caixa Acoplada Para Bacia Sanitária Porto Branco", 175.00, null, null],
    ["Caixa Acoplada Para Bacia Sanitária Leiria Kids 6 L", 234.00, null, null],
    ["Kit Bacia + Caixa Para Acoplar Saveiro - Celite", 485.00, null, null],
    ["Kit Bacia + Caixa Para Acoplar Parati - Logasa", 424.95, null, null],
    ["Bacia Para Caixa Sem Abertura Acesso Comfort - Roca", 799.00, null, null]
  ],
  metais: [
    ["Torneira Parede Bica Móvel Ref 2060 C-31 - Ir Metais", 67.90, null, "prod/torneira-parede-2060.jpg"],
    ["Torneira Jardim / Tanque Ref 1130 C-31 - Ir Metais", 42.90, null, "prod/torneira-jardim-1130.jpg"],
    ["Registro de Gaveta Para Uso Semi Industrial 1/2\"", 94.40, null, "prod/registro-gaveta.jpg"],
    ["Barra de Apoio Reta em PVC 50 cm - Astra", 128.00, null, null],
    ["Torneira Para Cozinha Parede Bica Alta Móvel", 65.60, null, "prod/torneira-cozinha-bica-alta.jpg"],
    ["Válvula de Retenção Horizontal 3/4 Portinhola", 155.90, null, "prod/valvula-retencao.jpg"],
    ["Torneira de Cozinha Parede Aquarius DN15", 209.90, null, null],
    ["Torneira Para Cozinha Parede Bica Alta Móvel Branca", 65.90, null, null],
    ["Torneira Para Lavatório de Mesa Orbe Branca 1/2\"", 21.50, null, null],
    ["Engate Flexível Trançado 40 cm - Sigma", 58.70, null, null],
    ["Papeleira Com Tampa Metal - Ir Metais", 16.90, null, null],
    ["Torneira de Parede Com Filtro e Bica Móvel Branca", 144.90, null, null],
    ["Castelo Para MVS Torneira Deca - Blukit", 38.90, null, null],
    ["Castelo Para Mecanismo de Saída Convencional", 23.90, null, null],
    ["Mangueira Flexível Para Gás 3/8\" 1 Metro", 56.90, null, null],
    ["Adaptador Para Filtro 1/2 Saída 1/4 Cromado - Blukit", 159.90, null, null],
    ["Base Registro de Gaveta 3/4 DN20 - Saga", 29.90, 49.90, null],
    ["Ducha Higiênica Lucca Black Flex 1,20", 346.40, null, null],
    ["Ducha Higiênica Com Derivação One Cromado", 259.90, null, null],
    ["Reparo MVS Para Torneira Pressurizada - Docol", 188.90, null, null],
    ["Adaptador e Acessórios - Blukit", null, null, "p-blukit.jpg", { desc: "Adaptadores, registros e acessórios práticos para instalação." }]
  ],
  limpeza: [
    ["Dispenser Big Roll Papel Higiênico Preto - Velox", 49.90, null, "prod/dispenser-big-roll.jpg"],
    ["Inseticida Aerossol SBP Eucalipto 450 ml - SBP", 23.90, null, "prod/inseticida-sbp.jpg"],
    ["Dispenser Toalheiro Papel Toalha Interfolhado - Velox", 45.90, null, "prod/dispenser-toalheiro.jpg"],
    ["Sabonete Líquido Musk Net Max 5 L - Quimilab", 29.90, null, "prod/sabonete-net-max.jpg"],
    ["Detergente Automotivo Brenner Cera 5 L - Quimilab", 62.90, null, "prod/detergente-brenner.jpg"],
    ["Essência Palmolux 100 ml - Valença", 13.90, null, "prod/essencia-palmolux.jpg"],
    ["Sabonete Guaraná e Açaí 1 L - Premisse", 16.90, 17.90, null],
    ["Refil Mop Brilhus Sekito - Bettanin", 37.70, null, null],
    ["Odorizador de Ambientes Becker Flower Capim-Limão", 125.90, null, null],
    ["Lixeira Gari Europeu Cinza Com Roda 240 L - Bralimpia", 739.90, null, null],
    ["Limpador Pisos e Pedras Detergente Desincrustante", 155.88, null, null, { sub: "Desincrustantes" }],
    ["Lixeira Com Pedal 7 L Branca - Jaguar", 28.50, null, null],
    ["Removedor de Ferrugem 2 em 1 1 L - Allchem Química", 73.21, null, null],
    ["Ponteira Direita Para Mangueira de Piscina", 9.90, null, null],
    ["Sabão Para Roupas Dínamo 2 L - Valença", 15.90, null, null],
    ["Cabo Alumínio Sem Rosca Azul Fosco 1,40 m", 45.90, null, null],
    ["Detergente Neutro 5 L - Valença", 19.90, null, null],
    ["Lava Roupas + Econômico 5 L - Becker", 36.00, 37.70, null],
    ["Cloro Oxypower Multiação Para Piscina 1kg", 24.90, null, null],
    ["Vaselina Líquida 1 L - Valença", 42.90, null, "prod/vaselina-liq-1l.jpg", { sub: "Vaselina" }],
    ["Vaselina Líquida 500 ml - Allchem Química", 42.53, null, "prod/vaselina-liq-500.jpg", { sub: "Vaselina" }],
    ["Vaselina Sólida 450g - Allchem Química", 53.87, null, "prod/vaselina-sol-450.jpg", { sub: "Vaselina" }],
    ["Vaselina Sólida 900g - Allchem Química", 102.44, null, "prod/vaselina-sol-900.jpg", { sub: "Vaselina" }],
    ["Desincrustante Voraz Grill 5 L - Quimilab", 109.90, null, "prod/voraz-grill.jpg", { sub: "Desincrustantes" }],
    ["Desincrustante Ácido Trax M50 5 L - Quimilab", 91.50, null, "prod/trax-m50.jpg", { sub: "Desincrustantes" }],
    ["Detergente Desincrustante Ácido Removic 5 L - Becker", 120.00, 128.00, "prod/removic-5l.jpg", { sub: "Desincrustantes" }],
    ["Detergente Desincrustante Ácido Removic 750 ml - Becker", 28.90, 33.50, "prod/removic-750.jpg", { sub: "Desincrustantes" }],
    ["Super Limpador Pós-Obra Para Cerâmica e Porcelanato", 29.90, null, "prod/super-limpador-pos-obra.jpg", { sub: "Desincrustantes" }]
  ],
  iluminacao: [
    ["Lâmpada Bulbo LED High Power 30W Bivolt Branca", 19.90, null, "prod/lampada-bulbo-30w.jpg"],
    ["Lâmpada Pera LED 9W Bivolt Branca 6500K - Avant", 2.90, null, "prod/lampada-pera-9w.jpg"],
    ["Painel Pop LED Embutir Redondo 22 cm 18W Bivolt - Avant", 24.90, null, "prod/painel-pop-redondo.jpg"],
    ["Painel Pop LED Embutir Quadrado 17x17 12W - Avant", 16.90, null, "prod/painel-pop-quadrado.jpg"],
    ["Refletor Slim LED 50W Branca 6500K - Avant", 39.90, null, "prod/refletor-50w.jpg"],
    ["Refletor Slim LED 20W Branca 6500K - Avant", 34.90, null, "prod/refletor-20w.jpg"],
    ["Luminária Spot LED Supimpa Quadrada 5W", 12.90, null, null],
    ["Spot LED Quadrada Embutir 5W Amarela 3000K", 9.90, null, null],
    ["Luminária Slim LED Embutir Quadrado 12W", 18.90, null, null],
    ["Luminária de Emergência 30 LEDs 2W Branca 6500K", 23.90, null, null],
    ["Lâmpada LED Retrô Globo G95 2200K 4W Bivolt", 41.90, null, null],
    ["Luminária LED Slim 6.500K 60 cm 18W - Blumenau", 29.90, null, null],
    ["Luz Noturna Com Sensor Quadrado Liso 3.000K", 33.90, null, null],
    ["Painel LED Slim Embutir Quadrado 12W 6.500K", 16.90, null, null],
    ["Plafonier Alumínio Preto 140 mm 1 Lâmpada", 14.90, null, null],
    ["Luminária de Luz Noturna LED Corujinha 3000K", 19.90, null, null],
    ["Luminária de Luz Noturna LED Bola 3000K 1W", 19.90, null, null],
    ["Painel LED Sobrepor Redondo Alumínio 24W", 43.90, null, null],
    ["Ventilador de Mesa Turbo Preto 6 Pás 40 cm - Ventisol", 134.90, null, null],
    ["Ventilador de Mesa Turbo Bronze 6 Pás 50 cm - Ventisol", 169.90, null, null]
  ],
  hidraulica: [
    ["Caixa D'água de Polietileno 500 L Com Tampa - Fortlev", 299.90, null, "prod/caixa-dagua-500.jpg"],
    ["Caixa D'água de Polietileno 1000 L Com Tampa - Fortlev", 449.90, null, "prod/caixa-dagua-1000.jpg"],
    ["Caixa D'água de Polietileno 1500 L Com Tampa - Fortlev", 1229.90, null, "prod/caixa-dagua-1500.jpg"],
    ["Caixa D'água de Polietileno 10.000 L Com Tampa - Fortlev", 7462.00, null, "prod/caixa-dagua-10000.jpg"],
    ["Grelha Ecológica Quadrada 100 mm Branca - Tigre", 8.50, null, "prod/grelha-eco-100.jpg"],
    ["Grelha Abre e Fecha Quadrada 150 mm Branca", 38.90, null, "prod/grelha-abre-fecha.jpg"],
    ["Grelha Ecológica Quadrada 150 mm Branca - Tigre", 16.90, null, "prod/grelha-eco-150.jpg"],
    ["Porta Grelha Redondo 100 mm Branco - Tigre", 11.00, null, "prod/porta-grelha-branco.jpg"],
    ["Porta Grelha Redondo 100 mm Prata - Tigre", 16.50, null, "prod/porta-grelha-prata.jpg"],
    ["Porta Grelha Quadrado Para Grelha Quadrada 150 mm", 21.00, null, "prod/porta-grelha-quadrado.jpg"],
    ["Porta Grelha Redondo 150 mm Branco - Tigre", 15.90, null, "prod/porta-grelha-150.jpg"],
    ["Sifão Tubo Extensível Branco Com Suporte", 8.90, null, "prod/sifao-suporte.jpg"],
    ["Sifão Tubo Extensivo Universal Branco - Blukit", 5.90, null, null],
    ["Sifão Tubo Extensivo Duplo Universal Branco - Blukit", 21.90, null, null],
    ["Sifão Tubo Extensivo Universal Cromado - Blukit", 39.90, null, null],
    ["Grelha Quadrada Inox Para Caixa Sifonada", 25.90, null, null],
    ["Grelha Redonda Inox Para Caixa Sifonada", 26.90, null, null],
    ["Grelha Quadrada Inox Para Caixa Sifonada Com Fecho", 41.90, null, null],
    ["Grelha Redonda Inox Para Caixa Sifonada Com Fecho", 44.90, null, null],
    ["Super Cano Branco Para Duchas e Chuveiros 30 cm", 28.90, null, "prod/super-cano-ducha.jpg", { sub: "Chuveiros" }],
    ["Chuveirinho Quick Com Suporte e Mangueira", 44.90, null, "prod/chuveirinho-quick.jpg", { sub: "Chuveiros" }],
    ["Cano Haste Para Chuveiro 30 cm Branco Gelo", 51.35, null, "prod/super-cano-ducha.jpg", { sub: "Chuveiros" }],
    ["Cano Haste Para Chuveiro 40 cm Branco Gelo", 50.30, null, "prod/super-cano-ducha.jpg", { sub: "Chuveiros" }],
    ["Tubos e Conexões PVC - Tigre", null, null, "p-tubos.jpg", { desc: "Linha completa para água fria, esgoto e conexões. Bitolas sob consulta." }]
  ],
  ferramentas: [
    ["Espátula Aço Cabo Plástico 6 cm - Atlas", 11.90, null, "prod/espatula-atlas.jpg"],
    ["Colher de Pedreiro 9 Polegadas Canto Reto", 27.90, null, "prod/colher-pedreiro.jpg"],
    ["Nivelador Para Cerâmica Plástico 1,5 mm - Atlas", 12.90, null, "prod/nivelador-ceramica.jpg"],
    ["Chave Fixa 10x11 mm Basic Corpo em Aço", 10.90, null, null],
    ["Lápis Para Carpinteiro - Tramontina", 3.15, null, "prod/lapis-carpinteiro.jpg"],
    ["Folha de Lixa D'água Grão 120 - Norton", 3.68, null, "prod/lixa-dagua-120.jpg"],
    ["Folha de Lixa Ferro Grão 50 Ref K246 - Norton", 5.78, null, null],
    ["Lâminas Reposição Para Estiletes 10 Unidades", 44.99, null, null],
    ["Escada Extensiva Alumínio 15x2 Degraus - Botafogo", 1409.90, null, null],
    ["Broca Para Aço 5/32\" - Tramontina", 8.40, null, null],
    ["Desempenadeira de Metal Retangular Chanfrada", 166.90, null, null],
    ["Disco de Corte Para Inox 178 x 1,6 x 22,23 mm", 8.64, null, null],
    ["Serra Copo Diamantada Com Haste 12 mm", 24.72, null, null],
    ["Espátula T de Aço Inox 30 cm - Pincéis Tigre", 66.00, null, null],
    ["Espátula de Aço Polido 76,2 mm 3 Polegadas", 20.90, null, null],
    ["Disco Abrasivo Telado 225 mm Grão 150 - Atlas", 8.90, null, null],
    ["Broca Titanium 10 mm - Starrett", 38.72, null, null],
    ["Soprador Térmico 2000W 220V - Atlas", 167.90, null, null],
    ["Serra Copo Diamantada Haste e Pino Guia", 125.90, null, null],
    ["Lixa D'água 120 - Atlas", 2.90, null, null]
  ],
  pisos: [
    ["Cerâmica Stela 46x46 Monteiro (A)", 23.90, 29.90, "oferta-stela-monteiro.jpg", { un: "m²", prebl: true, desc: "Efeito madeira em tom quente, para salas e quartos aconchegantes.", specs: [["Formato", "46x46 cm"], ["Classe", "A"], ["Acabamento", "Efeito madeira"]] }],
    ["Porcelanato Elizabeth 70x70 Paraná (A)", 79.90, 95.90, "oferta-elizabeth.jpg", { un: "m²", prebl: true, desc: "Branco marmorizado com veios dourados. Visual sofisticado de mármore.", specs: [["Formato", "70x70 cm"], ["Classe", "A"], ["Linha", "Paraná"]] }],
    ["Cerâmica Arielle 54x54 Riviera Branco (A)", 29.90, 36.90, "oferta-arielle.jpg", { un: "m²", prebl: true, desc: "Branco neutro e atemporal, que amplia e ilumina o ambiente.", specs: [["Formato", "54x54 cm"], ["Classe", "A"], ["Cor", "Riviera Branco"]] }]
  ],
  eletricos: [
    ["Luva Eletroduto Roscável 3/4 Polegada", 1.60, null, "prod/luva-eletroduto.jpg"],
    ["Caixa de Sobrepor Para 1 ou 2 Disjuntores", 12.90, null, "prod/caixa-disjuntor.jpg"],
    ["Placa 4\" x 2\" Com Suporte Cega Evidence - Fame", 8.00, null, "prod/placa-4x2.jpg"],
    ["Controlador / Variador de Velocidade Para Ventilador", 89.90, null, "prod/controlador-ventilador.jpg"],
    ["2 Tomadas 2P+T 10A/250V Com Placa", 28.90, null, "prod/2-tomadas.jpg"],
    ["Caixa de Proteção Embutir Com Tomada 2P+T 20A", 24.05, null, "prod/caixa-tomada-20a.jpg"],
    ["Prolongador Fêmea 2P+T 10A 250V Branco", 4.73, null, null],
    ["Quadro Sistema VDI 30x30 Embutir - Tigre", 298.50, null, null],
    ["Plugue 2P+T 20A/250V Cinza Sobrepor - Fame", 11.50, null, null],
    ["Cabo Flexível Antichamas 1,5 mm Branco Rolo", 169.90, 299.90, null],
    ["Fita Isolante 18 mm x 10 m Verde", 4.90, null, null],
    ["Disjuntor Monopolar 40A Curva C 1P", 18.90, null, null],
    ["Bomba D'água Periférica Bifásica 1/2 CV 220V", 159.90, null, null],
    ["Interruptor Simples 16A/250V e 2 Tomadas", 33.90, null, null],
    ["Tomada 2P+T 20A/250V Habitat Black - Fame", 22.90, null, null],
    ["2 Interruptores Simples 10A/250V Com Placa", 11.45, null, null],
    ["1 Interruptor Simples + 1 Tomada 2P+T 10A/250V", 12.90, null, null],
    ["Cabo Flexível Antichamas Flexsil 1,50 mm Rolo", 35.90, null, null],
    ["2 Interruptores Paralelos 10A - Mectronic", 15.23, null, null],
    ["Click Interruptor 1 Simples + 2 Tomadas 2P+T 20A", 14.60, null, null]
  ],
  basicos: [
    ["Graute Fluido 25kg - do Mestre", 45.90, null, "prod/graute.jpg"],
    ["Reboco Acabamento Grosso 25kg - do Mestre", 21.90, null, "prod/reboco.jpg"],
    ["Cumeeira Universal 1,10 m - Brasilit", 79.90, null, "prod/cumeeira.jpg"],
    ["Fixtudo Branco 400g - Quartzolit", 53.90, null, "prod/fixtudo.jpg"],
    ["Rejunte Epóxi Corda 1kg - Quartzolit", 193.90, null, "prod/rejunte-epoxi-corda.jpg"],
    ["Rejunte Epóxi Cinza Platina 1kg - Quartzolit", 193.90, null, "prod/rejunte-epoxi-cinza.jpg"],
    ["Rejunte Cerâmicas Flexível Bege 5kg - Quartzolit", 58.90, null, null],
    ["Rejunte Porcelanatos e Cerâmicas Bege 5kg", 89.90, null, null],
    ["Tecplus 1 3,6 L - Quartzolit", 49.90, null, null],
    ["Tecplus 1 1 L - Quartzolit", 22.00, null, null],
    ["Rejunte Siliconado Preto 1kg - do Mestre", 12.90, null, null],
    ["Rejunte Cerâmicas Flexível Marrom Café 1kg", 14.90, null, null],
    ["Argamassa AC II Cimentcola Externo Cinza", 52.90, null, null],
    ["Contrapiso Pronto 25kg - do Mestre", 22.90, null, null],
    ["Protetor de Armadura 1kg - Quartzolit", 108.90, null, null],
    ["Fita Veda Tudo Autoadesiva 10 cm x 10 m", 59.00, null, null],
    ["Telha de Policarbonato Translúcida 2,44 x 0,50 m", 70.25, null, null],
    ["Areia Saco 20kg - Granumix", 12.90, null, null],
    ["Argamassa Colante AC III-D Especial Para Fachada", 45.90, null, null],
    ["Fita Veda Tudo Blister Cinza - Dryko", 14.00, null, null]
  ],
  portas: [
    ["Porta Pronta Rocha", null, null, "p-porta.jpg", { desc: "Porta pronta com qualidade e estilo, agora no Canal. Medidas e acabamentos sob consulta." }],
    ["Porta Sanfonada de PVC Marrom 72 cm x 210 cm", 146.90, null, null],
    ["Porta Sanfonada de PVC Cinza 84 cm x 210 cm", 203.18, null, null],
    ["Porta Sanfonada de PVC Bege 96 cm x 210 cm", 185.75, null, null],
    ["Porta Sanfonada de PVC Branca 60 cm x 210 cm", 138.60, null, null],
    ["Porta Sanfonada PVC 0,80 x 2,10 Branca - Fortlev", 139.90, null, null],
    ["Porta de Giro Veneziana 60x210 Lado Esquerdo", 549.90, null, null],
    ["Janela Basculante de Alumínio Branco Vidro Liso", 129.90, null, null],
    ["Janela Basculante de Alumínio Natural", 75.90, null, null],
    ["Janela Basculante de Alumínio Vidro Canelado", 109.90, null, null],
    ["Janela de Correr de Alumínio 2 Folhas", 385.00, null, null],
    ["Janela de Correr de Alumínio 2 Folhas Vidro Liso", 304.90, null, null],
    ["Janela de Correr de Alumínio 2 Folhas Vidro Canelado", 189.90, null, null],
    ["Fixador de Porta Magnético Cromado", 83.90, null, null],
    ["Número Para Casa Adesivo 8 ACM - Atlas", 21.90, null, null],
    ["Número Para Casa Adesivo 1 ACM - Atlas", 23.90, null, null],
    ["Número Para Casa Adesivo 5 ACM - Atlas", 23.90, null, null],
    ["Número 0 em ABS 39 mm Cromado - Bemfixa", 17.50, null, null],
    ["Número 3 em ABS 39 mm Cromado - Bemfixa", 17.50, null, null],
    ["Número 5 em ABS 39 mm Cromado - Bemfixa", 17.50, null, null],
    ["Número 2 em ABS 145 mm Cromado - Bemfixa", 39.90, null, null]
  ],
  fechaduras: [
    ["Corrente Soldada e Zincada 3 mm x 1 m", 13.55, null, "prod/corrente.jpg"],
    ["Corrente Soldada e Zincada 4 mm x 1 m", 24.05, null, "prod/corrente.jpg"],
    ["Corrente Soldada e Zincada 5 mm x 1 m", 35.60, null, "prod/corrente.jpg"],
    ["Corrente Soldada e Zincada 6 mm x 1 m", 39.80, null, "prod/corrente.jpg"],
    ["Corrente Soldada e Zincada 8 mm x 1 m", 85.05, null, "prod/corrente.jpg"]
  ],
  cadeados: [
    ["Cadeado Latão 25 mm Preto - Pado", 28.25, null, "prod/cadeado-preto-25.jpg"],
    ["Cadeado Tradicional Latão 20 mm - Pado", 24.05, null, "prod/cadeado-20.jpg"],
    ["Cadeado Tradicional Latão 25 mm - Pado", 28.25, null, "prod/cadeado-25.jpg"],
    ["Cadeado Tradicional Latão 30 mm - Pado", 33.50, null, "prod/cadeado-30.jpg"],
    ["Cadeado Tradicional Latão 35 mm - Pado", 44.10, null, "prod/cadeado-35.jpg"],
    ["Cadeado Tradicional Latão 40 mm - Pado", 49.25, null, "prod/cadeado-40.jpg"],
    ["Cadeado Tradicional Latão 45 mm - Pado", 59.75, null, "prod/cadeado-40.jpg"],
    ["Cadeado Tradicional Latão 50 mm - Pado", 69.20, null, "prod/cadeado-40.jpg"],
    ["Cadeado Tradicional Latão 60 mm - Pado", 115.40, null, "prod/cadeado-40.jpg"]
  ],
  epi: [
    ["Bota PVC Cano Médio Safety Boots Preta", 83.90, null, null],
    ["Bota de Couro Elástico Combat Preta", 83.90, null, null],
    ["Bota com Elástico Bico Plástico Couro Relax Preta", 119.90, null, null],
    ["Bota com Elástico Bico Plástico Couro Relax", 118.90, null, null],
    ["Bota PVC Safety Boots Cano Alto Branca nº 42", null, null, null, { esgotado: true }],
    ["Tênis Feminino Branco nº 38", 105.90, null, null],
    ["Óculos de Segurança Leopardo", 9.35, null, null],
    ["Luva de Segurança PU - Kalipso", 6.20, null, null],
    ["Capa de Chuva PVC Com Capuz Amarela", 29.90, 42.90, null],
    ["Pedestal de Sinalização Plástico Preto e Amarelo", 59.90, null, null],
    ["Fita Antiderrapante Amarela 50 mm x 5 m - Adere", 46.90, null, null],
    ["Fita Antiderrapante Zebrada Preta e Amarela 50 mm x 5 m", 54.90, null, null],
    ["Fita Para Demarcação de Área Zebrada Preta e Amarela", 29.90, null, null],
    ["Fita de Demarcação de Solo Preta 50 mm x 15 m - Adere", 39.90, 46.90, null],
    ["Fita de Demarcação de Solo Verde 50 mm x 15 m - Adere", 26.90, null, null],
    ["Fita de Demarcação de Solo Azul 50 mm x 15 m - Adere", 27.90, null, null]
  ],
  automotivo: [
    ["Graxa Chassis 2 500g - Lubri Motors", 27.20, null, "prod/graxa-chassis.jpg"],
    ["Grafite Aerossol 200 ml - Allchem Química", 35.86, null, "prod/grafite-aerossol.jpg"],
    ["Cera Pasta Tradicional Com Carnaúba 200g - Proauto", 25.90, null, "prod/cera-pasta.jpg"],
    ["Lava Autos Com Cera Carnaúba 500 ml - Proauto", 21.90, null, "prod/lava-autos.jpg"],
    ["Massa de Polir Nº 2 Base D'água 500g - Proauto", 39.90, null, "prod/massa-polir.jpg"],
    ["Odorizador Breeze Gel Carro Novo 60g - Proauto", 5.90, 10.90, "prod/breeze-carro-novo.jpg"],
    ["Odorizador Breeze Lavanda 60g - Proauto", 15.90, null, null],
    ["Odorizador Breeze Morango 60g - Proauto", 8.90, null, null],
    ["Limpa Pneu Líquido 1 L - Valença", 11.90, null, null],
    ["Graxa Azul Grasa 62 1kg - YPF", 104.90, null, null],
    ["Aspirador de Pó Portátil Para Carros 12V - Tramontina", 115.40, null, null],
    ["Espuma Mágica Limpador Instantâneo a Seco", null, null, null, { esgotado: true }]
  ],
  tintas: [
    ["Tinta Acrílica Coral Rende Muito", null, null, "u-tintas.jpg", { desc: "Alto rendimento e ótima cobertura para paredes internas. Cores e embalagens sob consulta." }],
    ["Tinta Suvinil Rende e Cobre Muito", null, null, "u-parede-verde.jpg", { desc: "Cobertura que rende: menos demãos, mais economia. Cores sob consulta." }],
    ["Esmalte Sintético Novacor - Sherwin-Williams", null, null, "p-novacor.jpg", { desc: "Renove portas e metais com proteção e brilho." }]
  ]
};

/* ---------- monta a lista final de produtos ---------- */
const slug = s => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const P = [];
for (const [cat, list] of Object.entries(RAW)) {
  list.forEach(([nome, preco, de, img, o = {}], i) => {
    const k = nome.lastIndexOf(" - ");
    P.push({
      id: slug(nome), nome, cat, preco, de, img,
      marca: o.marca || (k > 0 ? nome.slice(k + 3).trim() : null),
      un: o.un || "un", esgotado: !!o.esgotado, prebl: !!o.prebl,
      desc: o.desc || null, specs: o.specs || null, sub: o.sub || null, ordem: i
    });
  });
}
