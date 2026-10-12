#!/usr/bin/env python3
"""Prica pricing guide: computes every figure from the comparable table and writes markdown -> docx."""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
FX = 1365.0   # NGN per USD, approximation (CurrencyConvert quote dated 2026-07-29; other sources 1,360-1,376 and one outlier 1,645)
def ngn(usd): return f'₦{round(usd * FX / 50) * 50:,.0f}'
def u(v): return f'${v:,.2f}'
PRINT_FIXED, PRINT_PAGE, PAGES = 1.00, 0.017, 144   # KDP large trim, B&W, 110-828 pages (KDP printing-cost page)
PCOST = PRINT_FIXED + PRINT_PAGE * PAGES
def roy(price):
    rate = 0.60 if price >= 9.99 else 0.50
    return rate * price - PCOST
def kroy(price, delivery=0.15): return (0.7 * price - delivery) if 2.99 <= price <= 12.99 else 0.35 * price

comps = [  # platform, product, format, native price, signal
 ('Amazon (print)', 'How to Parent Children with ADHD (Laine)', 'Paperback', 16.48, 'BSR 5,335; est. $8,305/mo (third-party estimate)'),
 ('Amazon (print)', 'Angry Parent Angry Child (Khang)', 'Paperback', 17.95, 'BSR 17,143; est. $4,523/mo (third-party estimate)'),
 ('Amazon (print)', 'ADHD Parenting Guide for Boys (Bass)', 'Paperback', 17.22, 'BSR 19,919; est. $3,857/mo (third-party estimate)'),
 ('Amazon (print)', 'Helping Children with ADHD and ODD, CBT workbook (SpreadLife)', 'Paperback workbook', 14.91, 'BSR 26,184; est. $2,504/mo (third-party estimate)'),
 ('Amazon (print)', 'ADHD Parenting Guide for Boys (Giles)', 'Paperback', 12.99, 'BSR 35,189; est. $1,454/mo (third-party estimate)'),
 ('Amazon (print)', 'Understanding Girls with ADHD (Nadeau)', 'Paperback', 21.95, 'BSR 57,377; est. $614/mo (third-party estimate)'),
 ('Amazon (print)', 'CBT and DBT Workbook for Children with ADHD and Anger (SpreadLife)', 'Paperback workbook', 21.67, 'BSR 61,780; est. $606/mo (third-party estimate)'),
 ('Amazon (print)', 'Unlock Parenting Skills for ADHD Boys (Pisciotta)', 'Paperback', 17.99, 'BSR 87,666; est. $503/mo (third-party estimate)'),
 ('Amazon (print)', 'ADHD Success Workbook for Kids (Cargill)', 'Paperback workbook', 12.99, 'BSR 81,596; est. $363/mo (third-party estimate)'),
 ('Amazon (print)', 'Essential Guide to Parenting ADHD Children (Pratt)', 'Paperback', 9.99, 'BSR 66,621; est. $279/mo (third-party estimate)'),
 ('Amazon (print)', 'Thriving with ADHD Workbook for Kids (Miller)', 'Paperback workbook', 17.99, '315 Goodreads ratings (review count as proxy)'),
 ('Amazon (Kindle)', 'ADHD is Awesome (Holderness)', 'Ebook', 3.99, 'Kindle BSR 11,735; 1,138 reviews (third-party estimate and reported count)'),
 ('Amazon (Kindle)', 'Angry Parent Angry Child (Khang)', 'Ebook', 9.99, 'Kindle BSR 46,677 (third-party estimate)'),
 ('Amazon (Kindle)', 'ADHD Parenting Guide for Boys (Giles)', 'Ebook', 0.99, 'Kindle BSR 32,027; est. $138/mo (third-party estimate)'),
 ('Gumroad', 'ADHD parenting guide with five bonus worksheets', 'PDF ebook', 25.00, 'Listing only; no sales signal'),
 ('Gumroad', 'ADHD parenting guide for school and home', 'PDF', 9.00, 'Listing only; no sales signal'),
 ('Gumroad', 'Parenting guide plus daily planner bundle', 'PDF bundle', 30.00, 'Listing only; no sales signal'),
 ('Gumroad', 'Low-priced ADHD parent guides', 'PDF', 4.99, 'Some listings show 0 sales (reported on listing)'),
 ('Payhip', 'ADHD Parent Toolkit, 7 guides, printables, ages 6-12', 'PDF toolkit', 29.00, 'Listing only; no sales signal'),
 ('Payhip', 'ADHD parent survival guide (routines, behaviour tools)', 'PDF', 28.00, 'Listing only; no sales signal'),
 ('Etsy', 'ADHD parenting guides and printable toolkits (range low)', 'Printable PDF', 2.98, 'No bestseller badge visible; some listings unreviewed'),
 ('Etsy', 'Notion-style parenting workbook (range high)', 'Template', 24.99, 'No bestseller badge visible'),
 ('VitalSource', 'The ADHD Workbook for Parents (Parker)', 'eTextbook', 5.99, 'Listing only; not a sales signal'),
 ('Teachable', 'Interactive Parenting Children with ADHD (live Zoom cohort)', 'Course', 499.00, 'Listing price (Feb 2026 cohort); different product tier'),
 ('Teachable', 'Parenting program, start anytime', 'Course', 299.00, 'Listing price; different product tier'),
]
P_PRINT = 16.99; P_FLOOR = 14.99; P_CEIL = 17.99
P_K = 6.99; K_LO, K_HI = 4.99, 9.99
P_PDF = 12.00; PDF_LO, PDF_HI = 9.00, 19.00

md = []; A = md.append
A('---\ntitle: "Prica Pricing Guide: Raising a Superhero"\nsubtitle: "Cimple Books | Naira primary, USD noted"\n---\n')
A(f'**Date:** 2026-10-12. **Exchange rate used:** ₦{FX:,.0f} per US$1, an approximation. It comes from a [CurrencyConvert](https://currencyconvert.online/usd/ngn) quote dated 2026-07-29 (about three months old). Other sources I found ranged from ₦1,360 to ₦1,376, and one undated source showed ₦1,645. Re-check a live rate before publishing. All ₦ figures are rounded to the nearest ₦50.\n')
A('**Not financial advice.** This is a strategic estimate from observed listing evidence, not a guarantee of sales.\n')

A('# 1. Market and Product Derivation\n')
A('- **Format:** print-first paperback activity workbook (144 pages, 7 x 10 in, black-and-white interior) with a Kindle companion and a printable PDF.\n- **Target market:** English-speaking parents of children about 5 to 12 with ADHD, shopping on Amazon first (US, then UK, Canada, Australia). A Nigeria-direct channel is secondary.\n'
  '- **Value proposition:** forty simple activities plus a built-in parent-patience practice; non-medical.\n- **Production depth that affects price expectations:** 144 pages, 40 activities, a Patience Toolkit, Phrase Bank, 30-Day Tracker and Wins Log. The kid-workbook competitors run 96 to 184 pages.\n')

A('# 2 to 4. Comparable Shortlist, Trend Signal and Currency-Normalised Table\n')
A('Trend labels: **third-party estimate** = Kindle Ranker BSR and monthly-sales estimates; **proxy** = review or rating counts; **listing only** = a price seen on a listing with no sales evidence. None is a verified sales figure.\n')
A('| # | Platform | Product | Format | Native price (USD) | ₦ equivalent | Trend signal |\n|---|---|---|---|---|---|---|')
for i, (pl, pr, fm, p, sig) in enumerate(comps, 1):
    A(f'| {i} | {pl} | {pr} | {fm} | {u(p)} | {ngn(p)} | {sig} |')
A('\n**Platforms searched with no usable comparables:** Selar (no ADHD-parenting listing surfaced; Selar listings may exist but were not indexed), Podia and Stan Store (no results), Creative Market and Design Bundles (not searched; their buyers are designers, not parents).\n')

A('# 3. Price and Trend Clustering (print, Amazon)\n')
A('| Price band | Titles (BSR) | Reading |\n|---|---|---|\n'
  '| $16.48 to $17.99 | Laine (5,335), Khang (17,143), Bass (19,919), Pisciotta (87,666), Thriving workbook (no BSR) | Holds the top three ranks in the list. The cluster contains the strongest signals |\n'
  '| $12.99 to $14.91 | SpreadLife ODD (26,184), Giles (35,189), Cargill (81,596) | Mid-ranked; cheaper does not mean better-ranked |\n'
  '| $9.99 | Pratt (66,621) | Weak signal at the low end |\n'
  '| $21.67 to $21.95 | Nadeau (57,377), SpreadLife CBT/DBT (61,780) | Weaker signal at the high end; possible overpricing, though other factors (age, reviews) are mixed in |\n')
A('**Caution:** rank depends on reviews, ads and listing quality as well as price, so this shows where the best signals sit, not a price effect. On Kindle, the two $0.99 titles (Giles, Vooley) rank at 32,027 and 159,874, so a race to the bottom does not look rewarded.\n')

A('# 5. Pricing Recommendation\n')
A('## Paperback (lead product)\n')
A(f'- **Recommended price:** **{u(P_PRINT)} ({ngn(P_PRINT)})**.\n'
  f'- **Defensible range:** floor **{u(P_FLOOR)} ({ngn(P_FLOOR)})**, bounded by SpreadLife\'s ODD workbook at $14.91 (rank 26,184), the lowest price among the top-ranked workbook-style titles. Ceiling **{u(P_CEIL)} ({ngn(P_CEIL)})**, bounded by Pisciotta at $17.99, Khang at $17.95 and the Thriving workbook at $17.99. Avoid $19.99 and above, where the two $21.67 to $21.95 titles show weaker signals.\n'
  f'- **Positioning:** upper-middle of the strongest cluster ($16.48 to $17.99). Laine, the top title, is priced at $16.48; $16.99 matches the depth of a 144-page workbook with 40 activities against the 96 to 184-page workbook set.\n'
  f'- **Launch option (a judgment, not evidence):** list at {u(P_FLOOR)} for the first weeks to earn early reviews, then move to {u(P_PRINT)}. A new book has no review moat, and the top comparables have 250 to 500 reviews.\n')
A('### Margin check (KDP, from KDP\'s own printing-cost and royalty pages)\n')
A(f'7 x 10 in is KDP "Large" trim. Black ink, 144 pages: printing cost = $1.00 + $0.017 x 144 = **{u(PCOST)}**. Royalty is 60% of list price above $9.98 minus printing cost (50% at $9.98 or below). Expanded Distribution pays 40%. KDP did not show an effective date on these tables, so re-check in the dashboard.\n')
A('| List price | ₦ | Royalty (60%) | Royalty (Expanded Distribution, 40%) |\n|---|---|---|---|')
for p in (P_FLOOR, P_PRINT, P_CEIL):
    A(f'| {u(p)} | {ngn(p)} | {u(roy(p))} ({ngn(roy(p))}) | {u(0.4 * p - PCOST)} ({ngn(0.4 * p - PCOST)}) |')
A(f'\n**Colour interior is not viable at this price:** premium colour on Large trim would cost $1.00 + $0.08 x 144 = {u(1 + 0.08 * 144)} per copy, so choose black-and-white.\n')
A('## Kindle companion\n')
A(f'- **Recommended:** **{u(P_K)} ({ngn(P_K)})**; range {u(K_LO)} to {u(K_HI)} ({ngn(K_LO)} to {ngn(K_HI)}). All inside the verified 70% band of $2.99 to $12.99 (effective 7 July 2026).\n'
  f'- **Why:** the Kindle median in the ADHD and hyperactivity categories is $9.00 to $9.99 (third-party estimate), but a fill-in workbook has less value on a screen and a print edition will anchor the value. {u(K_HI)} is the ceiling; $0.99 deal pricing ranked poorly in the comparables.\n'
  f'- **Royalty:** about {u(kroy(P_K))} per sale at {u(P_K)} (70% minus an assumed $0.15 delivery cost; delivery cost is an assumption to check on KDP).\n')
A('## Printable PDF, direct sale\n')
A(f'- **Recommended:** **{u(P_PDF)} ({ngn(P_PDF)})**; range {u(PDF_LO)} to {u(PDF_HI)} ({ngn(PDF_LO)} to {ngn(PDF_HI)}).\n'
  '- **Bounds:** floor at the $9 Gumroad guide; ceiling below the $25 to $30 Gumroad bundles and $28 to $29 Payhip toolkits, which contain more separate files than a single workbook. Etsy listings span $2.98 to $24.99.\n'
  '- **Evidence limit:** none of these listings showed sales, so this price rests on listing positions only. No Selar comparable was found, so I cannot support a naira-denominated price for Nigerian buyers from evidence. If you sell locally, check Selar listings first and consider a lower naira price point as a test.\n')
A('## Platform notes and risk flags\n')
A('- **Single global price or differentiated?** Amazon and Gumroad/Payhip are USD-denominated; keep one USD price per product. A separate naira price on a local platform should be tested, not assumed.\n'
  '- **Risk flags:** (1) exchange rate: approximation, with sources ranging widely; (2) rank signals are estimates; (3) thin direct-sales evidence (no sales counts); (4) the top titles have large review counts that a new book lacks; (5) KDP printing and royalty tables had no effective date shown; (6) the Teachable programs ($299 to $499) are a different product tier and are not used to set the workbook price.\n')

A('# 6. Platform Recommendation (ranked)\n')
A('| Rank | Platform | Why here | Why not instead | Fees and payout |\n|---|---|---|---|---|\n'
  '| 1 | **Amazon KDP (paperback, then Kindle)** | Strongest evidence: every top-ranked comparable is here; buyers are the target market; native print-on-demand for a fill-in workbook | Direct sales would lack the search traffic these titles show | Royalty from KDP pages (60% minus printing cost; 70% Kindle in the band); Nigeria is paid by wire transfer in NGN (verified 2026-10-11) |\n'
  '| 2 | **Gumroad or Payhip (printable PDF)** | Both host comparable parent guides and toolkits at $9 to $30; good for social traffic from Reels | No visible sales signal; discovery depends on your own audience | Fee rates not verified in this run |\n'
  '| 3 | **Etsy (printable download)** | Many parent printables and toolkits sit here | Price pressure ($2.98 and up) and no bestseller signal; seven-page toolkits dilute a 144-page workbook | Fee rates not verified in this run |\n'
  '| 4 | **Apple Books (via an aggregator, ebook only)** | Reaches iPad readers | Thin demand: the top ADHD parent title has 90 ratings, and no ADHD chart presence; Nigeria has no paid storefront | Not verified in this run |\n')
A('**Ruled out or unranked:** Teachable (courses are a different product; $299 to $499 tiers), Podia and Stan Store (no comparables found, so not ranked), Selar (no comparables found, not ranked; it may still suit a Nigeria-direct test), Creative Market and Design Bundles (audience mismatch and not researched).\n')
A('# Sources\n')
A('[Kindle Ranker categories](https://www.kindleranker.com/book_categories/11441/US/books+parenting+&+relationships+special+needs+hyperactivity) | [KDP printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340) | [KDP paperback royalty](https://kdp.amazon.com/en_US/help/topic/G201834330) | [KDP eBook royalty band](https://kdp.amazon.com/en_US/help/topic/G200634560) | [KDP payment methods](https://kdp.amazon.com/en_US/help/topic/GJD7DFFX6X88AK46) | [Gumroad listing](https://adhdparentinghelp.gumroad.com/l/cpg) | [Payhip listing](https://payhip.com/b/LXD37) | [Teachable programs](https://adhd-support-australia.teachable.com/) | [CurrencyConvert](https://currencyconvert.online/usd/ngn)\n')
open(os.path.join(HERE, 'prica_raising-a-superhero.md'), 'w').write('\n'.join(md))
subprocess.run(['pandoc', os.path.join(HERE, 'prica_raising-a-superhero.md'), '-o', os.path.join(HERE, 'prica_raising-a-superhero.docx')], check=True)
print('print cost', PCOST, 'royalties', {p: round(roy(p), 2) for p in (P_FLOOR, P_PRINT, P_CEIL)}, 'kindle', round(kroy(P_K), 2))
