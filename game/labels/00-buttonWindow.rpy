# label btnWindow:
#     # this file arranges and provides function to two buttons: chat toggle and subscribe. upper right corner.

#     init python:
#         btnWindowHeight = 72
#         btnWindowWidth = 300
#         btnWindowX = 960
#         btnWindowY = 24

#         #variable to hold the on/off state of chat window
#         chatIsOn = False
        

#     screen btnWindow:
#         modal False
#         tag btnWindow

#         fixed at alphaFade:
#             xysize(btnWindowWidth, btnWindowHeight)
#             xpos btnWindowX
#             ypos btnWindowY
                         
#             hbox:       
#                 #this button is intended to toggle the in-game chat window into and out of sight.                          
            
#                 showif chatIsOn == False:
#                     button:
#                         text "Chat":
#                             yalign 0.5
#                             xalign 0.5
#                         xysize(btnWindowWidth/2, btnWindowHeight)
#                         background "#111111"
                        
#                         action [ToggleVariable("chatIsOn"), Show("chatterbox"), Hide("loveScreen")]

#                 showif chatIsOn:
#                     button:
#                         text "Status":
#                             yalign 0.5
#                             xalign 0.5
#                         xysize(btnWindowWidth/2, btnWindowHeight)
#                         background "#111111"
                        
#                         action [ToggleVariable("chatIsOn"), Hide("chatterbox"), Show("loveScreen")]

#                 button:
#                         text "Tips":
#                             yalign 0.5
#                             xalign 0.5
#                         xysize(btnWindowWidth/2, btnWindowHeight)
#                         background "#111111"
                        
#                         action Notify("Not working yet")

                