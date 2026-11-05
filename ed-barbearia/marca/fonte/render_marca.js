// Gera ../ED-Barbearia-Marca-Nova.pdf e os PNGs em ../png (fundo transparente fora do desenho).
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + __dirname + '/marca.html');
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  await p.pdf({path: __dirname + '/../ED-Barbearia-Marca-Nova.pdf', printBackground: true, preferCSSPageSize: true});
  fs.mkdirSync(__dirname + '/../png', {recursive: true});
  for (const f of fs.readdirSync(__dirname + '/exp')) {
    const horiz = f.includes('horizontal');
    await p.setViewportSize({width: horiz ? 1520 : 1080, height: horiz ? 440 : 1080});
    await p.goto('file://' + __dirname + '/exp/' + f);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
    await p.locator('svg').screenshot({path: __dirname + '/../png/' + f.replace('.html', '.png'), omitBackground: true});
  }
  await b.close();
})();
