label kylieEnding:
    $hideSeverancePanel()
    $hideGui()
    scene bg black

    stop music fadeout 5.0

    pause 1.0

    k "Huh?"

    pause 0.5

    k "Why does... ow! I... why does..."

    k "it hurts"

    # sfx
    show image screenCrack

    k "why"

    # sfx
    show image screenCrack2

    k "somebody"

    # sfx
    show image screenCrack3

    k "h... h...hel..."

    # sfx
    show image screenCrack4 with dissolve

    # some quote about there's no using burning the boats while you're still on them

    screen splashBoat:
        add splashBoats
        modal True


    pause 1.0

    scene bg black with longFade

    show screen splashBoat with dissolve
    pause


