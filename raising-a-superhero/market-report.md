# Raising a Superhero: Kindle + Apple Books Market Report

Concept: a non-medical workbook for parents raising kids with ADHD. It helps them turn the child's traits into real-world strengths and builds the parent's patience.
Snapshot: 2026-10-11 (one snapshot only, so no rank velocity)
Companion data: `raising-a-superhero-market-scout.xlsx` (same folder)

Labels used throughout: **REPORTED** = read from a source. **EST** = calculated by me. **INFERRED** = my judgement.

---

## 1. Bottom line

1. **Build this print-first.** The same indie ADHD-parenting titles rank far higher in print than on Kindle. The Kindle "Hyperactivity" #1 sells about 7 copies a day. The print #1 sells about 15 a day, and the top print title (BSR 5,335) is estimated at about $8,300 a month. (REPORTED, third-party estimates.)
2. **Apple Books is a footnote for this niche.** No ADHD or kids title appears in Apple's Health, Mind & Body top-40 paid chart. The most-rated ADHD-parent title I found has 90 ratings. Treat Apple as a later "wide" release.
3. **The pain points are consistent and fixable.** Across the titles I read: "not actionable", repetitive, too wordy for the child, generic, suspected AI writing, and sloppy editing.
4. **Recommended length: about 160 interior pages in print.** The ebook edition should be about 110-140 reading pages, with worksheets as a printable PDF bundle.
5. **Graphics should reduce reading load, not decorate it.** Short text blocks, a consistent hero mascot, trackers, checklists and mission boards. Evidence on competitor interiors is thin (see section 7), so this is mostly INFERRED from the complaints.
6. **Opportunity score: 62/100, Tier B (validate).** It cannot be Tier A with a single snapshot. Re-run weekly.

---

## 2. Method and confidence

**Access mode: Fallback (no browser).** I could not open Amazon Best Sellers or Amazon reviews. What I used:

| Source | What it gave | Status |
|---|---|---|
| Kindle Ranker category pages (downloaded directly) | Top-15 per category, BSR, price, review count, estimated monthly $, category averages | Worked. Third-party; capture date unknown |
| Apple iTunes Search API (US) | Title, price, average rating, ratings count, release date for ADHD ebooks | Worked (intermittent; retried) |
| Apple chart pages (Health, Mind & Body top-paid and top-free) | 40 rows each, fully captured | Worked |
| PopVortex Self-Help ebooks | 35 rows (page truncated after #35) | Worked, partial |
| Goodreads book pages | Page counts, ratings, critical review text | Worked. Star rating per review is not shown |
| KDP help pages | Royalty band, AI rule, payment method | Worked |

**Not achieved:** the overall Kindle Store top 100, Amazon critical reviews, Reddit threads, and any trend series. Overall confidence is **Medium-low**.

---

## 3. Market size signals (Kindle Ranker, REPORTED)

| Category | #1 sales/day | #50 sales/day | Median price | Avg pages | Median monthly $ (top 30) |
|---|---|---|---|---|---|
| Kindle > ADHD | 106 | 1 | $9.00 | 215 | $504 |
| Kindle > Parenting > Special Needs > Hyperactivity | 7 | 1 | $9.99 | 211 | $559 |
| Print > Parenting > Special Needs > Hyperactivity | 15 | 1 | $15.47 | 176 | $433 |
| Kindle > Parenting > Child Care | 1 | 0 | $6.12 | 203 | $171 |
| Kindle > Counseling > Children | 1 | 0 | $5.05 | 116 | $0 |

How to read it:
- The Kindle ADHD "106 a day" is **misleading**. The #1 there is *How to Keep House While Drowning* (KC Davis), an adult cleaning title. Strip it out and the category is small.
- Kindle Ranker lists the ADHD category as 95% volatile, with 30% indie success and 33% KDP Select. The niche is winnable, but a single rank reading will mislead. (REPORTED.)
- Cross-check of Kindle Ranker's monthly $ against my own BSR-based estimate for five Kindle titles: four agreed within about 15% (ADHD is Awesome $1,351 vs $1,228; ADHD 2.0 $1,438 vs $1,678; Angry Parent Angry Child $880 vs $839; Taking Charge of ADHD $419 vs $368). One was off by 2x (Giles Parenting Guide for Boys, $65 vs $138). So the figures are usable as a range, not as precise sales.

---

## 4. Kindle / Amazon top 20 competitors

Selection: parent- or child-focused ADHD titles drawn from the three most relevant Kindle Ranker lists plus the best-known kid workbooks. BSR is as reported by Kindle Ranker (print BSR for print rows, Kindle BSR for Kindle rows). Monthly $ is Kindle Ranker's estimate.

| # | Format | Title (author) | BSR | Price | Reviews | Est $/mo | Pages | GR avg |
|---|---|---|---|---|---|---|---|---|
| 1 | Print | How to Parent Children with ADHD (Laine) | 5,335 | $16.48 | 385 | $8,305 | 142 | 3.73 |
| 2 | Print | Angry Parent Angry Child (Khang) | 17,143 | $17.95 | 503 | $4,523 | n/a | n/a |
| 3 | Print | ADHD Parenting Guide for Boys (Bass) | 19,919 | $17.22 | 243 | $3,857 | 220 | 3.83 |
| 4 | Print | Helping Children with ADHD and ODD: CBT Workbook (SpreadLife) | 26,184 | $14.91 | 122 | $2,504 | n/a | n/a |
| 5 | Print | ADHD Parenting Guide for Boys (Giles) | 35,189 | $12.99 | 83 | $1,454 | n/a | n/a |
| 6 | Print | Understanding Girls with ADHD (Nadeau) | 57,377 | $21.95 | 424 | $614 | n/a | n/a |
| 7 | Print | CBT & DBT Workbook for Children with ADHD & Anger (SpreadLife) | 61,780 | $21.67 | 116 | $606 | n/a | n/a |
| 8 | Print | Parenting Girls with ADHD (Reed) | 62,333 | $12.69 | 31 | $355 | n/a | n/a |
| 9 | Print | Transforming Oppositional Defiant Disorder (Greene) | 65,423 | $9.99 | 18 | $279 | n/a | n/a |
| 10 | Print | Essential Guide to Parenting ADHD Children (Pratt) | 66,621 | $9.99 | 140 | $279 | n/a | n/a |
| 11 | Print | ADHD Success Workbook for Kids (Cargill) | 81,596 | $12.99 | 54 | $363 | n/a | n/a |
| 12 | Print | Unlock Parenting Skills for ADHD Boys (Pisciotta) | 87,666 | $17.99 | 54 | $503 | n/a | n/a |
| 13 | Kindle | ADHD is Awesome (Holderness) | 11,735 | $3.99 | 1,138 | $1,228 | 320 (Apple) | n/a |
| 14 | Kindle | ADHD 2.0 (Hallowell) | 28,552 | $9.99 | 3,094 | $1,678 | n/a | n/a |
| 15 | Kindle | Taking Charge of ADHD (Barkley) | 60,885 | $13.17 | 913 | $368 | n/a | n/a |
| 16 | Workbook | Thriving with ADHD Workbook for Kids (Miller) | n/a | $17.99 | 315 ratings (GR) | n/a | 148 | 4.26 |
| 17 | Workbook | The ADHD Workbook for Kids (Shapiro) | n/a | n/a | 159 ratings (GR) | n/a | 184 | 4.01 |
| 18 | Workbook | Learning to Slow Down & Pay Attention (Nadeau) | n/a | n/a | 225 ratings (GR) | n/a | 96 | 3.95 |
| 19 | Kindle | ADHD Raising an Explosive Child (Brain) | n/a | n/a | 62 ratings (GR) | n/a | 257 | 3.26 |
| 20 | Kindle | ADHD Raising an Explosive Child (Payne) | n/a | n/a | 30 ratings (GR) | n/a | 150 | 2.60 |

Also tracked but outside the top 20: *Parenting Superkids with ADHD* (Waldren, 237 pp, $4.99 ebook, NetGalley listing) and *Parenting Children with ADHD Unlocked* (Kindle BSR 159,874, $0.99, 11 reviews).

What the Kindle/Amazon data says:
- **Indie print titles beat traditional publishers** in the parent-guide slot. All twelve print rows are indie or small press.
- **Anger and patience is a proven sub-theme.** *Angry Parent Angry Child* is #2 in print at an estimated $4,523 a month and also appears on the Kindle list. Our "parent patience" angle sits on demonstrated demand.
- **Activity books sell inside this category.** *Kids' Ultimate Maze Book* (70 mazes) sat at print BSR 42,413 with an estimated $671 a month. It's a signal that kid activity content moves here.
- **Translation works.** A Spanish edition of *Angry Parent Angry Child* sits at print BSR 56,959 with an estimated $837 a month.
- **Two-gender splitting is normal.** Separate "Boys" and "Girls" titles both rank.
- **Titles are long and keyword-heavy.** Kindle Ranker reports a median title-plus-subtitle length of 14 words in the ADHD category.

---

## 5. Apple Books top 20 competitors

Apple does not publish ADHD or kids-parenting charts. This list is the 20 most-rated parent- or child-relevant ADHD ebooks I could find through Apple's search API (US storefront, REPORTED). Apple shows only ratings, so ratings count is the best demand proxy.

| # | Title | Price | Avg rating | Ratings | Released |
|---|---|---|---|---|---|
| 1 | ADHD 2.0 (Hallowell) | $9.99 | 4.5 | 90 | 2021 |
| 2 | How to ADHD (McCabe) | $13.99 | 5.0 | 25 | 2024 |
| 3 | ADHD is Awesome (Holderness) | $19.99 | 4.5 | 20 | 2024 |
| 4 | The Gift of ADHD | $13.99 | 2.0 | 17 | 2010 |
| 5 | ADHD Parenting (Forris) | $9.99 | 2.5 | 12 | 2011 |
| 6 | Parenting Kids With ADD/ADHD (Winebarger) | $14.99 | 2.0 | 12 | 2011 |
| 7 | Helping Kids with ADD/ADHD Make Friends | $10.99 | 2.0 | 12 | 2011 |
| 8 | The ADHD Fix | $3.99 | 2.0 | 11 | 2013 |
| 9 | Parenting ADD/ADHD Children (Miles) | $3.99 | 3.5 | 10 | 2013 |
| 10 | The ADHD Workbook for Teens | $12.99 | 1.5 | 10 | 2011 |
| 11 | Gordy the Rabbit has ADHD | Free | 4.0 | 10 | 2015 |
| 12 | What Your ADHD Child Wishes You Knew (Saline) | $1.99 | 3.5 | 9 | 2018 |
| 13 | Parenting Your Child With ADHD (Wiener) | $10.99 | 2.5 | 9 | 2012 |
| 14 | The ADD/ADHD Checklist | $12.99 | 1.5 | 9 | 2008 |
| 15 | Making the System Work for Your Child with ADHD | $17.99 | 2.5 | 9 | 2004 |
| 16 | Empowering Youth with ADHD | $19.99 | 1.5 | 8 | 2010 |
| 17 | How to Help Your Child With ADHD | $13.99 | 1.5 | 7 | 2012 |
| 18 | The ADHD Advantage (Archer) | $7.99 | 4.0 | 7 | 2015 |
| 19 | Coping with ADHD | $2.99 | 1.5 | 7 | 2012 |
| 20 | The ADHD Workbook for Parents (Parker) | $23.99 | 1.0 | 6 | 2006 |

Further Apple facts:
- The only ADHD-titled entry in Health, Mind & Body top-free is *Adult ADHD Starter Guide* at #40. Top-paid (40 rows) has none. (REPORTED.)
- The PopVortex Self-Help list (35 rows read) has no ADHD title.
- *What Your ADHD Child Wishes You Knew* is on Apple at $1.99, 272 pages, 3.6 average from 9 ratings (page read directly).
- *ADHD is Awesome* is $19.99 on Apple at 320 pages, versus $3.99 on Kindle at the time of the Kindle Ranker capture. Cross-store price gaps are common here.
- Several 2026 releases (Mercer, Dunstan, Power) have no ratings yet. I cannot judge their quality from the data I have.
- **Rating quality is poor.** Of the 20, 13 average 2.5 or below. The category is stale and low-rated on Apple, which is an opening only if Apple shoppers exist, and the ratings counts suggest few do.
- **Nigeria note:** Apple's availability page showed no paid Apple Books storefront in Africa when last checked (2026-09-23). Publish through an aggregator (Draft2Digital, PublishDrive) if you want Apple at all. I did not re-check this on 2026-10-11.

---

## 6. Pain points from similar books

Quotes below were re-checked against the live Goodreads pages on 2026-10-11 and match word for word. Goodreads pages did not show a star rating per review, so I cannot say each was 1-3 stars; the overall ratings are given with each title.

| Theme | Evidence | Title (pages, GR avg) |
|---|---|---|
| **Not actionable** | "There are very few actionable strategies or fresh ideas that would actually support a parent dealing with the day-to-day realities of raising a child with ADHD." (Steph B, 2025-07-21) | Parenting ADHD guide, Bass (220 pp, 3.83) |
| **Not actionable** | "This book will not help your adhd child overcome the things they struggle with but just make you both frustrated" (Erika Smith, 2023-10-27) | ADHD Workbook for Kids, Shapiro (184 pp, 4.01) |
| **Generic** | "It's nothing you can't find in a free Google search and save yourself the money and time in reading it." (Kelly O'Banner, 2023-10-12) | Supporting a Hyperactive Child, Payne (152 pp Kindle, 2.60) |
| **Trust: suspected AI** | "Complete garbage. Sounds like a book written by AI fed only the Wikipedia page on ADHD." (Jac, 2023-11-16) | Raising an Explosive Child, Brain (257 pp, 3.26) |
| **Editing quality** | "Honestly, there are so many grammatical errors in this book it feels like a rough draft." (Mikelle, 2020-12-02) | same |
| **Repetitive** | "I had a difficult time with the repetition of prefacing everything that was going to be shared." (Shannon, 2026-01-16) | How to Parent Children with ADHD, Laine (142 pp, 3.73) |
| **Too wordy for the child** | "This book is a bit too wordy for a source that's supposed to help young children struggling with ADHD." (Casseroll, 2026-04-25) | Thriving with ADHD Workbook for Kids (148 pp, 4.26) |
| **Too wordy for the child** | "my poor little ADHD child could not focus on performing any of the tasks due to all the extra reading involved." (Aimee, 2023-03-11) | same |
| **Wrong voice** | "Writing them TO a child with ADHD instead of their parents seems off the mark" (Sarah Stevens) | Learning to Slow Down & Pay Attention (96 pp, 3.95) |
| **Age fit** | "many of the things didn't really apply to my kindergartener" (Elizabeth) | same |
| **Oversimplified** | "oversimplifies the complexities of the diagnosis" (Castspells) | same |

Notes on these quotes:
- The last three Nadeau rows are from the earlier fetch and were not in the five-quote re-check. They are as reported by the page summary. Re-open them before using them in marketing.
- A Goodreads status update quoted in search results said one ADHD parenting guide "was largely written by AI" (January 2026). I did not open that page, so I have not used the wording as a quote.
- Praise themes seen: "activities include writing work and worksheets" (Stacy, on Shapiro) and a parent who completes the Thriving workbook activities together in the evening (Indigo listing, single review).
- Parent mental load is real but I found no ADHD-specific figure for yelling or patience. Studies I found show high stress and depression in parent samples (Saudi Arabia, 151 parents: about 36% moderate-to-severe depression; Indonesia, 65 respondents). A CHADD summary cites 66% parental burnout, but I could not confirm that sample was ADHD-specific. Do not quote any of these as ADHD-specific market statistics.

**What this means:** buyers want something they can do tonight. They punish padding, repeated framing, AI-sounding generic text, and anything that makes the child read a lot.

---

## 7. Page count recommendation

| Evidence | Pages |
|---|---|
| Kindle ADHD category average | 215 |
| Kindle Hyperactivity average | 211 |
| Print Hyperactivity average | 176 |
| Top-selling indie print title (Laine) | 142 |
| Kid workbooks: Nadeau / Thriving / Shapiro | 96 / 148 / 184 |
| Worst-rated parent guides (Brain, Payne) | 257 / 150-152 |

**Recommendation (INFERRED from the above):**
- **Print workbook: about 160 interior pages** (range 144-176). It sits at the print average, above the best-selling indie title, and matches the best-rated workbooks (148-184).
- **Do not pad to the 211-215 Kindle averages.** Those are for narrative books. The top-rated workbooks are shorter, and the "repetitive" and "too wordy" complaints appear on the longer titles.
- **Ebook edition: about 110-140 reading pages**, with worksheets delivered as a printable PDF bundle. Interactive pages work poorly on e-readers. This is my judgement; I did not find a source on ebook worksheet complaints in this run.
- **Words per page:** keep child-facing pages light (my target is under 80 words), and put the longer explanations in the parent sections. This directly answers the "too wordy" reviews.

Suggested split (starting point only): about 55-60 parent pages (understanding, patience practice, scripts), about 90 child/shared activity pages, and about 10 pages of front and back matter and trackers.

---

## 8. Graphics content

**What I could confirm about competitor interiors (thin):**
- *Learning to Slow Down & Pay Attention* is illustrated (illustrator credited on Goodreads) and is a 96-page workbook.
- ADDitude's review of that book describes "plenty of activity pages" and "checklists to help young readers identify the problems they'd like to solve" for ages 9-12.
- *Thriving with ADHD Workbook for Kids* includes a homework chart and a morning routine lesson per its publisher listing. Its interior illustration is not described in anything I found.
- *The Mini ADHD Coach: A Visual Guide* exists in the Kindle list (BSR 51,182, $1.99), but I did not see its interior.
- A maze book ranks in the print Hyperactivity list.

Nobody I found complained about illustrations. The complaints are about **reading load**. So graphics should be functional.

**Recommended graphic system (INFERRED):**
1. **One recurring hero mascot or sidekick** who "talks" to the child so the parent text can stay adult. This fixes the "wrong voice" complaint (a book written to the child that the parent has to read).
2. **Parent-side "origin story" pages**: one-glance summaries of a trait with a "superpower / kryptonite / sidekick tool" layout. Avoid clinical diagrams.
3. **Mission boards and trackers**: weekly routine tracker, calm-down plan, reward chart, homework mission card. Large tick boxes, minimal writing.
4. **Visual schedules and icon-based checklists** the child can follow without reading.
5. **Short activity formats** that cost little reading: mazes, matching, draw-it boxes, circle-the-feeling faces.
6. **Parent patience tools in the same visual language**: a "pause" card, a 3-step script card, a reset tracker. Make these pull-out pages.
7. **Large type, generous white space, a restrained palette.** Fewer elements per page suits both ADHD readers and tired parents.
8. **Black-and-white interior with a colour cover**, to protect margins. Check KDP's current print cost for colour before deciding.
9. **Do not use Marvel/DC or other recognisable characters or costumes.** Create original characters.

**KDP rule that affects graphics (REPORTED, verified 2026-10-11):** AI-generated text or images, including cover and interior images, must be disclosed to KDP even after substantial edits. AI-assisted work you created yourself does not need disclosure.

---

## 9. Other observations that give us an edge

1. **The dual-audience workbook is the open lane.** Existing books are either parent guides (long, text-heavy) or kid workbooks (the parent has to coach). A single book with a parent track and a child track, in two voices, is rare in what I saw.
2. **"Superpower" framing exists, but weakly.** Found: *Parenting Superkids with ADHD* (237 pp, $4.99 ebook), *ADHD Is Our Superpower* (children's book, ages 8-12, with a parents section), *ADHD is Awesome* (Kindle BSR 11,735, 1,138 reviews). I found no book titled exactly "Raising a Superhero" in one search. That is not exhaustive. Run a KDP title search and a trademark check before locking the name.
3. **Patience is a proven sub-theme** (*Angry Parent Angry Child* at #2 in print). Few ADHD books make parent self-regulation a first-class section.
4. **Trust is a differentiator.** Use a real, named author voice, no claims you cannot back, and a plain "non-medical" notice. KDP's page I read has no specific medical-claims rule, but it forbids content "meant to mislead customers". Avoid "treat", "cure", "reduce symptoms" language entirely.
5. **Editing quality.** Several top indie titles are criticised for repetition and typos. A human edit and a no-repetition rule is a real, cheap edge.
6. **Series room.** Boys, Girls, Teens and Spanish editions each have a ranked precedent. Plan a core workbook, then a "kid mission book" spin-off.
7. **Back-to-school timing.** I have no seasonality data. Build a launch plan and test it against the August-September window, but treat this as an assumption.
8. **Price points.** Competing indie prints: $9.99-$21.95, with the best sellers at $16.48-$17.95. Plan print at $14.99-$17.99. For Kindle, the 70% royalty band is now **$2.99-$12.99** (effective 7 Jul 2026, verified on KDP); I'd price in the $6.99-$9.99 range, close to the category median of $9.00-$9.99.
9. **Payment (Nigeria):** KDP pays Nigeria by wire transfer in NGN, with no direct deposit or cheque (verified 2026-10-11).

---

## 10. Opportunity score and stress test

| Factor | Weight | Score | Basis |
|---|---|---|---|
| Demand | 25 | 6 | Indie print BSR 5.3k-20k; Kindle Hyperactivity #1 only about 7/day |
| Cross-platform | 10 | 4 | Apple is thin; no ADHD chart presence |
| Complaint gap | 20 | 7 | Same complaints on 6+ titles |
| Competition (10 = least) | 15 | 6 | Indie-friendly, but many cloned "Parenting Guide" titles |
| Trend | 10 | 5 | No trend series captured; neutral |
| Format fit | 10 | 8 | Print workbook is native; ebook-only would score about 4 |
| Price and royalty | 10 | 7 | Print $14-$22 is normal |
| **Weighted** | | **62 / 100** | **Tier B** (recomputed independently; matches the workbook) |

**Case against (stress test):**
- **Small ceiling.** Kindle Hyperactivity #1 sells about 7 a day, and the #50 title sells about 1 a day. This is a modest-volume niche, even in print.
- **Cloned competition.** Near-identical "Parenting Guide for Boys" titles from several indie publishers suggest sales depend on keywords and ads. We would need ads or an audience to climb.
- **AI-slop saturation** cuts both ways: it makes quality a differentiator, but it also means buyers are wary and reviews are the moat.
- **Review moat.** The top print titles have 250-500 reviews. Early on we will not.
- **Apple adds little.** It may not justify extra effort at launch.
- **Health claims.** Even "non-medical" books attract scrutiny. Keep language to skills, routines and attitudes.
- **Single snapshot.** Everything here is one reading; volatility is reported at 95% for the ADHD category.

---

## 11. Hand-off briefs

**booka (build):** Print-first 160-page workbook, 8.5x11 or similar workbook trim (confirm), two tracks (parent and child), 8 modules, an original hero mascot, no medical claims, human-edited, no repeated framing, child pages under about 80 words.

**prica (price):** Print $14.99-$17.99; Kindle $6.99-$9.99 within the $2.99-$12.99 band; printable PDF bundle as an add-on if sold direct.

**louda (marketing):** Lead with "tonight-ready" and "calm parent, confident kid". Use parent-burnout empathy without citing unverified statistics. Back-to-school hook (unverified seasonality).

**coverforge:** Original illustrated hero character for the child, warm adult-friendly palette, readable at thumbnail size. Avoid recognisable superhero IP. Disclose any AI-generated artwork to KDP.

---

## 12. Caveats and next steps

- Single snapshot, fallback access mode, third-party estimates. Run weekly to get rank velocity before treating anything as Tier A.
- Re-open the three Nadeau quotes and the Kimola/ADDitude pages before marketing use. The Kimola report URL returned HTTP 410, so I did not use it. ADDitude's "Amazon is flooded" line from a search snippet was **not found** on the page I opened, so I left it out.
- To upgrade confidence: capture Amazon Best Sellers and critical reviews through a browser, add Reddit threads (r/ADHD_Parenting, r/ADHD), and get a second snapshot.

## Sources

- Kindle Ranker: [ADHD](https://www.kindleranker.com/kindle_categories/11717478011/US/kindle+ebooks+health,+fitness+&+dieting+counseling+psychology+pathologies+attention-deficit+disorder), [Hyperactivity (print)](https://www.kindleranker.com/book_categories/11441/US/books+parenting+&+relationships+special+needs+hyperactivity), [Hyperactivity (Kindle)](https://www.kindleranker.com/kindle_categories/157625011/US/kindle+ebooks+parenting+hyperactivity), [Child Care](https://www.kindleranker.com/kindle_categories/157613011/US/kindle+ebooks+parenting+&+relationships+child+care), [Counseling Children](https://www.kindleranker.com/kindle_categories/156521011/US/kindle+ebooks+health,+fitness+&+dieting+counseling+psychology+children)
- Apple: [Health, Mind & Body top-paid](https://books.apple.com/us/charts/health-mind-body/9025/top-paid), [top-free](https://books.apple.com/us/charts/health-mind-body/9025/top-free), [ADHD is Awesome](https://books.apple.com/us/book/adhd-is-awesome/id6451078144), [What Your ADHD Child Wishes You Knew](https://books.apple.com/us/book/what-your-adhd-child-wishes-you-knew/id1312463438), [PopVortex Self-Help](https://www.popvortex.com/books/charts/self-help-ebooks.php), iTunes Search API (US, ebook entity)
- Goodreads: [Shapiro](https://www.goodreads.com/book/show/8303577), [Bass](https://www.goodreads.com/book/show/60285810), [Brain](https://www.goodreads.com/book/show/54882468), [Payne (Explosive Child)](https://www.goodreads.com/book/show/63065497), [Payne (Hyperactive Child)](https://www.goodreads.com/book/show/61855442), [Laine](https://www.goodreads.com/book/show/208598332), [Thriving workbook](https://www.goodreads.com/book/show/170356371), [Nadeau](https://www.goodreads.com/book/show/582045)
- Other: [NetGalley, Parenting Superkids with ADHD](https://www.netgalley.com/catalog/book/524325), [ADDitude on Nadeau](https://www.additudemag.com/learning-to-slow-down-and-pay-attention/), [Porchlight listing for Thriving workbook](https://www.porchlightbooks.com/products/thriving-with-adhd-workbook-for-kids-kelli-miller-9781641520416), [CHADD on parental burnout](https://chadd.org/adhd-weekly/irritable-and-overwhelmed-signs-of-parental-burnout/)
- KDP help: [royalty bands](https://kdp.amazon.com/en_US/help/topic/G200634560), [AI content](https://kdp.amazon.com/en_US/help/topic/G200672390), [payment methods](https://kdp.amazon.com/en_US/help/topic/GJD7DFFX6X88AK46)
