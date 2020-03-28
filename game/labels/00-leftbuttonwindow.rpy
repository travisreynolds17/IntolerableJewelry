label leftbuttonwindow:
    init python:
        lbtnX = 20
        lbtnY = 219

        lbtnWidth = 180
        lbtnHeight = 292

        

    screen leftBtnWindow:
        modal False
        tag leftBtnWindow
        fixed at summonSoph:
            xpos lbtnX
            ypos lbtnY
            xysize(lbtnWidth, lbtnHeight)
            vbox:
                button:
                    text "Tips":
                        xalign 0.5
                        yalign 0.5
                    xysize(lbtnWidth, lbtnHeight/3)
                    action Notify("Doesn't work yet")
                    background "#444444"

                button:
                    text "Tips":
                        xalign 0.5
                        yalign 0.5
                    
                    xysize(lbtnWidth, lbtnHeight/3)
                    action Notify("Doesn't work yet")
                    background "#111111"

                button:
                    text "Chat History":
                        xalign 0.5
                        yalign 0.5
                    xysize(lbtnWidth, lbtnHeight/3)
                    background "#dddddd"
                    action Function(showChatHistory)


    #transform functions
    # hide and show GUI around splashes, major scene changes
    