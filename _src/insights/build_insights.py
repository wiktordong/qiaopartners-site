"""Builds the Insights section: /insights/ (English articles) plus /pl/insights/ and /zh/insights/ indexes.
Articles are released one a week: only articles whose RELEASE date is on or before today (Warsaw time) are built.
Called from _src/build.py; can also run alone: python3 _src/insights/build_insights.py"""
import json, re, shutil, sys
from datetime import date, datetime
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from articles import ARTICLES, SERIES  # noqa: E402

SITE = "https://qiaopartners.eu"
AUTHOR = "Wiktor Dong"
TODAY = datetime.now(ZoneInfo("Europe/Warsaw")).date()

# One article a week from 1 November 2026. Edit dates here to change the schedule.
RELEASE = {
    "europe-energy-market-2026": date(2026, 11, 1),
    "european-biomethane-market-2026": date(2026, 11, 8),
    "biomethane-equipment-market-europe": date(2026, 11, 15),
    "china-europe-biomethane-investment": date(2026, 11, 22),
    "biomethane-revenue-stack-eu-regulation": date(2026, 11, 29),
    "poland-biomethane-market-2026": date(2026, 12, 6),
}

UI = {
    "en": dict(lang="en", base="/", ins="/insights/", label="EN", h1="Insights",
               dek="Research on Europe's energy transition and the China–Europe corridor: markets, regulation, equipment and trade.",
               series="Series", latest="Latest", parts="part series", part="Part", of="of", read="min read",
               next="Next in the series", out="Published", toc="In this series", topics="Topics", keypoints="Key points",
               prev="Previous", nxt="Next", crumbs="Insights", note="", banner="Now booking market checks for Q1 2027",
               cta_p="Need help entering the European market? Book a 30-minute market check.", cta_b="Book a call",
               nav=[("About", "/#about"), ("Services", "/#services"), ("Market trends", "/#sectors"), ("Insights", "/insights/"), ("Contact", "/#contact")],
               foot="Qiao Partners provides commercial advisory services. This material is for information only and is not investment advice. Views are those of Qiao Partners at the date of publication."),
    "pl": dict(lang="pl", base="/pl/", ins="/pl/insights/", label="PL", h1="Analizy",
               dek="Analizy transformacji energetycznej w Europie i korytarza Chiny–Europa: rynki, regulacje, urządzenia i handel.",
               series="Seria", latest="Najnowsze", parts="części", part="Część", of="z", read="min czytania",
               next="Następna część", out="Opublikowano", toc="W tej serii", topics="Tematy", keypoints="Najważniejsze",
               prev="Poprzednia", nxt="Następna", crumbs="Analizy",
               note="Artykuły publikujemy najpierw po angielsku. Wersja polska wkrótce.",
               banner="Przyjmujemy rezerwacje rozmów na I kwartał 2027",
               cta_p="Potrzebują Państwo wsparcia w wejściu na rynek europejski? Umów 30-minutową rozmowę o rynku.", cta_b="Umów rozmowę",
               nav=[("O nas", "/pl/#about"), ("Usługi", "/pl/#services"), ("Trendy rynkowe", "/pl/#sectors"), ("Analizy", "/pl/insights/"), ("Kontakt", "/pl/#contact")],
               foot="Qiao Partners świadczy usługi doradztwa biznesowego. Materiały mają charakter wyłącznie informacyjny i nie stanowią doradztwa inwestycyjnego."),
    "zh": dict(lang="zh-CN", base="/zh/", ins="/zh/insights/", label="中文", h1="洞察",
               dek="关于欧洲能源转型与中欧通道的研究：市场、监管、设备与贸易。",
               series="系列", latest="最新", parts="篇系列", part="第", of="篇，共", read="分钟阅读",
               next="系列下一篇", out="发布于", toc="本系列", topics="主题", keypoints="要点",
               prev="上一篇", nxt="下一篇", crumbs="洞察",
               note="文章先以英文发布，中文版即将推出。",
               banner="现可预约2027年第一季度市场评估",
               cta_p="需要进入欧洲市场的支持？预约30分钟市场评估。", cta_b="预约沟通",
               nav=[("关于我们", "/zh/#about"), ("服务", "/zh/#services"), ("市场趋势", "/zh/#sectors"), ("洞察", "/zh/insights/"), ("联系我们", "/zh/#contact")],
               foot="Qiao Partners 提供商业咨询服务。本材料仅供参考，不构成投资建议。"),
}

SERIES_T = {
    "pl": dict(name="Rozbudowa rynku biometanu",
               dek="Sześcioczęściowa seria o europejskim rynku gazu odnawialnego: jak bardzo urósł, czego wymaga cel na 2030 r., gdzie trafią urządzenia i kapitał oraz jak przepisy kształtują przychody instalacji."),
    "zh": dict(name="欧洲生物甲烷产业扩张",
               dek="六篇系列文章，解读欧洲可再生天然气市场：当前规模、实现2030年目标的条件、设备与资本的流向，以及法规如何决定项目收益。"),
}

ART_T = {
    "europe-energy-market-2026": {
        "pl": ("Szok gazowy w Europie w 2026 r. i argumenty za krajowym gazem",
               "Cena gazu TTF wzrosła od lutego niemal trzykrotnie. Biometan przestał być wyłącznie narzędziem klimatycznym i stał się kwestią bezpieczeństwa dostaw, a to zmienia, kto go kupuje i dlaczego."),
        "zh": ("2026年欧洲天然气冲击与本土气源的价值",
               "自2月以来，荷兰TTF天然气价格上涨近两倍。生物甲烷由此从气候工具变为供应安全问题，这也改变了买家是谁以及他们为何购买。")},
    "european-biomethane-market-2026": {
        "pl": ("Biometan na poziomie 8 mld m³: ile Europa osiągnęła i ile jej brakuje",
               "Zainstalowana moc wzrosła w ciągu roku o 17%, a zobowiązania inwestycyjne sięgnęły 36 mld euro. Nawet jeśli powstaną wszystkie ogłoszone projekty, Europa osiągnie mniej więcej połowę celu na 2030 r."),
        "zh": ("生物甲烷达到80亿立方米：欧洲走了多远，还差多少",
               "一年内装机容量增长17%，投资承诺达到360亿欧元。即使所有已公布项目全部建成，欧洲也只能完成2030年目标的一半左右。")},
    "biomethane-equipment-market-europe": {
        "pl": ("6500 instalacji do zbudowania: gdzie trafią europejskie wydatki na urządzenia do biometanu",
               "Osiągnięcie celu na 2030 r. wymaga ponad czterokrotnie szybszej budowy niż obecnie. Wąskim gardłem nie są już surowce i finansowanie, lecz moce produkcyjne i wykonawcze."),
        "zh": ("建设6500座工厂：欧洲生物甲烷设备支出流向何处",
               "实现2030年目标需要目前年建设速度的四倍以上。瓶颈已从原料和融资转向制造与施工能力。")},
    "china-europe-biomethane-investment": {
        "pl": ("Chiny a rozbudowa europejskiego biometanu: struktury, które działają",
               "Europie brakuje mocy produkcyjnych do budowy biometanowni. Chińscy dostawcy je mają, ale mierzą się z ostrzejszą polityką przemysłową UE. Struktura wejścia na rynek jest dziś równie ważna jak cena."),
        "zh": ("中国与欧洲生物甲烷产业扩张：行之有效的合作结构",
               "欧洲缺乏建设生物甲烷工厂的制造能力。中国供应商具备这一能力，但面临更严格的欧盟产业政策。如今，市场进入的结构与价格同样重要。")},
    "biomethane-revenue-stack-eu-regulation": {
        "pl": ("Struktura przychodów biometanowni: jak przepisy UE wyznaczają zarobki instalacji",
               "Biometanownia sprzedaje gaz oraz zestaw atrybutów tworzonych przez prawo. Większość wartości zależy od tego, który odbiorca otrzyma który atrybut, i od tego, by nigdy nie rozliczyć tej samej korzyści dwa razy."),
        "zh": ("生物甲烷收入结构：欧盟法规如何决定工厂收益",
               "生物甲烷工厂出售的是天然气以及一系列由法律创设的属性。大部分价值取决于哪个买家获得哪项属性，以及同一收益绝不能重复申报。")},
    "poland-biomethane-market-2026": {
        "pl": ("Polska: kolejny europejski rynek biometanu",
               "Do 2025 r. Polska była największą luką na europejskiej mapie biometanu. W 2026 r. zyskała system aukcyjny, program dotacji i prostsze zasady przyłączania do sieci. Okno na wczesne pozycje to lata 2026–2028."),
        "zh": ("波兰：欧洲下一个生物甲烷市场",
               "到2025年，波兰一直是欧洲生物甲烷版图上最大的空白。2026年，波兰推出了竞拍机制、补贴计划和更简便的并网规则。2026至2028年是抢占先机的窗口期。")},
}

# Insights photos (img/insights/), kept separate from the home-page photos. file: (alt text, crop focus)
PHOTO = {
    "insights/crossroads.jpg": ("A person standing at a road junction with arrows pointing in four directions", "50% 50%"),
    "insights/eu-flag-mountains.jpg": ("European Union flag flying against misty mountains", "50% 45%"),
    "insights/biomethane-domes.jpg": ("Biomethane plant with green digester domes in a field", "50% 55%"),
    "insights/field-road-truck.jpg": ("Red truck on a straight dirt road through green crop fields, seen from above", "50% 72%"),
    "insights/biomethane-plant-trucks.jpg": ("Biomethane plant with feedstock trucks arriving", "50% 55%"),
    "insights/solar-crew.jpg": ("Workers in red helmets installing solar panels", "50% 40%"),
    "insights/handshake-close.jpg": ("Close-up of a business handshake across a table", "50% 52%"),
    "insights/solar-handshake-sunset.jpg": ("Two engineers shaking hands on a solar roof at sunset", "50% 55%"),
    "insights/eu-flags-berlaymont.jpg": ("European Union flags outside the European Commission building", "50% 35%"),
    "insights/solar-wind-coast.jpg": ("Solar panels and wind turbines by the coast", "50% 45%"),
    "insights/wind-patchwork.jpg": ("Wind turbine among patchwork farm fields, seen from above", "50% 50%"),
    "insights/tractor-mowing.jpg": ("Tractor mowing a green field, seen from above", "50% 58%"),
    "insights/solar-lake.jpg": ("Solar panels along a winding path beside a lake, seen from above", "50% 50%"),
    "insights/winding-road-fields.jpg": ("A winding road through farmland, seen from above", "50% 45%"),
}
ALT = {k: v[0] for k, v in PHOTO.items()}
# (cover, photo break inside the article)
IMG = {
    "europe-energy-market-2026": ("insights/crossroads.jpg", "insights/eu-flag-mountains.jpg"),
    "european-biomethane-market-2026": ("insights/biomethane-domes.jpg", "insights/field-road-truck.jpg"),
    "biomethane-equipment-market-europe": ("insights/biomethane-plant-trucks.jpg", "insights/solar-crew.jpg"),
    "china-europe-biomethane-investment": ("insights/handshake-close.jpg", "insights/solar-handshake-sunset.jpg"),
    "biomethane-revenue-stack-eu-regulation": ("insights/eu-flags-berlaymont.jpg", "insights/solar-wind-coast.jpg"),
    "poland-biomethane-market-2026": ("insights/wind-patchwork.jpg", "insights/tractor-mowing.jpg"),
}
HUB_IMG, SERIES_IMG = "insights/solar-lake.jpg", "insights/winding-road-fields.jpg"


def img(f, cls, lazy=True, pos=None):
    pos = pos or PHOTO[f][1]
    return (f'<img class="{cls}" src="/img/{f}" alt="{escape(ALT[f])}" style="object-position:{pos}"'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async">')


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", t).lower()).strip("-")[:60]


def enrich(body, mid):
    """Give each section heading an id (for the contents list) and add a photo break after the third paragraph."""
    heads = []

    def h2(m):
        t = m.group(1)
        i = slugify(t)
        heads.append((i, re.sub(r"<[^>]+>", "", t)))
        return f'<h2 id="{i}">{t}</h2>'
    body = re.sub(r"<h2>(.*?)</h2>", h2, body, flags=re.S)
    parts = body.split("</p>")
    if len(parts) > 4:
        photo = f'<figure class="photo-break">{img(mid, "pb-img")}<figcaption>{escape(ALT[mid])}</figcaption></figure>'
        body = "</p>".join(parts[:3]) + "</p>" + photo + "</p>".join(parts[3:])
    return body, heads


LOGO = '''<a class="q-logo" href="{home}" aria-label="Qiao Partners"><svg viewBox="0 0 108 50" aria-hidden="true">
<path d="M12 16 Q54 -10 96 16" fill="none" stroke="#8EC5F0" stroke-width="2.4" stroke-linecap="round"/>
<text class="word" x="0" y="48" textLength="108" lengthAdjust="spacing">QIAO</text></svg><span class="partners">Partners</span></a>'''

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500;600'
         '&family=Noto+Sans+SC:wght@300;400;500&display=swap">')


def published():
    return [a for a in ARTICLES if RELEASE[a["slug"]] <= TODAY]


def upcoming():
    return [a for a in ARTICLES if RELEASE[a["slug"]] > TODAY]


def fdate(d, lang):
    if lang == "pl":
        m = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia", "września", "października", "listopada", "grudnia"]
        return f"{d.day} {m[d.month - 1]} {d.year}"
    if lang == "zh":
        return f"{d.year}年{d.month}月{d.day}日"
    return d.strftime("%-d %B %Y")


def read_min(a):
    return max(3, round((len(re.sub(r"<[^>]+>", " ", a["body"]).split()) + 60 * len(a["keypoints"])) / 220))


def chrome(k, current_ins, lang_paths):
    u = UI[k]
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == u["ins"] else ""}>{escape(t)}</a>' for t, h in u["nav"])
    langs = "".join(f'<li><a href="{lang_paths[x]}"{" aria-current=\"page\"" if x == k else ""} lang="{UI[x]["lang"]}">{UI[x]["label"]}</a></li>' for x in UI)
    head = f'''<div class="q-banner"><div class="wrap"><a href="{u["base"]}#book"><i aria-hidden="true"></i>{escape(u["banner"])} <span aria-hidden="true">→</span></a></div></div>
<header class="q-head"><div class="wrap">{LOGO.format(home=u["base"])}<nav class="q-nav" aria-label="Main">{nav}</nav>
<div class="q-right"><details class="q-lang"><summary aria-label="Language">{u["label"]}<i aria-hidden="true"></i></summary><ul>{langs}</ul></details>
<a class="btn" href="{u["base"]}#book">{escape(u["cta_b"])}</a></div></div></header>'''
    foot = f'''<section class="cta"><div class="wrap"><p>{escape(u["cta_p"])}</p><a class="btn" href="{u["base"]}#book">{escape(u["cta_b"])} <span aria-hidden="true">→</span></a></div></section>
<footer class="q-foot"><div class="wrap"><p>{escape(u["foot"])}</p>
<p>© 2026 Qiao Partners · <a href="mailto:contact@qiaopartners.eu">contact@qiaopartners.eu</a> · Warsaw · Beijing</p></div></footer>
<script>(function(){{var d=document.querySelector('.q-lang');if(!d)return;document.addEventListener('click',function(e){{if(d.open&&!d.contains(e.target))d.open=false}});document.addEventListener('keydown',function(e){{if(e.key==='Escape')d.open=false}})}})();</script>'''
    return head, foot


def page(k, title, desc, url, css, body, ld, lang_paths, og="website"):
    head, foot = chrome(k, True, lang_paths)
    alts = "".join(f'<link rel="alternate" hreflang="{UI[x]["lang"]}" href="{SITE}{lang_paths[x]}">' for x in UI)
    return f'''<!doctype html>
<html lang="{UI[k]["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{SITE}{url}">{alts}
<meta property="og:type" content="{og}"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{SITE}{url}"><meta property="og:site_name" content="Qiao Partners">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
{FONTS}
<link rel="stylesheet" href="{css}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
{head}
<main>
{body}
</main>
{foot}
</body>
</html>
'''


def art_url(a):
    return f"/insights/{SERIES['slug']}/{a['slug']}/"


def t_art(a, k):
    if k == "en":
        return a["title"], a["standfirst"]
    return ART_T[a["slug"]][k]


def t_series(k):
    return (SERIES["name"], SERIES["dek"]) if k == "en" else (SERIES_T[k]["name"], SERIES_T[k]["dek"])


def hub(k, css):
    u, pub, up = UI[k], published(), upcoming()
    name, dek = t_series(k)
    total = len(ARTICLES)
    toc = "".join(f'<li><a href="{art_url(a)}"><span class="toc-n">{a["part"]:02d}</span><span class="toc-t">{escape(t_art(a, k)[0])}</span></a></li>' for a in pub)
    nxt = ""
    if up:
        a = up[0]
        nxt = f'<p class="upcoming">{escape(u["next"])}: <b>{escape(t_art(a, k)[0])}</b> · {fdate(RELEASE[a["slug"]], k)}</p>'
    soon = "".join(f'''<article class="card soon"><a class="thumb" tabindex="-1" aria-hidden="true">{img(IMG[a["slug"]][0], "")}</a>
<div class="eyebrow">{escape(u["next"])} · {fdate(RELEASE[a["slug"]], k)}</div>
<h3>{escape(t_art(a, k)[0])}</h3><p>{escape(t_art(a, k)[1])}</p></article>''' for a in up[:2])
    cards = "".join(f'''<article class="card"><a class="thumb" href="{art_url(a)}" tabindex="-1" aria-hidden="true">{img(IMG[a["slug"]][0], "")}</a><div class="eyebrow">{escape(SERIES["topic"] if k == "en" else name)}</div>
<h3><a href="{art_url(a)}">{escape(t_art(a, k)[0])}</a></h3><p>{escape(t_art(a, k)[1])}</p>
<div class="meta">{fdate(RELEASE[a["slug"]], k)} · {read_min(a)} {escape(u["read"])}</div></article>''' for a in reversed(pub))
    note = f'<p class="lang-note">{escape(u["note"])}</p>' if u["note"] else ""
    body = f'''<div class="wrap">
<section class="hub-hero"><div><div class="eyebrow">Qiao Partners</div><h1>{escape(u["h1"])}</h1><p>{escape(u["dek"])}</p>{note}</div>
<figure class="hub-pic">{img(HUB_IMG, "", lazy=False)}</figure></section>
<div class="section-h"><h2>{escape(u["series"])}</h2></div>
<section class="series-feature"><div>
<figure class="series-pic">{img(SERIES_IMG, "")}</figure>
<div class="eyebrow">{total}-{escape(u["parts"])}</div>
<h3>{escape(name)}</h3><p>{escape(dek)}</p>{nxt}</div>
<ol class="toc">{toc}</ol></section>
<div class="section-h"><h2>{escape(u["latest"])}</h2></div>
<div class="cards">{cards}{soon}</div>
</div>'''
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": f"{u['h1']} | Qiao Partners", "url": f"{SITE}{u['ins']}",
          "inLanguage": u["lang"], "publisher": {"@type": "Organization", "name": "Qiao Partners", "url": SITE},
          "hasPart": [{"@type": "Article", "headline": a["title"], "url": f"{SITE}{art_url(a)}"} for a in pub]}
    paths = {x: UI[x]["ins"] for x in UI}
    return page(k, f"{u['h1']} | Qiao Partners", u["dek"], u["ins"], css, body, ld, paths)


def article(i, css):
    pub = published()
    a = pub[i]
    u = UI["en"]
    kp = "".join(f"<li>{escape(x)}</li>" for x in a["keypoints"])
    rail = "".join(f'<li><a href="{art_url(b)}"{" aria-current=\"page\"" if b is a else ""}><span>{b["part"]:02d}</span><span>{escape(b["short"])}</span></a></li>' for b in pub)
    up = upcoming()
    if up:
        rail += f'<li><span class="meta">{up[0]["part"]:02d} · {escape(up[0]["short"])} · {fdate(RELEASE[up[0]["slug"]], "en")}</span></li>'
    prev_ = pub[i - 1] if i > 0 else None
    next_ = pub[i + 1] if i < len(pub) - 1 else None
    pager = ""
    if prev_ or next_:
        left = (f'<a href="{art_url(prev_)}"><span class="meta">Previous · Part {prev_["part"]}</span><span>{escape(prev_["short"])}</span></a>') if prev_ else "<span></span>"
        right = (f'<a href="{art_url(next_)}"><span class="meta">Next · Part {next_["part"]}</span><span>{escape(next_["short"])}</span></a>') if next_ else "<span></span>"
        pager = f'<nav class="pager" aria-label="Series">{left}{right}</nav>'
    d = RELEASE[a["slug"]]
    cover, mid = IMG[a["slug"]]
    art_body, heads = enrich(a["body"], mid)
    contents = "".join(f'<li><a href="#{i}">{escape(t)}</a></li>' for i, t in heads)
    body = f'''<div class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/insights/">Insights</a> / {escape(SERIES["topic"])}</nav>
<header class="art-head"><div class="inner">
 <div class="eyebrow">{escape(SERIES["name"])} · Part {a["part"]} of {len(ARTICLES)}</div>
 <h1>{escape(a["title"])}</h1>
 <p class="standfirst">{escape(a["standfirst"])}</p>
 <div class="byline"><span><b>{AUTHOR}</b>, Qiao Partners</span><span>{fdate(d, "en")}</span><span>{read_min(a)} min read</span></div>
</div>
<figure class="cover">{img(cover, "", lazy=False)}<figcaption>{escape(ALT[cover])}</figcaption></figure></header>
<div class="art-grid">
 <article class="prose">
  <section class="keypoints" aria-label="Key points"><h2>Key points</h2><ul>{kp}</ul></section>
  {art_body}
  {pager}
 </article>
 <aside class="rail"><div class="rail-sticky">
  <div class="rail-block"><h2>On this page</h2><ol class="contents">{contents}</ol></div>
  <div class="rail-block"><h2>In this series</h2><ol>{rail}</ol></div>
  <div class="rail-block"><h2>Topics</h2><p>{escape(a["keywords"])}</p></div>
 </div></aside>
</div>
</div>'''
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["seo"],
          "datePublished": d.isoformat(), "dateModified": d.isoformat(), "inLanguage": "en",
          "author": {"@type": "Person", "name": AUTHOR}, "publisher": {"@type": "Organization", "name": "Qiao Partners", "url": SITE},
          "isPartOf": {"@type": "CreativeWorkSeries", "name": SERIES["name"]}, "image": f"{SITE}/img/{cover}", "keywords": a["keywords"], "mainEntityOfPage": f"{SITE}{art_url(a)}"}
    paths = {"en": art_url(a), "pl": UI["pl"]["ins"], "zh": UI["zh"]["ins"]}
    return page("en", f"{a['title']} | Qiao Partners", a["seo"], art_url(a), "/insights/insights.css", body, ld, paths, og="article")


def build(root: Path):
    out = root / "insights"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copy(HERE / "insights.css", out / "insights.css")
    (out / "index.html").write_text(hub("en", "/insights/insights.css"), encoding="utf-8")
    for k in ("pl", "zh"):
        d = root / k / "insights"
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(hub(k, "/insights/insights.css"), encoding="utf-8")
    pub = published()
    for i, a in enumerate(pub):
        d = out / SERIES["slug"] / a["slug"]
        d.mkdir(parents=True)
        (d / "index.html").write_text(article(i, "/insights/insights.css"), encoding="utf-8")
    urls = [UI[k]["ins"] for k in UI] + [art_url(a) for a in pub]
    return urls, [(a["title"], art_url(a), a["seo"]) for a in pub]


if __name__ == "__main__":
    print(build(Path(__file__).resolve().parents[2]))
