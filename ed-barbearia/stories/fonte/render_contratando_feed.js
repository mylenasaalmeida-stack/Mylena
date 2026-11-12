// PNG 1080x1350 do post "Estamos contratando" em ../../feed/
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1080, height: 1350}});
  const out = __dirname + '/../../feed'; fs.mkdirSync(out, {recursive: true});
  await p.goto('file://' + __dirname + '/feed-estamos-contratando.html');
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
  const fim = await p.evaluate(() => Math.max(...[...document.querySelectorAll('.body *')].map(e => e.getBoundingClientRect().bottom)));
  if (fim > 1290) console.log('APERTADO feed', Math.round(fim));
  await p.screenshot({path: out + '/feed-estamos-contratando.png'});
  await b.close();
})();
