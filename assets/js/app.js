(()=>{const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
// theme
const root=document.documentElement;try{const t=localStorage.getItem('theme');if(t)root.dataset.theme=t}catch(e){}
$('#theme')?.addEventListener('click',()=>{const dark=root.dataset.theme!=='light';const n=dark?'light':'dark';root.dataset.theme=n;try{localStorage.setItem('theme',n)}catch(e){}});
// mobile menu
const bg=$('#burger'),lk=$('#links');bg?.addEventListener('click',()=>{const o=lk.classList.toggle('open');bg.setAttribute('aria-expanded',o)});
// cursor spotlight on glass cards
addEventListener('pointermove',e=>{const c=e.target.closest?.('.card,.stat,.file');if(!c)return;const r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px')},{passive:true});
// progress bar
const pr=$('#progress');addEventListener('scroll',()=>{const h=document.documentElement;pr.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight||1)*100)+'%'},{passive:true});
// reveal + counters
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.08});$$('.rv').forEach(el=>io.observe(el));
$$('[data-count]').forEach(el=>{const end=parseFloat(el.dataset.count),suf=el.dataset.suffix||'',dec=(el.dataset.count.split('.')[1]||'').length;const co=new IntersectionObserver(([e])=>{if(!e.isIntersecting)return;co.disconnect();const t0=performance.now();(function f(t){const p=Math.min(1,(t-t0)/1200);el.textContent=(end*(1-Math.pow(1-p,3))).toFixed(dec)+suf;if(p<1)requestAnimationFrame(f)})(t0)});co.observe(el)});
// YouTube facade
$$('.vid[data-yt]').forEach(v=>{const id=v.dataset.yt,b=v.firstElementChild;b.style.backgroundImage=`url(https://i.ytimg.com/vi/${id}/hqdefault.jpg)`;b.addEventListener('click',()=>{v.innerHTML=`<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0" title="${v.dataset.title||'Video'}" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>`})});
// lightbox
const lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.innerHTML='<span class="ct"></span><button class="x" aria-label="Close">×</button><button class="pv" aria-label="Previous">‹</button><img alt=""><p></p><button class="nx" aria-label="Next">›</button>';document.body.append(lb);
let grp=[],ix=0;const im=$('img',lb),cp=$('p',lb),ct=$('.ct',lb);
const show=i=>{ix=(i+grp.length)%grp.length;const a=grp[ix];im.src=a.href;im.alt=$('img',a)?.alt||'';cp.textContent=a.dataset.cap||im.alt;ct.textContent=(ix+1)+' / '+grp.length;$('.pv',lb).style.display=$('.nx',lb).style.display=grp.length>1?'':'none'};
const close=()=>{lb.classList.remove('open');im.src='';document.body.style.overflow=''};
document.addEventListener('click',e=>{const a=e.target.closest('a[data-lb]');if(!a)return;e.preventDefault();grp=$$('a[data-lb="'+a.dataset.lb+'"]').filter(x=>!x.closest('[hidden]'));show(grp.indexOf(a));lb.classList.add('open');document.body.style.overflow='hidden'});
lb.addEventListener('click',e=>{if(e.target===lb||e.target.matches('.x'))close();if(e.target.matches('.pv'))show(ix-1);if(e.target.matches('.nx'))show(ix+1)});
addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(ix-1);if(e.key==='ArrowRight')show(ix+1)});
let sx=0;lb.addEventListener('touchstart',e=>sx=e.touches[0].clientX,{passive:true});lb.addEventListener('touchend',e=>{const d=e.changedTouches[0].clientX-sx;if(Math.abs(d)>50)show(ix+(d<0?1:-1))});
// project filter + search
const chips=$$('.chip'),cards=$$('.proj'),q=$('#q');let cat='all';
const apply=()=>{const s=(q?.value||'').toLowerCase().trim();let n=0;cards.forEach(c=>{const ok=(cat==='all'||c.dataset.cat===cat)&&(!s||c.textContent.toLowerCase().includes(s));c.hidden=!ok;if(ok)n++});const m=$('#none');if(m)m.hidden=n>0};
chips.forEach(c=>c.addEventListener('click',()=>{cat=c.dataset.cat;chips.forEach(x=>x.setAttribute('aria-pressed',x===c));apply()}));q?.addEventListener('input',apply);
// files: link to local copy if it exists, else fall back to the old site
$$('a[data-file]').forEach(a=>{fetch(a.dataset.file,{method:'HEAD'}).then(r=>{if(r.ok){a.href=a.dataset.file;a.removeAttribute('data-missing');a.target='_blank'}}).catch(()=>{})});
})();
