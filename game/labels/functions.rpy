    # a file for "functions" to be held and accessed with CALL.


label severInput:
        #Severinput first checks to see if Kylie has been severed. If so, the ending is determined already. 
        # next, it gets input from the player. If the player keys in the severance function provided in game with a name as argument, there are effects.
        # if the girl's correct code has already been entered, the check loops back to player input so a player doesn't waste a chance. Counts down.
        # if all have been severed, check will stop popping up.
    if severAll == True and severChances > 0:
        "Fate determined."
        $success = True
    else:
        $success = False
        #Kyliecheck
        if severKylie == False:

            while success == False:
                $userInput = renpy.input("")
                
                python:
                    if len(userInput) > 0:
                        userInput = userInput.strip()
                        userInput = userInput.lower()

                        #input check.
                        if userInput == "stringsever(cassandra)":
                            if severCass == True:
                                un("Repeat input detected. Object \"Cassandra\" does not exist.", True)
                                success = False
                            else:
                                un("Validated.", True)
                                severCass = True
                                success = True

                        elif userInput == "stringsever(robin)":
                            if severRobin == True:
                                un("Repeat input detected. Object \"Robin\" does not exist.", True)
                                success = False
                            else:
                                un("Validated.", True)
                                severRobin = True
                                success = True

                        elif userInput == "stringsever(lichelle)":
                            if severLich == True:
                                un("Repeat input detected. Object \"Lichelle\" does not exist.", True)
                                success = False
                            else:
                                un("Validated.", True)
                                severLich = True
                                success = True

                        elif userInput == "stringsever(tania)":
                            if severTania == True:
                                un("Repeat input detected. Object \"Tania\" does not exist.", True)
                                success = False
                            else:
                                un("Validated.", True)
                                severTania = True
                                success = True

                        elif userInput == entityName:
                            if severEntity == True:
                                un("Repeat input detected. Object does not exist.", True)
                                success = False
                            else:
                                un("Validated.", True)
                                severEntity = True
                                success = True

                        elif userInput == "stringsever(god)":
                            un("Validated.", True)
                            un("for(i = 0; i < len(multiverse); i++\n  multiverse[i].pop()).", True)
                            existence = existence / 0

                        else:
                            success == False
                            un("Validation failed.", True)
                #end input check.

                #else here related to length check
                    else:
                        un("Severance failed.", True)
            call allSeveredCheck from _call_allSeveredCheck
            $severChances -= 1
            "There are [severChances] attempts remaining."
            if severChances == 0:
                "Fate determined. Thus we cast our destiny into the hands of catastrophe."
        
        # else of kylie check below
        else:
            "Fate determined. The future no longer is yours to influence."



label allSeveredCheck:

    python:
        if severCass == True:
            if severRobin  == True:
                if severLich  == True:
                    if severTania  == True:
                        if severEntity  == True:
                            un("Fate determined. Resign yourself to inevitability.")
                            severAll = True




#--------------------------------------------------------------------
# quick legend: each girl has an array. 0 index is the main one that determines whether we're sitll in the menu loop of asking questions. indexes 1 through 5 correspond to whether a question's already been asked. Each girls' interview is in the same order, same questions.

label buildArrays:
    #build list because python is dumb.

    python:
        i = 0
        

        while i < 6:
            cassDone.append(False)
            robinDone.append(False)
            taniaDone.append(False)
            lichDone.append(False)

            i += 1
    
#=====================================================================