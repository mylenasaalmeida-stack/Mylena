// uso: node render.js cartao panfleto  ->  ../<nome>_grafica.pdf  +  ../previa/<nome>-N.png
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();fs.mkdirSync('../previa',{recursive:true});
for(const f of process.argv.slice(2)){
  const p=await b.newPage({deviceScaleFactor:6});
  await p.goto('file://'+process.cwd()+'/'+f+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
  await p.pdf({path:'../'+f+'_grafica.pdf',printBackground:true,preferCSSPageSize:true});
  const pages=await p.$$('.page');
  for(let i=0;i<pages.length;i++) {const bb=await pages[i].boundingBox();await p.screenshot({fullPage:true,path:`../previa/${f}-${i+1}.png`,clip:{x:Math.ceil(bb.x),y:Math.ceil(bb.y),width:Math.floor(bb.width)-1,height:Math.floor(bb.height)-1}});}
  await p.close();}
await b.close();})();
