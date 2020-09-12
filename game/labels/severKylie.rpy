# these labels are mini stories from the perspective of the severed character, providing some light on their part in the story.
label severKylie:
    $hideSeverancePanel()

    $renpy.notify("Perhaps you aren't yet ready for this. ")
    menu:
        "Have you come to love the knife?"
        "Yes, I love her":
            
            "I love the knife."
                
            menu:
                "Have you come to love the needle?"
                "I love the needle.":
                    menu:
                        "I love the needle."
                        "Sever Kylie":
        
                            if robinBio.severViewed and persistent.loveFontaine:
                                $severKylie = True
                                "Ah. so you do."
                                "Sophie."
                                "Be true to yourself, at the end."
                                $kylieSevered = True
                            else:
                                "Liar."
                                jump kylieEnding
                        "Maybe better not":
                            "Certainly, Kylie does not know how close she came to dissolution."
                "I do not.":
                    "Then step away."

        "I do not.":
            "Then step away."

        
    return

