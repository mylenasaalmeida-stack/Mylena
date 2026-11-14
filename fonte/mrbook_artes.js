// Exporta cada elemento [data-out] de uma página HTML como PNG.
// Uso: node fonte/mrbook_artes.js <pagina.html> <pasta_saida> [escala]
const {chromium} = require('playwright');
const fs = require('fs'), path = require('path');

(async () => {
  const [html, out, scale] = process.argv.slice(2);
  const b = await chromium.launch();
  const ctx = await b.newContext({viewport: {width: 1300, height: 1600}, deviceScaleFactor: Number(scale || 1)});
  const p = await ctx.newPage();
  p.on('requestfailed', r => { if (!r.url().includes('fonts.g')) console.log('FALHOU', r.url()); });
  await p.goto('file://' + path.resolve(html));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForLoadState('networkidle');
  await p.waitForTimeout(800);
  const els = await p.$$('[data-out]');
  for (const e of els) {
    const f = path.join(out, (await e.getAttribute('data-out')) + '.png');
    fs.mkdirSync(path.dirname(f), {recursive: true});
    await e.screenshot({path: f});
  }
  console.log(els.length, 'arquivos em', out);
  await b.close();
})();
