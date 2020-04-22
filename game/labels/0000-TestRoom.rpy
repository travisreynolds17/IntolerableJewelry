# use this to test all the things.

# currently testing: how to mimic DDLC transforms
label testRoom:
    transform sink(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein .5 ypos 1.06

    transform hop(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein 2.6 yoffset -20
        easeout .1 yoffset 0



        #------ setup

    scene bg bar

    $showGui()

    show c at center

    $breakLoop = False

    while breakLoop == False:
        menu:
            "Hop":
                hide c 
                hide l 
                hide r 
                hide t
                show c 1a at f11
                show l 2b at f13
                show r 3c at f21
                show t at fl22
            "Sink":
                hide c 
                hide l 
                hide r 
                hide t
                show c at fl11
                show l at f12
                show r at f13

