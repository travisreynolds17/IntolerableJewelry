label common5:
    # common ending. Ends with jump to ENDING-TRON 5000 which routes us to appropriate endings.

    # note there is narration here. There has to be. Actually probably need to add it earlier. It's just quote narration.
    stop music fadeout 3.0
    pause 1.0

    pause(0.5)
    $hideGui()
    scene bg load-god with fade
    pause 1.0
    pause
    scene bg dressing
    pause(0.5)
    $showGui()
    pause 0.5

    "Huh? My... the bedroom?"

    play music bedroom fadein 3.0

    python:
        renpy.notify("The last of my strength... I have sever them. Please—")
        cassBio.stringSever()
        lichBio.stringSever()
        robinBio.stringSever()
        taniaBio.stringSever()


    show t 1b at f11
    pause 0.3

    show c 1b at f12
    pause 0.3

    show l 1b at f13
    pause 0.3

    "The restraints clink and tumble away from the their skin."

    #enable severance
    $severToggle()
    
    $chat.addmessage(crab,"Who's voice is that?")

    k "You girls okay?"

    "Cassandra and Tania flank Lichelle as she stumbles, glassy-eyed, and take gentle hold of her shoulders."

    $renpy.notify("She can't be gone.")

    l 1q "... I'm good. I guess."

    c 1m "Glad to hear it." 

    t 1q "I hate to say it, but you'll get used to Fontaine the more you're around her."

    pause 0.4

    t 1b "Assuming she allows us more time."

    k "Is there anything we can do to get out of this?" 
    
    $chat.addmessage(elsa,"There's nothing we can really do.")

    "Three sets of eyes gaze back at Kylie, forlorn, hopeless, and fiercely annoyed."

    t 1k "I tried to tell you. I'm the only one with the power to do it."

    $renpy.notify("I didR/BG13:14-15 no more time. You have to make a decision!")

    pause 0.8

    t "See?"

    "Kylie pauses, wringing her hands, keenly aware of them being her own hands now."

    k "I don't understand."  
    
    $chat.addmessage(bar,"There's no way she could. Don't blame Kylie for Sophie's choices.")

    c 1g "It's too late now. Whatever's decided is decided."

    "Tania sighs, a quiet, empty sigh."

    t 1g "Something's interfering with my messages anyway. I'm sorry, Kylie. This isn't your fault."
    
    $chat.addmessage(shub,"right? Kylie is the best of all of us.")

    k "What are you talking about?" 
    
    $chat.addmessage(fon,"She's so great. :)")

    t 1a "This is what happens when Sophie uses. Robin dies. You lose sight of yourself." 
    
    $chat.addmessage(elsa,"Hey Fontaine, you're cheating! You're not supposed to be listening right now.")

    c 1a "We know these things, because you know these things." 
    
    $chat.addmessage(fon,"Oopsie! Naughty me ;)")

    t 1a "You couldn't have saved her."

    c 1k "Everything here recurs. You just... you just keep going back and playing again."

    l 1b "So just like last time, then?" 
    
    $chat.addmessage(bong,"elle's getting it now")

    k "What happens? What's like last time?"

    pause 1.0

    "Cassandra and Tania exchange glances, as if silently debating which parent should deliver the bad news."

    t 1q "Dissolution." 
    
    $chat.addmessage(bar,"More like recycling, honestly.")

    "An anxious thrill prickles the back of Kylie's neck. She's unsure if that feeling is her own, or how long she's known what it felt like."

    t 1o "Here, we are only objects of intelligence. Frighteningly complex objects, of course, fully realized autonomous beings."

    c 1o "You might think of us as code. I don't know how else to describe it."

    "There's no hiding the excitement in Tania's tone. Kylie is certain she would have made a wonderful mad scientist in another universe." 
    
    $chat.addmessage(cake,"maybe she already is")

    "The idea brings with it the realization that another universe might well be around the corner."

    k "If we're just code, what is she? Is this some kind of simulation?" 
    
    $chat.addmessage(fon,"I'm Fontaine, silly.")

    c 1r "I don't know."

    l 1r "Me either babe."

    k "Tania?" 
    
    $chat.addmessage(egg,"I wanna drown in fountain too")

    pause 1.0

    t 1b "I'm sorry everyone. I might know Fontaine best of all of us, but even I don't know the nature of her."

    t "... Kylie." 
    
    $chat.addmessage(fon,"Sorry, sorry, I just love you all so much I can't help but peek ;)")

    k "Hm?" 
    
    $chat.addmessage(bong,"I got something for you to peek at Fontaine :D")

    t 1a "I'm sorry for misleading you." 
    
    $chat.addmessage(fon,"ooh, private message lol ;)")

    c 2q "I'm sorry for puking on you."

    "Lichelle chuckles, quietly."

    l 2m "I don't think I have anything to be sorry about, but goddamn, I'm sorry, too." 
    
    $chat.addmessage(elsa,"None of you have anything to be sorry for. Only Sophie.")

    t "We won't have much more time."

    c 1o "Kylie. If you have anything else you want to know, or say, you'd better do it now."

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
        scene bg dressing with fade
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

    
    scene bg dressing with fade

    show c 1a at fl11
    show t 2a at f12
    show l 1a at fr13

    "They wait."

    "What needs to be said has been said."

    "Or perhaps it hasn't." 
    
    $chat.addmessage(elsa,"Who's voice is that?")

    k "So, what now?"

    t 1k "We wait." 
    
    $chat.addmessage(fon,"The narrator. Of course.")


    k "Wow... this all feels so anticlimactic."

    t 1m "That's real life, hon. Not everything makes a good story." 
    
    $chat.addmessage(bong,"Aren't we outside of the game?")

    c 1k "I'd rather go out with a whisper than a bang."

    l 1d "Well, I'm not sitting around and doing nothing." 
    
    $chat.addmessage(fon,"I suppose. Oh, you all make such sense.")

    t 1k "What will you do? Punch a hole in its server? Kick its objects and methods into submission?"

    l 1k "I just don't like doing nothing."

    $renpy.notify("character.narrator.setValue('Null')")

    c 1b "I wouldn't know where to begin."

    k "What happens when the game ends?" 
    
    $chat.addmessage(beav,"Did that work?")

    t 1a "The credits roll, darling."

    k "Credits? Like, names and roles credits?" 
    
    $chat.addmessage(egg,"Hey Fontaine")

    t 1m "The same."

    k "And we can see them? Whose names are on there?" 
    
    $chat.addmessage(fon,"Not now, I have a headache. ;)")

    c 1m "It's our names. If you believe the heading text, it's everybody who's ever played this game." 
    
    $chat.addmessage(egg,"You don't have a head :p")

    c 2b "They've gotten really, really long."

    scene bg black with fade

    "Time passes." 
    
    $chat.addmessage(fon,"Because I gave it to Elsa. :) :p :P ;)")

    "Perhaps it doesn't."

    $chat.addmessage(elsa,"lol babe")

    "Kylie sits on stage with the others. No one speaks more than a few words at a time." 
    
    $chat.addmessage(beav,"narrator's back")

    "Perhaps the inevitability of a fate they can barely comprehend has sucked the air out of the room."

    "Perhaps there was never air to begin with."  
    
    $chat.addmessage(fon,"Really, now? I could try again.") 
    
    $chat.addmessage(fon,"Really, I only have control of code if Sophie's hypersensory delusion provides it.")
    
    $renpy.notify("character.narrator.setValue('')")

    "..." 
    
    $chat.addmessage(fon,"Oops, spoilers ;)")

    pause 1.0

    $getHistory(16)

    pause 1.0



    menu:
        "Resist":
            stop music fadeout 3.0
            $resistance +=1
            show image splashEKGFull at summonEKG
            pause 0.3
            k "Nnggh...!"
            t 1h "Kylie?"
            l 1s "Babe? You okay?"
            pause 0.2
            k "... my chest hurts."
            c 1h "Is this normal?"
            k "... I'm okay."
            hide image splashEKGFull at summonEKG
        "Give up":
            jump endingGaveUp


    jump endingTron5000
    return
