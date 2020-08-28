# these labels are mini stories from the perspective of the severed character, providing some light on their part in the story.
label severKylie:
    $hideSeverancePanel()
    menu:
        "Are you sure you wish to cut connection to Kylie?"

        "Sever Kylie":
            jump kylieEnding
        "Maybe better not":
            "Certainly, Kylie does not know how close she came to dissolution."
    return

