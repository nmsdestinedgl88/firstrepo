import re
CB = ("Tara, a 44-year-old Black British woman with warm mid-brown skin, an oval face, soft laugh lines, a small mole above her left eyebrow, "
      "and shoulder-length dark brown natural curls. She wears round tortoiseshell glasses pushed up on her head, small gold stud earrings, and a sage-green "
      "cardigan over a plain white tee. Medium build, about five foot six. Friendly, slightly rushed, self-deprecating energy. She speaks with a warm London accent.")
PL = ("PRODUCT LOCK: a portrait paperback workbook, US letter proportions (8.5 by 11 inches), softcover. Pale mint ruled-notebook-paper cover with faint horizontal lines. "
      "Large rounded hand-lettered dark charcoal title: \"The 5-Minute Memory Workbook\". Below it, in smaller rounded sans-serif: \"Tiny Daily Habits for a Sharper, More Reliable Mind After 40\". "
      "Lower half shows green hand-drawn doodles: a steaming coffee cup, a pair of keys, a weekly calendar strip with three ticks, a sticky note with a star, a lightbulb, and a row of six tick-boxes with the first four ticked. "
      "Grey footer band with the words \"Cimple Books\" and \"www.cimpledigital.com/books\". Only the product text above exists; the product matches the reference image exactly and keeps its design and printed text for the whole clip.")
GENERIC = "a plain closed paperback workbook with a blank pale cover, no title, no logo and no text"
assert 60 <= len(CB.split()) <= 90, len(CB.split())
END_P = "No subtitles, captions or watermarks. Any text on the product is exactly as in the reference image and does not change."
END_N = "No on-screen text, no subtitles, no logos, no watermarks."
SPK = "only these words are spoken, nothing else; lips match the words"
NOSP = "no dialogue, no speech"
clips = []
def clip(n, label, tmpl, beat, mode, prod, setting, shot, action, light, dialogue, sfx, edit):
    if dialogue: assert len(dialogue.split()) <= 18, (n, len(dialogue.split()))
    p = f"{CB}\n"
    if prod: p += f"{PL}\n"
    else: p += f"If any book appears it is {GENERIC}.\n"
    p += f"Setting: {setting}\nShot: {shot}\nAction (8 seconds): {action}\nLighting and mood: {light}\n"
    p += (f"Dialogue, in a warm London accent: \"{dialogue}\" ({SPK}).\n" if dialogue else f"({NOSP}).\n")
    p += f"Sound: {sfx}; no background music.\n"
    p += (END_P if prod else END_N)
    clips.append(dict(n=n, label=label, tmpl=tmpl, beat=beat, mode=mode, prompt=p, edit=edit, dialogue=dialogue))
K = "a bright, lived-in UK terraced-house kitchen, morning light through a side window, a wall key hook, a mug on the counter, a ruled notepad on the table"
clip(1, 'The Doorway Freeze', 'A: The Keys Reveal', 'Hook (0-3s)', 'Frames to Video (first frame: character_5min-memory-workbook.png)', False, K,
     'Medium shot, handheld, one slow push-in',
     'Tara walks into the kitchen holding a coat, stops dead in the doorway, looks around with a puzzled frown, then turns slowly toward camera and raises her eyebrows.',
     'Warm natural window light, gently comic mood', 'Why did I come in here?', 'quiet kitchen ambience, soft footsteps, a kettle ticking as it cools',
     'Overlay text: "Every. Single. Day." Cut to Clip 2 at the reveal beat.')
clip(2, 'Keys In The Fridge', 'A: The Keys Reveal', 'Problem (3-8s)', 'Frames to Video', False, K,
     'Close-up over her shoulder, camera locked',
     'Tara opens the fridge, finds her house keys on a shelf next to the milk, holds them up and laughs at herself, shaking her head.',
     'Cool fridge light mixed with warm window light, playful mood', 'Keys. In the fridge. Again.', 'fridge door hum, a soft clink of keys, her light laugh',
     'Overlay: "Sound familiar?" Insert real footage of the cover for 2 seconds if desired.')
clip(3, 'Turning To Camera', 'A: The Keys Reveal', 'Product moment (8-13s)', 'Ingredients to Video (character image, product reference image)', True, K,
     'Medium close-up, locked camera, shallow depth of field',
     'Tara sits at the table and slides the workbook from beside the notepad into frame with both hands, holds the front cover steady toward the camera for three seconds, then taps it once and smiles.',
     'Soft window light, warm and reassuring', 'Five minutes a day. That is the whole plan.', 'gentle paper rustle, a soft tap on the cover, quiet kitchen ambience',
     'Overlay: "6 weeks. 5 minutes a day." Insert real flip-through footage of pages 14, 18 and 22 here.')
clip(4, 'Tick The Box', 'A: The Keys Reveal', 'CTA (13-18s)', 'Ingredients to Video (character image, product reference image)', True, K,
     'Top-down shot of the table, locked camera',
     'Tara\'s hands tick the first box on a tracker page of the open workbook with a pen, then close it and rest her hand on the cover; the product does not move or change shape.',
     'Soft overhead window light, calm mood', None, 'pen scratch on paper, a soft exhale, quiet kitchen ambience',
     'Overlay: "Link in bio". Add the real store link and price in the caption. Real page footage should replace this if the interior is visible.')
LR = "a tidy living-room corner with a sofa, a plant, a mug on a side table and warm afternoon window light"
clip(5, 'Not Broken', 'B: Why Your Brain Is Not Broken', 'Hook (0-3s)', 'Frames to Video', False, LR,
     'Medium talking-head shot at eye level, camera locked',
     'Tara faces the camera, takes a breath, and speaks directly with a reassuring half-smile, gesturing gently with one hand.',
     'Soft natural light, calm and warm', 'Forgetting your keys in your forties does not mean your brain is broken.', 'quiet living-room ambience, a soft clock tick',
     'Overlay: "Not broken. Overloaded." Cut quickly.')
clip(6, 'Three Real Causes', 'B: Why Your Brain Is Not Broken', 'Body (3-12s)', 'Frames to Video', False, LR,
     'Medium close-up, camera locked',
     'Tara counts three fingers on one hand as she speaks, glancing up as she thinks of each point, then looks back at the camera.',
     'Soft natural light, steady and friendly', 'Usually it is attention, sleep and stress, not something sinister.', 'quiet living-room ambience, a faint breath',
     'Overlay the three words as they are spoken: Attention, Sleep, Stress. Add the doctor line in the caption.')
clip(7, 'Start Small', 'B: Why Your Brain Is Not Broken', 'CTA (12-18s)', 'Ingredients to Video (character image, product reference image)', True, LR,
     'Medium shot, slow push-in',
     'Tara picks up the workbook from the sofa arm, holds the cover toward the camera with both hands, then lowers it into her lap and nods.',
     'Warm afternoon light, hopeful mood', 'Start with five minutes. And see a doctor if you are worried.', 'soft paper rustle, quiet ambience',
     'Overlay: "Not medical advice." Pin the link and the doctor note in the comments.')
D = "a small home desk by a window with a laptop, a mug, a notepad and a houseplant, mid-morning light"
clip(8, 'Counting Down', 'C: Five Minutes, Six Weeks', 'Hook (0-3s)', 'Frames to Video', False, D,
     'Medium close-up, camera locked',
     'Tara glances at a small kitchen timer, presses start, and turns to the camera with a bright, slightly mischievous smile.',
     'Soft window light, upbeat mood', 'Five minutes. One tiny habit. Watch what happens.', 'a crisp timer click, quiet room tone, gentle ticking',
     'Overlay: a five-minute countdown. Cut to real screen or flip-through footage next.')
clip(9, 'The Habit Sentence', 'C: Five Minutes, Six Weeks', 'Demo (3-12s)', 'Ingredients to Video (character image, product reference image)', True, D,
     'Top-down then slight tilt to over-the-shoulder, camera moves once only',
     'Tara opens the workbook flat on the desk, runs her pen along the line of a fill-in sentence, writes a few words, and then taps the page with the pen and looks up.',
     'Bright, clean desk light, focused mood', 'After my coffee, I do my tiny habit. That is it.', 'pen on paper, the timer ticking, a soft click',
     'Overlay: "After I ___, I will ___." Replace this clip with real footage of the planner page if possible.')
clip(10, 'Six Boxes', 'C: Five Minutes, Six Weeks', 'CTA (12-18s)', 'Ingredients to Video (character image, product reference image)', True, D,
     'Medium close-up, locked camera',
     'Tara holds the closed workbook up beside her face, grins, and gives a small satisfied nod, then lowers it back to the desk without it changing shape.',
     'Warm window light, confident and cheerful', 'Six weeks from now, you will be glad you started today.', 'soft paper tap, quiet room tone',
     'Overlay: "Link in bio". Add a real shot of the cover and the price.')

IMG = (f"Ultra-realistic photograph, vertical 9:16, medium shot from mid-thigh up, facing the camera with a warm natural expression. {CB} "
       "She stands in a bright, lived-in UK terraced-house kitchen with a wall key hook, a mug on the counter and a ruled notepad on the table; soft morning window light. "
       "True-to-life skin texture with visible pores, natural hair detail, realistic fabric and true colour, full-frame 85mm f/1.8 look; sharp focus on the subject, no motion blur, no film grain overlay, no lens dirt, no vignette. "
       f"She holds the product from the reference image, close to her chest with the cover facing the camera. {PL} "
       "No added text, captions or watermarks; not a real or famous person; natural five-fingered hands.")
SHEET = (f"Character reference sheet on a flat neutral grey backdrop: the same woman shown in three views side by side (front, three-quarter and profile), full body, standing relaxed, even soft studio light. {CB} "
         "Consistent outfit and features in all views, true-to-life skin texture, sharp focus, no text, no labels, no watermarks, natural five-fingered hands.")

# ---------- companion txt ----------
txt = ["LOUDA PROMPTS: The 5-Minute Memory Workbook", "Attach character_5min-memory-workbook.png (and the product cover image where noted) in Flow.", "",
       "=== NANO BANANA: CHARACTER IMAGE (file: character_5min-memory-workbook.png) ===", "Attach: cover_memory-workbook.png as the product reference.", IMG, "",
       "=== NANO BANANA: OPTIONAL CHARACTER SHEET (file: character_sheet_5min-memory-workbook.png) ===", SHEET, ""]
for c in clips:
    txt += [f"=== FLOW CLIP {c['n']}: {c['label']} | Template {c['tmpl']} | {c['beat']} ===", f"Mode: {c['mode']}", c['prompt'], f"Edit note: {c['edit']}", ""]
open('/home/user/firstrepo/memory-workbook/louda_prompts_5min-memory-workbook.txt', 'w').write("\n".join(txt))

# ---------- markdown ----------
md = []
a = md.append
a("# Louda Pack: The 5-Minute Memory Workbook\n")
a("**Product:** The 5-Minute Memory Workbook: Tiny Daily Habits for a Sharper, More Reliable Mind After 40 (Cimple Books). Paperback workbook, 128 pages, plus a lean ebook.\n")
a("**Evidence note:** The research below came from a handful of web searches. It found creator and product listings, but **no verified view counts or sales figures**. Everything marked *proxy* is inferred from what was visible, not measured. Treat the ranking of hooks and formats as a starting hypothesis to test with real posts.\n")
a("## 1. Niche Derivation\n")
a("- **Category:** self-help habit workbook (health and mind).\n- **Niche:** a gentle, evidence-informed memory-and-focus habit workbook for busy adults in midlife, including people experiencing perimenopausal brain fog.\n"
  "- **Buyer persona:** a time-poor 40-something who keeps losing keys, names and trains of thought, is worried but not in crisis, and wants something practical and non-medical.\n"
  "- **Positioning angle:** small, specific, reassuring. *Five minutes a day, six weeks, no gimmicks.*\n"
  "- **Key target market (content speaks to first):** English-speaking women and men aged 38-50 in the US, UK, Canada and Australia (the stores where the paperback sells), with a **female skew** in the perimenopause and brain-fog conversation. The buyer is the user.\n")
a("## 2. Niche Content Framework Scan\n")
a("What turned up (proxy; no creator metrics available):\n"
  "- **Meno TikTok is large.** A CBC report says menopause-hashtag videos have recorded over a billion views on TikTok in total ([CBC](https://www.cbc.ca/1.6861886)). That is the whole category, not any single video.\n"
  "- **Recurring pillars:** symptom lists that go beyond hot flushes, relatable humour about mid-sentence blanks, and reassurance that it is a hormonal or life-stage change and not a personal failing (summarised from the same search).\n"
  "- **Credibility gap:** one guide warns that menopause hashtags carry a lot of unreliable content ([Chatelaine](https://www.chatelaine.com/health/menopause-tiktok/)), so creators who pair personal experience with medical grounding stand out.\n"
  "- **Storytelling shapes seen:** relatable-moment humour, reassurance myth-busting, and \"things nobody tells you\" listicles.\n"
  "- **Brain-health content also exists as a product category:** a brand recruiting creators for \"memory recall\" and productivity-hack content on TikTok and Instagram shows that memory is a commercial content theme.\n")
a("## 3. Competitor Product Shortlist\n")
a("| Product | Platform | Price (listing) | Signal |\n|---|---|---|---|\n"
  "| [Brain Fog Reset workbook](https://payhip.com/b/Wmvk7) | Payhip | £6.99 | Listing only; weekly reflection, planning matrix, habit tracker. No sales shown. |\n"
  "| [Brain Fog Breaker Reset](https://payhip.com/b/fbKSh) | Payhip | $7 | Listing only; brain-dump and sorting pages. |\n"
  "| [Focus + Brain Clarity Bundle](https://payhip.com/b/uUIZV) | Payhip | $20 | Listing only; five-guide bundle aimed at adults 40+. |\n"
  "| [Printable Mind Reset / The Clarity Code](https://calmwithinher.gumroad.com/l/printable-mind-reset) | Gumroad | $24.99 | Listing only; no ratings shown. |\n"
  "| [The Mind Reset Guide](https://themindresetguide.gumroad.com/l/Mind-Reset-Guide) | Gumroad | €14.99 | 5 ratings shown (the only review-like signal found, and it is thin). |\n"
  "| [Executive dysfunction workbook printable](https://www.etsy.com/listing/4467464032/executive-dysfunction-workbook-printable) | Etsy | n/a | 71-page printable with habit tracker and working-memory pages. No bestseller badge confirmed. |\n"
  "| [HashimotoTracker](https://www.etsy.com/ca/shop/HashimotoTracker) | Etsy | n/a | Brain-fog-friendly tracker with large text and 1-5 scales. |\n")
a("**Read-across:** the closest competitors are **low-priced printable PDFs** ($7-$25), mostly \"brain fog reset\" planners. None of the listings found is a printed 128-page programme with a baseline and final self-check, which is the product's angle. No platform exposed sales ranks, so *top-selling* could not be confirmed (editorial proxy).\n")
a("## 4. Viral Content Analysis (proxy)\n")
a("No competitor-specific viral posts or \"I tried\" reviews were found, so this table is built from the niche scan only and ranked by how often a pattern recurred in that small sample.\n")
a("| Rank | Topic | Hook pattern | Format | Evidence trail |\n|---|---|---|---|---|\n"
  "| 1 | Everyday slips are normal and relatable | Relatable-moment opener (\"mid-sentence blank\") | POV or self-deprecating skit | Humour creators sharing their own pauses (search 4) |\n"
  "| 2 | \"Not your fault, not dementia\" reassurance | Myth-bust / reassurance opener | Talking head with a plain explanation | Brain-fog-is-not-losing-your-mind messaging (search 4) |\n"
  "| 3 | Symptom lists and \"things nobody tells you\" | Number-promise opener | Listicle or flip-through | 34-symptoms-style viral video (search 4) |\n"
  "| 4 | Small daily routines | \"Five minutes\" promise | Demo of a tracker or planner | Brain-fog and reset workbooks all sell on short daily use (searches 2, 3) |\n")
a("*Limits:* no view counts, no named viral posts. Nothing here is a verified engagement figure.\n")
a("## 5. Character Profile\n")
a("**Name:** Tara (fictional). **Role:** the buyer: a 44-year-old project coordinator and parent of teenagers who has started to joke about her memory and quietly worries about it.\n"
  "- **Age and look:** 44, Black British woman, warm mid-brown skin, oval face, soft laugh lines, a small mole above her left eyebrow, shoulder-length dark brown natural curls. Medium build, about five foot six.\n"
  "- **Wardrobe:** sage-green cardigan over a plain white tee (a quiet nod to the brand green #56CB87 and #30A666).\n- **Accessories:** round tortoiseshell glasses pushed up on her head; small gold stud earrings.\n"
  "- **Setting:** a bright, lived-in UK terraced-house kitchen with a wall key hook, a mug and a ruled notepad; a home desk by a window.\n- **Default energy:** friendly, slightly rushed, self-deprecating.\n- **Voice:** warm London accent.\n"
  "- **Consistency anchors:** (1) sage-green cardigan; (2) tortoiseshell glasses on her head; (3) small gold studs; (4) the mole above her left eyebrow; (5) natural curls at shoulder length.\n")
a("**Why this character:** the key market is English-speaking midlife buyers with a female skew, so she is a recognisable woman in her mid-40s in an ordinary home. The casting (ethnicity, region) is a **choice, not a data point**: no buyer demographics were available, so test a second character against her before committing the whole campaign. She is the buyer, and no children appear on screen.\n")
a("### Character Consistency Block (paste verbatim)\n")
a("> " + CB + "\n")
a("### Product Lock (paste verbatim whenever the book is visible)\n")
a("> " + PL + "\n")
a("Attach `cover_memory-workbook.png` as the product reference image in every generation that shows the book.\n")
a("## 6. Nano Banana Prompts\n")
a("### Character image (file: `character_5min-memory-workbook.png`)\n\n```\n" + IMG + "\n```\n")
a("### Optional character reference sheet (file: `character_sheet_5min-memory-workbook.png`)\n\n```\n" + SHEET + "\n```\n")
a("## 7. Reel Templates\n")
a("All three share Tara as the presenter. Real product footage (cover and interior flips) is needed wherever the notes say so. Claims stay at \"habits for everyday forgetfulness\"; no cure, prevention or supplement claims.\n")
T = [("A: The Keys Reveal", "Topic 1 (everyday slips are normal) + relatable-moment hook + POV skit", "Rank-1 topic and format; the cheapest to shoot and the most shareable.",
      ["That moment you walk into a room and forget why.", "Me, every morning at 7:42.", "Nobody warned me about the keys in the fridge."],
      "0-3s Doorway freeze (Clip 1). 3-8s Keys in the fridge (Clip 2). 8-13s She slides the workbook into frame (Clip 3). 13-18s Tick-the-box close (Clip 4).",
      "\"Every. Single. Day.\" / \"Sound familiar?\" / \"6 weeks. 5 minutes a day.\"",
      "If you walk into rooms and forget why, you are not alone. Six weeks of five-minute habits helped me feel more on top of things. Link in bio. (Not medical advice.)", "Comment your funniest memory slip. Link in bio.", "15-18 seconds"),
     ("B: Why Your Brain Is Not Broken", "Topic 2 (reassurance) + myth-bust hook + talking head", "Rank-2 pattern; builds trust and addresses the fear behind midlife memory searches.",
      ["Forgot a name again? Here is the boring, reassuring reason.", "It is probably not what you are scared it is.", "Three things that mess with your memory in your forties."],
      "0-3s Not broken (Clip 5). 3-12s Three real causes (Clip 6). 12-18s Start small and see a doctor if worried (Clip 7).",
      "\"Not broken. Overloaded.\" / \"Attention. Sleep. Stress.\" / \"Not medical advice.\"",
      "Everyday forgetfulness is common, and small habits can help. If you are worried, speak to your doctor. Link in bio. (Not medical advice.)", "Share this with a friend who needs the reminder.", "18 seconds"),
     ("C: Five Minutes, Six Weeks", "Topic 4 (small daily routines) + number-promise hook + demo", "Rank-4 pattern; shows the actual product and the habit sentence.",
      ["Five minutes. Six weeks. Zero gimmicks.", "The tiniest memory habit I have ever tried.", "Fill in one sentence a day."],
      "0-3s Counting down (Clip 8). 3-12s The habit sentence (Clip 9) with real flip-through of pages 14, 18, 22 inserted. 12-18s Six boxes (Clip 10).",
      "Countdown timer / \"After I ___, I will ___.\" / \"Link in bio\"",
      "A six-week habit workbook, five minutes a day. Sleep, attention, movement, recall and tagging. Link in bio.", "Save this for Monday.", "18-20 seconds")]
for (name, combo, why, hooks, beats, otext, cap, cta, length) in T:
    a(f"### Template {name}\n- **Built from:** {combo}\n- **Why:** {why}\n- **Alternate hooks:** " + " | ".join(f"\"{h}\"" for h in hooks) +
      f"\n- **Beats:** {beats}\n- **On-screen text:** {otext}\n- **Caption:** {cap}\n- **CTA:** {cta}\n- **Length:** {length}\n")
a("## 8. Google Flow Clip Prompts (10 clips, 8 seconds each)\n")
a("Dialogue is at most 18 words per clip. The Character Consistency Block is repeated verbatim in each prompt. The first frame for Frames to Video is `character_5min-memory-workbook.png`.\n")
for c in clips:
    a(f"### Clip {c['n']}: {c['label']}\n- **Template / beat:** {c['tmpl']} / {c['beat']}\n- **Flow mode:** {c['mode']}\n- **Dialogue words:** {len(c['dialogue'].split()) if c['dialogue'] else 0}\n\n```\n{c['prompt']}\n```\n\n- **Edit note:** {c['edit']}\n")
a("## 9. Posting Notes\n- Add the real store link and price in each caption; check the interior pages shown in inserted footage match the final print.\n- Pin a comment with the doctor note: *If you are worried about your memory, please talk to your doctor.*\n- Test Tara against a second character (different region or gender) on two organic posts before paying for any promotion.\n")
open('/home/user/firstrepo/memory-workbook/louda_memory-workbook.md', 'w').write("\n".join(md))
print('ok', len(CB.split()), [len(c['dialogue'].split()) if c['dialogue'] else 0 for c in clips])
