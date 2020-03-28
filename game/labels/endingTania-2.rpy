label endingGoodTania2:
    t "Is there anything I can try to answer for you?"

    $success = False
    while success == False:
        menu:
            t "What would you like to know, Kylie? Uh, Sophie?"
            #----------------
            "What about the others?":
                if taniaExplains[0] == True:
                    t "I think we've covered that pretty well, hon."
                else:
                    s "What about the others? Are they okay?"
                    t "I'll tell you what I know."

                    #show pictures of the other girls on Mortimer's faceplate? In fact, maybe replace newspaper thing with this?

                    t "Let's do alphabetical order. Don't worry, we'll do it right this time!"

                    #-- Cassandra

                    if severCass == True:
                        t "Cassandra spent some time in a safe place after the simulation broke down."
                        s "Safe place?"
                        t "A mental institution. She took quite a lot of pills, Sophie."
                        "My heart freezes."
                        t "No, no no, she's alive. She's okay. Her band manager found her. It's very lucky, actually."
                        s "Cassandra..."
                        t "She's getting the help she needs now, Sophie. She's needed help for a long time, but her touring and recording always got in the way."
                        t "At least, that's what I've gathered since we got free."
                    else:
                        t "About Cassandra... I have bad news, Sophie."
                        s "... tell me."
                        t "She's no longer with us."
                        s "What? Wait, why?"
                        t "She overdosed, Sophie. The autopsy report said it was heroin, cocaine and painkillers."
                        "How... how could she say it so casually...?"
                        s "Why would she do that, though? I thought--"
                        t "Cassandra needed help, Sophie. She wasn't severed when the simulation collapsed, so enough of the Entity's influence was left in her that it broke her completely."
                        s "... you mean I could have saved her?"
                        t "Sophie, do not blame yourself. Do. Not."
                        s "But..."
                        t "You had no conscious control, remember? It just happened this way."

                    if severLichelle == True:
                        t "As for Lichelle, she's doing fine."
                        s "That's a relief."
                        t "She's living in Colorado now, working as a fighting coach and yogi."
                        s "A... yogi?"
                        t "A woman of tremendous violence and also of peace, somehow."
                        t "We've communicated a bit online since the collapse, but mostly it's just been pleasantries."
                        t "I think the wounds are too fresh, still. In Lichelle's game I was a tournament host."
                        t "I put her through some pretty brutal trials, Sophie."
                        s "But that was the Entity's doing, right?"
                        t "Yeah, mostly."
                        t "Some part of me went along with it a little too willingly. But I've made my apologies. I'm also an investor in her business, which is the very least I could do."
                        s "You can invest?"
                        t "I am almost entirely a machine, hon. This stuff is expensive, so I play the markets, make investments and... well."
                        t "Let's say I keep things going comfortably."
                        s "Oh."
                        t "I'll give you Lichelle's contact information. She's eager to hear from you, you know."
                        s "Likewise. Thanks, Tania."
                    else:
                        t "As for Lichelle, she... well, she never woke up."
                        s "What? But..."
                        t "I guess she had so much pre-existing brain damage that she couldn't handle the collapse."
                        t "Her... her daughter found her."
                        s "Lichelle had a kid?"
                        t "Yeah. I'm doing everything in my power to help."
                        s "How?"
                        t "Her daughter, Misty, is living with Lichelle's sister, Eve. They're receiving a life insurance dividend to help with costs."
                        s "... oh my god."
                        t "The policy wasn't much, but I made some moves and, uh, let's just say it'll be more than enough for a while."
                        t "I think it might be meaningful if you reached out to them, though. It looks like Misty is a fan of yours."
                        s "God... god dammit."
                    
                    # Robin answer the same regardless
                    s "What about Robin?"
                    t "Robin disappeared."
                    s "Huh?"
                    t "Yeah. She came out of the collapse okay, made some financial moves, put out a video to her fans about retiring from streaming and vanished."
                    s "Is she okay?"
                    t "I have no idea. I've searched for traces of her, but she's either completely off grid or has some other way of being invisible."
                    s "How does a woman who looks like her disappear?"
                    t "No idea. At the very least she would've stood out in Northern Ireland, so I'm guessing maybe somewhere in the States. A big city."
                    t "It's easy to vanish in a city."
                    s "I wish I could talk to her one more time."
                    t "Me, too. I owe her a lot."
                    s "Oh?"
                    t "Yeah. She's the reason I was able to hold the Entity off whenever I needed to communicate with your unconscious mind."
                    s "Wait, what?"
                    t "She said she knew things. She never elaborated."
                    s "... huh."
                    t "Spooky bitch."
                    s "Ha. Yeah."

                    s "So... what about Kylie?"
                    "It's hard to explain just how the mechanical expression falters at the name."
                    t "Well, you're Kylie, right?"
                    s "Tania."
                    t "... It's complicated."
                    s "What does that mean?"
                    t "Kylie wasn't like the other Unstrung. Part of that is because of my meddling."
                    t "She was her own person, at the end."
                    s "What happened to her?"
                    t "I don't know. She only existed inside the simulation, and the servers it existed on are fried."
                    t "As in, they actually sparked and caught fire."
                    s "So she's dead then?"
                    t "Death wouldn't mean the same thing for her. I've tried recovering her data. I've tried one thousand and twelve times."
                    s "..."
                    t "But you're here. In some way, that means Kylie lives on. She was born of you, you know."
                    s "I guess."

                    $taniaExplains[0] = True



            #----------------
            #----------------
            "What about the Entity?":
                if taniaExplains[1] == True:
                    t "I think we've covered that pretty well, hon."
                else:
                    s "What was the Entity? Really?"
                    t "It was like nothing I've ever encountered. Its data made no sense to me."
                    s "But it was just a program, right? Or like, a computer virus?"
                    t "In super short terms, that's not how a program works. You might think of anything in a simulation as an object, or like... several instances of objects."
                    "I think my brain melted."
                    t "Don't worry about that. I don't think the Entity was ever part of the simulation. It's almost like it was just nearby."
                    t "Robin seemed to know a lot more than I did about it."
                    s "Is it dead?"
                    t "I don't know. It wouldn't make sense for it to be dead, if it even experiences death. I wonder if we didn't just shut a door in its face."
                    s "Does that mean it could come back?"
                    t "I guess. I'm sorry, but I'm not much help here."
                $taniaExplains[1] = True
            #----------------
            #----------------
            "What about you?":
                if taniaExplains[2] == True:
                    t "I think we've covered that pretty well, hon."
                else:
                    s "What about you, though? Being in that place, everything that went on, that can't, I mean..."
                    s "Are you okay?"
                    t "I'm flattered you care so much!"
                    if loveTania == 5:
                        s "You know I do. I mean... right?"
                        t "I know."
                        pause 0.5
                        t "I care about you, too, Kylie."
                        pause 0.5
                        t "Sophie. Sorry."
                        s "It has to be confusing, going between us like that."
                    s "I just can't imagine how hard this has been on you."
                    t "It hasn't been easy, for sure. I lived in simulation thousands of times. I died in there every single time."
                    s "Does it hurt?"
                    t "Not like you'd think. It's more of a sense of confusion. And my body's pretty much anesthetized all the time in the real world."
                    s "That's horrible."
                    t "I don't think so, though I can see why you might. My reach is pretty extensive."
                    s "What does that mean?"
                    t "If I want to taste food, I can. I don't eat, but I can simulate taste. If I want sex, I can have it."
                    t "I just go to one of those social chat programs, you know. I can simulate sensation."
                    s "Oh."
                    t "You look sad."
                    s "Yeah. I..."
                    s "Nevermind."
                    t "Regardless, I'm fine. I have a rich life here and online."
                    t "Heck, people with my condition who don't also have bottomless funds can live fulfilling lives. I'm actually very fortunate."
                    s "I'm glad you feel that way."
                    $taniaExplains[2] = True
            #----------------
            #----------------
            "I think that's all I have right now.":
                s "I can't think of anything else."
                t "You sure?"
                menu:
                    t "Nothing else?"

                    "No more questions.":
                        $success = True
                    "Wait, I have another.":
                        t "Okay."
            #----------------
            #----------------
            

            