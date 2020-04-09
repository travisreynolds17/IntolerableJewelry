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
        selectedRecap = ""

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
            "Perfect Hell",
            "Am I Evil",
            "Fugue",
            "R/BG13:14-15",
            "Hold",
        ]

        chatRecaps = [
            "I was nervous, but I pushed through my insecurity for long enough to meet Cassandra, Robin, Tania, and Lichelle.\n\nTania explained the process of One Week Waifu and reassured me about things after the show. I rested, and picked an outfit for my first date with the mysterious songstress, Cassandra Sanna.\n\nWell. Mysterious isn't the right word. ;)",

            "I met up with Cassandra at a bar, which I wasn't super hyped about. I'm not much of a drinker. \n\nMy hesitation vanished when I saw her, though. My musical idol, here in person. She's shorter than I thought she'd be, but the shape of her mouth was exactly the way I remember it. It was everything I could do to keep from shrieking and asking a million questions.\n\nThankfuly, Cassandra handled my glistening fandom with amused accommodation. Then, she offered me a spot on her upcoming album after I revealed my fangirl status. We headed straight off for her studio after that. I was losing my mind!",

            "What a thrill! Being in my idol's studio was amazing. She even brought me into the recording booth! Underneath that choker, though, I discovered she's deeply scarred and using her voice even a little leaves her with blood in her mouth. She sang a song that reminds me too much of the past.",

            "Tania took me to Robin's playhouse for our date. Robin wasted no time in unleashing her theatrics, shutting off the house lights and (as far as I can tell) magically appearing right in front of me. It pissed Tania off to no end, but I kind of enjoyed it.\n\nCan I tell you something? It's hard to explain, but something about Robin made me nostalgic. It could be her perfume. It could be the way she looks like she's always right on the edge of tears.\n\nSome part of me wishes I was more of a thirsty girl, so I could objectify her at least a little bit.\n\nIt sounds stupid, but without that I feel like she's too close to my heart and mind, too quickly. At least being hot for her right away would put up a bulwark.",

            "I still can't believe it. Robin revealed, through the power of French cuisine, that she and I met a long time ago, and that she is only 19! Blew my mind twice.\n\nTurns out I was her first paying customer in Paris all those years ago, and I guess I made an impression! Then she did some more magic, and then... then, she kissed me. In the dark, just like that. So confident, so... Her perfume sets me at ease even as her touch sets me on fire. I might have lied earlier about being thirsty. God, save me.",

            "I overslept, to be awoken by a frantic Tania at the door. Not only was it 5 p.m., but I hadn't even showered yet. How the hell did I sleep all day?\n\nSome part of me thinks Robin drugged me. What a story that would make. I'm not woozy though, and I remember last night clearly.\n\nAnd then, Lichelle ghosted us. I couldn't believe it. Why go through all this effort just to go truant? Poor Tania's blood pressure was through the roof.\n\nCan we talk about Tania for a second? She's instantly someone I feel like I can trust. That's probably stupid. She reminds me of a school nurse, somehow. A cute school nurse, which complicates the issue somewhat.",

            "I've never been bold. Ever. Something about today, though, brought out my courage and I asked Tania to go out with me instead of Lichelle. She seemed unwilling before, but today she agreed! And... we didn't actually make it to a date. My bedroom was right there, so... \nWe made love for hours. For a minute, it felt like just sex. Raw, animalistic sex. I guess both of us were pent up. But then, I felt her pressed against my back, our arms interlaced, and I felt safe. Something like that. \nI turned in her arms and kissed her forehead, and asked her why she was crying. I guess she'd been doing this for so long, orchestrating other people's love lives, that she'd never taken time to pursue her own. \nWe never got married. Neither of us felt like bringing legal documents into it. We never needed to. Maybe I was the first Waifu on the show to do it, but I found a love in Tania that would last a lifetime. It wasn't always easy. Sometimes she hated me. Still, long after the fires of our sex life had gone from ravenous flames to carefully-tended embers, our communication and understanding burned brighter and brighter. \nTania. My only Suitor. I love you, now and forever.",

            "I was nervous, but I met Cassandra, Robin, Tania, and Lichelle. Tania explained the process of One Week Waifu and reassured me about things after the show. She seemed like a trustworthy person, someone I could lean on if all this were to become more than I can handle.\n\nI don't want to talk about Cassandra just yet, because I want to make sure about something.\n\nRobin is a demon. A spectre. A wraith. Something. When she looked directly at me it was all I could do not to cry, inexplicably. I can't wait to get to know her.\n\nLichelle was a house of fire. What a bright smile! She seemed so genuine, like a person who would tell you exactly when and how she would beat your ass should you cross her.\n\nI rested, and picked an outfit for my first date: the mysterious songstress, Cassandra Sanna.",

            "I wasn't expecting Lichelle to show up at my door today, but sadly my new buddy Tania is injured. I would've liked to talk with her more, you know? Tania makes me feel so comfortable.\n\nLichelle, though, was more than I was ready for, honestly. Everything about her is power, power, power. I won't lie, she... left me in a state. She could kill me, if she wanted to. I can feel it. It's so... god. I don't have words.\n\nDeep down, I want... nope, I don't wanna talk about it. Thanks.",

            "I met up with Cassandra at a bar, which I wasn't super hyped about. My hesitation vanished when I saw her, though. My musical idol, here in person.\n\nI learned some disappointing things, honestly. She's in so much pain. Her friend, Marina. My god. It's like the love of her life killed herself and blamed Cassandra.\n\nIt can't have been that long ago.\n\nHow can I ask someone suffering so deeply to love me? One-Week Waifu is just a dream.\n\nShe drank a lot. A lot. I can't believe someone her size can still walk after that many shots. Who the hell let her onto this show in such a state? She needs help. She needs R/BG13:14-15.\n\nI wasn't happy about it, but we headed to her studio anyway.",

            "Well... in summary, I was hit in the head and KO'd by a trash can. My idol currently is in the hospital with alcohol poisoning. My new friend Tania is laid up with a broken ankle.\n\nLichelle.\n\nDid you ever meet someone who legit made your knees weak? I know nothing about her. The things I felt were basic bitch animal lust. She smells alive. Her voice is husky, sultry, delicious.\n\nI rode home with such a woman who tended to me like she'd known me forever after that can cracked me.\n\nThe way she plays with that cross necklace when we're in the car burns me alive. I don't know if she's doing that intentionally, or if it's a tic, but it puts me on a breathless edge.\n\nTrue story? If this show was called 'One Week Stand' Lichelle and I might never leave my room. What the hell am I even talking about?",

            "R/BG13:14-15. Eye bee leave inn ewe. lol. el o el. l OWE l. ul. oh. el. R/BG13:14-15. \nIt's a strange sensation to feel so disconnected. Nightmare visions plague me. I dream of snow, and cold. I dream of puncture wounds. \nI dream of someone's coat under my hands, submerged in... something?",

            "Nothing in life is easy, is it? Somehow I found myself surrounded by desirable Suitors, I was paid to have them compete over me, and yet I find myself sinking a little. \n\nMaybe it's because Cassandra turned out to be a real person and not my idealized version of her. Maybe it's because Lichelle keeps grabbing me by the id and squeezing. \n\nI'm not a toy for them to play with. I don't want to get drunk. I don't want sudden, breath-stealing kisses. \n\nI don't want to admit I want those things. Confusion holds me in her arms.\n\nRobin is up next and only god knows what perfect hell she's going to put me though.",

            "I'm terrified of her.\n\nRobin moves like a shadow. I know she has feet that touch the ground because I noticed she wears cute open-toed shoes, but I'm still not sure she isn't a ghost. \n\nThere's something so painfully familiar about her. It's like... have you ever had a possible job opportunity crop up, and you miss the call? Then you have a voicemail asking for a callback, and you're like, 'Oh god, do I even want to call back? What if I just don't call back? It'll be okay, right? OH GOD.' \n\nIt's that kind of feeling. That sick-in-the-gut, cold-in-the-heart sensation. That desparate need to cry and tell someone, anyone, that I'm so sorry for whatever I've done even if I haven't done anything.\n\nI want to run. I'm so scared, so scared right now. I don't know why.",

            "... I don't believe her. I don't believe her. I don't believe her. I can't believe her. There's no way. No. I don't. No. I won't. That's not me. It isn't. She isn't real. She's a liar. Liar.\n\nIn the dark I wasn't afraid of her anymore. I should've been. It should've been the scariest time, even. I saw what she can do. That knife gleamed, so bright, so bright, right out of nowhere.\n\nI thought Lichelle was gonna smash her face. But then Robin was just behind her. Wrapped around her. Robin could've killed her so easily from there. I couldn't do anything. I would've watched a woman's murder, frozen in place.\n\nIs Robin like that? Could she do it? If I believe her story, the answer is absolutely, yes. Does Lichelle know how close she came to dying?\n\nCan I tell you a secret?\n\nThe blood on Lichelle was fake.\n\nThe blood on my neck was real.\n\nWhen that edge dragged across my neck, I... that jolt. I felt it, electrical. It tucked my tailbone, it dragged me off the chair.\n\nAm I horrible? She owns me, now, and I want it. I want it so badly.\n\nI'm sorry, mom. I'm a monster.",

            "... hello? Hello? Someone, I can't... she's not moving. I think she's dead. I can't move her. She's frozen. I'm freezing. Help. Help me. Help her! please please please Louisa don't leave me don't die I'm sorry wake up wake up wake up you're okay you're fine honey breathe please breathe I can't do this alone come back, come back, come back, you're so cold, so\n\ncold, I love you, I never said it, I never said it! I never said it! someone! anyone! Take me instead! Kill me, save her! Give her my breath my heart my lungs whatever she needs, god, are you real? not her! me! I hate you! This is my fault! This is your fault! God! Elsa! David! LOUISA COME BACK please~\n\nThe Clinic defines dissociation as a separation of mental focus from physical reality. There are three types of dissociative disorders: Dissociative amnesia, dissociative identity disorder, and depersonalization-derealization disorder.\n\nI wonder what it would be like for all of those things to happen at once. And what kind of stimulus could cause such a thing?",

            "14 And deceiveth them that dwell on the earth by the means of those miracles which he had power to do in the sight of the beast; saying to them that dwell on the earth, that they should make an image to the beast, which had the wound by a sword, and did live.\n\n15 And (she) had power to give life unto the image of the beast, that the image of the beast should both speak, and cause that as many as would not worship the image of the beast should be killed.\n\n14 Everywhere are (her) hands and feet, eyes, heads, and faces. (Her) ears too are in all places, for (she) pervades everything in the universe.\n\n15 Though (she) perceives all sense-objects, yet (she) is devoid of the senses. (She) is unattached to anything, and yet (she) is the sustainer of all. Although (she) is without attributes, yet (she) is the enjoyer of the three modes of material nature.\n\nDo you think if I position myself as a goddess, you would become my missionary? ;) xoxoxo",
            
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

        def getAllHistories():
            #test function to fill out recap and titles section
            for i in histories:
                i.seen = True

        def chatHistUpdate(scene):
            global selectedRecap
            # selectedHistory refers to the currently active history, i.e., you have clicked scene 1 and now scene 1's chat log is stored in selectedHistory

            # chatHistory here refers to the box itself
            chatHistory.history = histories[scene].history
            selectedRecap = histories[scene].recap

        def selectRecap(value):
            newRecap = int(value)
            return newRecap
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
                            text "FUCK"
                            # text i.person:
                            #     font nameFont
                            #     color i.color

                            # text i.message:
                            #     font messageFont

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

    screen chatRecaps:
        frame at summonRecaps:
            viewport id "chatRecaps":

                yinitial 0.0
                mousewheel True
                scrollbars "vertical"
                side_area(10, 0, histChatWidth, histChatHeight)
                vbox:
                    box_wrap True
                    xsize histMaxWidth
                    text selectedRecap
                    # text selectedRecap.recap
