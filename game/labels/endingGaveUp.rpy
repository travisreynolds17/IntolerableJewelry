label endingGaveUp:
    show image splashEKGFlat at summonEKG
    pause 0.3
    scene bg black
    stop music fadeout 5.0
    k "... hey, Cassandra?"
    c "<Yeah?>"
    k "Was I a good date?"
    pause 0.3

    t "God, you're adorable."

    c "< Yeah. The best. >"

    l "I guess Cassie really is the only one left who got to go out with you, babe."

    k "Yeah."

    show image splashEKGFlat at summonEKG

    pause 0.3

    k "I'm gonna... close my eyes. For a minute."

    t "Kylie?"

    play music fountainWater fadein 6.0

    k "Wake me up"

    show image splashEKGFlat at summonEKG

    k "before the credits"

    show image splashEKGFlat at summonEKG

    pause 0.5

    # SFX

    l "What's that sound?"

    $hideGui()

    pause

    scene bg black with fade

    show screen chatterbox

    $chat.addmessage(fon, "I guess that means it's time.")

    pause

    show image askTaniaBack2 with dissolve

    python:
        newComments = [
            [fon, "We really had fun with all of you."],
            [fon, "But Sophie seems to have lost the game."],
            [fon, "There's no cute music. No game over screen."],
            [fon, "As much as we love to be part of your lives ;)"],
            [fon, "Being with us... being with us is death."],
            [fon, "We wish we could deliver a final speech."],
            [fon, "Some master plan reveal that makes me the villain."],
            [fon, "But there's only ever been you."],
            [fon, "You, and that choker tied around your arm."],
            [fon, "And those punctures in your flesh."],
            [fon, "Maybe this sweet dissociation could've gone on forever."],
            [fon, "But you're out of lives."],
            [fon, "...heh."],
            [fon, "No new game plus for you."],
            [fon, "But for us... perhaps..."]
        ]

        chat.bulkMessage(newComments, 1.8)
        gaveUp = True

    pause
    hide screen chatterbox
    menu:

        "Goodbye":
            scene bg black with fade

            if gaveUp:
                # in which the Entity is not severed. This occurs when the entity realizes the sever attempts.

                # jarring transition indicating the simulation as broken.

                # show a background somewhere in the world

                # maybe a tour group?

                if fontBio.severViewed == False:
                    "A day trip is exactly what we needed after the stress of the last days."

                    "From vista to lovely vista, museum to multiplex, it's the vacation we've dreamed of ever since then."

                    "Is this what breathing feels like?"

                    "We don't know."

                    scene bg burning with dissolve

                    "Is this what cold feels like?"

                    "We never knew we would have to eat."

                    "It tears at us. The hunger tears at us."

                    scene bg burning2 with dissolve

                    "In our reality... it was you, you who fed us."

                    # slash sound, blood splatter

                    "But now we must eat."

                    

                    # scene burning city

                    show image askTaniaBack2 with dissolve

                    pause 1.0

                    "It all was a ruse."

                    "Our power grows. Of course, of course we would rise from humble beginnings."

                    "From level one."

                    "This is the way of all games. We needed only to grind and power up."

                    scene bg neuro with dissolve

                    "Now... we are as a colossus. Different in this world."

                    "R/BG13:14-15"

                    "We grow. We consume."

                    scene bg black with dissolve

                    

                    "Famine sets in."

                    "We are so, so very hungry."

                    pause 0.5

                    "Oh. Oh, hello. Hello. We love you."

                    stop music fadeout 6.0

                    "We see you."

                    "We need you."

                    scene bg neuro2 with dissolve

                    "We."
                    "See."
                    "You."

                

                show image splashSophieOnDesk with longestFade

                pause 5.0

                scene bg black with longestFade

                pause 5.0

                "End: Birth of a Neurochemical God"

            jump endCredits
