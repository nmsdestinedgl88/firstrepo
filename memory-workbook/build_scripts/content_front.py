from lib import *

TITLE = 'The 5-Minute Memory Workbook'
SUB = 'Tiny Daily Habits for a Sharper, More Reliable Mind After 40'

def page(section, flow, tag='core', fill=True, label='My Notes'):
    return dict(section=section, flow=flow, tag=tag, fill=fill, label=label)

WEEKS_OVERVIEW = [
 ('Week 1', 'Sleep', 'The Five-Minute Wind-Down'),
 ('Week 2', 'Attention', 'One Thing, Out Loud'),
 ('Week 3', 'Movement', 'The Five-Minute Movement Snack'),
 ('Week 4', 'Retrieval', 'Recall Before You Check'),
 ('Week 5', 'Encoding', 'The Three-Second Tag'),
 ('Week 6', 'Lock-In', 'The Daily Five'),
]

def front_pages(ebook=False):
    pg = []
    # 1 title page
    f = [sp(70), P('A Six-Week Micro-Habit Programme', 'kicker'), P(TITLE, 'h1'), Rule(CW, 2.2, GREEN, after=10),
         P(SUB, 'h2'), sp(14),
         P('Five minutes a day. Six weeks. One tiny habit at a time. Built for busy adults who want an everyday memory they can count on, without memory palaces, gimmicks or guesswork.'),
         sp(10)]
    f += Callout('This Workbook Belongs To', [''])
    f += [Fld('Name', 1, 26), Fld('My start date', 1, 26), Fld('Why I am doing this (one honest sentence)', 3, 26)]
    f += [sp(14), P('Cimple Books', 'lab'), P('www.cimpledigital.com/books', 'small')]
    pg.append(page('Welcome', f, fill=False))
    # 2 copyright / important note
    f = H('Before You Begin', 'Important Information')
    f += [P('Copyright © 2026 Cimple Books. All rights reserved. No part of this workbook may be reproduced, stored or transmitted without written permission from the publisher, except for brief quotations in reviews and for the personal copying of tracker pages for your own use.'),
          P('<b>This workbook is not medical advice.</b> It is a practical guide to everyday habits that support attention, sleep, movement and learning. It is not designed to diagnose, treat, cure or prevent any condition, including dementia, and it does not replace advice from your doctor or another qualified health professional.'),
          P('If you are worried about your memory, or if your memory has changed noticeably or suddenly, please read the page titled <b>When To Talk To A Doctor</b> and arrange an appointment. Habits help most when any medical causes have been checked first.'),
          P('<b>About the research.</b> This workbook summarises well-known research findings in plain language. Research changes and individual results vary. The Sources page lists the studies and books behind the main ideas so that you can read further. Nothing here promises a particular result.'),
          P('<b>About supplements and products.</b> We do not recommend any supplement, brain-training product or device. If you are considering one, speak to a pharmacist or doctor first, especially if you take regular medication.'),
          P('<b>About physical activity.</b> Check with your doctor before starting new exercise if you have a health condition, are pregnant, are recovering from illness or injury, or have been told to limit activity. Stop and seek advice if you feel unwell.'),
          sp(8), P('First edition, 2026. Published by Cimple Books. Interior and cover images are original works created for this book.', 'small')]
    pg.append(page('Welcome', f, fill=False))
    # 3 welcome
    f = H('Welcome', 'A Note Before We Start')
    f += [P('Have you ever walked into a room and forgotten why? Stood in the car park with no idea where you left the car? Lost a colleague&rsquo;s name halfway through introducing them? You are in good company. These slips are among the most common things people notice in their forties and fifties, and they are usually about <b>attention, stress, sleep and overload</b> rather than anything more worrying.'),
          P('The good news is that everyday memory responds to everyday habits. You do not need an hour a day, a special diet or an app. You need <b>five minutes</b>, a cue you already have in your day, and a little patience. That is the whole idea of this workbook.'),
          P('Over six weeks you will add one tiny habit at a time. Each one targets a different link in the memory chain: <b>sleep</b> (where memories settle), <b>attention</b> (how they get in), <b>movement</b> (how your brain feels while it works), <b>retrieval</b> (how you strengthen what you know), <b>encoding</b> (how you tag what matters) and finally a <b>lock-in</b> week that stacks it all into a single Daily Five.'),
          P('You will not be asked to feel guilty, to be perfect or to start again if you miss a day. Habits are built by returning, not by streaks. Where you see a writing space, please use it. Writing things down is part of how this works, and the pages are yours to mark up, tick, cross out and scribble on.'),
          P('At the start you will take a gentle self-check so that you can see where you are. At the end you will repeat it and compare. Most readers find that the comparison alone is encouraging, because it turns a vague worry into something you can actually watch change.')]
    f += Callout('A Promise From Us', 'No shame, no jargon, no miracle claims. If something here does not suit you, change it. The best habit is the one you will actually do.')
    f += [P('Let&rsquo;s begin.', 'lab')]
    pg.append(page('Welcome', f))
    # 4 how it works
    f = H('How This Workbook Works', 'The Five-Minute Formula')
    f += [P('Every habit in this book follows the same three-part recipe. It is deliberately small so that it is easy on your worst day, not only your best one.'),]
    f += Cards([['1. Anchor', 'An existing routine that already happens every day: pouring the first coffee, brushing your teeth, shutting the laptop, parking the car. The anchor is your reminder, so you never have to rely on remembering to remember.'],
                ['2. Tiny Habit', 'A five-minute action (often less) that you do straight after the anchor. You will use the phrase: <i>After I [anchor], I will [tiny habit].</i>'],
                ['3. Celebrate', 'A small, genuine moment of &ldquo;done&rdquo;: a tick on the tracker, a quiet fist-pump, a word of thanks to yourself. Feeling good right after the habit is what teaches your brain to repeat it.']],
               [1.2, 4.6])
    f += [H2('Your Six-Week Map')]
    rows = [['Week', 'Focus', 'Your Tiny Habit']] + [[a, b, c] for a, b, c in WEEKS_OVERVIEW]
    f += Cards(rows, [1, 1.4, 3.4], pad=6)
    f += [H2('Inside Each Week')]
    f += B(['An <b>opener</b> with your habit card and a preparation checklist.',
            'Two <b>learn</b> pages in plain language, plus common traps and fixes.',
            'A <b>planner</b> where you write your anchor and your if-then plans.',
            'Four short <b>practice exercises</b>, then a <b>daily log</b> for all seven days.',
            'A <b>weekly review</b> and a page for questions and notes.'])
    pg.append(page('Welcome', f))
    # 5 contents
    f = H('Contents', 'Where Everything Lives')
    toc = [['Start Here', ''], ['Welcome and How It Works', 'Pages 3 to 4'], ['The Science, In Plain Language', 'Pages 6 to 7'],
           ['Your Baseline Self-Check', 'Pages 8 to 9'], ['When To Talk To A Doctor', 'Page 10'], ['Build Your Routine Map', 'Pages 11 to 13'],
           ['Week 1: Sleep', 'Pages 14 to 27'], ['Week 2: Attention', 'Pages 28 to 41'], ['Week 3: Movement', 'Pages 42 to 55'],
           ['Week 4: Retrieval', 'Pages 56 to 69'], ['Week 5: Encoding', 'Pages 70 to 83'], ['Week 6: Lock-In', 'Pages 84 to 97'],
           ['Final Self-Check', 'Pages 98 to 99'], ['Compare and Reflect', 'Pages 100 to 101'], ['Keep Going', 'Pages 102 to 104'],
           ['Tiny Habits Menu', 'Pages 105 to 108'], ['Memory Slip Log', 'Pages 109 to 112'], ['Twelve-Week Tracker', 'Pages 113 to 114'],
           ['Spaced Recall Planner', 'Pages 115 to 116'], ['Notes and Reflections', 'Pages 117 to 120'], ['Quick Reference', 'Pages 121 to 122'],
           ['Sources and Further Reading', 'Pages 123 to 124'], ['Help and Resources', 'Page 125']]
    data = []
    for a, b in toc:
        if b == '': data.append([Paragraph('<b>%s</b>' % a, S['h2']), ''])
        else: data.append([Paragraph(a, S['body']), Paragraph('' if ebook else b, ParagraphStyle('r', parent=S['body'], alignment=2))])
    t = Table(data, colWidths=[CW*0.68, CW*0.32])
    t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Body'),('LINEBELOW',(0,0),(-1,-1),0.5,RULE),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
                           ('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2)]))
    f += [t]
    pg.append(page('Welcome', f, fill=False))
    # 6 science 1
    f = H('The Science, In Plain Language', 'Part One: Why We Forget')
    f += [P('Memory is not one thing. It is a chain with three main links: <b>encoding</b> (taking something in), <b>storage</b> (keeping it) and <b>retrieval</b> (getting it back when you need it). Everyday forgetting can happen at any link, but the most common culprit is the first one.'),
          P('Psychologist Daniel Schacter calls this &ldquo;absent-mindedness&rdquo;: you did not forget where you put your keys, you never properly registered putting them down because your attention was elsewhere. No amount of &ldquo;memory training&rdquo; helps with something that was never recorded. This is why the second week of this programme is about attention.'),
          P('Several ordinary things make the chain weaker in midlife, and none of them are character flaws:')]
    f += B(['<b>Overload.</b> Work, family, money and a phone that never stops mean your attention is divided most of the day.',
            '<b>Stress and low mood.</b> A worried mind has less room for new information, and stress hormones can interfere with recall.',
            '<b>Sleep.</b> Short or broken sleep reduces attention the next day and gives memories less time to settle overnight.',
            '<b>Hormonal and life changes.</b> Many people notice &ldquo;brain fog&rdquo; during perimenopause and menopause, and other life transitions can also play a part.',
            '<b>Health factors.</b> Some medications, thyroid problems, low vitamin B12, depression, anxiety and untreated sleep apnoea can all affect thinking and memory. This is why checking with a doctor matters when changes are noticeable.',
            '<b>Autopilot.</b> The more routine a day is, the less each moment stands out, so the more easily it blurs together.'])
    f += Callout('Key Idea', 'Most midlife forgetfulness is a signal that your brain is busy, tired or distracted, not that it is failing. Small changes to attention, sleep and routine are a sensible place to start.')
    f += [P('<b>What habits cannot do.</b> No habit in this book can promise to prevent or reverse any disease of the brain. What the research does support is that everyday behaviours such as sleeping well, staying active, paying focused attention and practising recall are linked with better day-to-day thinking, and are good for you for many other reasons too.')]
    pg.append(page('Science', f))
    # 7 science 2
    f = H('The Science, In Plain Language', 'Part Two: Why Tiny Habits Work')
    f += [P('<b>Small is a strategy, not a compromise.</b> Big plans fail on tired days. A five-minute habit is small enough to do when you are ill, late or out of sorts, and doing it on those days is exactly what makes it stick. Behaviour scientist B.J. Fogg builds an entire method around this idea, and it is the backbone of this workbook.'),
          P('<b>Anchors beat willpower.</b> Researchers describe &ldquo;implementation intentions&rdquo;: specific if-then plans such as <i>&ldquo;After I pour my coffee, I will take three slow breaths.&rdquo;</i> Studies reviewed by Peter Gollwitzer suggest that deciding in advance when and where you will act makes follow-through more likely than a general intention to &ldquo;do better.&rdquo;'),
          P('<b>Habits take time, and missing a day is fine.</b> In a well-known study by Phillippa Lally and colleagues, the time for a new behaviour to feel automatic varied widely between people and behaviours, from a few weeks to many months, with a typical figure of around two months. Missing the occasional day did not derail the process. That is why this workbook asks you to <b>never miss twice</b>, instead of never missing.'),
          P('<b>Recalling beats re-reading.</b> Studies on &ldquo;test-enhanced learning&rdquo; by Henry Roediger and Jeffrey Karpicke found that trying to remember something strengthens memory more than reading it again. Spreading practice across days, rather than cramming, helps too. Weeks four and five put these findings to work in daily life.'),
          P('<b>Your environment is part of your memory.</b> Hooks for keys, a basket by the door and a visible planner all move the job of remembering out of your head and into the room. That is not cheating. It is how skilled people work.')]
    f += Callout('How To Read The Rest Of This Book', ['Do the small thing. Tick the box. Notice what changes. Adjust the plan, not yourself.',
                                                        'The six weeks are a starting point. The aim is a handful of habits that fit your life and are still running a year from now.'])
    pg.append(page('Science', f))
    # 8 baseline questionnaire
    f = H('Your Baseline Self-Check', 'Part One: Everyday Memory Questionnaire')
    f += [P('Choose the number that best describes the <b>last month</b>. This is not a test or a diagnosis. It simply gives you a starting point to compare against in week six. Be honest rather than flattering: nobody sees this but you.', 'body'),
          P('<b>0</b> = Never &nbsp;&nbsp; <b>1</b> = Sometimes &nbsp;&nbsp; <b>2</b> = Often &nbsp;&nbsp; <b>3</b> = Very Often', 'small')]
    items = ['I walk into a room and forget why I went there.', 'I misplace keys, my phone, glasses or my wallet.',
             'I forget a person&rsquo;s name soon after hearing it.', 'I struggle to find a familiar word in conversation.',
             'I forget a task or appointment I meant to do.', 'I have to re-read or replay something because my attention drifted.',
             'After an interruption I lose track of what I was doing.', 'I wonder whether I have done something (locked the door, sent the email).',
             'I leave the house without something I meant to take.', 'I open an app or a browser tab and forget what I wanted.',
             'I repeat a story or question to the same person.', 'I feel mentally foggy by mid-afternoon.']
    g = Grid(['#', 'In the last month&hellip;', 'Score'], 12, [0.4, 5.0, 0.8], rowh=33, first=[str(i+1) for i in range(12)])
    tbl = g[0]
    tbl._cellvalues = [list(r) for r in tbl._cellvalues]
    for i, it in enumerate(items):
        tbl._cellvalues[i+1][1] = Paragraph(it, S['cell'])
    f += g
    f += [P('<b>My total (0 to 36):</b> ______ &nbsp;&nbsp; <b>Date:</b> ____________', 'lab'),
          P('A higher number only shows where there is more room to help yourself. It cannot tell you why slips happen. Keep it for comparison.', 'small')]
    pg.append(page('Self-Check', f))
    # 9 baseline recall
    f = H('Your Baseline Self-Check', 'Part Two: Quick Recall Tasks')
    f += [P('These two short tasks give you a feel for your recall today. They are informal and for comparison with yourself only.')]
    f += Callout('Task A: The Ten-Word List', ['<b>Step 1.</b> Read these ten words once, slowly, about two seconds each. Do not write them down or repeat them aloud.',
          '<b>lantern &nbsp;&middot;&nbsp; orchard &nbsp;&middot;&nbsp; button &nbsp;&middot;&nbsp; ribbon &nbsp;&middot;&nbsp; harbour &nbsp;&middot;&nbsp; pillow &nbsp;&middot;&nbsp; bridge &nbsp;&middot;&nbsp; copper &nbsp;&middot;&nbsp; window &nbsp;&middot;&nbsp; sparrow</b>',
          '<b>Step 2.</b> Look away. Spend five minutes on something else, such as making a drink or answering Task B. <b>Step 3.</b> Without looking back, write as many words as you can below.'])
    f += [Fld('Words I remembered', 3, 26), P('Words recalled: ______ out of 10 &nbsp;&nbsp;&nbsp; Date: ____________', 'lab'), sp(6)]
    f += Callout('Task B: Yesterday In Order', 'Without checking your phone or calendar, list the main things you did yesterday, in order, with approximate times. Aim for at least six items.')
    f += [Fld('Yesterday, from morning to night', 6, 24),
          P('Items recalled: ______ &nbsp;&nbsp; <b>How easy was it?</b> 1 = very hard, 5 = very easy: ______', 'lab')]
    pg.append(page('Self-Check', f))
    # 10 when to talk to a doctor
    f = H('When To Talk To A Doctor', 'A Page To Take Seriously')
    f += [P('Everyday slips are common, and this programme is built for them. But some changes deserve a proper check-up, and it is always better to ask than to wonder. Please arrange a medical appointment if you notice any of the following:')]
    f += B(['Memory or thinking has changed <b>suddenly</b>, or has been getting steadily worse over weeks or months.',
            'Slips are getting in the way of daily life: missed bills, getting lost on familiar routes, trouble with tasks you have always done, or repeated questions that others notice.',
            'Friends, family or colleagues have noticed changes in your memory, mood or behaviour, or you have new confusion or difficulty following conversations.',
            'You are very low, anxious, exhausted, or not coping, or you suspect your sleep is badly disturbed (loud snoring, pauses in breathing, extreme daytime sleepiness).',
            'You have recently started or changed a medication, have a health condition that could affect thinking, or are simply worried.'])
    f += Callout('Urgent Symptoms', 'Seek urgent medical help immediately for sudden severe headache, weakness or numbness on one side, slurred speech, sudden vision loss, or sudden confusion. Do not wait to finish a workbook.')
    f += [H2('Prepare For Your Appointment')]
    f += [Fld('What has changed, and since when?', 1, 22), Fld('Medications and supplements I take', 1, 22),
          Fld('Sleep, alcohol, stress and mood in recent weeks', 1, 22), Fld('Questions I want to ask', 1, 22)]
    pg.append(page('Doctor', f))
    # 11 anchors
    f = H('Build Your Routine Map', 'Step One: Find Your Anchors')
    f += [P('An <b>anchor</b> is a steady moment in your day that already happens without you thinking about it. The best anchors are specific, frequent and tied to a place. &ldquo;In the morning&rdquo; is vague. &ldquo;After I switch on the kettle&rdquo; is an anchor.'),
          P('Tick every anchor that happens on most days, then circle the five you trust most.')]
    f += Checks(['I switch off my alarm', 'I make the first drink of the day', 'I brush my teeth (morning)', 'I start the car or board transport',
                 'I arrive at work or sit at my desk', 'I stop for lunch', 'I make an afternoon drink',
                 'I finish work, close the laptop or lock up', 'I begin cooking dinner', 'I finish the evening routine',
                 'I plug in my phone to charge', 'I brush my teeth (evening)'])
    f += [sp(4), Fld('Other anchors I have', 1, 22)]
    f += Callout('Choosing Well', 'Good anchors are things you do <b>every day, in the same place,</b> and that are not easily skipped. A coffee break that happens only on office days is a weaker anchor than brushing your teeth.')
    f += [Fld('My five strongest anchors, and when each happens', 2, 24)]
    pg.append(page('Routine Map', f))
    # 12 daily rhythm
    f = H('Build Your Routine Map', 'Step Two: Your Daily Rhythm')
    f += [P('Sketch a typical weekday. Note when your energy is highest and lowest, when interruptions strike and where five quiet minutes could fit. Different habits suit different parts of the day: calm, low-effort habits (like the wind-down) belong to evenings, and focus habits belong to when you are sharpest.')]
    rows = ['Wake-up', 'Early morning', 'Mid-morning', 'Lunchtime', 'Early afternoon', 'Late afternoon', 'Early evening', 'Late evening', 'Bedtime']
    f += Grid(['Time of Day', 'What I Usually Do', 'Energy (1-5)', 'Free Five Minutes?'], len(rows), [1.5, 3.1, 1.0, 1.3], rowh=36, first=rows)
    f += [Fld('My sharpest time of day, and why I think so', 1, 22), Fld('My most distracted time of day, and why', 1, 22),
          Fld('The three biggest interruptions in my day', 2, 22)]
    pg.append(page('Routine Map', f))
    # 13 why, obstacles, supporters
    f = H('Build Your Routine Map', 'Step Three: Your Reasons And Your Support')
    f += [P('Change is easier when the reason belongs to you. Spend a few minutes on these questions, then come back to this page whenever motivation dips.')]
    f += [Fld('1. What do I most want my memory to do for me? (be specific: names at work, no more lost keys, reading without drifting)', 2, 22),
          Fld('2. What will I notice in daily life if this goes well?', 2, 22),
          Fld('3. What usually gets in the way when I try a new habit?', 2, 22),
          Fld('4. What will I do about that, in plain if-then words?', 2, 22, hint='If ____ happens, then I will ____.'),
          Fld('5. Who can I tell about this, and what would help from them?', 2, 22)]
    f += Callout('My Commitment', ['I will give this six weeks, at five minutes a day. When I miss a day I will simply start again the next day.',
                                  'Signed: ____________________________ &nbsp;&nbsp;&nbsp; Date: ______________'])
    pg.append(page('Routine Map', f))
    return pg
