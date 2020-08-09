label endingGoodTania2:
    t "Is there anything I can try to answer for you?"
    default taniaExplains = [False, False, False, False, False]

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
                    show m 2m
                    t "Let's do alphabetical order. Don't worry, we'll do it right this time!"

                    #-- Cassandra

                    if cassBio.fullySevered == True:
                        
                        show m 2m at mt1
                        show c 1m at f12
                        t "Cassandra spent some time in a safe place after the simulation broke down."
                        s "Safe place?"
                        show m 2b
                        t "A mental institution. She took quite a lot of pills, Sophie."
                        "My heart freezes."
                        show m 2h
                        t "No, no no, she's alive. She's okay. Her band manager found her. It's very lucky, actually."
                        s "Cassandra..."
                        show m 2b
                        t "She's getting the help she needs now, Sophie. She's needed help for a long time, but her touring and recording always got in the way."
                        t "At least, that's what I've gathered since we got free."
                    else:
                        show m 2b
                        t "About Cassandra... I have bad news, Sophie."
                        s "... tell me."
                        t "She's no longer with us."
                        s "What? Wait, why?"
                        show m 2c
                        t "She overdosed, Sophie. The autopsy report said it was heroin, alcohol and painkillers."
                        "How... how could she say it so casually...?"
                        s "Why would she do that, though? I thought--"
                        show m 2b
                        t "Cassandra needed help, Sophie. She wasn't severed when the simulation collapsed, so enough of Fontaine's influence was left in her that it broke her completely."
                        s "... you mean I could have saved her?"
                        show m 2d
                        t "Sophie, do not blame yourself. Do. Not."
                        s "But..."
                        t "You had no conscious control, remember? It just happened this way."

                    if lichBio.fullySevered == True:
                        show m 2m at mt1
                        show l 1m at f12
                        t "As for Lichelle, she's doing fine."
                        s "That's a relief."
                        t "She's living in Colorado now, working as a fighting coach and yogi."
                        s "A... yogi?"
                        show m 2a
                        t "A woman of tremendous violence and also of peace, somehow."
                        t "We've communicated a bit online since the collapse, but mostly it's just been pleasantries."
                        show m 2b
                        t "I think the wounds are too fresh, still. In Lichelle's game I was a tournament host."
                        t "I put her through some pretty brutal trials, Sophie."
                        s "But that was the Fontaine's doing, right?"
                        show m 2q
                        t "Yeah, mostly."
                        t "Some part of me went along with it a little too willingly. But I've made my apologies. I'm also an investor in her business, which is the very least I could do."
                        s "You can invest?"
                        show m 2a
                        t "I am almost entirely a machine, hon. This stuff is expensive, so I play the markets, make investments and... well."
                        t "Let's say I keep things going comfortably."
                        s "Oh."
                        t "I'll give you Lichelle's contact information. She's eager to hear from you, you know."
                        s "Likewise. Thanks, Tania."
                    else:
                        show m 2b
                        t "As for Lichelle, she... well, I'll tell you about her in a bit."
                        s "Oh. Okay."
                        
                    
                    # Robin answer the same regardless
                    show m 2a at mt2
                    s "What about Robin?"
                    t "You know, it amazed me someone like her could even exist."
                    s "Huh?"
                    show m 2p
                    t "She was almost like a fanfiction version of someone you knew personally."
                    s "Is she okay?"
                    show m 2a
                    t "I have no idea. I've searched for traces of her, but she's either completely off grid or has some other way of being invisible."
                    s "How does a woman who looks like her disappear?"
                    show m 2q
                    t "I can't say, Kyles. I mean, Sophie."
                    t "I'm still not sure she was ever real."
                    s "..."
                    pause 1.0
                    s "I can't let myself believe the simulation created her from nothing."
                    show m 2a
                    t "Not nothing. Even Fontaine told us a lot of what we were seeing in Kylie's history belonged to you."
                    s "... Louisa?"
                    t "Yeah."
                    s "I had to lose her twice, then."
                    show m 2q
                    t "And yet here you are. Stronger, healthier than ever."
                    s "... huh."
                    t "I'll miss her, though. In there, Robin was my friend."
                    pause 0.1
                    s "So... what about Kylie?"
                    show m 2c
                    "It's hard to explain just how the mechanical expression falters at the name."
                    t "Well, you're Kylie, right?"
                    s "Tania."
                    show m 2b
                    t "... It's complicated."
                    s "What does that mean?"
                    pause 0.5
                    show m 2g
                    t "Kylie wasn't like the other rest of us. Part of that is because of my meddling."
                    t "She was her own person, at the end."
                    s "What happened to her?"
                    show m 2b
                    t "I don't know. She only existed inside the simulation, and the servers it existed on are fried."
                    t "As in, they actually sparked and caught fire."
                    pause 0.1
                    s "So she's dead then?"
                    show m 2a
                    t "Death wouldn't mean the same thing for her. I've tried recovering her data. I've tried one thousand and twelve times."
                    s "..."
                    t "But you're here. In some way, that means Kylie lives on. She was born of you, you know."
                    s "I guess."

                    $taniaExplains[0] = True



            #----------------
            #----------------
            "What about Fontaine?":
                if taniaExplains[1] == True:
                    t "I think we've covered that pretty well, hon."
                else:
                    s "What was Fontaine? Really?"
                    show m 2k
                    t "It was like nothing I've ever encountered. Its data made no sense to me."
                    s "But it was just a program, right? Or like, a computer virus?"
                    t "In super short terms, that's not how a program works. You might think of anything in a simulation as an object, or like... several instances of objects."
                    "I think my brain melted."
                    show m 2m
                    t "Don't worry about that. I don't think Fontaine was ever part of the simulation. It's almost like it was just nearby."

                    t "Robin seemed to know a lot more than I did about it."
                    s "Is she dead?"
                    show m 2r
                    t "I don't know. It wouldn't make sense for it to be dead, if it even experiences death."
                    
                    t "I wonder if we didn't just shut a door in its face."
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
                    show m 2m
                    t "I'm flattered you care so much!"
                    if loveTania >= 4:
                        s "You know I do. I mean... right?"
                        show m 2a
                        t "I know."
                        pause 0.5
                        show m 2t
                        t "I care about you, too, Kylie."
                        pause 0.5
                        show m 2q
                        t "Sophie. Sorry."
                        s "It has to be confusing, going between us like that."
                    s "I just can't imagine how hard this has been on you."
                    show m 2a
                    t "It hasn't been easy, for sure. I lived in simulation thousands of times. I died in there more than once."
                    s "Does it hurt?"
                    show m 2m
                    t "Not like you'd think. It's more of a sense of confusion. And my body's pretty much anesthetized all the time in the real world."
                    s "That's horrible."
                    show m 2a
                    t "I don't think so, though I can see why you might. My reach is pretty extensive."
                    s "What does that mean?"
                    show m 2m
                    t "If I want to taste food, I can. I don't eat, but I can simulate taste. If I want sex, I can have it."
                    show m 2u
                    t "I just go to one of those social chat programs, you know. I can simulate sensation."
                    s "Oh."
                    show m 2b
                    t "You look sad."
                    s "Yeah. I..."
                    s "Nevermind."
                    show m 2a
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
            

            