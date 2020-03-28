label btnWindow:
    # this file arranges and provides function to two buttons: chat toggle and subscribe. upper right corner.

    init python:
        btnWindowHeight = 72
        btnWindowWidth = 300
        btnWindowX = 960
        btnWindowY = 24

        #variable to hold the on/off state of chat window
        chatIsOn = False
        #Variable to hold contextual title for subscribe button
        subBtnText = "Subscribe"
        #variable to hold message for subscribe button
        subBtnMsg = "Error: Subscription failed. Contact administrator."

    screen btnWindow:
        modal False
        tag btnWindow

        fixed at alphaFade:
            xysize(btnWindowWidth, btnWindowHeight)
            xpos btnWindowX
            ypos btnWindowY
                         
            hbox:       
                #this button is intended to toggle the in-game chat window into and out of sight.                          
            
                showif chatIsOn == False:
                    button:
                        text "Chat":
                            yalign 0.5
                            xalign 0.5
                        xysize(btnWindowWidth/2, btnWindowHeight)
                        background "#111111"
                        
                        action [ToggleVariable("chatIsOn"), Show("chatterbox"), Hide("loveScreen")]

                showif chatIsOn:
                    button:
                        text "Status":
                            yalign 0.5
                            xalign 0.5
                        xysize(btnWindowWidth/2, btnWindowHeight)
                        background "#111111"
                        
                        action [ToggleVariable("chatIsOn"), Hide("chatterbox"), Show("loveScreen")]

                button:
                    # this button is intended to show a contextual message depending on story point
                    text subBtnText:
                        yalign 0.5
                        xalign 0.5
                    xysize(btnWindowWidth/2, btnWindowHeight)
                    background "#777777"
                    action Notify(subBtnMsg)