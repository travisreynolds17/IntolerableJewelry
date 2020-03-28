# The script of the game goes in this file.
# Theme: A Twitch Streamer playing a VN game based on some dating reality show. Horror game. Commenters slowly get evil. Each contestant
# has some horrible beginning story. Tania is host.


# scenes that exist are
# bg resta, opening restaurant, might use later
# bg bar, a rest area fr contexstant
# bg hallway, the hall outside the dressing room
# bg stage, where the main game takes place
# bg near stage, just off to the side of stage
# bg dressing, the dressing room
# bg playhouse near and far, Robin date


# The game starts here. First, housekeeping.

# define all characters, transforms, variables, etc.
call declarations
# create and declare the chat window.
call chatwindow

# define what we need for main game GUI
call mainWindow

# create and declare the love window
call loveBox
# create and declare button window
call btnWindow
call leftbtnwindow

label start:

  # just to whatever we're testing currently
    jump common1

    # This ends the game.

    return
