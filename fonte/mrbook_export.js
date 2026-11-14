// Exporta as peças do rebrand Mr.Book em PNG a partir de mr-book/proposta.html
// Uso: node fonte/mrbook_export.js <proposta_embrulhada.html> <pasta_saida>
const {chromium} = require('playwright');
const fs = require('fs'), path = require('path');

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1200, height: 900}});
  await p.goto('file://' + path.resolve(process.argv[2]));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(1500);
  const OUT = process.argv[3];

  await p.evaluate(() => {
    const st = document.createElement('style');
    st.textContent = `
 #ex{position:absolute;left:0;top:0;z-index:999}
 #ex>*{display:block}
 .xl{width:2400px;height:1000px;display:grid!important;place-items:center}
 .xl .wm{font-size:300px}
 .xa{width:1080px;height:1080px;background:#FFCE1B;display:grid!important;place-items:center}
 .xa .wm{font-size:150px;color:#16181D}
 .xp{width:1080px;height:1440px}
 .xp svg{width:100%;height:1440px;display:block}
 .xc{width:1080px;height:1920px;background:#FFCE1B;color:#16181D;display:grid!important;place-items:center}
 .xc svg{width:420px;height:420px}
 .xs{width:1080px;height:1920px;padding:110px 90px 120px;display:flex!important;flex-direction:column;justify-content:space-between;font-family:var(--body);font-size:58px;line-height:1.25;box-sizing:border-box;border-radius:0}
 .xs .bars{display:flex;gap:12px}.xs .bars i{flex:1;height:8px;border-radius:8px;background:currentColor;opacity:.3}.xs .bars i.on{opacity:1}
 .xs b{display:block;font-family:var(--display);font-stretch:118%;font-weight:900;font-size:108px;line-height:1;margin-bottom:40px;overflow-wrap:anywhere;letter-spacing:-.02em}
 .xs .cta{font-family:var(--mono);font-size:40px;letter-spacing:.04em;text-transform:uppercase;border:4px solid currentColor;border-radius:999px;padding:18px 36px}
 .xs .foot{display:flex;justify-content:space-between;align-items:center;gap:30px}
 .xs .foot .wm{font-size:64px}
 .xs.st-d b,.xs.st-d .wm{color:#FFCE1B}
 .xs.st-p{border:0}`;
    document.head.append(st);
    const ex = document.createElement('div'); ex.id = 'ex'; document.body.append(ex);
    const WM = '<span class="wm">mr.b<svg class="ook"><use href="#ook"/></svg></span>';
    let h = '';
    [['amarelo','#FFCE1B','#16181D'],['grafite','#16181D','#FFCE1B'],['branco','#FFFFFF','#16181D'],['transparente-grafite','transparent','#16181D'],['transparente-branco','transparent','#FFFFFF']]
      .forEach(([n,bg,fg]) => h += `<div class="xl" data-out="logo/logo-${n}" style="background:${bg};color:${fg}">${WM}</div>`);
    h += `<div class="xa" data-out="perfil/foto-de-perfil">${WM}</div>`;
    const names = ['1-quem-somos','2-kits-por-curso','3-como-comprar'];
    [0,1,2].forEach(i => h += `<div class="xp" data-out="fixados/fixado-${names[i]}"><svg viewBox="${i*1080} 0 1080 1440"><use href="#tri"/></svg></div>`);
    h += `<div class="xp" data-out="fixados/previa-os-tres" style="width:3240px"><svg viewBox="0 0 3240 1440"><use href="#tri"/></svg></div>`;
    HL.forEach((x, n) => {
      const num = String(n+1).padStart(2,'0');
      h += `<div class="xc" data-out="destaques/${num}-${x.id}/00-capa"><svg><use href="#${x.icon}"/></svg></div>`;
      x.st.forEach((s, k) => h += `<div class="xs ${s[0]}" data-out="destaques/${num}-${x.id}/${String(k+1).padStart(2,'0')}-story">
        <div class="bars">${x.st.map((_,j) => `<i class="${j<=k?'on':''}"></i>`).join('')}</div>
        <div><b>${s[1]}</b>${s[2]}</div>
        <div class="foot">${s[3] ? `<span class="cta">${s[3]}</span>` : '<span></span>'}${WM}</div></div>`);
    });
    ex.innerHTML = h;
  });
  await p.waitForTimeout(800);
  const els = await p.$$('#ex>[data-out]');
  for (const e of els) {
    const o = await e.getAttribute('data-out');
    const f = path.join(OUT, o + '.png');
    fs.mkdirSync(path.dirname(f), {recursive: true});
    await e.screenshot({path: f, omitBackground: o.includes('transparente')});
  }
  console.log(els.length, 'arquivos');

  // mockup do perfil do Instagram em alta resolução (celular inteiro)
  const ctx = await b.newContext({viewport: {width: 1200, height: 1400}, deviceScaleFactor: 3});
  const m = await ctx.newPage();
  await m.goto('file://' + path.resolve(process.argv[2]));
  await m.evaluate(() => document.fonts.ready);
  await m.waitForTimeout(1500);
  const phone = await m.$('.phone');
  fs.mkdirSync(path.join(OUT, 'perfil'), {recursive: true});
  await phone.screenshot({path: path.join(OUT, 'perfil/mockup-perfil-instagram.png')});
  console.log('mockup do perfil');
  await b.close();
})();
