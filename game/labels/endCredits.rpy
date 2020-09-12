label endCredits:
    # music?

    $hideChat()
    scene bg black with fade

    

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
    


    # secret Kylie ending. Only achievable if love confession is Robin's, all severs are viewed, Kylie is severed, and Fontaine is forgiven. Also requires you to have picked Fontaine as a love interest.
    if kylieSevered and entityForgiven and fontBio.severViewed and robinBio.severViewed and persistent.loveRobin and persistent.loveFontaine and sophieEndingViewed:
        call secretKylie from _call_secretKylie

    jump newGamePlus