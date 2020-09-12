label newGamePlus:
    scene bg black with longestFade
    stop music fadeout 3.0

    pause 3.0

    menu:
        "N-n-n-new game plus?"
        "Perpetuate the vicious cycle.":
            jump opening
            $persistent.playthrough += 1
        "... just let me die.":
            "As you wish."
            pause 5.0