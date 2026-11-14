/* Happy Fatora landing - all text is pre-rendered in HTML (SEO). This file only adds behaviour. */
(function(){
var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var LS={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};

/* Theme */
var THEME=document.documentElement.getAttribute('data-bs-theme')||'light';
function setTheme(t){THEME=t;LS.set('theme',t);document.documentElement.setAttribute('data-bs-theme',t);var i=$('#themeBtn i');if(i)i.className='bi '+(t==='dark'?'bi-sun':'bi-moon-stars')}
var tb0=$('#themeBtn');if(tb0){tb0.addEventListener('click',function(){setTheme(THEME==='dark'?'light':'dark')});setTheme(THEME)}

/* Marquee built from the visible use-case list */
var mq=$('#mq'),uses=$$('#useList li');
if(mq&&uses.length){var items=uses.map(function(li){return '<span class="mq-i"><i class="bi '+li.dataset.ic+'"></i><span>'+li.textContent.trim()+'</span></span>'});mq.innerHTML=items.concat(items,items,items).join('')}

/* Close mobile menu on click */
$$('#nav .nav-link').forEach(function(a){a.addEventListener('click',function(){if(window.bootstrap){var c=bootstrap.Collapse.getInstance($('#nav'));if(c)c.hide()}})});

/* Gallery arrows */
var gp=$('#gPrev'),gn=$('#gNext'),gal=$('#gal');
if(gp&&gn&&gal){gp.addEventListener('click',function(){gal.scrollBy({left:-280,behavior:'smooth'})});gn.addEventListener('click',function(){gal.scrollBy({left:280,behavior:'smooth'})})}

/* Reveal + counters */
if('IntersectionObserver' in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.15});
  $$('.rv').forEach(function(e){io.observe(e)});
  var count=function(el){var to=+el.dataset.count,suf=el.dataset.suf||'',t0=null;(function s(t){t0=t0||t;var p=Math.min((t-t0)/1400,1);el.textContent=Math.round(to*p)+(p===1?suf:'');if(p<1)requestAnimationFrame(s)})(performance.now())};
  var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){count(e.target);io2.unobserve(e.target)}})});
  $$('[data-count]').forEach(function(e){io2.observe(e)});
}else{$$('.rv').forEach(function(e){e.classList.add('in')})}

/* Hero phone tilt (desktop pointer only) */
var st=$('#stage'),hp=$('#heroPhone');
if(st&&hp&&matchMedia('(hover:hover)').matches){
  st.addEventListener('mousemove',function(e){var r=st.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;hp.style.transform='rotateY('+x*14+'deg) rotateX('+-y*14+'deg)'});
  st.addEventListener('mouseleave',function(){hp.style.transform=''});
}

/* Spotlight on cards, scroll progress, back-to-top, blob parallax */
document.addEventListener('mousemove',function(e){var c=e.target.closest&&e.target.closest('.fcard');if(c){var r=c.getBoundingClientRect();c.style.setProperty('--x',e.clientX-r.left+'px');c.style.setProperty('--y',e.clientY-r.top+'px')}});
var prog=$('#prog'),tb=$('#top2'),bl=$$('.blob');
addEventListener('scroll',function(){var h=document.documentElement,y=h.scrollTop;if(prog)prog.style.width=(y/(h.scrollHeight-h.clientHeight)*100)+'%';if(tb)tb.style.display=y>600?'grid':'none';bl.forEach(function(b,i){b.style.translate='0 '+(y*(i?-.08:.12))+'px'})},{passive:true});
if(tb)tb.addEventListener('click',function(){scrollTo({top:0,behavior:'smooth'})});
})();
