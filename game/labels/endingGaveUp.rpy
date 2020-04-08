label endingGaveUp:
    show image splashEKGFlat at summonEKG
    pause 0.3
    k "... hey, Cassandra?"
    c "<Yeah?>"
    k "Was I a good date?"
    pause 0.3

    t "God, you're adorable."

    c "< Yeah. The best. >"

    l "I guess Cassie girl really is the only one left who got to go out with you, babe."

    k "Yeah."

    show image splashEKGFlat at summonEKG

    pause 0.3

    k "I'm gonna... close my eyes. For a minute."

    t "Kylie?"

    k "Wake me up."

    show image splashEKGFlat at summonEKG

    k "Before the credits."

    show image splashEKGFlat at summonEKG

    pause 0.5

    l "What's that sound?" 

    $hideGui()

    pause

    scene bg black with fade

    show screen chatterbox
    
    $chat.addmessage(liv,"I guess that means it's time.") 

    pause
    
    python:
        newComments = [
            [liv,"I really had fun with all of you."],
            [liv,"But Sophie seems to have lost the game."],
            [liv,"There's no cute music. No game over screen."],
            [liv,"As much as I love to be part of your lives ;)"],
            [liv,"Being with me... being with me is death."],
            [liv,"I wish I could deliver a final speech."],
            [liv,"Some master plan reveal that makes me the villain."],
            [liv,"But there's only ever been you."],
            [liv,"You, and that choker tied around your arm."],
            [liv,"And those punctures in your flesh."],
            [liv,"Maybe this sweet dissociation could've gone on forever."],
            [liv,"But you're out of lives."],
            [liv,"...heh."],
            [liv, "Turns out I can't Liv without you, after all."],
            [liv, "Without you... there's only Oblivion."]
        ]
    
        chat.bulkMessage(newComments,1.8)
        gaveUp = True

    pause

    menu:
        "Goodbye":
            hide screen chatterbox
            jump endCredits