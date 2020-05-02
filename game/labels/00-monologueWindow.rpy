# label monologueWindow:

#     init python:

#         def showMonologue():
#             renpy.show_screen("monologueWindow")

#         def hideMonologue():
#             renpy.hide_screen("monologueWindow")

#     screen monologueWindow:
#         modal True

#         frame:
#             for i in toPost:
#                 temp = 0
#                 text i at textFade(monoTextX, monoTextY[temp])
#                 temp += 1
                