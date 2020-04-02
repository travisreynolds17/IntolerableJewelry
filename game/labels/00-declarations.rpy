label declarations:
    # declarations. Organize here for cleaner code.

    init python:
        # declare lots of variables to hold color and font choices, makes it easier to change later.
        colorSophie = "#c5859d"
        colorCass = "#5e81a1"
        colorLich = "#bcb4ec"
        colorRobin = "#bcb4ec"
        colorTania = "#a3d1b9"
        colorEntity = "#c5859d"
        colorKylie = "#ffa4d5"

        fontSophie = "fonts/Roboto-Black.ttf"
        fontCass = "fonts/Lobster-Regular.ttf"
        fontLich = "fonts/ElsieSwashCaps-Black.ttf"
        fontRobin = "fonts/Parisienne-Regular.ttf"
        fontTania = "fonts/Courgette-Regular.ttf"
        fontEntity = "fonts/EncodeSans-Black.ttf"
        fontKylie = "fonts/Roboto-Black.ttf"

        # girls thumbnail images. Note: update when we have more.
        picSophie = "img/pic-Kylie.png"
        picCass = "img/pic-Kylie.png"
        picLich = "img/pic-Kylie.png"
        picRobin = "img/pic-Kylie.png"
        picTania = "img/pic-Kylie.png"
        picEntity = "img/pic-Kylie.png"
        picKylie = "img/pic-Kylie.png"

    define s = Character("Sophie", who_color="#c5859d", who_font="fonts/Roboto-Black.ttf", what_color=colorKylie, what_font=fontKylie)
    # skin tone #c58c85
    # hair tone / name tone #c5859d
    define r = Character("Robin", who_color="#bcb4ec", who_font="fonts/Parisienne-Regular.ttf")
    # skin tone #503335
    # hair tone / name tone #bcb4ec
    define t = Character("Tania", who_color="#a3d1b9", who_font="fonts/Courgette-Regular.ttf")
    # skin tone #d1a3a4
    # hair tone / name tone #a3d1b9
    define c = Character("Cassandra", who_color="#89cff0", who_font=fontCass)
    # skin tone #a1665e	rgb(161, 102, 94)
    # hair tone / name tone #5e81a1

    define l = Character("Lichelle", who_color="#5e81a1", who_font="fonts/ElsieSwashCaps-Black.ttf")
    # skin tone #503335
    # hair tone #503933
    # name tone #d46359 (to avoid everything about her being brown so peeps don't get upset)
    define d = Character("David")
    define k = Character("Kylie", who_color="#ffa4d5", who_font="fonts/Roboto-Black.ttf")
    # skin tone #c58c85
    # hair tone / name tone ffa4d5

    # This is for kylie's inner monologue.
    define ki = Character("")
    # skin tone #c58c85
    # hair tone / name tone #ffa4d5
    define un = Character("???")
    define sk = Character("Sophie & Kylie", who_color="#c5859d", who_font="fonts/Roboto-Black.ttf")
    define e = Character("[entityName]", who_color="#c5859d", who_font="fonts/EncodeSans-Black.ttf")
    # skin tone #503335
    # hair tone / name tone

    define m = Character("Mortimer")
    define o = Character("Oblivion")
    define girls = Character("Cass, Lichelle & Robin")

    # define a = Character("Ashley")

    # useful images

    define splashTitle = Image("img/ingameSplash.png")
    define splashBRB = Image("img/ingameBRB.png")
    define chatHistoryBack = Image("img/chatHistoryBack.png")
    define splashHorror = Image("img/flash horror 1.jpg")
    define splashErrorTania = Image("img/ingameSplashErrorTania.png")




    # --------------------------------------------------------------------------------------------

    # TRANFORMS

    # TRANSITIONS

    # define basic positions

    transform subscribeCenter:
        xalign 0.0 ypos 0.66

    transform subscribeLeave:
        xpos - 0.5 ypos 0.66

    transform midToRight:
        linear 0.6 xpos 0.8

    transform midToLeft:
        linear 0.6 xpos 0.2

    transform rightToLeft:
        linear 0.6 xpos 0.2

    transform rightToMid:
        linear 0.6 xpos 0.5

    transform leftToRight:
        linear 0.6 xpos 0.8

    transform leftToMid:
        linear 0.6 xpos 0.5

    transform alphaFade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            alpha 1.0
            linear 1.0 alpha 0.0

    # transitions

    define longFade = Fade(0.5, 1.1, 0.5)

    # For chatbox
    transform summonChat:
        on show:
            xpos 1280
            ypos chatYPos
            linear 0.3 xpos chatXPos

        on hide:
            linear 0.3 xpos 1280

    transform summonSoph:
        on show:
            xpos - 200
            ypos lbtnY
            linear 0.2 xpos lbtnX

        on hide:
            linear 0.2 xpos - 200

    transform summonChatHorror:
        xpos chatXPos ypos chatYPos
        alpha 0
        on show:
            linear 0.2 alpha 0.15
            linear 0.2 alpha 0.075
            repeat
        on hide:
            xalign 0.5 yalign 0.5
            linear 0.5 zoom 10



        

# -------------------------------------------------------------------------------------------------

    init:
        # variables

        # relationships
        $loveCass = 0
        $loveRobin = 0
        $loveLich = 0
        $loveTania = 0
        $loveEntity = 0
        # in late game you'll have a chance to confess. Only way to get a love ending.
        $loveConfession = "None"
        $severChances = 9
        $severCass = False
        $severRobin = False
        $severLich = False
        $severTania = False
        $severKylie = False
        $severEntity = False
        $severGod = False
        $severAll = False  # checks for all five primary good ending severs
        $severCodeBase = "stringSever"  # kill code for the being
        $severInput = "unknown"
        $entityName = "Oblivion"
        $entityForgiven = False
        $entityForgiven = True

        $sceneNum = 0

        # Variables for left button menu
        python:
            leftBtnTxt = [
                "Tips", "ComeFundMe", "History"
            ]

        # regarding severance. Ending determined by severance.
        # sever all four girls but not the entity, sophie escapes but everyone dies and the entity lives on. Bad newsreel ending. sever the entity and none of the girls, everyone dies. Bad newsreel ending but entity dead. No need to severkylie. Sever the entity and some of the girls, good ending where whoever's left unsevered dies. sever all four girls and the entity, best ending where all girls meet together and Robin reveals she's the one who was giving out code hints, and tells you she voluntarily went into the code because she's dealt with cosmic entities before. If the girl you have at least 4 romance with survives, hook up IRL for a special exclusive scene.
        # bonus. If at any point you try to sever Kylie, special ending where Sophie wakes up in a hospital bed surrounded by the Unstrung versions of the girls. Bad end. Bonus ending if you try to sever god, the game crashes. Will get one chance each time

    # choices in order of appearance

        $which_girl_1 = ""  # common1, first choice of girls
        $groupThing = False  # in which girl choice, common1
        $which_girl_2 = ""  # TBD
        $taniaEnd = 0  # if we've seen the joke ending
        $currentEnding = ""
        $badEndings = []  # holds which characters are getting a non-severed or bad ending. Bad ending label will check for each and display approprite clips

    # note. The following variables are in python form because I'm an idiot and didn't do the others that way.

    init python:

        # chatbox variables
        # ZOrder for main game gui. The idea is to control layers.
        mainZorder = 100
        loveZorder = mainZorder + 1
        loveBarsZorder = loveZorder + 1
        chatzorder = loveBarsZorder + 1
        historyzorder = loveBarsZorder + 1
        horrorZorder = historyzorder + 1
        #current position of history objects
        
        currentHistory = 0

        #decision variables. I'm bad at organizing. 
        #outfits. These guys are for a few scenes. I don't want to tie love points to this. Too arbitrary.
        outfitBlackDress = 0
        outfitJeans = 0
        outfitPantsuit = 0
        outfitCurrent = ""

        #variables to show that cover chat window
        horrorChat = ""
        horrorTwixt = [Image("img/twixtNorm.png"), Image("img/twixtNorm1.png"), Image("img/twixtNorm2.png")]


    #useful functions

        # functions to show and hide the primary in-game gui: sophie's stream window
        def hideGui():
            renpy.hide_screen("mainGameWindow") 
            renpy.hide_screen("loveScreen")
            renpy.hide_screen("chatterbox")
            renpy.hide_screen("leftBtnWindow")
            chatIsOn = False
            renpy.hide_screen("btnWindow") 
            renpy.pause(2.0)

        def showGui():
            
            renpy.show_screen("mainGameWindow") 
            renpy.show_screen("loveScreen") 
            renpy.show_screen("chatterbox")
            renpy.show_screen("leftBtnWindow")
            chatIsOn = True
            renpy.show_screen("btnWindow") 
            renpy.pause(2.0)

        # create a custom function to display the chat history screen.
        def showChatHistory():
            renpy.show_screen("chatHistory")
            renpy.show_screen("historyDisplay")
            renpy.show_screen("historySelect")

        def hideChatHistory():
            renpy.hide_screen("chatHistory")
            renpy.hide_screen("historyDisplay")
            renpy.hide_screen("historySelect")

        #create a custom function that takes a string and returns it in reverse

        def reverseString(userInput):
            #apparently this is the slice function, and it steps backward. fluckin python
            return userInput[::-1]

        

        

