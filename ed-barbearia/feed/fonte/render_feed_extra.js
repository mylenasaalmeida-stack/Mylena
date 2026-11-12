// PNG 1080x1350 das artes extras em ../ e aviso se o conteúdo encostar no rodapé.
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1080, height: 1350}});
  for (const f of fs.readdirSync(__dirname).filter(f => /^F\d-.*\.html$/.test(f))) {
    await p.goto('file://' + __dirname + '/' + f);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
    const gap = await p.evaluate(() => document.querySelector('.rod').getBoundingClientRect().top -
      Math.max(...[...document.querySelectorAll('.c *')].map(e => e.getBoundingClientRect().bottom)));
    if (gap < 30) console.log('APERTADO', f, Math.round(gap));
    await p.screenshot({path: __dirname + '/../' + f.replace('.html', '.png')});
  }
  await b.close();
})();
