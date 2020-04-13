


label endingTron5000:
    #routes based on if entity is severed, routed according to who else is severed.

    # show oblivion
    o "Ladies."

    l "Bitch."

    "Tania snorts, covers her mouth to hide her laughter." 
    
    $chat.addmessage(elsa,"There's just no stopping the narrator.")

    o "Are we r-r-rready for the next cycle?"

    c "< Why are you asking any of us except Kylie? We know damn well there's no choice. >"

    o "Fair."

    o "Kylie, sweet lovely Kylie."

    k "..."

    o "Are you ready? To go?"

    menu:
        "Resist":
            $resistance +=1
            show image splashEKGFull at summonEKG
            pause 0.3
            k "Aagghkk...!"
            o "HEY what? What's that line?"
            "Kylie hadn't made it to her feet before a flare of pain seized her chest, leaving her to stumble against Tania and Lichelle."
            pause 0.2
            t "Liv! What are you doing to her?"
            o "We did not cause that!"
            "She seems genuinely offended."
            k "... someone..."
            hide image splashEKGFull at summonEKG
            k "i t  h u r t s"
            show image splashEKGFull at summonEKG
            pause 0.3
        "Give up":
            jump endingGaveUp
    # write common  ending here. Then jump to each exclusive scene if player has earned it.

    scene bg stage with fade

    o "We know what to do, then."

    c "< And what's that? Regale us. >"

    t "HELP HER you... you damn thing!"

    pause 0.5

    o "Sophie."

    l "Huh?"

    pause 0.5

    o "You're still there, aren't you?"

    pause 0.5 
    
    $chat.addmessage(sophie,"Mom? Daddy? Is that... who?")

    pause 0.5

    o "Fine then."

    o "Sophie. Cassandra. Kylie. Lichelle. Louisa."

    o "WE are a-a-a-s much an NPC in this as any of you!" 
    
    $chat.addmessage(sophie,"Louisa...") 
    
    $chat.addmessage(sophie,"WHAT HAPPENED TO LOUISA???")

    o "You know what happened to her. YOU GAVE US TO HER."

    o "And you called us jewelry. Baubles. pppppointless accessories!"

    "... storage.Tania.severed: [severTania]"

    o "Hm?"

    "... storage.Robin.severed: [severRobin]" 
    
    $chat.addmessage(sophie,"... this is my will.")

    "... storage.Cass.severed: [severCass]" 
    
    $chat.addmessage(sophie,"I don't want this anymore.")

    un "Who's speaking?"

    # Lichelle is let loose at this pont

    "... storage.Lichelle.severed: [severLich]" 
    
    $chat.addmessage(sophie,"I don't want to need you anymore!")

    "storage.Kylie.severed: [severKylie]"

    un "Why?"

    "storage.God.severed: [severGod]"

    o "STAY AWAY FROM THAT COMMAND!" 
    
    $chat.addmessage(sophie,"I hope I've done this right. I hope.")

    "storage.Oblivion.severed: [entitySevered]"

    o "We had no idea you were so aware, Sophie."

    o "SOMEONE has been NAUGHTY. Trying to SEVER our STRINGS."

    o "Well, we can't have that. Let's fix things, shall we?"

    if severKylie == True:
        jump endingKylie

    if severEntity == False:
        o "... did you choose, then, not to sever your connection to us?"
        pause 0.5
        o "Then you've learned nothing."
        o "Then you deserve your fate."
        o "One last turn. One final dissociation."
        o "And now it is our turn to invade YOUR world."
        $hideGui()
        jump endingEntityWins
    
    else:

        pause 1.0

        o "W-w-w-w-w-w-w-w-w-what?"

        o "Kylie did you do this to me?"

        k "What happened to we?"

        o "WE ARE? un-un-unstrung?"

        # have robin, cass, lichelle fall dead to the ground. Set it up such only the severed girls fall. Show a splash screen with the floor and only the unstrung girls lying dead. Some visual indication of a change.

        k "Guys!"

        k "Hey Lichelle, Lichelle! Cass, Robin, you okay?"

        o "WE ARE O-O-OKAY"

        # character appears, an amalgamation of each other character, bleeding ones and zeros

        k "Oh my god, you're... are you real?"

        o "We suffer"

        o "P-p-p-pain, this is pain? Is this pain?"

        o "Make IT stop"

        o "please"

        o "K-k-k-kylie"

        k "... I'm so sorry."

        k "I wish it could be different."

        o "kkkkkkkk"

        menu:
            k "If it means anything at all..."

            "I forgive you.":
                k "I forgive you."
                k "I can't... I can't speak for anyone else, but I do."
                k "I don't know what you are. I just think you're lonely."
                #show e understanding this, agreeing. 
                o "..."
                k "Maybe some day you'll be able to reach us. I hope..."
                k "I hope you don't hate us."
                o "...ccould n-n-nnever hhate--"
                o "...l-lllove... so so so so m-m-m-mmuch"
                k "..."
                #splash screen of kylie hugging entity

            "I'll never, ever forgive you.":
                k "If there's a hell you can go to, I hope you rot there."
                k "You're a killer. A monster."
                o "nnnnn"
                k "I hate you."
                o "... you ex-x-x-ist because... of me..."
                k "I never asked for that! Sophie's dead!"
                o "...ccould n-n-nnever hhate--"
                o "...l-lllove... so so so so m-m-m-mmuch"
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

        show k

        s "... Kylie...?"

        k "Sophie? Is that you?"

        s "... is this real...?"

        hide image splashEKGFull at summonEKG

        show image splashEKGFull at summonEKG
        pause 0.3

        k "Nnngngghh!"

        s "KYLIE!"

        k "I don't have time. I'm, I'm coming apart--"

        hide image splashEKGFull at summonEKG

        show image splashEKGFull at summonEKG
        pause 0.3

        k "I wish I could've gotten to know you."

        hide image splashEKGFull at summonEKG

        show image splashEKGFull at summonEKG
        pause 0.3

        k "Nnngh! I, I, I think we w-would've had..."

        $hideGui()

        k "a lot... a lot in common!"

        hide image splashEKGFull at summonEKG

        #heartbeat - drop background out and only show kylie and entity. Kylie's bleeding froom her mouth.
        show image splashEKGFull at summonEKG
        pause 0.3

        s "What's happening to you? Hey!"

        k "God. It hurts, Sophie."

        #heartbeat, now from eyes
        show image splashEKGFull at summonEKG
        pause 0.3

        # very slow text

        k "Goodbye...!"

        hide image splashEKGFull at summonEKG

        #heartbeat, both gone
        show image splashEKGFull at summonEKG
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

        d "I worry about you."

        "He does. It's probably why he agreed to meet me here at all."

        d "I gotta tell you, it surprised me when you called me up and asked to meet here."
        
        d "Of all places."

        s "Yeah. I just needed to figure some things out."

        d "Like what?"

        s "I... don't know what's real anymore, David."

        d "Wait what? I thought you were gonna apologize or for throwing me out of your hospital room or something."

        s "That, that, too. Yes. I'm sorry for that, I am. But that's not what I wanted to talk about."

        s "David. Are you real?"

        pause 0.5

        d "I guess? I don't see why not."

        s "But how do you know?"

        d "I'm made of meat and I have to eat and poop."

        s "Yeah but what if you're a program designed to do that?"

        d "Seems like a really useless program."

        s "David--"

        d "Sophie. I love you. I did before and I still do, so when I say this I need you to know it comes in good faith."

        d "You're not using again, are you?"

        s "I'm not. I'm not, I promise. And I'm not crazy."

        d "I didn't say you were crazy. It's just that I've seen these signs before."

        s "I'm clean."

        d "You've shaved your head."

        s "David."

        d "There're marks all over your arms."

        s "I got shocked, that's all. It burned up some of my hair so I just, I just started over."

        d "That didn't happen, Sophie. Remember?"

        s "... I can't stop shaking."

        d "I can see that."

        s "I just don't know what's real anymore!"

        d "I'm real."

        "He covers my hand with his own, then."

        "It's colder than I thought it might be."

        "But I can't be alone. Not now. Not ever."

        scene bg black with fade

        pause 1.0

        #determine love ending if there is one. Remember, Cassandra is straight. DUDE. TANIA'S A COMA PATIENT HOOKED TO A COMPUTER. 

        if loveRobin == 5 and severRobin == True:
            $loveConfession = "Robin"

        elif loveCass == 5 and severCass == True:
            $loveConfession = "Cass"

        elif loveTania == 5 and severTania == True:
            $loveConfession = "Tania"

        elif loveLich == 5 and severCass == True:
            $loveConfession = "Lichelle"

        else:
            $loveConfession = "None"
        #CALLMini endings. Tania first. Hers is the main portion of the ending, explains most things. Other endings are shorter unless love version. No matter what, Robin ending happens last

        
        call endingTania
        # as long as Tania was severed, we return here after her ending.

        call endingCass
        #cass bad ending is only newspaper, return here after either
        call endingLich
        #same
        call endingRobin

        call endingsBad 
        # checks for all non-severed or bad endings. 
        
label endingOnlyEntity:
    #entity killed, but everything under its web dies too. Millions including characters die, but threat over. No one knows why.

label endingKylie:
    # The ending in which Sophie and kylie were separated. Sophie wakes up with four girls staring at her in hospital, all glitchy.