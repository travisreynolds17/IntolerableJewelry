label realWorld3:

    
    "She was the host."

    "For a while."

    "I met her there, sitting outside by the fountain, scribbling away on my sketch pad."

    "Hey. That's mine."

    play music tension fadein 4.0


    "Where did you find that, I asked her, courageous."

    "She showed me her drawing, and I was amazed at how precise a single point could be."

    "A single point, molecular sharp, somehow evoking an intense, pillowy calmness."

    "How could you draw like that, miss? And... where did you find my sketch pad?"

    "Snow wafts obliviously to the earth."

    "I'll show you, she would have said, if I could have heard it."

    "It's cold, I wondered. Inside? Inside the bar?"

    "We are already there, and I love you."

    "Mmm. Thank you for saying so."

    "You know Elsa, too?"

    "You've been watching me."

    "Yes."

    "I was waiting for you to say something."

    "This is how our conversation went."

    menu:
        "Are we dreaming?"

        "Iterating torpor":
            "Shh. I don't think the swelling will go down again."
            "Oh. The pencil was bad, wasn't it."

        "Suicide symptomatic of Birth":
            "Nothing is anything or anything else."
            "Whose blood is that? The tile feels cool."

    "You're yellow."

    "Was I always?"

    "I love you."

    "The pencil was no good."

    "It wasn't, was it."

    "Tainted. The tainted pencil drew corrupt pictures."

    "Oh, no."

    "You aren't breathing."

    "I'm not, am I. Oh, well."

    "I love your lap."

    "Please breathe."

    "I should?"

    "It's a good idea, isn't it?"

    "No. Why did you corrupt the pencil?"

    "You knew about that, Sophie?"

    "Mm. I can't hear your music anymore."

    "You liked it?"

    "Yes. I can't see though so it's sad I can't hear it."

    "Her name was Louisa."

    "Was? Her?"

    "The tile is cold, isn't it?"

    "Mm. But your lap is warm."

    "She's cold now. Because of you. But I love you."

    "I love you, too."

    "I'm taking your clothes away. Do you mind?"

    "So tired."

    "Sleep. Never wake up."

    "Mmkay."

    "Promise?"

    "Mm."

    "You're the most yellow you've ever been."

    "Thank you for saying that. I feel colder than the tile. Sweating."

    "You should."

    "Kiss me."

    "I'd love to."

    "What did you give me? You're kissing me, but I can't feel your lips."

    "I only ever felt nothing at you."

    "I can't feel your fingers. What did you put in me?"

    "Peace."

    "Am I going to die?"

    "I hope so."

    "You're sure?"

    "It's what I want, anyway."

    "Oh. I'm happy."

    "Why would you be happy when I'm the one killing you?"

    "I miss your music."

    "... shut up."

    "Your notes took the hurt away, some. Just some, but some."

    "Shut up."

    "Am I tingling? Am I that yellow?"

    "And blue."

    "Oh. Thank you so much."

    "And dying."

    "Am I?"

    "Please do."

    "I'm happy because I'm finally able to give you something you want."

    "You are?"

    "If I die."

    "Oh. I might write a song about you."

    "Would you do that?"

    "I promise."

    "Okay."

    "Okay."

    #sfx knock

    "Oh. No."

    #knock

    "Someone's at the door."

    "Shh. Hurry and die."

    "I'm doing my best."

    "You're not sad?"

    "No, should I be?"

    "No. But I want want you to know something."

    #knock harder

    "I..."

    

    menu:
        "I forgive you":
            s "I can't ask for it in return."
            s "But... I forgive you."
            un "... dammit. Why are you making this so hard?"
            un "Why couldn't you just die?"
            # sfx knock
            pause 1.5
            # sfx door opening
            l "Oh god. Elsa, they're in here!"
            $cassBio.stringSever()

        "I can't forgive you":
            s "I know you put something else in the needle."
            s "I'm not... stupid."
            un "... why didn't you stop me?"
            un "Why couldn't you just die?"
            # sfx knock
            pause 1.5
            s "... I deserve to die."
            # sfx door opening
            l "Oh god. Elsa, they're in here!"

    stop music fadeout 5.0
    jump robinDate2
    return