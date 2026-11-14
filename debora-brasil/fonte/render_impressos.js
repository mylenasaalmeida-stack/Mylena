// Gera os PDFs de impressão e prévias PNG. Uso: node render_impressos.js
const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();
for(const [f,w,h] of [['vela',790,2540],['porta',610,910]]){
  const p=await b.newPage();await p.goto('file://'+path.join(__dirname,f+'.html'));await p.evaluate(()=>document.fonts.ready);
  await p.pdf({path:path.join(__dirname,'..','impressao',f+'.pdf'),width:w+'mm',height:h+'mm',printBackground:true,pageRanges:'1'});
  const px=1600/w;await p.setViewportSize({width:Math.round(w*3.7795),height:Math.round(h*3.7795)});
  const q=await b.newPage({viewport:{width:Math.round(w*3.7795),height:Math.round(h*3.7795)},deviceScaleFactor:(f=='vela'?0.45:0.9)});
  await q.goto('file://'+path.join(__dirname,f+'.html'));await q.evaluate(()=>document.fonts.ready);await q.waitForTimeout(200);
  await q.screenshot({path:path.join(__dirname,'..','impressao',f+'-previa.png')});
  const n=await q.evaluate(()=>{const d=document.querySelector('.faixa div');return d?[d.getBoundingClientRect().height/3.7795, d.getBoundingClientRect().width/3.7795]:null});console.log(f,n);
}
await b.close();})();
