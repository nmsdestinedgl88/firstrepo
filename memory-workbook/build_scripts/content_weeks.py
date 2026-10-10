from lib import *
from content_front import page, WEEKS_OVERVIEW

W = {}
W[1] = dict(pillar='Sleep', habit='The Five-Minute Wind-Down', tagline='Give today&rsquo;s memories the best chance to settle overnight.',
 recipe=['Right after your evening anchor, put your phone on charge <b>out of arm&rsquo;s reach</b> of the bed.',
         'Write tomorrow&rsquo;s top three tasks and anything circling in your head on one page (the <b>brain dump</b>).',
         'Dim the lights and take six slow breaths, longer out than in.',
         'Tick today&rsquo;s box and say, &ldquo;Done. Tomorrow is planned.&rdquo;'],
 prep=['Choose a charging spot away from the bed', 'Put a notepad and pen where you will see them in the evening', 'Decide a rough lights-out time (a range is fine)', 'Check your lamp or lighting can be dimmed', 'Tell one person you are starting'],
 why=['Sleep is one of the best-supported links between a good day and a good memory. During sleep the brain replays and reorganises what you took in, helping new information settle into long-term memory. A review by Susanne Diekelmann and Jan Born describes this role of sleep in detail.',
      'Short or broken sleep also hits <b>attention</b> the next day, and attention is the doorway through which everything enters memory. Many midlife slips on a bad-sleep day are really attention slips.',
      'A busy mind at bedtime makes sleep harder. A small study from Michael Scullin and colleagues found that people who wrote a to-do list before bed fell asleep a little faster than those who wrote about the day. The finding is modest and needs more research, but offloading tomorrow onto paper costs five minutes and is worth a try.',
      'Aim for a consistent wake-up time, a dark and cool room, and caffeine early in the day. Alcohol can feel like it helps you drift off but tends to disturb sleep later in the night.'],
 trapfix=[('I scroll in bed &ldquo;just for a minute&rdquo;.', 'Charge the phone in another room, and buy a cheap alarm clock.'), ('My mind races at night.', 'Extend the brain dump to a second page, and add a &ldquo;worry window&rdquo; earlier in the evening.'),
          ('Bedtime keeps drifting later.', 'Set an alarm for the <i>start</i> of the wind-down, not bedtime.'), ('I share a room with a partner or children.', 'Do the wind-down in the living room, then move quietly.'),
          ('I snore, wake unrefreshed or feel sleepy in the day.', 'Mention it to your doctor. Sleep problems are common and treatable.')],
 ex=[('My Sleep Snapshot', 'For seven nights, note the basics. You are looking for patterns, not perfection.',
      ['Grid', ['Night', 'Lights Out', 'Woke Up', 'Wake-Ups', 'Last Caffeine', 'Screens Off'], 7, ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
       'What pattern do I notice?']),
     ('Wind-Down Design', 'Pick the cues that will tell your body that the day is ending. Tick three or more and add your own.',
      ['Checks', ['Phone on charge outside the bedroom', 'Lights dimmed 30 minutes before bed', 'Warm shower or wash', 'Same pyjamas or a calming ritual', 'Reading something light (paper or e-ink)', 'Gentle stretching', 'Herbal tea or warm water (no caffeine)', 'Quiet music or a podcast with a timer'],
       'My wind-down in five minutes, step by step']),
     ('The Brain Dump Page', 'Practise the core skill. Empty your head onto the page, then choose what matters tomorrow.',
      ['Sections', ['Tasks I must do', 'Things worrying me', 'Ideas to keep', 'Reminders for others'], 'My top three for tomorrow']),
     ('A One-Week Mini-Experiment', 'Pick one small sleep change for seven days and track the result. Rate each morning from 1 (foggy) to 5 (clear).',
      ['Experiment', 'The change I will try', 'My prediction', 'Mornings rated', 'What I learned'])],
 daily=('Hours slept (approx.)', 'Time I started the wind-down'), qa=[('What if I miss a night?', 'Just do it the next night. One miss changes nothing, and two misses in a row is the signal to restart gently.'),
        ('I work shifts. Does this still work?', 'Yes. Anchor it to the end of your shift or before your main sleep, wherever that falls.'), ('Do I need eight hours?', 'Needs vary. Aim for what leaves you alert most days and discuss persistent problems with a doctor.')])

W[2] = dict(pillar='Attention', habit='One Thing, Out Loud', tagline='Memory starts with paying attention. Make it deliberate for five minutes.',
 recipe=['After your anchor, set a five-minute timer and choose <b>one</b> task.', 'Phone face-down or in another room, one window open, notifications off.', 'Work only on that task until the timer ends.',
         'Once a day, <b>say aloud</b> where you put something down: &ldquo;Keys on the hook.&rdquo; Tick the box.'],
 prep=['Choose your daily task type (email, reading, planning, admin)', 'Find a timer that is not on your phone, or use airplane mode', 'Pick one &ldquo;home&rdquo; for each item you often lose', 'Silence non-essential notifications', 'Tell colleagues or family you may be offline for five minutes'],
 why=['Most everyday forgetting is not storage failure: the information never fully registered. Daniel Schacter calls this absent-mindedness. If your mind is on tomorrow&rsquo;s meeting while you put your glasses down, there is nothing to retrieve later.',
      'Splitting attention has a cost. Eyal Ophir, Clifford Nass and Anthony Wagner found that people who habitually juggle several media streams did worse at filtering out distractions than those who did not. You do not need to give up your phone, only to give yourself short stretches where one thing has your attention.',
      '<b>Saying it aloud</b> works because it forces a moment of attention and adds a second route into memory (hearing yourself). Pair it with a glance at the object and its place, and you have built a mini-memory in two seconds.',
      'Start with five minutes. Attention, like a muscle, responds to short, regular effort better than to occasional marathons.'],
 trapfix=[('The timer feels pointless; five minutes is nothing.', 'Five minutes is the point. Make the habit unmissable, and lengthen later if you wish.'), ('Someone interrupts me.', 'Say, &ldquo;Give me five minutes.&rdquo; Most requests can wait that long.'),
          ('I keep checking my phone.', 'Put it in another room. Out of sight reduces temptation more than willpower does.'), ('I forget to say it aloud.', 'Attach it to one specific object, such as the front-door keys.'),
          ('I feel silly speaking to myself.', 'A whisper counts. You are building a habit, not giving a performance.')],
 ex=[('My Distraction Audit', 'For one day, note each time your attention is pulled away. Patterns reveal easy wins.',
      ['Grid', ['Time', 'What Interrupted Me', 'Source', 'Avoidable?'], 8, None, 'My three biggest distractions, and what I will change']),
     ('Place It, Say It, Picture It', 'Choose five items you often misplace. Give each a permanent home, and practise placing them with attention.',
      ['Grid', ['Item', 'Its Home', 'Placed Aloud?', 'Found It Later?'], 6, None, 'What I notice when I place things on purpose']),
     ('Five-Minute Focus Sprints', 'Log seven sprints. Rate your focus from 1 (scattered) to 5 (locked in).',
      ['Grid', ['Day', 'Task', 'Focus 1-5', 'Interruptions'], 7, ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], 'What helped me focus most?']),
     ('Notification And Phone Reset', 'Tick what you will do this week, then note how it felt.',
      ['Checks', ['Turn off non-essential notifications', 'Move distracting apps off the first screen', 'Keep the phone out of reach during sprints', 'Set grey-scale or do-not-disturb at set times', 'Use a physical alarm clock', 'Create a charging spot away from the desk', 'Agree a &ldquo;reply by&rdquo; time with colleagues', 'Close unneeded browser tabs at day&rsquo;s end'], 'How did it feel, and what changed?'])],
 daily=('Items I placed aloud today', 'Sprint focus rating (1-5)'), qa=[('Do I have to use a timer?', 'A timer makes the five minutes concrete. If you hate them, use a song, or the boil of a kettle.'),
        ('What if my job is all interruptions?', 'Choose a different anchor, such as arriving home, and keep to five minutes.'), ('Is it OK to look at my phone for calls?', 'Absolutely. Set the phone so key people can reach you, and keep everything else quiet.')])

W[3] = dict(pillar='Movement', habit='The Five-Minute Movement Snack', tagline='Wake the brain by moving the body, a few minutes at a time.',
 recipe=['After your anchor, <b>move for five minutes</b>: brisk walk, stairs, marching on the spot, or chair-based movement.', 'As you move, recall your plan for the day, or yesterday, in order, in your head.', 'Notice how you feel afterwards.', 'Tick the box and move on.'],
 prep=['Check you are comfortable with the activity (ask your doctor if unsure)', 'Choose footwear and a safe, easy route', 'Pick an indoor option for bad weather', 'Decide on one chair-based alternative', 'Put your anchor and your route in the planner'],
 why=['Regular physical activity is linked with better cognitive function and overall brain health, and it improves sleep and mood, which in turn help memory. Even brief bouts matter: a meta-analysis by Yu-Kai Chang and colleagues found small positive effects of a single session of exercise on cognitive performance.',
      'You do not need a gym. Five minutes of brisk movement after a long sit raises heart rate, shifts attention and breaks a stuck mood. It is also a perfect anchor for recall: thinking through the day while you walk links movement and memory practice into one habit.',
      'Choose movement you can do on your <b>worst</b> day. A walk to the end of the street counts. So does standing up and marching in place during a call. If you want to do more, wonderful, but never less than the five-minute floor.',
      'People with joint, heart, balance or other health conditions should adapt movements and check with a health professional. The aim is to feel pleasantly warmed up, not exhausted.'],
 trapfix=[('I do not have time.', 'Five minutes fits almost anywhere. Walk while you wait for the kettle, or take the longer route to the car.'), ('It is raining, or I am in the office.', 'Use stairs, a corridor or marching on the spot.'),
          ('I am out of shape.', 'Begin at an easy pace. Comfortable and consistent beats fast and abandoned.'), ('I feel embarrassed.', 'Choose a private spot, or bring a friend. Some of the best habits are shared.'),
          ('I have pain or a health condition.', 'Adapt the movement and take advice from your doctor or physiotherapist.')],
 ex=[('My Movement Menu', 'Tick five movement snacks you could do. Add your own at the bottom.',
      ['Checks', ['Brisk walk around the block', 'Stairs up and down twice', 'Marching on the spot', 'Gentle stretching', 'Chair squats or sit-to-stand', 'Dancing to one song', 'Walking while on a call', 'Carrying the shopping the long way', 'Gardening or housework with intent', 'Chair-based arm and leg movements'], 'My top three, and where each fits in my day']),
     ('Walk And Recall', 'On a walk, recall yesterday in order, aloud or in your head. Afterwards, jot down what you remembered and check it.',
      ['Fields', ['What I remembered about yesterday', 'What I missed, then checked', 'How I felt afterwards']]),
     ('Energy And Focus Tracker', 'Rate before and after a movement snack on six different days. Look for a pattern.',
      ['Grid', ['Day', 'Energy Before', 'Energy After', 'Focus Before', 'Focus After'], 6, None, 'What changes do I notice, if any?']),
     ('Stack Builder', 'Write your movement snack into an if-then plan and design a backup for bad weather or low energy.',
      ['Fields', ['After I (anchor)&hellip;', 'I will move by (activity)&hellip;', 'For five minutes in (place)&hellip;', 'On a wet or low-energy day I will&hellip;'], 'Who could join me, and how will I ask?'])],
 daily=('Minutes I moved today', 'Energy after moving (1-5)'), qa=[('Does five minutes really count?', 'Yes. It builds the habit, and many people find they naturally do more once they have started.'),
        ('What if I already exercise?', 'Great. Keep it, and add this snack as a memory cue after a long sit.'), ('What about recovery days?', 'Do a gentle version: stretching or an easy stroll.')])

W[4] = dict(pillar='Retrieval', habit='Recall Before You Check', tagline='Strengthen what you know by pulling it out, not by looking it up.',
 recipe=['After your anchor, <b>close the notes</b> and write down what you remember: yesterday, today&rsquo;s plan, or a person&rsquo;s name.', 'Then check and correct what you missed.', 'Once or twice a week, use your recall cards (names or facts) on a 1-3-7-day schedule.', 'Tick the box and celebrate the effort, not just the score.'],
 prep=['Choose your daily recall topic (yesterday, tomorrow, a name, a fact)', 'Prepare a pack of index cards or use the planner pages', 'Make a list of five people or facts you want to remember', 'Set a recurring reminder for your review days', 'Decide a place to keep your cards'],
 why=['Re-reading feels productive but is surprisingly weak. In a classic study, Henry Roediger and Jeffrey Karpicke found that people who practised <b>retrieving</b> information remembered more a week later than those who simply studied it again. The effort of pulling something out is what strengthens it.',
      'Spacing helps too. A large review by Nicholas Cepeda and colleagues found that spreading practice across days generally beats cramming it all together. A simple pattern is to review a new item after one day, three days and seven days.',
      'This week is not about memory tricks. It is about practising the real thing: &ldquo;What was her name? What is on today&rsquo;s list?&rdquo; Struggling a little before you look is a feature, not a flaw.',
      'Be kind to yourself. If you forget something during practice, you are exactly where the benefit happens. Check the answer, say it aloud once, and move on.'],
 trapfix=[('I get frustrated when I cannot recall.', 'That struggle is the useful bit. Take a breath, check, and try again tomorrow.'), ('I forget to review.', 'Link review days to anchors, such as Monday coffee and Thursday lunch.'),
          ('I do not know what to practise.', 'Start with yesterday&rsquo;s events and one name a day.'), ('The cards pile up.', 'Retire cards you get right three times in a row.'), ('Someone tests me and I panic.', 'Practise in private first, then in low-pressure settings.')],
 ex=[('Daily Recall Page', 'Without checking, write what you remember from yesterday, then compare with your calendar or messages.',
      ['Fields', ['Yesterday I&hellip;', 'People I spoke to', 'Things I meant to do and did', 'Things I meant to do and missed']]),
     ('Names And Faces Cards', 'List five people whose names you want to hold on to. Add a link: where you met, what they do, an image that fits.',
      ['Grid', ['Name', 'Where Met', 'My Link or Image', 'Review Dates'], 6, None, 'How will I use their name this week?']),
     ('Spaced Recall Practice', 'Write five facts you want to remember. Tick each review as you do it.',
      ['Grid', ['Fact To Remember', 'Day 1', 'Day 3', 'Day 7'], 6, None, 'Which facts stuck? Which slipped?']),
     ('Teach It Back', 'Explain something you learned this week to a friend or write it in your own words. Teaching is a strong form of recall.',
      ['Fields', ['What I learned', 'How I would explain it simply', 'Where I stumbled', 'Who I explained it to']])],
 daily=('What I recalled without checking', 'Review I did today (cards, names or facts)'), qa=[('What counts as practice?', 'Anything where you try to remember before you look: names, plans, facts, the shopping list.'),
        ('Should I keep a streak?', 'Keep a record, but do not worry about perfect streaks. Return quickly after a gap.'), ('What if I forget everything?', 'Then start with one small item, and expect gradual improvement.')])

W[5] = dict(pillar='Encoding', habit='The Three-Second Tag', tagline='Tag what matters in the moment, so you can find it later.',
 recipe=['When you hear a name, park the car or put something down, <b>pause for three seconds</b>.', '<b>Notice</b> it with your full attention, <b>say</b> it (aloud or silently) and <b>link</b> it to a picture, place or meaning.', 'Use the name or fact again within a minute, or write one word in your notebook.', 'At day&rsquo;s end tick the box if you tagged at least one thing.'],
 prep=['Carry a small notebook or use a notes app', 'Choose three situations to tag (new names, parking, where you put things)', 'Practise with three people this week', 'Review last week&rsquo;s recall cards', 'Invent a silly phrase to remind yourself: &ldquo;Notice, say, link.&rdquo;'],
 why=['Memory depends on how deeply you process something when you first meet it. Fergus Craik and Robert Lockhart showed that attending to meaning and connections leads to better remembering than skimming the surface. A name heard once is gone. A name noticed, repeated and linked to a picture is far more likely to stay.',
      '<b>Tags</b> are quick hooks: a vivid image (&ldquo;Rose, who has the red scarf&rdquo;), a link to someone you already know, or a location (&ldquo;Level 3, near the lift&rdquo;). The more personal and unusual the link, the better it tends to work.',
      '<b>Chunking</b> helps with numbers: 0207 946 0123 is easier than ten separate digits. <b>Stories</b> help with lists: link each item to the next in a short, silly story.',
      'None of this requires a special gift. It takes three seconds of attention, a link and a repeat, ideally within a minute of meeting the information.'],
 trapfix=[('I miss the name because I am nervous.', 'Ask them to repeat it: &ldquo;Sorry, I want to get your name right.&rdquo;'), ('My links feel silly.', 'They are meant to be. Silly and personal beats sensible and forgettable.'),
          ('I forget to pause.', 'Tie it to one situation per day, such as a new colleague or parking the car.'), ('I use the name and still forget.', 'Add a written one-word tag in your phone, and review it at day&rsquo;s end.'),
          ('Crowded rooms overwhelm me.', 'Aim for just one or two names. Quality beats quantity.')],
 ex=[('The Name Game', 'Practise on people you will meet this week. Build a link for each name.',
      ['Grid', ['Name', 'What I Noticed', 'My Link or Picture', 'Used It Aloud?'], 6, None, 'Which link worked best, and why?']),
     ('Chunk It', 'Turn long numbers and codes into chunks you can hold. Write three real examples from your life.',
      ['Fields', ['A number I need (phone, code)', 'How I chunked it', 'A date or list I need', 'How I linked it']]),
     ('Story Link', 'Memorise a list of ten items by linking each to the next in a short, vivid story. Use the shopping list or ten errands.',
      ['Fields', ['My ten items', 'My story that links them', 'How many I recalled later (tonight)', 'How many I recalled tomorrow']]),
     ('Parking And Place Tags', 'Practise tagging real-world locations: the car, the bike, the umbrella, the passport.',
      ['Grid', ['Item', 'Where I Put It', 'My Tag', 'Found It?'], 7, None, 'What have I learned about myself as a placer of things?'])],
 daily=('Names or items I tagged today', 'Which tag worked best?'), qa=[('Is it rude to ask someone to repeat their name?', 'Not at all. Most people appreciate the effort.'),
        ('Does this work for numbers?', 'Chunking helps. Linking numbers to dates or images you know helps further.'), ('Can I just write everything down?', 'Notes are great. Tagging helps when you cannot, and it makes your notes more useful.')])

W[6] = dict(pillar='Lock-In', habit='The Daily Five', tagline='Stack your habits into a rhythm that survives real life.',
 recipe=['After your main anchor, do <b>one</b> of your five habits for five minutes: wind-down, one-thing, movement, recall, tag.', 'Rotate by day, or choose the one you need most today.', 'Keep a backup plan for disrupted days.', '<b>Never miss twice.</b> If you miss, return the next day.'],
 prep=['Review your five habits and choose a rotation', 'Mark your anchors for each habit in the planner', 'List events that could disrupt you (travel, illness, deadlines)', 'Prepare backup plans', 'Tell someone how you want to be supported'],
 why=['This week turns practice into routine. Phillippa Lally and colleagues found that the time for a new behaviour to become automatic varied widely, from a few weeks to many months, and that missing the odd day did not derail the process. What mattered was getting back to it.',
      'That is why the Daily Five is flexible. Some days you will do the wind-down, other days a focus sprint, a walk, a recall page or a tag. What matters is that <b>something</b> happens at your anchor each day.',
      'Habits are most fragile during disruption: holidays, illness, new schedules. Decide now what the smallest possible version looks like (&ldquo;two minutes counts&rdquo;) and write it down. Deciding in advance is far easier than deciding in the moment.',
      'Finally, look at the evidence of change. Compare your baseline with your week-six scores, but also notice the small wins: fewer lost keys, an easier day, a name remembered.'],
 trapfix=[('I am tempted to do all five every day.', 'Resist. Five minutes of one habit is the floor. More is a bonus, not the rule.'), ('Life got busy and I missed three days.', 'Do the two-minute version today. Restarting beats waiting for a perfect Monday.'),
          ('I feel bored with it.', 'Swap a habit from the menu at the back of the book.'), ('I lost motivation.', 'Re-read your reasons on the Routine Map page.'), ('I feel no different.', 'Check your final self-check and slip log. Progress can be quiet.')],
 ex=[('Build My Daily Five', 'Choose which habit goes with which day, and the anchor you will use.',
      ['Grid', ['Day', 'Habit', 'Anchor', 'Backup'], 7, ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], 'What makes this plan realistic for my life?']),
     ('Disruption Plan', 'Write if-then plans for the situations most likely to throw you.',
      ['Fields', ['If I am travelling, then I will&hellip;', 'If I am ill or exhausted, then I will&hellip;', 'If work is overwhelming, then I will&hellip;', 'If I miss two days, then I will&hellip;']]),
     ('Habit Strength Check', 'Rate each statement from 1 (not at all) to 5 (completely) about your main habit.',
      ['Scales', ['I do it without having to think about it', 'I would feel odd if I skipped it', 'I do it even when I am busy or tired', 'It feels like part of my day', 'I would notice if I stopped'], 'My strongest habit so far and why']),
     ('My Proof Page', 'List concrete signs of change, however small, so you can see progress.',
      ['Fields', ['Things I now do that I did not before', 'Slips that happen less often', 'Moments I felt sharper', 'What I am proud of'] ])],
 daily=('Habit I did today', 'Any slip, and what I learned'), qa=[('What if I want to do more than five minutes?', 'Go ahead, but keep five minutes as your non-negotiable floor.'),
        ('Can I change my anchors?', 'Yes. If an anchor is unreliable, replace it. Better a steady anchor than a stubborn plan.'), ('What happens after week six?', 'Keep going with whichever habits worked best, and use the Keep Going section.')])

def week_pages(n):
    d = W[n]; pg = []; sec = 'Week %d: %s' % (n, d['pillar'])
    # 1 opener
    f = H('Week %d: %s' % (n, d['pillar']), 'Your Habit: %s' % d['habit'])
    f += [P('<i>%s</i>' % d['tagline'], 'body')]
    f += Callout('Your Five-Minute Recipe', [('%d. %s' % (i+1, s)) for i, s in enumerate(d['recipe'])])
    f += [H2('Get Ready This Week')]
    f += Checks(d['prep'])
    f += [sp(6), Fld('My anchor for this habit', 1, 24), Fld('When and where I will do it', 1, 24),
          Fld('How I will celebrate when I finish', 1, 24)]
    f += Callout('This Week In One Line', 'Small, steady, specific. If it takes more than five minutes, shrink it.')
    pg.append(page(sec, f))
    # 2 learn
    f = H('Why It Works', 'Week %d: Learn' % n)
    f += [P(t) for t in d['why'][:3]]
    f += Callout('Key Idea', d['why'][3])
    f += [Fld('One thing I want to try from this page', 2, 24), Fld('One thing I am unsure about', 1, 24)]
    pg.append(page(sec, f))
    # 3 tips
    f = H('Common Traps And Fixes', 'Week %d: Learn' % n)
    f += [P('Most people hit at least one of these in the first week. Spot yours in advance, and decide what you will do about it.')]
    rows = [['Trap', 'A Simple Fix']] + [[a, b] for a, b in d['trapfix']]
    f += Cards(rows, [2.5, 3.4], pad=8)
    f += [Fld('The trap I am most likely to fall into', 1, 24), Fld('My if-then answer to it', 2, 24, hint='If ____, then I will ____.')]
    pg.append(page(sec, f))
    # 4 planner
    f = H('Make It Yours: Planner', 'Week %d: Plan' % n)
    f += [P('Write your plan in the sentences below. The more specific you are, the more likely you are to follow through.')]
    f += Callout('My Habit Sentence', ['After I <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> (anchor),',
         'I will <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> (habit) for five minutes.'])
    f += [Fld('Make it obvious: how will I see or hear my cue?', 2, 22), Fld('Make it easy: what will I prepare the night before?', 2, 22),
          Fld('Make it satisfying: how will I celebrate?', 1, 22), Fld('Obstacle 1 and my if-then plan', 1, 22, hint='If ____, then I will ____.'),
          Fld('Obstacle 2 and my if-then plan', 1, 22, hint='If ____, then I will ____.'), Fld('My two-minute backup version', 1, 22),
          Fld('Who will I tell, and how will they help?', 1, 22)]
    pg.append(page(sec, f))
    # 5-8 exercises
    for i, ex in enumerate(d['ex']):
        title, intro, spec = ex
        f = H(title, 'Week %d: Practice %s' % (n, 'ABCD'[i]))
        f += [P(intro)]
        kind = spec[0]
        if kind == 'Grid':
            _, headers, nrows, first, closing = spec
            rowh = 28 if nrows <= 8 else 24
            f += Grid(headers, nrows, [1.2] + [1.4]*(len(headers)-1) if first else [1.7]+[1.5]*(len(headers)-1), rowh=rowh, first=first)
            f += [FillLines(closing, 24)]
        elif kind == 'Checks':
            _, items, closing = spec
            f += Checks(items); f += [sp(6), FillLines(closing, 24)]
        elif kind == 'Sections':
            _, labels, closing = spec
            for l in labels: f += [Fld(l, 3, 22)]
            f += [FillLines(closing, 24)]
        elif kind == 'Experiment':
            f += [Fld(spec[1], 2, 24), Fld(spec[2], 1, 24)]
            f += Grid(['Day', 'Morning Clarity (1-5)', 'Notes'], 7, [1, 2, 4], rowh=26, first=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
            f += [FillLines(spec[4], 24)]
        elif kind == 'Fields':
            for l in spec[1]: f += [Fld(l, 3 if len(spec[1]) <= 4 else 2, 24)]
            if len(spec) > 2: f += [FillLines(spec[2], 24)]
        elif kind == 'Scales':
            for l in spec[1]: f += [Scale(l, 5, 'Not at all', 'Completely'), sp(10)]
            f += [FillLines(spec[2], 24)]
        pg.append(page(sec, f))
    # 9-12 daily logs
    days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
    def day_block(dname):
        b = [Table([[Paragraph('<b>%s</b>' % dname, ParagraphStyle('db', fontName='Body-B', fontSize=14, textColor=WHITE, leading=17)),
                     Paragraph('Date: ____________________', ParagraphStyle('dd', fontName='Body', fontSize=12, textColor=WHITE, leading=15))]],
                   colWidths=[CW*0.35, CW*0.65], style=TableStyle([('FONTNAME',(0,0),(-1,-1),'Body'),('BACKGROUND',(0,0),(-1,-1),GREEN),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),5),('LEFTPADDING',(0,0),(-1,-1),9)])),
             sp(5)]
        b += [Check('I used my anchor today'), Check('I did my five-minute habit'), sp(2)]
        b += [Fld(d['daily'][0], 1, 15), Fld(d['daily'][1], 1, 15)]
        b += [Scale('Energy today', 5, 'Low', 'High'), Scale('Focus today', 5, 'Scattered', 'Sharp')]
        b += [Fld('Memory slip today (what happened?)', 1, 15), Fld('Something I recalled without checking', 1, 15), Fld('My tiny win', 1, 15)]
        return b
    for pi, (a, b) in enumerate([(0, 1), (2, 3), (4, 5), (6, None)]):
        f = [Paragraph('Daily Log: Week %d' % n, S['kicker'])]
        f += day_block(days[a]) + [sp(4)]
        if b is not None: f += day_block(days[b])
        else:
            f += [sp(4), H2('End-Of-Week Check')]
            f += [Scale('How easy was this habit this week?', 5, 'Hard', 'Easy'), Scale('How useful did it feel?', 5, 'Not much', 'Very'),
                  Scale('How confident am I about continuing?', 5, 'Not yet', 'Very'),
                  FillLines('What I notice about myself after a week', 22)]
        pg.append(page(sec, f, tag='print'))
    # 13 weekly review
    f = H('Weekly Review', 'Week %d: Reflect' % n)
    f += [P('Take ten minutes to look back. The point is not to judge, but to learn what to adjust.')]
    f += [Fld('Days I did my habit (out of 7)', 1, 22), Fld('What worked best this week?', 2, 22), Fld('What got in the way?', 2, 22),
          Fld('Memory slips this week, and any pattern I notice', 2, 22)]
    f += [H2('Decide'), Check('<b>Keep</b> it as it is'), Check('<b>Tweak</b> it (what will I change?)'), Check('<b>Swap</b> it for something easier'), sp(4)]
    f += [Fld('My plan for next week', 2, 22), Fld('A note to my future self', 1, 22), Check('<b>Week complete. I celebrated.</b>')]
    pg.append(page(sec, f))
    # 14 Q&A + notes
    f = H('Questions And Notes', 'Week %d: Reflect' % n)
    f += Cards([['Question', 'Answer']] + [[q, a] for q, a in d['qa']], [2.0, 3.9], pad=8)
    f += [FillLines('Notes, doodles and questions for later', 24)]
    pg.append(page(sec, f, tag='print'))
    return pg
