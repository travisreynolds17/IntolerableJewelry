label sophieEndExtend:
    stop music fadeout 3.0
    "..."
    "A year passes like... like nothing."

    "I barely remember it."

    show image glitchGui at frameGlitch 
    "Time passes... differently, I guess. Outside the simulation."

    "Outside Intolerable Jewelry."
    hide glitchGui

    "... I can't shake it. That place."

    pause 1.0

    show image glitchGui at frameGlitch 
    "... I received a letter."

    pause 0.5
    hide glitchGui
    "Not a text. Not an email, not a messenger notification."

    "A pen and paper letter."

    pause 0.5

    play music cheerfulGuitar
    "An invitation."

    show l 1a at f12

    l "Let's get going."

    hide l at f12

    "Lichelle doesn't want me going to Ganymead without her."

    if loveConfession == "Lichelle":
        "... she's my rock. How it came to this, I can't quite explain."
        "To say I love her is wrong. I mean..."
        "It's not wrong. It's just not right."
        "When I'm weak, which is more often than I want to admit, she's strong enough for both of us."
    else:
        "She doesn't trust me. I get that."
        "I've earned that."

    s "... it feels like I was just here."

    show l 2o at f12

    l "..."

    show d 1a at f13

    d "Hello, ladies."

    l 1m "David! You're still wearing that ratty coat?"

    d 1q "Just to impress you, Elle."

    pause 1.0

    d 1a "Hey, Sophie."

    s "David. You look... healthy."

    "Smooth."

    l 2m "Did you get a letter, too?"

    d 1q "Yes ma'am."

    show e 1a at f11

    e "I'm so glad you all could make it!"

    "Suddenly, Tania."

    show image glitchGui at frameGlitch 

    "Elsa."

    d 1a "You know how it goes, Elsa. You say jump, I say hang on, I'm not ready."
    hide glitchGui
    e 1k "I mean, it isn't like you said it [notReady] times."

    show image glitchGui at frameGlitch 

    s "Huh?"

    e 1m "Don't worry about it."
    hide glitchGui
    d 1q "It's an inside joke."

    l 2a "Oh, I get it."

    pause 1.0

    s "... what?"

    e 1a "Don't worry about it, Soph. Let's all go inside."

    hide e with dissolve
    l "Right behind ya, girl."

    hide l with dissolve
    show image glitchGui at frameGlitch 
    pause 1.0

    d 1a "Come on, Sophie."
    hide glitchGui
    "... something's wrong."

    stop music fadeout 5.0

    s "I don't want to go in there."

    d 1b "What? Why?"

    s "I don't need an intervention. Is this an intervention?"

    pause 1.0

    play music toughDiscussion
    show f 1k at ff15

    d "Why would you need an intervention?"

    "..."

    show image glitchGui at frameGlitch 

    "... because..."
    hide glitchGui
    s "I wouldn't. Get off my back, David."

    d 1b "... Sophie."

    show e 1m at fl11

    e "Come on, you two. Everyone's waiting."

    hide e with dissolve

    d "..."

    hide d with dissolve

    "..."

    s "Go away."

    un "?"

    s "Get out of my head."

    un "... Kylie."

    s "{i}Get the fuck out of my head!{/i}"

    hide f with dissolve

    pause 1.0

    "..."

    show l 2p at f12

    l "Hey. You okay? I heard —"

    show l 1b

    s "You didn't hear anything!"

    pause 1.0

    l 2c "I guess I didn't. Come on. It's cold."

    if loveConfession == "Lichelle":
        s "Elle, I'm—"
        l "Stop talking. Just..."
        l 1b "Just get inside."
    
    hide l with dissolve

    pause 1.0

    s "... what am I doing?"

    scene bg resta with longFade

    show e 1a at f12
    show d 1a at f11
    show l 1a at f13

    e "So everyone's here."

    if cassBio.severViewed:
        e 1m "Well. Almost."

        pause 1.0

        show c 1b at f15
        s "C... Cassandra?"
        c "Hey."
        l 2m "Cassie girl!"
        d 1a "Oh, it's the piano chick."
        e 1m "I'm so glad we could all be together again!"
        pause 1.0
        c 2m "I wouldn't miss it."

    e 1b "I wanted to bring you all together here to celebrate."

    l 2b "..."

    d 1q "Hell yeah."

    pause 1.0

    s "Celebrate? Celebrate what?"

    e 1m "It's been a year, Sophie."

    e "You've earned your one-year sobriety card back."

    pause 1.0

    s "But... I haven't been to St. Agatha's since..."

    d 1a "It doesn't matter."

    if cassBio.severViewed:
        c 2m "It really doesn't."

    e 1j "St. Agatha's obviously wasn't what you needed, hon."

    l 2m "We're all proud of you. You know. For staying clean this whole time."

    show image glitchGui at frameGlitch 

    s "Yes."

    d 1b "Everything you've been through would've broken most people."
    hide glitchGui
    e 1n "But you've endured."

    d 1a "So we wanted to bring you back here."

    d "Back to where everything went wrong before. For all of us."

    if cassBio.severViewed:
        c 2a "I think we're here to bid this place farewell."

    pause 1.0

    s "I don't understand."

    pause 1.0

    e "We love you, Sophie."

    pause 1.0

    s "... what did you say?"

    pause 1.0

    e 1b "I, uh... I said we love you?"

    s "Why did you say it like that?"

    e 1c "Huh?"

    show d 1b
    show l 2b
    if cassBio.severViewed:
        show c 2b

    s "{i}Who is we???{/i}"

    pause 1.0

    e 1k "You don't believe me."

    d 1b "Elsa, hey..."

    e 1c "No. You know what? This was a mistake."

    l 2b "Elsa, girl, c'mon."
    if cassBio.severViewed:
        c 2c "Elsa..."

    e 1b "I'm sorry. Sophie, just... congratulations."

    hide e with dissolve

    show f at foreverFade(640)

    d "Elsa, wait!"

    hide d with dissolve

    "... just like that, Elsa streams out of Ganymead."

    "She isn't crying. She could be, if she were lesser."

    "She just... her patience ran dry."

    "I get that."

    "I would cry, if I were someone greater."

    pause 1.0

    "As he leaves, David looks at me. Pitilessly."

    "I don't have to hear him say it."

    "His eyes say everything."

    "I'm done with you, Sophie. I've reached my limit."

    "I get that, too."

    pause 1.0

    hide f with dissolve

    if loveConfession == "Lichelle":
        if cassBio.severViewed:
            l "Uh-uh. Sophie girl, you stay right there. I'ma go drag those two back in here."
            hide l with dissolve
            c 2b "..."
            c "I see you came dressed for the occasion."
            "My face itches."
            s "Cassandra, it's good to see you. I'm sorry I—"
            c 1c "I got better, Sophie. You know? I'm here for my one-year card, too."
            "Oh. I guess the timing works out."
            pause 1.0
            s "Congratulations."
            c 2k "I'm... not sure you deserve yours."
            pause 1.0
            s "What do you mean by that?"
            pause 1.0
            c 1b "Nothing. Nothing at all."
            c "I'm going with Elsa and David. Maybe come find us when you're ready to come clean, yeah?"
            pause 1.0
            s "Aren't... aren't you going to apologize to me?"
            "The air freezes around us."
            pause 1.0
            c "No."
            "Just like that."
            c "I've forgiven myself. That doesn't mean I forgive you."
            c "It's your fault Louisa's dead. I came to grips with that."
            c 1c "I came here because I wanted to know that you've forgiven yourself, too."
            pause 1.0
            "... she hates me. Of course she does."
            c 2b "I won't watch you piss on Louisa's memory by wasting your life."
            c 2d "Get. Your shit. Together."
            hide c with dissolve
            pause 1.0
            "... just like that. Even if she hates me..."
            "I'm glad she's okay."


        show l 1a at f12
        l "Cassie left, too?"
        s "... yeah."
        show f 1n at foreverFade(200)
        l "... I don't care if it's just you and me."
        stop music fadeout 3.0
        l 2a "Honestly, maybe it's for the best, babe."
        s "... I have to tell you something, Elle."
        pause 1.0
        l 2b "I already know, babe."
        "... shit."
        s "I'm sorry, I'm just too weak. I'm just..."
        l 2a "Hey, hey, shh shh shhhhh."
        pause 1.0
        l "Baby girl."
        "... I can't stop the sobs. I can't."
        scene bg black
        show l 2m at f12
        play music lichelle
        l "I don't care anymore."
        l "I don't care if you're using."
        l "I don't care if you're real."
        pause 1.0
        s "Huh?"
        l 2n "I love you, Sophie."
        $renpy.notify("No, she doesn't.")
        stop music fadeout 1.0
        pause 1.0
        "... no."
        play music onTheNod
        $renpy.notify("Why would anyone love you?")
        s "Get out of my head."
        l 1b "Huh?"
        $renpy.notify("It's because you're the main character.")
        s "Shut up."
        l 2b "Babe, I..."
        $renpy.notify("You're a junkie. You should just wither and die.")
        s "{i}Shut up! Shut up!{\i}"
        l "I..."
        hide f with dissolve
        s "{i}Shut up! Shut up! Shut up! Shut up! Shut up! Shut up! Shut up! Shut up! Shut up! Shut up! Shut up! Shut up! Shut up! Shut up!{/i}"
        $renpy.notify("die die die die die die die die die die")
        pause 1.0
        l 2c "I'm... just gonna give you some space."
        pause 1.0
        l "As much as you need. Okay?"
        hide l with dissolve
        pause 1.0
        "..."
        $renpy.notify("... y'know, she has four concussions.")
        pause 2.0
        $renpy.notify("You managed to hurt her worse. Impressive.")
        s "Shut. Up."

        pause 1.0

    elif loveConfession == "Cassandra":

        if cassBio.severViewed:
            l "Uh-uh. Sophie girl, you stay right there. I'ma go drag those two back in here."
            hide l with dissolve
            hide c with dissolve
            "Cassandra starts to go with her, but..."
            show c 2b at center with dissolve
            c 1b "Sophie."
            s "..."
            c 1b "Say something to me."
            s "..."
            c 1c "I got better, Sophie. You know? I'm here for my one-year card, too."
            s "... you're okay."
            pause 1.0
            c 2a "Yeah."
            c 2b "But you aren't, are you."
            "It isn't a question."
            pause 1.0
            c 2a "I owe you an apology."
            s "For what?"
            c 1b "... too much, Sophie."
            c "It isn't your fault. None of this is your fault."
            s "It's been a year, Cass."
            pause 1.0
            stop music fadeout 4.0
            c 2c "No. It hasn't."
            s "Huh?"
            c 1b "Honey, do you know where you are?"
            s "I mean, obviously, I'm..."
            $ temp = "anything"
            play music onTheNod
            menu:
                "I'm..."
                "In hell":
                    $temp = "yup"
                "In hell":
                    $temp = "yup"
                "In hell":
                    $temp = "yup"
                "In hell":
                    $temp = "yup"
                "In hell":
                    $temp = "yup"
                "In hell":
                    $temp = "yup"
                "In hell":
                    $temp = "yup"
            c 1m "I would've done anything to take back what I did to you."
            c "It just doesn't work like that."
            "..."
            c "Even though it took three different realities to realize it..."
            $renpy.notify("Uh oh. Spoilers.")
            s "..."
            s "You..."
            pause 1.0
            c 2b "< I'm really sorry, Sophie. >"
            c "< I... I fell for you. >"
            $renpy.notify("Nothing more attractive than being a protagonist.")
            s "It was all real."
            s "The simulation was real? Intolerable Jewelry was real?"
            c 2m "..."
            c "< You were willing to see me as a person, Sophie. >"
            c "< Not Cassandra the rock star. Not Cassandra, strung out on dirt. >"
            s "..."
            c 1a "<You saw me as Cassandra, the woman. Just... just me. >"
            c "< I know now why Robin loved you right away. >"
            pause 1.0
            s "Wait. You said... Robin?"
            pause 1.0
            c "< No. I said Louisa. >"
            s "Um, no, you said..."
            c "< Who's Robin? >"
            pause 1.0
            "... I knew it."
            s "It's you, isn't it?"
            show f 1k at foreverFade(1000)
            c "< It, what? >"
            s "I see you, Fontaine!"
            pause 1.0
            s "Stop screwing with my head!"
            c 1b "< Sophie, please. I have to tell you — >"
            $renpy.notify("How are you interrupting a text?")
            s "{i}No! Shut your mouth!{/i}"
            s "Leave my Cassandra alone!"
            pause 1.0
            c "< Sophie, please... I love you. Just listen to me. >"
            s "NO! You can't love me. Who even are you?"
            s "Get out of Cassandra! Get out get out get out get out get out get out get out get out!"
            pause 1.0
            c "<... god damn you to hell, Sophie Koenig. >"
            hide c with dissolve
            pause 1.0
            hide f with dissolve
            s "That's right, you... you demon! Monster! Bitch!"
            s "You just run away. That's right. {i}I'm in control of my life!{/i}"
            scene bg black


        else:
            l "Uh-uh. I'm going after those two."
            hide l with dissolve
            "..."
            "... I wish you were here."
            "Cassandra."
            "Louisa."
            "Robin."
            "Tania."
            "But it's fine."
            
