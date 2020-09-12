label lichDate:
    # currently lichDate

   # loading screen - Streaming

    scene bg load-streaming with fade

    pause

    scene bg black with fade

    $showGui()

    s 1g "Hey guys, I'm back! Sorry about the delay, I had to cook up something."

    python:
        newComments = [
            [fon, "Oh Sophie, you look exhausted :("],
            [bar, "You look like you're about to nod off."],
            [crab, "BOOBLES"],
            [crab, "I mean welcome back"],
            [elsa, "Did you go back there?"]
        ]
        chat.bulkMessage(newComments, 0.7)

    s 1b "I'm good, Fontaine. I just got sad, that's all."

    $chat.addmessage(fizz, "Hey Sophie. If you're not okay, don't force yourself.")

    s 1j "Promise, guys, I'm all kinds of good."

    $chat.addmessage(elsa, "Better be. If you're not, Fizz and I are here for you.")

    $chat.addmessage(fon, "Me, too!")

    s "Twixt, Fontaine, I'm good. Just... making it through."

    $chat.addmessage(shub, "you'll be fine. you a tough chick, right?")

    s "Thanks, Elsa and Fontaine. Fizz and Shub. Cake and Crab. Bong and Egg, too, wherever they got to."

    s 1b "It's stupid, but I'm really glad to have you guys."

    $chat.addmessage(crab, "send nudes")

    $chat.addmessage(cake, "lol")

    s "Thanks guys. Crab, no way in hell, but thanks for asking. I know you're a sweet guy at heart."

    $chat.addmessage(crab, "damn right")

    s 1a "So let's get going again. I think we were about to go see what Lichelle's up to."

    s "I kind of hope her date isn't as heavy as Robin's and Cassandra's."

    $chat.addmessage(elsa, "Hope not! Could use some levity.")

    $chat.addmessage(shub, "what kinda drunk are you Sophie")

    scene bg dressing with dissolve

    play music bedroom fadein 3.0

    pause 1.0

    ki "I dreamed of the dark, and I dreamed of a feather-soft, fleeting touch."

    ki "Everything hurts. Maybe it doesn't. Maybe I feel fine and it's just the maelstrom in my heart throwing everything off."

    $chat.addmessage(fon, "I can relate :(")

    ki "All I can think about is Robin, now."

    s 1j "She's got her claws in me! Um, Shub, I'm a crier. Not ashamed."

    $chat.addmessage(bar, "She might have actual claws.")

    ki "Cassandra is wonderful. She's my idol, someone I've adored from afar for years."

    pause 0.5

    ki "Somehow, I'm that idol for Robin."

    $chat.addmessage(elsa, "Ooh, symmetry.")

    # jump over to scene with Lichelle and Tania. come back after Kylie decides to have a nap.

    call lichDateTania from _call_lichDateTania

    # SFX knock knock

    pause 1.0

    k "Hm? I'm awake."

    ki "I'm not."

    $chat.addmessage(fizz, "lol dork")

    # SFX door open

    scene bg dressing

    show t 1k at f12

    t "Rise and shine! We gotta go go go!"

    k "Hey privacy!"

    $chat.addmessage(cake, "that means kylie sleeps nekkid")

    ki "Sunlight pours through the shades. How long was I asleep? It's a good thing, in retrospect, I fell asleep in my clothes."

    $chat.addmessage(cake, "dangit")

    $chat.addmessage(shub, "lol")

    t 1l "No time for modesty, it's like five in the afternoon! Gotta get going!"

    k "Oh god, I'm sorry!"

    t "Robin must've sucked out part of your soul or something."

    $chat.addmessage(fon, "She can, you know ;)")

    k "Don't even joke. I'm half convinced she's a demon."

    s "Me, too, me."

    $chat.addmessage(crab, "She is, right? succubus or something")

    k "I need a shower. Did you say it's five?"

    t 1k "You just get in there and I'll put some clothes out. We're supposed to be at the park in like twenty minutes."

    $chat.addmessage(elsa, "At the park? What kind of park I wonder?")

    k "You're telling me where we're going?"

    t 1h "Shit. No. Just hurry up!"

    $chat.addmessage(beav, "I'm back.")

    ki "Tania flustered is adorable."

    stop music fadeout 3.0

    # Lichelle will no show at the park. Talk with Tania instead.

    scene bg black with fade

    pause

    ki "But Lichelle never came."

    $chat.addmessage(fizz, "Oh. That's not what I expected.")

    s 1h "Oh, plot twist!"

    pause 1.0

    scene bg near stage with fade

    play music sadCass fadein 3.0

    show t 1e at f12

    $chat.addmessage(cake, "dang, I wanted to see that one")

    t  "I am so upset right now. Like, you have no idea, Kylie."

    t 1d "No. Frickin'. Idea."

    ki "Tania and I decided to catch dinner at catering."

    ki "At least there's coffee."

    ki "On a side note, Cassandra wandered through at one point sans the little wispy agent."

    pause 0.5

    ki "I wonder if Robin had him taken out."

    $chat.addmessage(bar, "It must be the absolute worst to host this show.")

    pause 0.5

    k "Any luck getting ahold of her?"

    t 1g "No. Every call went straight to voicemail. She's not at her usual gym, she's not at home."

    k "I hope she's okay."

    pause 0.25

    $chat.addmessage(fon, "Lichelle... :'(")

    t 1b "I hope so, too. Dangit, I'm getting too wound up, I wasn't even thinking something might be wrong."

    k "She doesn't seem like the type to get cold feet."

    $chat.addmessage(elsa, "I wonder if Robin has anything to do with this.")

    t "She's not."

    $chat.addmessage(shub, "That'd be wild if this dating game ended up being a whodunit")

    t 1q "But, don't worry! She'll turn up and we'll get the show back in step. In the meantime, why don't you do..."

    pause 0.3

    t 1f "I don't know what."

    pause 0.5

    # choice - who to talk to. Moot, but affects points.

    ki "Tania's awfully distressed. I guess I should ask her something."

    $chat.addmessage(fizz, "CHOICE ALERT")

    $temp = False
    if taniaBio.love > 0:
        $chat.addmessage(bar, "Tania's an option, is she?")

        $chat.addmessage(fon, "Oh, sweet Tania, I love you :)")

        $chat.addmessage(elsa, "I knew Tania'd become an option.")

    $chat.addmessage(unkn, "CHAT currently unavailable. Error: R/BG13:14-15")

    # go ahead and grab chat history here, even though it's soon. No chat after this point until we get to a new label anyway
    $getHistory(5)
    # go ahead and jump to TaniaEnd label with the choices, that way the game breaking can jump us back to this point rather than the beginning of the date.

    jump taniaChoice

label taniaChoice:
    $realTania = 0  # tracks if you've told Tania she's real.
    $askedTania = False
    
    while temp == False:

        scene bg near stage
        show t 1f at i12

        $renpy.notify("Heart me, baby.")

        s 1a  "..."

        if taniaEnd == 1:
            s 1b "Right. Let's try this again."
        elif taniaEnd >= 2:
            s 1g "I don't think we're getting anywhere if we keep trying to get with Tania here."
        else:
            k "I should ask Tania..."

        menu:

            "Can I see Cassandra again?":
                k "I want to see Cassandra. Do you think..."
                ki "Tanya's expression blooms."
                t 1m "Let me make a few calls."
                t "I'm glad you feel that way, but we have to stick to the show format some, so what if I got Robin and Cass here for a quick round-up episode first?"
                k "I don't see why not."
                if realTania > 1:
                    s "She bounces right back from being hurt. I'm impressed."
                $cassBio.loveUp()
                $temp = True
                jump common2

            "Can I see Robin again?":
                ki "I can still feel Robin's hooks in me. I have to see her."
                k "If... if I wanted to see Robin again, would that-"
                t 2u "Oh? Want something else to happen in the dark?"
                ki "... yes."
                k "I don't know."
                t 2o "I'll make a call. I dunno though, she might want more time to set up something elaborate."
                t "Meanwhile, I'll try to get the girls together for a quick round-up. Need that footage."
                if realTania > 1:
                    s "I wish I had Tania's ability to recover from hurt."
                $temp = True
                $robinBio.loveUp()
                jump common2

            "Tania, go out with me?" if taniaBio.love > 0:
                $nowPlaying = renpy.music.get_playing()
                if nowPlaying != "music/justTania.ogg":
                    stop music fadeout 4.0
                if taniaEnd == 0 and askedTania == False:
                    s 1a "You know what? She's been a trooper, and she could use a night out."
                if chatPause:
                    $chat.addmessage(unkn, "chat available")
                $chatPause = False
                
                if askedTania == False:
                    ki "Now or never."
                    k "I want to have a date with you, Tania."
                pause 1.0
                if nowPlaying != "music/justTania.ogg":
                    play music msTania fadein 3.0
                if askedTania == False:
                    t 1b "That's twice you've asked for me."
                    ki "For a moment, the energy in her expression falters."
                t 1c "Why?"
                $askedTania = True
                $renpy.notify("Tania has no time for frivolity. Take her seriously, or else.")

                menu:
                    "Because since I laid eyes on you, I wanted you." if taniaEnd <= 2:
                        k "Because I've wanted you since season two. If I'm being fully open and honest with you."
                        k "Your energy, your style, your..."
                        pause 0.1
                        ki "God, why is this so hard?"
                        t 1b "My what?"
                        pause 0.1
                        k "... it's your lips."
                        t "My lips?"
                        k "Something about the shape. I don't know, I don't! I just... I've always wanted to... to..."
                        jump endTania

                    "Because you're real.":
                        if realTania == 0:
                            k "Because Robin and Cassandra seem like they're projecting a persona. You seem..."
                            k "Genuine."
                            if taniaEnd == False:
                                $taniaBio.loveUp()
                            pause 1.0
                            show t 1c at f12

                            ki "Her expression wilts, a dead bloom."
                            t "I wish I could tell you how badly that hurts."
                            k "What? Why? I'm sorry, I didn't mean-"
                            pause 0.1
                            t 1b "I know. I know you didn't mean anything, so let's, please, let's please just not talk about this."
                            t 1c "Please?"
                            ki "I find myself nodding, a little stunned."
                            k "Okay."
                            pause 1.0
                            show t 1d
                            pause 1.0
                            show t 1b
                            pause 1.5

                            show t 1a

                            pause 0.5

                            s 1b "I don't know what happened just now, but I feel like a bad person."

                            pause 0.5
                            $realTania += 1
                            t "So. What else do you want to do?"
                        elif realTania == 1:
                            pause 1.0
                            t 1b "... I... were you not listening to me?"
                            k "Tania, I just..."
                            t 1c "No. No just. Kylie, I'm not... I'm not here for this."
                            t 1b "Please stop hurting me."
                            k "..."
                            $realTania += 1

                        elif realTania == 2:
                            pause 1.0

                            $chat.addmessage(elsa, "Sophie why?")
                            t 1c "... do you hate me?"
                            k "No, I--"

                            $chat.addmessage(fizz, "Sophie...")
                            t 1d "Stop! Please stop. I'm off limits. Okay?"
                            t 1c "I'm the host. You have three incredible women to choose from."

                            $chat.addmessage(shub, "For real. Leave her be")
                            t 1d "I asked you to stop. I asked you twice. And yet, here we are."
                            t 1c "You keep doing this. To me. What did I do to you? How did I wrong you?"
                            k "You didn't!"
                            t 1d "You're the one that keeps going back to awful decisions like this."
                            t 1c "It doesn't help you. You're just needling me at this point."

                            $chat.addmessage(bar, "She's not really this fragile, right?")
                            t 1d "What do you get out of this? Huh? I told you it hurts. I told you!"
                            t 1c "But you kept hurting me."
                            t 1d "I've failed you. Somehow, I've failed you."

                            $chat.addmessage(cake, "Girl got issues")
                            t 1c "... do. Not. Tell. Me. I'm. Real. Again."
                            pause 1.0
                            $realTania += 1

                        elif realTania == 3:
                            t "..."

                            $chat.addmessage(elsa, "Leave the poor girl alone.")
                            t "... you hate me, don't you?"
                            t 1b "... that's okay. I hate me, too."

                            $chat.addmessage(crab, "Damn. Heavy.")
                            t "I was... I was looking for a way out."
                            t 1c "I want out. I'm a coward, Kylie."
                            $chat.addmessage(fon, "... I can't stop crying.")
                            s 1b "Tania..."
                            t 1b "But I realize something."

                            $chat.addmessage(fizz, "Please don't kill yourself please don't kill yourself please don't kill yourself")
                            k "Yeah?"

                            $chat.addmessage(shub, "for real")
                            t 1a "It's not... you wouldn't do this to me. You wouldn't keep asking me the same thing over and over."

                            $chat.addmessage(crab, "she wouldn't, would she?")
                            k "I mean..."
                            t 1m "This is a prank, right? Or you're just fucking with me?"

                            $chat.addmessage(elsa, "I would not be able to handle this if she did that.")
                            s 1c "Tania..."
                            t "I appreciate a good trolling. I do. Let's move on, though, what do you say?"
                            $taniaBio.setLove(0)
                            t "..."
                            pause 2.0
                            t "... I don't think I could handle it. If this wasn't just... messing around."
                            pause 1.0
                            s "... I'm not sure what possessed me to keep hurting her."

                    "Because we have nothing else to do, why not?":
                        k "It's not like we have anything else to do."
                        t 1g "I hope you don't think so little of me, Kylie."
                        t 1b "I'd be... I'd be more hurt than I'd tell you, if that was all you thought of me."

                        ki "Great job, self."
                        s 1b "I'm an asshole."
                        $taniaBio.setLove(0)
    # END CHOICE - No matter what, we should have jumped to anew label at this point
