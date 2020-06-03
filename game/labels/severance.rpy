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
        #icon
        
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
            # alters state of subscribe button such that it can be clicked.
            # this communicates directly with functions in leftbuttonwindow file.
            global severAvailable

            if severAvailable:
                setSubBtn("stringSever")
                severAvailable = True
            else:
                setSubBtn("Subscribe")
                severAvailable = False

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

        def showSeverancePanel():
            #
            renpy.show_screen("severancePanel")

        def hideSeverancePanel():
            renpy.hide_screen("severancePanel")
            global currentInput
            currentInput = ""

        def severCommit():
            # temp
            global currentInput
            renpy.notify("WARNING: Severance cannot be undone.")

            if currentInput == "cassandra":
                if cassBio.severed:
                    renpy.call_label("severCass")
                else:
                    renpy.notify("Cassandra's absolution is incomplete.")

            if currentInput == "robin":
                if robinBio.severed:
                    renpy.call_label("severRobin")
                else:
                    renpy.notify("Robin's absolution is incomplete.")

            if currentInput == "lichelle":
                if lichBio.severed:
                    renpy.call_label("severLichelle")
                else:
                    renpy.notify("Lichelle's absolution is incomplete.")

            if currentInput == "tania":
                if taniaBio.severed:
                    renpy.call_label("severTania")
                else:
                    renpy.notify("Tania's absolution is incomplete.")

            if currentInput == "kylie":
                renpy.call_label("severKylie")

            if currentInput == "fontaine":
                fontBio.stringSever()
                renpy.call_label("severFontaine")


# these labels are mini stories from the perspective of the severed character, providing some light on their part in the story.
label severKylie:
    $hideSeverancePanel()
    menu:
        "Are you sure you wish to cut connection to Kylie?"

        "Sever Kylie":
            jump kylieEnding
        "Maybe better not":
            "Certainly, Kylie does not know how close she came to dissolution."
    return


label kylieEnding:
    $hideSeverancePanel()
    scene bg black

    k "Huh?"

    k "Why does... ow! I... why does..."

    k "it hurts"

    k "why"

    k "somebody"

    k "h... h...hel..."

    # cracked screen?
    # SFX
    # sophie's eyes roll back
    # she falls

    # some quote about there's no using burning the boats while you're still on them

    jump endCredits
    return

transform summonSeverance:
    on show:
        xpos 0.2 ypos 0.0
        easein 0.5 xpos 0.2 ypos 0.1
    on hide:
        easein 0.5 ypos 0.0


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
