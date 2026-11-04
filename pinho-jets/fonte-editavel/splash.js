// Gerador procedural de mar + splash (canvas). Seeded para resultado reproduzível.
// desenha numa camada temporária e aplica blur uma vez só
function layer(ctx,blur,fn){
  if(!blur){fn(ctx);return}
  const c=document.createElement('canvas');c.width=ctx.canvas.width;c.height=ctx.canvas.height;
  const t=c.getContext('2d');fn(t);ctx.save();ctx.filter=`blur(${blur}px)`;ctx.drawImage(c,0,0);ctx.restore();
}
function rng(seed){let s=seed>>>0;return()=>{s=(s*1664525+1013904223)>>>0;return s/4294967296}}

// Mar: gradiente + reflexos horizontais
function ocean(ctx,W,H,y0,opt={}){
  const r=rng(opt.seed||7);
  const g=ctx.createLinearGradient(0,y0,0,H);
  g.addColorStop(0,opt.top||'#0e3f63');g.addColorStop(.35,opt.mid||'#0a2742');g.addColorStop(1,opt.bot||'#041322');
  ctx.fillStyle=g;ctx.fillRect(0,y0,W,H-y0);
  // linha do horizonte brilhante
  const hg=ctx.createLinearGradient(0,y0-30,0,y0+40);
  hg.addColorStop(0,'rgba(19,179,196,0)');hg.addColorStop(.5,'rgba(120,220,230,.35)');hg.addColorStop(1,'rgba(19,179,196,0)');
  ctx.fillStyle=hg;ctx.fillRect(0,y0-30,W,70);
  // reflexos
  for(let i=0;i<(opt.n||900);i++){
    const t=Math.pow(r(),1.6);const y=y0+t*(H-y0);
    const w=(6+r()*60)*(0.4+t*2.2);const x=r()*W;
    ctx.globalAlpha=(0.05+r()*0.22)*(1-t*0.6);
    ctx.fillStyle=r()<.7?'#bfe9ef':'#13b3c4';
    ctx.beginPath();ctx.ellipse(x,y,w,0.8+t*3.2,0,0,Math.PI*2);ctx.fill();
  }
  ctx.globalAlpha=1;
}

// Splash: partículas balísticas com rastro (rooster tail / spray)
function splash(ctx,o){
  const r=rng(o.seed||1);
  const N=o.n||2600, g=o.g??900, T=o.T||1.1;
  const a0=o.a0*Math.PI/180,a1=o.a1*Math.PI/180;
  const layers=[{blur:18,frac:.35,alpha:.35,mult:2.6},{blur:5,frac:.35,alpha:.5,mult:1.4},{blur:0,frac:.3,alpha:.95,mult:1}];
  // névoa / corpo do spray
  const glow=ctx.createRadialGradient(o.x,o.y,0,o.x,o.y,o.glow||420);
  glow.addColorStop(0,'rgba(235,250,255,.55)');glow.addColorStop(1,'rgba(235,250,255,0)');
  ctx.fillStyle=glow;ctx.fillRect(o.x-(o.glow||420),o.y-(o.glow||420),2*(o.glow||420),2*(o.glow||420));
  for(const L of layers){
    layer(ctx,L.blur,(ctx)=>{
    const n=Math.floor(N*L.frac);
    for(let i=0;i<n;i++){
      const a=a0+(a1-a0)*Math.pow(r(),o.bias||1);
      const v=(o.v||900)*(0.35+r()*0.85);
      const t=T*Math.pow(r(),0.8);
      const vx=Math.cos(a)*v,vy=-Math.sin(a)*v;
      const x=o.x+vx*t+(r()-.5)*(o.jitter||30), y=o.y+vy*t+.5*g*t*t+(r()-.5)*(o.jitter||30);
      const cvx=vx,cvy=vy+g*t;const sp=Math.hypot(cvx,cvy)||1;
      const rad=(0.6+Math.pow(r(),5)*9)*L.mult*(o.scale||1);
      const len=rad*(1.5+sp/120*(o.streak||1));
      const life=1-t/T;
      ctx.globalAlpha=Math.min(1,L.alpha*(0.25+life*0.9));
      ctx.fillStyle=r()<.12?'#bdeff4':'#f4fbff';
      ctx.save();ctx.translate(x,y);ctx.rotate(Math.atan2(cvy,cvx));
      ctx.beginPath();ctx.ellipse(0,0,len,rad,0,0,Math.PI*2);ctx.fill();ctx.restore();
    }
    ctx.globalAlpha=1;});
  }
  // fios de água (sheets)
  layer(ctx,1.5,(ctx)=>{
  for(let i=0;i<(o.sheets||70);i++){
    const a=a0+(a1-a0)*r(),v=(o.v||900)*(0.6+r()*0.6),tEnd=T*(0.3+r()*0.6);
    const vx=Math.cos(a)*v,vy=-Math.sin(a)*v;
    ctx.beginPath();
    for(let k=0;k<=24;k++){const t=tEnd*k/24;const x=o.x+vx*t,y=o.y+vy*t+.5*g*t*t;k?ctx.lineTo(x,y):ctx.moveTo(x,y)}
    ctx.strokeStyle='rgba(240,250,255,.22)';ctx.lineWidth=1+r()*5*(o.scale||1);ctx.stroke();
  }});
  ctx.globalAlpha=1;
}

// espuma na linha d'água
function foam(ctx,x,y,w,h,seed){
  const r=rng(seed||3);
  layer(ctx,3,(ctx)=>{
  for(let i=0;i<900;i++){
    const t=r();const px=x+t*w,py=y+(r()-.5)*h*(0.3+ (1-t)*0.9);
    ctx.globalAlpha=.15+r()*.5;ctx.fillStyle='#f2fbff';
    ctx.beginPath();ctx.ellipse(px,py,4+r()*26,1+r()*5,0,0,Math.PI*2);ctx.fill();
  }ctx.globalAlpha=1;});
}

// gotas soltas na frente (foreground drops)
function drops(ctx,W,H,seed,n){
  const r=rng(seed||11);
  for(let i=0;i<(n||60);i++){
    const x=r()*W,y=r()*H,rad=2+Math.pow(r(),3)*16;
    const gr=ctx.createRadialGradient(x-rad*.3,y-rad*.3,0,x,y,rad);
    gr.addColorStop(0,'rgba(255,255,255,.95)');gr.addColorStop(.6,'rgba(220,245,250,.45)');gr.addColorStop(1,'rgba(220,245,250,0)');
    ctx.fillStyle=gr;ctx.beginPath();ctx.arc(x,y,rad,0,Math.PI*2);ctx.fill();
  }
}
