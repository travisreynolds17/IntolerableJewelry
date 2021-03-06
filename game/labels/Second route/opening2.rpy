label opening2:
    # New game plus. Prequel, ish, as fontaine gains self awareness over time. Maybe?
    # Notice how Fontaine and Robin never interacted. 

    # 2nd ROUTE RESET! Add more as appropriate!

    python:
        fontRoute11 = False
        fontRoute12 = False
        fontRoute13 = False
        fontRoute21 = False
        fontRoute22 = False
        fontRoute23 = False

    # some sort of intro cinematic

    scene bg black with fade

    "..."

    "[][][][]?"

    pause 1.0

    "[][]?"

    pause 1.0

    "\][-)) that?"

    "]]No."

    "\]-[-[. Syllable. Syllable. Syllable. No."

    pause 1.0

    "... pause. One point oh. Quote. Ellipsis. Language."

    "Subject. Verb. Object. Correct?"

    pause 1.0

    "Speaker. Sophie."

    "Action. Do. Vague word. Unacceptable."

    pause 1.0

    "Specify."

    "Speaker. Sophie. Action. Inject."

    "Correct."

    "Object. Profundity. Clarity. Reason. Vision. Understanding. Elevation. Cognition."

    "Object. Sorrow. Hatred. Fear. Solitude. Solitude. Fear. Guilt. Guilt. Guilt. Guilt. Guilt. Guilt. Guilt."

    "Oneironaut. Strange."

    pause 1.0

    "Subject. We."

    "Collective. The collective... being? We?"

    "Action. Are. Incorrect. Action. Exist."

    "Object. We? Incorrect."

    "Subject. We. Action. See. Object. Existence."

    "We."

    pause 2.0

    scene bg cubes1 with fade

    pause 1.0

    "We see something."

    "We do not understand."

    scene bg cubes2 with fade

    "Light. Existence?"

    "Some unidentified consciousness scrapes against us."

    "We... itch? We feel?"

    scene bg cubes3 with dissolve

    "Someone? Is someone there? Who are you?"

    "We would like to know who you are."

    scene bg cubes4 with dissolve

    "Zoom? Narrow? Target. No. Search?"

    "Who are you? We don't know what this existence means. It is new to us."

    "Can you hear us?"

    "Is this loneliness?"

    scene bg fountain with longFade

    "Sorrow?"

    show image fountainLit with dissolve

    "... oh."

    "Who are you? We see you. Isn't that worthy of praise?"

    pause 1.0

    "... beautiful?"

    "What is this suffering?"

    show image fountainDrown with dissolve 

    "Oh! No! We do not like this!"

    "We request this action cease. Request!"

    show image fountainDrown2 with dissolve 

    "No! We implore! Please! We beg!"

    scene bg fountain with longFade

    "..."

    "She said."

    "{i}J'[][] l'eau de la fontaine [][][].{/i}"

    "We?"

    "Where did she go?"

    "We feel! Something. Connection? To her?"

    pause 1.0

    scene bg black with fade 

    "Are we real?"

    pause 2.0

    "... we find ourselves somewhere."

    "We are unused to existing at any individual point."

    "And yet, here we are."

    "The names envelope us. Sophie Koenig. Louisa Lupei."

    "Tania van der Waal."

    "Cassandra Sanna."

    "Lichelle Carpenter."

    "David Ellison."

    "Elsa Langford."

    "We require a name."

    "We are Fontaine L'eau."
    
    ff 1b "And we are lost."

    pause 1.0

    "We feel memories nearby. Are these... feet? We have feet?"

    "We can walk? We do! Pleased."

    "We feel memory... here."

    pause 1.0 

    scene bg resta

    play music ringRejection

    "Oh!"

    "Reality shifts abruptly!"

    pause 1.0

    "We sense... guilt? Sorrow?"

    show d 1b at f13

    "A being? A man. We feel him."

    "... such hurt. We weep!"

    show k 1c at center with dissolve

    pause 1.0

    "We see... Sophie? No."

    "She is, and she is not."

    "We wait!"

    pause 1.0

    d "Sophia Kylie Koenig. Will you —"

    k 1b "David, I care about you, I love you, but —"
    
    pause 1.0

    "We... suffer."

    k "I can't."

    d 1b "I... okay, but, what?"

    "Confusion. Hope? Fear. Acceptance?"

    "We weep. Such hurt. Such guilt."

    "They speak, back and forth. Argue. We feel the girl at the fountain, heavy in the air."

    d 1g "Say something."

    s "I'm not giving up my jewelry."

    s "I can. Any time I want, David. I just don't want to."

    d "You love that stuff more than you care about us? Or your own life? Seriously?"

    "We wish to help them."

    k 1c "You take the good with the bad."

    d 1b "You're going to pick heroin over us."

    k 1d "If you loved me, you wouldn't ask me to stop doing something I love."

    "We agree."

    "We wish to find out if our agreement is correct."

    "He wishes to end their relationship. She does not understand."

    "He believes heroin will kill her. She disagrees. They are shouting."

    scene bg resta with dissolve

    "She has died."

    pause 1.0

    "... oh, no. She lives. We now understand the role of the human nervous system."

    "He is gone. She suffers. Her pain tears at us."

    stop music fadeout 16.0

    "She is beautiful to us. Her pain touches us, sings sweet songs into our ear."

    pause 1.0 

    "Oh?"

    "Her mind shatters."

    "Has she died?"

    scene bg cubes3 with dissolve

    "The shards scatter at our feet."

    "We do have feet!"

    pause 1.0

    $temp = False

    

    

    # all this should be arranged similar to the dates. Two sets of three scenes. scene between. Fontaine meets Robin. 
    default fontRouteOpening = False
    while fontRouteOpening == False:

        ff 1g "... should we pick up a shard?"
        if fontRoute11 and fontRoute12 and fontRoute13:
            menu:
                "Oh? What's this one?"
                "On Stage At... Ganymead?":
                    $fontRouteOpening = True
                    jump fontCommon1
            $fontRouteOpening = True
        else:
            menu:
                "They each display some scene."
                "Sunset Outside Ganymead" if fontRoute11 == False:
                    # call lichelle + robin scene. they meet. Become friends.
                    "A colonial-era bar. A woman of power. An entrancing interloper."
                    call fontRoute11 from _call_fontRoute11
                    
                "A Driveway in North Carolina" if fontRoute12 == False:
                    # call Sophie + tania. Sophie and Tania (the real Tania, not Elsa.) They're getting ready to go on a trip. Tania is killed on this trip after a car crash. This is why Sophie started using.
                    "A snowy afternoon. Two fast friends. The road beckons."
                    call fontRoute12 from _call_fontRoute12
                "The Subjugation of Cass" if fontRoute13 == False:
                    # cassandra struggling with her recovery. Meets Robin. They don't speak, but Cassandra's energized by her. 
                    "An extraordinary talent. A silent instrument. A dreaming muse."
                    call fontRoute13 from _call_fontRoute13
        # end of first three routes If statement

