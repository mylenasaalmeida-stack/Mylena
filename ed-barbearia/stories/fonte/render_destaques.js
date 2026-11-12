// PNG 1080x1920 das capas de destaque em ../destaques/
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  const out = __dirname + '/../destaques'; fs.mkdirSync(out, {recursive: true});
  for (const f of fs.readdirSync(__dirname).filter(f => f.startsWith('destaque-') && f.endsWith('.svg'))) {
    await p.goto('file://' + __dirname + '/' + f);
    await p.screenshot({path: out + '/' + f.replace('.svg', '.png')});
  }
  await b.close();
})();
