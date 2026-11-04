// Gera ../ED-Barbearia-Plano-de-Conteudo-Novembro-2026-v2.pdf e acusa slide com conteúdo passando do rodapé.
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + __dirname + '/plano.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const over = await p.evaluate(() => [...document.querySelectorAll('.s')].map((s, i) => {
    const f = s.querySelector('.foot'); if (!f) return null;
    const lim = f.getBoundingClientRect().top - 4;
    let max = 0;
    s.querySelectorAll('*').forEach(e => { if (!f.contains(e) && !e.classList.contains('hc')) max = Math.max(max, e.getBoundingClientRect().bottom); });
    return max > lim ? `slide ${i + 1}: +${Math.round(max - lim)}px` : null;
  }).filter(Boolean));
  console.log(over.length ? 'ESTOURO: ' + over.join(' | ') : 'ok, sem estouro');
  await p.pdf({path: __dirname + '/../ED-Barbearia-Plano-de-Conteudo-Novembro-2026-v2.pdf', printBackground: true, preferCSSPageSize: true});
  await b.close();
})();
