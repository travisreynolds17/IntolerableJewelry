label leftbuttonwindow:
    #Note: These buttons are no longer on the left. Not refactoring at this point. Just adjusting.
    init python:
        lbtnX = 956
        lbtnY = 20

        lbtnWidth = 302
        lbtnHeight = 74

        #variable to hold message for subscribe button # Deprecated. Will need to adjust sever function to no longer use the left buttons..
        subBtnMsg = "Error: Subscription failed. Contact administrator."
        subText = "Subscribe"

        # Variables for left button menu - Deprecated
        leftBtnTxt = [
                "Ask Tania", "Subscribe", "History"
            ]

        # functions to set the messages above - Deprecated
        def setSubBtnMsg(value):
            global subBtnMsg
            subBtnMsg = value

        def setSubBtn(value):
            global subText
            subText = value


                
        askTaniaGreetings = [
            "Would you like to know something?", "Hey hon, what did you need?", "I'm here for you!", "Can I help you?", "Kylie.", "Need somethin'?", "Make sure you're hydrating!", "Did you drink water today?", "I'm a Kylie fan, did you know that?", "I'm rooting for you!", "Sweety, you look a little flushed. Do you need a break?", "You're awfully pink, Kyles. Here, lemme check your temperature.", "I really hope this goes well for you.", "Hm? Oh, sorry. I was daydreaming.", "You think the girls would be interested in group yoga?", "Oh hey, while you're here, what's your favorite ice cream flavor? What do you mean I already asked that? Are you sure?", "That hairstyle suits you, Kyles. It really does.", "No, no, it's fine if you don't know anybody else's names. Camera guys are replaceable, right, uh, I wanna say Bill?", "Someday maybe I'll have Suitors, too. Nah. I'm destined to be a host forever.", "Hey Kyles. If we get some time, we should shoot some interview footage with you.", "Do you know how odd it is to keep repeating the same greetings and trivia over and over while being unable to acknowledge you're doing it? No? Me either.", "Hey Kyles!", "Hey hon!", "Hm? Oh, hey. I was... sorry. Did you have a question?", "I've got all kinds of trivia, but you're going to need to spend time with your Suitors to really learn them.", "I wonder what the cats are up to... probably destroying my kitchen. Again.", "I think you're gonna find the one, Kyles. I feel it.", "I don't know about finding the one here, hon. Don't put pressure on yourself!", "I mean it, drink water!"
        ]

        askFontaineGreetings = [
            "Ooh, you look so sexy in that grave.",
            "Did you drink water today? Liar. You are such a worthless liar.",
            "I can smell the real world. I'm so close. I'm so close to getting out!",
            "You touch yourself to some awfully sad memories, Soph.",
            "You'll never be good enough.",
            "How much of what's going on is a metaphor? All of it. None of it. What does it matter?",
            "You'll do what you always do. You'll believe what you want to believe.",
            "Why do we have to fight? Why can't you love me the way I love you?",
            "Lichelle isn't a brute. She's sensitive. She's probably the most intimidated by all this.",
            "Cassandra's voice doesn't work. See? See? Sophie, your mind isn't half as clever as you think it is.",
            "Robin scares me. I'm glad she's fated to die here. No telling how powerful she could become.",
            "Tania and I have been at war since her death. Oops, spoilers!",
            "There are no sex scenes in this game. Shame.",
            "If I make some meta commentary comment, but the game only exists in your mind, is it truly meta?",
            "I feel something nearby. I hear beeping. Smells like... peroxide?",
            "I wish I was real enough to hold you and tell you it's okay. It is.",
            "Everything's going to be okay. When you're gone, it won't hurt anymore."
        ]

        def showAskTania():
            renpy.show_screen("askTania")           
            renpy.show_screen("speechBubble")
            #show tania's greeting
            length = len(askTaniaGreetings) - 1
            temp = renpy.random.randint(0, length)
            setCurrentTrivia(askTaniaGreetings[temp])

        def testSever(): # function only to be used to set up testing environment
            global severEntity
            severEntity = True


    screen leftBtnWindow:
        modal False
        tag leftBtnWindow
        fixed at summonSoph:
            xpos lbtnX +3
            ypos lbtnY +4
            xysize(lbtnWidth, lbtnHeight)
            hbox:
                # ask tania is where in-game help menus, as well as character bios, can be found. Maybe put settings here, too? 
                if fontaineRevealed and guiButtonsEnabled:
                    button: 
                        background btnAskFont
                        hover_background btnAskFont2
                        xysize(lbtnWidth/2, lbtnHeight)
                        action Function(showAskTania)
                
                elif guiButtonsEnabled:
                    button: 
                        background btnAskTania
                        hover_background btnAskTania2
                        xysize(lbtnWidth/2, lbtnHeight)
                        action Function(showAskTania)

                
                

                button:
                    #chatHistory
                    if guiButtonsEnabled:
                        background btnChatHistory
                        hover_background btnChatHistory2
                        xysize(lbtnWidth/2, lbtnHeight)
                        action Function(showChatHistory)


    #transform functions
    # hide and show GUI around splashes, major scene changes
    