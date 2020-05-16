


label endingTron5000:
    #routes based on if entity is severed, routed according to who else is severed.

    # show oblivion

    show f 1a at f12
    o "Ladies."

    show l 1d at fr13

    l "Bitch."

    show l 1m at fr22

    "Tania snorts, covers her mouth to hide her laughter."

    show c 1k at fr12 
    
    $chat.addmessage(elsa,"There's just no stopping the narrator.")

    o 1l "Are we r-r-rready for the next cycle?"

    c "Why are you asking any of us except Kylie? We know damn well there's no choice."

    o 1j "Fair."

    o 1m "Kylie, sweet lovely Kylie."

    k "..."

    o "Are you ready? To go?"

    menu:
        "Resist":
            $resistance +=1
            show image splashEKGFull at summonEKG
            pause 0.3
            k "Aagghkk...!"
            o 1h "HEY what? What's that line?"
            show l 1h
            show t 1i
            "Kylie hadn't made it to her feet before a flare of pain seized her chest, leaving her to stumble against Tania and Lichelle."
            pause 0.2
            t "Fontaine! What are you doing to her?"
            o 1b "We did not cause that!"
            "She seems genuinely offended."
            k "... someone..."
            hide image splashEKGFull at summonEKG
            k "i t  h u r t s"
            show image splashEKGFull at summonEKG
            pause 0.3
        "Give up":
            jump endingGaveUp
    

    o "We know what to do, then."

    c 1d "And what's that? Regale us."

    t 1e "HELP HER you... you damn thing!"

    pause 0.5

    o 1a "Sophie."

    l 1r "Huh?"

    pause 0.5

    o 1n "You're still there, aren't you?"

    pause 0.5 
    
    $chat.addmessage(sophie,"Mom? Daddy? Is that... who?")

    pause 0.5

    o 1k "Fine then."

    o "Sophie. Cassandra. Kylie. Lichelle. Louisa."

    o 1m "WE are a-a-a-s much an NPC in this as any of you!" 
    
    $chat.addmessage(sophie,"Louisa...") 
    
    $chat.addmessage(sophie,"WHAT HAPPENED TO LOUISA???")

    o "You know what happened to her. {i}YOU GAVE US TO HER{/i}."

    o 1b "And you called us jewelry. Baubles. pppppointless accessories!"

    "... storage.Tania.severed: [taniaBio.severed]"

    if severTania:
        show t 1i at fr13
        pause 0.5
        show t 1c at d13

    o 1h "Hm?"

    "... storage.Robin.severed: [robinBio.severed]" 
    
    $chat.addmessage(sophie,"... this is my will.")

    "... storage.Cass.severed: [cassBio.severed]"

    if cassBio.severed:
        show c 1i at f13
        pause 0.5
        show c 1c at d13
    
    $chat.addmessage(sophie,"I don't want this anymore.")

    un "Who's speaking?"

    # Lichelle is let loose at this pont

    "... storage.Lichelle.severed: [lichBio.severed]"

    if lichBio.severed:
        show l 1i at fr13
        pause 0.5
        show l 1c at d13
    
    $chat.addmessage(sophie,"I don't want to need you anymore!")

    un "Why?"
    
    $chat.addmessage(sophie,"I hope I've done this right. I hope.")

    "storage.Fontaine.severed: [fontBio.severed]"

    o 1b "We had no idea you were so aware, Sophie."

    o 1c "SOMEONE has been NAUGHTY. Trying to SEVER our STRINGS."

    o "Well, we can't have that. Let's fix things, shall we?"

    if fontBio.severed == False:
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

        pause 1.0

        o 1c "W-w-w-w-w-w-w-w-w-what?"

        o "Kylie did you do this to us?"

        k "What happened to we?"

        o 1i "WE ARE? Severed???"

        # Show a splash screen with the floor and only the unstrung girls lying dead. Some visual indication of a change.

        k "Guys!"

        k "Hey Lichelle, Lichelle! Cass, Tania, you okay?"

        o 1f "WE ARE O-O-OKAY"

        # character appears, an amalgamation of each other character, bleeding ones and zeros

        k "Oh my god, you're... are you real?"

        o "We suffer"

        o 1r "P-p-p-pain, this is pain? Is this pain?"

        o 1c "Make IT stop"

        o "please"

        o 1f "K-k-k-kylie"

        k "... I'm so sorry."

        k "I wish it could be different."

        o 1h "kkkkkkkk"

        menu:
            k "If it means anything at all..."

            "I forgive you.":
                k "I forgive you."
                k "I can't... I can't speak for anyone else, but I do."
                k "I don't know what you are. I just think you're lonely."
                #show e understanding this, agreeing. 
                o 1b "..."
                k "Maybe some day you'll be able to reach us. I hope..."
                k "I hope you don't hate us."
                o "...ccould n-n-nnever hhate--"
                o 1m "...l-lllove... so so so so m-m-m-mmuch"
                k "..."
                #splash screen of kylie hugging entity

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
                # splash screen of kylie turning from entity

        # effect suggesting collapse of game
                
        # sophie gets up
        
        k "... oh."

        show image splashEKGFull at summonEKG
        pause 0.3

        k "nngh"

        ki "Why does everything hurt...?"

        hide image splashEKGFull at summonEKG

        show image splashEKGFull at summonEKG
        pause 0.3

        s "What..."

        ki "What's that... that smell...?"

        hide image splashEKGFull at summonEKG

        show image splashEKGFull at summonEKG
        pause 0.3

        show k 1h 

        s "... Kylie...?"

        k "Sophie? Is that you?"

        s "... is this real...?"

        hide image splashEKGFull at summonEKG

        show image splashEKGFull at summonEKG
        pause 0.3

        k 1f "Nnngngghh!"

        s "KYLIE!"

        k 1q "I don't have time. I'm, I'm coming apart--"

        hide image splashEKGFull at summonEKG

        show image splashEKGFull at summonEKG
        pause 0.3

        k "I wish I could've gotten to know you."

        hide image splashEKGFull at summonEKG

        show image splashEKGFull at summonEKG
        pause 0.3

        k 1f "Nnngh! I, I, I think we w-would've had..."

        $hideGui()

        k 1n "a lot... a lot in common!"

        hide image splashEKGFull at summonEKG

        #heartbeat - drop background out and only show kylie and entity. Kylie's bleeding froom her mouth.
        show image splashEKGFull at summonEKG
        pause 0.3

        s "What's happening to you? Hey!"

        

        #heartbeat, now from eyes
        show image splashEKGFull at summonEKG
        pause 0.3


        hide image splashEKGFull at summonEKG

        #heartbeat, both gone
        show image splashEKGFull at summonEKG
        hide k at f12
         
        pause 0.3
        #heartbeat

        s "Kylie. KYLIE!"

        pause 1.0

        hide image splashEKGFull at summonEKG

        #splash screen with sophie screaming, maybe?

        scene bg black with fade

        #scene for sophie's room

        scene bg resta with fade

    

        d "Sophie? Hey, you okay?"

        s "..."

        s "Hm? Oh. I'm sorry, I... must've went away for a while."

        "Across the restaurant, the pianist's fingers dance beautifully across ebony and ivory."

        "For a moment her eyes land on us, but only for a moment."

        show d 1a at f12

        d "I worry about you."

        "He does. It's probably why he agreed to meet me here at all."

        d 1m "I gotta tell you, it surprised me when you called me up and asked to meet here."
        
        d "Of all places."

        s "Yeah. I just needed to figure some things out."

        d 1a "Like what?"

        s "I... don't know what's real anymore, David."

        d 1g "Wait what? I thought you were gonna apologize or for throwing me out of your hospital room or something."

        s "That, that, too. Yes. I'm sorry for that, I am. But that's not what I wanted to talk about."

        s "David. Are you real?"

        pause 0.5

        d 1r "I guess? I don't see why not."

        s "But how do you know?"

        d 1j "I'm made of meat and I piss a lot."

        s "Yeah but what if you're a program designed to do that?"

        d 1k "Seems like a really useless program."

        s "David--"

        d 1g "Sophie. I love you. I did before and I still do, so when I say this I need you to know it comes in good faith."

        pause 0.5

        d 1b "You're not using again, are you?"

        pause 0.4

        s "I'm not. I'm not, I promise. And I'm not crazy."

        d 1g "I didn't say you were crazy. It's just that I've seen these signs before."

        s "I'm clean."

        d "You cut your hair. You've lost weight."

        s "David."

        d 1k "Pull up your sleeves."

        s "I got shocked, that's all. My headset. It burned up some of my hair so I just, I just started over."

        d 1b "That didn't happen, Sophie. Remember?"

        s "... I can't stop shaking."

        d "I can see that. I need to see your arms, Sophie."

        menu:
            d "Pull up your sleeves."

            "Pull them up":
                s "Fine. I get why you wouldn't trust me."
                # show arms with no marks
                d 1q "It isn't that I don't trust YOU. I just know what that garbage does to people."
            "I refuse.":
                s "I shouldn't have to prove anything to you. Or anyone."
                d 1g "..."
                d 1k "I'm not gonna force you. I shoulda known what I signed up for."

        s "I just don't know what's real anymore!"

        d 1m "I'm real."

        "He covers my hand with his own, then."

        "It's colder than I thought it might be."

        "I can't be alone. Not now. Not ever."

        pause 0.1

        show image glitchGui at frameGlitch 
        s "I wonder how the girls are doing."

        pause 0.1

        d 1a "What girls?"
        hide glitchGui

        show image glitchGui at frameGlitch

        s "You know. Robin and the others."
        hide glitchGui

        d 1k "Sophie."

        s "What?"

        d "You know Robin isn't real."
        
        s "I know that. I mean..."

        s "..."

        s "I don't know what I mean."

        pause 0.1

        d 1m "Someday you will."

        pause 0.1

        s "It's just that I didn't recognize anyone else. Their names were there. Cassandra looked like Cassandra."

        d 1b "Sophie."

        s "Why would Louisa look different? Why did she have a different name?"

        d "Maybe it was just your mind trying to protect you. Or work through grief, something like that."

        s "I didn't even recognize {i}you{/i}."

                # knocking sound
        # voice "Ms Koenig? We have an application for someone to visit you. Want to have a look?" as a notification. NOPE. this is a phone thing. built a new chatlog with a phone graphic for texts, works exactly the same way.

        # david will be the centerpiece here. He keeps getting interrupted by "the girls" and giving up his seat, then coming back. For the love endings, tania asks david to excuse her and then goes off to wherever they are. In Robin's case she just shows up and David is nonchalantly, "Oh hey Louisa. Sorry I doubted you." notes her hair is wet.
        #full everyone is good ending would show her in hospital with david and a woman who turns out to be Elsa watching over her.
        # need to go through list. can only be visited by severed. whoever is first brings notice of those who weren't severed. Tania is first, then cass, then lichelle.
        # adjust the orders in the following ways. Fontaine is first, actually. dialog changes if you forgave her. either way not hostile. she brings news of the severed if we implement a way to confess to liv, she's still first. love confession is next to last. except liv, scenes need to be able to take place in any order. Robin's bad ending would have to take place last. We know Louisa's really gone, so it'd be sophie who found a way to stab david. Do I want it that way? It's like a person would have to sever everyone or get a bad end. if you get a bad end, it needs to be conveyed that all this happened in the span of a bad trip. she is NOT in a mental institution. too cliche. mention it once. someone saying that had a trip that lasted for a week, but then they opened their eyes to find two hours had passed.
        #Yes, this means we have to largely rewrite the endings.


        if loveRobin >= 4 and severRobin == True:
            $loveConfession = "Robin"

        elif loveCass >= 4 and severCass == True:
            $loveConfession = "Cassandra"

        elif loveTania >= 4 and severTania == True:
            $loveConfession = "Tania"

        elif loveLich >= 4 and severCass == True:
            $loveConfession = "Lichelle"

        else:
            $loveConfession = "None"




            #--------------------------------------------------------------------
        show d 1k

        d "Well, that's -"
        #phone sound SFX
        s "OH!"

        pause 0.1

        d 1j "It's your phone."

        s "I know that."

        "..."

        s "It's from Lichelle."

        d "Who?"

        s "Elle. You've met her, she used to be the door guard."

        d "Oh, Elle. Right. Biceps. What's she want?"

        s "To talk."

        s "If you don't mind giving up your seat for a sec."

        show l 1a at fr13

        l "Sophie. You look rough, girl."

        show d 1m

        "David swivels a bit in his chair and provides an easy smile to her."

        show l 1m

        "She returns it, bold and bright."

        s "I feel okay, though."

        l "I don't believe it. David, my guy, do you mind giving me and gamer girl a minute?"

        "He already was on his feet, brushing off his seat for her."

        show d 1a at mt1

        d "Anything for you, lady. You know, I never knew your name was Lichelle."

        "I didn't know they had such a friendly relationship."

        show l 2l at mt2

        l "Yeah, it is, but I'm Elle to you, bitch."

        d 1n "Yes ma'am. You two have fun, I'm gonna go admire the restroom."

        hide d at fl11

        "He's chuckling as he walks off, effervescent, easy. How could I have misjudged him so completely?"

        l 1a "Babe. Based on how you're looking right now, I need you to be honest."

        s "I'm not using."

        l 1j "On god?"

        s "On god."

        "She pauses, but her smile remains."

        l 1a "I found out something today."

        "She has my attention. I'm never sure whether to answer someone who opens a conversation with a statement like that, so I simply wait."

        if severCass == True:
            l "Cassandra woke up."

            s "What? Really? When?"

            l 1k "A few weeks ago. Her god damn agent hid it from me. If he wasn't already a damn lawsuit in a tracksuit I would've punched him in the mouth."

            s "Have you talked to her? Does she... does she hate me?"

            l 1a "I didn't ask, babe. But yeah, we had a heart to heart."

            pause 0.1

            l 1b "She doesn't say much. But you gotta know she has a lot on her mind."

            pause 0.1

            l "She did say she wants to talk to you, too."

            "My skin lights up with anxious jitters."

            s "... I don't know if I can. Talk to her, I mean."

            l 1a "You can, babe. In fact, I insist. It'd be good for both of you."

            pause 0.1

            s "... okay."

            l 1j "Okay what?"

            s "I'll talk to her."

            pause 0.1

            l 1m "Good."

            pause 0.1

            l "Tania's been asking about you, too."

        else:

            l 1b "Cassandra won't..."

            "She's cracking. Oh no. No no no no."

            l 1c "She won't, she..."

            "I knew it would be like this."

            l "... she's gone, babe."

            s "When? I heard she was just recovering."

            l 1b "A few weeks ago. Her agent hid it as long as he could, bastard."

            if loveCass >= 4:
                s "I never got to tell her. Out here."

                l 1r "Huh?"

                s "That I..."

                show l 1b

                "Lichelle's staring at me. Her jaw is set."

                l "That you what?"

                s "I just... we were close. In the simulation."

                l "The what?"

                s "When we all got trapped in Intolerable Jewelry together."

                "There's a tragedy writing its somber prose across her face as I speak."

                l 1g "David mentioned you might bring that up. Honey."

                "Here it comes."

                l 1d "There's no damn simulation. I don't even play video games and Cassandra sure as hell never streamed any."

                l "If we're gonna do this, you've gotta commit to reality."

                s "... it wasn't some fucking delusion."

                show l 1h

                "I wonder if the abruptness of my backbone caught her off guard."

                s "It doesn't matter. The Cassandra I fell in love with is gone either way."

                show l 1b

                pause 0.4

                l "Yeah, well. That means there's no need to worry about it, is there."

                l "I just wanted you to know. No more, no less."

                s "Thank you."

                l "Thank you. Sure thing. Thank you. Shit."

                pause 0.3

                "For a moment, I can feel the earth separating between us."

                show l at 1m

                "But then she smiles again, and her poker face is back in place."
            else:
                l "I just wanted you to know. Considering you two were... whatever you were."

                pause 0.3

                s "I know she didn't love me. Or even like me."

                l 1p "Oh yeah?"

                s "Oh come on. We were sleeping together. There's nothing more obvious in the world than a partner who isn't that into it."

                l 1m "Never been a thing for me."

                s "Good for you. I liked her, Elle. I didn't love her."

                l 1b "You didn't love you, either."

                "..."

                s "I guess not."

                l "..."

        pause 0.1 

        l 1a "Tania's been bugging me to have you call."
        
        "... I haven't returned any of her messages."

        "Frankly, I don't want to."

        l 1k "As a favor to me, call that girl back before she has a fit."

        s "Elle..."

        l 1j "Look. Sophie."

        "Her smile remains, but the light has dimmed."

        l "I need you to understand something."

        pause 0.3

        l "Louisa died months ago. She been gone long enough it's time we start sorting things out."

        l 1d "She only had eyes for you, god dammit, but she was my friend."
        
        l "I oughtta smack your damn mouth every day for the rest of your natural life for what you did."

        l "Giving her that trash."

        "Her tone remains friendly, even. I don't protest. She's not wrong."

        pause 0.4

        l 1b "But I won't."

        l "You're not evil. You're sick. Only damn way to do right by Louisa and Cassandra is to get your self cleaned up and do something with your life."

        l 1j "I've been talking to David for a while, too. I'm making it my personal mission to be up your ass every single day until I'm satisfied you're gonna be all right."

        s "... promise?"

        show l 1k

        "It's not much of a joke, but the pressure behind my eyes is enormous. I won't cry in front of her. I won't."

        pause 0.2

        l "I'm serious. Promise me you'll talk to Tania, too."

        s "You know, I never met her in person outside the simulation."

        l 1a "Oh babe. She's something else, lemme tell you."

        "I wonder what her silence on the simulation means."

        s "... will you go with me?"

        pause 0.5

        s "You don't owe me anything-"

        l 1m "I'll go."

        s "- but if you could... oh. Well."

        s "That's good then."

        l 1n "Yep."

        "She goes silent. Someone else's music occupies Ganymead's sonic space. It's not Cassandra playing anymore."

        l "You've lost enough time."

        s "..."

        l 1a "..."

        s "Now?"

        l 1j "Now."

        scene bg black with fade

        # mini endings. Note: Love confession ending is second to last. 

        
        call endingTania
        # as long as Tania was severed, we return here after her ending.

        call endingCass
       
        call endingLich

        call endingRobin

        call endingsBad 
        # checks for all non-severed or bad endings. 
        
        return