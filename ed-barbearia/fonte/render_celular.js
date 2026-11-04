// Gera o PDF e acusa página com texto estourando. Uso: node render_celular.js revisao
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + process.cwd() + '/' + f + '.html');
    await p.evaluate(() => document.fonts.ready);
    const over = await p.evaluate(() => [...document.querySelectorAll('.pg')].map((s, i) => {
      const foot = s.querySelector('.foot').getBoundingClientRect().top;
      const kids = [...s.children].filter(c => !c.classList.contains('foot'));
      const bottom = Math.max(...kids.map(c => c.getBoundingClientRect().bottom));
      return bottom > foot - 6 ? `página ${i + 1}: passa ${Math.round(bottom - foot + 6)}px` : null;
    }).filter(Boolean));
    if (over.length) console.log('ESTOURO:', over.join(' | ')); else console.log('ok, sem estouro');
    await p.pdf({path: '../' + f + '.pdf', printBackground: true, preferCSSPageSize: true});
  }
  await b.close();
})();
