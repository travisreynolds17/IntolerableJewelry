label endingRobin:

    scene bg black with fade

    show m 1a at fr12

    m "Shall we, madam?"

    s "I suppose. I'm not sure I'm into surprises right now."

    m "We're far past that, ma'am."

    s "... true. Lead on."

    hide m at fr12

    scene bg bar with fade 

    s "I'm more than a little unsettled by how similar this room looks to the meet-cute parlor from the simulation."

    m "I am unable to comment on that, ma'am, having not seen such a parlor."

    s "Right."

    show d 1m at f12 

    d "Hey, Sophie! This place is amazing, it turns out."

    "David's face seems a touch redder than usual. A TV in the corner blares with football sounds and commentary."

    s "It looks like just the place for you."

    d 1j "Yeah, I know you never liked football. There's also booze and robots."

    s "Fair."

    d 1a "So, you all done?"

    s "Tania said somebody else was coming here. She didn't say who."

    d 1r "Huh. That's kind of ominous."

    s "I'll say."

    show m 1a at fl11

    m "Here is your drink ma'am!"

    s "Oh. Uh, what is it?"

    m "Cranberry juice as you prefer."

    #glitch?

    s "Ah. Thank you, Mortimer! You're a good man bot."

    hide m at fl11

    d "Cranberry, eh?"

    "The juice tastes full, robust, and lightly sweet. There's a tingle to the aftertaste, the kind of afterburn unique to real fruit juice."

    if robinSever == False:
        # in which Robin appears in the restaurant and cuts David's throat. Then her body falls down.
        # SFX
        show image splashEKGFull at summonEKG
        pause 0.3
        d 1h "Sophie?"

        

        show image splashEKGFull at summonEKG
        pause 0.3
        s "What?"

        # sound effect of lights shutting off
        play sound "sounds/Lights Out.mp3"
        scene bg black

        s "OH!"

        pause 1.0

        scene bg bar
        # show dying robin stabbing david

        play sound "sounds/Lights Out.mp3"
        scene bg black

        scene bg bar
        # show dying robin

        r "... I found... found you. P-papillon."

        r "I..."

        r "... finally..."

        # show robin dropping dead

        scene bg black

        s "DAVID!!"

        jump endCredits

    else:
        # in which Robin finds Sophie, asks David to give them time, and tells her things. So, the nature of the rewrite means this has got to be mostly in Sophie's head. or at least positioned as such. IRL Louisa is gone, and David would recognize her even if Sophie called her Robin.

        un "... I am here to see someone."

        un "Excuse me."

        "That voice?"

        show r 1a at fr13
        show d 1i

        r "Papillon!"

        s "Robin!"

        d "JESUS CHRIST!"

        show d 1h at mt1

        "She looms over the table and my god, she seems taller somehow in person."

        r 1m "At last. I am so, so happy to finally meet you face to face."

        #glitch?

        d 1m "Who's your lovely friend?"

        "I... actually forgot for a moment that he was there."

        s "Sorry, sorry. David, meet Robin Godfrey. Robin, this David Ellison, my boyf-."

        d 1b "..."

        s "Sorry. My friend."

        "I'm sorry, David. It just came out."

        show d 1a at mt2

        show r 1b

        "He stands, offering his hand, and she does not take it."

        r "Forgive me, David. Would you do me the kindness of giving us some time alone?"

        "He looks at me for confirmation and I answer with a slight nod."

        "I'm sorry, David."

        d 1m "Anything for a lady. Sophie, I'll be around, I guess."

        show r 1q

        s "Sure. Thank you."

        show d 1a

        d "Hey robot! Where else can I go in this place?"

        show m 1a at fl11

        m "Come with me, sir, I believe a man of your caliber could appreciate the feel and fit of a brand new suit."

        d 1r "A... suit?"

        m "TO THE WARDROBE!"

        hide m at fl11

        pause 0.5

        d "Huh."

        pause 1.0 

        d 1m "TO THE WARDROBE!"

        hide d at fl12

        show r 1m at mt2

        pause 0.5

        r "What a lovely man."

        s "He's been too good to me. Don't get me wrong, he's got his issues, but..."

        r "He loves you, darling."

        s "... yeah."

        r 1a "But you do not love him in return."

        s "I do, but not... ugh. Not like that."

        pause 1.0

        r "..."

        s "..."

        $renpy.notify("Why didn't he recognize her?")

        r 1m "I meant to find you sooner."

        r "In fact, I wouldn't have been able to had Tania not lent assistance."

        s "How did you know I would be here?"

        r 1l "I didn't, love."

        "That sounds like Tania's been busy."

        #glitch
        "Something feels wrong about this."

        "I can't... can't quite understand."

        "She sits across from me, shoos away a robot server with a wave of her hand."

        "Her elegance almost glows. How can she look the way she does outside the simulation? Not a mark, not a blemish. Not a hair out of place."

        r 1p "Have you been well?"

        s "My whole world imploded."

        r 1j "These things happen."

        "She's so casual about it."

        s "Oh yeah? Creepy computer ghost things happen, do they?"

        r 1a "Yes. Among other things, draga mea."

        s "Things?"

        #glitch

        r 2l "I entered the simulation willingly, papillon."

        s "What? Why and how?"

        r 2o "Fontaine is an otherworldly thing, my dearest. It is not unique."

        show r 2a

        s "You're screwing with me, right?"

        r 2g "I find your incredulity disheartening, darling. Do you suppose a single instance of rationality-and-dimension-breaking intelligence exists, then?"

        s "So there's more of them. More like Fontaine."

        "I knew it."

        r 1k "They are like it, yes, but not exactly like it."

        "She reaches down, then, and rolls back her sleeve."

        "It... glitters?"

        "There are marks. Dozens of them, gleaming, neon."

        r 1b "I am one of them, my love."

        s "What."

        "I feel like all I can do is react, at this point. Even then, it is flat. I am a boxer being rabbit punched after the bell."

        r 1l "I went to that place to hunt Fontaine and add its name to my own horde."

        show image splashEKGFull at summonEKG
        pause 0.3

        "I'm shaking. It's too much."

        r "You must have felt it the first time we met."

        hide image splashEKGFull at summonEKG

        s "..."

        r 1p "In Paris."

        s "So it WAS you."

        r 1q "I'm surprised you didn't react more viscerally in the simulation."

        s "... do you hate me?"

        pause 0.5

        r 1b "... no."

        pause 0.5

        s "Robin, I--"

        r 2m "Don't apologize for Paris."

        s "But-"

        r "You must understand. I chose to be in that place. As poor of a decision as it may have been, it was mine."

        r 2g "The consequences were mine."

        r 2a "Still, you provided safety and comfort on a night that might have ended terribly, as so many others did."

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

        #glitch
        s "What? No. I mean... yes, I guess that's where it happened."

        s "My memory isn't... isn't what it used to be."
        pause 0.4

        "That's right."

        r 1a "I thought I could wrest control away from Fontaine. In this world, perhaps I could have."

        r 1k "In the simulation, I was overpowered."

        pause 0.5

        r "We have so much to discuss, Kylie. So very, very much."

        s "I have time. Where are you staying?"

        $renpy.notify("What? Who? Louisa, what are you saying?")

        r 1n "Tania rented a house for me just outside the city. She needn't have paid, but she is such a sweet creature to insist."

        r 1m "I imagine you've learned her true nature by now. Her reach is... vast."

        s "No kidding."

        pause 0.5

        r "Did the sight of her bother you?"

        s "Yes. You?"

        pause 0.5

        r 1q "Enormously."

        "We both laugh at that, not because it's funny but out of some small bit of shared trauma."

        pause 0.5

        show r 1b

        pause 0.2

        s "What do we do now, though?"

        r "I would expect your role in all this must be over."

        s "It's kind of hard to just forget what happened."

        r 1s "Try, nonetheless."

        s "What about you?"

        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        r 1m "I am standing here, somehow."

        s "Robin."

        r 1r "Dear?"

        s "What does that even mean?"

        "She sighs, softly, musically, and lifts her sleeve again."

        "The tattoos are gone."

        "Only scars remain."

        s "Wait, what?"

        "And like that, her hand falls upon mine. Only for a moment."

        r 1b "You've glimpsed an aspect of this existence most people cannot even comprehend, papillon."

        #glitch

        pause 0.5

        s "... Louisa?"

        r 1m "Your strength inspires me."

        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        "She stands, enormous, once again."

        r "While I'm staying in this country, would you join me for dinner from time to time?"

        s "Why... who are you?"

        r 1n "I would relish an opportunity to cook for you again."

        s "You're not... not going to tell me?"

        r 1b "I believe Tania told you I was a 'spooky bitch' so it seems in character, wouldn't you say?"

        #glitch 
        s "Maybe."

        hide r at f12

        "She's leaving."

        "Just like that."

        s "Robin!"

        show r 1r at f12

        "She turns so quickly I'm instantly convinced she wanted me to stop her."

        r "Draga mea?"

        s "You're not leaving without me."

        r 1a "Oh?"

        s "Yeah. You gotta show me how you did the tattoo trick."

        pause 0.5

        r 1j "A magician holds her secrets close to her chest, love."

        s "Then hold me there, too."

        show r 1h

        "Oh my god."

        "She's actually blushing."

        r "You're still under the compounding effect from the simulation, then?"

        s "I don't know."

        r 1b "Your feelings may not be real, love."

        s "Reality's just perception, right?"

        r "I suppose."

        s "Then I know what I feel is real."

        r "And what do you feel, exactly?"

        "I've made my way to her side."

        "I can see Mortimer and David in the doorway, dressed in matching suits."

        "He's smiling. He's happy for me, isn't he."

        s "I just want to be near you. I want to be near you."

        show r 1n 

        r "Sophie..."

        s "Yeah. Yeah, so just don't make a big deal out of it."

        r 1u "And here I believed I was the one searching for you this entire time."

        r "Do you truly care for me?"

        s "I'm not sure. I'm not sure exactly what I feel for you. I just..."

        s "If I don't follow you, I know I'll regret it."

        r 1m "Let's go, then."

        s "Where?"

        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        r "Does it matter?"

        s "You can't actually be here."

        #glitch

        s "You're dead."

        r "Yes."

        s "You drowned. In the fountain."

        r 1c "Yes."

        s "Who are you?"

        pause 0.5

        r 1b "Does it matter?"

        #glitch

        $renpy.notify("It matters!")

        s "No."

        "And so, I traded my soul to the Romanian witch with the icy eyes, endless legs and poisonous smile."

        "And I never looked back."

        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 0.3

        show bg black with fade

        show window

        un "She looks so peaceful."
        un "I guess it's time, isn't it."
        un "Elsa. David. You don't have to stay."
        un "I'll stay. I can't... I can't leave her."
        un "Me, too. I owe her that much. Thank you, Dr. Fontaine."
        o "I am truly sorry."
        o "Goodbye, Ms. Koenig."

        hide image splashEKGFull at summonEKG
        show image splashEKGFull at summonEKG
        pause 2.3

        nvl clear

        o "Time of death [hour]:[minute] on [day], [month] [dom]."

        nvl clear

        d "I love you Soph. I'm... I'll always love you."

        jump endcredits
    
        return
