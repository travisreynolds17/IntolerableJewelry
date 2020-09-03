label endingKylie:
    "My vision."

    "Was it ever really mine?"

    scene bg black with fade

    d "Doc. DOC! She's awake!"

    "I know that voice."

    e "Sophie? Hey girl! You..."

    "Something's muffled. Who's crying?"

    d "... scared us all to death."

    "Fizz? Elsa?"

    "My senses are putty, squashed together in an incoherent ball."

    "Suddenly, there are scrubs everywhere."

    "Then..."
    play audio beep noloop
    hide image splashEKGFull at summonEKG
    show image splashEKGFull at summonEKG
    pause 0.3

    scene bg black with fade
    pause 0.5
    scene bg hospital with fade

    play music hallwayChats

    show d 1a at f11

    d "... and Elle called the ambulance. Then she called Elsa, then me."

    show e 1a at f13

    e "You owe a helluva debt to Lichelle."

    "I do."

    s "Tania. I liked you better as a redhead."

    e 1p "Huh?"

    pause 0.1

    "... oh. That's right."

    s "Am I gonna be arrested?"

    d 1q "For what?"

    s "For giving the heroi-"

    e 1q "FOR DOING nothing like that, ha ha."

    pause 0.1

    "Right. Public."

    d 1g "It's no joke this time, Soph. You screw up again, you're going to prison."

    pause 0.1

    "Don't want that."

    e 1j "Believe me sweety, you're too cute for that. You'll get mauled in there."

    "Don't want that, either."

    s "... where's Louisa."

    d 1b "..."

    e 1h "..."

    e "Sweety. Do you know where you are?"

    s "Y-yeah. I'm..."

    # fontaine shows up in a lab coat
    # SFX - Knock
    pause 1.0

    show f 2m at f12

    stop music fadeout 4.0

    o "Sorry to interrupt."

    d 1a "Oh, uh, hey doc."

    show e 1j

    pause 0.2

    e "Try not to trip over your tongue, David."

    "..."

    o 2a  "Hello again, David. Let's have a little look at Sophie now that she's up and about, hey?"

    s "n-n-no."

    play music onTheNod

    e 1b "Sophie?"

    show d 1b

    s "Get away from me!"

    show f 2b

    o "It's okay, Sophie. I'm here to help."

    s "NO!"

    d 1s "What's gotten into you?"

    "I want to kick, to thrash, to scream."

    "I have no energy. Tubes sink into my arms."

    d 1b "Dr. Fontaine has been wonderful to you, and to us."

    show d 1b

    s "She's a monster. She's evil!"

    e 1j "She's single, so David might have a biased perspective."

    show f 2q

    d 1b "Shush."

    show d 1b

    s "That's her. That's Fontaine! She killed Robin. {i}She{/i} did it!"

    e 1b "Who's Robin?"

    o 2i "Um, my name is Robin."

    d 1j "You look awfully alive to me."

    pause 0.5

    show e 1k

    pause 0.5

    o 2m "Thank you, David."

    o 2r "I think?"

    s "David, don't talk to her. She'll... she'll kill you, too!"
    show f 2b
    show d 1b
    show e 1b

    d "Sophie..."

    s "She did it. Fontaine drowned Robin! I saw her body!"

    s "I saw her!"

    pause 0.2

    o 2g "It's not unheard of for dissociative patients to hear what's said around them."

    s "No, no no. Her name is Fontaine L'eau! It's a trap. {i}Help! Help me!{/i}"

    e 1h "..."

    e 1b "I get it now."

    e "Honey. Please calm down."

    o 2b "I should go. Sophie, I only want to help you."

    s "NO! BITCH! MURDERER!"

    o 2a "Ms. Langford. I'll ask the nursing staff to check up on Sophie shortly. We'll need to run a few tests now that she's awake."

    e 1m "Anything, doctor."

    o "David."

    d 1b "Ma'am?"

    o 2a "May I speak with you privately?"

    d 1k "Anything you need."

    o "Thank you."

    pause 0.1

    o 2b "Sophie, I'm not sure what you think I've done to you but I hope I can erase that perception in time."

    s "stay away, please stay away, please, please-"

    o 2a "I'm going. David, if you please?"

    d 1a "Sure."

    hide f at fr12

    d 1a "Be back soon."

    e 1a "Hey."

    d "Yeah?"

    e 1t "I think she likes you, buddy."

    d 1b "You think?"

    e "Yeah. Don't keep her waiting."

    d 1b "Of course. I'll be back soon."

    hide d at fr11

    e 1u "Not too soon, I hope."

    s "..."

    e 1a "Sophie."

    e 1m "She's your doctor. I've known that lady for a decade. She's normal. Fusses over her hair. Farts when she thinks nobody's paying attention."

    s "... she's horrible. You have to kill her."

    e 1k "For farting? Honey."

    s "She's evil. You have to believe me."

    s "I don't know how she got out of the simulation."

    e 1b "Sophie."

    s "She killed a million people!"

    e "..."

    s "..."
    pause 1.0
    e 1c "Listen to yourself."

    s "..."

    e 1b "Doctor Fontaine cares about you."

    e "I care about you."

    e 1c "Sophie, I -"

    show e 1h

    s "Where's Louisa?"

    pause 0.5

    e 1b "She's gone, honey."

    s "Where."

    e 1a "Hey. Listen. I'll make you a deal."

    s "Deal."

    e 1m "If you just close your eyes and rest, and get better, I promise we'll talk about it."

    s "..."

    show e 1h

    s "She'll kill him. She'll kill David. I saw her. In there. She's a monster."

    e "..."

    e 1b "Just rest. Okay?"

    e "I'm going to go get a soda. And breathe."

    "Her hand slides from mine."

    "I didn't realize it was there."

    "Elsa? Why are you crying?"

    hide e at fr13

    s "... Elsa?"

    s "..."

    stop music fadeout 5.0

    s "Chat's not working."

    "..."

    scene bg black with fade
    pause 0.5
    scene bg hospital with fade

    pause 0.5

    

    if entityForgiven == True:
        # show f
        show f 2q  at fr12
        o "Sophie."

        play music ringRejection

        s "... get out."

        o "You forgave me."

        "There are tears in her eyes. Her breath is quick, her lips trembling."

        o 2b "I was the worst. A monster, truly. A liar. But in there, you forgave me."

        o "Kylie did, anyway."

        s "I knew it."

        o "I've earned your scorn."

        o 2q "But out here, I am doing everything I can to make up for it."

        s "Where's David?"

        o "Resting. He's a beautiful man, Sophie."

        s "Did you..."

        o 2a "I accepted his invitation to dinner, yes."

        s "That's it?"

        o "I want to be better out here. I don't want to just give people pleasures they want, knowing they can't handle them."

        s "..."

        o 2m "He's a good man. He cares about you, and so do I."

        o "So... I hope you're not angry with me for that, at least."

        s "... I can't trust you."

        o 2b "You shouldn't. I deserve that."

        s "I'll kill you myself."

        o "I deserve that, too."

        o 2a "You did everything you could have done to make everything right, Sophie."

        o 2m "Even knowing none of this is real, you put your heart into being a good person."

        o 2n "I love you, Kylie."

        s "... don't call me that."

        o 2q "Why not? It's your name. One of them, anyway."

        s "... am I real?"

        o 2m "As real as anything else, yes."

        show e 1m at fr13

        show f 2h

        e "Hey doc. Where's David?"

        o "Uh, resting."

        e 1j "..."

        o 2q "..."

        e "That was fast."

        o "He asked me out."

        e 1m "Ah."

        o 2i "I didn't do anything."

        e 1n "Ah."

        o 2q "Shush."
        stop music fadeout 4.0
        nvl clear
        nvl show

        "Is it an act?"
        "Elsa trusts her."
        "Am I wrong? Was I ever right?"
        "If... she existed in the simulation, were any of her crimes real?"
        "Do they matter?"
        nvl hide
        nvl clear

        play music bedroom
        s "... I forgive you."

        e "huh?"

        o 2m "I'll earn that for the rest of my life, my Kylie."

        e 1r "I'm confused."

        s "I can't call you Robin. I can't."

        pause 0.4

        o 2b "I know."

        o "I'll have the nursing staff check in on you later, then."

        s "Thanks, Fontaine."

        o 2n "Anytime, love."

        show f at justFade

        "Elsa's looking between us as Fontaine leaves, confusion written on her face."

        show e 1j at mt2

        e 1j "So... besties already?"

        s "I guess."

        nvl show

        "Fontaine's smile retains a shade of sadness. I believe her. I think."

        "She is the entity from the simulation."

        "Alternatively, I talk in my sleep."

        "Alternatively alternatively, the jewelry..."

        "... the heroin."

        "It doesn't matter."

        "It really doesn't."

        "Things will be different this time."

        nvl hide
        nvl clear

        s "Elsa."

        e "Hm."

        s "I'll never touch that stuff again."

        e 1m "Hon..."

        s "I promise. I'll... I'm swearing off. Forever."

        

        show e 1b

        stop music fadeout 7.0

        "I promise."

        k "I'm a whole new woman."

        "I promise."

        scene bg black with fade
        $chat.delmessages()
        pause 3.0

        show screen chatterbox
        pause 0.5

        $chat.addmessage(bong, "lol b00bs lol")

        pause 1.0

        
        
        $chat.addmessage(unkn,"Oh. You're still here, too. ;)")

        pause 1.0
        
        
        python:
            newComments = [
                [bar,"Me, too."],
                [egg,"Yup."],
                [crab,"Where are we?"],
                [shub,"hell"],
                [cake, "no"],
                [beav, "... Fontaine?"]
            ]
        
            chat.bulkMessage(newComments, 0.7)

        
        
        $chat.addmessage(fon,"Don't worry.")
        pause 1.0
        
        
        $chat.addmessage(fon,"We'll take very, very good care of you boys.")

        pause 4.5

        "End: Tandem Rebirth"

        jump endCredits

    else:
        show e 1a at fr12
        e "Hey girl. Sorry to dip out like that."

        s "..."

        e "Dr. Fontaine said she'll postpone the tests until later. She's got David in her office now."

        s "..."

        e 1m "Don't let that bother you. David loves you, no matter what."

        s "... he wanted to marry me."

        e 1a "He did."

        s "I messed that up."

        e 1b "Sophie. You have a disease. A real one."

        s "Nobody ever cooked and shot cancer into their own arm."

        e 1g "Maybe not. I don't mean you shouldn't take personal responsibility. I just mean some aspect of this was always out of your control."

        s "..."

        e 1b "If it means anything, you're young. You have time. Your body is resilient."

        e 1m "Now that it's court-ordered, I'm pretty sure we can kick this heroin thing together."

        s "... I don't know if I can."

        e 1a "Whether you think you can or you can't, you're right."

        s "Did you get that from a self-help book?"

        e "Yoga instructor."

        s "Oh."

        pause 0.5

        e 1b "Sophie."

        s "Hm."

        e "Louisa had a long history of some really bad stuff."

        s "I know."

        e "I don't think you do."

        pause 1.0

        s "... maybe not."

        e 1g "She was a complicated woman. Fierce. Driven."

        s "Yeah."

        e "She had demons you and I can't begin to fathom."

        e 1b "Awful things, Sophie."

        s "Yeah."

        s "... I loved her."

        e 1c "She loved you, hon. She wouldn't shut up about you."

        s "I never deserved her."

        e "Nobody deserves anything. You get what you earn, no matter what."

        e 1a "I'll help you. Okay? We'll get your gaming channel going again, if you want."

        s "... I'd like that."

        e "For now, just rest."

        e "You've earned it."

        pause 1.0

        s "One... one last thing?"

        e 1q "Anything."

        s "Could you call me by my real name?"

        e 1i "Huh?"

        pause 0.1

        s "My name is Kylie."

        k "Is... is that okay?"

        show e 1n

        pause 0.5

        e "I understand. A whole new you, eh?"

        k "Something like that."

        e 1m "Okay, Kylie. I think I can do that."

        # SFX: Running?

        show e 1s

        k "What's all that noise?"

        play music fountainWater

        e 1s "A bunch of nurses just ran by."

        k "..."

        e 1m "Never a dull moment in a hospital, I suppose."

        k "I guess."

        scene bg black with fade

        pause 3.0
        $chat.delmessages()
        show screen chatterbox
        pause 0.5 
        
        $chat.addmessage(unkn,"...")

        pause 2.5

        $chat.addmessage(fizz, "*screams*")

        pause 4.5

        "End: Dr. L'eau, Amateur Surgeon"
        hide chatterbox

        pause 5.0
        stop music fadeout 6.0
        jump endCredits

        return
