FX = 1365.0
def n(usd): return '₦{:,.0f}'.format(round(usd*FX/100)*100)
def roy(price, pages=128, fixed=1.00, pp=0.017): 
    cost = fixed + pp*pages; return cost, 0.6*price - cost
rows = [
 ('Payhip', 'Brain Fog Reset workbook', 'Printable PDF', '£6.99', 6.99*1.30, 'None visible (listing only)', 'Close: weekly reflection + habit tracker'),
 ('Payhip', 'Brain Fog Breaker Reset', 'Printable PDF', '$7', 7.0, 'None visible', 'Close: brain dump + sorting pages'),
 ('Payhip', 'Focus + Brain Clarity Bundle', '5-guide bundle PDF', '$20', 20.0, 'None visible', 'Close: aimed at adults 40+'),
 ('Gumroad', 'The Clarity Code', 'Printable PDF workbook', '$24.99', 24.99, 'No ratings shown', 'Close: daily clarity trackers'),
 ('Gumroad', 'The Mind Reset Guide', 'PDF guide', '€14.99', 14.99*1.15, '5 ratings (thin, proxy)', 'Partial: morning reset routine'),
 ('Gumroad', 'Reset To Rise Workbook', '75-page PDF', 'CAD 12.99', 12.99*0.73, 'None visible', 'Partial: habit, focus, gratitude trackers'),
 ('Etsy', 'Executive Dysfunction Workbook', '71-page printable', 'n/a (not in results)', None, 'No bestseller badge confirmed', 'Partial: habit grid, working-memory pages'),
 ('Etsy', 'HashimotoTracker', 'Fillable PDF tracker', 'n/a', None, 'None visible', 'Weak: condition-specific'),
 ('Selar', 'Unlock Your Productivity (Nigerian Girl&rsquo;s Guide)', 'Ebook', '$14.75', 14.75, '0 ratings shown', 'Weak: Nigerian audience, habits angle'),
 ('Selar', 'Nigeria Survival Kit', 'Ebook', '$9 (was $19)', 9.0, '0 ratings shown', 'Weak: finance topic'),
 ('Selar', 'Still Broke After Every Course? The Nigerian Hustle Reset', 'Ebook', '₦9,900', 9900/FX, 'None visible', 'Weak: finance topic'),
 ('Retail (ThriftBooks)', 'The Memory Workbook (Mason &amp; Kohn, New Harbinger, 2001)', 'Paperback, 225 pp', '$29.95 list', 29.95, '5 ratings shown (thin)', 'Strong: memory exercises, much older and denser'),
 ('Retail (eBay, new)', 'Keep Your Brain Alive (Workman, 2014)', 'Paperback, 204 pp', '$11.17 marketplace', 11.17, 'None', 'Partial: brain exercises, not a habit workbook'),
]
out = []
a = out.append
a("# Prica Pricing Guide: The 5-Minute Memory Workbook\n")
a("**Product:** *The 5-Minute Memory Workbook: Tiny Daily Habits for a Sharper, More Reliable Mind After 40* (Cimple Books).\n")
a("**Exchange rate used:** **about ₦1,365 per US$1**. The most recent *dated* figure found was ~₦1,365 on 29 July 2026 ([CurrencyConvert](https://currencyconvert.online/usd/ngn)), with undated live quotes of ₦1,360-₦1,376. No October 2026 rate was found, so this is an approximation. Re-check before listing; ₦ values are rounded to the nearest ₦100. Non-USD comparable prices use assumed approximate rates (£1 = $1.30, €1 = $1.15, CA$1 = $0.73), **assumptions, not sourced rates**.\n")
a("## 1. Market And Product Derivation\n")
a("- **Category and format:** self-help habit workbook. Main product: **128-page US-letter paperback** (fillable pages: self-checks, daily logs, trackers). Companion: an **85-page ebook/PDF edition** (leaner).\n"
  "- **Target market:** English-speaking adults 38-55 in the US, UK, Canada and Australia who are worried about everyday forgetfulness; a female skew from the perimenopause and brain-fog conversation. Buyers are in USD/GBP/CAD/AUD storefronts, not Nigeria.\n"
  "- **Value proposition:** *five minutes a day, six weeks, a baseline and final self-check, no gimmicks.* Substance is real: 128 pages, six weekly modules, 24 practice exercises, 42 daily log entries.\n"
  "- **Production depth that affects price:** a printed, fillable 128-page workbook is deeper than the $7-$25 printable PDFs it competes with, but it carries a print cost and the buyer expects a physical book.\n")
a("## 2. Comparable Shortlist And Platform Notes\n")
a("Thirteen comparables were pooled. **No platform exposed unit sales or bestseller ranks in the pages reached**, so demand signal is mostly absent.\n"
  "- **Payhip and Gumroad:** many brain-fog or reset printables listed at $7-$25. These are the closest in niche, but only listings were visible (no sales counts).\n"
  "- **Etsy:** two relevant digital trackers found; prices were not captured and there was no confirmed bestseller badge.\n"
  "- **Selar:** Nigerian self-help and workbook ebooks, priced in USD or naira; every product showed **0 ratings**, so Selar gives no demand evidence for this topic.\n"
  "- **Retail print comparables:** *The Memory Workbook* (2001) lists at $29.95 for 225 pages; *Keep Your Brain Alive* shows a $11.17 new marketplace price. Neither is a current list price for a new habit workbook.\n"
  "- **Not researched in this run:** Teachable, Podia, Creative Market, Design Bundles, Stan Store and Shopify storefronts. They are digital-download or course platforms with little relevance to a printed workbook, and no evidence was gathered for them.\n"
  "- **Amazon Kindle and Apple Books:** not reachable via fetch in earlier scouts (Amazon blocks scraping; no memory-specific Apple chart found). KDP royalty bands are the only hard data (below).\n")
a("## 3. Purchase-Trend Evaluation\n")
a("- **No verified sales signal** was found for any comparable. All signals below are *proxies*.\n"
  "- **Price clustering (proxy):** printable brain-fog PDFs cluster at **$7-$25**, with the lowest-priced (£6.99, $7) being the simplest reset pages. The $20-$25 listings are bundles or longer workbooks. There is no evidence that higher-priced listings sell worse, but there is also no evidence that they sell.\n"
  "- **Print versus PDF:** the only print comparables are older and higher priced ($29.95 list, 225 pages). A new 128-page workbook has room between the $7-$25 PDFs and the $29.95 print book.\n"
  "- **Promo behaviour on Apple:** Apple Books Health, Mind &amp; Body top-40 includes many $1.99-$2.99 promotional prices, so a deep discount can lift chart rank but is not a sustainable price (from the earlier Apple scout).\n")
a("## 4. Currency-Normalized Comparison\n")
a("| Platform | Product | Format | Native price | ₦ equivalent | USD equivalent | Trend signal (proxy) | Market-fit note |\n|---|---|---|---|---|---|---|---|")
for p, t, f, nat, usd, sig, fit in rows:
    if usd is None: a(f"| {p} | {t} | {f} | {nat} | n/a | n/a | {sig} | {fit} |")
    else: a(f"| {p} | {t} | {f} | {nat} | {n(usd)} | ${usd:,.2f} | {sig} | {fit} |")
a("")
a("## 5. Pricing Recommendation\n")
cost, r1699 = roy(16.99); _, r1499 = roy(14.99); _, r1299 = roy(12.99); _, r1999 = roy(19.99); _, r2499 = roy(24.99)
a(f"**KDP print cost (third-party estimate, CHECK in KDP's calculator):** 8.5 x 11 in is a *large trim* (over 6.12 in wide), so a commonly cited US black-and-white rate is **$1.00 fixed + $0.017 per page**. For 128 pages that is about **${cost:.2f} per copy**. Other sources quote $0.012 per page (about $2.54), so the true figure may be lower. KDP royalty on paperbacks is typically 60% of list price minus printing cost. These are *estimates*, not confirmed KDP figures.\n")
a("### Paperback (main product)\n")
a(f"- **Recommended price: $16.99** (**{n(16.99)}**).\n- **Defensible range: $14.99 ({n(14.99)}) to $19.99 ({n(19.99)}).**\n"
  f"  - *Floor $14.99:* the Mind Reset Guide (about $17.24 at the assumed rate) and Selar's $14.75 productivity ebook show buyers pay roughly this for a PDF or ebook habit guide; below it a 128-page print book looks cheap next to them, and the royalty drops to about ${r1499[1] if False else roy(14.99)[1]:.2f}.\n"
  f"  - *Ceiling $19.99:* the Focus + Brain Clarity Bundle at $20 and The Clarity Code at $24.99 are the highest-priced direct competitors; $19.99 stays just under them while *The Memory Workbook* lists at $29.95 for a denser, older book.\n"
  f"- **Estimated royalty per copy (60% of list minus print cost):** $12.99 gives about ${roy(12.99)[1]:.2f}; **$14.99 about ${roy(14.99)[1]:.2f}; $16.99 about ${roy(16.99)[1]:.2f}; $19.99 about ${roy(19.99)[1]:.2f}.** At the recommended $16.99 that is roughly **{n(roy(16.99)[1])} per copy** at ₦1,365/$ (estimate).\n"
  "- **Positioning rationale:** priced in the *upper-middle* of the $7-$25 PDF cluster because the product is a physical, 128-page, structured programme with a baseline and final self-check, which none of the PDF comparables show. It sits well under the $29.95 older print book.\n"
  "- **Interior ink:** a B&amp;W (greyscale) interior is assumed for the cost above. A colour interior would raise the print cost materially (rates not confirmed) and push the viable price well above $19.99, so B&amp;W is the recommended setting.\n")
a("### Ebook / PDF edition (85 pages)\n")
a(f"- **Recommended price: $7.99** (**{n(7.99)}**). **Range: $6.99 ({n(6.99)}) to $9.99 ({n(9.99)}).** This sits inside the Kindle 70% band ($2.99-$12.99, effective 7 July 2026, [KDP](https://kdp.amazon.com/en_US/help/topic/G200634560)) and in line with the cheapest direct competitors ($7 Brain Fog Breaker Reset, £6.99 Brain Fog Reset). Royalty at 70% is about **${0.7*7.99:.2f} before delivery fees**.\n"
  "- **Format caution:** the workbook is designed to be written in. The ebook/PDF edition is a convenience version; it is a weaker product than the paperback, so keep it clearly cheaper.\n")
a("### Platform-specific notes\n- **One global USD price is more defensible** than differentiated pricing: all comparable evidence is USD-denominated and the buyers are in USD/GBP/CAD/AUD markets. Let Amazon convert to local storefronts (check each marketplace's prices).\n- **Selar / naira pricing:** only worth a separate naira listing for a Nigerian audience, and no comparable evidence supports a specific price: Selar comparables here are finance or productivity ebooks, with ₦9,900 as the only naira anchor.\n")
a("### Risk flags\n- **No verified sales evidence** for any comparable; the price band rests on listing prices only.\n- **Print cost is a third-party estimate** and Amazon changes rates, so recompute the royalty in KDP before locking the price.\n- **Exchange-rate risk:** the ₦/$ rate is volatile; the ₦ column is indicative only. KDP pays Nigerian authors by wire transfer in NGN (verified 2026-09-23; confirm current terms).\n- **Review moat:** established brain-health books have thousands of ratings (e.g. Goodreads shows tens of thousands for *Limitless* and *Unlimited Memory*); a new title starts with none, so early price promotions may be needed.\n- **Competitive crowding:** low-priced PDFs ($7) can anchor buyers low for the ebook edition.\n")
a("## 6. Platform Recommendation\n")
a("| Rank | Platform | Why here | Why not the next-best | Fees (approx., CHECK) |\n|---|---|---|---|---|\n"
  "| 1 (primary) | **Amazon KDP** (paperback + Kindle) | Largest buyer base for print workbooks; the product's natural format; print-on-demand, no inventory; Nigeria payout by wire in NGN | Gumroad and Payhip sell only digital files, so no print channel | Paperback: 60% minus print cost; Kindle: 70% in the $2.99-$12.99 band, 35% outside (verified royalty rules) |\n"
  "| 2 | **Apple Books** via an aggregator (e.g. Draft2Digital) | Memory and brain-health content charts on Apple; reaches US/GB/CA/AU readers | Apple does not suit fillable workbooks well and adds an aggregator fee; ebook only | Aggregator and Apple split not confirmed this run |\n"
  "| 3 | **Gumroad or Payhip** (printable PDF) | Closest direct competitors live here at $7-$25; fast to list the 85-page PDF edition | Neither has built-in discovery; traffic must come from the Louda social content | Not confirmed this run |\n"
  "| 4 | **Etsy** (digital printable) | Printable trackers sell here; some relevant listings found | No bestseller evidence found; crowded, with price pressure | Not confirmed this run |\n"
  "| 5 (optional) | **Selar** | Naira payments and a Nigerian audience | Comparables show 0 ratings and finance topics; the product targets US/UK buyers, not Nigeria | Not confirmed this run |\n")
a("**Ruled out or not judged:** Teachable and Podia (course platforms), Creative Market and Design Bundles (design assets), Stan Store and Shopify (own-store routes that need your own traffic). *No evidence was gathered for them in this run, so they were not ranked.*\n")
a("*This is a strategic estimate from observed listings, not financial advice or a guarantee of sales.*\n")
open('/home/user/firstrepo/memory-workbook/prica_memory-workbook.md','w').write("\n".join(out))
print(cost, r1699, n(16.99), n(7.99))
