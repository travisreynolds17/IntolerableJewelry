# 1. Subscribe Button                   SBBTN
# 2. Bulk chatt add                     CHATT
# 3. Hide/show Chat                     HSCH
# 4. Hide/show GUI                      HGUI

#--------------------------------------------------------------------------
# SBBTN
# pull in subscribe button. alter for other button messages

#move button in from left
show btn-subscribe at subscribeCenter with moveinleft
        # dialog or pause
#move button out
show btn-subscribe at subscribeLeave with moveoutleft

#--------------------------------------------------------------------------

#2. Bulk chat add                                                               CHATT
# between scenes, if we need to add several messages to chat, this snippet will be a little easier than typing $chat.addmessage over and over. I hope. add as many comments as you need.

python:
        newComments = [

                [name, "message"],
                [name, "message"]

        ]
        chat.bulkMessage(newComments)

#3. Hide/show chat. For when Sophie manipulates the board.                      HSCH

#to hide chat. Don't use if else because player can control chat.
if chatIsOn:
        hide screen chatterbox
        $chatIsOn = False
pause 1.0

if chatIsOn == False:
        show screen chatterbox
        $chatIsOn = True
pause 1.0

#-------------------------------------------------------------------------------------------------

# 4. Hide/show GUI. For when a full screen splash is needed.                    HGUI
#hide
hide screen mainGameWindow 
hide screen loveScreen 
hide screen chatterbox 
$chatIsOn = False
hide screen btnWindow 
pause 2.0

#show
show screen mainGameWindow 
show screen loveScreen 
show screen chatterbox 
$chatIsOn = True
show screen btnWindow 
pause 2.0