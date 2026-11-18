// Gera os PNGs da agenda Nov · Jan em ../png/
// Uso: cd sidney-filhinho/fonte && node render.js
const {chromium}=require('playwright');const path=require('path');
(async()=>{
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1200,height:2200},deviceScaleFactor:1});
  await p.goto('file://'+path.join(__dirname,'agenda-nov-jan.html'));
  await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
  for(const el of await p.locator('.art').all()){
    const id=await el.getAttribute('id');
    await el.screenshot({path:path.join(__dirname,'..','png',id+'.png')});
    console.log(id);
  }
  await b.close();
})();
