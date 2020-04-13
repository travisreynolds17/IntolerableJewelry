label endingRobin:
    if robinSever == False:
        # in which Robin appears in the restaurant and cuts David's throat. Then her body falls down.
        #heartbeat sound
        d "Sophie?"

        scene bg resta
        show d

        #heartbeat
        s "David?"

        # sound effect of lights shutting off
        play sound "sounds/Lights Out.mp3" 
        scene bg black

        s "OH!"

        pause 1.0

        scene bg resta
        #show dying robin stabbing david

        # sound effect of lights shutting off
        play sound "sounds/Lights Out.mp3" 
        scene bg black

        scene bg resta
        #show dying robin

        r "... I found... found you. P-papillon."

        r "I..."

        r "... finally..."

        

        #show robin dropping dead

        scene bg black

        s "DAVID!!"

        jump endCredits

    else:
        #in which Robin finds Sophie, asks David to give them time, and tells her things. So, the nature of the rewrite means this has got to be mostly in Sophie's head. or at least positioned as such. IRL Louisa is gone, and David would recognize her even if Sophie called her Robin.

        un "... reservation. I am here to see someone."

        un "Excuse me."

        "That voice?"

        show r at right with dissolve

        r "Papillon!"

        s "Robin!"

        "She looms over the table and my god, she seems taller somehow in person."

        show happy at right

        r "At last. I am so, so happy to finally meet you in person."

        d "Who's your lovely friend?"

        "I... actually forgot for a moment that he was there."

        s "Sorry, sorry. David, meet Robin. Robin, David."

        "He stands, offering his hand, and she does not take it."

        r "Forgive me, David. Would you do me the kindness of giving us some time alone?"

        "He looks at me for confirmation and I answer with a slight nod."

        "I'm sorry, David."

        d "Anything for a lady. Sophie, I'll call you tomorrow, kay?"

        s "Sure. Thank you."

        hide d with dissolve

        show r with dissolve

        pause 0.5

        s "So..."

        r "I meant to find you sooner."

        show r sad 

        r "In fact, I wouldn't have been able to had Tania not lent assistance."

        s "How did you know I would be here?"

        r "I didn't, love. It seems one of a few places you frequent since the collapse, though, and I suppose fortune favored me."

        "That sounds a lot like she was shadowing me, but I'll let it slide for now."

        "She sits across from me, shoos away a server with a wave of her hand."

        "Almost every eye in the place is on her, which seems vexing to her."

        r "Have you been well?"

        s "My whole world imploded."

        r "These things happen."

        "She's so casual about it."

        s "Oh yeah? Creepy computer ghost things happen, do they?"

        r "Yes. Among other things, draga mea."

        s "Things?"

        r "I entered the simulation willingly, papillon."

        s "What? Why and how?"

        r "Oblivion is an otherworldly thing, my dearest. It is not unique."

        s "You're screwing with me, right?"

        r "I find your incredulity disheartening, darling. Do you suppose a single instance of rationality-breaking oddity exists, then?"

        s "So there's more of them. More like Liv."

        r "Like it, yes, but not exactly like it."

        "She reaches down, then, and lifts the hem of her blouse to reveal a complex tattoo encircling her belly button."

        "It... glitters?"

        "The watching eyes peer closer."

        r "I am one of them, my love."

        s "What."

        "I feel like all I can do is react, at this point. Even then, it is flat. I am a boxer being rabbit punched after the bell."

        r "I went to that place to hunt Liv and add its name to my own horde."

        show image splashEKGFull at summonEKG
        pause 0.3

        "I'm shaking. It's too much."

        r "You must have felt it the first time we met."

        hide image splashEKGFull at summonEKG

        s "..."

        r "In Paris."

        s "So it WAS you."

        r "I'm surprised you didn't react more viscerally in the simulation."

        s "... do you hate me?"

        pause 0.5

        r "... no."

        pause 0.5

        s "Robin, I--"

        r "Don't apologize for Paris."

        s "But-"

        r "You must understand. I chose to be in that place. As poor of a decision as it may have been, it was mine."

        r "The consequences were mine."

        r "Still, you provided safety and comfort on a night that might have ended terribly, as so many others did."

        s "Robin."

        r "Papillon?"

        show image splashEKGFull at summonEKG
        pause 0.3

        s "I thought you drowned."

        r "Drowned?"

        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        s "You don't have to tell me about it. I'm just... I'm happy to see you're okay now."

        r "Ah, I see. In the simulation, you mean."

        pause 0.4

        r "I thought I could wrest control away from Liv. In this world, perhaps I could have."

        r "In the simulation, I could not touch it."

        pause 0.5

        r "We have so much to discuss, Sophie. So very, very much."

        s "I have time. Where are you staying?"

        r "Tania rented a house for me just outside the city. She needn't have paid, but she insisted."

        r "I imagine you've learned her true nature by now. Her reach is... vast."

        s "No kidding."

        pause 0.5

        r "Did the sight of her bother you?"

        s "Yes. You?"

        pause 0.5

        r "Enormously."

        "We both laugh at that, not because it's funny but out of some small bit of shared trauma."


        pause 0.5

        show r sad

        pause 0.2

        s "What do we do now, though?"

        r "I would expect your role in all this must be over. I intend to tell Cassandra and Lichelle the same."

        s "It's kind of hard to just forget what happened."

        r "Try, nonetheless."

        s "What about you?"

        r "Tania and I have an accord. There are other Oblivions gnawing at the roots of this world. The technological is her domain as the metaphysical is mine."

        s "Robin."

        r "Dear?"

        s "What does that even mean?"

        "She sighs, softly, musically, and lifts her hem again."

        "The tattoos are gone."

        s "Wait, what?"

        "And like that, her hand falls upon mine. Only for a moment."

        r "You've glimpsed an aspect of this existence most people cannot even comprehend, papillon."

        r "Your strength inspires me."

        "She stands, enormous, once again."

        r "While I'm staying in this country, would you join me for dinner from time to time?"

        r "I would relish an opportunity to cook for you again."

        s "You're going to drop a dozen mysteries in my lap and just vanish?"

        r "I believe Tania told you I was a 'spooky bitch' so it seems in character, wouldn't you say?"

        s "Maybe."

        if loveRobin == 5:
            "She's leaving."

            "Just like that."

            s "Robin!"

            "She turns so quickly I'm instantly convinced she wanted me to stop her."

            r "Draga mea?"

            s "You're not leaving without me."

            r "Oh?"

            s "Yeah. You gotta show me how you did the tattoo trick."

            r "A magician holds her secrets close to her chest, love."

            s "Then fucking hold me there, too."

            "Oh my god."

            "She's actually blushing."

            r "You're still under the compounding effect from the simulation, then?"

            s "I don't know."

            r "Your feelings may not be real, love."

            s "Reality's just perception, right?"

            r "I suppose."

            s "Then I know what I feel is real."

            r "And what do you feel, exactly?"

            "I've made my way across the restaurant and to her side."

            "All eyes are upon both of us, now."

            s "I just want to be near you. I want to be near you."

            show r happy

            r "Oh?"

            s "Yeah. Yeah, so just don't make a big deal out of it."

            r "And here I believed I was the one searching for you this entire time."

            r "Do you care for me?"

            s "I'm not sure. I'm not sure exactly what I feel for you. I just..."

            s "If I don't follow you, I know I'll regret it."

            r "Let's go, then."

            s "Where?"

            hide image splashEKGFull at summonEKG
            show image splashEKGFull at summonEKG
            pause 0.3

            r "Does it matter?"

            s "No."

            "And so, I traded my soul to the Romanian witch with the endless legs and poisonous smile."
        else:
            r "I will speak with you soon, papillon. Enjoy this new lease on your life."

            #back to endingtron. I think that might be all of the mnis?