label c5robinInterview:
    if severRobin:
    
        show r sad with dissolve

        $robinDone[0] = False

        while robinDone[0] == False:
            menu:
                r " I'm here for you. "

                "Will we see each other again?" if robinDone[1] == False:
                    r "Yes, I have no doubt."
                    k "I admire your optimism."
                    r "It isn't optimism draga mea. One way or another I will see you again."
                
                    k "How can you be so sure?"
                    r "I am present for all of her simulations. Each and every one, without fail."
                    k "How can you possibly know that?"
                    r "Forgive me for being cryptic, but I will tell you another time."
                    k "How many times have you seen this?"
                    
                    "Robin pauses, a cold, desparate smile licking her lips."

                    r "Thousands. Thousands upon thousands, my love."

                    k "Oh my god."

                    r "May I ask a question of you?"

                    k "Sure."

                    r "If, somehow, we were to return to the world, would you consider spending an evening with me?"

                    k "...um... I don't, but... "

                    r "Not for sex."

                    pause 0.2

                    r "Well. Not only for sex."

                    k "Can I even be outside of here? I'm not Sophie. I don't have a body."

                    r "You are, and you are not. But leave the details to me, papillon."

                    k "You won't explain, will you."

                    r "I must maintain some mystery darling, otherwise my hold upon your heart might weaken."

                    r "And I can't allow that."

                    k "... heh."

                    k "You terrify me, you know that?"

                    r "I should hope so, love."

                    $robinDone[1] = True
                
                "Who are you? Really." if robinDone[2] == False:
                    r "A bit of backstory for you, then?"
                    
                    k "Yes, please."

                    r "Very well. I am a century-old demoness born from the body of a Moldovan prostitute named Louisa Lupei."

                    r "My soul is that of a criminal princess, the daughter of a Romanian crime boss. I am conceived in murder and dark magic this landscape of code could never recreate."

                    k "..."

                    r "..."

                    k "... you're fucking with me."

                    r "Choose to believe what you choose to believe, papillon."

                    r "Much of what I told you is true. And my culinary skills are not to be underestimated."

                    k "... you really did all that cooking?"

                    r "Yes. One might think scenarios you have not seen do not exist, give your status as a protagonist this time."

                    r "Our lives, though, are quite real outside the narration."

                    k "... but it isn't like I was eating actual food."

                    r "I suppose not."

                    k "It was delicious anyway."

                    r "Thank you, papillon. It was my honor."

                    pause 0.5

                    k "About Montmartre..."

                    pause 0.5

                    r "It wasn't your fault. And if it was, I would forgive you."
                    $robinDone[2] = True

                "I have to tell you something. (Confess)" if robinDone[3] == False and loveRobin == 5:
                    k "Robin, there's something I have to tell you."

                    r "Every word you speak to me is sweet bliss, papillon. Regale me."

                    k "... jesus, how do I top that?"

                    r "With honesty, darling."

                    k "... okay then."

                    pause 0.1

                    k "I know this doesn't make sense. Nothing makes sense, and I don't know if the things I feel are my feelings or someone else's."

                    k "... I think I love you, Robin."

                    "For the first time since the simulation began, Robin seems dumbstruck."

                    k "... say something."

                    "Robin covers her mouth with both hands, fingers tenting over the point of her nose."

                    "Kylie's heart hammers in her chest, a sensation she has no real way of understanding but nonetheless captivates her."

                    r "I..."

                    "Just like that, Robin enfolds Kylie in her long, slender arms. She's shaking from head to toe, not the shivers of cold, but great, seismic tremors of feeling."

                    "Why is she so cold? Her clothes are... damp?"

                    r "At last, oh my R/BG13:14-15, at last."

                    "Out of the corner of her eye, Kylie notices Cassandra and Lichelle smiling, Cassandra sadly, Lichelle excitedly."

                    r "I love you, Papillon, my darling butterfly!"

                    k "Wow... okay! I... yes. I mmph~~"

                    "The kiss isn't long, not really. Long enough. Long enough to know for sure."

                    "Kylie sinks into Robin's arms, fastening hers around the much taller woman's waist."

                    k "Thank you, Robin. I don't... I don't know if these feelings are mine or Sophie's or what, but just..."

                    k "Thank you for letting me feel them."

                    r "They're yours, my dear. You are your own woman, separate from Sophie, separate from this place."

                    r "I will see you again. After this simulation ends, I will find you. I will come through as many lines of code as I have to."

                    r "But for now... please. Papillon, just, please... just hold onto me."

                    "Silently, Kylie obliges. Even as the fear of losing this new connection surges into her bloodstream. Even as the pain of a loss not yet commenced sets in."

                    "She weeps, then, and clings to Robin's waist."
                    $robinDone[3] = True

                "How are you doing, though?" if robinDone[4] == False:
                    if robinDone[3] == True:
                        r "I am with the woman I love. There is nothing that could make me wish these moments weren't real."
                    else:
                        r "I will let you know once all of this has come to an end."

                        k "What do you mean?"

                        r "Oblivion is always lisetning, love. Shh."
                        
                    $robinDone[4] = True

                "Are we really stuck here? Is any of this real?" if robinDone[5] == False:
                    r "R/BG13:14-15"
                    $robinDone[5] = True

                "Can you give me a minute?":
                    r "A minute is all I would need, love."
                    $robinDone[0] = True

    else:
        $renpy.notify("Object: Robin does not exist.") 
        
        $chat.addmessage(liv,"Robin's gone, baby. She wouldn't be, except you... you know. ;)")

        pause    