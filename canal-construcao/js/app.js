/* =====================================================================
   CANAL DA CONSTRUÇÃO — APLICAÇÃO (rotas, loja, sacola, conta, checkout)
   ===================================================================== */
"use strict";

/* ---------- utils ---------- */
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const brl = v => v.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
const waLink = m => `https://wa.me/${LOJA.whatsapp}?text=${encodeURIComponent(m)}`;
const store = { get(k, d) { try { const v = JSON.parse(localStorage.getItem(k)); return v ?? d } catch { return d } }, set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)) } catch { } } };
const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const norm = s => String(s).normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/['\u2019`]/g, "").toLowerCase();
const byId = id => P.find(p => p.id === id);
const catById = id => CATS.find(c => c.id === id);
const off = p => p.de && p.preco ? Math.floor((1 - p.preco / p.de) * 100) : 0;
const parcelas = v => Math.max(1, Math.min(LOJA.parcelasMax, Math.floor(v / LOJA.parcelaMin)));
const parcTxt = p => { if (p.preco == null) return ""; const n = parcelas(p.preco); return `ou ${n}x de ${brl(p.preco / n)} sem juros` };
const shortName = p => p.marca ? p.nome.slice(0, p.nome.lastIndexOf(" - ")) : p.nome;
const icoFor = p => (catById(p.cat) || {}).ic || "box";
const canBuy = p => !p.esgotado;
const pad = n => String(n).padStart(2, "0");

let cart = store.get("cc_cart", []).filter(c => byId(c.id));
let favs = new Set(store.get("cc_favs", []).filter(byId));
let user = store.get("cc_user", null);
let orders = store.get("cc_orders", []);
let seen = store.get("cc_seen", []).filter(byId);

/* ---------- render helpers ---------- */
function media(p, cls = "") {
  return p.img
    ? `<img class="${cls}" src="img/${p.img}" alt="${esc(p.nome)}" loading="lazy">`
    : `<div class="ph-ico ${cls}" role="img" aria-label="${esc(p.nome)}"><svg><use href="#c-${icoFor(p)}"/></svg><span>${esc(p.marca || (catById(p.cat) || {}).nome || "")}</span></div>`;
}
function priceBlock(p, big) {
  if (p.esgotado) return `<div class="price"><span class="sold">Produto esgotado</span></div>`;
  if (p.preco == null) return `<div class="price"><span class="q">Preço sob consulta</span></div>`;
  return `<div class="price">${p.de ? `<s>${brl(p.de)}</s>` : ""}<b class="${p.de ? "r" : ""}">${brl(p.preco)}</b>${p.un !== "un" ? `<span class="u">/${p.un}</span>` : ""}</div><div class="parc">${parcTxt(p)}</div>`;
}
function card(p, i = 0) {
  const o = off(p), defQ = p.un === "m²" ? 10 : 1;
  return `<article class="pc" style="animation-delay:${Math.min(i, 12) * 35}ms"><div class="mwrap">
    <a class="media" href="#/p/${p.id}" aria-label="${esc(p.nome)}">${media(p)}
      <span class="tags">${p.prebl ? `<span class="tg blk">PRÉ-BLACK</span>` : ""}${o ? `<span class="tg red">-${o}%</span>` : ""}${p.preco == null && !p.esgotado ? `<span class="tg">Orçamento</span>` : ""}${p.esgotado ? `<span class="tg">Esgotado</span>` : ""}</span>
    </a>
    <button class="fav ${favs.has(p.id) ? "on" : ""}" data-fav="${p.id}" aria-label="Favoritar"><svg><use href="#i-heart"/></svg></button>
    <button class="qv" data-quick="${p.id}">Espiar</button></div>
    <div class="body">
      <span class="brandl">${esc(p.marca || (catById(p.cat) || {}).nome)}</span>
      <a href="#/p/${p.id}" class="nm">${esc(shortName(p))}</a>
      ${priceBlock(p)}
      ${canBuy(p) ? `<div class="buy"><span class="step sm"><button data-st="-1" aria-label="Diminuir">−</button><input value="${defQ}" inputmode="numeric" aria-label="Quantidade"><button data-st="1" aria-label="Aumentar">+</button></span><button class="add" data-add="${p.id}" aria-label="Adicionar ${esc(p.nome)} à sacola"><svg class="ico"><use href="#i-bag"/></svg><span>${p.preco == null ? "Orçar" : "Adicionar"}</span></button></div>`
      : `<a class="add ghost" href="${waLink(`Olá! Quando volta o produto: ${p.nome}?`)}" target="_blank" rel="noopener">Avise-me</a>`}
    </div></article>`;
}
function shelf(title, list, more, sub) {
  if (!list.length) return "";
  return `<section class="shelf rv"><div class="shelf-h"><div><h3>${title}</h3>${sub ? `<p>${sub}</p>` : ""}</div><div class="shelf-c">${more ? `<a class="lnk" href="${more}">Ver tudo</a>` : ""}<button class="sa" data-sh="-1" aria-label="Anterior"><svg class="ico"><use href="#i-arrow"/></svg></button><button class="sa" data-sh="1" aria-label="Próximo"><svg class="ico"><use href="#i-arrow"/></svg></button></div></div><div class="track">${list.map(card).join("")}</div></section>`;
}
const crumbs = items => `<nav class="bc" aria-label="Você está em"><a href="#/">Início</a>${items.map(([t, h]) => h ? `<span>/</span><a href="${h}">${esc(t)}</a>` : `<span>/</span><b>${esc(t)}</b>`).join("")}</nav>`;
const countCat = id => id === "ofertas" ? P.filter(p => p.de).length : P.filter(p => p.cat === id).length;

/* ---------- router ---------- */
const VIEW = $("#view");
let catState = null;
function route() {
  const h = decodeURIComponent(location.hash.replace(/^#/, "") || "/");
  const [, a = "", b = "", c = ""] = h.split("/");
  closeLayer(); if (ckOpen()) closeCk(); closeMega(); hideSugg();
  let title = "Canal da Construção · Loja Online";
  if (!a) viewHome();
  else if (a === "c") title = viewList({ cat: b, page: +c || 1 }) || title;
  else if (a === "busca") title = viewList({ q: b, page: +c || 1 }) || title;
  else if (a === "p") title = viewProduct(b) || title;
  else if (a === "i") title = viewInst(b) || title;
  else viewNotFound();
  document.title = title;
  $$(".bnav [data-nav]").forEach(x => x.classList.toggle("on", (x.dataset.nav === "home" && !a) || (x.dataset.nav === "deps" && a === "c")));
  $("#q").value = a === "busca" ? b : "";
  if (!route.keepScroll) scrollTo({ top: 0, behavior: "instant" }); route.keepScroll = false;
  wireWa(VIEW); observeReveal();
}
addEventListener("hashchange", route);
const go = h => { if (location.hash === h) route(); else location.hash = h };

/* ---------- views ---------- */
function viewHome() {
  VIEW.innerHTML = $("#tpl-home").innerHTML;
  $("#deps").innerHTML = CATS.slice(0, 12).map(c => `<a class="dep rv ${c.light ? "light" : ""}" href="#/c/${c.id}"><img src="img/${c.img}" alt="" loading="lazy"><span class="arr"><svg class="ico"><use href="#i-arrow"/></svg></span><b>${c.nome}</b><small>${countCat(c.id) ? countCat(c.id) + " produtos" : c.sub}</small></a>`).join("");
  $("#allDeps").innerHTML = CATS.map(c => `<a href="#/c/${c.id}" class="dchip"><svg><use href="#c-${c.ic}"/></svg>${c.nome}</a>`).join("");
  $("#bfCards").innerHTML = P.filter(p => p.prebl).map(p => `<a class="bfc" href="#/p/${p.id}"><div class="im"><img src="img/${p.img}" alt="" loading="lazy"><span class="chip-off">-${off(p)}%</span></div><div class="tx"><small>${esc(p.nome.split(" ")[0].toUpperCase())}</small><h4>${esc(p.nome.split(" ")[1])}</h4><div class="pr"><b>${brl(p.preco)}</b><s>${brl(p.de)}</s></div></div></a>`).join("");
  const by = id => P.filter(p => p.cat === id && canBuy(p));
  $("#shelves").innerHTML =
    shelf("Ofertas que acabam rápido", P.filter(p => p.de), "#/c/ofertas", "Descontos reais em todos os departamentos") +
    shelf("Básicos para Construção", by("basicos"), "#/c/basicos", "Quartzolit, do Mestre, Brasilit e mais") +
    shelf("Materiais Elétricos", by("eletricos"), "#/c/eletricos", "Tomadas, interruptores, cabos e disjuntores") +
    shelf("Hidráulica", by("hidraulica"), "#/c/hidraulica", "Caixas d'água Fortlev, grelhas Tigre e chuveiros") +
    shelf("Louças e Metais", [...by("loucas"), ...by("metais")], "#/c/loucas", "Bacias, cubas, pias e torneiras") +
    shelf("Iluminação", by("iluminacao"), "#/c/iluminacao", "Lâmpadas, painéis e refletores Avant") +
    shelf("Ferramentas", by("ferramentas"), "#/c/ferramentas", "Atlas, Tramontina, Norton") +
    shelf("Limpeza", by("limpeza"), "#/c/limpeza", "Desincrustantes, vaselina e pós-obra") +
    shelf("Portas e Janelas", by("portas"), "#/c/portas") +
    shelf("EPI", by("epi"), "#/c/epi", "Segurança para quem está na obra") +
    shelf("Cadeados e Correntes", [...by("cadeados"), ...by("fechaduras")], "#/c/cadeados") +
    shelf("Automotivo", by("automotivo"), "#/c/automotivo");
  $("#storesHome").innerHTML = storesHTML();
  $("#hero-elz").setAttribute("href", "#/p/" + (byId("porcelanato-elizabeth-70x70-parana-a") || P[0]).id);
  tick();
}

const PRICE_R = [["ate25", "Até R$ 25", 0, 25], ["25-50", "R$ 25 a R$ 50", 25, 50], ["50-100", "R$ 50 a R$ 100", 50, 100], ["100-200", "R$ 100 a R$ 200", 100, 200], ["200", "Acima de R$ 200", 200, 1e9]];
const PER_PAGE = 12;
function listFor(st) {
  let list = st.q
    ? (() => { const t = norm(st.q).split(/\s+/).filter(Boolean); return P.filter(p => { const h = norm(`${p.nome} ${p.marca || ""} ${(catById(p.cat) || {}).nome}`); return t.every(w => h.includes(w)) }) })()
    : st.cat === "ofertas" ? P.filter(p => p.de) : P.filter(p => p.cat === st.cat);
  return list;
}
function applyFilters(list, st) {
  let l = list.filter(p =>
    (!st.sub || p.sub === st.sub) && (!st.brands.size || st.brands.has(p.marca || "—")) &&
    (!st.price || (() => { const r = PRICE_R.find(x => x[0] === st.price); return p.preco != null && p.preco >= r[2] && p.preco < r[3] })()) &&
    (!st.oferta || p.de) && (!st.disp || (canBuy(p) && p.preco != null)));
  const s = st.sort;
  if (s === "low") l.sort((a, b) => (a.preco ?? 1e9) - (b.preco ?? 1e9));
  if (s === "high") l.sort((a, b) => (b.preco ?? -1) - (a.preco ?? -1));
  if (s === "off") l.sort((a, b) => off(b) - off(a));
  if (s === "az") l.sort((a, b) => a.nome.localeCompare(b.nome));
  if (s === "rel") l.sort((a, b) => (a.esgotado - b.esgotado) || ((a.preco == null) - (b.preco == null)) || (!!b.img - !!a.img) || a.ordem - b.ordem);
  return l;
}
function filtersHTML(base, st, g = "") {
  const brands = [...new Set(base.map(p => p.marca || "—"))].sort((a, b) => a === "—" ? 1 : b === "—" ? -1 : a.localeCompare(b));
  const cnt = m => base.filter(p => (p.marca || "—") === m).length;
  const subs = [...new Set(base.map(p => p.sub).filter(Boolean))];
  return `<div class="flt">
    ${subs.length ? `<fieldset><legend>Subcategoria</legend><label class="fck"><input type="radio" name="fs${g}" data-fs="" ${!st.sub ? "checked" : ""}><span>Todas</span><small>${base.length}</small></label>${subs.map(x => `<label class="fck"><input type="radio" name="fs${g}" data-fs="${esc(x)}" ${st.sub === x ? "checked" : ""}><span>${esc(x)}</span><small>${base.filter(p => p.sub === x).length}</small></label>`).join("")}</fieldset>` : ""}
    ${brands.length > 1 ? `<fieldset><legend>Marca</legend>${brands.map(m => `<label class="fck"><input type="checkbox" data-fb="${esc(m)}" ${st.brands.has(m) ? "checked" : ""}><span>${m === "—" ? "Outras" : esc(m)}</span><small>${cnt(m)}</small></label>`).join("")}</fieldset>` : ""}
    <fieldset><legend>Preço</legend>${PRICE_R.map(r => `<label class="fck"><input type="radio" name="fp${g}" data-fp="${r[0]}" ${st.price === r[0] ? "checked" : ""}><span>${r[1]}</span></label>`).join("")}${st.price ? `<button class="lnk" data-fp="">Limpar preço</button>` : ""}</fieldset>
    <fieldset><legend>Mostrar</legend><label class="sw"><input type="checkbox" data-fo ${st.oferta ? "checked" : ""}><span>Só ofertas</span></label><label class="sw"><input type="checkbox" data-fd ${st.disp ? "checked" : ""}><span>Com preço e em estoque</span></label></fieldset>
  </div>`;
}
function viewList({ cat, q, page }) {
  const key = q ? "q:" + q : "c:" + cat;
  if (!catState || catState.key !== key) catState = { key, cat, q, brands: new Set(), sub: "", price: "", oferta: false, disp: false, sort: "rel", page: 1 };
  catState.page = page;
  const c = cat === "ofertas" ? { id: "ofertas", nome: "Ofertas", sub: "Descontos reais em todos os departamentos" } : catById(cat);
  if (!q && !c) return viewNotFound();
  renderList();
  return q ? `Busca: ${q} · Canal da Construção` : `${c.nome} · Canal da Construção`;
}
function renderList() {
  const st = catState, base = listFor(st), list = applyFilters(base, st);
  const pages = Math.max(1, Math.ceil(list.length / PER_PAGE)); st.page = Math.min(st.page, pages);
  const slice = list.slice((st.page - 1) * PER_PAGE, st.page * PER_PAGE);
  const c = st.q ? null : st.cat === "ofertas" ? { nome: "Ofertas", sub: "Descontos reais em todos os departamentos" } : catById(st.cat);
  const title = st.q ? `Resultados para “${esc(st.q)}”` : esc(c.nome);
  const active = st.brands.size + (st.price ? 1 : 0) + (st.sub ? 1 : 0) + st.oferta + st.disp;
  const hrefP = n => st.q ? `#/busca/${encodeURIComponent(st.q)}/${n}` : `#/c/${st.cat}/${n}`;
  const empty = !base.length;
  VIEW.innerHTML = `<div class="wrap page">
    ${crumbs(st.q ? [["Busca"]] : [[c.nome]])}
    <header class="list-h"><div><h1>${title}</h1><p>${base.length} ${base.length === 1 ? "produto" : "produtos"}${c && c.sub && !st.q ? " · " + esc(c.sub) : ""}</p></div>
      ${empty ? "" : `<div class="list-tools"><button class="btn btn-line btn-sm mob-only" data-open="flt"><svg class="ico"><use href="#i-filter"/></svg>Filtrar${active ? ` (${active})` : ""}</button>
      <label class="sort"><span>Ordenar</span><select id="sort"><option value="rel">Relevância</option><option value="low">Menor preço</option><option value="high">Maior preço</option><option value="off">Maior desconto</option><option value="az">A–Z</option></select></label></div>`}
    </header>
    ${!st.q && !empty ? `<div class="subcats">${[...new Set(base.map(p => p.sub).filter(Boolean))].map(x => `<button class="dchip sm ${st.sub === x ? "on" : ""}" data-fs="${esc(x)}" data-pick><svg><use href="#c-${c.ic || "box"}"/></svg>${esc(x)}</button>`).join("")}${CATS.filter(x => x.id !== st.cat && countCat(x.id)).slice(0, 10).map(x => `<a href="#/c/${x.id}" class="dchip sm"><svg><use href="#c-${x.ic}"/></svg>${x.nome}</a>`).join("")}</div>` : ""}
    ${empty ? emptyList(st, c) : `<div class="list-l">
      <aside class="list-side">${filtersHTML(base, st)}</aside>
      <div>
        ${active ? `<div class="chips-on">${st.sub ? `<button data-fs="" class="on-chip">${esc(st.sub)} ✕</button>` : ""}${[...st.brands].map(m => `<button data-fb="${esc(m)}" class="on-chip">${m === "—" ? "Outras" : esc(m)} ✕</button>`).join("")}${st.price ? `<button data-fp="" class="on-chip">${PRICE_R.find(r => r[0] === st.price)[1]} ✕</button>` : ""}${st.oferta ? `<button data-fo class="on-chip">Só ofertas ✕</button>` : ""}${st.disp ? `<button data-fd class="on-chip">Em estoque ✕</button>` : ""}<button class="lnk" data-fclear>Limpar tudo</button></div>` : ""}
        <p class="shown">Mostrando ${slice.length ? (st.page - 1) * PER_PAGE + 1 : 0}–${(st.page - 1) * PER_PAGE + slice.length} de ${list.length}</p>
        <div class="grid">${slice.length ? slice.map(card).join("") : `<div class="empty"><h3>Nenhum produto com esses filtros</h3><p>Tente remover algum filtro.</p><button class="btn btn-ink btn-sm" data-fclear>Limpar filtros</button></div>`}</div>
        ${pages > 1 ? `<nav class="pager" aria-label="Páginas"><a class="pg ${st.page === 1 ? "dis" : ""}" href="${hrefP(Math.max(1, st.page - 1))}" aria-label="Anterior">‹</a>${Array.from({ length: pages }, (_, i) => i + 1).map(n => `<a class="pg ${n === st.page ? "on" : ""}" href="${hrefP(n)}">${n}</a>`).join("")}<a class="pg ${st.page === pages ? "dis" : ""}" href="${hrefP(Math.min(pages, st.page + 1))}" aria-label="Próxima">›</a></nav>` : ""}
      </div></div>`}
  </div>`;
  const so = $("#sort"); if (so) so.value = st.sort;
  $("#fltBody").innerHTML = empty ? "" : filtersHTML(base, st, "m") + `<button class="btn btn-ink btn-block" data-close style="margin-top:14px">Ver ${list.length} produtos</button>`;
  wireWa(VIEW); observeReveal();
}
function emptyList(st, c) {
  if (st.q) {
    const sugg = P.filter(p => canBuy(p) && p.de).slice(0, 4);
    return `<div class="empty big"><img src="img/mascote.png" alt=""><h3>Não achei “${esc(st.q)}” no site… ainda!</h3><p>São mais de 20 mil itens nas lojas. Pergunta pra gente que a gente encontra.</p><a class="btn btn-wa" href="${waLink(`Olá! Vocês têm ${st.q}?`)}" target="_blank" rel="noopener"><svg class="ico"><use href="#i-wa"/></svg> Perguntar no WhatsApp</a></div>${shelf("Que tal aproveitar estas ofertas?", sugg)}`;
  }
  return `<div class="empty big"><img src="img/mascote.png" alt=""><h3>${esc(c.nome)} chegando no site</h3><p>Os produtos deste departamento estão nas lojas, e estamos colocando tudo online. Enquanto isso, a gente faz seu orçamento pelo WhatsApp.</p><a class="btn btn-wa" href="${waLink(`Olá! Quero ver produtos de ${c.nome}.`)}" target="_blank" rel="noopener"><svg class="ico"><use href="#i-wa"/></svg> Pedir orçamento de ${esc(c.nome)}</a></div>
  <div class="all-deps">${CATS.filter(x => countCat(x.id)).map(x => `<a href="#/c/${x.id}" class="dchip"><svg><use href="#c-${x.ic}"/></svg>${x.nome}<small>${countCat(x.id)}</small></a>`).join("")}</div>`;
}

function viewProduct(id) {
  const p = byId(id); if (!p) return viewNotFound();
  seen = [id, ...seen.filter(x => x !== id)].slice(0, 12); store.set("cc_seen", seen);
  const c = catById(p.cat), o = off(p), m2 = p.un === "m²";
  const specs = p.specs || [];
  const allSpecs = [["Marca", p.marca || "—"], ["Departamento", c.nome], ["Vendido por", p.un === "m²" ? "metro quadrado (m²)" : "unidade"], ...specs];
  const rel = P.filter(x => x.cat === p.cat && x.id !== p.id && canBuy(x)).slice(0, 10);
  const rec = seen.filter(x => x !== id).map(byId).slice(0, 10);
  VIEW.innerHTML = `<div class="wrap page">
    ${crumbs([[c.nome, "#/c/" + c.id], [shortName(p)]])}
    <div class="pdp">
      <div class="gal"><div class="gal-main ${p.img ? "zoom" : ""}">${media(p)}${o ? `<span class="chip-off">-${o}%</span>` : ""}${p.prebl ? `<span class="tg blk pre">PRÉ-BLACK</span>` : ""}</div>
        <p class="gal-note">${p.img && /^(oferta|u-|p-)/.test(p.img) ? "Imagem meramente ilustrativa." : "Imagem ilustrativa. Confira detalhes com o atendimento."}</p></div>
      <div class="buybox">
        <a class="brandl" href="#/busca/${encodeURIComponent(p.marca || c.nome)}">${esc(p.marca || c.nome)}</a>
        <h1>${esc(p.nome)}</h1>
        <div class="pdp-price">${priceBlock(p, true)}${o ? `<span class="save">Você economiza ${brl((p.de - p.preco))}${m2 ? "/m²" : ""}</span>` : ""}</div>
        ${p.desc ? `<p class="desc">${esc(p.desc)}</p>` : ""}
        ${canBuy(p) ? `
        <div class="calc">${m2 ? `<div class="lb">📐 Área do ambiente <span class="step"><button data-pq="-1" aria-label="Diminuir">−</button><input id="pd-n" value="20" inputmode="decimal" aria-label="Área em m²"><span class="un">m²</span><button data-pq="1" aria-label="Aumentar">+</button></span></div><label class="chk"><input type="checkbox" id="pd-mg" checked> +10% de margem para recortes</label>` : `<div class="lb">Quantidade <span class="step"><button data-pq="-1" aria-label="Diminuir">−</button><input id="pd-n" value="1" inputmode="numeric" aria-label="Quantidade"><span class="un">${p.un}</span><button data-pq="1" aria-label="Aumentar">+</button></span></div>`}<div class="res" id="pd-res"></div></div>
        <div class="pdp-actions"><button class="btn btn-ink" data-pd-add="${p.id}"><svg class="ico"><use href="#i-bag"/></svg>${p.preco == null ? "Adicionar ao orçamento" : "Adicionar à sacola"}</button><button class="btn btn-y" data-pd-buy="${p.id}">Comprar agora</button><button class="btn btn-line icon fav-pd ${favs.has(p.id) ? "on" : ""}" data-fav="${p.id}" aria-label="Favoritar"><svg class="ico"><use href="#i-heart"/></svg></button></div>`
      : `<div class="calc"><b>Produto esgotado</b><p class="note" style="margin:6px 0 0">Avisamos pelo WhatsApp assim que chegar.</p></div><div class="pdp-actions"><a class="btn btn-wa" href="${waLink(`Olá! Quando volta o produto: ${p.nome}?`)}" target="_blank" rel="noopener"><svg class="ico"><use href="#i-wa"/></svg> Avise-me quando chegar</a></div>`}
        <ul class="perks">
          <li><svg class="ico"><use href="#i-store"/></svg><span><b>Retire grátis na loja</b>Arruda ou Boa Viagem</span></li>
          <li><svg class="ico"><use href="#i-truck"/></svg><span><b>Entrega no Recife e região</b>Frete combinado com o atendente</span></li>
          <li><svg class="ico"><use href="#i-lock"/></svg><span><b>Compra segura</b>Você só paga depois da confirmação</span></li>
        </ul>
        <div class="pdp-links"><a class="lnk" href="${waLink(`Olá! Tenho uma dúvida sobre: ${p.nome}`)}" target="_blank" rel="noopener">Tirar dúvida no WhatsApp</a><button class="lnk" data-share="${p.id}">Compartilhar</button></div>
      </div>
    </div>
    <section class="pdp-info"><div class="tabs-x"><h2>Detalhes do produto</h2></div>
      <div class="pdp-grid"><div><h3>Descrição</h3><p>${esc(p.desc || `${p.nome}. Produto do departamento ${c.nome}${p.marca ? `, marca ${p.marca}` : ""}, disponível nas lojas do Canal da Construção no Recife.`)}</p><p>Precisa de ajuda para escolher ou calcular a quantidade? Fale com nosso time pelo WhatsApp ${LOJA.whatsappTxt}.</p></div>
      <div><h3>Especificações</h3><dl class="specs-t">${allSpecs.map(([k, v]) => `<div><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join("")}</dl></div></div></section>
    ${shelf("Quem viu também comprou", rel, "#/c/" + c.id)}
    ${shelf("Vistos recentemente", rec)}
  </div>`;
  if (canBuy(p)) calcPD(p);
  return `${p.nome} · Canal da Construção`;
}
function pdQty(p) { const v = Math.max(1, parseFloat(String($("#pd-n").value).replace(",", ".")) || 1); return p.un === "m²" ? Math.ceil(v * ($("#pd-mg").checked ? 1.1 : 1)) : Math.round(v) }
function calcPD(p) {
  const q = pdQty(p), r = $("#pd-res"); if (!r) return;
  if (p.preco == null) { r.innerHTML = `Você vai pedir <b>${q} ${p.un}</b>. O valor é confirmado pelo atendente.`; return }
  const t = q * p.preco, n = parcelas(t);
  r.innerHTML = `${p.un === "m²" ? `Você precisa de <b>${q} m²</b> → ` : ""}Total <b>${brl(t)}</b> <span class="parc">ou ${n}x de ${brl(t / n)} sem juros</span>${p.de ? ` · <span class="eco">economia de ${brl(q * (p.de - p.preco))}</span>` : ""}`;
}

const INST = {
  "quem-somos": ["Quem somos", () => `<p class="lead">O <b>Canal da Construção &amp; Condomínios</b> é o canal dos preços baixos no Recife: mais de 20.000 itens para construir e reformar, com lojas no Arruda e em Boa Viagem.</p>
    <p>Atendemos quem está construindo a primeira casa, quem está reformando um cômodo, profissionais de obra e condomínios. Trabalhamos com marcas como Quartzolit, do Mestre, Tigre, Coral, Suvinil, Sherwin-Williams, Iquine, Fame, Pado e Tramontina.</p>
    <div class="inst-cards"><div><b>+20 mil</b><span>itens para construir e reformar</span></div><div><b>2 lojas</b><span>Arruda e Boa Viagem</span></div><div><b>29,4 mil</b><span>seguidores no Instagram</span></div></div>
    <p>Nosso jeito é simples: preço justo, atendimento de quem entende de obra e tudo em um só lugar.</p>`],
  "lojas": ["Nossas lojas", () => `<p class="lead">Venha ver os produtos de perto, tirar dúvidas com o vendedor e sair com o material.</p><div class="stores">${storesHTML()}</div>`],
  "contato": ["Fale conosco", () => `<div class="contact-g">
    <a class="cc" href="${waLink("Olá! Vim pelo site.")}" target="_blank" rel="noopener"><svg class="ico"><use href="#i-wa"/></svg><b>WhatsApp</b><span>${LOJA.whatsappTxt}</span></a>
    <a class="cc" href="tel:${LOJA.telefoneLink}"><svg class="ico"><use href="#i-phone"/></svg><b>Telefone</b><span>${LOJA.telefone}</span></a>
    <a class="cc" href="mailto:${LOJA.email}"><svg class="ico"><use href="#i-mail"/></svg><b>E-mail</b><span>${LOJA.email}</span></a>
    <a class="cc" href="${LOJA.instagram}" target="_blank" rel="noopener"><svg class="ico"><use href="#i-ig"/></svg><b>Instagram</b><span>@canalconstrucao</span></a></div>
    <h3>Envie uma mensagem</h3>
    <form id="contactForm" class="contact-f"><div class="g2"><div class="field"><label for="ct-nome">Nome</label><input id="ct-nome" required autocomplete="name"></div><div class="field"><label for="ct-tel">Telefone</label><input id="ct-tel" data-mask="tel" inputmode="tel" autocomplete="tel"></div></div>
    <div class="field"><label for="ct-ass">Assunto</label><select id="ct-ass"><option>Orçamento</option><option>Dúvida sobre produto</option><option>Pedido feito no site</option><option>Trocas e devoluções</option><option>Condomínios</option><option>Outro</option></select></div>
    <div class="field"><label for="ct-msg">Mensagem</label><textarea id="ct-msg" rows="4" required></textarea></div>
    <div class="g2"><button class="btn btn-wa" type="submit" data-via="wa"><svg class="ico"><use href="#i-wa"/></svg> Enviar pelo WhatsApp</button><button class="btn btn-line" type="submit" data-via="mail"><svg class="ico"><use href="#i-mail"/></svg> Enviar por e-mail</button></div></form>`],
  "como-comprar": ["Como comprar", () => `<ol class="howto"><li><b>Escolha os produtos</b>Navegue pelos departamentos ou use a busca. Ajuste a quantidade e adicione à sacola.</li><li><b>Finalize a compra</b>Informe seus dados, o endereço (ou escolha retirar na loja) e a forma de pagamento.</li><li><b>Confirme no WhatsApp</b>Seu pedido chega pronto para a nossa equipe, que confirma estoque, frete e envia o pagamento.</li><li><b>Receba ou retire</b>Retire no Arruda ou em Boa Viagem, ou receba no endereço combinado.</li></ol><p>Itens “sob consulta” entram na sacola como orçamento e têm o valor confirmado pelo atendente.</p>`],
  "pagamento-e-entrega": ["Pagamento e entrega", () => `<h3>Formas de pagamento</h3><p>Pix, cartão de crédito (Mastercard, Visa, American Express, Diners, Elo e Hipercard) em até ${LOJA.parcelasMax}x sem juros, conforme o valor do pedido, e pagamento na loja na retirada.</p><div class="pay-row big">${payBadges()}</div>
    <h3>Retirada na loja</h3><p>Sem custo, nas lojas do Arruda e de Boa Viagem. Avisamos pelo WhatsApp quando o pedido estiver separado.</p>
    <h3>Entrega</h3><p>Entregamos no Recife e região. O frete é calculado pelo atendente conforme o bairro e o volume do pedido, e informado antes do pagamento.</p>`],
  "trocas-e-devolucoes": ["Trocas e devoluções", () => `<p class="lead">Queremos que você fique satisfeito com a compra.</p>
    <h3>Direito de arrependimento</h3><p>Em compras feitas fora da loja física (site, WhatsApp, telefone), você pode desistir em até <b>7 dias corridos</b> após o recebimento, conforme o art. 49 do Código de Defesa do Consumidor.</p>
    <h3>Produto com defeito</h3><p>Entre em contato informando o número do pedido e fotos do produto. Seguimos os prazos do Código de Defesa do Consumidor e a garantia do fabricante.</p>
    <h3>Como solicitar</h3><p>Fale com a gente pelo WhatsApp ${LOJA.whatsappTxt} ou pelo e-mail ${LOJA.email}.</p>
    <p class="note">Produtos cortados sob medida (como rolos de cabo fracionados) ou já aplicados na obra podem ter condições específicas. Consulte o atendimento.</p>`],
  "privacidade": ["Política de privacidade", () => `<p class="lead">Respeitamos seus dados, de acordo com a Lei Geral de Proteção de Dados (LGPD).</p>
    <h3>O que este site guarda</h3><p>Sua conta, sacola, favoritos, endereços e histórico de pedidos ficam salvos <b>apenas no seu navegador</b>, para facilitar as próximas compras. Você pode apagar tudo a qualquer momento saindo da conta ou limpando os dados do navegador.</p>
    <h3>Quando você finaliza um pedido</h3><p>Seus dados (nome, telefone, e-mail e endereço) são enviados para o WhatsApp da loja junto com o pedido, somente para atender a compra.</p>
    <h3>Seus direitos</h3><p>Você pode pedir acesso, correção ou exclusão dos seus dados pelo e-mail ${LOJA.email}.</p>`],
  "faq": ["Perguntas frequentes", () => `<div class="faq-l">${[
    ["Como funciona a compra pelo site?", "Você monta a sacola, informa dados, endereço ou retirada e a forma de pagamento. O pedido chega pronto no WhatsApp da loja, que confirma estoque, frete e envia o pagamento."],
    ["Posso parcelar?", `Sim, no cartão de crédito em até ${LOJA.parcelasMax}x sem juros, conforme o valor do pedido.`],
    ["Alguns itens aparecem como “sob consulta”. Por quê?", "São produtos com cores, medidas ou preços que variam. Eles entram na sacola como orçamento e o atendente confirma o valor."],
    ["Até quando valem as ofertas da Pré-Black?", "Até 30/11 ou enquanto durar o estoque, o que acontecer primeiro."],
    ["Não sei quantos m² de piso preciso.", "Na página do produto tem uma calculadora com margem de 10% para recortes. Se preferir, mande as medidas no WhatsApp."],
    ["Vocês atendem condomínios?", "Sim. Somos Canal da Construção & Condomínios. Peça um orçamento para manutenção e reforma de áreas comuns."],
    ["Onde ficam as lojas?", LOJA.lojas.map(l => `${l.nome}: ${l.end}`).join(" · ")]
  ].map(([q, a]) => `<details><summary>${q}</summary><p>${esc(a)}</p></details>`).join("")}</div>`]
};
function viewInst(slug) {
  const pg = INST[slug]; if (!pg) return viewNotFound();
  VIEW.innerHTML = `<div class="wrap page">${crumbs([[pg[0]]])}<div class="inst"><aside><nav>${Object.entries(INST).map(([k, v]) => `<a href="#/i/${k}" class="${k === slug ? "on" : ""}">${v[0]}</a>`).join("")}</nav><div class="inst-help"><b>Precisa de ajuda?</b><a class="btn btn-wa btn-sm" href="${waLink("Olá! Preciso de ajuda.")}" target="_blank" rel="noopener"><svg class="ico"><use href="#i-wa"/></svg> WhatsApp</a></div></aside><article class="prose"><h1>${pg[0]}</h1>${pg[1]()}</article></div></div>`;
  return `${pg[0]} · Canal da Construção`;
}
function viewNotFound() {
  VIEW.innerHTML = `<div class="wrap page"><div class="empty big"><img src="img/mascote.png" alt=""><h3>Página não encontrada</h3><p>O link pode ter mudado. Que tal voltar para o início?</p><a class="btn btn-ink" href="#/">Ir para o início</a></div></div>`;
  return "Página não encontrada · Canal da Construção";
}
function storesHTML() {
  return LOJA.lojas.map(l => `<div class="st rv"><iframe loading="lazy" title="Mapa da loja ${l.nome}" src="https://www.google.com/maps?q=${l.mapa}&output=embed"></iframe><div class="in"><h3>${l.nome}</h3><p>${l.end}</p><div class="acts"><a class="btn btn-ink btn-sm" target="_blank" rel="noopener" href="https://www.google.com/maps/dir/?api=1&destination=${l.mapa}">Como chegar</a><a class="btn btn-wa btn-sm" href="#" data-wa="Olá! Quero falar com a loja ${l.nome}."><svg class="ico"><use href="#i-wa"/></svg> Falar com a loja</a></div></div></div>`).join("");
}
function payBadges() { return ["Mastercard", "Visa", "Amex", "Diners", "Elo", "Hipercard", "Pix"].map(x => `<span class="pay-b">${x}</span>`).join("") }

/* ---------- header: search suggestions, mega menu ---------- */
function showSugg(q) {
  const box = $("#sugg"); q = q.trim();
  if (q.length < 2) return hideSugg();
  const t = norm(q).split(/\s+/);
  const hits = P.filter(p => { const h = norm(`${p.nome} ${p.marca || ""}`); return t.every(w => h.includes(w)) });
  const cats = CATS.filter(c => t.every(w => norm(c.nome).includes(w))).slice(0, 3);
  box.innerHTML = (cats.length ? `<div class="sg-cats">${cats.map(c => `<a href="#/c/${c.id}" class="dchip sm"><svg><use href="#c-${c.ic}"/></svg>${c.nome}</a>`).join("")}</div>` : "") +
    (hits.length ? hits.slice(0, 6).map(p => `<a class="sg" href="#/p/${p.id}"><span class="sgi">${media(p)}</span><span><b>${esc(shortName(p))}</b><small>${esc(p.marca || catById(p.cat).nome)}</small></span><em>${p.esgotado ? "Esgotado" : p.preco == null ? "Consultar" : brl(p.preco)}</em></a>`).join("") + `<a class="sg-all" href="#/busca/${encodeURIComponent(q)}">Ver todos os ${hits.length} resultados →</a>`
      : `<div class="sg-none">Nada encontrado para “${esc(q)}”. <a href="${waLink(`Olá! Vocês têm ${q}?`)}" target="_blank" rel="noopener">Perguntar no WhatsApp</a></div>`);
  box.hidden = false;
}
function hideSugg() { const b = $("#sugg"); if (b) b.hidden = true }
function renderMega() {
  const html = CATS.map(c => `<a href="#/c/${c.id}"><svg><use href="#c-${c.ic}"/></svg><span>${c.nome}<small>${countCat(c.id) ? countCat(c.id) + " produtos" : "sob consulta"}</small></span></a>`).join("");
  $("#megaList").innerHTML = html;
  $("#menuBody").innerHTML = `<a class="m-ofer" href="#/c/ofertas">🔥 Ofertas e Pré-Black</a><div class="m-list">${html}</div><div class="m-inst">${Object.entries(INST).map(([k, v]) => `<a href="#/i/${k}">${v[0]}</a>`).join("")}</div>`;
  $("#catsNav").innerHTML = `<button class="mega-btn" id="megaBtn" aria-expanded="false" aria-controls="mega"><svg class="ico"><use href="#i-menu"/></svg>Departamentos</button><a href="#/c/ofertas" class="hot">Ofertas 🔥</a>` + CATS.filter(c => countCat(c.id)).map(c => `<a href="#/c/${c.id}">${c.nome}</a>`).join("") + `<a href="#/i/lojas">Lojas</a>`;
}
function toggleMega(force) { const m = $("#mega"), on = force ?? m.hidden; m.hidden = !on; $("#megaBtn").setAttribute("aria-expanded", on) }
function closeMega() { const m = $("#mega"); if (m && !m.hidden) toggleMega(false) }

/* ---------- cart ---------- */
function saveCart() { store.set("cc_cart", cart); updateBadges() }
function addToCart(id, qty, fromEl) {
  const p = byId(id); if (!canBuy(p)) return;
  qty = Math.max(1, qty || (p.un === "m²" ? 10 : 1));
  const it = cart.find(c => c.id === id); it ? it.qty += qty : cart.push({ id, qty });
  saveCart(); flyTo(fromEl, p);
  toast(`${p.img ? `<img src="img/${p.img}" alt="">` : ""}<span>${qty} ${p.un} ${p.preco == null ? "no orçamento" : "na sacola"} ✓</span><button data-open="cart">Ver sacola</button>`);
}
function setQty(id, q) { const it = cart.find(c => c.id === id); if (!it) return; it.qty = Math.max(0, Math.min(9999, q | 0)); if (!it.qty) cart = cart.filter(c => c.id !== id); saveCart(); renderCart() }
function totals() { let sub = 0, de = 0, cons = 0; cart.forEach(c => { const p = byId(c.id); if (p.preco != null) { sub += p.preco * c.qty; de += (p.de || p.preco) * c.qty } else cons++ }); return { sub, eco: de - sub, cons } }
function renderCart() {
  const n = cart.length, foot = $("#cartFoot");
  $("[data-cart-label]").textContent = n ? `${n} ${n === 1 ? "item" : "itens"}` : "";
  if (!n) { $("#cartBody").innerHTML = `<div class="empty-d"><img src="img/mascote.png" alt=""><h4>Sua sacola está vazia</h4><p>Bora começar a obra? Tem oferta voando nos departamentos.</p><a class="btn btn-y" href="#/c/ofertas">Ver ofertas</a></div>`; foot.innerHTML = ""; foot.style.display = "none"; return }
  foot.style.display = "";
  const t = totals();
  $("#cartBody").innerHTML = (t.eco > 0 ? `<div class="progress">🎉 Você está economizando <span style="color:var(--green)">${brl(t.eco)}</span><div class="bar"><i style="width:${Math.min(100, 25 + t.eco / 4)}%"></i></div></div>` : "") +
    cart.map(c => { const p = byId(c.id); return `<div class="ci"><a href="#/p/${p.id}" class="cim">${media(p)}</a><div><h4><a href="#/p/${p.id}">${esc(p.nome)}</a></h4><div class="pp">${p.preco == null ? "Sob consulta" : `<b>${brl(p.preco * c.qty)}</b> · ${brl(p.preco)}/${p.un}`}</div></div><div class="ctl"><span class="step"><button data-dec="${p.id}" aria-label="Diminuir">−</button><input value="${c.qty}" inputmode="numeric" data-qty="${p.id}" aria-label="Quantidade"><span class="un">${p.un}</span><button data-inc="${p.id}" aria-label="Aumentar">+</button></span><button class="rm" data-rm="${p.id}">Remover</button></div></div>` }).join("");
  const np = t.sub ? parcelas(t.sub) : 0;
  foot.innerHTML = `${t.sub ? `<div class="tot"><span>Subtotal</span><span>${brl(t.sub + t.eco)}</span></div>` : ""}${t.eco > 0 ? `<div class="tot" style="color:var(--green)"><span>Descontos</span><span>− ${brl(t.eco)}</span></div>` : ""}
    ${t.cons ? `<div class="tot"><span>Itens para orçamento</span><span>${t.cons}</span></div>` : ""}
    <div class="tot big"><span>Total</span><b>${t.sub ? brl(t.sub) : "A orçar"}</b></div>
    ${t.sub ? `<div class="tot" style="justify-content:flex-end;font-size:.78rem;padding:0">ou ${np}x de ${brl(t.sub / np)} sem juros</div>` : ""}
    <p class="note">Frete e itens sob consulta são confirmados pelo atendente antes do pagamento.</p>
    <button class="btn btn-ink btn-block" id="checkout"><svg class="ico"><use href="#i-lock"/></svg> Finalizar compra</button>`;
}

/* ---------- account ---------- */
let accTab = "ped";
const initials = n => n.trim().split(/\s+/).slice(0, 2).map(s => s[0]).join("").toUpperCase();
function renderHeaderUser() {
  $("[data-acc-hi]").textContent = user ? `Olá, ${user.nome.split(" ")[0]}` : "Entre ou cadastre-se";
  $$("[data-av]").forEach(a => a.innerHTML = user ? esc(initials(user.nome)) : `<svg class="ico" style="width:18px;height:18px"><use href="#i-user"/></svg>`);
}
function favList() {
  const list = [...favs].map(byId).filter(Boolean);
  return list.length ? list.map(p => `<div class="mini"><a href="#/p/${p.id}" class="mim">${media(p)}</a><div><h4><a href="#/p/${p.id}">${esc(p.nome)}</a></h4><small>${p.esgotado ? "Esgotado" : p.preco == null ? "Sob consulta" : brl(p.preco) + "/" + p.un}</small></div>${canBuy(p) ? `<button data-add="${p.id}" aria-label="Adicionar à sacola"><svg class="ico" style="width:18px;height:18px"><use href="#i-plus"/></svg></button>` : ""}</div>`).join("") : `<div class="empty-d"><img src="img/mascote.png" alt=""><h4>Nenhum favorito</h4><p>Toque no ♥ dos produtos para salvar aqui.</p></div>`;
}
function renderAcc() {
  renderHeaderUser();
  const b = $("#accBody");
  if (!user) {
    b.innerHTML = `<div class="prof-h"><div class="av"><svg class="ico"><use href="#i-user"/></svg></div><div><b>Entre ou crie sua conta</b><small>Leva 10 segundos.</small></div></div>
    <div class="perk"><div><b>📦</b>Acompanhe pedidos</div><div><b>❤️</b>Salve favoritos</div><div><b>⚡</b>Checkout rápido</div></div>
    <form id="loginForm"><div class="field"><label for="f-nome">Nome completo</label><input id="f-nome" required autocomplete="name" placeholder="Como podemos te chamar?"></div>
    <div class="field"><label for="f-email">E-mail</label><input id="f-email" type="email" required autocomplete="email" placeholder="seu@email.com"></div>
    <div class="field"><label for="f-tel">WhatsApp</label><input id="f-tel" required inputmode="tel" autocomplete="tel" data-mask="tel" placeholder="(81) 90000-0000"></div>
    <div class="field"><label for="f-perfil">Você é…</label><select id="f-perfil"><option>Cliente final</option><option>Pedreiro / profissional de obra</option><option>Arquiteto(a) / designer</option><option>Síndico(a) / condomínio</option></select></div>
    <button class="btn btn-ink btn-block" type="submit">Entrar</button></form>
    ${accTab === "fav" ? `<div style="margin-top:24px"><div style="font-weight:800;margin-bottom:10px">Seus favoritos</div>${favList()}</div>` : ""}`;
    return;
  }
  const tabs = `<div class="tabs" role="tablist">${[["ped", "Pedidos"], ["fav", "Favoritos"], ["end", "Endereços"], ["dados", "Dados"]].map(([k, l]) => `<button data-tabb="${k}" class="${accTab === k ? "on" : ""}" role="tab" aria-selected="${accTab === k}">${l}</button>`).join("")}</div>`;
  let content = "";
  if (accTab === "ped") content = orders.length ? orders.map(o => `<div class="ord"><div class="top"><span>Pedido ${o.num}</span><span>${o.sub ? brl(o.sub) : "Orçamento"}</span></div><span class="stt">Enviado ao WhatsApp</span><p>${new Date(o.data).toLocaleDateString("pt-BR", { day: "2-digit", month: "short", year: "numeric" })} · ${o.itens.length} ${o.itens.length === 1 ? "item" : "itens"} · ${esc(o.ent)}${o.pag ? " · " + esc(o.pag) : ""}</p><button data-reorder="${o.num}">Comprar de novo</button></div>`).join("") : `<div class="empty-d"><img src="img/mascote.png" alt=""><h4>Nenhum pedido ainda</h4><p>Seus pedidos feitos pelo site aparecem aqui.</p><a class="btn btn-y" href="#/c/ofertas">Ir às compras</a></div>`;
  if (accTab === "fav") content = favList();
  if (accTab === "end") content = (user.enderecos || []).length ? user.enderecos.map((a, i) => `<div class="ord"><div class="top"><span>${esc(a.ident || "Endereço " + (i + 1))}</span><button data-rm-end="${i}" style="margin:0;color:var(--muted)">Remover</button></div><p style="margin-top:6px">${esc(a.rua)}, ${esc(a.num)}${a.comp ? " – " + esc(a.comp) : ""}<br>${esc(a.bairro)} · ${esc(a.cidade)}/${esc(a.uf)} · CEP ${esc(a.cep)}</p></div>`).join("") : `<div class="empty-d"><img src="img/mascote.png" alt=""><h4>Nenhum endereço</h4><p>Os endereços usados na finalização da compra ficam salvos aqui.</p></div>`;
  if (accTab === "dados") content = `<form id="dadosForm"><div class="field"><label for="d-nome">Nome</label><input id="d-nome" value="${esc(user.nome)}" required></div><div class="field"><label for="d-email">E-mail</label><input id="d-email" type="email" value="${esc(user.email || "")}"></div><div class="field"><label for="d-tel">WhatsApp</label><input id="d-tel" data-mask="tel" value="${esc(user.tel)}" required></div><button class="btn btn-ink btn-block" type="submit">Salvar alterações</button></form><button class="btn btn-line btn-block" style="margin-top:10px" id="logout">Sair da conta</button>`;
  b.innerHTML = `<div class="prof-h"><div class="av">${esc(initials(user.nome))}</div><div><b>${esc(user.nome)}</b><small>${esc(user.tel)}</small><br><span class="lvl">${esc(user.perfil || "Cliente Canal")}</span></div></div>${tabs}${content}`;
}

/* ---------- quick view ---------- */
let qvId = null;
function openQuick(id) {
  const p = byId(id); qvId = id; const m2 = p.un === "m²";
  $("#qvBox").innerHTML = `<button class="x" data-close aria-label="Fechar"><svg class="ico"><use href="#i-x"/></svg></button>
    <div class="qv-img">${media(p)}${off(p) ? `<span class="chip-off">-${off(p)}%</span>` : ""}</div>
    <div class="qv-in"><span class="eyebrow" style="color:var(--blue)">${esc(p.marca || catById(p.cat).nome)}</span><h3>${esc(p.nome)}</h3>${p.desc ? `<p class="desc">${esc(p.desc)}</p>` : ""}
      <div class="price">${priceBlock(p)}</div>
      ${canBuy(p) ? `<div class="calc"><div class="lb">${m2 ? "📐 Área" : "Quantidade"} <span class="step"><button data-m2="-1" aria-label="Diminuir">−</button><input id="qv-n" value="${m2 ? 20 : 1}" inputmode="decimal" aria-label="Quantidade"><span class="un">${p.un}</span><button data-m2="1" aria-label="Aumentar">+</button></span></div>${m2 ? `<label class="chk"><input type="checkbox" id="qv-mg" checked> +10% de margem para recortes</label>` : ""}<div class="res" id="qv-res"></div></div>
      <div class="qv-actions"><button class="btn btn-ink" data-add-qv="${p.id}"><svg class="ico"><use href="#i-bag"/></svg> ${p.preco == null ? "Adicionar ao orçamento" : "Adicionar à sacola"}</button></div>` : ""}
      <a class="lnk" href="#/p/${p.id}" style="margin-top:6px">Ver página completa do produto →</a>
    </div>`;
  if (canBuy(p)) calcQV(); openLayer("qv");
}
function qvQty() { const p = byId(qvId); const v = Math.max(1, parseFloat(String($("#qv-n").value).replace(",", ".")) || 1); return p.un === "m²" ? Math.ceil(v * ($("#qv-mg").checked ? 1.1 : 1)) : Math.round(v) }
function calcQV() { const p = byId(qvId), q = qvQty(), r = $("#qv-res"); if (!r) return; r.innerHTML = p.preco == null ? `Você vai pedir <b>${q} ${p.un}</b>.` : `${p.un === "m²" ? `Você precisa de <b>${q} m²</b> → ` : ""}Total <b>${brl(q * p.preco)}</b>${p.de ? ` · <span class="eco">economia de ${brl(q * (p.de - p.preco))}</span>` : ""}` }

/* ---------- layers ---------- */
let openId = null, lastFocus = null;
function openLayer(id, tab) {
  if (ckOpen()) closeCk();
  if (openId) closeLayer(true); else lastFocus = document.activeElement;
  if (id === "fav") { id = "acc"; tab = "fav" }
  if (id === "acc") { accTab = tab || accTab; renderAcc() }
  if (id === "cart") renderCart();
  openId = id; $("#" + id).classList.add("on"); $("#toast").classList.remove("on");
  $("#scrim").classList.add("on"); document.body.classList.add("lock");
  setTimeout(() => { const f = $("#" + id + " .x"); f && f.focus({ preventScroll: true }) }, 80);
}
function closeLayer(keep) {
  if (!openId) return; $("#" + openId).classList.remove("on"); openId = null;
  if (!keep) { $("#scrim").classList.remove("on"); document.body.classList.remove("lock"); lastFocus && lastFocus.focus && lastFocus.focus({ preventScroll: true }) }
}

/* ---------- toast, fly, badges ---------- */
let tt;
function toast(html) { const t = $("#toast"); t.innerHTML = html; t.classList.add("on"); clearTimeout(tt); tt = setTimeout(() => t.classList.remove("on"), 2800) }
function bump() { $$('#bagBtn,.bnav [data-open="cart"]').forEach(b => { b.classList.remove("bump"); void b.offsetWidth; b.classList.add("bump") }) }
function flyTo(el, p) {
  const target = innerWidth <= 760 ? $('.bnav [data-open="cart"]') : $("#bagBtn");
  if (!el || !p.img || matchMedia("(prefers-reduced-motion: reduce)").matches) return bump();
  const src = el.closest(".pc")?.querySelector(".media img") || $(".gal-main img") || $("#qvBox .qv-img img") || el.closest(".mini")?.querySelector("img");
  if (!src) return bump();
  const a = src.getBoundingClientRect(), b = target.getBoundingClientRect(), s = Math.min(a.width, a.height, 160);
  const f = document.createElement("img"); f.src = "img/" + p.img; f.className = "fly"; f.alt = "";
  Object.assign(f.style, { left: a.left + "px", top: a.top + "px", width: s + "px", height: s + "px" });
  document.body.appendChild(f);
  const dx = b.left + b.width / 2 - (a.left + s / 2), dy = b.top + b.height / 2 - (a.top + s / 2);
  f.animate([{ transform: "translate(0,0) scale(1)" }, { transform: `translate(${dx * .5}px,${dy * .5 - 90}px) scale(.55)`, offset: .55 }, { transform: `translate(${dx}px,${dy}px) scale(.1)`, opacity: .3 }], { duration: 760, easing: "cubic-bezier(.5,0,.3,1)" }).onfinish = () => { f.remove(); bump() };
}
function updateBadges() {
  $$("[data-cart-count]").forEach(b => { b.textContent = cart.length; b.classList.toggle("on", cart.length > 0) });
  $$("[data-fav-count]").forEach(b => { b.textContent = favs.size; b.classList.toggle("on", favs.size > 0) });
}
function toggleFav(id) {
  favs.has(id) ? favs.delete(id) : favs.add(id); store.set("cc_favs", [...favs]); updateBadges();
  const on = favs.has(id);
  $$(`[data-fav="${id}"]`).forEach(b => b.classList.toggle("on", on));
  toast(`<span>${on ? "♥ Salvo nos favoritos" : "Removido dos favoritos"}</span><button data-open="fav">Ver</button>`);
  if (openId === "acc") renderAcc();
}

/* ---------- checkout ---------- */
const UFS = "AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split(" ");
const ENVIOS = [{ id: "entrega", t: "Entrega no endereço", s: "Frete calculado pelo atendente conforme o bairro", need: true },
  ...LOJA.lojas.map(l => ({ id: l.id, t: "Retirar na loja " + l.nome, s: l.end }))];
const PAGS = [
  { id: "pix", t: "Pix", s: "Chave enviada pelo atendente após confirmar o pedido", ic: "⚡" },
  { id: "cartao", t: `Cartão de crédito em até ${LOJA.parcelasMax}x sem juros`, s: "Link de pagamento enviado pelo WhatsApp", ic: "💳" },
  { id: "loja", t: "Pagar na loja", s: "Dinheiro, débito ou crédito na retirada", ic: "🏬", pickup: true }];
const onlyD = v => String(v || "").replace(/\D/g, "");
const maskCep = v => { v = onlyD(v).slice(0, 8); return v.length > 5 ? v.slice(0, 5) + "-" + v.slice(5) : v };
const maskTel = v => { v = onlyD(v).slice(0, 11); if (!v) return ""; if (v.length <= 2) return "(" + v; if (v.length <= 6) return `(${v.slice(0, 2)}) ${v.slice(2)}`; if (v.length <= 10) return `(${v.slice(0, 2)}) ${v.slice(2, 6)}-${v.slice(6)}`; return `(${v.slice(0, 2)}) ${v.slice(2, 7)}-${v.slice(7)}` };
const emptyEnd = () => ({ cep: "", rua: "", num: "", comp: "", bairro: "", cidade: "Recife", uf: "PE", ident: "" });
let ck = null;
const ckOpen = () => $("#ck").classList.contains("on");
function openCheckout() {
  if (!cart.length) return;
  const saved = (user && user.enderecos) || [];
  ck = { step: user && user.email ? 2 : 1, dados: { email: user?.email || "", nome: user?.nome || "", tel: user?.tel || "" }, end: saved[0] ? { ...saved[0] } : emptyEnd(), semEnd: false, envio: "", pag: "", done: null };
  closeLayer(); renderCk();
  $("#ck").classList.add("on"); document.body.classList.add("lock"); $("#ck").scrollTop = 0;
}
function closeCk() { $("#ck").classList.remove("on"); if (!openId) document.body.classList.remove("lock") }
function ckSummary() {
  const t = totals(), fr = ck.envio === "entrega" ? "A combinar" : ck.envio ? "Grátis" : "—", np = t.sub ? parcelas(t.sub) : 0;
  return `<div class="ck-sum"><h4>Resumo do pedido <small>${cart.length} ${cart.length === 1 ? "item" : "itens"}</small></h4>
  <div class="ck-items">${cart.map(c => { const p = byId(c.id); return `<div class="ck-it"><span class="im">${media(p)}<i>${c.qty}</i></span><div><b>${esc(p.nome)}</b><small>${c.qty} ${p.un}${p.preco != null ? " · " + brl(p.preco) + "/" + p.un : ""}</small></div><span>${p.preco == null ? "Consultar" : brl(p.preco * c.qty)}</span></div>` }).join("")}</div>
  ${t.sub ? `<div class="tot"><span>Subtotal</span><span>${brl(t.sub + t.eco)}</span></div>` : ""}
  ${t.eco > 0 ? `<div class="tot" style="color:var(--green)"><span>Descontos</span><span>− ${brl(t.eco)}</span></div>` : ""}
  <div class="tot"><span>Frete</span><span>${fr}</span></div>
  ${t.cons ? `<div class="tot"><span>Itens sob consulta</span><span>${t.cons}</span></div>` : ""}
  <div class="tot big"><span>Total</span><b>${t.sub ? brl(t.sub) : "A orçar"}</b></div>
  ${t.sub ? `<div class="tot" style="justify-content:flex-end;font-size:.78rem;padding:0">ou ${np}x de ${brl(t.sub / np)} sem juros</div>` : ""}
  ${t.cons || ck.envio === "entrega" ? `<p class="note">${[t.cons ? "Itens sob consulta" : "", ck.envio === "entrega" ? "frete" : ""].filter(Boolean).join(" e ")} confirmados pelo atendente antes do pagamento.</p>` : ""}
  <div class="seal"><svg class="ico"><use href="#i-lock"/></svg><span><b>Compra segura</b>Você só paga depois que a loja confirmar seu pedido.</span></div></div>`;
}
function stepCard(n, title, sum, body) {
  const st = ck.step === n ? "cur" : ck.step > n ? "done" : "next";
  return `<section class="stp ${st}" id="stp${n}"><div class="stp-h"><span class="num">${st === "done" ? '<svg class="ico" style="width:18px;height:18px"><use href="#i-check"/></svg>' : n}</span><h3>${title}</h3>${st === "done" ? `<button class="lnk" data-ck-go="${n}">Editar</button>` : ""}</div>${st === "cur" ? `<div class="stp-b">${body()}</div>` : st === "done" ? `<div class="stp-s">${sum()}</div>` : ""}</section>`;
}
function renderCk() {
  const W = $("#ckWrap");
  if (ck.done) {
    const o = ck.done, pick = o.envio !== "entrega";
    W.innerHTML = `<div class="ck-ok"><div class="big"><svg class="ico" style="width:46px;height:46px"><use href="#i-check"/></svg></div><span class="eyebrow" style="color:var(--blue)">Pedido ${o.num}</span><h2>Pedido feito! 🎉</h2><p>Abrimos o WhatsApp com seu pedido completo. É só enviar a mensagem — o atendente responde por lá.</p>
    <ol class="tl"><li class="done"><b>Pedido enviado</b><span>${o.itens} ${o.itens == 1 ? "item" : "itens"} · ${o.sub ? brl(o.sub) : "orçamento"}</span></li><li><b>Confirmação</b><span>Atendente confirma estoque${pick ? "" : " e frete"}${o.cons ? " e itens sob consulta" : ""}</span></li><li><b>Pagamento</b><span>${esc(o.pag)}</span></li><li><b>${pick ? "Retirada" : "Entrega"}</b><span>${esc(o.envioT)}</span></li></ol>
    <div class="acts"><a class="btn btn-wa" href="${o.link}" target="_blank" rel="noopener"><svg class="ico"><use href="#i-wa"/></svg> Abrir WhatsApp de novo</a><button class="btn btn-line" data-open="acc" data-tab="ped">Meus pedidos</button><button class="btn btn-ink" data-ck-close>Continuar comprando</button></div></div>`;
    return;
  }
  const d = ck.dados, e = ck.end, saved = (user && user.enderecos) || [], pickup = ck.envio && ck.envio !== "entrega";
  const steps = [
    stepCard(1, "Dados pessoais",
      () => `<div class="kv"><div><small>E-mail</small><b>${esc(d.email)}</b></div></div><div class="kv two"><div><small>Nome</small><b>${esc(d.nome)}</b></div><div><small>Telefone</small><b>${esc(d.tel)}</b></div></div><button class="lnk" data-ck-logout>Não é você? Sair</button>`,
      () => `<form data-ck-form="1" novalidate><div class="field"><label for="c-email">E-mail <i>*</i></label><input id="c-email" type="email" autocomplete="email" value="${esc(d.email)}" placeholder="seu@email.com"></div><div class="g2"><div class="field"><label for="c-nome">Nome completo <i>*</i></label><input id="c-nome" autocomplete="name" value="${esc(d.nome)}" placeholder="Seu nome"></div><div class="field"><label for="c-tel">Telefone <i>*</i></label><input id="c-tel" inputmode="tel" autocomplete="tel" data-mask="tel" value="${esc(d.tel)}" placeholder="(81) 90000-0000"></div></div><p class="err" id="ck-err"></p><button class="btn btn-ink btn-block" type="submit">Continuar para entrega</button></form>`),
    stepCard(2, "Endereço de entrega",
      () => ck.semEnd ? `<b>Sem entrega</b> — vou retirar na loja` : `<b>${esc(e.ident || "Endereço")}</b><br>${esc(e.rua)}, ${esc(e.num)}${e.comp ? " – " + esc(e.comp) : ""}<br>${esc(e.bairro)} · ${esc(e.cidade)}/${esc(e.uf)} · CEP ${esc(e.cep)}`,
      () => `${saved.length ? `<div class="saved">${saved.map((a, i) => `<button type="button" class="chip-a ${a.cep === e.cep && a.num === e.num ? "on" : ""}" data-use-end="${i}"><b>${esc(a.ident || "Endereço " + (i + 1))}</b><span>${esc(a.rua)}, ${esc(a.num)}</span></button>`).join("")}<button type="button" class="chip-a" data-use-end="-1"><b>+ Novo</b><span>endereço</span></button></div>` : ""}
      <form data-ck-form="2" novalidate>
      <div class="field"><label for="c-cep">CEP <i>*</i></label><div class="cep-row"><input id="c-cep" inputmode="numeric" autocomplete="postal-code" data-mask="cep" value="${esc(e.cep)}" placeholder="00000-000"><a class="lnk" href="https://buscacepinter.correios.com.br/app/endereco/index.php" target="_blank" rel="noopener">Não sei meu CEP</a></div><small class="hint" id="cep-st"></small></div>
      <div class="field"><label for="c-rua">Endereço <i>*</i></label><input id="c-rua" autocomplete="address-line1" value="${esc(e.rua)}" placeholder="Rua, avenida..."></div>
      <div class="g2"><div class="field"><label for="c-num">Número <i>*</i></label><input id="c-num" value="${esc(e.num)}" placeholder="Nº"></div><div class="field"><label for="c-comp">Complemento</label><input id="c-comp" value="${esc(e.comp)}" placeholder="Apto, sala..."></div></div>
      <div class="field"><label for="c-bairro">Bairro <i>*</i></label><input id="c-bairro" value="${esc(e.bairro)}" placeholder="Bairro"></div>
      <div class="g2"><div class="field"><label for="c-cidade">Cidade <i>*</i></label><input id="c-cidade" autocomplete="address-level2" value="${esc(e.cidade)}" placeholder="Cidade"></div><div class="field"><label for="c-uf">Estado <i>*</i></label><select id="c-uf"><option value="">UF</option>${UFS.map(u => `<option ${u === e.uf ? "selected" : ""}>${u}</option>`).join("")}</select></div></div>
      <div class="field"><label for="c-ident">Identificação do endereço</label><input id="c-ident" value="${esc(e.ident)}" placeholder="Ex: Casa, Trabalho, Obra..."></div>
      <p class="err" id="ck-err"></p><button class="btn btn-ink btn-block" type="submit">Escolher modo de envio</button>
      <button type="button" class="lnk center" data-ck-pickup>Vou retirar na loja — pular endereço</button></form>`),
    stepCard(3, "Modo de envio",
      () => { const x = ENVIOS.find(x => x.id === ck.envio) || {}; return `<b>${esc(x.t || "")}</b><br>${esc(x.s || "")}` },
      () => `<form data-ck-form="3" novalidate><div class="opt">${ENVIOS.filter(x => !(x.need && ck.semEnd)).map(x => `<label><input type="radio" name="envio" value="${x.id}" ${ck.envio === x.id ? "checked" : ""}><span>${x.t}<small>${x.s}</small></span><em class="${x.need ? "ac" : ""}">${x.need ? "A combinar" : "Grátis"}</em></label>`).join("")}</div><p class="err" id="ck-err"></p><button class="btn btn-ink btn-block" type="submit">Escolher pagamento</button></form>`),
    stepCard(4, "Pagamento", () => "",
      () => `<form data-ck-form="4" novalidate><div class="opt">${PAGS.filter(x => !x.pickup || pickup).map(x => `<label><input type="radio" name="pag" value="${x.id}" ${ck.pag === x.id ? "checked" : ""}><span class="pi">${x.ic}</span><span>${x.t}<small>${x.s}</small></span></label>`).join("")}</div>
      <div class="pay-row">${payBadges()}</div>
      <p class="note">Nenhum dado de cartão é digitado aqui. Ao finalizar, seu pedido vai para o WhatsApp da loja, que confirma estoque${pickup ? "" : " e frete"} e envia o pagamento.</p>
      <label class="chk2"><input type="checkbox" id="c-ok"> Entendo que valores sob consulta${pickup ? "" : " e frete"} serão confirmados pelo atendente.</label>
      <p class="err" id="ck-err"></p><button class="btn btn-wa btn-block" type="submit"><svg class="ico"><use href="#i-wa"/></svg> Finalizar pedido</button></form>`)];
  const t = totals();
  W.innerHTML = `<ol class="ck-prog">${["Dados", "Entrega", "Envio", "Pagamento"].map((l, i) => `<li class="${i + 1 < ck.step ? "done" : i + 1 === ck.step ? "cur" : ""}">${l}</li>`).join("")}</ol>
  <details class="ck-mob"><summary>Resumo do pedido · ${t.sub ? brl(t.sub) : "A orçar"}<span>Ver itens</span></summary>${ckSummary()}</details>
  <div class="ck-grid"><div>${steps.join("")}</div><aside class="ck-side">${ckSummary()}</aside></div>`;
  requestAnimationFrame(() => { const cur = $("#ck .stp.cur"); if (!cur) return; const top = cur.getBoundingClientRect().top + $("#ck").scrollTop - 90; if (ck.step > 1) $("#ck").scrollTo({ top, behavior: "smooth" }); const f = $("input:not([type=radio]):not([type=checkbox]),select", cur); f && !f.value && f.focus({ preventScroll: true }) });
}
function ckErr(msg, ids = []) { $$("#ck .bad").forEach(x => x.classList.remove("bad")); ids.forEach(i => $("#" + i)?.classList.add("bad")); $("#ck-err").textContent = msg; if (ids[0]) $("#" + ids[0]).focus() }
function ckSubmit(n) {
  if (n === 1) {
    const email = $("#c-email").value.trim(), nome = $("#c-nome").value.trim(), tel = $("#c-tel").value.trim(), bad = [];
    if (!/^\S+@\S+\.\S{2,}$/.test(email)) bad.push("c-email"); if (nome.length < 3) bad.push("c-nome"); if (onlyD(tel).length < 10) bad.push("c-tel");
    if (bad.length) return ckErr("Confira os campos destacados.", bad);
    ck.dados = { email, nome, tel };
    user = { ...(user || { perfil: "Cliente final", enderecos: [] }), email, nome, tel }; store.set("cc_user", user); renderHeaderUser();
    ck.step = 2;
  }
  if (n === 2) {
    const v = id => $("#c-" + id).value.trim();
    const e = { cep: maskCep(v("cep")), rua: v("rua"), num: v("num"), comp: v("comp"), bairro: v("bairro"), cidade: v("cidade"), uf: $("#c-uf").value, ident: v("ident") };
    const bad = []; if (onlyD(e.cep).length !== 8) bad.push("c-cep"); ["rua", "num", "bairro", "cidade"].forEach(k => !e[k] && bad.push("c-" + k)); if (!e.uf) bad.push("c-uf");
    if (bad.length) return ckErr("Preencha os campos obrigatórios.", bad);
    ck.end = e; ck.semEnd = false; if (!ck.envio) ck.envio = "entrega";
    const list = (user.enderecos || []).filter(a => !(a.cep === e.cep && a.num === e.num)); list.unshift(e); user.enderecos = list.slice(0, 5); store.set("cc_user", user);
    ck.step = 3;
  }
  if (n === 3) { const r = $('#ck input[name="envio"]:checked'); if (!r) return ckErr("Escolha como quer receber."); ck.envio = r.value; if (ck.envio === "entrega" && ck.pag === "loja") ck.pag = ""; ck.step = 4 }
  if (n === 4) { const r = $('#ck input[name="pag"]:checked'); if (!r) return ckErr("Escolha a forma de pagamento."); if (!$("#c-ok").checked) return ckErr("Marque a confirmação para continuar.", ["c-ok"]); ck.pag = r.value; return finalize() }
  renderCk();
}
function finalize() {
  const t = totals(), num = "CC" + Date.now().toString().slice(-6), env = ENVIOS.find(x => x.id === ck.envio), pag = PAGS.find(x => x.id === ck.pag), e = ck.end, d = ck.dados;
  const linhas = cart.map(c => { const p = byId(c.id); return `• ${c.qty} ${p.un} — ${p.nome}${p.preco != null ? ` (${brl(p.preco)}/${p.un} = ${brl(p.preco * c.qty)})` : " (sob consulta)"}` }).join("\n");
  const msg = `Olá, Canal da Construção! Acabei de fazer um pedido pelo site 🛒\n\n*Pedido ${num}*\n${linhas}\n\n${t.sub ? `Total dos itens com preço: ${brl(t.sub)}\n` : ""}${t.eco > 0 ? `Descontos: ${brl(t.eco)}\n` : ""}${t.cons ? `Itens para orçamento: ${t.cons}\n` : ""}\n*Cliente*\n${d.nome}\n${d.tel}\n${d.email}\n\n*Envio:* ${env.t}${ck.envio === "entrega" ? `\n${e.rua}, ${e.num}${e.comp ? " – " + e.comp : ""}\n${e.bairro} – ${e.cidade}/${e.uf}\nCEP ${e.cep}` : ""}\n*Pagamento:* ${pag.t}`;
  const link = waLink(msg);
  orders.unshift({ num, data: new Date().toISOString(), itens: cart.map(c => ({ ...c })), sub: t.sub, ent: env.t, pag: pag.t }); orders = orders.slice(0, 20); store.set("cc_orders", orders);
  window.open(link, "_blank", "noopener");
  ck.done = { num, link, envio: ck.envio, envioT: env.t + (ck.envio === "entrega" ? ` · ${e.bairro}` : ""), pag: pag.t, sub: t.sub, cons: t.cons, itens: cart.length };
  cart = []; saveCart(); renderCk(); $("#ck").scrollTop = 0;
}
async function buscaCep(v) {
  const st = $("#cep-st"); if (!st) return; st.className = "hint"; st.textContent = "Buscando endereço…";
  try {
    const r = await fetch(`https://viacep.com.br/ws/${v}/json/`); const j = await r.json(); if (j.erro) throw 0;
    if (j.logradouro) $("#c-rua").value = j.logradouro; if (j.bairro) $("#c-bairro").value = j.bairro; $("#c-cidade").value = j.localidade || ""; $("#c-uf").value = j.uf || "";
    st.className = "hint ok"; st.textContent = "✓ Endereço encontrado"; $("#c-num").focus();
  } catch { st.className = "hint bad"; st.textContent = "Não encontramos esse CEP automaticamente. Preencha o endereço abaixo." }
}

/* ---------- misc ---------- */
function wireWa(root = document) { $$("[data-wa]", root).forEach(a => { a.href = waLink(a.dataset.wa); a.target = "_blank"; a.rel = "noopener" }) }
function tick() {
  const s = Math.max(0, Math.floor((new Date(LOJA.fimOferta) - Date.now()) / 1000));
  const v = [Math.floor(s / 86400), Math.floor(s % 86400 / 3600), Math.floor(s % 3600 / 60), s % 60].map(pad);
  $$("[data-cd-inline] i").forEach((e, i) => e.textContent = v[i] + "dhms"[i]);
  $$("[data-cd-big] b").forEach((e, i) => e.textContent = v[i]);
}
const io = new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target) } }), { threshold: .06, rootMargin: "0px 0px -30px 0px" });
function observeReveal() { $$(".rv:not(.in)").forEach(el => io.observe(el)) }

/* ---------- events ---------- */
document.addEventListener("click", e => {
  if (!e.target.closest("#mega,#megaBtn")) closeMega();
  if (!e.target.closest(".search")) hideSugg();
  const t = e.target.closest("button,a"); if (!t) return;
  const d = t.dataset;
  if (t.id === "megaBtn") { e.preventDefault(); toggleMega(); return }
  if (d.open) { e.preventDefault(); openLayer(d.open, d.tab); return }
  if (d.close !== undefined) { e.preventDefault(); closeLayer(); return }
  if (d.fav) { e.preventDefault(); e.stopPropagation(); toggleFav(d.fav); return }
  if (d.st) { const i = t.parentElement.querySelector("input"); i.value = Math.max(1, (parseInt(i.value) || 1) + +d.st); return }
  if (d.add) {
    e.preventDefault();
    const q = parseInt(t.closest(".buy")?.querySelector("input")?.value) || 0;
    addToCart(d.add, q, t);
    if (t.classList.contains("add") && !t.classList.contains("ok")) { const h = t.innerHTML; t.classList.add("ok"); t.innerHTML = `<svg class="ico"><use href="#i-check"/></svg><span>Pronto</span>`; setTimeout(() => { t.classList.remove("ok"); t.innerHTML = h }, 1300) }
    if (openId === "acc") renderAcc(); return
  }
  if (d.pdAdd) { addToCart(d.pdAdd, pdQty(byId(d.pdAdd)), t); return }
  if (d.pdBuy) { addToCart(d.pdBuy, pdQty(byId(d.pdBuy)), null); openCheckout(); return }
  if (d.pq) { const i = $("#pd-n"); i.value = Math.max(1, (parseFloat(String(i.value).replace(",", ".")) || 0) + +d.pq); calcPD(byId(location.hash.split("/")[2])); return }
  if (d.addQv) { e.preventDefault(); addToCart(d.addQv, qvQty(), t); setTimeout(() => closeLayer(), 250); return }
  if (d.quick) { e.preventDefault(); openQuick(d.quick); return }
  if (d.m2) { const i = $("#qv-n"); i.value = Math.max(1, (parseFloat(String(i.value).replace(",", ".")) || 0) + +d.m2); calcQV(); return }
  if (d.inc) { const c = cart.find(x => x.id === d.inc); setQty(d.inc, c.qty + 1); return }
  if (d.dec) { const c = cart.find(x => x.id === d.dec); setQty(d.dec, c.qty - 1); return }
  if (d.rm) { setQty(d.rm, 0); return }
  if (d.tabb) { accTab = d.tabb; renderAcc(); return }
  if (d.reorder) { const o = orders.find(x => x.num === d.reorder); o.itens.forEach(i => { if (!byId(i.id)) return; const c = cart.find(x => x.id === i.id); c ? c.qty += i.qty : cart.push({ ...i }) }); saveCart(); openLayer("cart"); return }
  if (d.sh) { const tr = t.closest(".shelf").querySelector(".track"); tr.scrollBy({ left: +d.sh * tr.clientWidth * .85, behavior: "smooth" }); return }
  if (d.share) { const p = byId(d.share), url = location.href; if (navigator.share) navigator.share({ title: p.nome, url }).catch(() => { }); else navigator.clipboard?.writeText(url).then(() => toast("<span>Link copiado ✓</span>")); return }
  if (d.pick !== undefined) { catState.sub = catState.sub === d.fs ? "" : d.fs; catState.page = 1; renderList(); return }
  if (d.fs !== undefined && t.tagName === "BUTTON") { catState.sub = ""; catState.page = 1; renderList(); return }
  if (d.fp !== undefined && t.tagName === "BUTTON") { catState.price = ""; catState.page = 1; renderList(); return }
  if (d.fb !== undefined && t.tagName === "BUTTON") { catState.brands.delete(d.fb); catState.page = 1; renderList(); return }
  if (d.fo !== undefined && t.tagName === "BUTTON") { catState.oferta = false; renderList(); return }
  if (d.fd !== undefined && t.tagName === "BUTTON") { catState.disp = false; renderList(); return }
  if (d.fclear !== undefined) { Object.assign(catState, { brands: new Set(), sub: "", price: "", oferta: false, disp: false, page: 1 }); renderList(); return }
  if (t.id === "checkout") { openCheckout(); return }
  if (d.ckClose !== undefined) { closeCk(); return }
  if (d.ckGo) { ck.step = +d.ckGo; renderCk(); return }
  if (d.ckLogout !== undefined) { user = null; store.set("cc_user", null); renderHeaderUser(); ck.dados = { email: "", nome: "", tel: "" }; ck.end = emptyEnd(); ck.step = 1; renderCk(); return }
  if (d.ckPickup !== undefined) { ck.semEnd = true; if (!ck.envio || ck.envio === "entrega") ck.envio = LOJA.lojas[0].id; ck.step = 3; renderCk(); return }
  if (d.useEnd) { ck.end = d.useEnd === "-1" ? emptyEnd() : { ...user.enderecos[+d.useEnd] }; renderCk(); return }
  if (d.rmEnd) { user.enderecos.splice(+d.rmEnd, 1); store.set("cc_user", user); renderAcc(); return }
  if (t.id === "logout") { user = null; store.set("cc_user", null); accTab = "ped"; renderAcc(); toast("<span>Você saiu da conta</span>"); return }
  if (d.nav === "deps") { e.preventDefault(); openLayer("menu"); return }
  if (d.nav === "home") { e.preventDefault(); go("#/"); return }
  if (t.getAttribute("href")?.startsWith("#/") && openId) closeLayer();
});
document.addEventListener("change", e => {
  const t = e.target, d = t.dataset;
  if (t.closest && t.closest("#ck") && $("#ck-err")) $("#ck-err").textContent = "";
  if (t.id === "sort") { catState.sort = t.value; catState.page = 1; renderList(); return }
  if (d.fb !== undefined) { t.checked ? catState.brands.add(d.fb) : catState.brands.delete(d.fb); catState.page = 1; renderListKeep(); return }
  if (d.fs !== undefined) { catState.sub = d.fs; catState.page = 1; renderListKeep(); return }
  if (d.fp !== undefined) { catState.price = d.fp; catState.page = 1; renderListKeep(); return }
  if (d.fo !== undefined) { catState.oferta = t.checked; catState.page = 1; renderListKeep(); return }
  if (d.fd !== undefined) { catState.disp = t.checked; catState.page = 1; renderListKeep(); return }
  if (t.id === "qv-mg") calcQV();
  if (t.id === "pd-mg") calcPD(byId(location.hash.split("/")[2]));
});
function renderListKeep() { const y = scrollY; renderList(); scrollTo({ top: y }) }
document.addEventListener("input", e => {
  const t = e.target;
  if (t.id === "q") showSugg(t.value);
  if (t.id === "qv-n") calcQV();
  if (t.id === "pd-n") calcPD(byId(location.hash.split("/")[2]));
  if (t.dataset.mask === "tel") t.value = maskTel(t.value);
  if (t.dataset.mask === "cep") { t.value = maskCep(t.value); const v = onlyD(t.value); if (v.length === 8 && v !== t._last) { t._last = v; buscaCep(v) } }
  if (t.closest && t.closest("#ck") && t.classList.contains("bad")) t.classList.remove("bad");
  if (t.dataset.qty) { const v = parseInt(t.value); if (v > 0) { const c = cart.find(x => x.id === t.dataset.qty); c.qty = Math.min(9999, v); saveCart(); clearTimeout(t._t); t._t = setTimeout(renderCart, 700) } }
});
document.addEventListener("submit", e => {
  e.preventDefault(); const f = e.target;
  if (f.dataset.ckForm) { ckSubmit(+f.dataset.ckForm); return }
  if (f.id === "searchForm") { const q = $("#q").value.trim(); if (q) { hideSugg(); $("#q").blur(); go("#/busca/" + encodeURIComponent(q)) } return }
  if (f.id === "loginForm") { user = { nome: $("#f-nome").value.trim(), email: $("#f-email").value.trim(), tel: $("#f-tel").value.trim(), perfil: $("#f-perfil").value, enderecos: [] }; store.set("cc_user", user); accTab = "ped"; renderAcc(); toast(`<span>Bem-vindo(a), ${esc(user.nome.split(" ")[0])}! 👷</span>`); return }
  if (f.id === "dadosForm") { user = { ...user, nome: $("#d-nome").value.trim(), email: $("#d-email").value.trim(), tel: $("#d-tel").value.trim() }; store.set("cc_user", user); renderAcc(); toast("<span>Dados salvos ✓</span>"); return }
  if (f.id === "contactForm") {
    const via = e.submitter?.dataset.via || "wa", txt = `${$("#ct-ass").value} — ${$("#ct-nome").value}${$("#ct-tel").value ? " (" + $("#ct-tel").value + ")" : ""}\n\n${$("#ct-msg").value}`;
    if (via === "wa") window.open(waLink(txt), "_blank", "noopener"); else location.href = `mailto:${LOJA.email}?subject=${encodeURIComponent("[Site] " + $("#ct-ass").value)}&body=${encodeURIComponent(txt)}`;
    toast("<span>Mensagem pronta para enviar ✓</span>"); return
  }
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape") { if (openId) closeLayer(); else if (ckOpen()) closeCk(); else { closeMega(); hideSugg() } }
  if (e.key === "/" && !/input|textarea|select/i.test(document.activeElement.tagName)) { e.preventDefault(); $("#q").focus() }
});
$("#q").addEventListener("focus", e => showSugg(e.target.value));
$("#scrim").addEventListener("click", () => closeLayer());
$("#qv").addEventListener("click", e => { if (e.target.id === "qv") closeLayer() });
addEventListener("scroll", () => $("#hdr").classList.toggle("scrolled", scrollY > 10), { passive: true });

/* ---------- init ---------- */
renderMega(); renderHeaderUser(); updateBadges(); wireWa(); route();
setInterval(tick, 1000);
$$("[data-year]").forEach(x => x.textContent = new Date().getFullYear());
