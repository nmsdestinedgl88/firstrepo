from lib import *
from content_front import page
from content_weeks import W

Q_ITEMS = ['I walk into a room and forget why I went there.', 'I misplace keys, my phone, glasses or my wallet.',
           'I forget a person&rsquo;s name soon after hearing it.', 'I struggle to find a familiar word in conversation.',
           'I forget a task or appointment I meant to do.', 'I have to re-read or replay something because my attention drifted.',
           'After an interruption I lose track of what I was doing.', 'I wonder whether I have done something (locked the door, sent the email).',
           'I leave the house without something I meant to take.', 'I open an app or a browser tab and forget what I wanted.',
           'I repeat a story or question to the same person.', 'I feel mentally foggy by mid-afternoon.']

def questionnaire_grid(f):
    g = Grid(['#', 'In the last month&hellip;', 'Score'], 12, [0.4, 5.0, 0.8], rowh=33, first=[str(i+1) for i in range(12)])
    tbl = g[0]; tbl._cellvalues = [list(r) for r in tbl._cellvalues]
    for i, it in enumerate(Q_ITEMS): tbl._cellvalues[i+1][1] = Paragraph(it, S['cell'])
    return f + g

def menu_page(title, kicker, pillar, items):
    f = H(title, kicker)
    f += [P('Tick the ones you want to try. Each takes five minutes or less. Swap one in whenever a habit stops working or starts to feel stale.')]
    rows = [[BoxF(), Paragraph('<b>%s</b><br/>%s' % (a, b), S['cell'])] for a, b in items]
    t = Table(rows, colWidths=[28, CW - 28])
    t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'Body'),('LINEBELOW',(0,0),(-1,-1),0.5,RULE),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LEFTPADDING',(0,0),(-1,-1),2)]))
    f += [t]
    return page('Tiny Habits Menu', f)

def back_pages():
    pg = []
    # 98-99 final self-check
    f = H('Your Final Self-Check', 'Part One: Everyday Memory Questionnaire')
    f += [P('Repeat the questionnaire from week zero, again thinking about the <b>last month</b>. Answer honestly and do not look back at your first answers until you have finished.'),
          P('<b>0</b> = Never &nbsp;&nbsp; <b>1</b> = Sometimes &nbsp;&nbsp; <b>2</b> = Often &nbsp;&nbsp; <b>3</b> = Very Often', 'small')]
    f = questionnaire_grid(f)
    f += [P('<b>My total (0 to 36):</b> ______ &nbsp;&nbsp; <b>Date:</b> ____________', 'lab')]
    pg.append(page('Final Self-Check', f))
    f = H('Your Final Self-Check', 'Part Two: Quick Recall Tasks')
    f += Callout('Task A: A New Ten-Word List', ['<b>Step 1.</b> Read these ten words once, slowly, about two seconds each.',
          '<b>compass &nbsp;&middot;&nbsp; blanket &nbsp;&middot;&nbsp; meadow &nbsp;&middot;&nbsp; hammer &nbsp;&middot;&nbsp; candle &nbsp;&middot;&nbsp; lemon &nbsp;&middot;&nbsp; river &nbsp;&middot;&nbsp; mirror &nbsp;&middot;&nbsp; saddle &nbsp;&middot;&nbsp; pepper</b>',
          '<b>Step 2.</b> Spend five minutes on something else, such as Task B. <b>Step 3.</b> Write as many words as you can, without looking back.'])
    f += [Fld('Words I remembered', 3, 26), P('Words recalled: ______ out of 10 &nbsp;&nbsp;&nbsp; Date: ____________', 'lab'), sp(6)]
    f += Callout('Task B: Yesterday In Order', 'Without checking your phone or calendar, list the main things you did yesterday, in order, with approximate times. Aim for at least six items.')
    f += [Fld('Yesterday, from morning to night', 6, 24), P('Items recalled: ______ &nbsp;&nbsp; <b>How easy was it?</b> 1 = very hard, 5 = very easy: ______', 'lab')]
    pg.append(page('Final Self-Check', f))
    # 100-101 compare
    f = H('Compare And Reflect', 'Then And Now')
    f += [P('Fill in the first two columns from your baseline pages (8 and 9) and your final self-check (98 and 99). A lower questionnaire score and a higher recall score both suggest improvement, but treat the numbers as a conversation starter rather than a verdict. Day-to-day variation is normal.')]
    f += Grid(['Measure', 'Baseline', 'Final', 'Change'], 4, [3.2, 1.2, 1.2, 1.2], rowh=36,
              first=['Questionnaire total (0-36, lower is fewer slips)', 'Ten-word recall (out of 10)', 'Items recalled from yesterday', 'How easy yesterday&rsquo;s recall felt (1-5)'])
    f += Callout('Reading Your Results', ['A difference of one or two points is within normal day-to-day variation, so do not over-read it. Look at the whole picture: slips, effort, mood and confidence.', 'If your numbers got worse, or you feel concerned, consider the doctor page again. Habits help, but they are not a substitute for a check-up.'])
    f += [Fld('What I notice when I compare them', 3, 24), Fld('The slip that has improved the most', 1, 24), Fld('The slip that still bothers me', 1, 24)]
    pg.append(page('Compare And Reflect', f))
    f = H('Compare And Reflect', 'Rate The Six Habits')
    f += [P('Think back over the six weeks and rate each habit. This tells you what to keep, what to adapt and what to leave behind.')]
    for n in range(1, 7):
        f += [Scale('Week %d: %s (ease)' % (n, W[n]['habit']), 5, 'Hard', 'Easy'), Scale('Week %d (usefulness)' % n, 5, 'Not much', 'Very')]
    f += [sp(4), Fld('My top two habits to keep', 1, 22), Fld('A habit to adapt, and how', 1, 22)]
    pg.append(page('Compare And Reflect', f))
    # 102-104 keep going
    f = H('Keep Going', 'Your Long-Term Plan')
    f += [P('Six weeks is a start. The aim is a small set of habits that still run in a year. Decide what continues, and tie each habit to its anchor.')]
    f += Grid(['Habit', 'Keep, Swap Or Drop?', 'Anchor', 'Backup'], 6, [2.2, 1.4, 1.8, 1.8], rowh=36, first=[W[n]['habit'] for n in range(1, 7)])
    f += [Fld('My Daily Five rotation in one sentence', 1, 24), Fld('When I will review this plan again (date)', 1, 24), Fld('What will help me keep going?', 2, 24)]
    pg.append(page('Keep Going', f))
    f = H('Thirty-Day Calendar', 'Keep Going')
    f += [P('Tick or colour each day you complete your five minutes. A day with just the two-minute version still counts.')]
    f += Grid(['Week', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 5, [1, 1, 1, 1, 1, 1, 1, 1], rowh=60, first=['1', '2', '3', '4', '5'])
    f += [FillLines('How the month is going', 24)]
    pg.append(page('Keep Going', f))
    f = H('Never Miss Twice', 'Keep Going')
    f += [P('Missing a day is not failure, and it does not undo your progress. The single most helpful rule is to <b>return the very next day</b>, even in a smaller form. Write your relapse plan now, while you feel good.')]
    f += [Fld('Situations that usually derail me', 2, 24), Fld('The smallest version of my habit (two minutes or less)', 1, 24),
          Fld('If I miss a day, then I will&hellip;', 1, 24), Fld('If I miss two days, then I will&hellip;', 1, 24),
          Fld('A reminder of why this matters to me', 2, 24), Fld('Someone I can tell when I wobble', 1, 24)]
    f += Callout('A Reminder', 'You are not starting from zero. Everything you tried in the last six weeks is still in you, and each return is practice at returning.')
    pg.append(page('Keep Going', f))
    # 105-108 menu
    menu = [
     ('Sleep And Wind-Down Habits', 'Menu One', 'Sleep', [
      ('Phone parking', 'Put your phone on charge outside the bedroom as the last act of the day.'), ('Tomorrow list', 'Write tomorrow&rsquo;s top three tasks before bed.'),
      ('Lights low', 'Dim the lights in your home half an hour before bed.'), ('Breathe out slowly', 'Take six slow breaths, longer on the way out.'),
      ('Caffeine curfew', 'Pick a cut-off time for caffeine and stick to it for a week.'), ('Fixed wake time', 'Get up at the same time every day, even weekends, give or take half an hour.'),
      ('Morning light', 'Step outside or sit by a window for five minutes in the morning.'), ('Cool, dark room', 'Check the bedroom is cool, dark and quiet before you get in.'),
      ('Gratitude line', 'Write one thing that went well today.'), ('Screen-free page', 'Read paper or e-ink for five minutes instead of scrolling.')]),
     ('Attention And Focus Habits', 'Menu Two', 'Attention', [
      ('Single-task sprint', 'Set a timer and work on one task only.'), ('Notifications off', 'Silence one noisy app for a week.'),
      ('Say it aloud', 'Say where you put something as you put it down.'), ('Tab trim', 'Close every tab you do not need before you stand up.'),
      ('Eyes-up pause', 'Look out of a window for 30 seconds between tasks.'), ('Mindful sip', 'Drink your first coffee or tea with no screen.'),
      ('Two-minute tidy', 'Clear your desk or entry table before you leave it.'), ('Parking note', 'Photograph or write where you left the car.'),
      ('Meeting minute', 'Write one sentence of what you want from a meeting before it starts.'), ('Phone-free meal', 'Eat one meal a day without a screen.')]),
     ('Movement And Energy Habits', 'Menu Three', 'Movement', [
      ('Stairs only', 'Take the stairs in one place every day.'), ('Call walk', 'Walk during one phone call a day.'),
      ('Doorway stretch', 'Stretch each time you pass through a doorway.'), ('Kitchen squats', 'Do five sit-to-stands while the kettle boils.'),
      ('Dance break', 'Move to one favourite song.'), ('Lunch lap', 'Take a five-minute loop after you eat.'),
      ('Park far', 'Park further away, or get off one stop early.'), ('Posture reset', 'Roll your shoulders and stand tall each hour.'),
      ('Evening saunter', 'Take a gentle walk after dinner.'), ('Weekend wander', 'Choose one longer walk on a weekend day.')]),
     ('Recall And Encoding Habits', 'Menu Four', 'Retrieval', [
      ('Yesterday replay', 'Recall yesterday in order, then check.'), ('Name recap', 'Say the names of people you met today before bed.'),
      ('Shopping list first', 'Recall your shopping list from memory, then check it.'), ('Teach one thing', 'Explain something you learned today to someone else.'),
      ('Number chunk', 'Learn one phone number or code by chunking it.'), ('Route recall', 'Picture the route you took today, in order.'),
      ('Word of the day', 'Learn one new word and use it three times.'), ('Story link', 'Link five items into a vivid little story.'),
      ('Three things', 'Recall three things you read or heard today.'), ('Review a card', 'Check one name or fact on a 1-3-7-day schedule.')])]
    for t, k, p, items in menu: pg.append(menu_page(t, k, p, items))
    # 109-112 slip log
    for i in range(4):
        f = H('Memory Slip Log', 'Page %d Of 4' % (i+1))
        if i == 0: f += [P('Slips are information, not failure. Jot down what happened and what was going on. After a few weeks, patterns often appear: the same time of day, the same stressor, the same kind of task.')]
        f += Grid(['Date', 'What I Forgot Or Lost', 'What Was Going On?', 'What Might Help'], 12 if i == 0 else 13, [0.9, 2.2, 2.0, 1.9], rowh=34 if i == 0 else 36)
        pg.append(page('Memory Slip Log', f, tag='print'))
    # 113-114 trackers
    f = H('Twelve-Week Habit Tracker', 'Keep Your Streak Honest')
    f += [P('Colour in a box for each day you did your five minutes. Fill the last column with a one-word note.')]
    f += Grid(['Week', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Note'], 12, [0.7, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 1.5], rowh=38, first=[str(i+1) for i in range(12)])
    pg.append(page('Trackers', f, tag='print'))
    f = H('Month-By-Month Check-In', 'Keep Your Streak Honest')
    f += [P('Once a month, pause and take stock. What has changed? What needs adjusting? What are you proud of?')]
    for m in ['Month One', 'Month Two', 'Month Three']:
        f += [H2(m), Fld('What is going well', 1, 22), Fld('What needs adjusting', 1, 22), Scale('Overall confidence', 5, 'Low', 'High')]
    f += [FillLines('A word to my future self', 22)]
    pg.append(page('Trackers', f, tag='print'))
    # 115-116 spaced recall planner
    for i in range(2):
        f = H('Spaced Recall Planner', 'Page %d Of 2' % (i+1))
        if i == 0: f += [P('Write each name or fact you want to keep. Review it after 1, 3, 7 and 14 days. Tick each review when done, and retire the item when you get it right three times in a row.')]
        f += Grid(['Name Or Fact', 'Date Learned', 'Day 1', 'Day 3', 'Day 7', 'Day 14'], 11 if i == 0 else 12, [3.0, 1.2, 0.8, 0.8, 0.8, 0.8], rowh=38)
        pg.append(page('Spaced Recall', f, tag='print'))
    # 117-120 notes
    prompts = [('My Attention Notes', ['When is my attention strongest?', 'What drags it away?', 'What small change helped?']),
               ('My Body And Energy Notes', ['How does sleep change my day?', 'What does movement do for my focus?', 'What do I want to protect?']),
               ('My Environment Notes', ['Which homes for objects work?', 'What reminders help most?', 'What should I move or remove?']),
               ('A Letter To My Future Self', ['Dear me, in six months&hellip;'])]
    for t, ps in prompts:
        f = H(t, 'Notes And Reflections')
        for p_ in ps[:-1]: f += [Fld(p_, 4, 24)]
        f += [FillLines(ps[-1], 24)]
        pg.append(page('Notes', f, tag='print'))
    # 121-122 quick ref
    f = H('Quick Reference', 'The Daily Five At A Glance')
    rows = [['Habit', 'The Five-Minute Recipe', 'Anchor Ideas']]
    rows += [['Wind-Down', 'Phone away, brain dump, six slow breaths.', 'Brushing teeth, plugging in phone'],
             ['One Thing, Out Loud', 'Timer, one task, say where things go.', 'First coffee, sitting at desk'],
             ['Movement Snack', 'Five minutes of brisk movement, recall as you go.', 'After lunch, before the school run'],
             ['Recall Before You Check', 'Write what you remember, then check.', 'Kettle on, commuting, lunchtime'],
             ['Three-Second Tag', 'Notice, say, link. Use it within a minute.', 'Meeting someone, parking, putting down keys']]
    f += Cards(rows, [1.6, 2.7, 2.0], pad=7)
    f += [H2('If-Then Templates')]
    f += B(['After I <b>[anchor]</b>, I will <b>[five-minute habit]</b> in <b>[place]</b>.', 'If I miss a day, then I will <b>do the two-minute version tomorrow</b>.',
            'If I feel too tired, then I will <b>do just one breath and tick the box</b>.', 'If I am travelling, then I will <b>do the habit at the hotel or station</b>.',
            'If something interrupts me, then I will <b>resume the moment it ends</b>.'])
    f += Callout('Remember', 'Small, specific and steady beats big and brief. Five minutes, every day you can, and back on track the day after you cannot.')
    pg.append(page('Quick Reference', f))
    f = H('Memory Tricks At A Glance', 'Quick Reference')
    rows = [['Trick', 'How It Works', 'Best For']]
    rows += [['Notice, Say, Link', 'Give a name or fact your full attention for three seconds, say it, link it to a picture.', 'Names, facts, new information'],
             ['Place It, Say It, Picture It', 'Put things in the same home, say where as you place them, and picture it.', 'Keys, glasses, phone, wallet'],
             ['Chunking', 'Break long strings into small groups.', 'Phone numbers, codes, dates'],
             ['Story Link', 'Link each item to the next in a vivid story.', 'Lists, errands, speeches'],
             ['Spaced Recall', 'Review after 1, 3, 7 and 14 days, recalling before you look.', 'Anything you want to keep'],
             ['Brain Dump', 'Empty your head onto paper before bed.', 'Racing thoughts, tomorrow&rsquo;s plan'],
             ['Never Miss Twice', 'Return the day after a miss, even in a tiny form.', 'Keeping habits alive']]
    f += Cards(rows, [1.5, 3.2, 1.7], pad=7)
    f += Callout('Habits Beat Tricks', 'Tricks help in the moment. Habits make them automatic. Keep using both.')
    f += [FillLines('My own tricks', 24)]
    pg.append(page('Quick Reference', f))
    # 123-124 sources
    f = H('Sources And Further Reading', 'Part One')
    f += [P('These are the main studies and books behind the ideas in this workbook. They are listed so that you can read further. Research evolves, and the plain-language summaries here are simplified, so please consult the originals before relying on any detail.', 'small')]
    src1 = ['Craik, F. I. M., &amp; Lockhart, R. S. (1972). Levels of processing: A framework for memory research. <i>Journal of Verbal Learning and Verbal Behavior, 11</i>(6), 671-684.',
            'Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., &amp; Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. <i>Psychological Bulletin, 132</i>(3), 354-380.',
            'Chang, Y. K., Labban, J. D., Gapin, J. I., &amp; Etnier, J. L. (2012). The effects of acute exercise on cognitive performance: A meta-analysis. <i>Brain Research, 1453</i>, 87-101.',
            'Diekelmann, S., &amp; Born, J. (2010). The memory function of sleep. <i>Nature Reviews Neuroscience, 11</i>(2), 114-126.',
            'Fogg, B. J. (2020). <i>Tiny Habits: The Small Changes That Change Everything.</i> Houghton Mifflin Harcourt.',
            'Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans. <i>American Psychologist, 54</i>(7), 493-503.']
    for s in src1: f += [Paragraph(s, S['bul'], bulletText='•'), sp(3)]
    pg.append(page('Sources', f))
    f = H('Sources And Further Reading', 'Part Two')
    src2 = ['Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., &amp; Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. <i>European Journal of Social Psychology, 40</i>(6), 998-1009.',
            'Ophir, E., Nass, C., &amp; Wagner, A. D. (2009). Cognitive control in media multitaskers. <i>Proceedings of the National Academy of Sciences, 106</i>(37), 15583-15587.',
            'Roediger, H. L., &amp; Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. <i>Psychological Science, 17</i>(3), 249-255.',
            'Schacter, D. L. (2001). <i>The Seven Sins of Memory: How the Mind Forgets and Remembers.</i> Houghton Mifflin.',
            'Scullin, M. K., Krueger, M. L., Ballard, H. K., Pruett, N., &amp; Bliwise, D. L. (2018). The effects of bedtime writing on difficulty falling asleep: A polysomnographic study comparing to-do lists and completed activity lists. <i>Journal of Experimental Psychology: General, 147</i>(1), 139-146.']
    for s in src2: f += [Paragraph(s, S['bul'], bulletText='•'), sp(3)]
    f += Callout('A Note On Evidence', 'This workbook does not claim that any habit prevents or reverses memory disease. It uses well-established findings about attention, sleep, practice and habit formation to help with everyday forgetfulness.')
    f += [FillLines('Notes on what I want to read next', 22)]
    pg.append(page('Sources', f))
    # 125 help
    f = H('Help And Resources', 'When You Want More Support')
    f += [P('If your memory worries you, a conversation is the best next step. Start with your family doctor, practice nurse or a pharmacist. In many countries a national health service website or a dementia or ageing charity offers plain-language information and helplines, and your doctor can point you to what is available where you live.'),
          P('If you feel overwhelmed, very low, or unsafe, please reach out right away to a doctor, a trusted person or your local emergency or crisis service.')]
    f += [H2('My Contacts')]
    f += [Fld('My doctor or clinic', 1, 24), Fld('My pharmacist', 1, 24), Fld('My support person', 1, 24), Fld('A local service or helpline I can use', 1, 24)]
    f += Callout('Take Someone With You', 'If you do book an appointment about your memory, it often helps to bring a trusted friend or family member who can add what they have noticed.')
    f += [FillLines('Notes', 22)]
    pg.append(page('Help', f))
    # 126 notes page
    f = H('Notes And Doodles', 'Space For Whatever You Need')
    f += [FillLines(None, 26)]
    pg.append(page('Notes', f, tag='print'))
    # 127 closing letter
    f = H('A Closing Note', 'You Did This')
    f += [P('Whatever your numbers say, you gave your memory a gentle, regular, practical push for six weeks. You paid attention to sleep, moved a little more, practised recall and learned to tag what matters. That is the work of caring for your mind, and it was worth the five minutes.'),
          P('Memory is not a single skill that sits in one place and either works or does not. It is the sum of many small daily conditions: rest, focus, movement, practice and a life that is not asking you to hold everything in your head at once. You have now got tools for all of them.'),
          P('Keep the habits that serve you and quietly drop the ones that do not. Come back to this book on busy weeks. Share it with a friend who keeps losing their keys. And if something worries you, ask a professional. That is not a failure of habits. It is part of looking after yourself well.'),
          P('Thank you for spending these weeks with us. We hope you remember how good it feels to keep a promise to yourself.'), sp(10),
          P('With warm wishes,', 'body'), P('<b>Cimple Books</b>', 'lab')]
    f += Callout('Keep Going', 'Pick your Daily Five rotation, check your anchors, and tick today&rsquo;s box.')
    pg.append(page('Closing', f, label='My Promise To Myself'))
    # 128 about
    f = H('About Cimple Books', 'Thank You')
    f += [P('Cimple Books creates practical workbooks and guides for everyday life: clear, usable and honest about what they can and cannot do.'),
          P('If this workbook helped you, one of the most useful things you can do is leave an honest review on the store where you bought it. A few sentences about what you tried and what you noticed helps other readers decide whether it is right for them.'),
          P('Find more from Cimple Books at <b>www.cimpledigital.com/books</b>.')]
    f += Callout('A Quick Reminder', 'This workbook is not medical advice. If you are worried about your memory, please talk to your doctor.')
    f += [FillLines('A sentence about what I will keep doing', 24)]
    pg.append(page('About', f))
    return pg
