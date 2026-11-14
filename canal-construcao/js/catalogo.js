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
  { id: "hidraulica",   nome: "Tubos e Conexões",        img: "p-tubos.jpg",       ic: "pipe",  sub: "PVC e Tigre" },
  { id: "metais",       nome: "Metais",                  img: "p-torneira.jpg",    ic: "drop",  sub: "Registros e acessórios" },
  { id: "loucas",       nome: "Louças",                  img: "p-banheiro.jpg",    ic: "drop",  sub: "Bacias e cubas" },
  { id: "banheiro",     nome: "Móveis para Banheiro",    img: "u-banheiro.jpg",    ic: "drop",  sub: "Gabinetes e espelhos" },
  { id: "pvc",          nome: "PVC",                     img: "u-obra.jpg",        ic: "pipe",  sub: "Forros e perfis" },
  { id: "iluminacao",   nome: "Iluminação",              img: "p-pendente.jpg",    ic: "bulb",  sub: "Luminárias e lâmpadas" },
  { id: "automotivo",   nome: "Automotivo",              img: "prod/cera-pasta.jpg", ic: "car", sub: "Cera, graxa, odorizador", light: true },
  { id: "limpeza",      nome: "Limpeza",                 img: "p-limpeza.jpg",     ic: "spray", sub: "Pós-obra e casa" },
  { id: "lar",          nome: "Utilidades do Lar",       img: "u-cozinha.jpg",     ic: "home",  sub: "Casa organizada" }
];

/* Produtos.
   Formato: [nome, preço (null = sob consulta), preço antigo (ou null), imagem (ou null), opções]
   opções: { un: "m²", esgotado: true, prebl: true, desc: "..." }
   Preços lidos do site canalconstrucao.com.br em 14/11/2026 — confira antes de publicar. */
const RAW = {
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
  ],
  metais: [
    ["Adaptador e Acessórios - Blukit", null, null, "p-blukit.jpg", { desc: "Adaptadores, registros e acessórios práticos para instalação." }]
  ],
  hidraulica: [
    ["Tubos e Conexões PVC - Tigre", null, null, "p-tubos.jpg", { desc: "Linha completa para água fria, esgoto e conexões. Bitolas sob consulta." }]
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
      desc: o.desc || null, specs: o.specs || null, ordem: i
    });
  });
}
