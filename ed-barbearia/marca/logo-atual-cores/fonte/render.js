// PNG 1080x1080 (fundo transparente) de cada SVG em ../
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport: {width: 1080, height: 1080}});
  for (const f of fs.readdirSync(__dirname + '/..').filter(f => f.endsWith('.svg'))) {
    const svg = fs.readFileSync(__dirname + '/../' + f, 'utf8').replace('width="2200" height="2200"', 'width="1080" height="1080"');
    await p.setContent(`<body style="margin:0;background:transparent">${svg}</body>`);
    await p.locator('svg').screenshot({path: __dirname + '/../' + f.replace('.svg', '.png'), omitBackground: true});
  }
  await b.close();
})();
