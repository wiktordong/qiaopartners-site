# Implementation brief — multi-page site (1 Nov 2026)

Wiktor does not want everything on one page. Turn the single page into a small multi-page site, in English, Polish and Chinese, keeping the current design.

## Target structure

| Page | EN path | PL path | ZH path | Content |
| --- | --- | --- | --- | --- |
| Home | `/` | `/pl/` | `/zh/` | Hero, About, quote, **What we do** (6 services), **How an engagement runs** (4 steps), Market trends (8 cards, Now / 2027–2030 / 2030–2035), team, key figures, short contact strip. Remove the full FAQ and the booking form from the home page. |
| Insights (blog index) | `/insights/` | `/pl/insights/` | `/zh/insights/` | List of articles, newest first: title, date, one-line summary, link. |
| Article | `/insights/<slug>/` | `/pl/insights/<slug>/` | `/zh/insights/<slug>/` | One page per article. |
| Book a call | `/book/` | `/pl/book/` | `/zh/book/` | Its own page, in the style of oumelabs.com/contact: heading, enquiry form on the left, Calendly calendar on the right (move the existing form and calendar here unchanged, including the drop-downs and the FormSubmit JS). |
| FAQ | `/faq/` | `/pl/faq/` | `/zh/faq/` | The 8 existing questions, with FAQPage JSON-LD. |

Wiktor asked for "a separate window that opens when people click Book a call": every "Book a call" button, the top banner and the hero button go to the `/book/` page of the current language. Ask him whether he wants it in the same tab (recommended) or a new tab (`target="_blank"`).

## Shared on every page
- Header with logo, nav (About, Services, Market trends, Insights, FAQ, Contact/Book), language switch that keeps the reader on the same page in the other language, "Book a call" button, and the "Now booking market checks for Q1 2027" banner.
- Footer with logo, disclaimer, email, LinkedIn, WeChat QR (`img/wechat-qr.jpg`) and WhatsApp QR (`img/whatsapp-qr.png`, link in `WHATSAPP`).
- Correct relative paths for images and favicons at every folder depth (e.g. `../../img/`), canonical URL and hreflang alternates per page.

## Articles
- Sources: `_src/articles/en/*.md` (3 drafted articles, front matter has `title`, `slug`, `date`, `author`, `summary_zh`).
- Build each article page from Markdown (tables, lists, links). Add `Article` JSON-LD (headline, author Wiktor Dong, datePublished, publisher Qiao Partners).
- PL and ZH: translate each article fully into `_src/articles/pl/` and `_src/articles/zh/` (use `summary_zh` as the Chinese lead). Wiktor speaks both languages and will review.
- End each article with a box: "Need help entering this market? Book a 30-minute market check" linking to `/book/`.
- Add every page to `sitemap.xml` and every article to `llms.txt`.

## Still waiting on Wiktor
- `CALENDLY_URL` in `_src/content.py` (he will create a 30-minute "Market check" event on Calendly and connect his Google or Outlook calendar).
- The first form submission triggers a FormSubmit confirmation email to contact@qiaopartners.eu; he must click it once.
- Approval to merge into `main` (goes live).

## Check before handing over
Run `python3 _src/build.py`, serve locally (`python3 -m http.server`), and check every page at 1366px and 390px wide, in all three languages: no horizontal scroll, all links and language switches resolve, no console errors.
