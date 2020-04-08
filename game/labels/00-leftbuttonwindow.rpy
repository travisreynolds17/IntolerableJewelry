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
                "Bios", "Subscribe", "History"
            ]

        def showScreenBios():
            renpy.show_screen("biographies")


    screen leftBtnWindow:
        modal False
        tag leftBtnWindow
        fixed at summonSoph:
            xpos lbtnX
            ypos lbtnY
            xysize(lbtnWidth, lbtnHeight)
            vbox:
                button:
                    text leftBtnTxt[0]:
                        xalign 0.5
                        yalign 0.5
                    xysize(lbtnWidth, lbtnHeight/3)
                    action Function(showScreenBios)
                    background "#444444"

                button:
                    # this button is intended to show a contextual message depending on story point
                    text leftBtnTxt[1]:
                        yalign 0.5
                        xalign 0.5
                    xysize(lbtnWidth, lbtnHeight/3)
                    
                    background "#777777"
                    action Function(getHistory,12)

                button:
                    text leftBtnTxt[2]:
                        xalign 0.5
                        yalign 0.5
                    xysize(lbtnWidth, lbtnHeight/3)
                    background "#dddddd"
                    action Function(showChatHistory)


    #transform functions
    # hide and show GUI around splashes, major scene changes
    