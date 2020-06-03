# use this to test all the things.

# currently testing: how to mimic DDLC transforms
label testRoom:
    transform sink(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein .5 ypos 1.06

    transform hop(x=640, z=0.80):
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein 2.6 yoffset - 20
        easeout .1 yoffset 0


        #------ setup

    scene bg bar

    # MONOLOGUE ------------------------------

    $showGui()

    pause 2.0

    $severToggle()

    pause

    s "Well, this is a waste of time."

    return