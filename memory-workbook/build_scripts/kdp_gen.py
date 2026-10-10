import re
desc = ("<p><b>Forgot why you walked into the room? Lost your keys again?</b></p>"
"<p>Everyday forgetfulness is common in midlife, and it is usually about attention, sleep, stress and overload. This workbook gives you a calm, practical way to work on it: <b>five minutes a day, for six weeks</b>.</p>"
"<p>Each week adds one tiny habit, tied to something you already do every day. You write your plan, track your progress and see for yourself what changes.</p>"
"<p><b>Inside you will find:</b></p>"
"<ul>"
"<li>A 6-week programme with one tiny habit per week: sleep wind-down, single-tasking, movement, recall practice and a simple way to tag names and places</li>"
"<li>A baseline self-check at the start and a final self-check at the end, so you can compare your own results</li>"
"<li>24 practice exercises, 42 daily log entries, weekly reviews and a 12-week tracker</li>"
"<li>If-then planners that tie each habit to your real routine</li>"
"<li>A memory slip log, a spaced recall planner and 40 more tiny habits to choose from</li>"
"<li>A plain-language page on when to talk to a doctor</li>"
"</ul>"
"<p><b>Who it is for:</b> busy adults, roughly 40 to 55, who want a more reliable everyday memory without memory palaces, gimmicks or guilt. It suits professionals, parents, and anyone noticing brain fog.</p>"
"<p><i>This is a practical habit workbook, not medical advice. If you are worried about your memory, please talk to your doctor.</i></p>")
kws = ["brain fog exercises for midlife women", "forgetfulness help for busy adults", "attention and focus routines", "sleep movement recall self-check journal",
       "names keys appointments forgetting guide", "perimenopause brain fog self help", "short routines for busy parents"]
assert all(len(k) <= 50 for k in kws)
t = "The 5-Minute Memory Workbook"; s = "Tiny Daily Habits for a Sharper, More Reliable Mind After 40"
md = f"""# Amazon KDP Data Sheet: The 5-Minute Memory Workbook

**Status:** paste-ready draft. Items marked **CHECK** could not be confirmed live inside KDP; the source of each figure is stated. Nothing here is an ISBN, ASIN or rank: none exists yet.

## Files To Upload (paperback)

| Item | File | Notes |
|---|---|---|
| Interior | `memory-workbook_interior_print.pdf` | 128 pages, US letter (8.5 x 11 in), fonts embedded, **no cover page** (KDP takes the cover as a separate file) |
| Cover | `cover_memory-workbook_wrap.pdf` | Back + spine + front, 17.54 x 11.25 in, built for 128 pages on white paper (spine 0.288 in) |
| Cover proof | `cover_memory-workbook_wrap_proof.png` | Trim, safe-margin, spine and barcode-zone overlay (internal use) |
| Ebook | **not ready** | `memory-workbook_ebook.pdf` is a PDF. KDP ebooks need EPUB, KPF or DOCX. See *Kindle Ebook* below. |

> **Cover resolution warning:** the accepted front and back art is 1,562 x 2,000 px, which is about **178 dpi** at wrap size (below 200 dpi). KDP may warn about it. Re-render both at 4K and rebuild the wrap before relying on it for print. **CHECK** KDP's cover upload validator.

## 1. Book Details

| Field | Entry |
|---|---|
| Language | English |
| Book title | {t} |
| Subtitle | {s} |
| Series | None |
| Edition number | Leave blank (first edition) |
| Author | First name: **Cimple** / Last name: **Books** (KDP requires two name fields; use this identical entry on every Cimple Books title). **CHECK** that KDP accepts the brand name. |
| Contributors | None |
| Publishing rights | I own the copyright and I hold necessary publishing rights |
| Sexually explicit content | No |
| Reading age | Leave blank / adult |
| Primary marketplace | Amazon.com |

**Title and subtitle match the cover:** the accepted front cover reads "The 5-Minute Memory Workbook" and "Tiny Daily Habits for a Sharper, More Reliable Mind After 40"; both were checked word for word against the cover image. (The cover lettering renders the hyphen in "5-Minute" as a long dash; keep the plain hyphen in KDP.)

## 2. Description (paste as HTML)

```html
{desc}
```

Character count (including tags): **{len(desc)}** (limit 4,000).

## 3. Keywords (7 phrases, 50 characters max each)

""" + "\n".join(f"{i+1}. {k} ({len(k)})" for i, k in enumerate(kws)) + f"""

None repeats words from the title or subtitle. Drawn from complaint and audience language in the earlier scouts and the Louda research (perimenopause brain fog, forgetfulness, busy parents). **CHECK** against Amazon autocomplete before finalising.

## 4. Categories (three browse paths)

Kindlescout's Kindle Ranker pages failed to load, so **no category thresholds were measured** for this product. Do not treat any figure below as known.

| # | Suggested path | Top-10 sales/day threshold |
|---|---|---|
| 1 | Books > Self-Help > Memory Improvement | **Not measured. CHECK** |
| 2 | Books > Health, Fitness & Dieting > Mental Health | **Not measured. CHECK** |
| 3 | Books > Self-Help > Personal Transformation | **Not measured. CHECK** |

Category names are from general knowledge of Amazon's structure and need confirming in the KDP category picker.

## 5. Format Settings

### Paperback (main product)

| Setting | Entry |
|---|---|
| ISBN | Use the free KDP ISBN (imprint shows as Amazon). **CHECK**: if you want "Cimple Books" as the publisher of record, buy your own ISBN. Do not invent one. |
| Print options | Black & white interior on **white paper** |
| Trim size | 8.5 x 11 in (21.59 x 27.94 cm) |
| Bleed | **No bleed** for the interior (no artwork runs to the page edge) |
| Cover finish | Matte (recommended; **CHECK** preference) |
| Printed page count | **128** (even) |
| Cover | Upload `cover_memory-workbook_wrap.pdf`; it includes the spine (0.2883 in at 128 pages, white paper, formula 0.002252 in per page) |
| Barcode | KDP adds it in the bottom-right corner of the back cover (the art keeps a plain zone there) |
| Expanded Distribution | **CHECK** eligibility for this trim and ink in KDP |
| Interior colour note | The interior uses green tints and header bands; on a black-and-white print these turn to greys. **CHECK** the KDP previewer. |

### Kindle ebook (not yet ready)

- **Format:** the interior is fillable and pages are fixed-layout, so a reflowable ebook is a poor fit. A fixed-layout KPF or EPUB would need to be produced (for example with Kindle Create); the PDF cannot be uploaded as the ebook file.
- **KDP Select:** recommended **out**, so the ebook can also go to Apple Books through an aggregator. **CHECK** the current Select terms.
- **DRM:** off (the product is a workbook meant to be used, not copied). **CHECK**.
- **Royalty plan and price band:** 70% requires a price from $2.99 to $12.99 ([KDP help, verified for this run](https://kdp.amazon.com/en_US/help/topic/G200634560)); the recommended $7.99 qualifies.

## 6. AI Content Declaration

| Question | Answer |
|---|---|
| Text | **Yes, AI-generated** (drafted with Claude, then structured and laid out by script). Disclose in KDP. |
| Images | **Yes, AI-generated**: front and back cover art (Nano Banana / Gemini). The interior has no AI images. |
| Translations | None |

([KDP content guidelines](https://kdp.amazon.com/en_US/help/topic/G200672390): AI-*generated* content must be disclosed.) **CHECK** the exact current wording in KDP.

## 7. Pricing And Territories

| Format | List price (USD) | Estimated royalty | Source |
|---|---|---|---|
| Paperback | **$16.99** | about **$7.02** per copy | 60% of list minus an *estimated* print cost of $1.00 + $0.017 x 128 pages = $3.18 (third-party estimate, **CHECK** in KDP's calculator) |
| Kindle ebook | **$7.99** | about **$5.59** before delivery fees | 70% of list; delivery fee depends on file size, **CHECK** |

Prices come from the Prica guide. Other Amazon marketplaces that matter for this buyer: **UK, Canada, Australia** (and Germany if you want European reach). Let KDP convert from USD first, then round to local price points. **CHECK** each marketplace's minimum and maximum.

**Payout:** the author is Nigeria-based. KDP pays Nigeria by wire transfer in NGN (confirmed 2026-09-23 on the KDP payments page; **CHECK** it is still current).

## 8. Back-Cover Blurb (already typeset on the wrap)

Headline: *Forgot Why You Walked Into the Room?* Blurb and five bullets as printed on `cover_memory-workbook_wrap.pdf`. The bullet "Daily logs, trackers and weekly reflection pages" and the other bullets match the finished interior (24 practice exercises, 42 daily log entries, a 12-week tracker, a doctor page).

## 9. Pre-Publish Checklist

- [ ] Re-render the cover art at 4K and rebuild the wrap
- [ ] Confirm print cost and royalty in KDP's calculator
- [ ] Confirm the three categories and add 7 keywords
- [ ] Have a qualified person fact-check the Sources page and the doctor page
- [ ] Order a KDP proof copy and check the greys and the spine
- [ ] Produce a fixed-layout ebook file before listing the Kindle edition
"""
open('/home/user/firstrepo/memory-workbook/amazon_kdp_metadata_memory-workbook.md', 'w').write(md)
print(len(desc), [len(k) for k in kws])
