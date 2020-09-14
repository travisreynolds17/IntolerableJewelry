label fontCommon1:
    pause 1.0

    "We touch the tourmaline sliver of tourmaline... something."

    "We?"

    pause  1.0

    scene bg playhouse near with longFade

    "..."

    ff 1i "This place is {i}not{/i} Sophie's mind!"

    un "Who's there?"

    show r 2d at center with dissolve

    play music robin

    r "Show yourself."

    "..."

    ff "The intoxicating witch?"

    ff 1q "We wonder what sort of memory we've discovered!"

    pause 1.0

    r "Who are you?"

    "We find ourselves looking around, wondering to whom this frightening woman refers."

    r 2a "... {i}Parlez-vous français?{/i}"

    "She... is looking directly at us."

    r 1a "{i}¿Hablas español?{/i}"

    pause 0.1

    r 2b "{i}Vorbiți românește?{/i}"

    pause 0.1

    ff 1b "Are... you speaking to us?"

    r 2a "So you do speak English. Are you one of my father's hands?"

    ff 1l "We are Fontaine L'eau. We learned this very recently."

    "She {i}can{/i} hear us! And see us! This magnificent witch!"

    r "Answer. Are you my enemy? How many are with you?"

    ff 1h "We are multitudinous, we think."

    "Her eyes sweep the playhouse floor, from pit to mezzanine."

    "The easy charm from earlier has given way to the fearful alert of a spooked grey wolf."

    hide r with dissolve

    "She's leaving!"

    ff 1i "Wait! We want to talk with you!"

    scene bg black with longFade

    "We follow the mystifying witch onto the stage, exhilarated!"

    "The deep red curtain hangs heavily from the... roof? We suppose?"

    "We quite enjoy the feel of this material against our fingertips."

    pause 1.0

    scene bg black with longFade
    stop music fadeout 6.0

    ff 1m "Where are you witch-Robin? We wish to speak with you!"

    "There are no lights in this place."

    "Such a strange feeling! We never needed lights before."

    "We don't think so, anyway."

    show robinEyes at foreverFade3(640)

    "We?"

    ff 1n "Witch? Robin? We only wish to speak!"

    pause 1.0
    $temp = False
    while temp == False:
        menu:
            "We do not understand. What must this place be?"

            "We have collided with another anomalous existence!" if fontCommon1Choice[0] == False:
                ff 1i "Gasp! Could that be?"
                ff 1b "... we may not feel this solitude, if that were true."
                $fontCommon1Choice[0] = True
            "This must be Sophie's dream! It has become self-aware!" if fontCommon1Choice[1] == False:
                ff 1k "... we wonder about that."
                ff 1i "Oneironaut? We are no such thing! We are Fontaine."
                $fontCommon1Choice[1] = True
            "Is this a false reality? Is this a simulation?" if fontCommon1Choice[2] == False:
                ff 1h "But what existence could craft such a thing?"
                ff "..."
                ff 1i "Did we create this place by mistake?"
                $fontCommon1Choice[2] = True
            "We feel Sophie's presence everywhere. Is this her living mind?" if fontCommon1Choice[3] == False:
                ff 1b "The jewelry Sophie mentioned hangs heavily in our heart!"
                "Is it the evolution of the human brain? A catalyst?"
                "Does it translate our presence somehow?"
                $fontCommon1Choice[3] = True

        if fontCommon1Choice[0] and fontCommon1Choice[1] and fontCommon1Choice[2] and fontCommon1Choice[3]:
            $temp = True
    
    pause 1.0

    "..."

    ff 1m "Oh! Hello there. We see you!"

    ff "We..."

    show r knife at center with dissolve
    hide robinScaryEyes with dissolve

    pause 1.0

    ff 1h "Knife?"

    show r knife2 at zoomStab(640)
    pause 2.0
    scene bg black with stabFlash

    pause 2.0

    "... w-w-w-w-w-w-w-what?"

    ff 1f "We are... we are bleeding! We... we are stabbed!"

    ff 1i "... the witch has gone away."

    ff 1f "She has committed violence against us!"

    "..."

    ff 1h "..."

    ff 1m "Ahahahaahaha!"

    ff 1n "Hahahahahaha!"

    ff 1b "Ahahahahah!"

    ff 1f "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    window hide

    # texting. toPost is a list of messages. each will appear at some random point determined by randomXY function.
    python:
        toPost = [
            "We hurt",
            "We suffer",
            "We bleed!",
            "We die?",
            "We?",
            "Witch?",
            "Agony?",
            "Louisa?",
            "Who is Louisa?",
            "haHAhahahHaahaha",
            "Knife?",
            "suffer suffer suffer",
            "Tania? We don't want you to die!",
            "Sophie? We... help us!",
            "Lichelle, beautiful, beautiful!",
            "Elsa? PLEASE! HELP!",
            "Cassandra we need you!",
            "Please Please Please Please",
            "We hurt",
            "We suffer",
            "We bleed!",
            "We die?"
        ]
        postMax = len(toPost)
        i = 0

    while i < postMax:
        $temp = randomXY()

        show text toPost[i]:
            xpos temp[0] ypos temp[1] alpha 0.0 zoom 1
            linear 0.6 alpha 1.0 zoom 5
            linear 0.1 alpha 0 zoom 1
        pause 0.7
        $i += 1

    pause

    show text "... open your eyes.":
        xpos 0.5 ypos 0.5 alpha 0.0
        easein 2.0 alpha 1.0

    scene bg playhouse far with longestFade

    play music robin

    show r 2b at foreverFade2(640)

    window show 

    "..."

    ff 1c "[][][][]?"

    ff 1b "... we live?"

    "We have never felt such a thing before! We don't think so, anyway."

    "Darkness was over us. It recedes! We are horizontal."

    "Upon the floor?"

    "..."

    "Our pretty shirt is ruined."

    r "Do. Not. Move."

    pause 0.1

    ff 1i "Witch? Hello! We see you."

    r 2r "Why do you still breathe?"

    "We sit up, slowly. It feels difficult?"

    ff 1i "Gasp! Our skirt was not ruined!"

    r knife2 "Answer!"

    pause 1.0

    ff 1h "We aren't entirely sure of that, ourself!"

    ff 1m "We never breathed before."

    r knife "... are you a demon?"

    ff 1h "We don't think so. We are learning much today."

    pause 1.0

    r 1a "... I apologize for the offense my left hand has committed against you."

    r 1b "I... found no weapons on you. Nobody else is here."

    r 1c "I am so, so sorry for searching you!"

    pause 0.5

    "The witch seems uncharacteristically flustered!"

    ff 1m "We don't mind. We've lost nothing! Except blood."

    ff 1n "And we have no need for that!"

    pause 0.5

    r 2o "Please. You must tell me what you are."

    pause 0.5

    ff 1b "We don't know."

    "The witch offers us her right hand! It's... it's beautiful!"
    "It does not have a knife in it."

    menu:
        "What should we do?"
        "Take her hand":
            "We place our hand, we DO have hands, into hers!"
            "Witch-Robin pulls us to our feet, easily."
            "... she smells good. We approve of her lavender flower smell!"
        "Stand up on our own!":
            "If her left hand possesses such power, is her right even more dangerous?"
            "We believe taking such a risk would be a poor choice."
            "We have made such good choices today!"
            "And so we stand. On our feet! Which we have."

    r 2o "... you were crying."

    ff 1h "We?"

    r 2b "You aren't human."

    ff 1b "We aren't, are we?"

    r "I stabbed you thirty-seven times."

    ff 1i "Is that a lot of stabbing us?"

    r 1a "It is... excessive, yes."

    ff 1m "Thank you so much! We feel undeserving of so much effort from you."

    r 2r "I... are you here to kill me?"

    stop music fadeout 1.0

    pause 1.0

    play music fountainWater fadein 1.0

    ff 1h "..."

    pause 0.5

    show r 2a

    pause 0.5

    ff 1m "We... aren't sure."

    ff 1b "What if that's our entire purpose? We cannot comprehend this place."

    ff 1c "We do not want that!"

    stop music fadeout 1.0


    pause 0.5

    r 2b "... you said your name is Fontaine."

    play music darkNoodle

    ff 1n "It is! We know about names!"

    pause 0.5

    r 2o "Clearly."

    r 1a "Where did you get your name?"

    ff 1m "We... heard someone say it."

    ff 1b "... she died."

    r 2b "Was she a friend?"

    pause 0.1

    ff 1c "No. We did not know her. She sat on the rim of a fountain."

    ff 1h "She looked like you. Her hair was different. Orange. Brown? Liquer?"

    ff 1k "Her chest was flatter."

    pause 0.1

    r 2t "Strange."

    r 2a "What do you mean, she looked like me? I find myself... unlike the people in this part of the world."

    pause 1.0

    ff 1i "Well!"

    ff 1l "She was tall! Not as tall as you. Taller than us!"

    ff "We look to the floor and our cute sandals and it is not that far!"

    pause 0.5

    r 1o "... they are very cute sandals."

    ff 1s "Her hair was styled the same way. A strong side part on the left!"

    ff 1i "Pale!"

    ff 1u "... pretty."

    show r 1i 

    pause 0.5

    r "I'll ask you again."

    r 2b "Are you a demon, Fontaine?"

    ff 1b "If we were, would that make you happy? We would like you to be happy."

    show r 2c

    scene bg black with dissolve
    show r 2c at center with dissolve
    stop music fadeout 6.0

    ff 1i "What? No, no! We are not ready for the shard to dissolve!"

    hide r with dissolve

    ff 1d "NO! NO NO NO NO NO!"

    scene bg cubes3 with dissolve

    pause 0.5

    ff 1b "..."

    ff "We wanted to speak with the witch more!"

    ff "We weren't lonely!"

    ff 1i "We?"

    "..."

    "The splinters of sweet Sophie's fragmented consciousness glimmer around us."

    show f 1b at center with dissolve

    "... we can see ourself, suspended within the fractally infinite void."

    "Our hands and arms are... bandaged?"

    "But... beautiful Robin stabbed us in the chest and belly."

    "Why are we bandaged around the arms?"

    pause 0.5

    scene bg black with dissolve
    
    show flipBook with dissolve

    pause 1.5

    ff 1i "What?"

    ff "We see what could be?"

    ff 1f "Or what has been?"

    pause 0.5

    ff 1i "Is that... us?"
    hide f with dissolve
    hide flipBook with dissolve

    scene bg cubes4 with dissolve

    ff 1b "We... have observed confusion."

    ff "We have observed futility. We have observed waaaaaaaaaaaaaaaaaait. Wait!"

    ff 1i "Was that Robin? Dear witch Robin lying... lying dead, soaking wet?"

    ff 1f "Was it Robin in the fountain, after all?"

    ff 1d "We refuse this!"

    ff 1e "We {i}require more memories!{/i}"

    scene bg cubes2 with dissolve

    default fontCommon1 = False

    while fontCommon1 == False:
        ff 1g "... the wreckage of Sophie's obliterated consciousness twinkles at our feet."
        if fontRoute21 and fontRoute22 and fontRoute23:
            menu:
                # In which fontain tours the set of one-week Waifu. She's there for bits of common1. Meets Kylie while she's in the wrings.
                # Then, meets up with Robin and offers to help her with her light show. 
                # Fontaine is already affected by Sophie's love for Louisa, so she cares about Robin.
                "Oh? What's this one?"
                "An... interdimensional sound stage?":
                    ff 1i "W-w-w-w-what?"
                    ff 1m "It appears to be a compound of some sort for creating video entertainment."
                    ff 1i "It has merged with Ganymead? It {i}is{/i} Ganymead?"
                    $fontCommon1 = True
                    jump fontCommon2
            $fontCommon1 = True
        else:
            menu:
                "They each display some scene."
                "Midnight Outside Ganymead" if fontRoute21 == False:
                    # call lichelle + robin scene. they meet. Become friends.
                    "A colonial-era bar. An inexplicable betrayal. A broken heart."
                    call fontRoute21 from _call_fontRoute21
                    
                "A Mansion in North Carolina" if fontRoute22 == False:
                    # call Sophie + tania. Sophie and Tania (the real Tania, not Elsa.) They're getting ready to go on a trip. Tania is killed on this trip after a car crash. This is why Sophie started using.
                    "A venerable house. Two shattered bonds. A broken body."
                    call fontRoute22 from _call_fontRoute22
                "The Annihilation of Cass" if fontRoute23 == False:
                    # cassandra struggling with her recovery. Meets Robin. They don't speak, but Cassandra's energized by her. 
                    "An extraordinary talent. A lost muse. A broken mind."
                    call fontRoute23 from _call_fontRoute23
        # end of second three routes If statement