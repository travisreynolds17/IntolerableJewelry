# note: this code is temporarily deprecated. 

# label sophieWindow:

#     # create a chat window for the stream. We're gonna add a lot of stuff to this. Character should be able to scroll through it. Sophie will be able to dismiss it.

#     # start python block at init, so this all is ready at the start

#     init python:

#         # useful variables
#         sophieWidth = 180
#         sophieHeight = 290
#         chatPadding = 20

#         # integer to hold pixel position of left side of chat box relative to left of screen. Update these if you change gimp gui
#         sophXPos = 20
#         # ditto y position from top
#         sophYPos = 220

#         # variable to determine max width of text lines inside box so it's not too close to edges
#         sophieMaxWidth = sophieWidth - chatPadding


#         # define a message class
#         class Sophiemessage:
#             # define the initial state of the class. arguments are the function itself, an object representing the speaker with name and text color, and the text
#             def __init__(self, person, message):
#                 self.person = person.name
#                 self.message = message
#                 self.color = person.color

#         # define a sophie side chat log class

#         class Sophielog:
#             def __init__(self):
#                 # by default, the chat will be an empty list. history refers to all the chats accrued over the game.
#                 self.history = []

#             # define a method by which a Message is appended (added) to the end of the chatlog.
#             # def addmessage(self, person, message):
#             #     self.history.append(Sophiemessage(person, message + "\n"))

#             # define a method by which the chatlog is cleared entirely.

#             def delmessages(self):
#                 self.history = []

#             # define a method by which we can add a list of lists to add many message at once between scenes

#             # def bulkMessage(self, newComments):
#             #     self.newComments = newComments
#             #     i = 0
#             #     for i in newComments:
#             #         self.history.append(Sophiemessage(i[0], i[1] + "\n"))

#     # Set a variable to infinity, to be used later. This part is to keep chat box showing newest chat at the bottom rather than forcing player to scroll.
#         #infyadjValue = float("inf")
#         # Create a ui.adjustment object and assign it to a variable so that we can reference it later.
#         #chatyadj = ui.adjustment()

#     # end python block

#     # define a screen that shows our chatlog. Tweak this as needed. If it doesn't fuck up performance, you can prob keep it offscreen most of the time.

#     screen sophieChat:
#         $ chatyadj.value = infyadjValue
#         # declare a frame to hold the whole bit. we're gonna make a transform, and it's declared at frame, to slide the box into sight.
#         frame at summonSoph:

#             viewport id "sophieChat":
#                 yadjustment chatyadj
#                 mousewheel True  # allow player to scroll at will? maybe not. Will def need to pull the box to specific points durint narrative

#                 # side area determines how text is placed in the box
#                 side_area(10, 0, sophieWidth, sophieHeight)
#                 # yinitial determines where in the scrollable box we're anchored. 0.0 would be at the top. 1.0 would be at the bottom.
#                 yinitial 1.0
#                 scrollbars "vertical"
#                 # declare a horizontal box. This will hold a combination of name/message in each horizontal box.
#                 vbox:
#                     # declare a vertical box. These two will loop through the chat object and display the elements within. in the loop, "i" will refer to an entry in the chat history. Remember each element in that history list is a person object with name and color attributes
#                     vbox:
#                         box_wrap True
#                         xsize sophieMaxWidth

#                         for i in soph.history:
#                             text i.person:
#                                 font nameFont
#                                 color i.color

#                             text i.message:
#                                 font messageFont

#     init:
#         default soph = Sophielog()
