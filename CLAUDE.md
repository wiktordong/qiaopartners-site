# Qiao Partners website — instructions for Claude

Static site for qiaopartners.eu, hosted on GitHub Pages (repo `wiktordong/qiaopartners-site`, CNAME `qiaopartners.eu`). The owner, Wiktor Dong, is not a developer: do the technical work for him and explain results in plain words.

## How the site is built (rebuilt 13 Nov 2026, repositioning)
- Never hand-edit generated HTML (`index.html`, `about/`, `services/`, `industries/`, `contact/`, `china-entry/`, and the same under `pl/`, `zh/`, `ru/`). Edit sources and rebuild: `python3 _src/build.py`.
  - `_src/lang/en.py`, `pl.py`, `zh.py`, `ru.py`: ALL copy, one file per language, identical structure (the build stops if keys or list lengths differ).
  - `_src/settings.py`: `EMAIL`, `LINKEDIN`, `CALENDLY_URL`, `WHATSAPP`, `FORM_ENDPOINT` (FormSubmit), search-console codes, `MEMBERS` (confirmed chamber memberships only; logos in `img/members/`).
  - `_src/site.css`: design system (white in light mode, navy in dark mode via prefers-color-scheme; bronze accents; Hanken Grotesk + Golos Text for Cyrillic, same as the previous site; previous-site animations: word-by-word headline, image mask reveals, logo stroke, count-up, reading progress). Fonts are self-hosted in `assets/fonts/` (`_src/fonts.css`) because Google Fonts is blocked in mainland China; Chinese uses system fonts. Built to `assets/site.css`.
  - `_src/chrome.py`: shared head (SEO, hreflang, JSON-LD), header, footer, network art and script, used by every page including Insights.
  - `_src/build.py`: page templates (home, about, services, industries, contact with FAQ + qualified enquiry form, china-entry), sitemap, robots, llms.txt.
  - `_src/insights/`: Insights (articles, translations, `RELEASE` dates, `HIDDEN` set). Uses the shared chrome; `insights.css` is scoped under `.ins`.
  - `.github/workflows/weekly-insights.yml` rebuilds every Monday.
  - Photos in `img/brand/` (bridge, glass office) were supplied by Wiktor in chat; licence to be confirmed.

## Business rules for copy
- Positioning: independent China–Europe market entry & strategic business development firm. Primary direction China → Europe; European companies entering China is a secondary page (`/china-entry/`). Four service lines: Strategic Advisory & Market Intelligence; Market Entry & Establishment; Commercial Development & Partnerships; European Representation & Expansion.
- Never fabricate clients, testimonials, partnerships, team size, offices or track record. Team employers (Goldman Sachs, J.P. Morgan, Tencent, Accenture) are prior employers only. No government-relations claims, no guaranteed outcomes, no public prices. Legal/tax/certification work is 'coordinated with qualified specialists'.
- It does not invest, manage funds or give investment advice. Never add investor-introduction or capital-raising wording (Wiktor wants to stay clear of MiFID).
- Four languages always: English, Polish, Simplified Chinese, Russian. Every page exists in all four.
- Facts in articles carry a date and a linked source.

## Git and publishing
- Work on a branch (currently `repositioning-2026-11`). Pushing to `main` puts the site live: only do it when Wiktor explicitly says so.
- See `IMPLEMENTATION_BRIEF.md` for open items needing Wiktor's verification.
