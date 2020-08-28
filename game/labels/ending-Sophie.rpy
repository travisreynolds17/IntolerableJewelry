label endingSophie:
    scene bg resta with fade

    play music jazzNoodle

    d "Sophie? Hey, you okay?"

    s "..."

    s "Hm? Oh. I'm sorry, I... must've went away for a while."

    "Across the restaurant, the pianist's fingers dance beautifully across ebony and ivory."

    "For a moment her eyes land on us, but only for a moment."

    show d 1a at f12

    d "I worry about you."

    "He does. It's probably why he agreed to meet me here at all."

    d 1q "I gotta tell you, it surprised me when you called me up and asked to meet here."
    
    d "Of all places."

    s "Yeah. I just needed to figure some things out."

    d 1a "Like what?"

    s "I... don't know what's real anymore, David."

    d 1g "Wait what? I thought you were gonna apologize or for throwing me out of your hospital room or something."

    s "That, that, too. Yes. I'm sorry for that, I am. But that's not what I wanted to talk about."

    s "David. Are you real?"

    pause 0.5

    d 1g "I guess? I don't see why not."

    s "But how do you know?"

    d 1j "I'm made of meat and I piss a lot."

    s "Yeah but what if you're a program designed to do that?"

    d 1k "Seems like a really useless program."

    s "David--"

    d 1g "Sophie. I love you. I did before and I still do, so when I say this I need you to know it comes in good faith."

    pause 0.5

    d 1b "You're not using again, are you?"

    pause 0.4

    s "I'm not. I'm not, I promise. And I'm not crazy."

    d 1g "I didn't say you were crazy. It's just that I've seen these signs before."

    s "I'm clean."

    d "You cut your hair. You've lost weight."

    s "David."

    d 1k "Pull up your sleeves."

    s "I got shocked, that's all. My headset. It burned up some of my hair so I just, I just started over."

    d 1b "That didn't happen, Sophie. Remember?"

    s "... I can't stop shaking."

    d "I can see that. I need to see your arms, Sophie."

    menu:
        d "Pull up your sleeves."

        "Pull them up":
            s "Fine. I get why you wouldn't trust me."
            # show arms with no marks
            d 1q "It isn't that I don't trust YOU. I just know what that garbage does to people."
        "I refuse.":
            s "I shouldn't have to prove anything to you. Or anyone."
            d 1g "..."
            d 1k "I'm not gonna force you. I shoulda known what I signed up for."

    s "I just don't know what's real anymore!"

    d 1a "I'm real."

    "He covers my hand with his own, then."

    "It's colder than I thought it might be."

    "I can't be alone. Not now. Not ever."

    pause 0.1

    show image glitchGui at frameGlitch 
    s "I wonder how the girls are doing."

    pause 0.1

    d 1g "What girls?"
    hide glitchGui

    show image glitchGui at frameGlitch

    s "You know. Robin and the others."
    hide glitchGui

    d 1k "Sophie."

    s "What?"

    d "You know Robin isn't real."
    
    s "I know that. I mean..."

    s "..."

    s "I don't know what I mean."

    pause 0.1

    d 1a "Someday you will."

    pause 0.1

    s "It's just that I didn't recognize anyone else. Their names were there. Cassandra looked like Cassandra."

    d 1b "Sophie."

    s "Why would Louisa look different? Why did she have a different name?"

    d "Maybe it was just your mind trying to protect you. Or work through grief, something like that."

    s "I didn't even recognize {i}you{/i}."






        #--------------------------------------------------------------------
    show d 1k

    d "You've been through a lot. You were already struggling, and then..."

    s "... I know."

    pause 1.0

    d "Are you going to be okay to go to Cassandra's funeral?"

    s "... I don't know."

    #phone sound SFX
    s "OH!"

    pause 0.1

    d 1j "It's your phone."

    s "I know that."

    "..."

    s "It's from Lichelle."

    d "Who?"

    s "Elle. You've met her, she used to be the door guard."

    d 1a "Oh, Elle. Right. Biceps. What's she want?"

    s "To talk."

    s "If you don't mind giving up your seat for a sec."

    show l 1a at fr13

    l "Sophie. You look rough, girl."

    show d 1q

    "David swivels a bit in his chair and provides an easy smile to her."

    show l 1m

    "She returns it, bold and bright."

    s "I feel okay, though."

    l 1j "I don't believe it. David, my guy, do you mind giving me and gamer girl a minute?"

    "He already was on his feet, brushing off his seat for her."

    show d 1a at mt1

    d "Anything for you, lady. You know, I never knew your name was Lichelle."

    "I didn't know they had such a friendly relationship."

    show l 2l at mt2

    l "Yeah, it is, but I'm Elle to you, bitch."

    d 1a "Yes ma'am. You two have fun, I'm gonna go admire the restroom."

    hide d 1a at f11

    "He's chuckling as he walks off, effervescent, easy. How could I have misjudged him so completely?"

    l 1d "Babe. Based on how you're looking right now, I need you to be honest."

    s "I'm not using."

    l 1j "On god?"

    s "On god."

    "She pauses, but her smile returns."

    if loveConfession == "Cassandra":
        s "I never got to tell her. Out here."

        l 1r "Huh?"

        s "That I..."

        show l 1b

        "Lichelle's staring at me. Her jaw is set."

        l "That you what?"

        s "I just... we were close. In the simulation."

        l "The what?"

        s "When we all got trapped in Intolerable Jewelry together."

        "There's a tragedy writing its somber prose across her face as I speak."

        l 1g "David mentioned you might bring that up. Honey."

        "Here it comes."

        l 1d "There's no damn simulation. I don't even play video games and Cassandra sure as hell never streamed any."

        l "If we're gonna do this, you've gotta commit to reality."

        pause 0.1

        s "... it wasn't some fucking delusion."

        show l 1h

        "I wonder if the abruptness of my backbone caught her off guard."

        s "It doesn't matter. The Cassandra I fell in love with is gone either way."

        show l 1b

        pause 0.4

        l "Yeah, well. That means there's no need to worry about it, is there."

        l "I just wanted you to know. No more, no less."

        s "Thank you."

        l "Thank you. Sure thing. Thank you. Shit."

        pause 0.3

        "For a moment, I can feel the earth separating between us."

        show l 1m

        "But then she smiles again, and her poker face is back in place."
    else:
        l "I just wanted you to know. Considering you two were... whatever you were."

        pause 0.3

        s "I know she didn't love me. Or even like me."

        l 1p "Oh yeah?"

        s "Oh come on. We were sleeping together. There's nothing more obvious in the world than a partner who isn't that into it."

        l 1m "Never been a thing for me."

        s "Good for you. I liked her, Elle. I didn't love her."

        l 1b "You didn't love you, either."

        "..."

        s "I guess not."

        l "..."


    l 1j "Look. Sophie."

    "Her smile remains, but the light has dimmed."

    l "I need you to understand something."

    pause 0.3

    l "Louisa died months ago. She been gone long enough it's time we start sorting things out."

    l 1d "She only had eyes for you, god dammit, but she was {i}my{/i} friend."
    
    l "I oughtta smack your damn mouth every day for the rest of your natural life for what you did."

    l 1e "Giving her that trash."

    "Her tone remains friendly, even. I don't protest. She's not wrong."

    pause 0.4

    l 1b "But I won't."

    l "You're not evil. You're sick. Only damn way to do right by Louisa and Cassandra is to get cleaned up and do something with your life."

    l 1j "I've been talking to David for a while, too. I'm making it my personal mission to be up your ass every single day until I'm satisfied you're gonna be all right."
    pause 0.2

    s "... promise?"

    show l 1k

    "It's not much of a joke, but the pressure behind my eyes is enormous. I won't cry in front of her. I won't."

    pause 0.2

    if loveConfession == "Lichelle":
        l 1b "Funny."

        s "... no. I mean, yeah, but... Elle."

        show l 1a

        l "?"

        s "I care about you."

        l 1q "You said what, now?"

        s "It doesn't mean anything to you. I know that."

        s "Wherever I was. Simulation. Dream. Bad trip. Whatever. I spent time with you there."

        l 1d "... woman."

        s "I have no right to ask you for anything."

        l 1a "True."

        pause 1.0 

        s "If you tell me to go to hell, that's okay."

        s "... but let me lean on you. Let me borrow your strength."

        pause 1.0

        l 1b "Death walks behind you, babe. Louisa. Cassandra."

        l 1c "People I cared about are in the damn ground because of you."

        s "... yes."

        pause 1.0

        l "And you wanna tell me you care about me."

        s "I do."

        pause 1.0

        l "... fine."

        l 1m "Something about you drew them close to you. I don't see it. I'ma give you a chance to show me what it is they saw in you."

        l 1b "But if you try to get me to take any of that shit, I'll fuck you up. Deal?"

        pause 1.0

        s "Deal."

    l "C'mon. We have a service to go to."

    s "... yeah."

    scene bg black with longFade

    pause 5.0

    "End: Free from Myself"