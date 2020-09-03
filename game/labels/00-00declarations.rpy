    init:
        # attempt to create default bios.

        default cassBio = Biography(0, "Cassandra Sanna", bioCass,
                                cassBioText, "22", "Ultramarine", cassTrivia, "No", "Vox the Python", "Pro Wrestling", "Britomart", "62 inches", "Charlotte, N.C.")
        default lichBio = Biography(1, "Lichelle Carpenter", bioLich,
                            lichBioText, "25", "Carmine Red", lichTrivia, "Hell no", "Nope", "MMA", "My dad", "66 inches", "Baltimore, Md.")
        default robinBio = Biography(2, "Robin Godfrey", bioRobin, robinBioText, "24",
                            "Royal Purple", robinTrivia, "Not yet", "Innumerable", "None", "You", "73 inches", "Bucharest, Romania")
        default fontBio = Biography(5, "Fontaine", bioFont, fontBioText, "R/BG13:14-15", "China White", fontTrivia, "I can't have kids. Comfort me?",
                            "I love animals!", "I don't understand sports", "Sophie ;)", "All of them, if I want", "Everywhere!")

        default taniaBio = Biography(3, "Tania van der Waal", bioTania,
                            taniaBioText, "26", "Tuscan Sun", taniaTrivia, "No", "Cats: Ferg, Della, Kana",  "Gymnastics", "R/BG13:14-15 Langford", "65 inches", "Centralia, Penn.")
        default kylieBio = Biography(4, "Kylie", bioKylie, kylieBioText, "23", "Golden Poppy", kylieTrivia, "Someday", "Someday I'll have a dog", "Basketball, I guess", "Elizabeth Bathory, jk", "66 inches", "Sobredosis, Nevada")

        # append Fontaine in common4 after change
        default allBios = [cassBio, lichBio, robinBio, taniaBio, kylieBio]
        default allStats = ["Height:", "Hometown:", "Pets:", "Age:", "Fav. Color:", "Fav. Sport:", "Kids:", "Idol:"]

        # name plates.
        default bioEyesCass = Image("img/bioEyesCass.png")
        default bioEyesLich = Image("img/bioEyesLich.png")
        default bioEyesRobin = Image("img/bioEyesRobin.png")
        default bioEyesTania = Image("img/bioEyesTania.png")
        default bioEyesKylie = Image("img/bioEyesKylie.png")
        default bioEyesFont = Image("img/bioEyesFont.png")

        default allPlates = [bioEyesCass, bioEyesLich, bioEyesRobin, bioEyesTania, bioEyesKylie]

        # chat history variables
    init -1:
        default histories = []
    
    init python:

        # time stuff
        import time
        year, month, day, hour, minute, second, dow, doy, dst = time.localtime()

        # declare lots of variables to hold color and font choices, makes it easier to change later.
        colorSophie = "#c5859d"
        colorCass = "#5e81a1"
        colorLich = "#bcb4ec"
        colorRobin = "#bcb4ec"
        colorTania = "#a3d1b9"
        colorEntity = "#c5859d"
        colorKylie = "#ffa4d5"
        colorHover = "#816161"

        fontSophie = "fonts/Roboto-Black.ttf"
        fontCass = "fonts/Lobster-Regular.ttf"
        fontLich = "fonts/ElsieSwashCaps-Black.ttf"
        fontRobin = "fonts/Parisienne-Regular.ttf"
        fontTania = "fonts/Courgette-Regular.ttf"
        fontEntity = "fonts/EncodeSans-Black.ttf"
        fontKylie = "fonts/Roboto-Black.ttf"

        allFonts = [fontCass, fontLich, fontRobin, fontTania, fontKylie]
        allColors = [colorCass, colorLich, colorRobin, colorTania, colorKylie]

        # girls thumbnail images. Note: update when we have more.
        picSophie = "img/pic-Kylie.png"
        picCass = "img/pic-Kylie.png"
        picLich = "img/pic-Kylie.png"
        picRobin = "img/pic-Kylie.png"
        picTania = "img/pic-Kylie.png"
        picEntity = "img/pic-Kylie.png"
        picKylie = "img/pic-Kylie.png"

        

        # we need characters to visually alter when speaking. we'll use a character callback for that, it seems. 

        def speakingCass(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("c"):
                    renpy.show("c", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("c"):
                    renpy.show("c", at_list = [speakNormal])
        
        def speakingLich(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("l"):
                    renpy.show("l", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("l"):
                    renpy.show("l", at_list = [speakNormal])

        def speakingTania(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("t"):
                    renpy.show("t", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("t"):
                    renpy.show("t", at_list = [speakNormal])

        def speakingRobin(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("r"):
                    renpy.show("r", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("r"):
                    renpy.show("r", at_list = [speakNormal])
        
        def speakingKylie(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("k"):
                    renpy.show("k", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("k"):
                    renpy.show("k", at_list = [speakNormal])

        def speakingFont(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("o"):
                    renpy.show("o", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("o"):
                    renpy.show("o", at_list = [speakNormal])

        def speakingDavid(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("d"):
                    renpy.show("d", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("d"):
                    renpy.show("d", at_list = [speakNormal])
        
        def speakingElsa(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("e"):
                    renpy.show("e", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("e"):
                    renpy.show("e", at_list = [speakNormal])

        def speakingMort(event, interact = True, **kwargs):
            if not interact:
                return
            # if event == begin means if a say statement has started.
            if event == "begin":
                if renpy.showing("m"):
                    renpy.show("m", at_list = [speakZoom])
            if event == "end":
                if renpy.showing("m"):
                    renpy.show("m", at_list = [speakNormal])

    define s = Character("Sophie", image="s", who_color="#c5859d", who_font="fonts/Roboto-Black.ttf", what_color=colorKylie, what_font=fontKylie)
    # skin tone #c58c85
    # hair tone / name tone #c5859d
    define r = Character("Robin", image="r", who_color="#bcb4ec", who_font="fonts/Parisienne-Regular.ttf")
    # skin tone #503335
    # hair tone / name tone #bcb4ec
    define rr = Character("Robin", who_color="#bcb4ec", who_font="fonts/Parisienne-Regular.ttf")
    # skin tone #503335

    define t = Character("Tania", image="t", who_color="#a3d1b9", who_font="fonts/Courgette-Regular.ttf")
    # skin tone #d1a3a4
    # hair tone / name tone #a3d1b9

    define e = Character("Elsa", image="e", who_color="#a3d1b9", who_font="fonts/Courgette-Regular.ttf")

    define c = Character("Cassandra", image="c", who_color="#89cff0", who_font=fontCass)
    # skin tone #a1665e	rgb(161, 102, 94)
    # hair tone / name tone #5e81a1

    define l = Character("Lichelle", image="l", who_color="#5e81a1", who_font="fonts/ElsieSwashCaps-Black.ttf")
    # skin tone #503335
    # hair tone #503933
    # name tone #d46359 (to avoid everything about her being brown so peeps don't get upset)
    define d = Character("David",  image="d",)
    define k = Character("Kylie", image="k", who_color="#ffa4d5", who_font="fonts/Roboto-Black.ttf")
    # skin tone #c58c85
    # hair tone / name tone ffa4d5

    # This is for kylie's inner monologue.
    define ki = Character("")
    # skin tone #c58c85
    # hair tone / name tone #ffa4d5
    define un = Character("???")
    define sk = Character("Sophie & Kylie", who_color="#c5859d", image="k", who_font="fonts/Roboto-Black.ttf")
    

    define m = Character("Mortimer", image="m")
    define o = Character("Fontaine", who_color="#c5859d", who_font="fonts/EncodeSans-Black.ttf", image="f")
    define girls = Character("Cass, Lichelle & Tania")

    define narr = Character(None, kind=nvl)

    # useful images

    define splashTitle = Image("img/ingameSplash.png")
    define splashBRB = Image("img/ingameBRB.png")
    define chatHistoryBack = Image("img/chatHistoryBack.png")
    define splashHorror = Image("img/flash horror 1.jpg")
    define splashErrorTania = Image("img/ingameSplashErrorTania.png")
    define splashEKGFull = Image("img/splashEKG.png")
    define splashEKGFlat = Image("img/splashEKGFlat.png")
    define splashBoats = Image("img/splashBoats.png")
    define splashSophieOnDesk = Image("img/splashSophieOnDesk.png")
    define askTaniaBack2 = Image("img/backAskTania2.png")
    define splashDrown = Image("img/drownedRobin.png")
    define splashDrown2 = Image("img/drownedRobin2.png")
    define splashChoice = Image("img/splashWrongChoice.png")
    define story7Edit = Image("img/bg story-7-edit.png")
    define story9Edit = Image("img/bg story-9-edit.png")

    #showNotes
    define showNotes1 = Image("img/showNotes1.png")
    define showNotes2 = Image("img/showNotes2.png")
    define showNotes3 = Image("img/showNotes3.png")
    define showNotes4 = Image("img/showNotes4.png")

    define kylieBlood1 = Image("img/kcBlood1.png")
    define kylieBlood2 = Image("img/kcBlood2.png")

    define credits1 = Image("img/endCredits1.png")
    define credits2 = Image("img/endCredits2.png")
    define credits3 = Image("img/endCredits3.png")
    define credits4 = Image("img/endCredits4.png")
    define credits5 = Image("img/endCredits5.png")

    define glitchGui = Image("img/glitchGUI.png")
    default doneSevering = False
    # to hold title of ending
    default endingTitle = ""
    default kylieSevered = False
    default lichClonked = False
    define endings = ["Birth of a Neurochemical God", "Sobredosis", "Damned in Elle", "Homunculus Post Mortem", "Papillon", "My Soul Is Yours", "Dr. L'eau, Amateur Surgeon", "Free from Myself"]

    # kylie and fontain dissolving

    define fontDiss1 = "images/chars/fc3.png"
    define fontDiss2 = "images/chars/fc4.png"
    define fontDiss3 = "images/chars/fc5.png"

    define kylieDiss1 = "images/chars/kc3.png"
    define kylieDiss2 = "images/chars/kc4.png"
    define kylieDiss3 = "images/chars/kc5.png"
    define kylieDiss4 = "images/chars/kc6.png"


    

    # --------------------------------------------------------------------------------------------

    # TRANFORMS

    # TRANSITIONS

    # define basic positions

    transform growShrink:
        on show:
            xzoom 0.0 xanchor 1.0 alpha 0.0
            linear 0.5 xzoom 1.0 alpha 1.0
        on hide:
            zoom 1.0 xanchor 1.0
            linear 0.1 xzoom 0.0

    transform alphaFade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            alpha 1.0
            linear 1.0 alpha 0.0

    transform alphaFaster:
        on show:
            alpha 0.0
            linear 0.5 alpha 1.0
        on hide:
            alpha 1.0
            linear 0.5 alpha 0.0

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
            xpos 1400
            ypos lbtnY
            linear 0.2 xpos lbtnX

        on hide:
            linear 0.2 xpos 1400

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

    transform summonChatHistory:
        on show:
            alpha 0.0 xpos 640 xcenter 0.5 ypos 180
            linear 0.3 alpha 1.0
        on hide:
            linear 0.1 alpha 0.0

    transform textFloatCenter:
        on show:
            xpos 0.5 ypos 0.5 alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            alpha 1.0
            linear 1.0 alpha 0.0

    transform summonEKG:
        on show:
            alpha 0.0
            linear 0.3 alpha 1.0
            linear 2.0 alpha 0.0
        on hide:
            linear 0.3 alpha 0.0

    transform frameGlitch:
        alpha 0.0
        linear 0.05 alpha 0.1
        linear 0.5 alpha 0.0

    


# transition

    define longFade = Fade(1.0, 0.0, 1.0)
    define longestFade = Fade(2.0, 0.0, 2.0)
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
        default loveConfession = "None"
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
        $entityName = "Fontaine"
        default entityForgiven = False

        # keep count of times said I'm not ready
        default notReady = 0

        $sceneNum = 0
        # Resistance. near end game the player will get a chance to push back a little
        $resistance = 0

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
        # current position of history objects

        currentHistory = 0

        # decision variables. I'm bad at organizing.
        # outfits. These guys are for a few scenes. I don't want to tie love points to this. Too arbitrary.
        outfitBlackDress = 0
        outfitJeans = 0
        outfitPantsuit = 0
        outfitCurrent = ""

        # variables to show that cover chat window
        horrorChat = ""
        horrorTwixt = [Image(
            "img/twixtNorm.png"), Image("img/twixtNorm1.png"), Image("img/twixtNorm2.png")]

    # useful functions

        # functions to show and hide the primary in-game gui: sophie's stream window

        def hideGui():
            renpy.hide_screen("mainGameWindow")
            renpy.hide_screen("chatterbox")
            renpy.hide_screen("leftBtnWindow")
         
            renpy.pause(2.0)

        def showGui():

            renpy.show_screen("mainGameWindow")
            renpy.show_screen("chatterbox")
            renpy.show_screen("leftBtnWindow")
           
            renpy.pause(2.0)

        # create a custom function to display the chat history screen.
        def showChatHistory():
            renpy.show_screen("chatHistory")

            renpy.show_screen("historySelect")
            renpy.show_screen("chatRecaps")

        def hideChatHistory():
            renpy.hide_screen("chatHistory")
            renpy.hide_screen("historyDisplay")
            renpy.hide_screen("historySelect")
            renpy.hide_screen("chatRecaps")

        # create a custom function that takes a string and returns it in reverse

        def reverseString(userInput):
            # apparently this is the slice function, and it steps backward. fluckin python
            return userInput[::-1]

        # return a random x,y coordinate in this game's range. Note: the range is shortened by pixels each direction to account for zoom and RtoL text
        def randomXY():
            temp = []

            temp.append(renpy.random.randint(200, 1080))
            temp.append(renpy.random.randint(100, 600))

            return temp

        # a function that takes a list of strings and shows each one, applying the specified transformation to each sequentially with delay seconds between iterations DOES NOT WORK YET

        def transformList(strings, transform, random):
            for i in strings:
                if random:
                    temp = randomXY()
                renpy.show(i, at_list=[transform])

        # function to construct and initialize multiple arrays. Takes a list of lists, a range, and a value to append in

        def buildArrays(arrayList, max, value):
            # note, range does not include final digit
            for i in arrayList:
                for k in range(0, max):
                    i.append(value)

        # function to pause chat history/ask tania buttons. Sometimes they don't need to work.
        guiPaused = False

        def pauseGui():
            global guiPaused
            guiPaused = True
        def unpauseGui():
            global guiPaused
            guiPaused = False

        #endingTestFunction to set up correct endings for beta testing
        def endingTest():
            for i in allBios:
                i.stringSever()
                i.severView()
                i.fullySever()
            taniaBio.setLove(5)
            fontBio.stringSever()
            fontBio.severView()
            fontBio.fullySever()

        # enable NVL mode for monologue

        #config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve
