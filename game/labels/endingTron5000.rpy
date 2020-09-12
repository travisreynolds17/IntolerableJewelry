

label endingTron5000:
    # routes based on if entity is severed, routed according to who else is severed.

    # show oblivion
    play music fountainWater
    show f 1a at f12
    o "Ladies."

    show l 1d at fr13

    l "Bitch."

    "Tania snorts, covers her mouth to hide her laughter."

    show c 1k at fl11

    $chat.addmessage(elsa, "There's just no stopping the narrator.")

    o 1l "Are we r-r-rready for the next cycle?"

    

    c "Why are you asking any of us except Kylie? We know damn well there's no choice."

    o 1j "Fair."

    if notReady > 6:
        pause 1.0
        o 1d "Dearest Cassandra, we would not want to waste your time."
        o 1m "Lovely Kylie wasn't ready [notReady] times last time I allowed her a choice."
        k "... I'm not sure I had a lot of control over that."
        pause 1.0
        o 1k "No. Obviously not."

    o 1m "Kylie, sweet lovely Kylie."

    o "We are curious. Did you... truly come to love any of them?"

    pause 1.0
    $temp = True
    while temp:
        menu:
            "Cassandra" if cassBio.love >= 4:
                $loveConfession = "Cassandra"
                c 2b "Kylie..."
                o 1a "Isn't that interesting... and yet, only we love you best."
                $temp = False
            "Lichelle" if lichBio.love >= 4:
                $loveConfession = "Lichelle"
                l "Babe..."
                o 1a "Isn't that interesting... she seemed so untouchable at first."
                $temp = False
            "Robin" if robinBio.love >= 4:
                $loveConfession = "Robin"
                o 1a "we loved her, as well. Such a pity. So sad."
                k "... Fontaine. Is that true?"
                pause 1.0
                o 1c "Yes."
                k "..."
                o 1n "We loved her with all of our hearts!"
                $persistent.loveRobin = True
                $temp = False
            "Tania" if taniaBio.love >= 4:
                $loveConfession = "Tania"
                t "I'm... not worth your affection, Kyles."
                o 1a "Isn't that interesting... Tania, we love you, too!."
                $temp = False
            "You, Fontaine" if fontBio.love >= 4 and loveConfession != "Fontaine":
                play audio heart noloop
                pause 1.0
                o 1k "Huh?"
                l "The hell, Kylie?"
                t "... I was afraid of that."
                c "..."
                pause 1.0
                o "We..."
                o "You think you... well. We, no, no, and no."
                k "... I can't even comprehend you."
                o 1m "True! We—"
                k "I'm coming apart even thinking about what you might be."
                k "... it's..."
                play audio heart noloop
                k "It's exhilarating..."
                t 1b "... come back, Kylie."
                o 1o "..."
                c 1b "Don't let her sway you!"
                l 1c "Fight back, babe."
                o 1c "... we are beyond such things."
                play audio heart noloop
                k "I don't believe that. You created an entire world for us."
                k "Even if it doesn't make sense, even if it's some senseless theatrical production."
                o 1d "Fool."
                show f 1t
                k "Don't 'fool' me!"
                k "I see through you. You resort to clichès when you're caught off guard. You—"
                play audio heart noloop
                o 1n "We love you so dearly! How absurd!"
                o 1d "CHOOSE SOMEONE ELSE."
                $persistent.loveFont = True
                $loveConfession = "Fontaine"
            "No. No, I didn't.":
                k "I'm... it wasn't enough time. I care about you all, even now, but..."
                o 1n "Real love blooms, it doesn't burn, does it? Your restraint is so impressive!"
                $loveConfession = "None"
                $temp = False

    k "..."

    o "Are you ready? To go?"

    menu:
        "Resist":
            $resistance += 1
            play audio beep noloop
            show image splashEKGFull at summonEKG
            pause 0.3
            k "Aagghkk...!"
            show f 1h at mt1
            show c 1i at mt2
            o 1h "HEY what? What's that line?"
            show l 1h

            show t 1i at f22
            "Kylie hadn't made it to her feet before a flare of pain seized her chest, leaving her to stumble against Tania and Lichelle."
            pause 0.2
            t "Fontaine! What are you doing to her?"
            o 1b "We did not cause that!"
            "She seems genuinely offended."
            k "... someone..."
            play audio beep noloop
            hide image splashEKGFull at summonEKG
            stop music fadeout 3.0
            k "i t  h u r t s"
            play audio beep noloop
            show image splashEKGFull at summonEKG
            pause 0.3
        "Give up":
            jump endingGaveUp

    pause 0.1
    o "We know what to do, then."

    c 1d "And what's that? Regale us."

    t 1e "HELP HER you... you damn thing!"

    pause 0.5

    o 1a "Sophie."

    l 2r "Huh?"

    pause 0.5

    play music onTheNod

    o 1n "You're still there, aren't you?"

    pause 0.5

    $chat.addmessage(sophie, "Mom? Daddy? Is that... who?")

    pause 0.5

    o 1k "Fine then."

    o "Sophie. Cassandra. Kylie. Lichelle. Louisa."

    o 1i "WE are a-a-a-s much an NPC in this as any of you!"

    $chat.addmessage(sophie, "Louisa...")

    $chat.addmessage(sophie, "WHAT HAPPENED TO LOUISA???")

    o "You know what happened to her. {i}YOU GAVE US TO HER{/i}."

    o 1b "And you called us jewelry. Baubles. pppppointless accessories!"

    

    "... storage.Tania.severed: [taniaBio.severViewed]"

    if taniaBio.severViewed:
        show t 1i at fr13
        pause 0.5
        hide t 1c at f13

    o 1h "Hm?"

    "... storage.Robin.severed: [robinBio.severViewed]"

    $chat.addmessage(sophie, "... this is my will.")

    "... storage.Cass.severed: [cassBio.severViewed]"

    if cassBio.severViewed:
        show c 1i at f13
        pause 0.5
        hide c 1c at f13

    $chat.addmessage(sophie, "I don't want this anymore.")

    un "Who's speaking?"

    # Lichelle is let loose at this pont

    "... storage.Lichelle.severed: [lichBio.severViewed]"

    if lichBio.severViewed:
        show l 1i at fr13
        pause 0.5
        hide l 1c at f13

    $chat.addmessage(sophie, "I don't want to need you anymore!")

    un "Why?"

    $chat.addmessage(sophie, "I hope I've done this right. I hope.")

    "storage.Fontaine.severed: [fontBio.severViewed]"

    pause 1.0

    o 1b "We had no idea you were so aware, Sophie."

    o 1c "SOMEONE has been NAUGHTY. Trying to SEVER our STRINGS."

    o "Well, we can't have that. Let's fix things, shall we?"

    if fontBio.severViewed == False:
        pause 1.0
        o 1b "... did you choose, then, not to sever your connection to us?"
        pause 0.5
        o 1c"Then you've learned nothing."
        o "Then you deserve your fate."
        o 1d "One last turn. One final dissociation."
        o 1e "We will see you soon, Sophie."
        $hideGui()
        $gaveUp = True
        jump endingGaveUp

    else:
        stop music fadeout 1.0
        pause 1.0

        o 1c "W-w-w-w-w-w-w-w-w-what?"

        o "Kylie did you do this to us?"

        play music kylieFightsBack

        k "What happened to we?"

        o 1i "WE ARE? Severed???"

        # Show a splash screen with the floor and only the unstrung girls lying dead. Some visual indication of a change.

        k "Guys!"

        k "Hey Lichelle, Lichelle! Cass, Tania, you okay?"

        o 1f "WE ARE O-O-OKAY"

        hide f with dissolve

        show image fontDiss1 at tDiss

        # character appears, an amalgamation of each other character, bleeding ones and zeros

        k "Oh my god, you're... are you real?"

        o "We suffer"

        o 1r "P-p-p-pain, this is pain? Is this pain?"

        o 1c "Make IT stop"

        show image fontDiss2 at tDiss

        o "please"

        o 1f "K-k-k-kylie"

        pause 1.0

        k "... I'm so sorry."

        k "I wish it could be different."

        o 1h "kkkkkkkk"

        menu:
            k "If it means anything at all..."

            "I forgive you.":
                k "I forgive you."
                k "I can't... I can't speak for anyone else, but I do."
                k "I don't know what you are. I just think you're lonely."
                # show e understanding this, agreeing.
                o 1b "..."

                show image fontDiss3 at tDiss
                k "Maybe some day you'll be able to reach us. I hope..."
                k "I hope you don't hate us."
                o "...ccould n-n-nnever hhate--"
                o 1m "...l-lllove... so so so so m-m-m-mmuch"
                k "..."
                
                $entityForgiven = True
                # splash screen of kylie hugging entity

            "I'll never, ever forgive you.":
                k "If there's a hell you can go to, I hope you rot there."
                k "You're a killer. A monster."
                o 1b "nnnnn"
                k "I hate you."
                o 1c "... you ex-x-x-ist because... of us..."
                k "I never asked for that! Sophie's dead!"
                o "...ccould n-n-nnever hhate--"
                o 1m "...l-lllove... so so so so m-m-m-mmuch"
                k "..."
                show image fontDiss3 at tDiss
                $entityForgiven = False
                # splash screen of kylie turning from entity

        # effect suggesting collapse of game

        # sophie gets up

        k "... oh."
        play audio beep noloop
        show image splashEKGFull at summonEKG
        pause 0.3

        hide f
        hide fontDiss1
        hide fontDiss2
        hide fontDiss3
        
        k "nngh"

        ki "Why does everything hurt...?"

        hide image splashEKGFull at summonEKG
        play audio beep noloop
        show image splashEKGFull at summonEKG
        pause 0.3

        s 1v "What..."

        ki "What's that... that smell...?"

        hide image splashEKGFull at summonEKG
        play audio beep noloop
        show image splashEKGFull at summonEKG
        pause 0.3

        show k 1h at f12

        s "... Kylie...?"

        k 1i "Sophie? Is that you?"

        s "... is this real...?"

        hide image splashEKGFull at summonEKG
        play audio beep noloop
        show image splashEKGFull at summonEKG
        pause 0.3

        k 1f "Nnngngghh!"

        hide k at f12

        s 1l "KYLIE!"

        show k 1v at f12

        k "I don't have time. I'm, I'm coming apart--"

        hide k with dissolve

        hide image splashEKGFull at summonEKG
        play audio beep noloop
        show image splashEKGFull at summonEKG
        pause 0.3

        show image kylieDiss1 at tDiss

        k "I wish I could've gotten to know you."

        hide image splashEKGFull at summonEKG
        play audio beep noloop
        show image splashEKGFull at summonEKG
        pause 0.3

        show image kylieDiss2 at tDiss
        k "Nnngh! I, I, I think we w-would've had..."

        $hideGui()

        show image kylieDiss3 at tDiss
        k "a lot... a lot in common!"
        stop music fadeout 3.0
        play audio beep noloop
        hide image splashEKGFull at summonEKG
        hide k with dissolve
        hide kylieDiss1 with dissolve
        hide kylieDiss2 with dissolve
        hide kylieDiss3 with dissolve
        show image kylieDiss4 at tDiss

        # heartbeat - drop background out and only show kylie and entity. Kylie's bleeding froom her mouth.
        show image splashEKGFull at summonEKG
        pause 0.3

        s 1v "What's happening to us? Hey!"

        # heartbeat, now from eyes
        play audio beep noloop
        show image splashEKGFull at summonEKG
        pause 0.3



        hide image splashEKGFull at summonEKG
        play audio beep noloop
        # heartbeat, both gone
        show image splashEKGFull at summonEKG
        hide kylieDiss4 with dissolve

        pause 0.3
        # heartbeat

        s "Kylie. KYLIE!"

        pause 1.0

        hide image splashEKGFull at summonEKG

        # splash screen with sophie screaming, maybe?

        scene bg black with fade

        # scene for sophie's room

        pause 2.0

        # heartbeat, both gone
        show image splashEKGFull at summonEKG

        pause 2.3
        hide image splashEKGFull at summonEKG
        call endingCass from _call_endingCass

        pause 2.0

        # heartbeat, both gone
        show image splashEKGFull at summonEKG

        pause 2.3
        hide image splashEKGFull at summonEKG
        call endingLich from _call_endingLich

        pause 2.0

        # heartbeat, both gone
        show image splashEKGFull at summonEKG

        pause 2.3
        hide image splashEKGFull at summonEKG
        call endingTania from _call_endingTania

        # heartbeat, both gone
        show image splashEKGFull at summonEKG

        pause 2.3
        hide image splashEKGFull at summonEKG

        # ending robin
        
        "The visions... the visions dance."
        "I expected something. Something. Robin, where are you?"
        "Where is your last word? Where is my closure?"

        pause 1.0

        show r 1c at f12

        r "Papillon. Life has never worked that way."

        hide r at f12

        "I can hear her saying that. But she didn't. She's gone. She's gone."

        "Louisa. I love you."

        pause 2.3
        hide image splashEKGFull at summonEKG

        pause 2.0

        "Who are you?"

        "Who are you really?"

        pause 1.0

        # Ending fork. I hate that we're cutting so much. But the game needs to be done. You know what? We can keep the mini endings. All of them are still in-delusion, though. There is no real ending.

        menu:
            "..."

            "I am Kylie":
                k "..."
                s "Go home, then, Kylie."
                hide image splashEKGFull at summonEKG
                play audio beep noloop
                # heartbeat, both gone
                show image splashEKGFull at summonEKG

                pause 2.3
                hide image splashEKGFull at summonEKG
                jump endingKylie

            "I am Sophie":
                s "..."
                k "Go home, Sophie."
                hide image splashEKGFull at summonEKG
                play audio beep noloop
                # heartbeat, both gone
                show image splashEKGFull at summonEKG

                pause 2.3
                hide image splashEKGFull at summonEKG
                jump endingSophie

        return
