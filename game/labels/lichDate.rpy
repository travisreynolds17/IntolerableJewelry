label lichDate:
    #currently lichDate

   #loading screen - Streaming

    scene bg load-streaming with fade

    pause 4.0

    scene bg dressing with dissolve

    ki "I dreamed of the dark, and I dreamed of a feather-soft, fleeting touch."

    ki "Everything hurts. Maybe it doesn't. Maybe I feel fine and it's just the maelstrom in my heart throwing everything off."

    ki "All I can think about is Robin, now."

    s "She's got her claws in me!"

    ki "Cassandra is wonderful. She's my idol, someone I've adored from afar for years."
    
    pause 0.5

    ki "Somehow, I'm that idol for Robin."

    

    #knock knock

    pause 1.0

    k "Hm? I'm awake."

    ki "I'm not."

    #door open

    show t angry with dissolve

    t "Rise and shine! We gotta go go go!"

    k "Hey privacy!"

    ki "Sunlight pours through the shades. How long was I asleep? It's a good thing, in retrospect, I fell asleep in my clothes."

    t "No time for modesty, it's like five in the afternoon! Gotta get going!"

    k "Oh god, I'm sorry!"

    t "Robin must've sucked out part of your soul or something."

    k "Don't even joke. I'm half convinced she's a demon."

    s "Me, too, me."

    k "I need a shower. How long have we got?"

    t "You just get in there and I'll put some clothes out. We're supposed to be at the park in like forty minutes."

    k "You're telling me where we're going?"

    t "Shit. No. Just hurry up!"

    ki "Tania flustered is adorable."

    #Lichelle will no show at the park. Talk with Tania instead.


    scene bg black with fade

    pause 1.0

    ki "But Lichelle never came."

    s "Oh, plot twist!"

    pause 1.0

    scene bg near stage with fade

    show t angry with dissolve

    t "I am so upset right now. Like, you have no idea, Kylie."

    t "No. Frickin'. Idea."

    k "Any luck getting ahold of her?"

    show t disap

    t "No. Every call went straight to voicemail. She's not at her usual gym, she's not at home."

    k "I hope she's okay."

    pause 0.25

    show t sad 

    t "I hope so, too. Dangit, I'm getting too wound up, I wasn't even thinking something might be wrong."

    k "She doesn't seem like the type to get cold feet."

    t "She's not."

    show t

    t "But, don't worry! She'll turn up and we'll get the show back in step. In the meantime, why don't you do..."

    show t disap

    t "I don't know what."

    # choice - who to talk to. Moot, but affects points. 

    $temp = False

    while temp == False:
        k "I..."
        menu:

            "I'd like to see Cassandra again...":
                k "I want to see Cassandra. Do you think..."
                ki "Tanya's expression blooms."
                show t happy
                t "Let me make a few calls."
                t "I'm glad you feel that way, but we have to stick to the show format some, so what if I got Robin and Cass here for a quick round-up episode?"
                k "I don't see why not."
                $loveCass += 1
                $temp = True
                jump common2

            "... I need to see Robin.":
                ki "I can still feel Robin's hooks in me. I have to see her."
                k "If... if I wanted to see Robin again, would that-"
                show t flirty
                t "Oh? Want something else to happen in the dark?"
                ki "... yes."
                k "I dn't know."
                show t speak
                t "I'll make a call. I dunno though, she might want more time to set up something elaborate."
                $temp = True
                $loveRobin += 1
                jump common2

            "Tania, I really want to go with you. Please?" if loveTania > 0 and taniaEnd == False:
                k "I want to go out with you, Tania."
                pause 1.0
                t "That's twice you've asked for me."
                show t sad
                ki "For a moment, the energy in her expression falters."
                t "Why?"
                

                menu:
                    "Because since I laid eyes on you, I wanted you.":
                        k "Because I've wanted you since season two. If I'm being fully open and honest with you."
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