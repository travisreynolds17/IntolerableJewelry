label c5lichInterview:
    show l sad with dissolve

    $lichDone[0] = False

    while lichDone[0] == False:
        menu:
            l " Hey babe. "

            "Will we see each other again?" if lichDone[1] == False:
                k "Will we see each other again?"
                l "Mind if I be totally honest with you?"
                k "Please do."
                l "I have no idea. Not a clue baby girl. This is the first time I've been on this side of it."
                k "This side?"
                l "Last time all this happened I was in your spot. I didn't handle it as good as you."
                k "I guess I'm not sure I believe any of it. Or maybe I do, it just isn't sinking in."
                l "I punched Robin."
                k "Wait what?"
                l "Yup."
                k "Why?"
                l "It seemed like the right move and I don't really like her. She's kind of this ivory tower chick. Oh she speaks like six languages, so what?"
                k "That doesn't seem like a good reason to hit someone."
                l "It's not. I just freaked the hell out about this, and I was sure she was behind it because she just knows too much."
                l "Don't you think?"
                k "I don't know what to think."
                l "That makes us both. But hey, maybe next time it'll be you and me on this side."
                k "Maybe."
                $lichDone[1] = True
            
            "Who are you? Really." if lichDone[2] == False:
                l "What I told you before was true. I beat girls asses for cash and prizes."
                l "Got my ass beat sometimes, too."
                k "For cash and prizes?"
                l "Damn right."
                l "But then, I guess the damage just added up over time. People don't think about how hard it is to fight."
                k "I can't imagine. I'd be terrified."
                l "It's not just fight day. We're getting tossed around and smacked up every day in training camp, all the time."
                l "And then, for women fighters, we don't get paid shit so most of us have to side hustle, too."
                k "So why fight, then? Why put yourself in that kind of danger?"
                l "I dunno."
                show l disap
                l "I guess I'm supposed to say something about how great comptetition is, or how I'm an adrenaline junkie or how I hate my dad."
                k "Your dad?"
                l "But no, I love my dad. My dad's a sweetie. And I'm afraid of roller coasters."
                k "Really?"
                l "Don't tell Robin. She'll find a way to make the next game we're stuck in a roller coaster simulator or something."
                k "Maybe you just want something to reach for?"
                l "Could be. I guess that's it."
                l "Regardless, that's all over now. Even if I didn't have five concussions, we're stuck in here now."
                k "I haven't minded being stuck with you three."
                l "Likewise, babe."

                $lichDone[2] = True

            "I have to tell you something. (Confess)" if lichDone[3] == False and loveLich == 5:
                l "aa"
                $lichDone[3] = True

            "How are you doing, though?" if lichDone[4] == False:
                l "I got all my crazy out the first time this happened. Guess I should still be freaking out, but it's fine."
                k "That entity thing was controlling you, though."
                l "Yeah, I guess. It's weird having all those voices in my head at once, but they're not too loud."
                l "It's kinda like passing notes more than chatter. I'm not too happy about that hillbilly voice, though."
                k "It was kind of cute."
                l "Y'liked it, darlin'?"
                k "Maybe."
                l "What about you though? You okay?"
                k "I have no idea."
                l "Yeah, that works. Hey if we're in this thing together next time, maybe we'll have a better idea."
                k "Maybe."
                $lichDone[4] = True

            "Are we really stuck here? Is any of this real?" if lichDone[5] == False:
                l "Babe, you are asking the wrong girl about that."
                k "You don't have an opinion?"
                l "I just don't know. I know it feels real. If someone told me we were all kidnapped and drugged up and this stage is just a set somewhere, I'd believe it."
                l "Or maybe it's a crazy elaborate prank. Maybe you three are actors."
                k "Maybe you're an actor."
                l "Fuckin' maybe."
                l "It doesn't matter. You and I can find out for sure on the next go around."
                l "If we see each other and remember any of this, we'll know for sure."
                k "You think it's that simple?"
                l "All I think is this whole situation so nutso that I can't bring myself to be worried."
                k "I can see that."
                $lichDone[5] = True

            "Can you give me a minute?":
                l "Sure babe. If you need something else, grab me. "
                $lichDone[0] = True