label endingCass:
    
    if cassBio.severViewed:
        scene bg music room with fade


        "The music room is intimate, warm and comfortable, everything one might expect from a place like this."

        "Even the floor is laid out in a black and white checkerboard pattern, like piano keys."

        "Speaking of which, there's a gorgeous baby grand sitting proudly across the room."

        show c 1p at f12

        "And suddenly, Cassandra."

        show image glitchGui at frameGlitch 

        "She looks exactly like her counterpart in the simulation, somehow."

        "Choker and all."

        s "Cassandra."

        "It's odd. Her name came to my lips, but anything beyond that?"

        "I have no idea what to say. Nice to see you? How've you been? Glad you're alive?"

        show c 1m

        "She doesn't answer. She doesn't have to."

        "Cassandra settles onto the piano bench, brushes a bit of her hair from her eyes."

        "And plays."

        #piano song. whatever.

        "She plays so beautifully."

        "And patiently."

        "She's clearly in no hurry, but that's fine."

        show c 1a

        "Watching her play is mesmerizing. The way she sways, the way she looks almost bored, resigned to her hands going through the motions."

        "She seems so unreachable."

        #fade out music

        "I find myself applauding, which I suppose is just clapping when a person is alone."

        show c 1m

        "She pats the piano bench next to her. Beckons to me with one hand."

        #show cass up close?

        "The bench is warm where she was sitting."

        "I don't know when, or if, to speak."

        "She begins to play again, a jaunty, upbeat tune with just a hint of wistfulness."

        "I don't recognize the tune, but a tilt of her chin leads me to follow her gaze to the sheet music."

        "'To you, my friend'."

        "I should say something. But for now, I only listen."

        "I guess I should have listened sooner."

        #love

        if loveConfession == "Cassandra":
            "She smells like coconut."
            
            "And... hibiscus. Definitely."

            "I wonder what to do."

            "No, I don't. I know."

            "She doesn't flinch when I slip my arm around her waist."

            "A smile. Just a small, small smile."

            "A tear on her cheek."

            "Out there, in here... our relationships were so different."
            
            "But I wonder."

            "Where we are... is it the Cassandra who is open to being with a woman?"

            "I don't know."

            "I won't push her. I won't try to change her."

            "I want to let her make up her own mind."

            "But for just now, just this moment"

            "I want to dream."

            pause 1.0

            "End: She In Silence Sang"
    else:
        "Cassandra's funeral drew quite a crowd."
        "Made headlines. What a tragedy. What a waste of young brilliance."
        "That's true. It's also true the throngs of people who came to be seen at her funeral could have been there for her as she fought with her own addiction."
        "Copy paste that line into almost every junkie's obituary."
        "I had to be there. Mine was the last bed she shared. For better or for worse."
        "She hated me. That much is clear, now. At least, she hated me when we went into the bathroom at Ganymead together."
        "I don't know what changed."
        "I don't know why she switched the doses at the last second."
        "What was in her syringe? What was in mine?"
        pause 1.0
        "Death. Just... death."
        "I'm sorry Cass. I failed you before I even knew you."
        "And again, when I did."

    pause 1.0
    "End: Sobredosis"
    return

    #end. To next ending (Lichelle) by way of EndingTron


