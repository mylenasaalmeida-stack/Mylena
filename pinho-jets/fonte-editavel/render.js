// uso: node render.js <arquivo.html> <pastaSaida>
// exporta cada <section class="f" data-out="nome"> como PNG; #pano vira 3 capas fatiadas
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const [html, out] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 3300, height: 2100 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(html));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForFunction(() => window.READY === true);
  await p.waitForTimeout(300);
  const pano = await p.$('#pano');
  if (pano) {
    const bb = await pano.boundingBox();
    for (let i = 0; i < 3; i++) {
      await p.screenshot({ path: `${out}/0${i + 1}_capa.png`, clip: { x: bb.x + i * 1012, y: bb.y, width: 1080, height: 1350 } });
    }
  }
  for (const el of await p.$$('section[data-out]')) {
    const name = await el.getAttribute('data-out');
    fs.mkdirSync(path.dirname(`${out}/${name}.png`), { recursive: true });
    await el.screenshot({ path: `${out}/${name}.png` });
  }
  await b.close();
})();
