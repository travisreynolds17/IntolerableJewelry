label endCredits:
    # music?

    $hideChat()
    scene bg black with fade

    # secret Kylie ending. Only achievable if love confession is Robin's, all severs are viewed, Kylie is severed, and Fontaine is forgiven.
    if kylieSevered and entityForgiven and fontBio.severViewed and lichBio.severViewed and robinBio.severViewed and cassBio.severViewed and taniaBio.severviewed:
        call secretKylie

    show image credits1 with fade
    pause
    show image credits2 with fade
    pause
    show image credits3 with fade
    pause
    show image credits4 with fade
    pause
    show image credits5 with fade
    pause
    scene bg black with longFade
    pause 


