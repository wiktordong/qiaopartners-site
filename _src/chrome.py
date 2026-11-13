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
      <div class="brand">{logo(k)}<p>{e(c["f_tag"])}</p><div class="member">{member_logo(k, True)}</div><p class="muted" style="color:var(--on-dark-3);font-size:13px">{e(c["f_member"])}</p></div>
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
    var parts=(root.lang.indexOf('zh')===0)?t.split(/(?<=[，。、])/):t.split(/\s+/);
    el.innerHTML=parts.map(function(w){return '<span class="w" aria-hidden="true"><span style="--i:'+(n++)+'">'+w+'</span></span>'}).join(root.lang.indexOf('zh')===0?'':' ');
  });}
  function tag(sel,kind,step,base){$(sel).forEach(function(el,i){el.setAttribute('data-r',kind||'');el.style.setProperty('--d',((base||0)+Math.min(i,6)*(step||0)).toFixed(2)+'s')})}
  tag('.strip a','mask',0.12,0.5);tag('.cred-pic, .banner-pic, .idet .pic','mask',0);tag('.ind','mask',0.1);tag('.art .pic','mask',0.1);
  tag('.shead > div > *, .shead > div > p',0,0.08);tag('.fact','',0.08);tag('.svc','',0.08);tag('.stage','',0.1);tag('.diff','',0.06);tag('.cmp','',0);
  tag('.sig','',0.06);tag('.sdet','',0);tag('.idet .txt','',0);tag('.split','',0);tag('.grid-list li','',0.05);tag('.next li','',0.08);tag('.faq details','',0.04);tag('.final .wrap > *','',0.12);
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
{SCRIPT}{extra}
</body>
</html>
'''
