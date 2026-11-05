// PNG 1080x1920 dos stories de vaga em ../../stories
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  const out = __dirname + '/../../stories'; fs.mkdirSync(out, {recursive: true});
  for (const n of ['vaga-barbeiro-1', 'vaga-barbeiro-2']) {
    await p.goto('file://' + __dirname + '/' + n + '.html');
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
    await p.screenshot({path: out + '/' + n + '.png'});
  }
  await b.close();
})();
