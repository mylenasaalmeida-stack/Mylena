// PNG 1080x1350 dos 3 fixados em ../ + prévia de como ficam lado a lado no perfil (grade 3:4).
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1080, height: 1350}});
  const ns = ['fixado-1-agenda', 'fixado-2-senta', 'fixado-3-volta'];
  for (const n of ns) {
    await p.goto('file://' + __dirname + '/' + n + '.html');
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
    await p.screenshot({path: __dirname + '/../' + n + '.png'});
  }
  // prévia: recorte 3:4 central de cada post, lado a lado com 3 px de espaço, como no perfil
  const w = 1012, h = 1350;
  await p.setViewportSize({width: w * 3 + 6, height: h});
  const imgs = ns.map(n => `<div style="width:${w}px;height:${h}px;background:url('file://${__dirname}/../${n}.png') center/cover"></div>`).join('');
  await p.setContent(`<body style="margin:0;display:flex;gap:3px;background:#fff">${imgs}</body>`);
  await p.waitForTimeout(300);
  await p.screenshot({path: __dirname + '/../previa-perfil.png'});
  await b.close();
})();
