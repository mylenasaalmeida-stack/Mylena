// PNG 1080x1920 de cada story em ../logo-antiga/
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  const out = __dirname + '/../logo-antiga'; fs.mkdirSync(out, {recursive: true});
  for (const f of fs.readdirSync(__dirname).filter(f => /^\d\d-.*\.html$/.test(f))) {
    await p.goto('file://' + __dirname + '/' + f);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
    const over = await p.evaluate(() => { const c = document.querySelector('.cta'); const b = document.querySelector('.body');
      return c ? b.getBoundingClientRect().bottom - c.getBoundingClientRect().top : b.getBoundingClientRect().bottom - 1580; });
    if (over > -10) console.log('APERTADO', f, Math.round(over));
    await p.screenshot({path: out + '/story-' + f.replace('.html', '.png')});
  }
  await b.close();
})();
