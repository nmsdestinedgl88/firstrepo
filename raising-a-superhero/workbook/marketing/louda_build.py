#!/usr/bin/env python3
"""Generates the louda marketing pack: markdown (-> docx via pandoc) and the plain-text prompt companion.
Every Flow prompt is assembled from the same constants so the Character Consistency Block and Product Lock repeat word for word."""
import os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'raising-a-superhero'

CCB = ("Maya, a 38-year-old American mother with warm medium-brown skin, an oval face with soft smile lines and brown eyes behind round "
       "tortoiseshell glasses, dark brown shoulder-length wavy hair worn in a loose low ponytail with one curl across her forehead, average build, "
       "about 5 feet 6 inches. She wears an oatmeal knit cardigan over a plain white t-shirt, small gold stud earrings and a black watch on her left "
       "wrist. Warm, tired-but-hopeful expression with dry humour; a sage-green mug is never far away.")
assert 60 <= len(CCB.split()) <= 90, len(CCB.split())

LOCK = ('The product is a printed paperback workbook, portrait, 7 by 10 inches, with a solid mid-green cover. A white shield-shaped emblem with a '
        'green five-point star sits upper centre, with a light-green cape swoosh to its left and three small round white and light-green seal stickers '
        'around it. A round green badge with a ribbon reads "40 Simple Activities". The title "Raising a Superhero" is set in large white rounded bold '
        'letters on two lines, "Raising a" then "Superhero". Beneath it, in smaller white text: "A Parent\'s Activity Workbook for Turning ADHD Traits '
        'into Strengths and Growing Your Patience". At the bottom, small white text: "Cimple Books" and "www.cimpledigital.com/books".')
STAND = 'The product matches the reference image exactly and keeps its design and printed text for the whole clip.'
CLOSE_P = 'No subtitles, captions or watermarks. Any text on the product is exactly as in the reference image and does not change.'
CLOSE_N = 'No on-screen text, no subtitles, no logos, no watermarks.'
VOICE = 'warm, calm, unhurried American English'
SETTING = ('a lived-in family kitchen and dining nook in a US suburban home, soft natural window light, a fridge with magnets, '
           'school bags on hooks by the door and a basket of shoes')

CLIPS = [
 # (n, label, template, beat, mode, product?, shot, action, light, dialogue, sfx, edit)
 (1, 'The Five-More-Minutes Confession', 'Template 1', 'Hook (0-3s)', 'Frames to Video (first frame: character_%s.png)' % SLUG, False,
  'Medium close-up, slow push-in', 'Maya leans on the kitchen counter, mug in hand, looks straight to camera with a wry half-smile, then raises her eyebrows on the last word.',
  'Soft morning window light, warm and natural', 'Why does stopping the game feel like pulling a fire alarm in our house?',
  'quiet kitchen ambience, a distant fridge hum', 'On-screen text over the first 3 seconds: "Stopping the game = fire alarm". Keep the real caption off-frame.'),
 (2, 'The Timer Table', 'Template 1', 'Problem to fix (3-9s)', 'Ingredients to Video (character image)', False,
  'Over-the-shoulder shot from behind a child at a table, the child seen only as the back of a small head and two hands building with blocks; locked camera',
  'Maya sits at the table beside the child (back of head only), sets a sand timer down, and taps it once with one finger.',
  'Warm late-afternoon window light', 'Ten minutes, five minutes, one minute. Same words, same voice, every single time.',
  'blocks clicking together, soft room tone', 'Insert text card: "10 - 5 - 1". Optionally cut to the real printed page from Mission 1.3 (The Gentle Landing).'),
 (3, 'The Counter Book', 'Template 1', 'Product moment (9-15s)', 'Ingredients to Video (character image + product image)', True,
  'Medium shot, handheld, gentle drift', 'Maya sets the closed book on the kitchen counter with the front cover facing the camera, rests one hand on it, and smiles.',
  'Soft natural window light', 'I keep this on the counter. Mission one point three is my favourite: the gentle landing.',
  'mug set down on the counter, soft room tone', 'Cut to REAL product footage: a hand flips to Mission 1.3 and shows the Say This box. Do not use generated interior pages.'),
 (4, 'Hold It Up', 'Template 1', 'CTA (15-20s)', 'Ingredients to Video (character image + product image)', True,
  'Medium close-up, locked camera', 'Maya lifts the book with both hands to chest height, front cover facing the camera and held still, and gives a small confident nod.',
  'Soft natural window light', 'Raising a Superhero. Forty simple activities. Link in bio.',
  'soft room tone', 'End card: the real front cover on a clean background and the listing link in the caption or sticker.'),
 (5, 'Instead Of Hurry Up', 'Template 2', 'Hook and swap 1 (0-5s)', 'Frames to Video (first frame: character_%s.png)' % SLUG, False,
  'Medium shot, slow push-in', 'Maya stands at the counter with her mug, glances toward the door where school bags hang, then turns to camera and speaks calmly.',
  'Bright morning window light', 'Instead of "hurry up," I say: "We leave in five minutes. What\'s left?"',
  'kitchen ambience, a toaster pop in the distance', 'On-screen split text: "Instead of: Hurry up!" then "Try: We leave in five minutes. What\'s left?"'),
 (6, 'The Guardian Pause', 'Template 2', 'Patience beat (5-11s)', 'Frames to Video (first frame: character_%s.png)' % SLUG, False,
  'Close-up on shoulders and upper chest, locked camera', 'Maya places one hand flat on the counter, closes her eyes for a moment, takes one slow breath in and a longer breath out, and her shoulders drop.',
  'Soft window light', 'And before I say it, one slow breath. That\'s the Guardian Pause.',
  'a slow inhale and exhale, soft room tone', 'Overlay a small pause-icon graphic and the words "5-second pause". Show the real Phrase Bank page as an insert.'),
 (7, 'Phrase Bank Plug', 'Template 2', 'Product moment and CTA (11-16s)', 'Ingredients to Video (character image + product image)', True,
  'Medium shot, locked camera', 'Maya sets the closed book on the counter, front cover facing the camera, rests two fingers on its top edge, and smiles at the camera.',
  'Soft natural window light', 'More phrases like these are in the Phrase Bank at the back of the book.',
  'soft room tone', 'Cut to REAL footage: a thumb flips to the Phrase Bank table (Instead of / Try). Add caption and link.'),
 (8, 'The Radar Confession', 'Template 3', 'Hook (0-4s)', 'Frames to Video (first frame: character_%s.png)' % SLUG, False,
  'Medium close-up on a sofa, slow push-in', 'Maya sits on a sofa with her mug, looks to camera with a rueful smile, shakes her head at herself, then lifts her eyebrows on the word radar.',
  'Soft afternoon window light', 'Confession: I used to call it a bad attention span. Now I call it a radar.',
  'quiet living room ambience', 'On-screen text: "Not a bad attention span. A wide radar." Keep it a parenting reframe, never a diagnosis claim.'),
 (9, 'The Bird At The Window', 'Template 3', 'Strength moment (4-10s)', 'Ingredients to Video (character image)', False,
  'Wide over-the-shoulder shot from behind, a child seen only as the back of a small head at a window, Maya in soft focus beside; locked camera',
  'The child points at something outside the window; Maya watches, then smiles and quietly lifts her mug.',
  'Golden late-afternoon light through the window', 'No dialogue, no speech.',
  'a soft bird chirp outside, quiet room tone', 'Overlay text: "Noticed what nobody else saw." Optional cut to the Wide Radar module opener (real page).'),
 (10, 'The Brag Board', 'Template 3', 'Win and CTA (10-16s)', 'Frames to Video (first frame: character_%s.png)' % SLUG, False,
  'Medium shot at the fridge, slow push-in', 'Maya writes on a small blank sticky note with a pen, presses it onto a cork board beside the fridge, steps back and smiles.',
  'Soft natural window light', 'Today\'s win: my kid noticed the bird nobody else saw. That\'s a real strength.',
  'pen scratching on paper, soft room tone', 'The sticky note stays blank in the generation; add real handwriting in the edit. End on the real book cover and link.'),
]

def flow_prompt(c):
    n, label, tmpl, beat, mode, prod, shot, action, light, dlg, sfx, edit = c
    words = len(re.findall(r"[A-Za-z0-9']+", dlg)) if not dlg.startswith('No dialogue') else 0
    assert words <= 18, (n, words)
    p = [CCB]
    if prod: p.append(LOCK + ' ' + STAND)
    p.append(f'Setting: {SETTING}.')
    p.append(f'Shot: {shot}.')
    p.append(f'Action over 8 seconds: {action}')
    p.append(f'Lighting and mood: {light}; warm, calm, relatable.')
    if dlg.startswith('No dialogue'):
        p.append('No dialogue, no speech.')
    else:
        p.append(f'Dialogue, spoken in {VOICE}: "{dlg}" Only these words are spoken, nothing else; lips match the words.')
    p.append(f'Sound: {sfx}; no background music.')
    p.append('Any child in frame is shown only as hands or the back of the head, never a close-up of a face; wholesome and non-identifiable.' if 'child' in action or 'child' in shot else '')
    p.append('Camera and wardrobe stay as described; the character\'s hands have five fingers; no extra people.')
    p.append(CLOSE_P if prod else CLOSE_N)
    return ' '.join(x for x in p if x), words

NB_PROMPT = ('Ultra-realistic vertical 9:16 photograph, medium shot from mid-thigh up, of ' + CCB + ' She faces the camera with a warm, natural expression, '
             'standing in ' + SETTING + ', holding the product from the reference image in her left hand against her hip with the front cover clearly visible. '
             + LOCK + ' ' + STAND + ' Realism: true-to-life skin texture with visible pores, natural hair detail, realistic knit and cotton fabric, true colour, '
             'natural window light, full-frame 85mm f/1.8 look with a softly blurred background. Capture: sharp focus on the subject, still and clean, no motion blur, '
             'no film grain overlay, no lens dirt, no vignette. No added text, captions or watermarks; not a real or famous person; natural five-fingered hands.')

REF_SHEET = ('Character reference sheet on a plain flat neutral grey background, three full-body views of the same woman side by side: front, three-quarter and profile, '
             'evenly lit, standing relaxed. ' + CCB + ' No product, no props except the sage-green mug held in her right hand in the front view. '
             'Ultra-realistic photographic look, sharp focus, no added text or watermarks; not a real or famous person; natural five-fingered hands.')

# ---------------------------------------------------------------- plain-text companion
txt = []
txt.append('LOUDA PROMPTS: RAISING A SUPERHERO (copy and paste)\n')
txt.append('Attach to EVERY image or video generation that shows the product: the accepted front cover (cover_%s.png). Paste the Product Lock unchanged.\n' % SLUG)
txt.append('=' * 70 + '\nNANO BANANA: character image (expected filename: character_%s.png)\nAttach: the front cover image as the product reference.\n' % SLUG + '=' * 70)
txt.append(NB_PROMPT + '\n')
txt.append('=' * 70 + '\nNANO BANANA (optional): character reference sheet (expected filename: character_%s_sheet.png)\n' % SLUG + '=' * 70)
txt.append(REF_SHEET + '\n')
flow_texts = {}
for c in CLIPS:
    fp, w = flow_prompt(c); flow_texts[c[0]] = (fp, w)
    txt.append('=' * 70 + f'\nGOOGLE FLOW CLIP {c[0]:02d}: {c[1]}  [{c[2]}, {c[3]}]  (8 seconds)\nMode: {c[4]}\n' + '=' * 70)
    txt.append(fp + '\n')
open(os.path.join(HERE, f'louda_prompts_{SLUG}.txt'), 'w').write('\n'.join(txt))

# ---------------------------------------------------------------- main document (markdown -> docx)
md = []
A = md.append
A('---\ntitle: "Louda Marketing Pack: Raising a Superhero"\nsubtitle: "Cimple Books | Reels, character and Google Flow prompts"\n---\n')
A('**Date:** 2026-10-12. **Product:** *Raising a Superhero: A Parent\'s Activity Workbook for Turning ADHD Traits into Strengths and Growing Your Patience* (print-first paperback, 144 pages, 7 x 10 in). **Product reference image:** the accepted front cover.\n')
A('**Evidence note:** public view counts for parenting-ADHD short videos were not accessible in this run. Every engagement signal below is either reported by a named source or labelled as inferred. No view counts are stated as fact.\n')

A('# 1. Niche Derivation\n')
A('- **Category:** parenting and neurodiversity workbook, print-first, non-medical.\n- **Specific niche:** a strengths-based activity workbook for parents of children about 5 to 12 who have ADHD, with a built-in parent-patience practice.\n'
  '- **Buyer persona (inferred):** a parent in their 30s or 40s, often the one managing mornings, homework and school contact, who is tired, wants something to do tonight and does not want to be shamed. I found no buyer-demographic data, so gender and ethnicity are not asserted.\n'
  '- **Buyer versus user:** the parent buys and uses it, with the child taking part in the activities. The child does not read the book.\n'
  '- **Positioning angle:** transformation in small steps ("simple things to do tonight") plus relief for the parent ("grow your patience"). Not a clinical or diagnostic angle.\n'
  '- **Key target market:** English-speaking parents shopping Amazon, US first (the Kindle Ranker and Apple search data in the market report are US), then UK, Canada and Australia. A direct-sales channel in Nigeria is a secondary market, with Naira pricing from prica.\n')

A('# 2. Niche Content Framework Scan\n')
A('| Finding | Evidence (source type) |\n|---|---|\n'
  '| Creators in this space post practical tips, personal stories and product reviews or unboxings, often in a "family centered, creative, colorful" look | Creator profiles on a creator marketplace ([Mindy C.](https://joinbrands.com/@mindy-caputo1), [Mimi](https://joinbrands.com/@mimitangugc)) (proxy: self-descriptions, not performance data) |\n'
  '| Highly viewed ADHD and autism TikToks mostly come from people with lived experience and mostly share personal experience in a humorous or self-deprecating tone; themes include lived experience, family and relationships, and strengths and challenges | [University of Western Australia study of 500 highly viewed TikTok videos](https://research-repository.uwa.edu.au/en/publications/autism-and-attention-deficithyperactivity-disorder-content-in-hig/) (study, reported) |\n'
  '| A parent-coach clip showing a three-tier rolling basket for clutter was reported as "viral"; format is a parent talking to camera with a physical demonstration | [Scary Mommy](https://www.scarymommy.com/parenting/adhd-cart-hack-tiktok-video) (reported; no view count given) |\n'
  '| A mother of three kids with ADHD explains a morning routine in a storytelling style: observe where the day goes wrong, prepare the night before, tailor it per child | [Upworthy](https://www.upworthy.com/?p=6370) (reported; no view count given) |\n'
  '| Misinformation and oversimplified symptom claims are a recognised concern in ADHD short video | Same UWA research and related press (reported). **Implication:** our content stays practical and makes no medical claims |\n'
  '| A creator-led, light and upbeat tone can sell an ADHD book: *ADHD is Awesome* was reported as #1 in ADHD books on Amazon at launch | [KARE 11](https://kare11.com/article/news/local/news-at-noon/adhd-is-awesome-book-launches/89-046b3c2c-1d5b-4182-b9c4-7e426b440784) (reported) |\n')
A('**Content pillars that recur:** (1) practical home hacks for daily friction; (2) honest, humorous lived experience; (3) strengths reframing. **Not found:** BookTok-style video reviews of ADHD parenting books, per-video view data, or hook wording from the videos themselves.\n')

A('# 3. Competitor Product Shortlist\n')
A('| # | Product | Platform | Signal (label) |\n|---|---|---|---|\n'
  '| 1 | *How to Parent Children with ADHD* (Laine) | Amazon print | BSR 5,335, est. $8,305/month (third-party Kindle Ranker estimate) |\n'
  '| 2 | *Angry Parent Angry Child* (Khang) | Amazon print and Kindle | print BSR 17,143, est. $4,523/month (third-party estimate) |\n'
  '| 3 | *ADHD is Awesome* (Holderness) | Amazon Kindle | Kindle BSR 11,735, 1,138 reviews (third-party estimate and reported counts) |\n'
  '| 4 | *Thriving with ADHD Workbook for Kids* (Miller) | Amazon / Goodreads | 148 pp, 4.26 average from 315 Goodreads ratings (reported) |\n'
  '| 5 | ADHD Parent Toolkit, 7 guides plus printables and quick-response cards, ages 6 to 12 | Payhip | listed at $29 (listing price, reported; no sales signal) |\n'
  '| 6 | ADHD parenting guide with five bonus worksheets | Gumroad | listed at $25; other listings show few or no sales (reported on listings) |\n'
  '| 7 | Parent guide plus daily planner bundle | Gumroad | listed at $30 (reported; no sales signal) |\n'
  '| 8 | ADHD parenting guides and printable toolkits, $2.98 to $24.99 | Etsy | no bestseller badge visible; some listings have no reviews (reported) |\n')
A('**Observations:** the stronger digital listings bundle printables or planners with the guide and use "not a discipline problem" framing. No Stan Store or Selar listings surfaced. Marketplace "top-selling" signals were not accessible for Etsy, Gumroad or Payhip, so those rows carry no sales claim.\n')

A('# 4. Viral Content Analysis (with evidence trail)\n')
A('Ranked by how often the pattern recurred across sources. **Hook patterns are inferred from article and study descriptions, not from the videos\' own wording, and no hook is reproduced.**\n')
A('| Rank | Topics and themes | Evidence |\n|---|---|---|\n'
  '| 1 | Practical fixes for daily friction (routines, clutter, mornings) | ADHD cart clip (Scary Mommy); morning-routine clip (Upworthy); creator profiles listing "tips" |\n'
  '| 2 | Honest, humorous lived experience and family relationships | UWA study themes and tone; creator profiles |\n'
  '| 3 | Strengths and challenges, positive reframing | UWA study subtheme; *ADHD is Awesome* positioning; Payhip and Gumroad listing language |\n'
  '| 4 | Product reviews and unboxings | creator profiles (proxy) |\n')
A('| Rank | Hook patterns (inferred) | Evidence |\n|---|---|---|\n'
  '| 1 | State a familiar daily problem, then show the fix | cart and morning-routine clips |\n'
  '| 2 | A self-deprecating, relatable admission | UWA study tone |\n'
  '| 3 | "Reverse-engineer the problem" curiosity opener | morning-routine description |\n')
A('| Rank | Formats | Evidence |\n|---|---|---|\n'
  '| 1 | Talking to camera with a physical prop demonstration | ADHD cart clip |\n'
  '| 2 | Routine walkthrough told as a story | morning-routine clip |\n'
  '| 3 | Humorous personal-experience clip | UWA study |\n'
  '| 4 | Review or unboxing | creator profiles |\n')

A('# 5. Character Profile\n')
A('**Fictional first name:** Maya.\n\n**Role:** mum of two (a nine-year-old with ADHD and a six-year-old) who keeps the workbook on the kitchen counter and does a mission after school.\n')
A('| Attribute | Detail |\n|---|---|\n| Age, look | 38; warm medium-brown skin; oval face with soft smile lines; brown eyes |\n'
  '| Hair | dark brown, shoulder-length, wavy, loose low ponytail with one curl across the forehead |\n| Build, height | average; about 5 ft 6 in |\n'
  '| Wardrobe | oatmeal knit cardigan over a plain white t-shirt, everyday and relatable; sage-green mug as a subtle nod to the cover palette |\n'
  '| Accessories | round tortoiseshell glasses, small gold stud earrings, black watch on the left wrist |\n'
  '| Setting | a lived-in suburban kitchen and dining nook, natural window light, school bags on hooks, shoe basket |\n'
  '| Expression, energy | warm, tired-but-hopeful, dry humour |\n| Voice | warm, calm, unhurried American English |\n')
A('**Consistency anchors:** (1) round tortoiseshell glasses; (2) loose low ponytail with one forehead curl; (3) gold stud earrings; (4) black watch on the left wrist; (5) sage-green mug.\n')
A('**Why this character:** the market evidence is Amazon-led and English-speaking, and the content pattern that recurs is a relatable parent speaking to camera in a real home with a humorous, tired-but-hopeful tone. I found no data on the buyers\' ethnicity, so the character is an everyday US parent, not a claim about who buys. If your audience is mainly in Lagos or another market, change only the first two sentences of the Consistency Block (appearance and setting) and regenerate; every prompt below reads the same block, so they update together.\n')
A('**Character Consistency Block (%d words, pasted word for word into every prompt):**\n\n> %s\n' % (len(CCB.split()), CCB))
A('**Product Lock (from the accepted front cover; the on-pack text is quoted exactly as printed):**\n\n> %s\n\nStanding line in every product prompt: *%s* Attach the front cover image to each generation that shows the book.\n' % (LOCK, STAND))

A('# 6. Nano Banana Character Image Prompts\n')
A('**Main prompt** (expected filename `character_%s.png`; attach the front cover as the product reference):\n\n```\n%s\n```\n' % (SLUG, NB_PROMPT))
A('**Optional reference sheet** (expected filename `character_%s_sheet.png`):\n\n```\n%s\n```\n' % (SLUG, REF_SHEET))

A('# 7. Instagram Reel Templates\n')
A('All three use Maya as presenter. Each is an original structure inspired by the patterns in section 4. Hook, topic and format combinations are all different. Children appear only as hands or the back of the head. Keep captions to practical tips and add "not medical advice".\n')
A('## Template 1: "The Ten-Minute Fix"\n'
  '- **Built from:** topic 1 (daily friction) + hook 1 (problem, then fix) + format 1 (talking to camera with a prop). It mirrors the most consistent pattern in the evidence.\n'
  '- **Alternative hooks:** "Stopping the game should not feel like a fire alarm." / "The transition is the hard part, so I plan the landing." / "Same five words, three warnings, no shouting."\n'
  '- **Beats (about 20 seconds):** 0-3s hook (Clip 1) | 3-9s the timer on the table (Clip 2) | 9-15s the book on the counter (Clip 3, plus REAL footage of Mission 1.3) | 15-20s CTA (Clip 4, plus the real cover end card).\n'
  '- **On-screen text:** "Stopping the game = fire alarm" / "10 - 5 - 1" / "Mission 1.3: The Gentle Landing".\n'
  '- **Caption:** "Transitions are where our evenings fall apart, so we practise the landing: ten minutes, five minutes, one minute. It is Mission 1.3 in Raising a Superhero. Not medical advice, just something to try tonight. Link in bio."\n'
  '- **CTA:** "Link in bio for the workbook." **Length:** 18 to 22 seconds.\n')
A('## Template 2: "Say This Instead"\n'
  '- **Built from:** topic 2 (patience and relationships) + hook 3 (a curiosity or "reverse-engineer" opener) + format 3 (a swap listicle told with on-screen text). It is the patience pillar from the research.\n'
  '- **Alternative hooks:** "Three phrases I swapped, and my mornings got calmer." / "I stopped saying hurry up. Here is what I say now." / "The five-second pause that stops me before I snap."\n'
  '- **Beats (about 16 seconds):** 0-5s first swap (Clip 5) | 5-11s the Guardian Pause (Clip 6) | 11-16s Phrase Bank plug (Clip 7, plus REAL footage of the Phrase Bank page) | end card.\n'
  '- **On-screen text:** "Instead of: Hurry up!" / "Try: We leave in five minutes. What\'s left?" / "5-second pause".\n'
  '- **Caption:** "Small swaps, calmer mornings. The Phrase Bank at the back of Raising a Superhero has a dozen more. Not medical advice. Link in bio."\n'
  '- **CTA:** "Save this for your next rough morning." **Length:** 15 to 18 seconds.\n')
A('## Template 3: "Not a Bad Attention Span"\n'
  '- **Built from:** topic 3 (strengths reframing) + hook 2 (a self-deprecating admission) + format 2 (a short story told as a day-in-the-life moment). It carries the strengths angle that the book sells on.\n'
  '- **Alternative hooks:** "I used to call it distraction. Now I call it radar." / "My kid notices everything, and I finally see it as a skill." / "Confession: I only ever listed the problems."\n'
  '- **Beats (about 16 seconds):** 0-4s confession (Clip 8) | 4-10s the bird at the window (Clip 9) | 10-16s the Brag Board win (Clip 10, plus REAL footage of Mission 8.4 and the cover) | CTA in caption.\n'
  '- **On-screen text:** "Not a bad attention span. A wide radar." / "Noticed what nobody else saw."\n'
  '- **Caption:** "Every child has a strength hiding in the thing that exasperates us. This week we caught one. Mission 8.4 in Raising a Superhero. Not medical advice. Link in bio."\n'
  '- **CTA:** "Tell me your child\'s hidden strength." **Length:** 15 to 18 seconds.\n')
A('**Where real footage is needed:** the book cover, interior pages (Mission 1.3, Phrase Bank, Mission 8.4) and any handwriting. The generator should never be asked to draw interior pages. If posting AI-generated video, add the platform\'s AI label.\n')

A('# 8. Google Flow Prompts (10 clips x 8 seconds)\n')
A('Distribution: Template 1 = clips 1 to 4, Template 2 = clips 5 to 7, Template 3 = clips 8 to 10. All dialogue is 18 words or fewer.\n')
for c in CLIPS:
    fp, w = flow_texts[c[0]]
    A(f'## Clip {c[0]:02d}: {c[1]}\n')
    A(f'- **Serves:** {c[2]}, {c[3]}\n- **Flow mode:** {c[4]}\n- **Dialogue words:** {w}\n')
    A('```\n' + fp + '\n```\n')
    A(f'**Edit note:** {c[11]}\n')

A('# 9. Caveats\n')
A('- No per-video view counts were accessible; the research supports patterns, not rankings of specific videos.\n- Competitor rows from marketplaces carry listing prices only.\n'
  '- The character is fictional. Do not pair it with claims about real families or real results.\n- Keep every caption free of medical claims and avoid implying a diagnosis.\n')
open(os.path.join(HERE, f'louda_{SLUG}.md'), 'w').write('\n'.join(md))
subprocess.run(['pandoc', os.path.join(HERE, f'louda_{SLUG}.md'), '-o', os.path.join(HERE, f'louda_{SLUG}.docx')], check=True)
print('ok', len(CCB.split()), 'CCB words;', {k: v[1] for k, v in flow_texts.items()})
