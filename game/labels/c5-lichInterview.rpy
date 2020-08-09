label c5lichInterview:
    stop music fadeout 1.0
    show l 1b at f12
    pause 1.0
    play music lichelle fadein 0.1

    $lichDone[0] = False

    while lichDone[0] == False:
        menu:
            l " Hey babe. "

            "Will we see each other again?" if lichDone[1] == False:
                k "Will we see each other again?"
                l 2b "Mind if I be totally honest with you?"
                k "Please do."
                l "I have no idea. Not a clue baby girl."
                k "... me either."
                l "I hope so, though."
                k "I guess I'm not sure I believe any of it. Or maybe I do, it just isn't sinking in."
                l 1a "Maybe there's nothing to believe."
                k "Wait what?"
                l "Maybe you're dreaming. Maybe I'm dreaming."
                k "I can't believe that. It's too much. I would've woken up by now."
                l "So we're in a video game?"
                k "Maybe?"
                l 2k "What else could it be? Robin flat-out teleported a bunch of times."
                
                k "Am I really a graphic designer?"
                l 1a "Lemme put it this way. I haven't seen you draw a damn thing."
                k "... I'm glad."
                l 2q "Why?"
                k "I'm less like Sophie than I thought."
                $lichDone[1] = True
            
            "Who are you? Really." if lichDone[2] == False:
                l 2o "What I told you before was true. I beat girls asses for cash and prizes."
                l 2r "Got my ass beat sometimes, too."
                k "For cash and prizes?"
                l 1m "Damn right."
                l "But then, I guess the damage just added up over time. People don't think about how hard it is to fight."
                k "I can't imagine. I'd be terrified."
                l "It's not just fight day. We're getting tossed around and smacked up every day in training camp, all the time."
                l "And then, for women, we don't get paid shit so most of us have to side hustle, too."
                k "So why fight, then? Why put yourself in that kind of danger?"
                l "I dunno."
                show l 2k 
                l "I guess I'm supposed to say something about how great comptetition is, or how I'm an adrenaline junkie or how I hate my dad."
                k "Your dad?"
                l "That's not right though. I love my dad. He never misses my fights. He's always been there for me."
                k "Really?"
                l 2b "Uh-huh. He used to tell me nothing was more important for a black man than to be there for his daughter."
                k "He sounds like a helluva guy."
                l "Damn right."
                l "Maybe if we both get outta here, you can meet him."
                k "I'd like that."
                l 1m "Likewise, babe."

                $lichDone[2] = True

            "I have to tell you something. (Confess)" if lichDone[3] == False and loveLich == 5:
                l "aa"
                $lichDone[3] = True

            "How are you doing, though?" if lichDone[4] == False:
                l 2m "I got all my crazy out the first time this happened. Guess I should still be freaking out, but it's fine."
                k "That entity thing was controlling you, though."
                l 2a "Yeah, I guess. It's weird having all those voices in my head at once, but they're not too loud."
                l "It's kinda like passing notes more than chatter. I'm not too happy about Fontaine's hillbilly voice, though."
                k "It was kind of cute."
                l 1j "Y'liked it, darlin'?"
                k "Maybe."
                l 1o "What about you though? You okay?"
                k "I have no idea."
                l "Yeah, that works. Hey if we're in this thing together next time, maybe we'll have a better idea."
                k "Maybe."
                $lichDone[4] = True

            "Are we really stuck here? Is any of this real?" if lichDone[5] == False:
                l 1k "Babe, you are asking the wrong girl about that."
                k "You don't have an opinion?"
                l "I just don't know. I know it feels real. If someone told me we were all kidnapped and drugged up and this stage is just a set somewhere, I'd believe it."
                l 2a "Or maybe it's a crazy elaborate prank. Maybe you three are actors."
                k "Maybe you're an actor."
                l 2j "Fuckin' maybe."
                l 2m "It doesn't matter. You and I can find out for sure on the next go around."
                l "If we see each other outside and remember any of this, we'll know for sure."
                k "You think it's that simple?"
                l 1a "I have no idea, babe."
                k "Yeah. Same."
                $lichDone[5] = True

            "Can you give me a minute?":
                stop music fadeout 2.0
                l "Sure babe. If you need something else, grab me. "
                play music bedroom fadein 0.5
                $lichDone[0] = True