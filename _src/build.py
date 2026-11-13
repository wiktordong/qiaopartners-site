# Builds the whole site in four languages (EN at /, PL at /pl/, ZH at /zh/, RU at /ru/) plus Insights, sitemap, robots and llms.txt.
# Run from the repository root:  python3 _src/build.py
# Copy lives in _src/lang/<code>.py, settings in _src/settings.py, design in _src/site.css, page chrome in _src/chrome.py.
import os, shutil, sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "insights"))
from chrome import L, ROOT, SITE, url, e, document, member_logo, org_ld, crumbs_ld, write_css  # noqa: E402
from settings import EMAIL, LINKEDIN, WHATSAPP, CALENDLY_URL, FORM_ENDPOINT  # noqa: E402
import build_insights  # noqa: E402

PAGES = ["home", "about", "services", "industries", "contact", "china"]
AR = '<span class="ar" aria-hidden="true">→</span>'


def check_structure():
    """Every language must have exactly the same keys and list lengths as English."""
    def walk(a, b, path):
        if type(a) is not type(b):
            raise SystemExit(f"Copy mismatch at {path}: {type(a).__name__} vs {type(b).__name__}")
        if isinstance(a, dict):
            if set(a) != set(b):
                raise SystemExit(f"Copy keys differ at {path}: {sorted(set(a) ^ set(b))}")
            for x in a:
                walk(a[x], b[x], f"{path}.{x}")
        elif isinstance(a, (list, tuple)):
            if len(a) != len(b):
                raise SystemExit(f"Copy list length differs at {path}: {len(a)} vs {len(b)}")
            for i, (x, y) in enumerate(zip(a, b)):
                walk(x, y, f"{path}[{i}]")
    for k in L:
        walk(L["en"], L[k], k)


def paths_for(page):
    return {k: url(k, page) for k in L}


def img(src, alt, cls="", lazy=True, pos="50% 50%"):
    return f'<img class="{cls}" src="/img/{src}" alt="{e(alt)}" style="object-position:{pos}"{" loading=\"lazy\"" if lazy else ""} decoding="async">'


def eyebrow(t):
    return f'<span class="eyebrow">{e(t)}</span>'


def shead(eb, h, p, h_tag="h2", extra=""):
    return f'''<div class="shead"><div>{eyebrow(eb)}<{h_tag} class="h2">{e(h)}</{h_tag}></div><div><p class="lead">{e(p)}</p>{extra}</div></div>'''


def final(k, ctype=""):
    f = L[k]["final"]
    q = f"?type={ctype}" if ctype else ""
    return f'''<section class="final"><img class="bg" src="/img/brand/bridge.jpg" alt="" loading="lazy" decoding="async">
  <div class="wrap">
    <div>{eyebrow("Qiao Partners")}<h2>{e(f["h"])}</h2><p class="lead">{e(f["p"])}</p>
      <a class="btn ivory" href="{url(k, "contact")}{q}">{e(f["cta"])} {AR}</a></div>
    <div class="side"><div class="qrs"><figure><img src="/img/wechat-qr.jpg" alt="WeChat QR code — Qiao Partners" loading="lazy"><figcaption>WeChat</figcaption></figure><figure><a href="{WHATSAPP}" rel="noopener" target="_blank"><img src="/img/whatsapp-qr.png" alt="WhatsApp QR code — Qiao Partners" loading="lazy"></a><figcaption>WhatsApp</figcaption></figure></div><p>{e(f["side"])} <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
  </div>
</section>'''


def phero(k, page, eb, h1, lead, extra=""):
    c = L[k]
    crumbs = "" if page == "home" else f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{url(k, "home")}">{e(c["nav"]["home"])}</a> / {e(eb)}</nav>'
    return f'''<section class="phero">
  <div class="wrap">{crumbs}{eyebrow(eb)}<h1>{e(h1)}</h1><p class="lead">{e(lead)}</p>{extra}</div>
</section>'''


# ---------------------------------------------------------------- Home
def home(k, has_ins):
    c, h = L[k], L[k]["home"]
    d = c["qiao_def"]
    bar = "".join(f'<a href="{url(k, "services", s["id"])}"><span>{s["n"]}</span>{e(s["title"])}</a>' for s in c["services"])
    facts = []
    for label, val, note in h["facts"]:
        if val == "@sinocham":
            v = f'<dd>{member_logo(k, False)}</dd>'
        else:
            v = f'<dd class="{"big" if len(val) < 9 else ""}">{e(val)}</dd>'
        facts.append(f'<div class="fact"><dt>{e(label)}</dt>{v}<small>{e(note)}</small></div>')
    svcs = "".join(f'''<article class="svc"><span class="n">{s["n"]}</span><h3>{e(s["title"])}</h3><p>{e(s["short"])}</p>
      <ul>{"".join(f"<li>{e(x)}</li>" for x in s["deliv"][:3])}</ul><a class="tlink" href="{url(k, "services", s["id"])}">{e(c["more"])} {AR}</a></article>''' for s in c["services"])
    inds = "".join(f'''<a class="ind" href="{url(k, "industries", i["id"])}">{img(i["img"], i["alt"])}<div class="in"><span class="k">{i["k"]}</span>
      <h3>{e(i["title"])}</h3><p>{e(i["short"])}</p><span class="more">{e(c["more"])} {AR}</span></div></a>''' for i in c["industries"])
    stages = "".join(f'<li class="stage"><span class="n">0{n + 1}</span><h3>{e(a.upper() if k != "zh" else a)}</h3><p class="t">{e(t)}</p><p>{e(p)}</p></li>'
                     for n, (a, t, p) in enumerate(h["stages"]))
    ch = h["cmp_head"]
    rows = "".join(f'<tr><th scope="row">{e(a)}</th><td data-h="{e(ch[1])}">{e(b)}</td><td data-h="{e(ch[2])}">{e(x)}</td></tr>' for a, b, x in h["cmp"])
    diffs = "".join(f'<li class="diff"><span class="n">0{n + 1}</span><h3>{e(t)}</h3><p>{e(p)}</p></li>' for n, (t, p) in enumerate(h["diffs"]))
    sigs = "".join(f'''<article class="sig"><div class="top"><span>{e(t)}</span><b>{e(dt)}</b></div><h3>{e(hh)}</h3><p>{e(p)}</p>
      <p class="src"><a href="{e(u)}" rel="noopener" target="_blank">{e(s)}</a></p></article>''' for t, dt, hh, p, s, u in h["signals"])
    arts = ""
    if has_ins:
        cards = "".join(f'<a class="art" href="{u}"><div class="pic">{img(im, al)}</div><span>{e(dt)}</span><h3>{e(t)}</h3></a>'
                        for t, u, im, al, dt in build_insights.latest(k, 3))
        arts = f'<div class="arts">{cards}</div><p style="margin-top:36px"><a class="tlink" href="{url(k, "insights")}">{e(h["ins_more"])} {AR}</a></p>'
    shots = [("wind-aerial.jpg", "energy-infrastructure", "50% 50%"), ("terminal.jpg", "energy-infrastructure", "55% 50%"),
             ("insights/charging-mountain.jpg", "mobility-automotive", "50% 70%"), ("insights/biomethane-plant-trucks.jpg", "energy-infrastructure", "50% 55%")]
    strip = "".join(f'<a href="{url(k, "industries", sec)}">{img(f, cap, pos=pos)}<span>{e(cap)}</span></a>' for (f, sec, pos), cap in zip(shots, c["strip"]))
    body = f'''<section class="hero">
  <div class="wrap">
    <p class="def"><b lang="zh-CN">{d[0]}</b>{e(d[1])} <i>{e(d[2])}</i> — {e(d[3])}</p>
    <div class="hero-grid">
      <div class="hero-main">{eyebrow(h["eyebrow"])}<h1><span class="a">{e(h["h1a"])}</span> <span class="b">{e(h["h1b"])}</span></h1></div>
      <div class="hero-side"><p class="lead">{e(h["lead"])}</p>
        <div class="ctas"><a class="btn solid" href="{url(k, "contact")}?type=expansion">{e(h["cta1"])} {AR}</a><a class="tlink" href="{url(k, "services")}">{e(h["cta2"])} {AR}</a></div></div>
    </div>
  </div>
  <div class="strip">{strip}</div>
</section>

<section class="sec">
  <div class="wrap cred">
    <figure class="cred-pic">{img("meeting.jpg", h["cred_pic"], pos="50% 40%")}</figure>
    <div class="cred-copy">{eyebrow(h["cred_eyebrow"])}<h2 class="h2">{e(h["cred_h"])}</h2><p class="lead">{e(h["cred_p"])}</p>
      <dl class="facts">{"".join(facts)}</dl>
      <a class="tlink" href="{url(k, "about")}">{e(c["nav"]["about"])} {AR}</a></div>
  </div>
</section>

<section class="sec stone" id="services">
  <div class="wrap">{shead(h["what_eyebrow"], h["what_h"], h["what_p"])}<div class="svcs">{svcs}</div></div>
</section>

<section class="sec" id="industries">
  <div class="wrap">{shead(h["ind_eyebrow"], h["ind_h"], h["ind_p"], extra=f'<p style="margin-top:22px"><a class="tlink" href="{url(k, "industries")}">{e(c["all_industries"])} {AR}</a></p>')}</div>
  <div class="wrap"><div class="inds">{inds}</div></div>
</section>

<section class="sec dark">
  <div class="wrap">{shead(h["appr_eyebrow"], h["appr_h"], h["appr_p"])}<ol class="stages">{stages}</ol></div>
</section>

<section class="sec">
  <div class="wrap why">
    <div class="why-copy">{eyebrow(h["why_eyebrow"])}<h2 class="h2">{e(h["why_h"])}</h2><p class="lead">{e(h["why_p"])}</p>
      <a class="btn solid" href="{url(k, "contact")}?type=expansion">{e(c["nav_cta"])} {AR}</a></div>
    <div><table class="cmp"><thead><tr><th scope="col">{e(ch[0])}</th><th scope="col">{e(ch[1])}</th><th scope="col">{e(ch[2])}</th></tr></thead><tbody>{rows}</tbody></table>
      <ol class="diffs">{diffs}</ol></div>
  </div>
</section>

<section class="sec stone" id="insights">
  <div class="wrap">{shead(h["ins_eyebrow"], h["ins_h"], h["ins_p"])}<div class="signals">{sigs}</div><p class="checked">{e(h["ins_checked"])}</p>{arts}</div>
</section>
{final(k)}
<script>(function(){{var m={{"#book":"contact","#contact":"contact","#faq":"contact","#about":"about","#sectors":"industries","#team":"about"}};var t=m[location.hash];if(t)location.replace("{url(k, "home")}"+t+"/");}})();</script>'''
    ld = [org_ld(k), {"@context": "https://schema.org", "@type": "WebSite", "name": "Qiao Partners", "url": SITE + url(k, "home"), "inLanguage": c["lang"]}]
    return document(k, "home", h["title"], h["desc"], paths_for("home"), body, ld, has_ins, body_cls="home")


# ---------------------------------------------------------------- About
def about(k, has_ins):
    c, a = L[k], L[k]["about"]
    blocks = []
    for title, paras in a["blocks"]:
        ps = "".join(f'<p class="strong">{e(p[1:])}</p>' if p.startswith("@") else f"<p>{e(p)}</p>" for p in paras)
        blocks.append(f'<div class="split"><h2>{e(title)}</h2><div class="body">{ps}</div></div>')
    blocks_html = '<hr class="rule" style="margin-block:clamp(48px,6vw,80px)">'.join(blocks)
    engage = "".join(f"<li><b>{e(t)}</b><span>{e(p)}</span></li>" for t, p in a["engage"])
    net = "".join(f"<li>{e(x)}</li>" for x in a["net"])
    body = f'''{phero(k, "about", a["eyebrow"], a["h1"], a["lead"])}
<figure class="banner-pic blend">{img("brand/bridge.jpg", a["pic"], lazy=False, pos="50% 55%")}</figure>
<section class="sec"><div class="wrap">{blocks_html}</div></section>
<section class="sec stone"><div class="wrap"><div class="split"><h2>{e(a["engage_h"])}</h2><ul class="grid-list">{engage}</ul></div></div></section>
<section class="sec"><div class="wrap"><div class="split"><h2>{e(a["net_h"])}</h2><div class="body"><p>{e(a["net_p"])}</p><ul class="ticks">{net}</ul></div></div></div></section>
<section class="sec dark tight"><div class="wrap">
  <div class="split"><h2>{e(a["ind_h"])}</h2><div class="body"><p>{e(a["ind_p"])}</p></div></div>
  <hr class="rule" style="margin-block:56px;background:var(--line-dark)">
  <div class="split"><h2>{e(a["mem_h"])}</h2><div class="body"><div class="member">{member_logo(k, True)}</div><p>{e(a["mem_p"])}</p></div></div>
</div></section>
{final(k)}'''
    ld = [org_ld(k), crumbs_ld(k, [(c["nav"]["home"], url(k, "home")), (c["nav"]["about"], url(k, "about"))]),
          {"@context": "https://schema.org", "@type": "AboutPage", "name": a["title"], "url": SITE + url(k, "about"), "inLanguage": c["lang"]}]
    return document(k, "about", a["title"], a["desc"], paths_for("about"), body, ld, has_ins, og_img="/img/brand/bridge.jpg")


# ---------------------------------------------------------------- Services
def services(k, has_ins):
    c, s = L[k], L[k]["svc_page"]
    sub = "".join(f'<a href="#{x["id"]}"><span>{x["n"]}</span>{e(x["title"])}</a>' for x in c["services"])
    dets = []
    for x in c["services"]:
        note = f'<p class="note">{e(x["note"])}</p>' if x.get("note") else ""
        dets.append(f'''<article class="sdet" id="{x["id"]}">
      <div class="l"><span class="n">{x["n"]}</span><h2>{e(x["title"])}</h2><p>{e(x["desc"])}</p>
        <a class="btn solid" href="{url(k, "contact")}?type={x["cta_type"]}">{e(x["cta"])} {AR}</a></div>
      <div class="r">
        <div><h3>{e(s["needs_h"])}</h3><ul class="ticks">{"".join(f"<li>{e(n)}</li>" for n in x["needs"])}</ul></div>
        <div><h3>{e(s["deliv_h"])}</h3><ul class="ticks">{"".join(f"<li>{e(n)}</li>" for n in x["deliv"])}</ul></div>
        <div><h3>{e(s["fmt_h"])}</h3><p class="fmt">{e(x["fmt"])}</p></div>{note}
      </div></article>''')
    body = f'''{phero(k, "services", s["eyebrow"], s["h1"], s["lead"])}
<nav class="subnav" aria-label="{e(s["eyebrow"])}"><div class="wrap">{sub}</div></nav>
<section class="sec"><div class="wrap">{"".join(dets)}</div></section>
<section class="sec stone"><div class="wrap">
  <div class="split"><h2>{e(s["spec_h"])}</h2><div class="body"><p>{e(s["spec_p"])}</p></div></div>
  <hr class="rule" style="margin-block:clamp(48px,6vw,72px)">
  <div class="split"><h2>{e(s["fees_h"])}</h2><div class="body"><p>{e(s["fees_p"])}</p></div></div>
  <hr class="rule" style="margin-block:clamp(48px,6vw,72px)">
  <div class="split"><h2>{e(s["eu2cn_h"])}</h2><div class="body"><p>{e(s["eu2cn_p"])}</p><p><a class="tlink" href="{url(k, "china")}">{e(c["more"])} {AR}</a></p></div></div>
</div></section>
{final(k)}'''
    ld = [org_ld(k), crumbs_ld(k, [(c["nav"]["home"], url(k, "home")), (c["nav"]["services"], url(k, "services"))])] + \
         [{"@context": "https://schema.org", "@type": "Service", "name": x["title"], "description": x["desc"], "serviceType": x["title"],
           "provider": {"@id": SITE + "/#org"}, "areaServed": "Europe", "url": SITE + url(k, "services", x["id"])} for x in c["services"]]
    return document(k, "services", s["title"], s["desc"], paths_for("services"), body, ld, has_ins)


# ---------------------------------------------------------------- Industries
def industries(k, has_ins):
    c, p = L[k], L[k]["ind_page"]
    sub = "".join(f'<a href="#{x["id"]}"><span>{x["k"]}</span>{e(x["title"])}</a>' for x in c["industries"])
    dets = "".join(f'''<article class="idet" id="{x["id"]}">
      <div class="pic">{img(x["img"], x["alt"])}<span>{x["k"]}</span></div>
      <div class="txt"><h2>{e(x["title"])}</h2><p class="lead" style="font-size:18px">{e(x["short"])}</p>
        <div><h3>{e(p["focus_h"])}</h3><ul class="chips">{"".join(f"<li>{e(i)}</li>" for i in x["items"])}</ul></div>
        <div><h3>{e(p["entry_h"])}</h3><ul class="ticks" style="grid-template-columns:1fr">{"".join(f"<li>{e(i)}</li>" for i in x["entry"])}</ul></div>
      </div></article>''' for x in c["industries"])
    body = f'''{phero(k, "industries", p["eyebrow"], p["h1"], p["lead"])}
<nav class="subnav" aria-label="{e(p["eyebrow"])}"><div class="wrap">{sub}</div></nav>
<section class="sec stone"><div class="wrap">{dets}<p class="note" style="margin-top:56px">{e(p["note"])}</p></div></section>
{final(k)}'''
    ld = [org_ld(k), crumbs_ld(k, [(c["nav"]["home"], url(k, "home")), (c["nav"]["industries"], url(k, "industries"))])]
    return document(k, "industries", p["title"], p["desc"], paths_for("industries"), body, ld, has_ins)


# ---------------------------------------------------------------- Contact
def contact(k, has_ins):
    c, f = L[k], L[k]["contact"]
    opts = lambda items: f'<option value="" disabled selected>{e(f["f_choose"])}</option>' + "".join(f"<option>{e(o)}</option>" for o in items)
    req = ' <em aria-hidden="true">*</em>'
    opt = f' <span class="muted" style="font-weight:400">({e(f["f_opt"])})</span>'
    types = "".join(f'<option value="{v}">{e(t)}</option>' for v, t in f["types"])
    form = f'''<form class="enq" id="enquiry" data-endpoint="{e(FORM_ENDPOINT)}" novalidate>
      <fieldset><legend class="first">{e(f["lg1"])}</legend>
        <label class="full"><span>{e(f["f_type"])}{req}</span><select name="enquiry_type" id="f-type" required>{types}</select></label></fieldset>
      <fieldset><legend>{e(f["lg2"])}</legend>
        <label><span>{e(f["f_company"])}{req}</span><input name="company" required autocomplete="organization"></label>
        <label><span>{e(f["f_country"])}{req}</span><input name="country" required autocomplete="country-name"></label>
        <label><span>{e(f["f_industry"])}{req}</span><select name="industry" required>{opts(f["ind_opts"])}</select></label>
        <label><span>{e(f["f_size"])}{req}</span><select name="company_size" required>{opts(f["sizes"])}</select></label></fieldset>
      <fieldset><legend>{e(f["lg3"])}</legend>
        <label><span>{e(f["f_presence"])}{req}</span><select name="european_presence" required>{opts(f["presence"])}</select></label>
        <label><span>{e(f["f_objective"])}{req}</span><select name="objective" required>{opts(f["objectives"])}</select></label>
        <label class="full">{e(f["f_msg"])}<textarea name="message" placeholder="{e(f["f_msg_ph"])}"></textarea></label></fieldset>
      <fieldset><legend>{e(f["lg4"])}</legend>
        <label><span>{e(f["f_name"])}{req}</span><input name="name" required autocomplete="name"></label>
        <label><span>{e(f["f_role"])}{opt}</span><input name="position" autocomplete="organization-title"></label>
        <label><span>{e(f["f_email"])}{req}</span><input name="email" type="email" required autocomplete="email"></label>
        <label><span>{e(f["f_method"])}{req}</span><select name="preferred_contact" required>{opts(f["methods"])}</select></label>
        <label class="full"><span>{e(f["f_handle"])}{opt}</span><input name="wechat_or_phone" autocomplete="tel"></label></fieldset>
      <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="full actions"><button class="btn solid" type="submit">{e(f["f_submit"])} {AR}</button><small>{e(f["f_note"])}</small></div>
    </form>
    <p class="status" id="enq-ok" role="status" hidden>{e(f["f_ok"])}</p>
    <p class="status err" id="enq-err" role="alert" hidden>{e(f["f_err"])}</p>'''
    nxt = "".join(f'<li><span>0{i + 1}</span><b>{e(t)}</b><p>{e(p)}</p></li>' for i, (t, p) in enumerate(f["next"]))
    wa = f'<figure><a href="{WHATSAPP}" rel="noopener" target="_blank"><img src="/img/whatsapp-qr.png" alt="WhatsApp QR code" loading="lazy"></a><figcaption>{e(f["scan_wa"])}</figcaption></figure>' if WHATSAPP else ""
    aside = f'''<aside class="aside">
      <div class="next"><h3>{e(f["next_h"])}</h3><ol>{nxt}</ol></div>
      <div class="direct"><h3>{e(f["direct_h"])}</h3><dl>
        <div><dt>{e(f["c_email"])}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>{e(f["c_li"])}</dt><dd><a href="{LINKEDIN}" rel="noopener" target="_blank">{e(f["c_li_txt"])}</a></dd></div>
        <div><dt>{e(f["c_base"])}</dt><dd>{e(c["f_base"])}</dd></div></dl></div>
      <div class="qrs"><figure><img src="/img/wechat-qr.jpg" alt="WeChat QR code — Qiao Partners" loading="lazy"><figcaption>{e(f["scan_wechat"])}</figcaption></figure>{wa}</div>
    </aside>'''
    cal = ""
    if CALENDLY_URL:
        cal = f'''<div class="cal-wrap"><div class="shead" style="margin-bottom:32px"><div>{eyebrow(f["cal_h"])}<h2 class="h2" style="font-size:clamp(28px,3vw,40px)">{e(f["cal_p"])}</h2></div><div></div></div>
      <div class="calendly-inline-widget" id="cal-widget" data-loading="{e(f["cal_loading"])}" data-url="{e(CALENDLY_URL)}?hide_gdpr_banner=1&amp;primary_color=0b1a33"></div></div>'''
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in f["faq"])
    body = f'''{phero(k, "contact", f["eyebrow"], f["h1"], f["lead"])}
<section class="sec" style="padding-top:clamp(56px,6vw,96px)"><div class="wrap">
  <div class="contact-grid"><div class="panel"><h2>{e(f["form_h"])}</h2><p>{e(f["form_p"])}</p>{form}</div>{aside}</div>
  {cal}
</div></section>
<section class="sec stone" id="faq"><div class="wrap faq"><div>{eyebrow("FAQ")}<h2 class="h2" style="margin-top:20px">{e(f["faq_h"])}</h2></div><div>{faqs}</div></div></section>'''
    script = r'''
<script>
(function(){
  var f=document.getElementById('enquiry');if(!f)return;
  var q=new URLSearchParams(location.search).get('type'),sel=document.getElementById('f-type');
  if(q&&sel&&sel.querySelector('option[value="'+q+'"]'))sel.value=q;
  f.addEventListener('submit',function(ev){
    ev.preventDefault();
    var ok=document.getElementById('enq-ok'),err=document.getElementById('enq-err');ok.hidden=true;err.hidden=true;
    if(!f.checkValidity()){f.reportValidity();return}
    var d={};new FormData(f).forEach(function(v,k){d[k]=v});if(d._honey)return;
    var t=sel.options[sel.selectedIndex].text;
    d._subject='Qiao Partners enquiry: '+(d.company||'')+' / '+t;d._template='table';d.page=location.pathname;d.language=document.documentElement.lang;
    var b=f.querySelector('button');b.disabled=true;
    fetch(f.getAttribute('data-endpoint'),{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(d)})
      .then(function(r){if(!r.ok)throw new Error(r.status);return r.json()})
      .then(function(){f.reset();if(q)sel.value=q;ok.hidden=false;ok.scrollIntoView({behavior:'smooth',block:'center'});
        var w=document.getElementById('cal-widget');if(w&&window.Calendly){w.innerHTML='';window.Calendly.initInlineWidget({url:w.getAttribute('data-url'),parentElement:w,prefill:{name:d.name,email:d.email}})}})
      .catch(function(){err.hidden=false})
      .then(function(){b.disabled=false});
  });
})();
</script>''' + ('\n<script src="https://assets.calendly.com/assets/external/widget.js" async></script>' if CALENDLY_URL else "")
    ld = [org_ld(k), crumbs_ld(k, [(c["nav"]["home"], url(k, "home")), (c["nav"]["contact"], url(k, "contact"))]),
          {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": c["lang"],
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in f["faq"]]},
          {"@context": "https://schema.org", "@type": "ContactPage", "name": f["title"], "url": SITE + url(k, "contact"), "inLanguage": c["lang"]}]
    return document(k, "contact", f["title"], f["desc"], paths_for("contact"), body, ld, has_ins, extra=script)


# ---------------------------------------------------------------- European companies entering China
def china(k, has_ins):
    c, p = L[k], L[k]["china"]
    items = "".join(f"<li><b>{e(t)}</b><span>{e(d)}</span></li>" for t, d in p["items"])
    body = f'''{phero(k, "china", p["eyebrow"], p["h1"], p["lead"])}
<section class="sec"><div class="wrap"><ul class="grid-list">{items}</ul>
  <p style="margin-top:48px"><a class="btn solid" href="{url(k, "contact")}?type=china">{e(p["cta"])} {AR}</a></p></div></section>
{final(k, "china")}'''
    ld = [org_ld(k), crumbs_ld(k, [(c["nav"]["home"], url(k, "home")), (p["eyebrow"], url(k, "china"))])]
    return document(k, "china", p["title"], p["desc"], paths_for("china"), body, ld, has_ins)


RENDER = {"home": home, "about": about, "services": services, "industries": industries, "contact": contact, "china": china}


def main():
    check_structure()
    write_css()
    from pathlib import Path
    ins_urls, ins_articles = build_insights.build(Path(ROOT))
    has_ins = bool(ins_urls)
    built = []
    for k in L:
        for p in PAGES:
            out = os.path.join(ROOT, url(k, p).strip("/"), "index.html")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w", encoding="utf-8").write(RENDER[p](k, has_ins))
            built.append(url(k, p))
    open(os.path.join(ROOT, "robots.txt"), "w").write(
        "User-agent: *\nAllow: /\n\n# AI assistants and search crawlers are welcome\n"
        "User-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\n"
        "User-agent: Google-Extended\nAllow: /\n\nSitemap: https://qiaopartners.eu/sitemap.xml\n")
    today = date.today().isoformat()
    xs = []
    for p in PAGES:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{L[x]["lang"]}" href="{SITE}{url(x, p)}"/>' for x in L)
        for k in L:
            xs.append(f"  <url><loc>{SITE}{url(k, p)}</loc><lastmod>{today}</lastmod>{alts}</url>")
    xs += [f"  <url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>" for u in ins_urls]
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(xs) + "\n</urlset>\n")
    en = L["en"]
    llms = ["# Qiao Partners", "", f"> {en['home']['desc']}", "",
            "Qiao Partners is an independent China–Europe market entry and strategic business development firm based in Warsaw, Poland. "
            "It helps Chinese companies enter, establish and grow across European markets, and supports selected European companies entering China. "
            "It is not a law firm, tax adviser, certification body or investment adviser, and it does not invest or give investment advice.", "",
            "## Services"] + [f"- [{s['title']}]({SITE}{url('en', 'services', s['id'])}): {s['desc']}" for s in en["services"]] + \
           ["", "## Industries"] + [f"- {i['title']}: {', '.join(i['items'])}" for i in en["industries"]] + \
           ["", "## Pages"] + [f"- [{en['nav'].get(p, 'European companies entering China')}]({SITE}{url('en', p)})" for p in PAGES] + \
           [f"- [{L[k]['name']}]({SITE}{url(k, 'home')})" for k in L if k != "en"] + \
           (["", "## Insights"] + [f"- [{t}]({SITE}{u}): {d}" for t, u, d in ins_articles] if ins_articles else []) + \
           ["", "## Contact", f"- Email: {EMAIL}", f"- LinkedIn: {LINKEDIN}", "- WeChat: QR code on every page", f"- Enquiry form: {SITE}/contact/", ""]
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(llms))
    print("built", len(built), "pages +", len(ins_urls), "insights pages")


if __name__ == "__main__":
    main()
