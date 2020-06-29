label endTania:
    show t 1r at f12
    # if we've gone through this choice once already, freeze the chat so messages don't repeat.
    if taniaEnd > 0:
        $chatPause = True
        $chat.addmessage(unkn, "chat unavailable")
    else:
        $chat.addmessage(unkn, "chat available")

    t "... to what?"

    $chat.addmessage(beav, "Friggin' chat not workin")
    k "Do I have to spell it out?"

    $chat.addmessage(bar, "There it is.")

    ki "For just a second, I think I might have to spell it out."

    $chat.addmessage(elsa, "Good. Without chat, how are Shub and Crab gonna fawn over flirty women?")

    t 1p "Really?"

    $chat.addmessage(shub, "Quietly lol")
    k "Really."
    pause 0.5
    t "But the show..."
    k "Forget the show. Let's go to my dressing room."

    show t 1o

    $chat.addmessage(fon, "I love when Kylie's assertive")

    if taniaEnd == 0:
        s "Oh my god, did I win?"

    t "This doesn't really feel earned, but..."
    t 1n "Okay."
    if taniaEnd == 0:
        s 1a "Okay, I think I won!"
    ki "Tania's gentle fingers brush my palm as she slides our hands together."

    $chat.addmessage(cake, "oh my god, really? really really?")
    ki "I take the first step, hoping against hope that she can't feel me trembling."

    $chat.addmessage(beav, "Fontaine said there's no H in this, so... how's it gonna give us the middle finger?")

    scene bg black with fade

    ki "I can hear her breath quickening. I'm not sure how this happened."

    $chat.addmessage(bar, "What's weird is how much I care about Tania, even though we haven't really talked to her.")

    ki "Everything about this has been fast, too fast. Condensed, even."

    $chat.addmessage(fizz, "It's almost like whole courtships have been shoved into a short game.")
    scene bg dressing with fade

    show t 1p at f12

    t "Leave the door open...?"
    k "Oh?"

    $chat.addmessage(crab, "DAMN she freaky")
    show t 1n
    ki "Her smile is bold, now, and bright."
    t "Well. We still have a show to film."

    $chat.addmessage(elsa, "Uh, no?")

    k "You want to film, uh, this?"
    
    
    t 2m "Of course."

    $chat.addmessage(fon, "So exciting!")

    ki "I should have guessed. One of the camera crew has already wedged his way into the doorway, even."

    $chat.addmessage(beav, "Fontaine, how'd I know you'd be into that?")

    k "Well..."


    t 1b "You don't want to?"

    $chat.addmessage(fon, "I told you. ;)")
    pause 1.0

    k "... I don't mind if you don't."

    $renpy.notify("This isn't me")

    $chat.addmessage(beav, "What? When?")

    show t 1m

    ki "There's a gentle rise and fall in her chest, now, less gentle with each passing moment."

    ki "It's now or never."

    $chat.addmessage(fon, "Just now :D")

    show t 1t at f12

    pause 0.2
    stop music
    show image splashErrorTania
    pause 1.0

    if taniaEnd == 0:

        s 1i "Oh what the hell!"

        $chat.addmessage(fizz, "AngeredBeaver, you called it.")

        pause 1.0

        s  "Alright chat, hang on. Looks like this part of the game is broken."

        $chat.addmessage(fon, ":D :D :D :D")

        pause 0.5

        s 1a "I'm counting that as a win, though!"

        $chat.addmessage(crab, "Hey Fontaine, did you know that was gonna happen?")

        s "Lemme try something, guys."

        scene bg black

        pause 1.0
        play music msTania fadein 0.5

        s 1m "Okay, progress."

        $chat.addmessage(cake, "dangit")

        pause 0.3

        stop music

        show image splashErrorTania

        pause 1.0

        s 1k "Damn. Alright, let me reload. One sec."

        $taniaEnd += 1

        scene bg black with fade

        play music msTania fadein 0.2

        $chat.addmessage(fon, "I'll never tell ;)")

        s 1a "I think we should consider that the good ending."

        # if it's second or third go, turn chat back on. Only get history once.
        if chatPause:
            $chatPause = False
        else:
            $getHistory(6)
            $chat.addmessage(unkn, "CHAT unavailable")

    elif taniaEnd == 1:

        $chat.addmessage(unkn, "CHAT unavailable")

        s "You know, I think the code might just be broken."

        pause 1.0
        stop music
        show image splashErrorTania:
            alpha 0 xanchor 0.5 yanchor 0.5
            linear 5.0 alpha 0.1 zoom 5.0
            linear 1.0 alpha 0
            
        pause 1.0

        s "I guess it's always a risk with these indie games."

        pause 0.5

        s 1m "Maybe it's just Tania being so shy she breaks the game."

        $taniaEnd += 1

        hide image splashErrorTania

        scene bg black with fade

    else:
        s 1d "Fluck! Flock! Flick!"

        s "We're just gonna... that's, we're just gonna move on."

    jump taniaChoice
