// Renderiza as capas de Reels (PNG 1080x1920 em ../capas-reels e cópia aqui pra grade) e o mockup completo (../mockup-perfil.png).
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  fs.mkdirSync(__dirname + '/../capas-reels', {recursive: true});
  for (const f of fs.readdirSync(__dirname).filter(f => f.startsWith('capa-reels-') && f.endsWith('.html'))) {
    await p.goto('file://' + __dirname + '/' + f);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
    const png = f.replace('.html', '.png');
    await p.screenshot({path: __dirname + '/' + png});
    fs.copyFileSync(__dirname + '/' + png, __dirname + '/../capas-reels/' + png);
  }
  const m = await b.newPage({viewport: {width: 1100, height: 1000}, deviceScaleFactor: 2});
  await m.goto('file://' + __dirname + '/mockup.html');
  await m.evaluate(() => document.fonts.ready); await m.waitForTimeout(500);
  await m.screenshot({path: __dirname + '/../mockup-perfil.png', fullPage: true});
  await b.close();
})();
