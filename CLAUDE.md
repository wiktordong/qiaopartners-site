# Qiao Partners website — instructions for Claude

Static site for qiaopartners.eu, hosted on GitHub Pages (repo `wiktordong/qiaopartners-site`, CNAME `qiaopartners.eu`). The owner, Wiktor Dong, is not a developer: do the technical work for him and explain results in plain words.

## How the site is built
- Never hand-edit the generated `index.html`, `pl/index.html` or `zh/index.html`. Edit the sources and rebuild:
  - `_src/content.py`: all copy, per language (`L["en"]`, `L["pl"]`, `L["zh"]`), plus settings `LINKEDIN`, `EMAIL`, `CALENDLY_URL`, `WHATSAPP`, `FORM_ENDPOINT`, `GOOGLE_SITE_VERIFICATION`, `BING_SITE_VERIFICATION` (paste the codes from Search Console / Bing Webmaster Tools, rebuild, push). Later `L[...].update(...)` blocks at the end of the file override earlier keys.
  - `MEMBERS` in `_src/content.py` lists confirmed chamber memberships (Memberships section); a logo at `img/members/<slug>.png` replaces the text tile automatically.
  - `_src/build.py`: page template, CSS and JS. Also writes `robots.txt`, `sitemap.xml`, `llms.txt`.
  - `_src/base.css`: original visual design (navy `#0A1C36`, baby blue `#8EC5F0`, Hanken Grotesk, light/dark themes). Keep this look.
  - `_src/insights/`: the Insights section. `articles.py` holds the articles (HTML bodies, exhibits via `charts.py`), `build_insights.py` renders `/insights/` plus `/pl/insights/` and `/zh/insights/` indexes, `insights.css` styles them. `RELEASE` in `build_insights.py` sets one release date per article (weekly from 1 Nov 2026); only articles dated today or earlier are built.
  - `.github/workflows/weekly-insights.yml` rebuilds every Sunday 06:05 Warsaw and pushes, so the next article goes live on its date.
  - `_src/articles/<lang>/<slug>.md`: older drafted articles, not yet published.
- Rebuild: `python3 _src/build.py` from the repo root.

## Business rules for copy
- Qiao Partners is a commercial advisory firm: market entry, market diagnosis, go-to-market strategy, EU business development and lead generation, entity/certification/tax setup with partner firms, regulation (incl. CBAM, EU ETS) and government relations, and China entry for European companies.
- It does not invest, manage funds or give investment advice. Never add investor-introduction or capital-raising wording (Wiktor wants to stay clear of MiFID).
- Three languages always: English, Polish, Simplified Chinese. Every new page exists in all three.
- Facts in articles carry a date and a linked source.

## Git and publishing
- Work on a branch (currently `redesign-2026-11`). Pushing to `main` puts the site live: only do it when Wiktor explicitly says so.
- See `IMPLEMENTATION_BRIEF.md` for the current task.
