label chatwindow:

    # create a chat window for the stream. We're gonna add a lot of stuff to this. Character should be able to scroll through it. Sophie will be able to dismiss it.

    # start python block at init, so this all is ready at the start

    init python:

        #hide/show chat functions to redraw chat window? Yup, this works.
        # flashing the chat window (hiding then immediately showing with no ttransfrom) repaints it, which resets the yadjustment value, forcing new texts to scroll the window.
        def hideChat():
            renpy.hide_screen("chatterbox")
        def showChat():
            renpy.show_screen("chatterbox")
        def flashChat():
            hideChat()
            showChat()

        # useful variables
        chatWidth = 300
        chatHeight = 400
        chatPadding = 20
        # sometimes we need to pause chat for repeated segments.
        chatPause = False

        # integer to hold pixel position of left side of chat box relative to left of screen. Update these if you change gimp gui
        chatXPos = 960
        # ditto y position from top
        chatYPos = 110

        # variable to determine max width of text lines inside box so it's not too close to edges
        chatMaxWidth = chatWidth - chatPadding

        # create all of our chat buddies

        class Chatter:
            def __init__(self, name, color):
                self.color = color
                self.name = name

            def setName(self, name):
                self.name = name

        # For chatbox

        nameFont = "fonts/EncodeSans-ExtraBold.ttf"
        messageFont = "fonts/EncodeSans-Light.ttf"
        # chatnames
        bong = Chatter("OberBong", "#421332")
        elsa = Chatter("ElsaLater", "#927732")
        fizz = Chatter("FizzyFizion", "#f21332")
        egg = Chatter("TweeterEgg101", "#a21332")
        fon = Chatter("Fontaine", "#921344")
        obliv = Chatter("Oblivion", "#921332")
        bar = Chatter("TwixtBar", "#999332")
        beav = Chatter("AngeredBeaver69", "#921332")
        cake = Chatter("poundCake", "#bbb123")
        shub = Chatter("Shub-Nickelrath", "#765633")
        crab = Chatter("Crablegs", "555125")
        sophie = Chatter("Sophie Koenig", "eeeeee")
        kyli = Chatter("Kylie", "eeeeee")
        unkn = Chatter("", "#000000")

        # define a message class

        class Message:
            # define the initial state of the class. arguments are the function itself, an object representing the speaker with name and text color, and the text
            def __init__(self, person, message):
                self.person = person.name
                self.message = message
                self.color = person.color

        # define a chat log class
        class Chatlog:
            def __init__(self):
                # by default, the chat will be an empty list. history refers to all the chats accrued over the game.
                self.history = []

            # define a method by which a Message is appended (added) to the end of the chatlog.
            def addmessage(self, person, message):
                if chatPause == False:
                    self.history.append(Message(person, message + "\n"))
                    flashChat()

            # define a method by which the chatlog is cleared entirely.

            def delmessages(self):
                self.history = []

            # define a method by which we can add a list of lists to add many message at once between scenes

            def bulkMessage(self, newComments, delay):
                self.newComments = newComments
                self.delay = delay
                i = 0
                for i in newComments:
                    self.history.append(Message(i[0], i[1] + "\n"))
                    if delay == "random":
                        suchRandom = renpy.random.randint(3, 10)
                        self.delay = suchRandom / 10
                    if self.delay > 0:
                        renpy.pause(self.delay)
                flashChat()

            # function to append a message to chatHistory in one continuous line
            # think of speed and modulus as numerator and denominator. Renpy pause, even at time 0, pauses for a bit. The lower modulus, the faster the text.
            def addLinearMessage(self, speaker, string, speed, modulus):
                self.string = string
                self.history.append(Message(speaker, ""))
                count = 0
                for i in string:
                    chat.history[-1].message += i
                    count += 1
                    if count % modulus == 0:
                        renpy.pause(speed)
                flashChat()

    # Set a variable to infinity, to be used later. This part is to keep chat box showing newest chat at the bottom rather than forcing player to scroll.
        infyadjValue = float("inf")
        # Create a ui.adjustment object and assign it to a variable so that we can reference it later.
        chatyadj = ui.adjustment()

    # end python block

    # define a screen that shows our chatlog. Tweak this as needed. If it doesn't fuck up performance, you can prob keep it offscreen most of the time.

    screen chatterbox:
        tag chatterbox
        $ chatyadj.value = infyadjValue
        # declare a frame to hold the whole bit. we're gonna make a transform, and it's declared at frame, to slide the box into sight.
        frame:
            xpos chatXPos
            ypos chatYPos
            
            viewport id "chatbox":
                yadjustment chatyadj
                mousewheel True  # allow player to scroll at will? maybe not. Will def need to pull the box to specific points durint narrative

                # side area determines how text is placed in the box
                side_area(10, 0, chatWidth, chatHeight)
                # yinitial determines where in the scrollable box we're anchored. 0.0 would be at the top. 1.0 would be at the bottom.
                yinitial 1.0
                scrollbars "vertical"
                # declare a horizontal box. This will hold a combination of name/message in each horizontal box.
                vbox:
                    # declare a vertical box. These two will loop through the chat object and display the elements within. in the loop, "i" will refer to an entry in the chat history. Remember each element in that history list is a person object with name and color attributes
                    vbox:
                        box_wrap True
                        xsize chatMaxWidth

                        for i in chat.history:
                            text i.person:
                                font nameFont
                                color i.color

                            text i.message:
                                font messageFont

    # To add a chatmessage, you might do:
    # $ chat.addmessage("Oberbong", "Wow, I love booty")

    # a screen for showing images ver the chat

    screen chatHorror:
        fixed at summonChatHorror:
            add horrorChat
            


    # declare the chat object.

    init:
        default chat = Chatlog()
