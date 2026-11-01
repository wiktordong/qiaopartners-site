# Builds index.html, pl/index.html, zh/index.html and SEO files from _src/content.py.
# Run from the repository root: python3 _src/build.py
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import L, LINKEDIN, EMAIL, CALENDLY_URL, WHATSAPP, FORM_ENDPOINT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://qiaopartners.eu/"
BASE_CSS = open(os.path.join(ROOT, "_src", "base.css"), encoding="utf-8").read()
e = html.escape

EXTRA_CSS = r"""

/* Language drop-down */
.langdd{position:relative}
.langdd summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;gap:8px;font-size:13px;letter-spacing:.06em;padding:6px 0;opacity:.78;transition:opacity .2s}
.langdd summary::-webkit-details-marker{display:none}
.langdd summary:hover,.langdd[open] summary{opacity:1}
.langdd summary i{width:6px;height:6px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:translateY(-2px) rotate(45deg);transition:transform .25s}
.langdd[open] summary i{transform:translateY(1px) rotate(-135deg)}
.langdd ul{position:absolute;right:-16px;top:calc(100% + 10px);list-style:none;margin:0;padding:4px 0 8px;min-width:0;background:var(--navy);text-align:right;z-index:30}
.langdd li a{display:block;padding:7px 16px;text-decoration:none;opacity:.6;font-size:13px;letter-spacing:.08em;white-space:nowrap;transition:opacity .2s,color .2s}
.langdd li a:hover{opacity:1}
.langdd li a[aria-current]{opacity:1;color:var(--baby)}
.nav .langdd ul{display:block;gap:0;font-size:14px}
.nav .langdd ul a::after{display:none}
/* Key figures: three across */
.figures .wrap.n3{grid-template-columns:repeat(3,minmax(0,1fr))}
@media (max-width:980px){.figures .wrap.n3{grid-template-columns:repeat(3,minmax(0,1fr))}.figures .wrap.n3 .fig:nth-child(3){padding-left:32px;border-left:1px solid var(--line)}}
@media (max-width:700px){.figures .wrap.n3{grid-template-columns:1fr;row-gap:40px}.figures .wrap.n3 .fig + .fig{padding-left:0;border-left:0;border-top:1px solid var(--line);padding-top:32px}}
.banner{background:var(--navy-2);color:var(--on-dark);font-size:14px;text-align:center}
.banner .wrap{padding-block:10px}
.banner a{text-decoration:none;display:inline-flex;align-items:center;gap:10px}
.banner i{width:8px;height:8px;border-radius:50%;background:#5FD08A;box-shadow:0 0 0 4px rgba(95,208,138,.2)}
.banner a:hover{color:var(--baby)}
.sec-cta{margin-top:40px}
/* Additions: language switch, buttons, services, steps, sectors, booking, FAQ, QR contact */
.nav-right{display:flex;align-items:center;gap:28px}
.lang{display:flex;gap:12px;font-size:13px;letter-spacing:.06em}
.lang a{text-decoration:none;opacity:.6}
.lang a:hover{opacity:1}
.lang a[aria-current]{opacity:1;color:var(--baby)}
.btn{display:inline-flex;align-items:center;gap:12px;background:transparent;color:inherit;border:1px solid currentColor;border-color:color-mix(in srgb,currentColor 55%,transparent);border-radius:999px;text-decoration:none;font-weight:400;font-size:15px;letter-spacing:.01em;padding:13px 28px;cursor:pointer;transition:background-color .35s ease,color .35s ease,border-color .35s ease}
.btn:hover,.btn:focus-visible{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.site .btn:hover,.hero .btn:hover,.site .btn:focus-visible,.hero .btn:focus-visible{background:var(--baby);color:var(--navy);border-color:var(--baby)}
.btn span{display:inline-block;transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.btn:hover span{transform:translateX(5px)}
.btn.small{padding:9px 20px;font-size:14px}
.btn:disabled{opacity:.5;cursor:default}
.hero .wrap > div{display:grid;gap:28px;justify-items:start}
@media (max-width:560px){.nav-right .btn.small{display:none}}

.svc{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 48px}
.svc article{border-top:1px solid var(--line);padding:28px 0 44px;display:grid;gap:12px;align-content:start}
.svc .n{font-size:13px;letter-spacing:.16em;color:var(--muted)}
.svc h3{font-size:24px;font-weight:400;letter-spacing:-.01em;line-height:1.2}
.svc p{color:var(--muted);font-size:16px;font-weight:300}
@media (max-width:980px){.svc{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:620px){.svc{grid-template-columns:1fr}}

.steps{background:var(--mist);border-block:1px solid var(--line)}
.steps .wrap{padding-block:110px}
.steps h2{font-size:clamp(32px,4vw,54px);line-height:1.08;margin-bottom:56px}
.steps ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));counter-reset:s}
.steps li{counter-increment:s;padding-right:32px;display:grid;gap:10px;align-content:start}
.steps li + li{padding-left:32px;border-left:1px solid var(--line)}
.steps li::before{content:"0" counter(s);font-size:clamp(40px,4vw,60px);font-weight:300;line-height:1;color:var(--baby)}
.steps h3{font-size:22px;font-weight:400}
.steps p{color:var(--muted);font-size:15px}
@media (max-width:980px){.steps ol{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:48px}.steps li:nth-child(3){padding-left:0;border-left:0}}
@media (max-width:560px){.steps ol{grid-template-columns:1fr}.steps li + li{padding-left:0;border-left:0;border-top:1px solid var(--line);padding-top:28px}.steps .wrap{padding-block:72px}}

.sectors{padding-block:140px}
.sectors .head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:80px;margin-bottom:56px;align-items:end}
.sectors h2{font-size:clamp(32px,4vw,54px);line-height:1.08}
.sectors .head p{color:var(--muted);font-size:19px;font-weight:300;max-width:46ch}
.sec{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:4px}
.sec .tag{justify-self:start;font-size:11px;letter-spacing:.16em;text-transform:uppercase;padding:4px 12px;border:1px solid rgba(142,197,240,.45);color:var(--baby);border-radius:999px}
.sec li[data-h="mid"]{background:var(--navy-2)}
.sec li[data-h="long"]{background:#173459}
.sec li{background:var(--navy);color:var(--on-dark);padding:32px 28px 36px;display:grid;gap:12px;align-content:start;min-height:220px}
.sec h3{font-size:22px;font-weight:400;line-height:1.2}
.sec p{color:var(--on-dark-muted);font-size:15px;font-weight:300}
@media (max-width:1100px){.sec{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:980px){.sectors .head{grid-template-columns:1fr;gap:20px}}
@media (max-width:560px){.sec{grid-template-columns:1fr}.sectors{padding-block:88px}.sec li{min-height:0}}

.book{background:var(--mist);border-block:1px solid var(--line)}
.book .wrap{padding-block:130px;display:grid;gap:56px}
.book .head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:80px;align-items:end}
.book h2{font-size:clamp(32px,4vw,54px);line-height:1.08}
.book .head p{color:var(--muted);font-size:19px;font-weight:300;max-width:46ch}
.book .panels{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:24px;align-items:start}
.panel{background:var(--paper);border:1px solid var(--line);padding:clamp(24px,3vw,40px);min-width:0}
.panel h3{font-size:22px;font-weight:400;margin-bottom:20px}
.enq{display:grid;grid-template-columns:1fr 1fr;gap:20px 20px;align-items:end}
.enq .full{grid-column:1/-1}
.enq label{display:grid;gap:8px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.enq input,.enq select,.enq textarea{font:inherit;font-size:16px;letter-spacing:0;text-transform:none;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:2px;padding:12px 14px;width:100%;min-width:0}
.enq select{appearance:none;-webkit-appearance:none;background-image:linear-gradient(45deg,transparent 50%,var(--muted) 50%),linear-gradient(135deg,var(--muted) 50%,transparent 50%);background-position:calc(100% - 20px) 52%,calc(100% - 15px) 52%;background-size:5px 5px;background-repeat:no-repeat;padding-right:40px}
.enq textarea{min-height:110px;resize:vertical}
.enq input:focus,.enq select:focus,.enq textarea:focus{outline:none;border-color:var(--baby);box-shadow:0 0 0 3px rgba(142,197,240,.3)}
.enq .actions{display:flex;flex-wrap:wrap;align-items:center;gap:16px 24px}
.enq .actions small{font-size:13px;color:var(--muted)}
.enq button{border:0;cursor:pointer;font:inherit}
.enq .hp{position:absolute;left:-9999px}
.enq-status{margin-top:20px;font-size:16px;padding:14px 16px;border-left:3px solid var(--baby);background:var(--mist)}
.enq-status.err{border-left-color:#C2513F}
.cal{min-height:640px}
.cal .ph{border:1px dashed var(--line);min-height:560px;display:grid;place-items:center;text-align:center;color:var(--muted);padding:24px;font-size:15px}
.calendly-inline-widget{min-width:280px;height:660px;position:relative}
.calendly-inline-widget:empty::before{content:attr(data-loading);position:absolute;inset:0;display:grid;place-items:center;color:var(--muted);font-size:15px}
@media (max-width:980px){.book .panels{grid-template-columns:1fr}.book .head{grid-template-columns:1fr;gap:20px}}
@media (max-width:620px){.enq{grid-template-columns:1fr}.book .wrap{padding-block:88px}}

.faq{padding-block:140px}
.faq .wrap{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:80px;align-items:start}
.faq h2{font-size:clamp(32px,4vw,54px);line-height:1.08}
.faq details{border-top:1px solid var(--line)}
.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:24px 40px 24px 0;font-size:20px;font-weight:400;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:4px;top:20px;font-size:26px;font-weight:300;color:var(--baby);transition:transform .3s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{color:var(--muted);font-size:17px;font-weight:300;padding:0 0 28px;max-width:62ch}
@media (max-width:900px){.faq{padding-block:88px}.faq .wrap{grid-template-columns:1fr;gap:32px}}

.contact .wrap{align-items:start}
.qr{display:flex;flex-wrap:wrap;gap:28px;margin-top:8px}
.qr figure{margin:0;display:grid;gap:10px;justify-items:start;width:160px}
.qr img,.qr .ph{width:160px;height:160px;border:1px solid var(--line);background:#fff}
.qr .ph{display:grid;place-items:center;text-align:center;font-size:12px;color:#5A687B;padding:12px;border-style:dashed}
.qr figcaption{font-size:13px;color:var(--muted)}
:lang(zh-CN) body,:lang(zh-CN) h1,:lang(zh-CN) h2{font-family:"Hanken Grotesk","Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif}
:lang(zh-CN) .hero h1{font-weight:400;letter-spacing:0}
:lang(zh-CN) h2{font-weight:400;letter-spacing:0}
"""

SCRIPT = r"""
<script>
(function(){
  var root=document.documentElement;
  var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
  var h1=document.querySelector('.hero h1');
  if(h1&&!still){
    var words=h1.textContent.trim().split(/\s+/);
    h1.setAttribute('aria-label',h1.textContent.trim());
    h1.innerHTML=words.map(function(w,i){return '<span class="w" aria-hidden="true"><span style="--i:'+i+'">'+w+'</span></span>'}).join(' ');
  }
  function tag(list,kind,base,step){list.forEach(function(el,i){el.setAttribute('data-reveal',kind||'');el.style.setProperty('--d',((base||0)+i*(step||0.12)).toFixed(2)+'s')})}
  tag($('.strip figure'),'mask',0.45,0.12);
  tag($('.intro h2, .intro p'),'',0,0.14);
  tag($('.quote .mark, .quote blockquote, .quote cite'),'',0,0.18);
  tag($('.team .photo'),'mask',0,0);
  tag($('.team h2, .team .wrap > div > p, .pedigree, .team .link'),'',0.15,0.12);
  tag($('.fig'),'',0,0.12);
  tag($('.practice h2, .practice .head p'),'',0,0.12);
  tag($('.svc article'),'',0,0.08);
  tag($('.steps h2, .steps li'),'',0,0.1);
  tag($('.sectors h2, .sectors .head p'),'',0,0.12);
  tag($('.sec li'),'',0,0.07);
  tag($('.book h2, .book .head p, .book .panel'),'',0,0.12);
  tag($('.faq h2, .faq details'),'',0,0.05);
  tag($('.contact h2, .contact dl > div'),'',0,0.12);
  tag($('footer .wrap'),'',0,0);
  function countUp(b){
    var t=b.firstChild; if(!t||t.nodeType!==3) return;
    var m=t.nodeValue.match(/^(\D*)([\d.,]+)(.*)$/); if(!m) return;
    var sep=m[2].indexOf(',')>=0?',':'.';
    var pre=m[1],end=parseFloat(m[2].replace(',','.')),dec=(m[2].split(sep)[1]||'').length,post=m[3],dur=1800,start=null;
    function fmt(v){return v.toFixed(dec).replace('.',sep)}
    function step(now){
      if(start===null) start=now;
      var k=Math.min(1,(now-start)/dur),ez=1-Math.pow(1-k,4);
      t.nodeValue=pre+fmt(end*ez)+post;
      if(k<1) requestAnimationFrame(step);
    }
    t.nodeValue=pre+fmt(0)+post;
    requestAnimationFrame(step);
  }
  function show(el){
    el.classList.add('in');
    if(el.classList.contains('fig')&&!el.hasAttribute('data-nocount')&&!still){var b=el.querySelector('b');if(b)countUp(b)}
    setTimeout(function(){el.style.setProperty('--d','0s')},2600);
  }
  var targets=$('[data-reveal]');
  if(still||!('IntersectionObserver' in window)){targets.forEach(function(el){el.classList.add('in')})}
  else{
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){if(en.isIntersecting){show(en.target);io.unobserve(en.target)}});
    },{threshold:0.12,rootMargin:'0px 0px -6% 0px'});
    targets.forEach(function(el){io.observe(el)});
  }
  var header=document.querySelector('.site'),bar=document.querySelector('.progress');
  var ticking=false;
  function frame(){
    ticking=false;
    var y=window.scrollY||window.pageYOffset,max=document.documentElement.scrollHeight-window.innerHeight;
    if(header) header.classList.toggle('scrolled',y>40);
    if(bar) bar.style.transform='scaleX('+(max>0?Math.min(1,y/max):0)+')';
  }
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(frame)}},{passive:true});
  window.addEventListener('resize',frame);
  frame();
  var f=document.getElementById('enquiry');
  if(f){
    f.addEventListener('submit',function(ev){
      ev.preventDefault();
      var ok=document.getElementById('enq-ok'),err=document.getElementById('enq-err');
      ok.hidden=true;err.hidden=true;
      if(!f.checkValidity()){f.reportValidity();return}
      var d={};new FormData(f).forEach(function(v,k){d[k]=v});
      if(d._honey) return;
      d._subject='Qiao Partners enquiry: '+(d.company||'')+' / '+(d.looking_for||'');
      d._template='table'; d.page=location.pathname;
      var btn=f.querySelector('button');btn.disabled=true;
      fetch(f.getAttribute('data-endpoint'),{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(d)})
        .then(function(r){if(!r.ok) throw new Error(r.status);return r.json()})
        .then(function(){
          f.reset();ok.hidden=false;
          var w=document.getElementById('cal-widget');
          if(w&&window.Calendly){w.innerHTML='';window.Calendly.initInlineWidget({url:w.getAttribute('data-url'),parentElement:w,prefill:{name:d.name,email:d.email}})}
        })
        .catch(function(){err.hidden=false})
        .then(function(){btn.disabled=false});
    });
  }
  requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.add('loaded')})});
})();
</script>"""

LOGO = '''<a class="logo" href="{home}" aria-label="Qiao Partners">
      <svg viewBox="0 0 108 50" aria-hidden="true">
        <path pathLength="100" d="M12 16 Q54 -10 96 16" fill="none" stroke="#8EC5F0" stroke-width="2.4" stroke-linecap="round"/>
        <text class="word" x="0" y="48" textLength="108" lengthAdjust="spacing">QIAO</text>
      </svg>
      <span class="partners">Partners</span>
    </a>'''

def page(key):
    c = L[key]
    up = "../" if c["path"] else ""
    home = up or "./"
    alts = "\n".join(f'<link rel="alternate" hreflang="{L[k]["lang"]}" href="{SITE}{L[k]["path"]}">' for k in L) + \
        f'\n<link rel="alternate" hreflang="x-default" href="{SITE}">'
    same_as = [LINKEDIN]
    org = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Qiao Partners",
           "url": SITE, "logo": SITE + "favicon-192.png", "email": EMAIL,
           "description": L["en"]["desc"], "areaServed": ["PL", "EU", "CN"],
           "knowsLanguage": ["zh", "pl", "en"], "sameAs": same_as,
           "address": [{"@type": "PostalAddress", "addressLocality": "Warsaw", "addressCountry": "PL"},
                       {"@type": "PostalAddress", "addressLocality": "Beijing", "addressCountry": "CN"}],
           "founder": {"@type": "Person", "name": "Wiktor Dong"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": c["lang"],
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
    ld = f'<script type="application/ld+json">{json.dumps(org, ensure_ascii=False)}</script>\n<script type="application/ld+json">{json.dumps(faq, ensure_ascii=False)}</script>'
    fonts = "family=Hanken+Grotesk:wght@300;400;500;600&family=Noto+Serif+SC:wght@500" + ("&family=Noto+Sans+SC:wght@300;400;500" if key == "zh" else "")
    links = []
    for k in L:
        href = (up + L[k]["path"]) or "./"
        cur = ' aria-current="page"' if k == key else ""
        links.append(f'<li><a href="{href}"{cur} hreflang="{L[k]["lang"]}" lang="{L[k]["lang"]}">{L[k]["label"]}</a></li>')
    lang_links = f'<details class="langdd"><summary aria-label="Language">{L[key]["label"]}<i aria-hidden="true"></i></summary><ul>{"".join(links)}</ul></details>'
    ids = ["about", "services", "sectors", "faq", "contact"]
    nav = "".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t in zip(ids, c["nav"]))
    strip_imgs = [("wind-aerial.jpg", "Wind turbine among green fields, seen from above", "60% 50%"),
                  ("terminal.jpg", "Gas terminal and jetty by the sea, seen from above", "55% 50%"),
                  ("sprayer.jpg", "Tractor working a maize field at sunset", "50% 50%"),
                  ("truck.jpg", "Lorry on an open road at dusk", "50% 50%")]
    strip = "".join(f'<figure><img src="{up}img/{f}" alt="{e(a)}" style="object-position:{p}"><figcaption>{e(cap)}</figcaption></figure>'
                    for (f, a, p), cap in zip(strip_imgs, c["strip"]))
    figs = "".join(f'<div class="fig"{" data-nocount" if nc else ""}><b>{b}</b><span>{e(t)}</span>' + (f'<span class="src">{e(s)}</span>' if s else "") + "</div>"
                   for b, t, s, nc in c["figs"])
    svc = "".join(f'<article><span class="n">0{i+1}</span><h3>{e(h)}</h3><p>{e(p)}</p></article>' for i, (h, p) in enumerate(c["svc"]))
    steps = "".join(f'<li><h3>{e(h)}</h3><p>{e(p)}</p></li>' for h, p in c["steps"])
    sec = "".join(f'<li data-h="{t}"><span class="tag">{e(c["tags"][t])}</span><h3>{e(h)}</h3><p>{e(p)}</p></li>' for h, p, t in c["sec"])
    faqs = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in c["faq"])
    opts = lambda items: f'<option value="" disabled selected>{e(c["f_choose"])}</option>' + "".join(f'<option>{e(o)}</option>' for o in items)
    form = f"""<form class="enq" id="enquiry" data-endpoint="{e(FORM_ENDPOINT)}" novalidate>
          <label>{e(c["f_company"])}<input id="f-company" name="company" required autocomplete="organization"></label>
          <label>{e(c["f_name"])}<input id="f-name" name="name" required autocomplete="name"></label>
          <label>{e(c["f_email"])}<input id="f-email" name="email" type="email" required autocomplete="email"></label>
          <label>{e(c["f_phone"])}<input id="f-phone" name="phone" autocomplete="tel"></label>
          <label>{e(c["f_country"])}<input id="f-country" name="country" autocomplete="country-name"></label>
          <label>{e(c["f_size"])}<select id="f-size" name="company_size">{opts(c["sizes"])}</select></label>
          <label>{e(c["f_industry"])}<select id="f-industry" name="industry" required>{opts(c["industries"])}</select></label>
          <label>{e(c["f_need"])}<select id="f-need" name="looking_for" required>{opts(c["needs"])}</select></label>
          <label class="full">{e(c["f_msg"])}<textarea id="f-msg" name="message"></textarea></label>
          <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="full actions"><button class="btn" type="submit">{e(c["f_submit"])} <span aria-hidden="true">→</span></button><small>{e(c["f_note"])}</small></div>
        </form>
        <p class="enq-status" id="enq-ok" role="status" hidden>{e(c["f_ok"])}</p>
        <p class="enq-status err" id="enq-err" role="alert" hidden>{e(c["f_err"])}</p>"""
    if CALENDLY_URL:
        cal = f'<div class="calendly-inline-widget" id="cal-widget" data-loading="{e(c["cal_loading"])}" data-url="{e(CALENDLY_URL)}?hide_gdpr_banner=1&amp;primary_color=0a1c36"></div><script src="https://assets.calendly.com/assets/external/widget.js" async></script>'
    else:
        cal = f'<div class="ph">{e(c["cal_ph"])}</div>'
    slot = f"""<div class="panels">
        <div class="panel">{form}</div>
        <div class="panel cal"><h3>{e(c["cal_h"])}</h3>{cal}</div>
      </div>"""
    if WHATSAPP:
        wa = f'<figure><a href="{WHATSAPP}" rel="noopener" target="_blank"><img src="{up}img/whatsapp-qr.png" alt="WhatsApp QR code"></a><figcaption>{e(c["scan_wa"])}</figcaption></figure>'
    else:
        wa = f'<figure><div class="ph">{e(c["wa_pending"])}</div><figcaption>{e(c["scan_wa"])}</figcaption></figure>'
    return f'''<!doctype html>
<html lang="{c["lang"]}">
<head>
<meta charset="utf-8">
<style>html,body{{margin:0;padding:0}}</style>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(c["title"])}</title>
<meta name="description" content="{e(c["desc"])}">
<link rel="canonical" href="{SITE}{c["path"]}">
{alts}
<meta property="og:title" content="{e(c["title"])}">
<meta property="og:description" content="{e(c["desc"])}">
<meta property="og:url" content="{SITE}{c["path"]}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE}img/wind-aerial.jpg">
<link rel="icon" href="{up}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{up}favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{up}favicon-192.png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
{ld}
<style>
{BASE_CSS}
{EXTRA_CSS}
</style>
<script>document.documentElement.classList.add('js')</script>
</head>
<body>

<div class="banner"><div class="wrap"><a href="#book"><i aria-hidden="true"></i>{e(c["banner"])} <span aria-hidden="true">→</span></a></div></div>

<header class="site">
  <div class="wrap nav">
    {LOGO.format(home=home)}
    <ul>{nav}</ul>
    <div class="nav-right">
      <nav class="lang" aria-label="Language">{lang_links}</nav>
      <a class="btn small" href="#book">{e(c["cta"])}</a>
    </div>
  </div>
  <div class="progress" aria-hidden="true"></div>
</header>

<main id="top">
  <section class="hero">
    <div class="wrap">
      <h1>{e(c["h1"])}</h1>
      <div>
        <p>{e(c["hero_p"])}</p>
        <a class="btn" href="#book">{e(c["hero_cta"])} <span aria-hidden="true">→</span></a>
      </div>
    </div>
    <div class="strip">{strip}</div>
  </section>

  <section class="intro" id="about">
    <div class="wrap">
      <h2>{e(c["about_h"])}</h2>
      <div>{"".join(f"<p>{e(p)}</p>" for p in c["about_p"])}</div>
    </div>
  </section>

  <section class="quote">
    <div class="wrap">
      <div class="mark" lang="zh">桥</div>
      <div>
        <blockquote>{e(c["quote"])}</blockquote>
        <cite><b>Qiao Partners</b></cite>
      </div>
    </div>
  </section>

  <section class="practice" id="services">
    <div class="wrap">
      <div class="head">
        <h2>{e(c["svc_h"])}</h2>
        <p>{e(c["svc_p"])}</p>
      </div>
      <div class="svc">{svc}</div>
      <div class="sec-cta"><a class="btn" href="#book">{e(c["svc_cta"])} <span aria-hidden="true">→</span></a></div>
    </div>
  </section>

  <section class="steps">
    <div class="wrap">
      <h2>{e(c["steps_h"])}</h2>
      <ol>{steps}</ol>
    </div>
  </section>

  <section class="sectors" id="sectors">
    <div class="wrap">
      <div class="head">
        <h2>{e(c["sec_h"])}</h2>
        <p>{e(c["sec_p"])}</p>
      </div>
      <ul class="sec">{sec}</ul>
      <div class="sec-cta"><a class="btn" href="#book">{e(c["sec_cta"])} <span aria-hidden="true">→</span></a></div>
    </div>
  </section>

  <section class="team" id="team">
    <div class="wrap">
      <div class="photo"><img src="{up}img/meeting.jpg" alt="Team meeting in an office with a city view"></div>
      <div>
        <h2>{e(c["team_h"])}</h2>
        <p>{e(c["team_p"])}</p>
        <div class="pedigree">
          <span class="kicker">{e(c["kicker"])}</span>
          <ul><li>Goldman Sachs</li><li>J.P. Morgan</li><li>Tencent</li><li>Accenture</li></ul>
        </div>
        <a class="link" href="#book">{e(c["work"])} <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </section>

  <section class="figures" aria-label="Key figures">
    <div class="wrap n{len(c['figs'])}">{figs}</div>
  </section>

  <section class="book" id="book">
    <div class="wrap">
      <div class="head">
        <h2>{e(c["book_h"])}</h2>
        <p>{e(c["book_p"])}</p>
      </div>
      {slot}
    </div>
  </section>

  <section class="faq" id="faq">
    <div class="wrap">
      <h2>{e(c["faq_h"])}</h2>
      <div>{faqs}</div>
    </div>
  </section>

  <section class="contact" id="contact">
    <div class="wrap">
      <div>
        <h2>{e(c["contact_h"])}</h2>
        <div class="qr">
          <figure><img src="{up}img/wechat-qr.jpg" alt="WeChat QR code for Qiao Partners"><figcaption>{e(c["scan_wechat"])}</figcaption></figure>
          {wa}
        </div>
      </div>
      <dl>
        <div><dt>{e(c["c_email"])}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>{e(c["c_li"])}</dt><dd><a href="{LINKEDIN}" rel="noopener" target="_blank">{e(c["c_li_txt"])}</a></dd></div>
        <div><dt>{e(c["c_eu"])}</dt><dd>{e(c["c_eu_v"])}</dd></div>
        <div><dt>{e(c["c_as"])}</dt><dd>{e(c["c_as_v"])}</dd></div>
      </dl>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    {LOGO.format(home=home)}
    <span>{e(c["foot"])}</span>
  </div>
</footer>
{SCRIPT}
<script>
(function(){{
  var faqs=document.querySelectorAll('.faq details');
  faqs.forEach(function(d){{d.addEventListener('toggle',function(){{if(d.open){{faqs.forEach(function(o){{if(o!==d)o.open=false}})}}}})}});
  var dd=document.querySelector('.langdd');
  if(dd){{
    document.addEventListener('click',function(ev){{if(dd.open&&!dd.contains(ev.target))dd.open=false}});
    document.addEventListener('keydown',function(ev){{if(ev.key==='Escape'&&dd.open){{dd.open=false;dd.querySelector('summary').focus()}}}});
  }}
}})();
</script>
</body>
</html>
'''

def main():
    for k, c in L.items():
        out = os.path.join(ROOT, c["path"], "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(page(k))
    open(os.path.join(ROOT, "robots.txt"), "w").write(
        "User-agent: *\nAllow: /\n\n# AI assistants and search crawlers are welcome\n"
        "User-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\n"
        "User-agent: Google-Extended\nAllow: /\n\nSitemap: https://qiaopartners.eu/sitemap.xml\n")
    urls = "".join(f"  <url><loc>{SITE}{c['path']}</loc></url>\n" for c in L.values())
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    en = L["en"]
    llms = ["# Qiao Partners", "", f"> {en['desc']}", "",
            "Qiao Partners is a commercial advisory firm based in Warsaw, Poland, with a presence in Beijing. It helps Chinese manufacturers enter the European market and European companies set up in China. It does not invest or give investment advice.", "",
            "## Services"] + [f"- {h}: {p}" for h, p in en["svc"]] + ["", "## Market trends we track (to 2035)"] + \
           [f"- {h} ({en["tags"][t]}): {p}" for h, p, t in en["sec"]] + ["", "## Pages",
            f"- [English]({SITE})", f"- [Polski]({SITE}pl/)", f"- [中文]({SITE}zh/)", "", "## Contact",
            f"- Email: {EMAIL}", f"- LinkedIn: {LINKEDIN}", "- WeChat: QR code on the website", f"- WhatsApp: {WHATSAPP}", ""]
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(llms))
    print("built", list(L))

if __name__ == "__main__":
    main()
