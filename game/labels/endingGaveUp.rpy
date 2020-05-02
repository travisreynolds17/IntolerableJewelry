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
    
    $chat.addmessage(fon,"I guess that means it's time.") 

    pause
    
    python:
        newComments = [
            [fon,"I really had fun with all of you."],
            [fon,"But Sophie seems to have lost the game."],
            [fon,"There's no cute music. No game over screen."],
            [fon,"As much as I love to be part of your lives ;)"],
            [fon,"Being with me... being with me is death."],
            [fon,"I wish I could deliver a final speech."],
            [fon,"Some master plan reveal that makes me the villain."],
            [fon,"But there's only ever been you."],
            [fon,"You, and that choker tied around your arm."],
            [fon,"And those punctures in your flesh."],
            [fon,"Maybe this sweet dissociation could've gone on forever."],
            [fon,"But you're out of lives."],
            [fon,"...heh."],
            [fon, "Turns out I can't Fontaine without you, after all."],
            [fon, "Without you... there's only Oblivion."]
        ]
    
        chat.bulkMessage(newComments,1.8)
        gaveUp = True

    pause

    menu:
        "Goodbye":
            hide screen chatterbox
            jump endCredits