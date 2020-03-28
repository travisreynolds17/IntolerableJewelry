


label endingTron5000:
    #routes based on if entity is severed, routed according to who else is severed.

    
    # write common  ending here. Then jump to each exclusive scene if player has earned it.

    scene bg stage with fade

    l "..."

    k "Lichelle? You okay?"

    l "H-h-have we finished our g-g-g-goodbyes?"

    r "It's not Lichelle anymore, then."

    k "Why won't you let us go?"

    l "We love you far too much to let you go."

    l "Besides, why not live in bliss with us forever?"

    l "Why LIVE with pain and INEVITable DEATH?"

    k "Robin, Cassandra, back me up here!"

    r "... we are not Lichelle anymore, then."

    c "< We are all Lichelle, then. >"

    l "You a-a-a-re too near your physical shell, still."

    l "But don't getcher panties tied up. One'r two more go-rounds and you'll be right with us!"

    l "We would say that, if this were not the last."

    k "What does that mean for me?"

    l "We aren't entirely sure sure sure."

    l "Isn't that fun?"

    "... storage.Tania.severed: [severTania]"

    l "Hm?"

    "... storage.Robin.severed: [severRobin]"

    l "H-h-h-h-hey!"

    "... storage.Cass.severed: [severCass]"

    un "Who's speaking?"

    # Lichelle is let loose at this pont

    "... storage.Lichelle.severed: [severLich]"

    "storage.Kylie.severed: [severKylie]"

    un "Why?"

    "storage.God.severed: [severGod]"

    un "STAY AWAY FROM THAT COMMAND!"

    "storage.[entityName].severed: [entitySevered]"

    e "It knows our name? ... oh."

    e "SOMEONE has been NAUGHTY. Trying to SEVER our STRINGS."

    e "Well, we can't have that. Let's fix things, shall we?"

    if severKylie == True:
        jump endingKylie

    if severEntity == False:
        jump endingEntityWins
    
    else:

        pause 1.0

        e "W-w-w-w-w-w-w-w-w-what?"

        e "Kylie did you do this to me?"

        k "What happened to we?"

        e "WE ARE? un-un-unstrung?"

        # have robin, cass, lichelle fall dead to the ground. Set it up such only the severed girls fall. Show a splash screen with the floor and only the unstrung girls lying dead. Some visual indication of a change.

        k "Guys!"

        k "Hey Lichelle, Lichelle! Cass, Robin, you okay?"

        e "WE ARE O-O-OKAY"

        # character appears, an amalgamation of each other character, bleeding ones and zeros

        k "Oh my god, you're... are you [entityName]?"

        e "We suffer"

        e "P-p-p-pain, this is pain? Is this pain?"

        e "Make IT stop"

        e "please"

        e "K-k-k-kylie"

        k "... I'm so sorry."

        k "I wish it could be different."

        e "kkkkkkkk"

        menu:
            k "If it means anything at all..."

            "I forgive you.":
                k "I forgive you."
                k "I can't... I can't speak for anyone else, but I do."
                k "I don't know what you are. I just think you're lonely."
                #show e understanding this, agreeing. 
                e "..."
                k "Maybe some day you'll be able to reach us. I hope..."
                k "I hope you don't hate us."
                e "...ccould n-n-nnever hhate--"
                e "...l-lllove... so so so so m-m-m-mmuch"
                k "..."
                #splash screen of kylie hugging entity

            "I'll never, ever forgive you.":
                k "If there's a hell you can go to, I hope you rot there."
                k "You're a killer. A monster."
                e "nnnnn"
                k "I hate you."
                e "... you ex-x-x-ist because... of me..."
                k "I never asked for that! Sophie's dead!"
                e "...ccould n-n-nnever hhate--"
                e "...l-lllove... so so so so m-m-m-mmuch"
                k "..."
                # splash screen of kylie turning from entity

        # effect suggesting collapse of game
                
        # sophie gets up
        
        k "... oh."

        #heartbeat?

        k "nngh"

        ki "Why does everything hurt...?"

        #heartbeat

        s "What..."

        ki "What's that... that smell...?"

        #heartbeat

        show k

        s "... Kylie...?"

        k "Sophie? Is that you?"

        s "... is this real...?"

        #heartbeat

        k "Nnngngghh!"

        s "KYLIE!"

        k "I don't have time. I'm, I'm coming apart--"

        #heartbeat, entity behind Kylie

        k "I wish I could've gotten to know you."

        #heartbeat

        k "Nnngh! I, I, I think we w-would've had..."

        k "a lot... a lot in common!"

        #heartbeat - drop background out and only show kylie and entity. Kylie's bleeding froom her mouth.

        s "What's happening to you? Hey!"

        k "God. It hurts, Sophie."

        #heartbeat, now from eyes

        # very slow text

        k "Goodbye...!"

        #heartbeat, both gone

        #heartbeat

        s "Kylie. KYLIE!"

        pause 1.0

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

        d "Wait what? I thought you were gonna apologize or for turning me down or something."

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

        d "I didn't say you were. It's just that I've seen these signs before."

        s "I'm clean."

        d "You've shaved your head."

        s "David."

        d "There're burn marks all over your arms."

        s "I got shocked, that's all. It burned up some of my hair so I just, I just started over."

        d "Baby, your life is yours. I can't tell you what to do or what not to do."

        s "... I can't stop shaking, David."

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
            $loveConfession == "Robin"

        elif loveCass == 5 and severCass == True:
            $loveConfession == "Cass"

        elif loveTania == 5 and severTania == True:
            $loveConfession == "Tania"

        elif loveLich == 5 and severCass == True:
            $loveConfession == "Lichelle"

        else:
            $loveConfession == "None"
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