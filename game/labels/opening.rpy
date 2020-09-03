label opening:

    # opening scene: basically same as other game, just tuned up. maybe can be skipped?
    # because we should only see this scene on starting a new game, we need to reset the game started variable, then force the game to restart so it runs init again. Right?
    # Test: We're going to populate all our bios here so it only happens when the game begins, rather than at init time.

    python:

        # This section of code is designed to update some stuff in the biographies that kept breaking when I did it at init. Seems to work.
        for i in allBios:
            i.font = allFonts[i.idNum]
            i.fontColor = allColors[i.idNum]
            i.love = 0  # reset love on new game start
        # go ahead and set up Fontaine's font.
        fontBio.font = fontEntity
        fontBio.fontColor = colorEntity
        # namePlaets
        for i in allBios:
            i.bioEyes = allPlates[i.idNum]

        fontBio.bioEyes = bioEyesFont

        # declare the history variables. Note: most of this won't actually be set in stone until later. Also, each of these histories will be re-declared when they're collected so as to collect the history correctly

        histBoxX = initialBoxX
        histBoxY = initialBoxY  # x and y are just guesses for now

        for i in range(0, 8):
            temp = History(i, histBoxX, histBoxY, [],
                           chatTitles[i], chatRecaps[i])

            histBoxY += histBoxHeight + boxMarginY
            histories.append(temp)

        histBoxX = initialBoxX
        histBoxY = initialBoxY  # x and y are just guesses for now
        histBoxX += histBoxWidth + boxMarginX

        for i in range(8, 17):
            temp = History(i, histBoxX, histBoxY, [],
                           chatTitles[i], chatRecaps[i])
            histBoxY += histBoxHeight + boxMarginY
            histories.append(temp)

        #reset lots of variables for new game.
        kylieSevered = False
        lichClonked = False

    # end python block.
    pause 1.0
    show image splashChoice with dissolve
    nvl hide

    pause 9.0

    scene bg black

    pause 1.0

    "It's not what you said."

    "It's how you said it."

    "I'm not stupid."

    "You didn't say that, but it's how you said what you said."

    "It's just the look on your face."

    play music ringRejection fadein 2.0

    "It doesn't matter what you think you mean or how you think you said it."

    "... these are why I would rather just play video games. Dealing with people is hard. I don't have the right interface."

    "Somehow I ended up here anyway."

    scene bg resta
    with fade

    "Trying to figure out how to turn down a wedding ring."

    show d 1a at f12

    "His face is earnest. He means it when he tells me he'll be there forever."

    "It's like firecrackers going off in my head, but somehow also in my stomach."

    d "Sophia Kylie Koenig, will you -"

    "It's now or never."

    s "David I care about you, I love you, but I-"

    show d 1g

    "Damn everything about this."

    "His eyes are widening. He's starting to shiver. He knows."

    s "I can't."

    "Across the restaurant, the pianist's fingers dance beautifully across ebony and ivory."

    "For a moment her eyes land on us, but only for a moment."

    d 1b "I... okay, but, what?"

    "Even now, his reaction is endearing."

    s "Because we can't communicate. Not even on a basic level. And you don't trust me."

    "Jesus Christ, self, could you let him down a little easier?"

    d 1g "I know sometimes I misinterpret what you're saying-"

    s "All the time, David. All the time, every time. It doesn't matter what I say."

    "Of course it matters. Hyperbole is just... easier."

    d 1b "I don't know what to say."

    "Neither do I."

    "There's a woman moving among tables, coiffed and exotic, speaking briefly with each table. Must be the manager. A thick, musical accent."

    "That's something else I haven't told him."

    d 1g "Say something."

    s "I'm not giving up my work. You're already too jealous about it and I love doing it so-"

    d "You love people online that call you a whore and wish you would die of space herpes? Seriously?"

    "He's getting angry. I understand, so I'm going to forgive some of the brunt of this."

    s "You take the good with the bad."

    d "You're going to pick a hobby over us?"

    s "It's not just a hobby. I make money, David. If you... if you..."

    "Breathe. Just say it."

    s "If you love me and care about me you wouldn't ask me to give up something I love doing."

    "He's quiet now. Shocked silent, I guess. There're a couple of door guards watching us now."

    "One of them, a short-haired woman in a vest and polo, wears a pained expression. I guess her hearing's pretty good."

    d 1b "So that's it then."

    s "That's what?"

    d "We.... I guess we break up now, right?"

    s "Why?"

    "Shit."

    d 1s "What do you mean, why?"

    s "Just because we disagree here doesn't mean we have to end it. We can compromise. I just don't want to sign a contract while -"

    d 1g "You see us getting married as a legal issue?"

    "There it is again. That's not what I meant."

    s "David, I don't mean anything legal, I just mean... I don't know."

    "But maybe we should? Just... end it. I can free him, right now. He's young enough that he could find someone else."

    d 1b "It's pretty hypocritical of you to be worried about things being legal."

    s "David. Don't."

    d 1b "I never, ever saw you as a burden or an obstacle. Ever. I just worry-"

    s "That I'll cheat on you with some Internet teenager?"

    d 1g "- that someone will find you some day, Sophie!"

    s "I can take care of myself!"

    "We're shouting now. Good times. Great times. The bouncer is heading over. It wasn't supposed to-"

    d 1b "I know that, but these guys -"

    s "They're not all guys, you know."

    pause 1.0

    "Quietly, before I could stop them, those words tumble out."

    d "So you're gay now?"

    "He's angry. Forgive him. Shouldn't have been a smartass."

    s "David-"

    d 1g "You know what? Fine."

    stop music fadeout 3.0

    d "Be a her in a d ct. Go righ ba k. I'm go na m v   t  f th hous  . You'll n  er have to wo  y ab  t    again."

    # she has a seizure
    # VFX

    "Oh. Oh no. No no no no no not now."

    hide d at f12

    "My arms pin themselves to my sides as my leg muscles lose all semblance of tension. There’s a sensation of impact when I hit the ground, but no accompanying pain."

    "Warmth blooms on my tongue and lips."

    "Vaguely, I hear voices around me. Something moves me. It’s always the same. I’m falling. Falling, and falling, while the ghosts of whatever was around me slide from side to side."

    "He’s not there for me this time. He’s not there to tell everyone what’s happening, to tell them not to crowd me, that the seizure will stop on its own."

    "He’s not there to tell me how long I lay writhing on the floor, how much time was stolen."

    "He’s not there."

    "It's my fault."

    "I should've tried harder."

    scene bg black
    with longFade

    pause 2.0

    jump common1
