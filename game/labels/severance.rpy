label severance:
    # use this for ending severance.

    # RULES. WE are not changing the story much more. Okay? Finish this bitch.

    # Put in a few easter eggs. The girls can't be severed until they're ready. avoid joke answers with a net response like: no link found

    #answers: Kylie

    # actually, maybe an ending where sophie wakes up and can't remember anything?

    # Fontaine - only way to get best ending. Make sure you stress this.
    # Self: gives Kylie ending
    # Any of the girls: "She is plagued with guilt. She must be absolved to achieve severance."

    init python:

        # useful variables
        severanceInput = ""
        severanceOptions = ["cassandra", "lichelle", "robin",
                            "tania", "god", "fontaine", "penis", "kylie", "louisa"]
        severAvailable = False
        underLabelText = ""
        # need this because button action functions can't take arguments.
        currentInput = ""
        # icon

        # useful functions

        def sanitizeInput(text):
            # convert to string
            temp = str(text)
            # strip spaces
            temp2 = temp.replace(" ", "")
            temp = temp2.lower()
            global underLabelText
            # do this to clear text with each keystroke. that way we don't have messages just hanging around.
            underLabelText = ""

            # test for nicknames, analogs: Tania's identity giveaway here

            if temp == "cass":
                temp = "cassandra"
                underLabelText = "analog acceptable for cassandra"
            if temp == "elle":
                temp = "lichelle"
                underLabelText = "analog acceptable for lichelle"
            if temp == "tania":
                underLabelText = "analog acceptable for elsa"
            if temp == "elsa":
                underLabelText = "analog acceptable for tania"
            if temp == "fontaine":
                underLabelText = "analog acceptable for heroin"
            if temp == "onyx":
                temp = "cassandra"
                underLabelText = "analog acceptable for cassandra"
            if temp == "legs":
                temp = "robin"
                underLabelText = "analog acceptable for robin"
            if temp == "heroin":
                underLabelText = "analog acceptable for fontaine"

            testInput(temp)

        # special severances that cannot be achieved in game
        def severKylie():
            renpy.jump("kylieEnding")

        def severFontaine():
            fontBio.stringSever()

        def severToggle():
            global severAvailable

            if severAvailable:
                renpy.hide_screen("severButton")
                severAvailable = False
            else:

                renpy.show_screen("severButton")
                severAvailable = True

        def testInput(text):
            # tests input to see if it matches possibilities
            global underLabelText
            global currentInput

            if text == "cassandra":
                if cassBio.severed:
                    renpy.notify("Cassandra's severance is complete.")

                else:
                    renpy.notify("Cassandra's severance is incomplete.")

            elif text == "lichelle":
                if lichBio.severed:
                    renpy.notify("Lichelle's severance is complete.")

                else:
                    renpy.notify("Lichelle's severance is incomplete.")

            elif text == "robin":
                if robinBio.severed:
                    renpy.notify(
                        "Robin's absolution is complete. Severance ready.")

                else:
                    renpy.notify("Robin's severance is incomplete.")

            elif text == "tania":
                if lichBio.severed:
                    renpy.notify(
                        "Tania's absolution is complete. Severance ready.")

                else:
                    renpy.notify("Tania's severance is incomplete.")

            elif text == "fontaine":
                if fontBio.severed:
                    renpy.notify(
                        "The Intervascular Anomaly's severance is complete. Severance ready.")

                else:
                    renpy.notify(
                        "The Intervascular Anomaly's absolution is incomplete. It cannot be severed yet.")

            elif text == "penis":
                renpy.notify(
                    "Poor David. Only one of those exists in this entire reality, and you wish to sever it.")

            elif text == "kylie":
                renpy.notify("Can a kite fly without its String?")

            elif text == "god":
                renpy.notify("Nietszche approved.")

            elif text == "louisa":
                renpy.notify(
                    "It is too late for her. But then, it always was.")

            else:
                renpy.notify("Input match not found.")
            currentInput = text

        def showSeverancePanel():
            #
            renpy.show_screen("severancePanel")

        def hideSeverancePanel():
            renpy.hide_screen("severancePanel")
            global currentInput
            currentInput = ""

        def showSeveranceMenu():
            renpy.show_screen("severanceMenu")
            renpy.call("severanceChoices")

        def hideSeveranceMenu():
            renpy.hide_screen("severanceMenu")

        def severCommit():
            # temp
            global currentInput
            renpy.notify(currentInput)

            if currentInput == "cassandra":
                if cassBio.severed:
                    renpy.call("severCassandra")
                else:
                    renpy.notify("Cassandra's absolution is incomplete.")

            if currentInput == "robin":
                if robinBio.severed:
                    renpy.call("severRobin")
                else:
                    renpy.notify("Robin's absolution is incomplete.")

            if currentInput == "lichelle":
                if lichBio.severed:
                    renpy.call("severLichelle")
                else:
                    renpy.notify("Lichelle's absolution is incomplete.")

            if currentInput == "tania":
                if taniaBio.severed:
                    renpy.call("severTania")
                else:
                    renpy.notify("Tania's absolution is incomplete.")

            if currentInput == "kylie":
                renpy.call("severKylie")
                renpy.notify("yup")

            if currentInput == "fontaine":
                fontBio.stringSever()
                renpy.call("severFontaine")

# label shows the choice menu for severance
label severanceChoices:
    $severToggle()

    while doneSevering == False:
        scene bg black with fade

        menu:

            "What? What is... sever them? Sever them from me?"

            "Cassandra" if cassBio.severViewed == False:
                $hideSeveranceMenu()
                pause 2.0
                call severCassandra from _call_severCassandra

            "Lichelle" if lichBio.severViewed == False:
                $hideSeveranceMenu()
                pause 2.0
                call severLichelle from _call_severLichelle
            "Robin" if robinBio.severViewed == False:
                $hideSeveranceMenu()
                pause 2.0
                call severRobin from _call_severRobin
            "Tania" if taniaBio.severViewed == False:
                $hideSeveranceMenu()
                pause 2.0
                call severTania from _call_severTania
            "Kylie":
                $hideSeveranceMenu()
                pause 2.0
                call severKylie from _call_severKylie
            "The Intervascular Anomaly" if fontBio.severViewed == False and fontaineRevealed:
                $hideSeveranceMenu()
                pause 2.0
                $fontBio.severView()
                "Freed from... it? But who is free? She or we?"
            "No... nobody.":
                $doneSevering = True

    $doneSevering = False
    $hideSeveranceMenu()
    scene bg dressing with fade
    play music bedroom fadein 3.0
    $showGui()
    $severToggle()
    pause


transform summonSeverance:
    on show:
        xpos 0.2 ypos 0.0
        easein 0.5 xpos 0.2 ypos 0.1
    on hide:
        easein 0.5 ypos 0.0

screen severanceMenu:
    modal True
    fixed at alphaFade:
        add severanceBack


screen severancePanel:
    modal True

    fixed at alphaFade:
        add severanceBack
        button:
            background iconBtnBack
            ypos 580
            xsize 100
            ysize 100
            xpos 50
            action Function(hideSeverancePanel)

        input:
            default ""
            changed sanitizeInput
            xsize 480
            ysize 20
            xpos 400
            ypos 400
            length 12

        text underLabelText:
            xsize 480
            ysize 20
            xpos 400
            ypos 450

        button:
            image iconBtnCommit
            xalign 1.0
            xsize 100
            xpos 900
            ypos 400
            action Function(severCommit)

# define a quick transform to show and hide button

transform severButton:
    xpos - 20 ypos 5

    on show:
        easein 3.0 xpos 450 ypos 11
    on hide:
        easein 1.0 xpos - 200 ypos 5

screen severButton:
    modal False

    fixed at severButton:
        xpos 30
        ypos 100
        button:
            xysize(lbtnWidth, lbtnHeight)
            background btnSever
            action Function(showSeveranceMenu)
            # Note: We may go back to showSeverancePanel at some point. For now, it will just be a menu.
