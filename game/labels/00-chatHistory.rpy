# IF the chat is going to be important, need to have a chat history to work with. This file wil lay out the screens and buttons needed to make it work.

label chatHistory:

    # declare pertinent variables

    init:
        define chatHistoryBack = Image("img/GUI-historyBack.png")
        # use a chatlog object. We're trying to get the chat history window to repopulate on clicking scene buttons.
        default chatHistory = Chatlog()

    init python:
        histWidth = 1280
        histHeight = 720

        histBoxWidth = 170
        histBoxHeight = 40
        initialBoxX = 60
        initialBoxY = 100
        boxMarginX = 20
        boxMarginY = 20
        histChatWidth = histWidth / 3
        histChatHeight = histHeight / 2
        histPadding = 20
        histMaxWidth = histChatWidth - histPadding

        # holds values for clickable chat menus
        selectedChat = 0
        # holds value of currently selected history
        selectedHistory = ""
        selectedTitle = ""

        # list of collected histories.
        histories = []
        chatTitles = [
            "New Faces",
            "Cassandra",
            "In Studio",
            "Robin",
            "She's Molten",
            "No-Show Lichelle",
            "Tania, My Tania",
            "New Faces *",
            "Elle, oh Elle",
            "My Heroine",
            "Pieta",
            "Conversations",
            "Hold",
            "Hold",
            "Hold",
            "Hold",
            "Hold",
        ]

        chatRecaps = [
            "I was nervous, but I met Cassandra, Robin, Tania, and Lichelle. Tania explained the process of One Week Waifu and reassured me about things after the show. I rested, and picked an outfit for my first date: the mysterious songstress, Cassandra Sanna.",

            "I met up with Cassandra at a bar, which I wasn't super hyped about. My hesitation vanished when I saw her, though. My musical idol, here in person. She offered me a spot on her upcoming album after I revealed my fangirl status. We headed straight off for her studio after that.",

            "What a thrill! Being in my idol's studio was amazing. She even brought me into the recording booth! Underneath that choker, though, I discovered she's deeply scarred and using her voice even a little leaves her with blood in her mouth. She sang a song that reminds me too much of the past.",

            "Tania took me to Robin's playhouse for our date. Robin wasted no time in unleashing her theatrics, shutting off the house lights and ? magically ? appearing right in front of me. It pissed Tania off to no end, but I kind of enjoyed it.",

            "I still can't believe it. Robin revealed, through the power of French cuisine, that she and I met a long time ago, and that she is only 19! Blew my mind twice. Turns out I was her first paying customer in Paris all those years ago, and I guess I made an impression! Then she did some more magic, and then... then, she kissed me. In the dark, just like that. So confident, so... god, save me.",

            "I overslept, to be awoken by a frantic Tania at the door. Not only was it 5 p.m., but I hadn't even showered yet. And then, Lichelle ghosted us. I couldn't believe it. Why go through all this effort just to go truant? Poor Tania's blood pressure was through the roof, and I had a decision to make.",
            
            "I've never been bold. Ever. Something about today, though, brought out my courage and I asked Tania to go out with me instead of Lichelle. She seemed unwilling before, but today she agreed! And... we didn't actually make it to a date. My bedroom was right there, so... \nWe made love for hours. For a minute, it felt like just sex. Raw, animalistic sex. I guess both of us were pent up. But then, I felt her pressed against my back, our arms interlaced, and I felt safe. Something like that. \nI turned in her arms and kissed her forehead, and asked her why she was crying. I guess she'd been doing this for so long, orchestrating other people's love lives, that she'd never taken time to pursue her own. \nWe never got married. Neither of us felt like bringing legal documents into it. We never needed to. Maybe I was the first Waifu on the show to do it, but I found a love in Tania that would last a lifetime. It wasn't always easy. Sometimes she hated me. Still, long after the fires of our sex life had gone from ravenous flames to carefully-tended embers, our communication and understanding burned brighter and brighter. \nTania. My only Suitor. I love you, now and forever.",
            
            "I was nervous, but I met Cassandra, Robin, Tania, and Lichelle. Tania explained the process of One Week Waifu and reassured me about things after the show. I rested, and picked an outfit for my first date: the mysterious songstress, Cassandra Sanna.",

            "I wasn't expecting Lichelle to show up, but sadly my new buddy Tania is injured. I would've liked to talk with her more, you know? Tania makes me feel so comfortable.\nLichelle, though, is more than I was ready for, honestly. Everything about her is power, power, power. I won't lie, she... left me in a state. She could kill me, if she wanted to. I can feel it. It's so... god. I don't have words.\nDeep down, I want... god, save me.",
            
            "I met up with Cassandra at a bar, which I wasn't super hyped about. My hesitation vanished when I saw her, though. My musical idol, here in person.\nI learned some disappointing things, honestly. She's in so much pain. Her friend, my god. Maybe the love of her life killed herself and blamed Cassandra.\nHow can I ask someone suffering so deeply to love me? One-Week Waifu is just a dream. I wasn't happy about it, but we headed to her studio anyway.",
            
            "Well... in summary, I was hit in the head and KO'd by a trash can. My idol currently is in the hospital with alcohol poisoning. My new friend Tania is laid up with a busted ankle. And I rode home with a woman who tended to me like she'd known me forever.\nThe way she plays with that cross necklace she wears burns me alive. I don't know if she's doing that intentionally, or if it's a tic, but it puts me on a breathless edge.",

            "It's impossible to prepare for Robin. It really is.",
            "Hold",
            "Hold",
            "Hold",
            "Hold",
            "Hold",
            "Hold",
            "Hold",
        ]
        # chat history is collected at the end of every major area. Mostly will take place where you have the story beats broken up.

        class History:
            def __init__(self, number, x, y, history, title, recap):
                # ID number corresponds to area of story
                self.number = number
                # where to show clickable buttons to swap between chat histories.
                self.x = x
                self.y = y
                # holds the entire chat log (chat.history) from an area as a list of Message objects
                self.history = history
                # clickable button's text
                self.title = title
                # scene recap. Might show this in its own window?
                self.recap = recap
                # has this section been collected yet
                self.seen = False

        # declare the history variables. Note: most of this won't actually be set in stone until later. Also, each of these histories will be re-declared when they're collected so as to collect the history correctly

        histBoxX = initialBoxX
        histBoxY = initialBoxY  # x and y are just guesses for now

        for i in range(0, 8):
            k = History(i, histBoxX, histBoxY, "hold",
                        chatTitles[i], chatRecaps[i])

            histBoxY += histBoxHeight + boxMarginY
            histories.append(k)

        histBoxX = initialBoxX
        histBoxY = initialBoxY  # x and y are just guesses for now
        histBoxX += histBoxWidth + boxMarginX

        for i in range(8, 16):
            k = History(i, histBoxX, histBoxY, "hold",
                        chatTitles[i], chatRecaps[i])
            histBoxY += histBoxHeight + boxMarginY
            histories.append(k)

        # add more as needed

        # function to collect chat history and cleanup
        # scene takes an int argument

        def getHistory(scene):
            i = scene
            histories[i].history = chat.history
            histories[i].seen = True
       
            chat.delmessages()

        def chatHistUpdate(scene):
            # selectedHistory refers to the currently active history, i.e., you have clicked scene 1 and now scene 1's chat log is stored in selectedHistory
            chatHistory.history = histories[scene].history
           


    # should chat history take up full screen or no? Maybe not. That's a lot of horizontal text. Use your chatbox code to create functions for acquiring and displaying chat text.

    screen chatHistory:

        add chatHistoryBack

        tag chatHistory
        modal True

    screen historyDisplay:
        hbox at alphaFade:

            frame:
                ypos initialBoxY
                xpos 800
                viewport id "chatHistory":
                    mousewheel True
                    yinitial 0.0
                    scrollbars "vertical"
                    # side area determines how text is placed in the box
                    side_area(10, 0, histChatWidth, histChatHeight)
                    
                    vbox:
                        box_wrap True
                        xsize histMaxWidth

                        # histories is a list of stored chat history object.
                        for i in chatHistory.history:
                            text i.person:
                                font nameFont
                                color i.color

                            text i.message:
                                font messageFont

    # this screen needs multiple windows. Let's do this with one screen, shall we? A vbox on the left with history number clickable boxes to change which chat displayed, the chat itself on the right, (or even in the middle of a few columns of scenes) and an exit button upper right. must not allow story underneath to continue if clicked.

    screen historySelect:
        fixed id "historySelectLeft":
            for i in histories:
                button:
                    if i.seen:
                        background "#888888"
                        text i.title:
                            xalign 0.5
                            yalign 0.5
                        action Function(chatHistUpdate, i.number)

                    else:
                        background "#444444"
                        text "??????":
                            xalign 0.5
                            yalign 0.5
                        action NullAction()
                    xpos i.x
                    ypos i.y

                    xsize histBoxWidth
                    ysize histBoxHeight

    # define a screen that holds the chat recaps.


