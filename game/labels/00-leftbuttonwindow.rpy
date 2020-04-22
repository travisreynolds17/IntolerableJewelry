label leftbuttonwindow:
    init python:
        lbtnX = 20
        lbtnY = 219

        lbtnWidth = 180
        lbtnHeight = 292

        #variable to hold message for subscribe button
        subBtnMsg = "Error: Subscription failed. Contact administrator."

        # Variables for left button menu
        leftBtnTxt = [
                "Ask Tania", "Subscribe", "History"
            ]
        askTaniaGreetings = [
            "Would you like to know something?", "Hey hon, what did you need?", "I'm here for you!", "Can I help you?", "Kylie.", "Need somethin'?", "Make sure you're hydrating!", "Did you drink water today?", "I'm a Kylie fan, did you know that?", "I'm rooting for you!", "Sweety, you look a little flushed. Do you need a break?", "You're awfully pink, Kyles. Here, lemme check your temperature.", "I really hope this goes well for you.", "Hm? Oh, sorry. I was daydreaming.", "You think the girls would be interested in group yoga?", "Oh hey, while you're here, what's your favorite ice cream flavor? What do you mean I already asked that? Are you sure?", "That hairstyle suits you, Kyles. It really does.", "No, no, it's fine if you don't know anybody else's names. Camera guys are replaceable, right, uh, I wanna say Bill?", "Someday maybe I'll have Suitors, too. Nah. I'm destined to be a host forever.", "Hey Kyles. If we get some time, we should shoot some interview footage with you.", "Do you know how odd it is to keep repeating the same greetings and trivia over and over while being unable to acknowledge you're doing it? No? Me either.", "Hey Kyles!", "Hey hon!", "Hm? Oh, hey. I was... sorry. Did you have a question?", "I've got all kinds of trivia, but you're going to need to spend time with your Suitors to really learn them.", "I wonder what the cats are up to... probably destroying my kitchen. Again.", "I think you're gonna find the one, Kyles. I feel it.", "I don't know about finding the one here, hon. Don't put pressure on yourself!", "I mean it, drink water!"
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
            xpos lbtnX
            ypos lbtnY
            xysize(lbtnWidth, lbtnHeight)
            vbox:
                # ask tania is where in-game help menus, as well as character bios, can be found. Maybe put settings here, too? 
                button: 
                    text leftBtnTxt[0]:
                        xalign 0.5
                        yalign 0.5
                    xysize(lbtnWidth, lbtnHeight/3)
                    action Function(showAskTania)
                    background "#444444"

                button:
                    # this button is intended to show a contextual message depending on story point. Note that subscribe never actually does anything.
                    text leftBtnTxt[1]:
                        yalign 0.5
                        xalign 0.5
                    xysize(lbtnWidth, lbtnHeight/3)
                    
                    background "#777777"
                    action [Function(getAllHistories), Function(testSever)]

                button:
                    #chatHistory
                    text leftBtnTxt[2]:
                        xalign 0.5
                        yalign 0.5
                    xysize(lbtnWidth, lbtnHeight/3)
                    background "#dddddd"
                    action Function(showChatHistory)


    #transform functions
    # hide and show GUI around splashes, major scene changes
    