label lovebox:    # necessary transform for lighting up nodes

    init python:

        # create a list of the girls. These declarations are made in declarations page.
        girls = [
            loveCass,
            loveLich,
            loveRobin,
            loveTania,
            loveEntity

        ]
        # x position in box of girls thumbnails, to the left of their hearts
        girlsNamesX = 10

        # x position of bars
        girlsBarsX = 70

        # x position of love trait
        girlsTraitX = 200

        class LoveBox:
            # a class to light up progress bars for each character's love. Remember an extra bottom row for the Entity.

            def loveCheck(self):

                # refresh love list
                girls = [
                    loveCass,
                    loveLich,
                    loveRobin,
                    loveTania,
                    loveEntity

                ]

    # end of python init
    default loveBox = LoveBox()

    screen loveScreen:
        tag loveScreen

        # we'll use the same transform as chat bc same place
        fixed at summonChat:
            # set the size of the whole window
            xysize(300, 400)

            viewport id "loveWindow":
                xfill True
                yfill True

                # sets padding and printable space inside window
                side_area(0, 0, chatWidth, chatHeight)
                mousewheel False
            # now let's make the bars for each girl. The idea is each bar will be underneath the chatbox. Lengthining it will cause the cut-out hearts to "fill" with the bars color as it passes on the layer below.

                # cassBar
                vbox:
                    xfill False
                    yfill False
                    box_wrap True
                    # cass bar
                    bar:
                        value loveCass
                        range 4
                        left_bar "#FF69B4"
                        right_bar "#000000"
                        xysize(120, 25)
                        xpos girlsBarsX
                        ypos 45
                # lichBar.
                vbox:
                    xfill False
                    yfill False
                    box_wrap True
                    # cass bar
                    bar:
                        value loveLich
                        range 4
                        left_bar "#FF69B4"
                        right_bar "#000000"
                        xysize(120, 25)
                        xpos girlsBarsX
                        ypos 115
                # RobinBar
                vbox:
                    xfill False
                    yfill False
                    box_wrap True
                    # cass bar
                    bar:
                        value loveRobin
                        range 4
                        left_bar "#FF69B4"
                        right_bar "#000000"
                        xysize(125, 35)
                        xpos girlsBarsX
                        ypos 185
                # TaniaBar
                vbox:
                    xfill False
                    yfill False
                    box_wrap True
                    # cass bar
                    bar:
                        value loveTania
                        range 4
                        left_bar "#FF69B4"
                        right_bar "#000000"
                        xysize(125, 35)
                        xpos girlsBarsX
                        ypos 255
                # livBar
                vbox:
                    xfill False
                    yfill False
                    box_wrap True
                    # cass bar
                    bar:
                        value loveEntity
                        range 4
                        left_bar "#FF69B4"
                        right_bar "#000000"
                        xysize(125, 35)
                        xpos girlsBarsX
                        ypos 325

                # Overlay. Have heart cut outs. Will be like a WinAmp skin. Also shows girls' faces. Might have that locked onto the GIMP part instead of programatically later.
                viewport id "loveScreen":
                    # show image
                    add "img/LoveBox.png" xpos 0 ypos 0

                    # girls' names. remember, hide entity with something until later. y Position here is adjusted because fonts are dumb.

                    add picKylie xpos girlsNamesX  ypos 37-10
                    add picKylie xpos girlsNamesX  ypos 107-10
                    add picKylie xpos girlsNamesX  ypos 177-10
                    add picKylie xpos girlsNamesX  ypos 247-10
                    add picKylie xpos girlsNamesX  ypos 317-10

                    # The trait for each girl

                    text "{size=20}{font=[fontEntity]} {color=[colorCass]}{b}Trust{/b}{/color} {/font}{/size}" xpos girlsTraitX ypos 40
                    text "{size=20}{font=[fontEntity]} {color=[colorLich]}Zeal{/color} {/font}{/size}" xpos girlsTraitX ypos 110
                    text "{size=20}{font=[fontEntity]} {color=[colorRobin]}Will{/color} {/font}{/size}" xpos girlsTraitX ypos 180
                    text "{size=20}{font=[fontEntity]} {color=[colorTania]}Care{/color} {/font}{/size}" xpos girlsTraitX ypos 250
                    text "{size=20}{font=[fontEntity]} {color=[colorEntity]}{/color}Desire{/font}{/size}" xpos girlsTraitX ypos 320
