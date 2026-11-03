const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const f of process.argv.slice(2)){await p.goto('file://'+process.cwd()+'/'+f+'.html');await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:f+'.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});}
await b.close();})();
