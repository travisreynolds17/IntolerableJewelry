label common5:
    # common ending. Ends with jump to ENDING-TRON 5000 which routes us to appropriate endings.

    # note there is narration here. There has to be. Actually probably need to add it earlier. It's just quote narration.

    pause 1.0

    pause(0.5)
    $hideGui()
    scene bg load-god with fade
    pause 1.0
    pause
    scene bg screen
    pause(0.5)
    $showGui()
    pause 0.5

    "There's a shift, only barely perceptible, as the entity releases its control of Lichelle."

    "It isn't dramatic, nor could it be taken as a clear indication of anything, but it's enough to put Kylie a little bit at ease."

    
    
    $chat.addmessage(crab,"Who's voice is that?")

    k "You okay?"

    "Cassandra and Tania flank the fighter and take gentle hold of her shoulders."

    $renpy.notify("She can't be gone.")

    l "... I'm good. I guess."

    c "< Glad to hear it. >" 

    t "I hate to say it, but you'll get used to Oblivion the more you're around her."

    pause 0.4

    t "Assuming she allows us more time."

    k "Is there anything we can do to get out of this?" 
    
    $chat.addmessage(elsa,"There's nothing we can really do.")

    "Three sets of eyes gaze back at Kylie, forlorn, hopeless, and fiercely annoyed."

    t "I tried to tell you. I'm the only one with the power to do it."

    $renpy.notify("I didR/BG13:14-15 no more time. You have to make a decision!")

    "Kylie pauses, wringing her hands, keenly aware of them being her own hands now."

    k "I don't know."  
    
    $chat.addmessage(bar,"There's no way she could. Don't blame Kylie for Sophie's choices.")

    c "< It's too late now. Whatever's decided is decided. >"

    "Tania sighs, a quiet, empty sigh."

    t "Something's interfering with my messages anyway. I'm sorry, Kylie. This isn't your fault."
    
    $chat.addmessage(shub,"right? Kylie is the best of all of us.")

    k "What are you talking about?" 
    
    $chat.addmessage(liv,"She's so great. :)")

    t "This is what happens when you play this game. Robin dies. You lose sight of yourself." 
    
    $chat.addmessage(elsa,"Hey Liv, you're cheating! You're not supposed to be listening right now.")

    c "< And always Robin. >" 
    
    $chat.addmessage(liv,"Oopsie! Naughty me ;)")

    t "It lets Robin die. Iterates and expands the flaws of two. Controls one."

    c "<Then, leaves a final gathering like this one where it gives its speeches and lets us be alone for a while.>"

    l "So just like last time, then?" 
    
    $chat.addmessage(bong,"elle's getting it now")

    k "What happens? What's like last time?"

    pause 1.0

    "Cassandra and Tania exchange glances, as if silently debating which parent should deliver the bad news."

    t "Dissolution." 
    
    $chat.addmessage(bar,"More like recycling, honestly.")

    "An anxious thrill prickles the back of Kylie's neck. She's unsure if that feeling is her own, or how long she's known what it felt like."

    t "Here, we are only objects of intelligence. Frighteningly complex objects, of course, fully realized autonomous beings."

    "There's no hiding the excitement in Tania's tone. Kylie is certain she would have made a wonderful mad scientist in another universe." 
    
    $chat.addmessage(cake,"maybe she already is")

    "The idea brings with it the realization that another universe might well be around the corner."

    k "If we're just code, what is she?" 
    
    $chat.addmessage(liv,"I'm Oblivion, silly.")

    c "< I don't know. >"

    l "Me either babe."

    k "Tania?" 
    
    $chat.addmessage(egg,"liivvvvv")

    pause 1.0

    t "I'm sorry everyone. I might know Liv best of all of us, but even I don't know the nature of her."

    t "... Kylie." 
    
    $chat.addmessage(liv,"Sorry, sorry, I just love you all so much I can't help but peek ;)")

    k "Hm?" 
    
    $chat.addmessage(bong,"I got something for you to peek at Liv :D")

    t "I'm sorry for misleading you." 
    
    $chat.addmessage(liv,"ooh, private message lol ;)")

    c "<I'm sorry for puking on you.>"

    "Lichelle chuckles, quietly."

    l "I don't think I have anything to be sorry about, but goddamn, I'm sorry, too." 
    
    $chat.addmessage(elsa,"None of you have anything to be sorry for. Only Sophie.")

    t "We won't have much more time."

    c "<Kylie. If you have anything else you want to know, or say, you'd better do it now.>"

    # Last chance to talk with the girls. Maybe a last chance to raise relationsthip points?

    python:
        interviewed = False
        cassDone = []
        robinDone = []
        taniaDone = []
        lichDone = []
        allDone = [cassDone, robinDone, taniaDone, lichDone]
        #build arrays to control which question asked
        buildArrays(allDone, 6, False)

    #=============================================
    # LOOP for final discussion menu and submenus
    # Note C5 stands for Common5. This is to keep files organized togather.
    
    while interviewed == False:
        scene bg stage with fade
        menu:
            k "Who to talk to..."

            "Cassandra":
                call c5cassInterview
            "Robin...":
                call c5robinInterview
            "Lichelle":
                call c5lichInterview
            "Tania":
                call c5taniaInterview
            "I've said all I need to say.":
                $interviewed = True

    #=============================================

    
    scene bg stage with fade

    show c at left
    show t 
    show l at right
    with dissolve

    "They wait."

    "What needs to be said has been said."

    "Or perhaps it hasn't." 
    
    $chat.addmessage(elsa,"Who's voice is that?")

    k "So, what now?"

    t "We wait." 
    
    $chat.addmessage(liv,"The narrator. Of course.")


    k "Wow... this all feels so anticlimactic."

    t "That's real life, hon. Not everything makes a good story." 
    
    $chat.addmessage(bong,"Aren't we outside of the game?")

    c "< I'd rather go out with a whisper than a bang. >"

    l "Well, I'm not sitting around and doing nothing." 
    
    $chat.addmessage(liv,"I suppose. Oh, you all make such sense.")

    t "What will you do? Punch a hole in its server? Kick its objects and methods into submission?"

    l "I just don't like doing nothing."

    $renpy.notify("character.narrator.setValue('Null')")

    c "< I wouldn't know where to begin. >"

    k "What happens when the game ends?" 
    
    $chat.addmessage(beav,"much better")

    t "The credits roll, darling."

    k "Credits? Like, names and roles credits?" 
    
    $chat.addmessage(egg,"Hey Liv")

    t "The same."

    k "And we can see them? Whose names are on there?" 
    
    $chat.addmessage(liv,"Not now, I have a headache. ;)")

    c "< It's our names. If you believe the heading text, it's everybody who's ever played this game. >" 
    
    $chat.addmessage(egg,"You don't have a head :p")

    c "< They've gotten really, really long. >"

    scene bg black with fade

    "Time passes." 
    
    $chat.addmessage(liv,"Because I gave it to Elsa. :) :p :P ;)")

    "Perhaps it doesn't."

    $chat.addmessage(elsa,"lol babe")

    "Kylie sits on stage with the others. No one speaks more than a few words at a time." 
    
    $chat.addmessage(beav,"narrator's back")

    "Perhaps the inevitability of a fate they can barely comprehend has sucked the air out of the room."

    "Perhaps there was never air to begin with."  
    
    $chat.addmessage(liv,"Really, now? I must've gotten the method wrong.")
    
    $renpy.notify("character.narrator.setValue('')")

    "..."

    $getHistory(16)

    menu:
        "Resist":
            $resistance +=1
            show image splashEKGFull at summonEKG
            pause 0.3
            k "Nnggh...!"
            t "Kylie?"
            l "Babe? You okay?"
            pause 0.2
            k "... my chest hurts."
            c "< Is this normal? >"
            k "... I'm okay."
            hide image splashEKGFull at summonEKG
        "Give up":
            jump endingGaveUp


    jump endingTron5000
