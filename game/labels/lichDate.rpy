label lichDate:
    #currently lichDate

   #loading screen - Streaming

    scene bg load-streaming with fade

    pause 4.0

    pause

    

    $showGui()

    s "Hey guys, I'm back! Sorry about the delay. I wantcha to know I'm a bit tipsy on some negroni."

    python:
        newComments = [
            [liv, "Oh Sophie, why drink? Are you unwell? :("],
            [bar, "You didn't drive I hope."],
            [crab, "BOOBLES"],
            [crab, "I mean welcome back"],
            [elsa, "You see that girl?"]
        ]
        chat.bulkMessage(newComments, 0.7)

    s "I'm good, Liv. I just got sad, that's all."

    $chat.addmessage(fizz, "Hey Sophie. If you're not okay, don't force yourself.")

    s "Promise, guys, I'm all kinds of good."

    $chat.addmessage(elsa, "Better be. If you're not, Fizz and I are here for you.")

    $chat.addmessage(liv, "Me, too!")

    s "No, TwixtBar, I walked. I live two minutes from a little bar I like. I'd never drink and drive."

    $chat.addmessage(shub, "you'll be fine. you a tough chick, right?")

    s "Thanks, Elsa and Liv. Fizz and Shub. Cake and Crab. Bong and Egg, too, wherever they got to."

    s "It's stupid, but I'm really glad to have you guys. Normally we get so many people in here that it's hard to just talk like this, but I think I need it to be this way tonight."

    $chat.addmessage(crab, "send nudes")

    $chat.addmessage(cake, "lol")

    s "Thanks guys. Crab, no way in hell, but thanks for asking. I know you're a sweet guy at heart."

    $chat.addmessage(crab, "damn right")

    s "So let's get going again. I think we were about to go see what Lichelle's up to."

    s "I kind of hope her date isn't as heavy as Robin and Cassandra's!"

    $chat.addmessage(elsa, "Hope not! Could use some levity.")

    $chat.addmessage(shub, "what kinda drunk are you Sophie")
    
    scene bg dressing with dissolve

    pause 1.0

    ki "I dreamed of the dark, and I dreamed of a feather-soft, fleeting touch."

    ki "Everything hurts. Maybe it doesn't. Maybe I feel fine and it's just the maelstrom in my heart throwing everything off."

    $chat.addmessage(liv, "I can relate :(")

    ki "All I can think about is Robin, now."

    s "She's got her claws in me! Um, Shub, I'm a crier. Not ashamed." 
    
    $chat.addmessage(bar, "She might have actual claws.")

    ki "Cassandra is wonderful. She's my idol, someone I've adored from afar for years."
    
    pause 0.5

    ki "Somehow, I'm that idol for Robin." 
    
    $chat.addmessage(elsa, "Ooh, symmetry.")

    #knock knock

    pause 1.0

    k "Hm? I'm awake."

    ki "I'm not." 
    
    $chat.addmessage(fizz, "lol dork")

    #door open

    show t angry with dissolve

    t "Rise and shine! We gotta go go go!"

    k "Hey privacy!" 
    
    $chat.addmessage(cake, "that means kylie sleeps nekkid")

    ki "Sunlight pours through the shades. How long was I asleep? It's a good thing, in retrospect, I fell asleep in my clothes." 
    
    $chat.addmessage(cake, "dangit") 
    
    $chat.addmessage(shub, "lol")

    t "No time for modesty, it's like five in the afternoon! Gotta get going!"

    k "Oh god, I'm sorry!"

    t "Robin must've sucked out part of your soul or something." 
    
    $chat.addmessage(liv, "She can, you know ;)")

    k "Don't even joke. I'm half convinced she's a demon."

    s "Me, too, me." 
    
    $chat.addmessage(crab, "She is, right? succubus or something")

    k "I need a shower. How long have we got?"

    t "You just get in there and I'll put some clothes out. We're supposed to be at the park in like forty minutes." 
    
    $chat.addmessage(elsa, "At the park? What kind of park I wonder?")

    k "You're telling me where we're going?"

    t "Shit. No. Just hurry up!" 
    
    $chat.addmessage(beav, "I'm back.")

    ki "Tania flustered is adorable."

    #Lichelle will no show at the park. Talk with Tania instead.


    scene bg black with fade

    pause

    ki "But Lichelle never came." 
    
    $chat.addmessage(fizz, "Oh. That's not what I expected.")

    s "Oh, plot twist!"

    pause 1.0

    scene bg near stage with fade 
    
    $chat.addmessage(cake, "dang, I wanted to see that one")

    show t angry with dissolve

    t "I am so upset right now. Like, you have no idea, Kylie."

    t "No. Frickin'. Idea." 
    
    $chat.addmessage(bar, "It must be the absolute worst to host this show.")

    k "Any luck getting ahold of her?"

    show t disap

    t "No. Every call went straight to voicemail. She's not at her usual gym, she's not at home."

    k "I hope she's okay."

    pause 0.25

    show t sad 
    
    $chat.addmessage(liv, "Lichelle... :'(")

    t "I hope so, too. Dangit, I'm getting too wound up, I wasn't even thinking something might be wrong."

    k "She doesn't seem like the type to get cold feet." 
    
    $chat.addmessage(elsa, "I wonder if Robin has anything to do with this.")

    t "She's not." 
    
    $chat.addmessage(shub, "That'd be wild if this dating game ended up being a whodunit")

    show t

    t "But, don't worry! She'll turn up and we'll get the show back in step. In the meantime, why don't you do..."

    pause 0.3

    show t disap

    t "I don't know what."

    # choice - who to talk to. Moot, but affects points. 

    ki "Tania's awfully distressed. I guess I should ask her something." 
    
    $chat.addmessage(fizz, "CHOICE ALERT")

    $temp = False 
    if loveTania >0:
        $chat.addmessage(bar, "Tania's an option, is she?") 
        
        $chat.addmessage(liv, "Oh, sweet Tania, I love you :)") 
        
        $chat.addmessage(elsa, "I knew Tania'd become an option.")

    
    
    $chat.addmessage(unkn, "CHAT currently unavailable. Error: R13:14-15")

    # go ahead and grab chat history here, even though it's soon. No chat after this point until we get to a new label anyway
    $getHistory(5)

    while temp == False:
        k "I should ask Tania..."
        menu:

            "Can I see Cassandra again?":
                k "I want to see Cassandra. Do you think..."
                ki "Tanya's expression blooms."
                show t happy
                t "Let me make a few calls."
                t "I'm glad you feel that way, but we have to stick to the show format some, so what if I got Robin and Cass here for a quick round-up episode first?"
                k "I don't see why not."
                $loveCass += 1
                $temp = True
                jump common2

            "Can I see Cassandra again?":
                ki "I can still feel Robin's hooks in me. I have to see her."
                k "If... if I wanted to see Robin again, would that-"
                show t flirty
                t "Oh? Want something else to happen in the dark?"
                ki "... yes."
                k "I don't know."
                show t speak
                t "I'll make a call. I dunno though, she might want more time to set up something elaborate."
                t "Meanwhile, I'll try to get the girls together for a quick round-up. Need that footage."
                $temp = True
                $loveRobin += 1
                jump common2

            "Tania, go out with me?" if loveTania > 0 and taniaEnd == False:
                s "You know what? She's been a trooper, and she could use a night out."
                ki "Now or never."
                k "I want to have a date with you, Tania."
                pause 1.0
                t "That's twice you've asked for me."
                show t sad
                ki "For a moment, the energy in her expression falters."
                t "Why?"
                $renpy.notify("Tania has no time for frivolity. Take her seriously, or else.")

                menu:
                    "Because since I laid eyes on you, I wanted you.":
                        k "Because I've wanted you since season two. If I'm being fully open and honest with you."
                        k "Your energy, your style, your..."
                        ki "God, why is this so hard?"
                        t "My what?"
                        k "... it's your lips."
                        t "My lips?"
                        k "Something about the shape. I don't know, I don't! I just... I've always wanted to... to..."
                        jump endTania

                    "Because you're real.":
                        k "Because Robin and Cassandra seem like they're projecting a persona. You seem..."
                        k "Genuine."
                        $loveTania += 1
                        pause 1.0
                        show t heartbroken with dissolve
                        
                        ki "Her expression wilts, a dead bloom."
                        t "I wish I could tell you how badly hearing that hurts."
                        k "What? Why? I'm sorry, I didn't mean-"
                        show t sad with dissolve
                        t "I know. I know you didn't mean anything, so let's, please, let's please just not talk about this."
                        t "Please?"
                        ki "I find myself nodding, a little stunned."
                        k "Okay."
                        pause 1.0
                        show t sad with dissolve
                        pause 1.0
                        show t disap with dissolve
                        pause 0.5

                        show t with dissolve

                        pause 0.5

                        s "I don't know what happened just now, but I feel like a bad person."

                        pause 0.5

                        t "So. What do you want to do?"


                    "Because we have nothing else to do, why not?":
                        k "It's not like we have anything else to do."
                        show t disap
                        t "You might not, but I have a hundred things to do. I'm sorry, Kylie."
                        $taniaLove = 0
                        ki "Great job, self."
    # END CHOICE - No matter what, we should have jumped to anew label at this point

    scene bg black with fade