label endingTania:

    scene bg resta
    show d 1a at fl11
    show l 1b at f12

    d "Back."

    l 1m "You're just in time. Sophie's about to make a call, and could you just make sure she does it?"

    d 1g "Uh, sure."

    l "You're a decent man, David."

    d 1a "I aim to please, I guess?"

    "Lichelle gives his seat back, brushing it off just as he had for her."

    "I wonder at the nature of their relationship, but it feels overwhelmingly like siblings rather than romance."

    l 1o "I'll talk to both of you later."

    "She touches him lightly on the shoulder as he sits. Maybe I was wrong."

    hide l at fr12

    pause 0.8

    show d 1a at mt2

    d "So, what's this call about?"

    s "... I'm calling Tania."

    d 1b "You mean Elsa?"

    "I find my head shaking before the notion occurs to me."

    s "I can't face her."

    d "Sophie. There is no Tania."

    s "No. I'm calling Tania."

    pause 0.1

    # SFX
    s "OH!"

    d 1j "Phone."

    s "I know, it is. I'm sorry."

    # Maybe a graphic of tania's text?
    s "Huh. I don't know this number."

    show d 1a

    un "Hey. I hope this is the right person. My name is Tania van der Waal."

    "A shock shoots up my spine."
    nvl clear
    nvl show

    t "If you recognize my name, please respond and let me know."

    t "If I have the wrong number, forgive me."
    stop music fadeout 3.0

    t "But I don't think I do."

    nvl hide

    nvl clear

    d 1g "What's going on?"

    s "Tania called ME."

    d 1k "Wha?"
    play music darkNoodle fadein 3.0

    t "Yeah... sorry, hon. Lichelle called me and let me know you were next to your phone."

    show d 1b

    "So much for trust."

    t "I have a proposition for you."

    s "Wait, what?"

    t "I own a place in North Carolina, a refuge I go to when I need to disappear from the world for a few days."

    s "Uh-huh?"

    t "I'd like you to stay with me for a little while."

    s "That's... that's a big ask, Ms. van der Waal"

    t "Tania."

    s "We've never met in person."

    t "... yes, we have."

    show d 1s

    d "What's she saying?"

    s "Not now, David."

    d 1g "Alright. I'll just be looking at boobs or something then. Somewhere."

    hide d with dissolve

    t "Sophie?"

    s "... why should I go?"

    t "Because I believe you. About the simulation."

    s "..."

    t "I can't explain it over the phone. Not in a way that makes sense."

    pause 0.5

    nvl show

    t "I can still feel Fontaine. Creeping around in my head."

    s "You too?"

    t "Yeah."

    t "For weeks. Her stupid little giggle, her compliments, her innuendo. Weeks."

    s "Me, too. God."

    nvl hide

    nvl clear

    menu:
        t "Will you come? I'll pay for a rental car and expenses."

        "Only if David comes, too":
            s "I'll go."
            t "That's-"
            s "David has to go, too."
            show d 1k at f12
            d "Ah?"
            t "We've already been in touch. He agreed weeks ago."
            show d 1a
            s "..."
            t "Don't be mad. You wouldn't return my calls."
            t "Lichelle and Cassandra had a different experience than you. You were at the helm."
            t "I need you."
            pause 0.5
            s "Tell me when."
            t "Right now."
            s "I mean..."
            t "Relax. It'll be fast. It'll be just like a fadeout."
            s "What?"

        "No. I'm not going.":
            s "I can't. No."
            t "Just like that?"
            s "Yeah."
            t "You don't want to talk about the simulation?"
            s "No."
            t "I can force you."
            pause 0.5
            s "What?"
            t "Don't test me, hon. We've been through something incredible."
            t "We have to figure this out."
            s "This call is over."
            t "It's not."
            "Mouth agape with wonder and fury, I tap the big red X on my phone to disconnect."
            pause 0.2
            t "I told you it's not over."
            "Disconnect. Disconnect."
            pause 0.2
            t "Sophie."
            s "What the fuck?"
            t "Language."
            s "How are you doing this? Are we... are we still there?"
            "disconnect"
            t "We're not there, but I can't help you if you don't come see me."
            t "Relax. It'll be fast. It'll be just like a fadeout."
            s "What?"
    stop music fadeout 3.0
    scene bg black with fade

    pause 1.0

    scene bg road with fade
    play music hallwayChats fadein 3.0

    "I must have dozed off again."

    "The drive from home to North Carolina stretches off into eternity. I'm glad David is with me, letting me sleep through most of it."

    "Winter's settled in, carpeting the city with a neat patina of snow."

    "The quiet of a snowy day puts me at ease. At least it used to."

    "I don't know what's waiting for me at the address Tania provided, whether it's even Tania who called me."

    "Not like I know her voice."

    "I guess we can only see."

    scene bg gates with fade

    show d 1a at f12

    d "Tania lives in a mansion? You should've told me you had a rich girlfriend, Soph."

    "We're at the right address. Off the road, gates, with high walls stretchig aroud the property line and..."

    s "Is that a guard house?"

    d 1k "Looks that way. And that would be a security camera."

    "He points, and sure enough, at the corner of the gates before us the cold red eye of a camera gazes unflinchingly."

    "David presses the intercom buzzer by the gate."

    un "Name and business."

    d 1a "Hi, uh, David Ellison and Sophie Koenig. We're hear to see... uh..."

    s "We're here to see Tania van der Waal. We were invited."

    pause 0.5

    "Silence. David presses and releases the buzzer."

    pause 0.5

    un "We're opening the gates. Drive to the front of the house and park in the red zone."

    "The voice is cold, but not in a malicious way. It's very businesslike."

    un "Ms. Koenig will see Ms. van der Waal. Mr. Ellison will receive refreshment in the parlor. Mr. Ellison will not leave the parlor until Ms. Koenig's visit is complete."

    d 1k "Uh..."

    un "These are the terms. If we cannot agree, Mr. Ellison may wait in the vehicle."

    s "David. Do you mind?"

    d 1k "Are you sure we're not being led into an ambush?"

    un "We also will permit Mr. Ellison to wait outside the gate."

    d "In the snow, eh?"

    un "Correct."

    d 1q "I can wait in the parlor, then. What kind of refreshments are we talking about?"

    un "Opening gate. Please stay clear."

    hide d at f12

    # gate sound

    "David guides the car up a long, winding driveway lined with evergreen trees, neatly trimmed."

    "They rather look like Christmas trees."

    "The red zone is easy to find, aflame with blinking crimson lights."

    "David guides the car to a stop, kills the engine."

    s "I really appreciate you coming."

    show d 1a at f12

    d "Hey, look at this place. They probably have the fanciest snacks in there, you couldn't ask for better."

    s "No... really. Thank you. You didn't have to."

    show d 1q

    "He smiles a resigned smile."

    d "If I can't be your husband, I can still be your point man, right?"

    d 1q "Besides. It's nice to score points with Elle."

    "I can only nod. Slowly. I know it stings him, still, but I also know I can count on him."

    "Someday, I hope, I'll find a way to make it right."

    "Until then, I'll keep relying on him."

    scene bg mansion with fade

    show d 1a at f12

    "David whistles, as one should when entering a house like this."

    d 1k "I'll bet my apartment has cheaper utilities, though."

    s "Probably."

    # show robot? Dic bot.

    un "Welcome, Ms. Koenig, Mr. Ellison."

    d 1g "Holy shit."

    stop music fadeout 2.0

    un "Language sir."

    show d 1s at mt1

    pause 0.1

    show m 1a at fr12

    "The little floating ball in front of us hovers into sight as easily as if it were an everyday occurence."

    play music mortimer

    "Its kind of like a floating soccer ball with a cute face."

    un "This unit is designated Mortimer, steward of the van der Waal estate."

    m 1d "May I take your coats?"

    d 1k "Um... nice to meet... you? Yes?"

    s "How?"

    m 1a "I'm kidding. I can't take your coats. I have no hands."

    m 1c "There is a coat rack behind you. Dust off!"

    "David and I stare, still, at Mortimer."

    s "You're a robot."

    m 1a "Correct."

    d 1k "Soph, did you know about this?"

    s "No."

    m 1c "Yes, Ms. van der Waal likes her privacy."

    m "Which is why Mr. Ellison, if you would kindly turn to your left and enter the lit room before you and stay there until you are summoned."

    "A light ticks on, sure enough, to his left."

    d 1g "Alright. Sophie, if you're sure about this, I'll go."

    s "I'm sure."

    m 1a "Quite good. Consume away."

    pause 0.5

    hide d at fl11

    "David gazes at the robot for a moment and then shrugs, turns to the parlor entrance, and promptly is greeted by another floating orb with another cute face."

    un "Mister David, is it? Come this way, we have the best snacks for you. Oh we never get company 'round here, do you like football? We have a guest TV..."

    pause 0.5

    s "..."

    m 1a "He will be fine. The snacks truly are top notch."

    s "How do you know?"

    m 1c "The packaging says so. Now, if you'll kindly follow me? The madam is eager to see you again."

    "Mortimer turns, somehow. It isn't immediately clear how its little body moves."

    "I don't see any kind of propulsion."

    hide m at f12

    "In any other situation I would have ten million questions."

    "Now, I simply follow the floating robo-orb thing down a corridor, lit almost as if it's an afterthought. There are sounds, whirring and grinding, like RC cars racing behind the walls."

    "I see no more robots, though."

    "Maybe that's positive."

    show m 1a at f12

    m "We're here."

    "Mortimer faces a plate to the left of a security door."

    scene bg black with longFade

    # SFX

    "The door slides open."

    stop music fadeout 3.0

    m "In you go."

    "It has to be a trap."

    s "Okay."

    pause 1.0

    "..."

    pause 1.0

    play music ringRejection
    show image splashWired

    hide m

    s "Oh my..."

    "She lies utterly still, draped in a translucent sheet."

    "There is no rise, no fall of her chest."

    show m 1a at fr13

    "The security door slides closed behind me. Mortimer floats past my shoulder, settles above the young woman's feet."

    "Her... her feet."

    "She has no... no feet. No shins, no, no arms."

    "I can't see."

     # with tania. figure this out. the 2 series for mortimer is tania faces


    show m 2a at f13
    "Mortimer's cute face vanishes, replaced abruptly by a familiar one. A woman with a slightly crooked smile, eyes the green of a dewy Scottish glade."

    "She looks like the girl on the bed, but... healthy."

    s "T... no. Tania?"

    

    t "Hey. It's good to see you again, Kylie."

    show m 2q

    t "Sorry. I meant Sophie."

    "My stomach knots."

    t "I guess you weren't expecting this, huh."

    "I shake my head. Words no longer reside in my mouth."

    show m 2a

    t "If it means anything, you're the only person outside my dad's employ who's seen me in years."

    show m 2b

    t "How's my body looking? Probably not as cute as you remember."

    s "... you have no, no legs. No arms."

    s "... what happened to you...?"

    show m 2q

    t "It's a complicated world, isn't it? To have all the money in the world, all the prestige, and yet."

    s "What do you mean?"

    show m 2m

    t "This is who I am. Who I've been the entire time."

    s "Are you... are you awake?"

    t "Technically. I have what's called locked-in syndrome. Part of my brain is disconnected, I guess."

    show m 2j
    t "Wanna see something spooky?"

    hide m at f13

    pause 1.0

    "..."



    show image splashWiredOpen with dissolve

    "Her eyes are open and she's looking right at me. Blinking. Gazing."

    s "W-what does that mean?"
    show m 2a at f13
    t "I'm almost fully paralyzed. I can move my eyes though, and I can see you. And hear you."

    t "Honestly, I'd expected you to ask how I'm talking through Mortimer by now."

    s "I... s-sorry, I, uh, how? You're not... not breathing."

    "How poetic. How empathetic, Sophie."
    show m 2m
    t "I guess it would freak me out, too. I didn't know how to warn you about me."

    t "Nobody knows about me. I'm a black book project."

    s "Tania, what are you?"
    show m 2j
    t "I'm the next step in human evolution. It might not look that way, but it's true."

    t "I'm everywhere. I'm all these machines, Sophie."
    show m 2o
    t "My brain is just a processor, now. Isn't that wonderful?"

    show m 2a

    s "I... don't know. I don't know, Tania."

    s "It's unbelievable!"

    hide image splashWiredOpen with dissolve

    t "You lived inside a simulation for quite a while, yourself. I wonder what is so unbelievable about it."
    show m 2m
    t "Thanks for cracking that open, by the way. I thought Fontaine was going to keep us there forever."

    s "... I need to sit."

    "No sooner than I've said it, a hip-high metal box on wheels skids into sight and unfolds in a dozen directions."

    "It's like watching a rose bloom into a chair."

    t "Sit. Don't worry, I'm very comfortable."

    stop music fadeout 3.0

    "Exhibiting a 'just go with it' attitude far beyond my abilities, I settle carefully onto the robo-chair."

    if loveTania >= 4:
        show m 2u
        t "It's almost like having you on my lap. Almost."
        "I might blush if the oddity of the situation wasn't dominating my mind."

    show m 2a
    
    play music2 msTania fadein 3.0
    
    t "So... I've missed you."
    show m 2p
    t "I know we only really spent a short time together, but I really liked you. I knew you would be the one to get my messages."

    t "And to be strong enough to forgive."

    s "Forgive? What?"
    show m 2r
    t "..."

    s "..."

    t "You don't remember? You don't remember the monologues? The choices?"

    s "No."

    "Tania sighs through the robot, an odd sight at the very least."
    show m 2g
    t "I guess my messages were bypassing conscious thought after all. I worried about that."

    s "I'm so confused."
    show m 2a
    t "Yeah. Well, think of it this way. You might not consciously have saved the day, but the inner you that drives the outer you took care of it."

    s "... what?"

    t "It's hard to explain outside machine language, and I figure you don't speak ones and zeroes."

    # call to q and a session with tania

    call endingGoodTania2

    pause 0.5

    show m 2q

    t "I suppose there's no recovering from all this. Your whole worldview is probably skewed."

    show m 2a

    t "For me, Fontaine's actions changed almost nothing."

    t "..."

    show m 2h

    t "Hey. Hey, don't cry."

    "I didn't realize I was."

    "But I am."

    if loveConfession == "Tania":
        s "Nothing makes sense anymore."
        s "Nothing makes sense!"

        show m 2m
        t "It shouldn't."

        s "Why? Why not?"

        show m 2b

        t "Love doesn't make sense."

        s "Wha?"


        t "You love me."

        s "w-w-w-w..."

        "After everything else she's said, to come out and say it so bluntly, so plainly, I just can't."

        "I can't stop the tears."

        show m 2a

        t "I knew then, you know."

        t "Everything's compounded in the simulation. Everything acts under the rules of a video game, you know."

        t "You were always going to love me."

        show m 2m

        t "Kylie told me so."

        s "You're saying I had no choice in the matter?"

        t "I'm saying you had a choice, but it wasn't you who made it. It doesn't mean the way you feel about me now isn't legitimate."

        show m 2p

        t "It could've been Robin, you know. I imagine she's the most desirable, perhaps even the one Fontaine intended you to fall for."

        "Tania chuckles through the robot."

        show m 2m

        t "How cruel."

        s "I feel sick."

        t "And look, now you're expositing."

        s "No, I think I'm actually gonna be sick."
        show m 2h
        t "Oh!"

        "Just like that, another fold-out robot wheels into sight, becoming a waste basket in a flash. It even slaps a biohazard bag into itself."

        "Mercifully, the lurch in my stomach subsides."

        "I don't stop to think about why those bags are necessary in this place."
        show m 2a

        "Who am I even talking to?"

        "My gaze flits between her face, projected within Mortimer's visor shield thing, and the immobile body all but sewn to its bed."

        s "I do love you. Tania, this, this personality. But what now?"

        show m 2p

        t "It's not as if we can go on a date, right?"

        s "Right."

        t "And if we had a date online, only I could taste. Only I could feel."

        s "Yeah..."

    show m 2m

    t "I wanna show you something."

    s "O-okay."

    t "Follow Mortimer, would you?"

    hide m with dissolve

    "The little robot lifts and floats, still bearing Tania's face, and glides across the room to what would appear to be a closet door."

    "It presses its head to a plate to the side and the door whooshes open with a pneumatic hiss."

    #SFX

    # show body

    s "Jesus!"

    show m 2m at fl11
    t "Do you like it?"

    s "I... no? Yes? What is it?"

    t "It's me. Or it will be."

    s "Is that, is that real skin?"

    show m 2j

    t "No no, you silly thing, it's synthetic. You can't tell the difference, though."

    "I wheel about and stare the Mortimer bot in its face, a gesture I realize may be wholly unnecessary."

    s "How?"

    show m 2m

    t "I have all the money, hon. I have control. Our society has voluntarily tethered itself to computers. Phones, games, musical instruments, vehicles, everything is a computer now."

    show m 2a

    t "I've done nothing immoral or unjust. I just put resources into places that would let me reach this point and... well. There I am."

    s "... it's like I, Robot."

    t "Sort of. I'm not bound by any robotic laws, but I'm still a human mind, Sophie."

    show m 2b

    t "I just want to be able to walk around again."

    # love version

    if loveConfession == "Tania":

        show m 2p
        t "I want to hold your hand and kiss you and smell you."
        t "I can do these things, all of them. If you'll have me, that is."
        s "I can't process this."
        show m 2m
        t "You can! Look at all the processing my brain can do."
        s "That's not what I..."
        "But then, I guess that's exactly what I mean."
        show m 2b
        t "I just need some time. Just a little more time, Sophie. And then, if you truly care about me, I can show you directly how much I care about you."
        s "O-okay. Okay, Tania."

    s "It doesn't mean this isn't unnerving."
    t "My real body is unnerving, too. For now."
    # ----------------------------------------------------
    # ----------------------------------------------------
    if taniaBio.severed == False:
        call endingTaniaBad
    # ----------------------------------------------------
    # ----------------------------------------------------
    else:
        show m 2k
        t "For now, though, I have work to do. I have to ask you to promise me you'll keep all this a secret."
        t "If anyone found out about me or my body here, it could be bad. Government, terrorists, companies, everyone would come for me."
        s "What would happen then?"
        show m 2q
        t "I'm capable of defending myself, but let's not find out, okay?"
        t "Promise me?"
        "Something about that line makes me entirely certain I don't want to spill this secret."
        "I feel... an odd compulsion not to."
        s "I promise."
        show m 2m
        t "Good. You can visit any time, Sophie. I'd be thrilled to have you."
        t "I'm also a surprisingly excellent MOBA player, if you ever want to squad up with me."

        "The robot chuckles."

        show m 2a
        t "Oh."

        t "By the way."

        # Here, we have the diversions for potential sever changes. We know Cass not being severed means she didn't wake up. Lichelle not being severed means she meets up with David in the compound. Robin not being severed ends the same. Waterlogged corpse attack. Tania's stays the same.

        if cassBio.severed == True:
            t "Cassandra's here, too."
            "What?"
            s "What?"
            show m 2a
            t "She's recovering well."
            s "Where is she?"
            if loveConfession == "Cassandra":
                t "Mortimer'll take you there."
                t "She'll be in the music room if she's anywhere. Practicing."
                call endingCass
            else:
                t "She's in isolation, for now. Don't worry. I expect her to be up and about in a week."
        # else for if severCass True
        else:
            show m 2b
            t "I was sorry to hear about Cassandra. Lichelle told me you two were close."
            if loveConfession == "Cassandra":
                s "... I loved her."
                show m 2g
                t "I'm sorry, hon."
                t "Don't blame yourself. She made her own choices."
                s "... I wish I had died instead of them. Louisa. Cassandra."
                show m 2a
                t "You didn't, though. Wishes mean nothing."
                s "Tania..."
                t "I'd have legs, for example."
                s "I'm sorry."
                show m 2m
                t "Don't be. Just live."
                s "... I can do that."
            else:

                s "Not really."
                show m 2r
                t "You were a couple, though?"
                s "It wasn't... it wasn't like that."
                t "No? I must be mistaken then."

        # lichelle endings
        if loveConfession == "Lichelle":
            show m 2q
            t "So I might have misled you earlier."
            t "Someone else is here, too."
            s "Oh? Who?"
            show m 2a
            t "Mortimer will show you to her. Down in the gym."
            pause 0.1
            s "Gym?"
            show m 2m
            t "Yeah. Gym."
            call endingLich
        else:
            if lichBio.severed == False:
                show m 2b
                t "Lichelle is here, too."
                s "Oh?"
                t "She's dead."
                pause 1.0
                s "huh"
                show m 2k
                t "You failed to sever her, Sophie. I sent so many messages."
                s "But I just talked to her a few days ago..."
                show m 2b
                t "Fontaine thought she could hide inside someone else. I guess."
                t "She thought she could hide from me in this world, you know?"
                s "You... did you kill her?"
                t "Lichelle was already gone, hon. Like Cass. Like I would've been if you hadn't saved me."
                t "I just wanted you to know what happened."
                s "... I'm fine with that."
                show m 2p
                t "Oh?"
                s "If it meant stopping Fontaine, I'm fine with it."
                t "Good. I would've killed you, too, if she'd tried to hide in you."
                "I find myself smiling, somehow."
                s "I'd hope so."
                # end of lichelle not severed
            else:
                t "She's in isolation, though. It'll be weeks. I have to ensure she's free of Fontaine's influence."
                s "I understand."

            # robin endings
            if loveConfession == "Robin" and robinBio.severed == True:
                show m 2a
                t "Before you leave, I think you ought to visit the bar downstairs."
                s "I don't want to drink."
                t "David's there, it looks like."
                show m 2j
                t "Someone else is on the way, too. Go talk to her, would you?"
                s "Why are you being so cryptic?"
                show m 2m
                t "Surprises are better left as surprises."

                call endingRobin

         # if no ending has been achieved yet, that means no love confessions and Sophie survived. This might actually be the best ending? Dunno.
         #
         # Here, she wakes up in hospital
         #
        stop music2
        #sfx
        play audio beep noloop
        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        s "Tania? What's happening?"
        play audio beep noloop
        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        show m 2b

        t "Oh. I guess time's up."
        play audio beep noloop
        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        s "What?"

        t "Don't forget us, Sophie. We'll always be with you, one way or another."

        s "I don't understand."

        show m 2c

        t "You can't. Not yet."
        play audio beep noloop
        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        "My vision."

        "Was it ever really mine?"

        scene bg black with fade

        d "Doc. DOC! She's awake!"

        "I know that voice."

        e "Sophie? Hey girl! You..."

        "Something's muffled. Who's crying?"

        d "... scared us all to death."

        "Fizz? Elsa?"

        "My senses are putty, squashed together in an incoherent ball."

        "Suddenly, there are scrubs everywhere."

        "Then..."
        play audio beep noloop
        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        scene bg black with fade
        pause 0.5
        scene bg hospital with fade

        play music hallwayChats

        show d 1a at f11

        d "... and Elle called the ambulance. Then she called Elsa, then me."

        show e 1a at f13

        e "You owe a helluva debt to Lichelle."

        "I do."

        s "Tania. I liked you better as a redhead."

        e 1p "Huh?"

        pause 0.1

        "... oh. That's right."

        s "Am I gonna be arrested?"

        d 1q "For what?"

        s "For giving the heroi-"

        e 1q "FOR DOING nothing like that, ha ha."

        pause 0.1

        "Right. Public."

        d 1g "It's no joke this time, Soph. You screw up again, you're going to prison."

        pause 0.1

        "Don't want that."

        e 1j "Believe me sweety, you're too cute for that. You'll get mauled in there."

        "Don't want that, either."

        s "... where's Louisa."

        d 1b "..."

        e 1h "..."

        e "Sweety. Do you know where you are?"

        s "Y-yeah. I'm..."

        # fontaine shows up in a lab coat
        # SFX - Knock
        pause 1.0


        show f 2m at f12

        stop music fadeout 4.0

        o "Sorry to interrupt."

        d 1a "Oh, uh, hey doc."

        show e 1j

        pause 0.2

        e "Try not to trip over your tongue, David."

        "..."

        o 2a  "Hello again, David. Let's have a little look at Sophie now that she's up and about, hey?"

        s "n-n-no."

        play music onTheNod

        e 1b "Sophie?"

        show d 1b

        s "Get away from me!"

        show f 2b

        o "It's okay, Sophie. I'm here to help."

        s "NO!"

        d 1s "What's gotten into you?"

        "I want to kick, to thrash, to scream."

        "I have no energy. Tubes sink into my arms."

        d 1b "Dr. Fontaine has been wonderful to you, and to us."

        show d 1b 

        s "She's a monster. She's evil!"

        e 1j "She's single, so David might have a biased perspective."

        show f 2q

        d 1b "Shush."

        show d 1b

        s "That's her. That's Fontaine! She killed Robin. {i}She{/i} did it!"

        e 1b "Who's Robin?"

        o 2i "Um, my name is Robin."

        d 1j "You look awfully alive to me."

        pause 0.5

        show e 1k

        pause 0.5

        o 2m "Thank you, David."
        
        o 2r "I think?"
        
        s "David, don't talk to her. She'll... she'll kill you, too!"
        show f 2b
        show d 1b
        show e 1b

        d "Sophie..."

        s "She did it. Fontaine drowned Robin! I saw her body!"

        s "I saw her!"

        pause 0.2

        o 2g "It's not unheard of for coma patients to hear what's said around them."

        s "No, no no. Her name is Fontaine L'eau! It's a trap. {i}Help! Help me!{/i}"

        e 1h "..."

        e 1b "I get it now."

        e "Honey. Please calm down."

        o 2b "I should go. Sophie, I only want to help you."

        s "NO! BITCH! MURDERER!"

        o 2a "Ms. Langford. I'll ask the nursing staff to check up on Sophie shortly. We'll need to run a few tests now that she's awake."

        e 1m "Anything, doctor."

        o "David."

        d 1b "Ma'am?"

        o 2a "May I speak with you privately?"

        d 1k "Anything you need."

        o "Thank you." 

        pause 0.1
        
        o 2b "Sophie, I'm not sure what you think I've done to you but I hope I can erase that perception in time."

        s "stay away, please stay away, please, please-"

        o 2a "I'm going. David, if you please?"

        d 1a "Sure."

        hide f at fr12

        d 1a "Be back soon."

        e 1a "Hey."

        d "Yeah?"

        e 1t "I think she likes you, buddy."

        d 1b "You think?"

        e "Yeah. Don't keep her waiting."

        d 1b "Of course. I'll be back soon."

        hide d at fr11

        e 1u "Not too soon, I hope."

        s "..."

        e 1a "Sophie."

        e 1m "She's your doctor. I've known that lady for a decade. She's normal. Fusses over her hair. Farts when she thinks nobody's paying attention."

        s "... she's horrible. You have to kill her."

        e 1k "For farting? Honey."

        s "She's evil. You have to believe me."

        s "I don't know how she got out of the simulation."

        e 1b "Sophie."

        s "She killed a million people!"

        e "..."

        s "..."
        pause 1.0
        e 1c "Listen to yourself."

        s "..."

        e 1b "Doctor Fontaine cares about you."

        e "I care about you."

        e 1c "Sophie, I -"

        show e 1h

        s "Where's Louisa?"

        pause 0.5

        e 1b "She's gone, honey."

        s "Where."

        e 1a "Hey. Listen. I'll make you a deal."

        s "Deal."

        e 1m "If you just close your eyes and rest, and get better, I promise we'll talk about it."

        s "..."

        show e 1h

        s "She'll kill him. She'll kill David. I saw her. In there. She's a monster."

        e "..."

        e 1b "Just rest. Okay?"

        e "I'm going to go get a soda. And breathe."

        "Her hand slides from mine."

        "I didn't realize it was there."

        "Elsa? Why are you crying?"

        hide e at fr13

        s "... Elsa?"

        s "..."

        stop music fadeout 5.0

        s "Chat's not working."

        "..."

        

        scene bg black with fade
        pause 0.5
        scene bg hospital with fade

        pause 0.5

        show f 2q  at fr12

        if entityForgiven == True:
            # show f
            o "Sophie."

            play music ringRejection 

            s "... get out."

            o "You forgave me."

            

            "There are tears in her eyes. Her breath is quick, her lips trembling."

            o 2b "I was the worst. A monster, truly. A liar. But in there, you forgave me."

            o "Kylie did, anyway."

            s "I knew it."

            o "I've earned your scorn."

            o 2q "But out here, I am doing everything I can to make up for it."

            s "Where's David?"

            o "Resting. He's a beautiful man, Sophie."

            s "Did you..."

            o 2a "I accepted his invitation to dinner, yes."

            s "That's it?"

            o "I want to be better out here. I don't want to just give people pleasures they want, knowing they can't handle them."

            s "..."

            o 2m "He's a good man. He cares about you, and so do I."

            o "So... I hope you're not angry with me for that, at least."

            s "... I can't trust you."

            o 2b "You shouldn't. I deserve that."

            s "I'll kill you myself."

            o "I deserve that, too."

            o 2a "You did everything you could have done to make everything right, Sophie."

            o 2m "Even knowing none of this is real, you put your heart into being a good person."

            o 2n "I love you, Kylie."

            s "... don't call me that."

            o 2q "Why not? It's your name. One of them, anyway."

            s "... am I real?"

            o 2m "As real as anything else, yes."

            show e 1m at fr13

            show f 2h

            e "Hey doc. Where's David?"

            o "Uh, resting."

            e 1j "..."

            o 2q "..."

            e "That was fast."

            o "He asked me out."

            e 1m "Ah."

            o 2i "I didn't do anything."

            e 1n "Ah."

            o 2q "Shush."
            stop music fadeout 4.0
            nvl clear
            nvl show

            "Is it an act?"
            "Elsa trusts her."
            "Am I wrong? Was I ever right?"
            "If... she existed in the simulation, were any of her crimes real?"
            "Do they matter?"
            nvl hide
            nvl clear

            play music bedroom
            s "... I forgive you."

            e "huh?"

            o 2m "I'll earn that for the rest of my life, my Kylie."

            e 1r "I'm confused."

            s "I can't call you Robin. I can't."

            pause 0.4

            o 2b "I know."

            o "I'll have the nursing staff check in on you later, then."

            s "Thanks, Fontaine."

            o 2n "Anytime, love."

            show f at justFade

            "Elsa's looking between us as Fontaine leaves, confusion written on her face."

            show e 1j at mt2

            e 1j "So... besties already?"

            s "I guess."

            nvl show

            "Fontaine's smile retains a shade of sadness. I believe her. I think."

            "She is the entity from the simulation."

            "Alternatively, I talk in my sleep."
            
            "Alternatively alternatively, the jewelry..."
            
            "... the heroin."

            "It doesn't matter."

            "It really doesn't."

            "Things will be different this time."

            nvl hide
            nvl clear

            s "Elsa."

            e "Hm."

            s "I'll never touch that stuff again."

            

            e 1m "Hon..."

            s "I promise. I'll... I'm swearing off. Forever."

            show e 1b

            stop music fadeout 7.0

            "I promise."

            "I promise."

            scene bg black with fade

            pause 3.0

            show screen chatterbox
            pause 0.5

            $chat.addmessage(bong, "lol b00bs lol")

            pause 0.5

            jump endcredits

        else:
            show e 1a at fr12
            e "Hey girl. Sorry to dip out like that."

            s "..."

            e "Dr. Fontaine said she'll postpone the tests until later. She's got David in her office now."

            s "..."

            e 1m "Don't let that bother you. David loves you, no matter what."

            s "... he wanted to marry me."

            e 1a "He did."

            s "I messed that up."

            e 1b "Sophie. You have a disease. A real one."

            s "Nobody ever cooked and shot cancer into their own arm."

            e 1g "Maybe not. I don't mean you shouldn't take personal responsibility. I just mean some aspect of this was always out of your control."

            s "..."

            e 1b "If it means anything, you're young. You have time. Your body is resilient."

            e 1m "Now that it's court-ordered, I'm pretty sure we can kick this heroin thing together."

            s "... I don't know if I can."

            e 1a "Whether you think you can or you can't, you're right."

            s "Did you get that from a self-help book?"

            e "Yoga instructor."

            s "Oh."

            pause 0.5

            e 1b "Sophie."

            s "Hm."

            e "Louisa had a long history of some really bad stuff."

            s "I know."

            e "I don't think you do."

            pause 1.0

            s "... maybe not."

            e 1g "She was a complicated woman. Fierce. Driven."

            s "Yeah."

            e "She had demons you and I can't begin to fathom."

            e 1b "Awful things, Sophie."

            s "Yeah."

            s "... I loved her."

            e 1c "She loved you, hon. She wouldn't shut up about you."

            s "I never deserved her."

            e "Nobody deserves anything. You get what you earn, no matter what."

            e 1a "I'll help you. Okay? We'll get your gaming channel going again, if you want."

            s "... I'd like that."

            e "For now, just rest."

            e "You've earned it."

            pause 1.0

            s "One... one last thing?"

            e 2q "Anything."

            s "Could you call me by my real name?"

            e 2i "Huh?"

            pause 0.1

            s "My name is Kylie."

            k "Is... is that okay?"

            show e 2n

            pause 0.5

            e "I understand. A whole new you, eh?"

            k "Something like that."

            e 1m "Okay, Kylie. I think I can do that."

            #SFX: Running?

            show e 2s

            k "What's all that noise?"

            play music fountainWater

            e 1s "A bunch of nurses just ran by."

            k "..."

            e 1m "Never a dull moment in a hospital, I suppose."

            k "I guess."

            scene bg black with fade

            pause 3.0

            show screen chatterbox
            pause 0.5

            $chat.addmessage(fizz, "*screams*")

            pause 0.5

            jump endCredits

            return