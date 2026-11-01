from datetime import date
from charts import bars, line, stack

SERIES = {
    "slug": "biomethane",
    "name": "The Biomethane Build-Out",
    "topic": "Biomethane",
    "dek": ("A six-part series on Europe's renewable gas market: how large it has become, what it will take "
            "to reach the 2030 target, where the equipment and capital will go, and how the rules shape "
            "what a plant can earn."),
}

PUBLISHED = date(2026, 11, 2)


def src(*links):
    return " · ".join(f'<a href="{u}" rel="noopener" target="_blank">{t}</a>' for t, u in links)


def exhibit(n, title, body, source, note=""):
    note_html = f'<p class="ex-note">{note}</p>' if note else ""
    return (f'<figure class="exhibit"><figcaption><span class="ex-num">Exhibit {n}</span>'
            f'<span class="ex-title">{title}</span></figcaption>'
            f'<div class="ex-body">{body}</div>{note_html}'
            f'<p class="ex-source">Source: {source}</p></figure>')


def table(head, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl-wrap"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


# ---------------------------------------------------------------- 1
A1_TTF = line(
    [(date(2025, 9, 1), 32.06, None), (date(2025, 11, 3), 31.87, None),
     (date(2026, 2, 27), 32.1, None), (date(2026, 3, 24), 54.04, "54"),
     (date(2026, 4, 1), 47.51, None), (date(2026, 5, 1), 45.96, None),
     (date(2026, 6, 1), 47.41, None), (date(2026, 7, 1), 43.60, None),
     (date(2026, 8, 3), 57.49, None), (date(2026, 9, 1), 71.77, None),
     (date(2026, 10, 22), 89.0, "89")],
    "Dutch TTF gas price, September 2025 to October 2026, in euros per MWh",
    unit=" €/MWh", notes=[(date(2026, 2, 27), "Conflict begins")])

A1 = dict(
    slug="europe-energy-market-2026",
    title="Europe's 2026 gas shock and the case for domestic molecules",
    short="Europe's 2026 gas shock",
    part=1,
    standfirst=("Dutch TTF gas has almost tripled since February. The price move has turned biomethane from a "
                "climate instrument into a question of supply security, and that changes who buys it and why."),
    keypoints=[
        "TTF traded near €89/MWh on 22 October 2026, 177% above its level when the Middle East conflict began in February.",
        "Carbon is now priced at the EU border as well as inside it: the first CBAM certificate price was set at €75.36/tCO₂ in April.",
        "The Commission's AccelerateEU plan names biomethane as a homegrown supply lever. We expect buyers to value it as security supply, not only as a green attribute.",
    ],
    seo="TTF gas rose 177% in 2026. How the price shock, CBAM and ETS2 change the value of domestic renewable gas in Europe.",
    keywords="European energy market 2026, TTF gas price, AccelerateEU, ETS2, biomethane, energy security",
    body=f"""
<p>Ten months ago the European gas market looked settled. The one-month TTF contract fell below €27/MWh in early December 2025, its lowest level in 20 months, as LNG supply grew and storage looked comfortable. On 22 October 2026 the same benchmark stood near €89/MWh, according to European Commission data reported by ANSA. That is a 177% rise since February, when the conflict involving Iran began and shipments through the Strait of Hormuz came into question.</p>

{exhibit(1, "TTF gas price, September 2025 to October 2026 (€/MWh)", A1_TTF,
         src(("minfin.com.ua TTF history", "https://index.minfin.com.ua/markets/gas/ttf/2026-09/"),
             ("Trading Economics", "https://tradingeconomics.com/commodity/eu-natural-gas%20"),
             ("ANSA via SoldiOnline", "https://www.soldionline.it/notizie/forex-commodities/gas-ue-177-da-febbraio-cosa-ce-dietro-il-balzo-del-ttf-a-89-mwh")) + "; Qiao Partners.",
         "Single-day prints, mostly the first trading day of each month. The late-February level is implied from the Commission's +177% figure.")}

<h2>Diversification reduced one risk and exposed another</h2>
<p>After 2022 Europe replaced Russian pipeline gas with LNG from the United States, Qatar and elsewhere. That reduced dependence on a single supplier. It did not reduce dependence on shipping lanes, or on competing with Asian buyers for the same cargoes. The 2026 disruption tested exactly that exposure.</p>
<p>Three features now define the market. Price volatility has become structural: a buyer who budgeted on the December 2025 forward curve is paying more than three times as much today. Gas and carbon now trade as one complex. December 2026 EUA futures touched about €92/t in mid-January, then fell back to €74–77/t by May as high gas prices changed fuel-switching economics. And carbon is now charged at the border. CBAM entered its definitive phase on 1 January 2026, and the Commission published the first quarterly CBAM certificate price, €75.36/tCO₂, on 7 April.</p>

<h2>Brussels has framed biomethane as a security measure</h2>
<p>The Commission's response, AccelerateEU (COM(2026) 370), was published on 22 April 2026. It combines short-term relief for households and industry with measures to cut exposure to imported fossil fuels, and it names biomethane among the domestic sources to scale up immediately. An EU biomethane platform followed. Energy Commissioner Dan Jørgensen described its purpose as strengthening security of supply.</p>
<p>The long-term carbon framework has hardened at the same time. On 5 March 2026 the Council formally adopted a 2040 target of a 90% net cut in emissions against 1990. In the same package, the start of ETS2, which prices fuel for buildings and road transport, moved one year to 1 January 2028.</p>

{exhibit(2, "Price and policy markers, 2026",
         table(["Date", "Event", "Relevance for gas buyers"], [
             ["1 Jan", "CBAM definitive phase begins", "Carbon cost applies to imported steel, cement, aluminium, fertilisers, hydrogen and power"],
             ["15 Jan", "EUA Dec-26 trades above €92/t", "Highest carbon price in more than two years"],
             ["5 Mar", "2040 target adopted; ETS2 moved to 2028", "Long-term carbon trajectory fixed in law"],
             ["7 Apr", "First CBAM certificate price: €75.36/t", "Border carbon cost becomes a known number"],
             ["22 Apr", "AccelerateEU published", "Biomethane named as a domestic supply lever"],
             ["22 Oct", "TTF near €89/MWh", "Up 177% since February"],
         ]),
         src(("ICAP", "https://icapcarbonaction.com/en/news/eu-reaches-agreement-2040-climate-target-postpones-ets-2-one-year"),
             ("GMK Center", "https://gmk.center/en/news/european-carbon-prices-exceeded-e90-t-in-january/"),
             ("Homaio", "https://homaio.com/post/2030-eua-price-predictions-expert-analysis-of-3-scenarios"),
             ("Brussels Times", "https://www.brusselstimes.com/2091683/eu-unveils-accelerateeu-clean-energy-plan-amid-mounting-fossil-fuel-crisis")) + ".")}

<h2>Why the molecule matters here</h2>
<p>Electrification will carry most of Europe's decarbonisation. A large share of demand still needs a gas or liquid fuel: high-temperature industrial heat, chemicals, heavy road transport, shipping, and seasonal balancing of the power system. For that demand the realistic options are imported fossil gas, hydrogen, liquid biofuels and biomethane.</p>
<p>Of these, biomethane is the only one that is produced domestically, chemically identical to natural gas, compatible with existing grids and burners, and commercially mature today. A plant fed by manure, crop residues or food waste injects into the same network that carries imported LNG. No new end-use equipment is needed.</p>

<h2>Implications</h2>
<p>For industrial buyers, fossil gas now carries three price risks at once: the commodity, the EU carbon price and, for exporters into the EU and their competitors, the border price. A multi-year biomethane contract addresses all three, which is why procurement teams that treated it as a sustainability purchase are starting to treat it as a hedge.</p>
<p>For investors, the security framing matters because it widens political support. Climate policy can be delayed, as ETS2 was. Security policy tends to outlast changes of government. Biomethane now has both behind it.</p>
<p>For governments, the 2030 target of 35 bcm is out of reach on the current build rate, which we examine in the second and third parts of this series. The lever that moves investment fastest is revenue certainty, through contracts for difference, auctions and blending obligations, rather than capital grants alone.</p>

<h2>Outlook</h2>
<p>Gas prices may ease if shipping normalises, and EUA prices will continue to move with them. We do not think the change in buyer behaviour will reverse with the price. The 2026 shock has shown industrial and public buyers what an imported molecule costs in a crisis, and the regulatory calendar to 2030 adds carbon cost on top. Capital that builds domestic renewable gas supply now is entering at a point where demand is supported by climate law and by security policy at the same time.</p>
""",
)

# ---------------------------------------------------------------- 2
A2_PLANTS = bars([("2018", 483), ("2020", 729), ("2021", 1023), ("2022–23", 1322),
                  ("2024", 1548), ("2025", 1678), ("2026", 1975)],
                 "Biomethane plants in operation in Europe by map edition, 2018 to 2026", highlight=-1)
A2_GAP = stack([("Installed, mid-2026", 8.2, "accent"),
                ("Committed pipeline", 9.0, "mid"),
                ("No identified project", 17.8, "gap")], 35,
               "Biomethane capacity versus the 35 bcm 2030 target, in bcm per year", unit=" bcm")

A2 = dict(
    slug="european-biomethane-market-2026",
    title="Biomethane at 8 bcm: how far Europe has come and how far it has to go",
    short="Biomethane at 8 bcm",
    part=2,
    standfirst=("Installed capacity grew 17% in a year and investment commitments reached €36 billion. "
                "Even if every announced project is built, Europe reaches about half of its 2030 target."),
    keypoints=[
        "Europe had 1,975 biomethane plants and 8.2 bcm/year of capacity at the end of Q2 2026, after 327 plants were commissioned in twelve months.",
        "Announced investment of €36 billion would add about 9 bcm by 2030, leaving roughly 18 bcm of the 35 bcm target without an identified project.",
        "Five countries produce 95% of output. The next phase of growth will come from new markets and from multi-plant platforms.",
    ],
    seo="Europe's biomethane capacity reached 8.2 bcm in 2026 across 1,975 plants. The gap to the 35 bcm 2030 target and where growth will come from.",
    keywords="European biomethane market, biomethane capacity Europe 2026, REPowerEU 35 bcm, biomethane investment",
    body=f"""
<p>The European Biogas Association and Gas Infrastructure Europe published the 2026 European Biomethane Map on 1 July. It shows 8.2 bcm a year of installed capacity at the end of the second quarter, an increase of more than 1 bcm, or 17%, on the previous year. The number of operating plants rose from 1,678 to 1,975, with 327 new plants entering operation. The plant count has roughly quadrupled since 2018.</p>

{exhibit(1, "Biomethane plants in operation in Europe, by map edition", A2_PLANTS,
         src(("EBA / GIE European Biomethane Map 2026", "https://advancedbiofuelsusa.info/europe-adds-1-bcm-of-biomethane-production-but-acceleration-of-its-own-source-of-renewable-gas-can-go-much-faster"),
             ("GIE, earlier editions", "https://www.gie.eu/?p=3977")) + ".",
         "Each edition counts plants in operation at its data cut-off. The 2026 edition covers data to the end of Q2 2026.")}

<h2>A larger and more industrial fleet</h2>
<p>The average European biomethane plant now produces about 472 Nm³/h. That is several times the size of the farm biogas engines that dominated the previous decade, and it reflects a shift from electricity generation on site to upgrading and injection into the gas grid.</p>
<p>The wider biogas sector is much bigger than the biomethane fleet. Combined biogas and biomethane output in Europe was 22 bcm in 2024, 19 bcm of it in the EU, according to the EBA's Statistical Report. Most of that biogas is still burned in engines to make power and heat. Each of those sites is a candidate for conversion to grid injection, which is often cheaper and faster than a greenfield project.</p>
<p>Leadership has also changed. France overtook Germany as Europe's largest biomethane producer, on the back of a feed-in tariff that made small and mid-sized injection plants bankable.</p>

<h2>The arithmetic of 2030</h2>
<p>The EBA's 2026 Investment Outlook counts €36 billion of committed investment, up from €28 billion a year earlier. If all of it is spent, it adds about 9 bcm of annual capacity by 2030. Added to the installed base, that takes Europe to roughly 17 bcm, about half of the 35 bcm REPowerEU target.</p>

{exhibit(2, "Capacity against the 2030 target (bcm per year)", A2_GAP,
         src(("EBA Biomethane Investment Outlook 2026", "https://uabio.org/en/news/19820/"),
             ("EBA / GIE", "https://advancedbiofuelsusa.info/europe-adds-1-bcm-of-biomethane-production-but-acceleration-of-its-own-source-of-renewable-gas-can-go-much-faster")) + "; Qiao Partners calculation.",
         "Installed capacity covers Europe including non-EU countries; the 35 bcm target is for the EU. The comparison is indicative.")}

<p>Feedstock does not appear to be the limit. A 2026 Guidehouse study for the EBA puts the EU's sustainable potential at 31–32 bcm by 2030 and up to 184 bcm by 2050. The binding constraints are permitting time, grid connection, revenue certainty and the capacity of developers and contractors to build. The EBA also notes that five countries account for 95% of European production. Most member states have barely started.</p>

<h2>Where the growth will come from</h2>
{exhibit(3, "European biomethane markets by stage of development",
         table(["Stage", "Examples", "Position", "Typical opportunity"], [
             ["Mature", "France, Germany, Denmark, Italy, Netherlands", "Established tariffs or quotas; competition for feedstock", "Consolidation, repowering, conversion of biogas engines to injection"],
             ["Scaling", "Spain, Belgium, United Kingdom, Austria, Sweden", "Frameworks in place, pipelines growing", "Greenfield platforms backed by offtake contracts"],
             ["Early", "Poland, Czechia, Romania, Hungary, Greece, Baltic states", "Support schemes legislated in 2025–26", "Early positions in land, grid capacity and feedstock"],
         ]),
         "Qiao Partners, based on EBA country data and national legislation.")}

<p>The first wave of European biomethane was led by farmers and driven by national subsidy. We expect the next wave to look different: portfolios of 10 to 50 plants owned by infrastructure funds and utilities, built to standard designs, run from central control rooms, and earning revenue from several sources at once. Spain's Asterion Industrial Partners, which plans €1.5 billion for a pan-European platform targeting 20 operating plants by the end of 2026, is an example of the model.</p>

<h2>Outlook</h2>
<p>At the current build rate Europe will add perhaps 1–1.5 bcm a year. Reaching 35 bcm by 2030 would require something closer to 6 bcm a year. The target will probably be missed, but the size of the shortfall still matters to investors: it means demand for new capacity, and for the certificates it generates, will exceed supply through the end of the decade. We see the most attractive entry points in the early markets, where policy has recently been put in place and competition for sites and feedstock is still limited.</p>
""",
)

# ---------------------------------------------------------------- 3
A3_RATE = bars([("Commissioned, last 12 months", 327),
                ("Needed per year: committed pipeline", 480),
                ("Needed per year: 35 bcm target", 1430)],
               "Biomethane plants commissioned per year compared with the build rate needed by 2030", highlight=2)

A3 = dict(
    slug="biomethane-equipment-market-europe",
    title="Building 6,500 plants: where Europe's biomethane equipment spend will go",
    short="The equipment build-out",
    part=3,
    standfirst=("Reaching the 2030 target would require more than four times the current annual build rate. "
                "The constraint has moved from feedstock and finance to manufacturing and construction capacity."),
    keypoints=[
        "On our estimate, about 6,500 plants of today's average size would be needed to close the gap to 35 bcm, against 327 commissioned in the last year.",
        "Forecasts put the global biogas upgrading market at $1.6–2.2 billion in 2026, growing about 10–11% a year, with Europe taking 45–66% of demand.",
        "Upgrading, digestion and balance of plant, CO₂ recovery and bio-LNG form four distinct equipment markets, with service revenue on top.",
    ],
    seo="Europe would need about 6,500 more biomethane plants to reach 35 bcm by 2030. Sizing the upgrading, digestion, CO₂ and bio-LNG equipment markets.",
    keywords="biomethane equipment market, biogas upgrading market Europe, membrane upgrading, bio-LNG equipment, biogenic CO2",
    body=f"""
<p>Europe's 1,975 biomethane plants produce about 8.2 bcm a year, or roughly 4.2 million cubic metres each. At that average size, closing the gap to 35 bcm would require about 6,500 new plants. Building only the projects already committed under the EBA's €36 billion pipeline would require about 2,200. Spread over the four and a half years to the end of 2030, those figures imply roughly 1,430 and 480 plants a year respectively. Europe commissioned 327 in the last twelve months.</p>

{exhibit(1, "Plants commissioned per year, actual and required to 2030", A3_RATE,
         "EBA / GIE European Biomethane Map 2026; EBA Biomethane Investment Outlook 2026; Qiao Partners calculation.",
         "Requirement assumes the 2026 average plant output of about 4.2 million m³ a year and an end-2030 deadline. Larger plants would reduce the count, not the equipment value.")}

<p>Larger plants would bring the count down, and some capacity will come from converting existing biogas sites. Neither changes the conclusion. Europe's developers, engineering contractors and equipment suppliers would need to deliver several times their current output for the rest of the decade.</p>

<h2>How large is the equipment market</h2>
<p>Commercial forecasts differ in scope but agree on direction, and on Europe's share of demand.</p>

{exhibit(2, "Published forecasts for biogas upgrading equipment",
         table(["Source (date)", "Scope", "Forecast", "Growth", "Europe share"], [
             ['<a href="https://www.gminsights.com/industry-analysis/biogas-upgrading-technology-market" target="_blank" rel="noopener">Global Market Insights</a> (Jun 2026)', "Upgrading technology, global", "$2.2bn (2026) to $5.9bn (2035)", "11.2% a year", "Largest region"],
             ['<a href="https://www.persistencemarketresearch.com/market-research/biogas-upgrading-market.asp" target="_blank" rel="noopener">Persistence Market Research</a> (Aug 2026)', "Upgrading, global", "$1.6bn (2026) to $3.2bn (2033)", "10.1% a year", "44.7%"],
             ['<a href="https://www.gasworld.com/story/biogas-upgrading-market-to-top-4bn-by-2030/2254502.article/" target="_blank" rel="noopener">gasworld</a>', "Upgrading, global", "Above $4bn (2030)", "–", "61.9%"],
             ['<a href="https://marketpublishers.com/report/equipment/global-biogas-upgrading-equipment-market-2018-by-manufacturers-forecast-to-2023.html" target="_blank" rel="noopener">QYResearch</a> (2026)', "Upgrading equipment, global", "–", "–", "About 66%"],
             ['<a href="https://www.bccresearch.com/market-research/energy-and-resources/biogas-upgrading.html?ro=yes" target="_blank" rel="noopener">BCC Research</a>', "Gas separation membranes, all uses", "$1.5bn (2025) to $2.5bn (2031)", "9.1% a year", "–"],
         ], cls="tbl-dense"),
         "Publishers as linked. Figures are not directly comparable because scope differs.")}

<p>Upgrading is only part of a plant's capital cost. Digesters, feedstock handling, gas storage, compression, grid connection, liquefaction and CO₂ recovery together account for the larger share. The total equipment market for European biomethane is therefore several times the upgrading figures above.</p>

<h2>Four equipment markets</h2>
<p><strong>Upgrading.</strong> About half of Europe's grid-connected plants separate methane from CO₂ with membranes, according to the EBA. The rest use pressure swing adsorption, water or amine scrubbing, or cryogenic systems. Membranes have gained share because they are modular and cheap to run, and suppliers now sell containerised units from about 80 to 12,000 Nm³/h. Margin sits in the membrane modules, compressors and control systems.</p>
<p><strong>Digestion and balance of plant.</strong> Tanks, mixers, double-membrane gas holders, pumps, heat exchangers, desulphurisation and feedstock pre-treatment. This is high-volume steel and polymer fabrication that can be standardised. In tenders it is decided mostly on price and delivery time.</p>
<p><strong>CO₂ recovery.</strong> Upgrading produces a stream of nearly pure biogenic CO₂ that most plants still vent. Liquefied, it can be sold to food, drinks and greenhouse users, or stored permanently. A Swiss project has contracted with INEOS to store biogenic CO₂ from biomethane production under the Danish North Sea from 2026.</p>
<p><strong>Bio-LNG and bio-CNG.</strong> Many feedstock sources are far from a gas grid. Small-scale liquefaction, cryogenic storage, ISO containers and fuelling stations allow those plants to sell to road transport and shipping, where compliance markets pay a premium.</p>
<p>Each plant also creates about 20 years of service revenue: remote monitoring, biological optimisation, membrane replacement and maintenance contracts.</p>

<h2>Who is building</h2>
<p>European integrators are expanding but under pressure. Germany's EnviTec Biogas announced a €100 million biomethane investment in July 2026, while guiding its 2026 pre-tax profit down to €5–15 million after regulatory setbacks. Weltec Biopower has built more than 450 plants in 27 countries. Asian suppliers have entered the market: Chinese manufacturers already supply membrane upgrading units and double-membrane gas holders to projects in Poland, Spain, Italy and the United Kingdom.</p>

{exhibit(3, "What buyers weigh when selecting equipment",
         table(["Buyer priority", "What suppliers need to show"], [
             ["Time to commissioning", "Pre-engineered, containerised, factory-tested units"],
             ["Bankability", "European references, performance guarantees, insured warranties"],
             ["Methane slip", "Certified low-slip performance; it feeds directly into RED III GHG savings and certificate value"],
             ["Local service", "Spares and technicians in Europe, response within 24–48 hours"],
             ["Total cost of ownership", "Energy use per Nm³, membrane life, availability above 95%"],
         ]),
         "Qiao Partners.")}

<h2>Outlook</h2>
<p>We expect the equipment market to move from project engineering toward industrial manufacturing: standard designs, repeatable modules, volume pricing and long service contracts. Suppliers able to deliver standard 250–1,000 Nm³/h trains, assembled and serviced in Europe, are likely to win a disproportionate share of the next wave. Because European manufacturing capacity is limited, partnerships with Asian suppliers are becoming a practical question for developers rather than a political one. We look at how those partnerships can be structured in the next part of the series.</p>
""",
)

# ---------------------------------------------------------------- 4
A4 = dict(
    slug="china-europe-biomethane-investment",
    title="China and Europe's biomethane build-out: structures that work",
    short="China and the build-out",
    part=4,
    standfirst=("Europe is short of manufacturing capacity for biomethane plants. Chinese suppliers have that capacity, "
                "but they face a tighter EU industrial policy. The structure of a market entry now matters as much as the price."),
    keypoints=[
        "Chinese manufacturers already supply upgrading units and gas holders into European projects; demand for capacity will rise through 2030.",
        "The Net-Zero Industry Act applies resilience criteria in public tenders and auctions from 2026. The proposed Industrial Accelerator Act would attach joint-venture and know-how conditions to large foreign investments.",
        "EU-majority joint ventures, technology licensing and minority stakes in European platforms are the entry models most likely to withstand that policy shift.",
    ],
    seo="How Chinese manufacturers and investors can take part in Europe's biomethane build-out under the Net-Zero Industry Act, the Industrial Accelerator Act and FDI rules.",
    keywords="Chinese investment Europe biomethane, Net-Zero Industry Act resilience criteria, Industrial Accelerator Act FDI, China EU clean tech, biogas equipment China",
    body=f"""
<p>The previous part of this series estimated that Europe would need to commission several times more biomethane plants each year than it does today to approach its 2030 target. European integrators cannot fabricate, ship and commission at that rate on their own. Chinese manufacturers can supply membranes, steel vessels, compressors and cryogenic equipment in volume and at lower cost. The obstacle is that 2026 has also brought the most assertive EU industrial policy in a generation.</p>

<h2>Why the opportunity exists</h2>
<p>Three conditions favour Chinese participation. The first is the capacity gap described above. The second is cost: higher European energy and labour costs have raised fabrication prices for EU vendors at the moment developers most need cheaper capital equipment. The third is experience. China operates one of the largest biogas programmes in the world, its planning framework has included thousands of large-scale plants, and Chinese suppliers already export double-membrane gas holders and membrane upgrading units to European projects.</p>
<p>The relationship already runs in both directions. EnviTec Biogas has built several plants in China, and Air Liquide has launched a biomethane business there. European firms know Chinese partners, and Chinese firms have references with European technology.</p>

<h2>The rules a Chinese entrant has to navigate</h2>
{exhibit(1, "EU rules relevant to Chinese participation in biomethane, as of 1 November 2026",
         table(["Instrument", "What it does", "Status", "Relevance to biomethane"], [
             ["Net-Zero Industry Act", "Requires non-price resilience and sustainability criteria in public procurement and renewable energy auctions", "Applies from 30 Dec 2025 to at least 30% of auction volume or 6 GW a year; tender guidance issued July 2026", "Equipment from a dominant third-country supplier can score lower in subsidised tenders; EU assembly improves the score"],
             ["Industrial Accelerator Act (proposal)", "Investments above €100m in sectors where one third country holds over 40% of global capacity must meet four of six conditions, including a JV with at most 49% foreign ownership and IP licensing", "Proposed 4 Mar 2026; in the legislative process, adoption expected 2027", "Aimed mainly at batteries and electric vehicles; it shows how Brussels intends to treat large Chinese investments"],
             ["Foreign Subsidies Regulation", "Commission review of foreign state support in large tenders and acquisitions", "In force", "Relevant to large platform acquisitions and public contracts"],
             ["National FDI screening", "Member-state review of investment in energy and critical infrastructure", "In force in most member states", "Grid-connected plants can trigger review; minority and JV structures are easier to clear"],
             ["Product and sustainability rules", "CE marking, pressure equipment and ATEX rules; RED III GHG calculation; certification schemes such as ISCC", "In force", "Lenders and certifiers audit equipment performance as well as price"],
         ], cls="tbl-dense"),
         src(("Herbert Smith Freehills Kramer", "https://www.hsfkramer.com/zh/notes/energy/2025-posts/the-net-zero-industry-act-new-implementing-rules-to-accelerate-clean-technology-manufacturing-in-the-eu"),
             ("Carbon Pulse", "https://carbon-pulse.com/534444/"),
             ("Jones Day", "https://trendingnowinesg.jonesday.com/post/102mm0d/eu-industrial-accelerator-act-what-companies-need-to-know"),
             ("Squire Patton Boggs", "https://www.squirepattonboggs.com/media/v10hvn1w/industrial-accelerator-act-a-general-overview.pdf"),
             ("JD Supra", "https://www.jdsupra.com/legalnews/european-commission-proposes-industrial-7246033/")) + ".")}

<p>China's Ministry of Commerce warned in April that it would take countermeasures if the Industrial Accelerator Act harms Chinese companies. For a company entering Europe, this means the durability of its position depends on how the entry is structured, not only on whether it complies with the rules in force today.</p>

<h2>Five ways in</h2>
{exhibit(2, "Entry models for Chinese manufacturers and investors",
         table(["Model", "How it works", "Capital required", "Exposure to policy change", "Suited to"], [
             ["EU assembly and service JV", "Chinese core components; an EU-majority company assembles, certifies and services", "Medium", "Low", "Manufacturers seeking lasting market share"],
             ["Technology licence", "Membrane, compression or cryogenic IP licensed to a European manufacturer for royalties", "Low", "Low", "Technology owners that do not want to build in Europe"],
             ["Minority stake in a European platform", "Investor takes less than 50% of a multi-plant developer, often with equipment supply rights", "Medium to high", "Low to medium", "Funds, industrial groups, family offices"],
             ["Vendor finance", "Equipment supplied on deferred terms in return for project equity or a long O&amp;M contract", "Medium", "Medium", "Manufacturers with balance sheet; developers short of capital"],
             ["Direct export", "Complete systems sold through European distributors", "Low", "High", "Components, spares, unsubsidised projects"],
         ], cls="tbl-dense"),
         "Qiao Partners.")}

<h2>What European buyers and lenders ask for</h2>
<p>In our experience the same five questions decide most procurement processes. Is the warranty enforceable, through an EU-domiciled entity and insurance, over a 20-year asset life? Is performance certified, particularly methane slip and energy use per Nm³, which feed directly into RED III GHG savings and certificate value? Are there operating references in Europe? Can spares and technicians reach the site within 24 to 48 hours? And is the documentation complete, from CE files to the cybersecurity of connected control systems and transparency on how the supplier is financed?</p>
<p>Two or three operating European plants carry more weight with a lender than a much larger reference list in Asia.</p>

<h2>Outlook</h2>
<p>We expect the Chinese companies that do well in European biomethane to combine Chinese manufacturing cost and depth with European assembly, majority European control of the operating company, and bankable guarantees. Pure export will remain possible for components and smaller projects, but it is the most exposed to tender scoring and to future trade measures. The firms that establish installed bases between 2026 and 2028 will also hold the service contracts on those plants when Europe's build-out peaks around 2030.</p>
""",
)

# ---------------------------------------------------------------- 5
A5 = dict(
    slug="biomethane-revenue-stack-eu-regulation",
    title="The biomethane revenue stack: how EU regulation sets what a plant earns",
    short="The revenue stack",
    part=5,
    standfirst=("A biomethane plant sells gas and a set of attributes created by law. Most of the value depends on "
                "which buyer receives which attribute, and on never claiming the same benefit twice."),
    keypoints=[
        "One MWh of biomethane can earn revenue from the gas itself, national support, certificates, transport quotas, maritime compliance and carbon markets, plus CO₂ and digestate.",
        "ETS2 will add a new group of obligated buyers from 1 January 2028. Certified biomethane counts as zero-emission under it.",
        "Carbon intensity sets the price. Low-slip, manure-based plants with CO₂ recovery earn the highest premiums in quota and maritime markets.",
    ],
    seo="How EU ETS, ETS2, RED III, FuelEU Maritime, CBAM and guarantees of origin combine to set the revenue of a European biomethane plant.",
    keywords="biomethane revenue model, biomethane ETS2, FuelEU Maritime bio-LNG, Union Database, guarantees of origin, RED III",
    body=f"""
<p>The revenue of a European biomethane plant is the sum of a physical gas price and up to five attributes created by regulation, plus by-products. In 2026 two developments lifted the whole stack. Fossil gas repriced to near €89/MWh. And each of the carbon instruments that biomethane offsets, from the EU ETS and its maritime extension to CBAM and the coming ETS2, moved closer to full effect.</p>

{exhibit(1, "Revenue layers available to a European biomethane producer",
         table(["Layer", "Instrument", "Paid by", "What drives it in 2026–28"], [
             ["Commodity", "Physical gas sold at a hub (TTF, THE, PEG)", "Shippers, utilities, industry", "TTF near €89/MWh on 22 Oct 2026"],
             ["National support", "Feed-in tariffs, contracts for difference, auctions, capital grants", "Governments", "New schemes in Poland, Greece and elsewhere; AccelerateEU"],
             ["Certificates", "Guarantees of origin; proofs of sustainability under RED III, tracked in the Union Database", "Corporate buyers, utilities", "Scope 1 reporting; RED III transposition"],
             ["Transport quotas", "National GHG-reduction quotas on fuel suppliers, e.g. Germany's THG-Quote", "Fuel suppliers", "Low carbon-intensity and manure-based gas earn a premium"],
             ["Maritime", "FuelEU Maritime GHG-intensity limits (2% below 2020 from 2025, 6% from 2030) and the EU ETS for shipping", "Shipowners, compliance pools", "Bio-LNG demand from LNG-fuelled fleets"],
             ["Carbon markets", "EU ETS (sustainable biomethane zero-rated); ETS2 from 2028", "Installations, fuel suppliers", "Certified biomethane treated as zero-emission under ETS2"],
             ["By-products", "Biogenic CO₂, digestate fertiliser", "Food and drink, greenhouses, CO₂ storage, farms", "First storage contracts; fertiliser prices"],
         ], cls="tbl-dense"),
         src(("3Degrees", "https://3degreesinc.com/insights/eu-ets2-what-it-means-and-why-biomethane-matters"),
             ("ANSA via SoldiOnline", "https://www.soldionline.it/notizie/forex-commodities/gas-ue-177-da-febbraio-cosa-ce-dietro-il-balzo-del-ttf-a-89-mwh")) + "; Qiao Partners.",
         "Not every layer is open to every plant. Eligibility depends on feedstock, certification and member state.")}

<h2>The carbon layer is changing fastest</h2>
<p><strong>EU ETS.</strong> Analysts expect allowance supply to tighten through 2026 and 2027. In December 2025 Montel forecast a 2026 average near €92/t; high gas prices then pulled the market back into the mid-€70s by spring. Member states are writing practical rules for using biomethane inside ETS installations, and Italy approved such guidelines in 2026.</p>
<p><strong>ETS2.</strong> From 1 January 2028, suppliers of fuel for buildings and road transport must hold allowances for the emissions of what they sell. The first surrender is due in May 2029. Each certified MWh of biomethane in the distribution grid reduces that obligation, which creates a new and large group of buyers.</p>
<p><strong>CBAM.</strong> With the first certificate price set at €75.36/tCO₂, EU producers of steel, cement, fertilisers, aluminium and hydrogen that cut emissions from process heat gain a cost advantage over carbon-intensive imports and over domestic competitors that do not.</p>

<h2>Three rules for combining revenue</h2>
<p><strong>Each benefit is claimed once.</strong> The same MWh cannot count towards a transport quota, a shipping pool and a company's Scope 1 reduction at the same time. RED III mass balance and the Union Database exist to enforce this, and buyers increasingly audit it.</p>
<p><strong>Carbon intensity sets the price.</strong> Feedstock and plant performance determine the GHG score. Manure-based plants with low methane slip and CO₂ recovery achieve the best scores and the highest premiums. Poor slip control reduces value in every layer.</p>
<p><strong>Gas and attributes are priced separately.</strong> Long-term offtake contracts increasingly combine a hub-indexed price for the gas with fixed or floored prices for the attributes. Producers get revenue a lender can underwrite, and buyers get compliance at a known cost.</p>

<h2>Outlook</h2>
<p>We expect the next source of advantage in European biomethane to be commercial rather than technical. Producers and offtakers that can certify, track and allocate each attribute to the market that pays most for it, across borders and through the 2028 start of ETS2, will earn margins that a plant selling a single bundled product does not. For investors, this means the quality of a project's certification and offtake structure deserves as much diligence as its engineering.</p>
""",
)

# ---------------------------------------------------------------- 6
A6 = dict(
    slug="poland-biomethane-market-2026",
    title="Poland: Europe's next biomethane market",
    short="Poland",
    part=6,
    standfirst=("Until 2025 Poland was the largest gap on Europe's biomethane map. In 2026 it gained an auction "
                "scheme, a grant programme and simpler grid rules. The window for early positions is 2026 to 2028."),
    keypoints=[
        "Poland now has a feed-in premium for plants up to 1 MW, an auction scheme for larger plants passed by parliament in September, and PLN 800 million of capital grants.",
        "The Polish Biomethane Organisation counted 122 projects in development at the end of Q3 2025, and 208 agricultural biogas plants were registered by Q1 2026.",
        "A large agri-food sector, a gas-dependent industry and access to German and maritime compliance markets make Polish volumes valuable beyond Poland.",
    ],
    seo="Poland's new biomethane auctions, PLN 800m in grants and 122-project pipeline. Why 2026 to 2028 is the window for early positions.",
    keywords="Poland biomethane, biometan Polska, biomethane auction Poland, NFOŚiGW biomethane grants, CEE renewable gas",
    body=f"""
<p>Poland has one of Europe's largest agricultural feedstock bases and an industry that depends heavily on gas, yet until 2025 it had almost no biomethane production. Law firm Rödl &amp; Partner described it as the largest gap on the European biomethane map. That has changed quickly. By the autumn of 2026 Poland had a support scheme for small plants, an auction scheme for large ones, a grant programme and new rules on grid access.</p>

<h2>The policy framework</h2>
{exhibit(1, "Polish support for biomethane, as of 1 November 2026",
         table(["Instrument", "What it offers", "Status"], [
             ["Feed-in premium for plants up to 1 MW", "Producers sell at market and are paid the difference to a guaranteed price", 'In operation; entry open until 30 June 2027 (<a href="https://cms.law/en/pol/legal-updates/poland-enacted-law-creating-incentives-for-investing-in-renewable-energy" target="_blank" rel="noopener">CMS</a>)'],
             ["Auction scheme for plants above 1 MW", "Competitive auctions with sustainability criteria; imported biomethane may take up to 5% of annual volume", 'Approved by government 14 July 2026; passed by the Sejm in early September; RES Act amendment adopted by the Senate 24 September (<a href="https://www.qcintel.com/biofuels/article/polish-legislators-vote-for-biomethane-support-scheme-law-72371.html" target="_blank" rel="noopener">QCI</a>, <a href="https://kpmg.com/pl/en/insights/law/energy-newsletter-biomethane-gets-a-new-support-scheme.html" target="_blank" rel="noopener">KPMG</a>)'],
             ["NFOŚiGW grant programme", "Up to 45% of eligible capital cost from a PLN 800 million (about €189 million) Modernisation Fund allocation", 'Applications from H1 2026 (<a href="https://task37.ieabioenergy.com/wp-content/uploads/sites/32/2026/04/Newsletter-T37-03_2026-Policy-issues.pdf" target="_blank" rel="noopener">IEA Bioenergy</a>)'],
             ["Energy Law amendment", "Simpler procedures for biogas; direct biomethane pipelines where grid connection is uneconomic", "Signed 2 April 2026"],
         ], cls="tbl-dense"),
         src(("Bird &amp; Bird", "https://www.twobirds.com/en/insights/2025/poland-introduces-auction-based-support-system-for-biomethane-production-in-installations-above-1-mw"),
             ("Poland Insight", "https://polandinsight.com/polands-biogas-and-biomethane-market-needs-stronger-support-to-unlock-its-full-potential-66601/")) + " and as linked.")}

<p>Early drafts sized the first auction at about 300 million m³ a year, around 3.1 TWh, which the Polish Biomethane Organisation estimated would support roughly 50 new plants. Final volumes and dates depend on the implementing regulations.</p>

<h2>The pipeline</h2>
<p>The Polish Biomethane Organisation identified 122 biomethane projects at various stages of development by the end of the third quarter of 2025. Separately, 208 agricultural biogas installations were registered with KOWR by the end of the first quarter of 2026. Most of those burn biogas for power and heat, and many could be converted to grid injection. Public capital is also taking part: in January 2026 the Polish Green Fund signed a PLN 59 million agreement with Green Gas Energy for nine farm-based biomethane plants.</p>

<h2>Why Polish volumes matter outside Poland</h2>
<p>Poland's livestock, dairy and food-processing sectors produce manure and residues, the low carbon-intensity feedstocks that earn the highest premiums in German transport quotas and in maritime compliance. Domestic demand is substantial: chemicals, fertilisers, refining, glass, food processing and district heating all use gas and are exposed to the EU ETS, CBAM and, from 2028, ETS2. Through mass balance and the Union Database, certified Polish biomethane can also be sold to buyers elsewhere in the EU. And Poland's location makes it a practical base for assembling and servicing equipment for Central and Eastern Europe.</p>

<h2>Risks</h2>
{exhibit(2, "Execution risks and mitigations",
         table(["Risk", "Mitigation"], [
             ["Delays to auction implementing rules", "Qualify early phases under the 1 MW scheme or grants; keep permits auction-ready"],
             ["Grid connection capacity", "Use the new direct-pipeline route, cluster plants, or liquefy to bio-LNG"],
             ["Competition for feedstock", "Sign multi-year manure and residue contracts with cooperatives early"],
             ["Local acceptance", "Odour, traffic and digestate management plans; benefit sharing with communities"],
         ]),
         "Qiao Partners.")}

<h2>Outlook</h2>
<p>Poland today resembles France about a decade ago: the policy framework is in place, and the market has not yet responded. In our experience that gap closes within three to four years. Developers, suppliers and investors who secure feedstock, land, grid capacity and offtake before the first large auctions clear will set the terms for those who follow.</p>
""",
)

ARTICLES = [A1, A2, A3, A4, A5, A6]
