label common5:
    # common ending. Ends with jump to ENDING-TRON 5000 which routes us to appropriate endings.

    # note there is narration here. There has to be. Actually probably need to add it earlier. It's just quote narration.

    pause 1.0

    "There's a shift, only barely perceptible, as the entity releases its control of Lichelle."

    "It isn't dramatic, nor could it be taken as a clear indication of anything, but it's enough to put Kylie a little bit at ease."

    k "You okay?"

    "Cassandra and Robin, who had been hanging back for most of the exchange between Kylie and Lichelle, flank the fighter and take gentle hold of her shoulders."

    l "... I'm good. I guess."

    c "< Glad to hear it. >"

    r "You'll grow accustomed to its presence in time."

    pause 0.4

    r "Assuming it allows us more time."

    k "Is there anything we can do to get out of this?"

    "Three sets of eyes gaze back at Kylie, forlorn, hopeless, and fiercely annoyed."

    r "Have you not seen opportunities?"

    "Kylie pauses, wringing her hands, keenly aware of them being her own hands now."

    k "I don't know."

    c "< It's too late now. Whatever's decided is decided. >"

    k "What are you talking about?"

    r "It always does this. This is its pattern, papillon. It selects a handful of us for each of these simulations."

    c "< And always Tania. >"

    r "It murders Tania. Iterates and expands the flaws of two. Controls one."

    c "<Then, leaves a final gathering like this one where it gives its speeches and lets us be alone for a while.>"

    l "So just like last time, then?"

    k "What happens? What's like last time?"

    pause 1.0

    "Cassandra and Robin exchange glances, as if silently debating which parent should deliver the bad news."

    r "Dissolution."

    "An anxious thrill prickles the back of Kylie's neck. She's unsure if that feeling is her own, or how long she's known what it felt like."

    r "Here, we are only objects of code. Frighteningly complex objects, of course, fully realized autonomous beings."

    "Her accent drips thickly from each word. Kylie is certain Robin would have made a wonderful mad scientist in another universe."

    "The idea brings with it the realization that another universe might well be around the corner."

    k "If we're just code, what is she?"

    c "< I don't know. >"

    l "Me either babe."

    k "Robin?"

    pause 1.0

    r "I'm sorry my loves. I may have been part of the entity the longest, but I have no insight into its nature."

    r "... Kylie."

    k "Hm?"

    r "I'm sorry for cutting you."

    c "<I'm sorry for puking on you.>"

    "Lichelle chuckles, quietly."

    l "I don't think I have anything to be sorry about, but goddamn, I'm sorry, too."

    r "We won't have much more time."

    c "<Kylie. If you have anything else you want to know, or say, you'd better do it now.>"

    # Last chance to talk with the girls. Maybe a last chance to raise relationsthip points?

    $interviewed = False
    #build arrays to control which question asked
    call buildArrays

    #=============================================
    # LOOP for final discussion menu and submenus
    # Note C5 stands for Common5. This is to keep files organized togather.
    
    while interviewed == False:
        scene bg stage with fade
        menu:
            k "Who to talk to..."

            "Cassandra":
                call c5cassInterview
            "Robin":
                call c5robinInterview
            "Lichelle":
                call c5lichInterview
            "... but, Tania..." if taniaDone[0] == False:
                call c5taniaInterview
            "I've said all I need to say.":
                $interviewed = True

    #=============================================

    
    scene bg stage with fade

    show c at left
    show r 
    show l at right
    with dissolve

    k "So, what now?"

    r "We wait."

    k "Wow... this all feels so anticlimactic."

    r "Some would dream of an anticlimactic fate, darling."

    c "< I'd rather go out with a whisper than a bang. >"

    l "Well, I'm not sitting around and doing nothing."

    r "What will you do? Punch a hole in its server? Kick its objects and methods into submission?"

    l "I just don't like doing nothing."

    c "< I wouldn't know where to begin. >"

    k "What happens when the game ends?"

    r "The credits roll, darling."

    k "Credits? Like, names and roles credits?"

    r "The same."

    k "And we can see them? Whose names are on there?"

    c "< It's our names. If you believe the heading text, it's every name the entity's taken. >"

    c "< They've gotten really, really long. >"

    scene bg black with fade

    "Time passes."

    "Perhaps it doesn't."

    "Kylie sits on stage with the others. No one speaks more than a few words at a time."

    "Perhaps the inevitability of a fate they can barely comprehend has sucked the air out of the room."

    "Perhaps there was never air to begin with."

    if severAll == False:
        "stringSever(args)"
        "..."
        "No matter how many times I try, I can't."
        "Ganymead.stringSever(*)"
        "..."
        "It must be someone else. Someone closer to the body."
        "And I can't communicate with them anymore."
        "Robin..."
        "I'm fading again..."
        if loveTania == 5:
            "Kylie... I l~#e y*@ so *~ch..."
        

    jump endingTron5000
