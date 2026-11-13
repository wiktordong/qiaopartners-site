"""Shared page chrome for every page on qiaopartners.eu: <head>, header, footer, network art and site script.
Used by build.py (main pages) and insights/build_insights.py (Insights), so the whole site looks the same."""
import hashlib, html, json, math, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from settings import SITE, EMAIL, LINKEDIN, WHATSAPP, MEMBERS, GOOGLE_SITE_VERIFICATION, BING_SITE_VERIFICATION  # noqa: E402
from lang import en, pl, zh, ru  # noqa: E402

e = html.escape
L = {"en": en.C, "pl": pl.C, "zh": zh.C, "ru": ru.C}
SLUG = {"home": "", "about": "about/", "services": "services/", "industries": "industries/",
        "insights": "insights/", "contact": "contact/", "china": "china-entry/"}


def url(k, page, anchor=""):
    return "/" + L[k]["path"] + SLUG[page] + (f"#{anchor}" if anchor else "")


def css_href():
    p = os.path.join(ROOT, "assets", "site.css")
    v = hashlib.md5(open(p, "rb").read()).hexdigest()[:8] if os.path.exists(p) else "1"
    return f"/assets/site.css?v={v}"


def write_css():
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    css = open(os.path.join(HERE, "fonts.css"), encoding="utf-8").read() + "\n" + open(os.path.join(HERE, "site.css"), encoding="utf-8").read()
    open(os.path.join(ROOT, "assets", "site.css"), "w", encoding="utf-8").write(css)


LOGO = '''<a class="logo" href="{home}" aria-label="Qiao Partners — {homelabel}">
      <svg viewBox="0 0 108 50" aria-hidden="true"><path pathLength="100" d="M12 16 Q54 -10 96 16" fill="none" stroke="#C2A47A" stroke-width="2.4" stroke-linecap="round"/>
      <text class="word" x="0" y="48" textLength="108" lengthAdjust="spacing">QIAO</text></svg><span class="partners">Partners</span></a>'''


def logo(k):
    return LOGO.format(home=url(k, "home"), homelabel=e(L[k]["nav"]["home"]))


def network(seed=7, w=1600, h=1000, cls="net", pylon=(1260, 250), deck=((760, 840), (1700, 740)), n=40, area=(860, 30, 1600, 980)):
    """Abstract constellation plus a cable-stayed fan: the bridge idea without a literal bridge drawing."""
    rnd = random.Random(seed)
    pts = [(rnd.uniform(area[0], area[2]), rnd.uniform(area[1], area[3])) for _ in range(n)]
    lines = set()
    for i, p in enumerate(pts):
        near = sorted(range(len(pts)), key=lambda j: (pts[j][0] - p[0]) ** 2 + (pts[j][1] - p[1]) ** 2)[1:3]
        for j in near:
            lines.add(tuple(sorted((i, j))))
    out = [f'<svg class="{cls}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false"><g class="drift">']
    for i, j in lines:
        (x1, y1), (x2, y2) = pts[i], pts[j]
        out.append(f'<line class="l" x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}"/>')
    for x, y in pts:
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.choice([1.6, 2, 2.4, 3]):.1f}"/>')
    out.append('</g><g class="drift2">')
    (dx1, dy1), (dx2, dy2) = deck
    px, py = pylon
    for i_, t in enumerate([i / 13 for i in range(14)]):
        x, y = dx1 + (dx2 - dx1) * t, dy1 + (dy2 - dy1) * t
        bronze = " b" if i_ in (0, 13) else ""
        out.append(f'<line class="l{bronze}" x1="{px}" y1="{py}" x2="{x:.0f}" y2="{y:.0f}"/>')
    out.append(f'<line class="l b" x1="{dx1}" y1="{dy1}" x2="{dx2}" y2="{dy2}"/>')
    out.append(f'<line class="l" x1="{px}" y1="{py - 120}" x2="{px + 30}" y2="{dy1 + (dy2 - dy1) * ((px + 30 - dx1) / (dx2 - dx1)) + 60:.0f}"/>')
    out.append(f'<circle class="h pulse" cx="{px}" cy="{py}" r="9"/><circle class="b" cx="{px}" cy="{py}" r="3.2"/></g></svg>')
    return "".join(out)


ICON = {
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.15c0-1.23-.02-2.81-1.71-2.81-1.72 0-1.98 1.34-1.98 2.72V21h-4z"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.25-.12-1.46-.72-1.69-.8-.23-.08-.39-.12-.56.12-.16.25-.64.8-.78.97-.14.16-.29.18-.54.06a6.7 6.7 0 0 1-3.32-2.9c-.25-.43.25-.4.71-1.33.08-.16.04-.3-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.42h-.48a.92.92 0 0 0-.67.31 2.8 2.8 0 0 0-.87 2.08 4.9 4.9 0 0 0 1.02 2.58 11.2 11.2 0 0 0 4.29 3.79c1.6.69 2.22.75 3.02.63.49-.07 1.46-.6 1.67-1.18.2-.58.2-1.07.14-1.18-.06-.1-.22-.16-.47-.28z"/></svg>',
    "wechat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M9.2 3C4.9 3 1.5 5.9 1.5 9.4c0 2 1.1 3.8 2.9 5l-.7 2.2 2.6-1.4c.9.3 1.9.5 2.9.5h.6a5.8 5.8 0 0 1-.2-1.6c0-3.3 3.2-6 7.1-6h.6C16.6 5.2 13.2 3 9.2 3zM6.6 6.6a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm5.2 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2zM16.7 9.4c-3.4 0-6.1 2.3-6.1 5.1s2.7 5.1 6.1 5.1c.7 0 1.4-.1 2.1-.3l2.1 1.1-.6-1.8c1.5-1 2.5-2.5 2.5-4.1 0-2.8-2.7-5.1-6.1-5.1zm-2 2.6a.85.85 0 1 1 0 1.7.85.85 0 0 1 0-1.7zm4 0a.85.85 0 1 1 0 1.7.85.85 0 0 1 0-1.7z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" d="M3 5.5h18v13H3zM3.5 6l8.5 7 8.5-7"/></svg>',
}


def social(k, cls="social"):
    c = L[k]
    return (f'<ul class="{cls}" aria-label="{e(c["f_social"])}">'
            f'<li><a href="{LINKEDIN}" rel="noopener" target="_blank" aria-label="LinkedIn">{ICON["linkedin"]}<span>LinkedIn</span></a></li>'
            f'<li><a href="{WHATSAPP}" rel="noopener" target="_blank" aria-label="WhatsApp">{ICON["whatsapp"]}<span>WhatsApp</span></a></li>'
            f'<li><button type="button" class="wx-open" aria-haspopup="dialog" aria-label="WeChat">{ICON["wechat"]}<span>WeChat</span></button></li>'
            f'<li><a href="mailto:{EMAIL}" aria-label="Email">{ICON["mail"]}<span>Email</span></a></li></ul>')


def wechat_dialog(k):
    c = L[k]
    return (f'<dialog class="wx" id="wx"><form method="dialog"><img src="/img/wechat-qr.jpg" alt="WeChat QR code — Qiao Partners" width="260" height="260">'
            f'<p>{e(c["f_scan"])}</p><button class="btn small" value="close">{e(c["f_close"])}</button></form></dialog>')


def lang_switch(k, paths):
    items = "".join(f'<li><a href="{paths[x]}" hreflang="{L[x]["lang"]}" lang="{L[x]["lang"]}"{" aria-current=\"true\"" if x == k else ""}>{L[x]["name"]}</a></li>' for x in L)
    return f'<details class="dd"><summary aria-label="{e(L[k]["lang_label"])}">{L[k]["label"]}<i aria-hidden="true"></i></summary><ul>{items}</ul></details>'


def header(k, page, paths, has_ins):
    c = L[k]
    keys = ["home", "about", "services", "industries"] + (["insights"] if has_ins else []) + ["contact"]
    links = "".join(f'<a href="{url(k, p)}"{" aria-current=\"page\"" if p == page else ""}>{e(c["nav"][p])}</a>' for p in keys)
    cta = f'<a class="btn small" href="{url(k, "contact")}">{e(c["nav_cta"])}</a>'
    mnav = (f'<details class="mnav"><summary aria-label="{e(c["menu"])}"><i aria-hidden="true"></i></summary>'
            f'<div class="panel">{links}<a class="btn" href="{url(k, "contact")}">{e(c["nav_cta"])}</a></div></details>')
    return f'''<a class="skip" href="#main">{e(c["skip"])}</a>
<header class="site">
  <div class="wrap nav">
    {logo(k)}
    <nav class="menu" aria-label="Main">{links}</nav>
    <div class="nav-r">{lang_switch(k, paths)}{cta}{mnav}</div>
  </div>
  <div class="progress" aria-hidden="true"></div>
</header>'''


def member_logo(k, dark=True, cls=""):
    out = []
    for m in MEMBERS:
        f = f'img/members/{m["slug"]}{"-dark" if dark else ""}.png'
        if not os.path.exists(os.path.join(ROOT, f)):
            f = f'img/members/{m["slug"]}.png'
        if os.path.exists(os.path.join(ROOT, f)):
            out.append(f'<img class="{cls}" src="/{f}" alt="{e(m["name"])}: {e(m["full"][k])}" width="1000" height="283" loading="lazy">')
        else:
            out.append(f'<b>{e(m["name"])}</b>')
    return "".join(out)


def footer(k, has_ins):
    c = L[k]
    svc = "".join(f'<li><a href="{url(k, "services", s["id"])}">{e(s["title"])}</a></li>' for s in c["services"])
    svc += f'<li><a href="{url(k, "china")}">{e(c["f_eu2cn"])}</a></li>'
    comp_keys = ["about", "industries"] + (["insights"] if has_ins else []) + ["contact"]
    comp = "".join(f'<li><a href="{url(k, p)}">{e(c["nav"][p])}</a></li>' for p in comp_keys)
    return f'''<footer>
  <div class="wrap">
    <div class="fgrid">
      <div class="brand">{logo(k)}<p>{e(c["f_tag"])}</p>{social(k)}<div class="member">{member_logo(k, True)}</div><p class="muted" style="color:var(--on-dark-3);font-size:13px">{e(c["f_member"])}</p></div>
      <div><h4>{e(c["f_services"])}</h4><ul>{svc}</ul></div>
      <div><h4>{e(c["f_company"])}</h4><ul>{comp}</ul></div>
      <div><h4>{e(c["f_contact"])}</h4><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{LINKEDIN}" rel="noopener" target="_blank">LinkedIn</a></li><li><a href="{WHATSAPP}" rel="noopener" target="_blank">{e(c["f_whatsapp"])}</a></li><li>{e(c["f_base"])}</li></ul>
        <div class="fqr"><figure class="qr"><img src="/img/wechat-qr.jpg" alt="WeChat QR code — Qiao Partners" loading="lazy"><figcaption>WeChat</figcaption></figure><figure class="qr"><a href="{WHATSAPP}" rel="noopener" target="_blank"><img src="/img/whatsapp-qr.png" alt="WhatsApp QR code — Qiao Partners" loading="lazy"></a><figcaption>WhatsApp</figcaption></figure></div></div>
    </div>
    <div class="flegal"><p>{e(c["f_legal"])}</p><p>{e(c["f_copy"])}</p></div>
  </div>
</footer>'''


SCRIPT = r"""<script>
(function(){
  var d=document,root=d.documentElement;
  var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $=function(s,c){return Array.prototype.slice.call((c||d).querySelectorAll(s))};
  if(!still){var n=0;$('.hero h1 > span, .phero h1').forEach(function(el){
    var t=el.textContent.trim();el.setAttribute('aria-label',t);
    var zh=root.lang.indexOf('zh')===0,parts=zh?t.replace(/([，。、])/g,'$1\u0001').split('\u0001').filter(Boolean):t.split(/\s+/);
    el.innerHTML=parts.map(function(w){return '<span class="w" aria-hidden="true"><span style="--i:'+(n++)+'">'+w+'</span></span>'}).join(root.lang.indexOf('zh')===0?'':' ');
  });}
  function tag(sel,kind,step,base){$(sel).forEach(function(el,i){el.setAttribute('data-r',kind||'');el.style.setProperty('--d',((base||0)+Math.min(i,6)*(step||0)).toFixed(2)+'s')})}
  tag('.strip a','mask',0.12,0.5);tag('.cred-pic, .banner-pic, .idet .pic','mask',0);tag('.ind','mask',0.1);tag('.art .pic','mask',0.1);
  tag('.shead > div > *, .shead > div > p',0,0.08);tag('.fact','',0.08);tag('.svc','',0.08);tag('.stage','',0.1);tag('.diff','',0.06);tag('.cmp','',0);
  tag('.sig','',0.06);tag('.quote blockquote, .quote cite, .quote .mark','',0.18);tag('.tl-row','',0.08);tag('.sdet','',0);tag('.idet .txt','',0);tag('.split','',0);tag('.grid-list li','',0.05);tag('.next li','',0.08);tag('.faq details','',0.04);tag('.final .wrap > *','',0.12);
  function countUp(b){var t=b.firstChild;if(!t||t.nodeType!==3)return;var m=t.nodeValue.match(/^(\D*)(\d+)(.*)$/);if(!m)return;
    var end=+m[2],start=null,dur=1800;function step(now){if(start===null)start=now;var k=Math.min(1,(now-start)/dur),ez=1-Math.pow(1-k,4);t.nodeValue=m[1]+Math.round(end*ez)+m[3];if(k<1)requestAnimationFrame(step)}
    t.nodeValue=m[1]+'0'+m[3];requestAnimationFrame(step)}
  function show(el){el.classList.add('in');if(el.classList.contains('fact')&&!still){var b=el.querySelector('dd.big');if(b)countUp(b)}}
  var t=$('[data-r]');
  if(still||!('IntersectionObserver' in window)){t.forEach(function(el){el.classList.add('in')})}
  else{var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){show(x.target);io.unobserve(x.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});t.forEach(function(el){io.observe(el)})}
  var hdr=d.querySelector('.site'),bar=d.querySelector('.progress'),tick=false;
  function frame(){tick=false;var y=window.scrollY||window.pageYOffset,max=root.scrollHeight-window.innerHeight;
    if(hdr)hdr.classList.toggle('scrolled',y>40);if(bar)bar.style.transform='scaleX('+(max>0?Math.min(1,y/max):0)+')'}
  window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(frame)}},{passive:true});window.addEventListener('resize',frame);frame();
  var dd=$('details.dd, details.mnav');
  d.addEventListener('click',function(ev){dd.forEach(function(x){if(x.open&&!x.contains(ev.target))x.open=false})});
  d.addEventListener('keydown',function(ev){if(ev.key==='Escape')dd.forEach(function(x){x.open=false})});
  var wx=d.getElementById('wx');$('.wx-open').forEach(function(b){b.addEventListener('click',function(){if(wx&&wx.showModal)wx.showModal();else location.href='/img/wechat-qr.jpg'})});
  if(wx)wx.addEventListener('click',function(ev){if(ev.target===wx)wx.close()});
  var fq=$('.faq details');fq.forEach(function(x){x.addEventListener('toggle',function(){if(x.open)fq.forEach(function(o){if(o!==x)o.open=false})})});
  requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.add('loaded')})});
})();
</script>"""


def head(k, title, desc, path, paths, ld, og_img="/img/brand/bridge.jpg", og_type="website"):
    c = L[k]
    alts = "\n".join(f'<link rel="alternate" hreflang="{L[x]["lang"]}" href="{SITE}{paths[x]}">' for x in L)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{paths["en"]}">'
    verify = (f'\n<meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">' if GOOGLE_SITE_VERIFICATION else "") + \
             (f'\n<meta name="msvalidate.01" content="{BING_SITE_VERIFICATION}">' if BING_SITE_VERIFICATION else "")
    pre = "" if k == "zh" else ('<link rel="preload" href="/assets/fonts/hanken-grotesk-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
                                '<link rel="preload" href="/assets/fonts/hanken-grotesk-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>')
    lds = "".join(f'\n<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="{c["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">{verify}
<meta name="theme-color" content="#0B1A33">
<link rel="canonical" href="{SITE}{path}">
{alts}
<meta property="og:site_name" content="Qiao Partners">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og_img}">
<meta property="og:locale" content="{ {"en": "en_GB", "pl": "pl_PL", "zh": "zh_CN", "ru": "ru_RU"}[k] }">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{pre}
<link rel="stylesheet" href="{css_href()}">{lds}
<script>document.documentElement.classList.add('js')</script>
</head>'''


def org_ld(k):
    c = L[k]
    return {"@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE + "/#org", "name": "Qiao Partners",
            "url": SITE + "/", "logo": SITE + "/favicon-192.png", "image": SITE + "/img/brand/bridge.jpg", "email": EMAIL,
            "description": L["en"]["home"]["desc"], "slogan": "Your European Ambitions. Our Local Execution.",
            "areaServed": [{"@type": "Place", "name": "Europe"}, {"@type": "Country", "name": "China"}],
            "knowsLanguage": ["en", "zh", "pl", "ru"], "sameAs": [LINKEDIN],
            "address": {"@type": "PostalAddress", "addressLocality": "Warsaw", "addressCountry": "PL"},
            "memberOf": [{"@type": "Organization", "name": f'{m["name"]} — {m["full"]["en"]}'} for m in MEMBERS],
            "knowsAbout": ["China–Europe market entry", "European market entry consulting", "European representation for Chinese companies",
                           "Distributor identification", "Market intelligence", "Go-to-market strategy"]}


def crumbs_ld(k, trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(trail)]}


def document(k, page, title, desc, paths, body, ld, has_ins, body_cls="", og_img="/img/brand/bridge.jpg", og_type="website", extra=""):
    return f'''{head(k, title, desc, paths[k], paths, ld, og_img, og_type)}
<body class="{body_cls}">
{header(k, page, paths, has_ins)}
<main id="main">
{body}
</main>
{footer(k, has_ins)}
{wechat_dialog(k)}{SCRIPT}{extra}
</body>
</html>
'''
