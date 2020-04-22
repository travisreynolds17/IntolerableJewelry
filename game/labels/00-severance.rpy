label severance:
    #this label will deal with the stringSever() function

    init:

        transform summonSever:
            on show:
                zoom 0.0
                linear 0.2 zoom 1.0
            on hide:
                linear 0.2 zoom 0.0

    init python:

        #necessary variables

        # to hold all successful severed as strings of the character's name
        allSevered = []         

        #default list of strung characters. Remember, god is an instant game over so won't appear here
        allStrung = ["cassandra", "lichelle", "robin", "tania", "kylie"]

        #function to be attached to subscribe button when it changes in common 4. Opens slide menu for player input.
        def inputToSever():
            renpy.show_screen(severInput)


        # function to format code correctly for verifying.
        def sanitizeInput(playerInput):
            tempInput = str(playerInput)
            tempInput = tempInput.lower()
            strippedInput = tempInput.strip()
            finalInput = strippedInput.replace(" ", "")
            return finalInput

        # function tests player's input to find
        def verifyInput(playerInput):
            matchFound = False
            # make sure there are some Strung left
            if len(allStrung) > 0:
                # see if player input matches the correct names
                for i in allStrung:
                    if allStrung[i] == playerInput:
                        allSevered.append(allStrung[i])
                        allStrung.remove(playerInput)
                        renpy.notify("[playerInput].severed = True")
                        matchFound = True
                    #if no match, message
                    if matchFound == False:
                        renpy.notify("Input not recognized as severable object.")
            
            else:
                renpy.notify("All severance complete.")



    screen severInput:
        modal True
        fixed at summonSever:
        
            input:
                id "input" 
                default "--------"
            