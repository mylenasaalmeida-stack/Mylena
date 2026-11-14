const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:2000}});
await p.goto('file://'+process.cwd()+'/artes_ig.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
fs.mkdirSync('artes',{recursive:true});
for(const id of fs.readFileSync('artes_ig.list','utf8').trim().split('\n')){await p.locator('[id="'+id+'"]').screenshot({path:'artes/'+id+'.png'});}
await b.close();})();
