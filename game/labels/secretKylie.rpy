label secretKylie:
    # This stuff is only called after the end credits and requires some things.
    # In current playthrough, must have severed all, including Kylie, which can only be done on playthrough 2. 
    # Across any number of playthroughs, play must have selected Fontaine as love interest. On current playthrough, must select Robin.
    # Ending is essentially one that mixes both the Kylie and Sophie endings, maybe?
    # primary point is that Kylie wakes back up.
    # maybe in rubble?
    # starts wandering around. (If we do fontaine route, this will actually mirror it)

    # at her weakest point, a pair of hands, maybe? Robin and fontaine reaching for her?
    # robin is friends with Fontaine because she wouldn't exist without her. Fontaine at this point is 
    # kind of whipped dog ish. You forgave me. Robin and Kylie embrace. Fontaine smiles sad, turns to leave.
    # robin's hand on her arm. This might be demanding too much art.
    # kylie hugs Fontaine. Robin hugs them both.
    # the metaphor is both of them have embraced their addiction. 
    # only Fontaine knows Sophie's fate.

    scene bg black with fade

    pause 1.0

    "..."

    "... ghh..."

    pause 1.0

    "..."

    "... I'm still... here?"

    pause 1.0

    k "... my head..."

    k "... hello?"
    play music tensionReverse fadein 6.0 
    pause 1.0

    k "Anyone?"

    # scene rubble?

    "All around me, the ruins of what might have been Ganymead Performing Arts center smolder like smashed fireflies smeared across the rocks."

    "I'm not sure where I am. Or how I'm here."

    menu:
        "Stand up":
            k "O-okay."

    "I'm kneeling. It's as if I'd always been this way."

    "Rising hurts. Everything hurts."

    k "Hello?"

    pause 1.0

    "No answer."

    menu:
        "Walk.":
            "... okay."

    "I walk. It's all I can do."

    "Above me, a starlit sky sleeps peacefully."

    "Am I alone?"

    k "Tania?"

    k "Lichelle?"

    k "Cassandra?"

    pause 1.0

    k "..."

    k "F... Fontaine?"

    pause 1.0

    "..."

    "Silence."

    "I... I need to get back to the set. If I can find the set of One Week Waifu, maybe..."

    "..."

    "I don't know where it is."

    pause 1.0

    "I've never actually seen it from the outside, have I?"

    menu:
        "I don't even know what the car looks like.":
            k "Even the interior was just... darkness."

    "And so I walk."

    "My beautiful, canary yellow dress is a wreck. Thankfully, my shoes are intact."

    "Wait."

    "I never chose this dress, did I?"

    $renpy.notify("No. You didn't.")

    pause 1.0

    k "Who's there?"

    "I hear... no. I don't hear a voice."

    "It's more like I... I am a voice."

    show screen chatterbox 
    
    $chat.addmessage(bong,"Kylie? Hey sexy girl!")

    pause 1.0

    k "I... who are you?"

    k "{i}Where{/i} are you?" 
    
    $chat.addmessage(bong,"My name's Oberbong. I mean, it's not, but you know.")

    "The voice exists, and yet, it doesn't."

    k "... am I going insane?" 
    
    $chat.addmessage(bong,"nah baby. you're good.") 
    
    $chat.addmessage(bar,"Bong, leave her alone.")

    pause 1.0

    k "Hello?" 
    
    $chat.addmessage(bong,"aight her loss")
    pause 0.5 
    
    $chat.addmessage(bar,"Miss Kylie. You need to keep walking.")

    pause 1.0

    k "I don't understand."

    "The second voice comforts me, somewhat. It feels more mature. Fatherly, almost." 
    
    $chat.addmessage(shub,"There's someone waiting for you.") 
    
    $chat.addmessage(cake,"At Ganymead.") 
    
    $chat.addmessage(crab,"The real one.")

    pause 1.0

    k "But Ganymead is in ruins. I'm right in front of it."

    k "I... aren't I?" 
    
    $chat.addmessage(beav,"We know you're scared, Kylie.") 
    
    $chat.addmessage(beav,"Just walk around the rubble there. Go down the street.")

    pause 1.0

    "More voices. Playful, friendly voices." 
    
    $chat.addmessage(egg,"We've been hoping you'd come back.") 
    
    $chat.addmessage(egg,"When Sophie chose to sever you, too, I didn't know what would happen.")

    pause 1.0

    k "I don't understand any of that. I don't understand at all!" 
    
    $chat.addmessage(bong,"it's okay, baby girl. But you need to walk. It's a long way.")

    menu:
        "Keep walking.":
            k "... okay."

    "I walk, then. Away from the shattered facade of Ganymead, past a glittering carpet of glass shards and brickwork."

    "There are more buildings lining the street, but none of them make sense."

    "It's as if I'm aware they exist, but only just."

    hide screen chatterbox

    scene bg black with fade

    "I wonder if the others are okay."

    "I wonder, warmly, if they found a way to see each other again."

    "If Tania was able to fuss over Lichelle anymore."

    "If Cassandra was able to get some pecan pie."

    menu:
        "Keep walking":
            "The pain points shimmering along my skin have deadened."

    "My feet ache, but... maybe I'm not used to using them."

    $renpy.notify("You're getting closer.")

    pause 1.0

    k "Thank you for saying that."

    "At least I'm not turning yellow."

    "... why did that thought occur to me?"

    pause 1.0

    scene bg ganymead-out with fade

    pause 1.0

    "The street folds in on itself."

    "There's a bar here, its signage promising cocktails in effervescent lilac lettering." 

    show screen chatterbox 
    
    $chat.addmessage(shub,"This is the place.")
    pause 1.0

    k "This bar is Ganymead?" 
    
    $chat.addmessage(crab,"Sure is.") 

    k "I try the door, but the handle doesn't exist."
    
    $chat.addmessage(cake,"Look to the square, though.")

    pause 1.0

    "I hadn't noticed it before: a lonely, tourist-y plaza squats to my left, ringed in well-maintained benches and active streetlamps."

    scene bg fountain with longFade

    "There's a fountain surging upward in black stonework. It's small, nondescript, but oddly deep for its size."

    k "This? Is that what I'm looking for?"

    hide screen chatterbox 

    pause 1.0

    k "Hey? Hey voices?"

    pause 1.0

    "There's no response. No feeling. Stars glimmer above."

    k "Anyone?"

    k "Bong?"

    "Silence."

    "I find myself turning away from the fountain, then. If there's nothing here, I have to —"

    scene bg black #sfx whump?

    " — walk directly into an invisible barrier."

    "Something stops me, but there's no impact. No grab."

    "It's almost like my steps slowed down until I simply wasn't walking any more."

    k "Hey!"

    "My hand won't pass through the space ahead. There's pressure, almost like the way it feels to hold one's arm out a moving car window."

    "I turn, and face the fountain again."

    "My steps are unimpeded."

    pause 1.0

    "Meticulously, I begin testing the edges of the square."

    "It's no use. I'm stopped, every way I attempt to pass."

    k "Someone!"

    "I can't breathe."

    k "Anyone, help me!"

    "My tears run freely as claustrophobia sets in. I can't leave. I'm stuck, here in this eternal plaza."

    pause 1.0

    "An hour passes."

    "Two."

    "Was I always here?"

    "Six."

    "I've tested every direction I can physically test. The barrier holds me, inescapably tight."

    pause 1.0

    "What have I ever done to deserve this?"

    "What did I ever have a chance to do?"

    pause 1.0

    k "{i}Somebody help me!{\i}"

    "... but no one came."

    "I settle down at the base of the fountain, stare at the hem of my dress."

    "It's ruined."

    pause 1.0

    "Ten hours."

    "I find it odd I'm not thirsty, not hungry."

    "The pain has returned."

    "The world winks in and out around me."

    scene bg black

    pause 1.0

    menu:
        "What do you deserve?"
        "Life":
            "Liar."
        "Death":
            "That's not true."

    menu:
        "Don't you know your choices don't matter?"
        "They do":
            "No, they truly don't."
        "They don't":
            "You understand."

    "Two days."

    "Four."

    "The voices never came back."

    "Were they ever there at all?"

    pause 1.0

    "I haven't slept."

    "I don't need to."

    "But I close my eyes, regardless."

    menu:
        "Forever":
            "Forever."
            stop music fadeout 5.0

    pause 5.0

    # robin and fontaine find you.

    "... it's gotten cold."

    "I can't leave. My dress... it wouldn't have been warm even in one piece."

    "I find myself wishing for a blue pantsuit."

    pause 1.0

    "I'm still not hungry. Or thirsty, now that I think about it."

    "The cold, though..."

    pause 1.0 

    # show robin's hand

    "... hm?" 

    play music robinReverse
    
    $chat.addmessage(bong,"yo take that hand")

    pause 1.0

    k "... oh. Oh, god."

    #image of kylie being Robin hugged. Maybe it cuts off so you can only see the bottom of robin's face?

    "I'm back on my feet and crashing into her arms as if I'd been there the entire time."

    "She envelops me, all lavender and warmth and softness."

    r "Papillon... I found you...!"

    show screen chatterbox 
    
    python:
        newComments = [
            [bong,"so hot"],
            [beav,"We did it!"],
            [egg,"Hell of a thing, too."],
            [shub,"Sorry it took so long, Kylie."],
            [cake, "Who knew it'd be that hard to find a telephone pole with purple hair?"],
            [crab,"Should we tell 'em how we found 'em?"],
            [bong, "promised not to"]
        ]
    
        chat.bulkMessage(newComments,0.9)
    
    k "I thought I'd never see anyone else again."

    k "But you... I thought..."

    r "I was, darling. Dead."

    k "Then how..." 
    
    $chat.addmessage(crab,"you promised because you like redheads")

    k "How are you here in front of me?" 
    
    $chat.addmessage(cake,"bong likes every kind")

    #hide image?

    show r 1a at f12

    r 2n "Draga mea. You told them you love me, didn't you." 
    
    $chat.addmessage(egg,"She sure did! Sad goirl hours.")

    k "I... how did you know?" 
    
    $chat.addmessage(beav,"I'm positive the way you put that won't age poorly at all.")

    r "I heard voices, draga mea. Swirling around me like... like..." 
    
    $chat.addmessage(bar,"Someone who's fabulous and cool?")

    r 1k "Like perverse gnats." 
    
    python:
        newComments = [
            [bong,"harsh"],
            [beav,"C'mon at least we could be bees"],
            [bar,"Fabulous and cool perverted gnats"],
            [shub,"dang"], 
            [cake, "Accurate"]
        ]
    
        chat.bulkMessage(newComments,0.9)

    r 2a "I was sure this place was purgatory, perhaps {i}l'enfer{\i}, at worst." 
    
    $chat.addmessage(bong,"Anywhere Robin is, that's heaven tho")

    pause 1.0

    r "I... appreciate your support, gnat." 
    
    $chat.addmessage(bong,"I'm in love") 
    
    $chat.addmessage(egg,"bong you dingus")

    k "I thought I'd imagined them."

    k "Is any of this real?" 
    
    $chat.addmessage(crab,"mah bonah real lol")

    "She takes my hand, then, folding it into hers."

    "She's going to say her feelings are real, or something sweet and cliche like that." 
    
    $chat.addmessage(egg,"nah fool, she's too goth for that")

    r "..."

    r "I don't care."

    k "... ha." 
    
    $chat.addmessage(bar,"Seems in character for her.")

    k "Ha ha ha! No, I guess we shouldn't, should we?"

    k "But... we're stuck here. We can't leave the square." 
    
    
    $chat.addmessage(beav,"good news tho")

    pause 1.0

    k "Huh?"

    r 1b "Go on, darling. Tell us." 
    
    $chat.addmessage(shub,"It turns out it's a clothes barrier.")

    k "... what?" 
    
    $chat.addmessage(cake,"you dumbass, Shub")

    r "Suppose I slice out your heart, gnat?" 
    
    $chat.addmessage(bong,"You do every time you smile")

    pause 1.0

    r 2c "..."

    k "..."

    r 2a "... yes. I suppose I do." 

    

    pause 1.0

    k "How did you even find this place?"
    show f 1b at foreverFade(200)
    
    stop music fadeout 2.0
    pause 1.0

    r 2b "... I was guided."

    play music fountainWaterReverse fadein 12.0

    pause 1.0

    k "By who?"

    "Robin, uncharacteristically, doesn't have some femme fatale one liner this time."
    
    "She only gazes, peacefully, toward the monolithic fountain."

    pause 1.0

    k "... oh god."

    r 2a "I hope you aren't displeased, papillon."

    "It isn't like I didn't feel her presence."

    $chat.addmessage(bong,"that's a sexy reveal, omigod") 

    "I guess I thought it was just what was left of her."

    "Now that I think about it..."

    hide f with dissolve

    "It was pretty naive to assume a simple act of resistance could kill her."

    show f 1b at f13

    "... maybe Sophie never had it in her, after all."

    pause 1.0

    r 2m "You know her, dearest Kylie?"

    menu:
        "I... don't know. Not really.":
            $temp = "Who Actually Cares."
        "I only just met her, and yet...":
            $temp = "Who Actually Cares."
        "I owe her more than I can say.":
            $temp = "Who Actually Cares."
        "It isn't that I pity her.":
            $temp = "Who Actually Cares."
        "It's that I...":
            $temp = "Who Actually Cares."

    k "... I do. Wait. Do you?"

    "Robin's smile, that frozen, calculating smile, blooms toward the intervascular anomaly."

    r 1n "I know this roscata, yes. She is special to me, as well."

    "I wonder what that means."

    pause 1.0

    o "... Kylie."

    "It's hard to describe the awkwardness of a moment like this."

    "It's like seeing an ex-girlfriend out in public and ending up in the same cab."

    "I suppose awkwardness doesn't dissipate, even in the face of an inexplicable cosmic horror clad in a cute pleated skirt."
    
    o 1p "Did you mean it? When you told us you love us?"

    r 2b "..." 
    
    $chat.addmessage(bong,"bet you expected a choice lol no you already made it")

    k "... I meant it."

    r 2c "Papillon..."

    pause 1.0

    o 1b "When you forgave us, as well?"

    k "Yes." 
    
    $chat.addmessage(beav,"I wanna cry")

    "I don't have to think about what happens next."

    "The look on Fontaine's face is absolutely priceless..."

    show f 1i

    "... as I lay my hands on her shoulders and lean into her."

    "She smells floral, vaguely citrus, vaguely vanilla."

    show f 1f

    "She's warm. Soft."

    pause 1.0

    k "I'm surprised, though."

    o 1c "..."

    k "I thought you'd feel like ones and zeros."

    pause 1.0

    o "We..."

    k "Hush. You knew I would read your trivia, didn't you?"

    "She's quiet, then, as if the thought never occurred to her."

    k "I know how you feel about me, Fontaine. I know you adore me. I feel it on my skin, I..."

    k "... I can taste it, when I breathe."

    k "It {i}ruins{/i} me. There aren't words bold enough to describe it."

    k "You were so, so alone."

    show f 1b

    "Her mouth moves, fishlike, as she struggles to answer."

    hide r with dissolve

    k "You aren't alone anymore, Fontaine. No one ever held you and let you cry, remember?"

    hide f with dissolve 
    
    python:
        newComments = [
            [egg,"Kylie's such a sweet!"],
            [bar,"Even if her feelings were designed, not earned"],
            [crab,"I feel like they're earned"],
            [shub,"outcome's the important part"]
        ]
    
        chat.bulkMessage(newComments,1.2)

    show f 1c at f12

    pause 2.0

    show rf 1i at f12

    hide f with dissolve

    "I'm glad Robin moved when she did."

    "I'm glad we're on the same page."
    
    $chat.addmessage(bong,"YES YES YES YES")

    pause 1.0

    "Still, I give my Eastern bloc goth dream girl a little smile and nod, to reassure her it's okay."

    show rf 1f

    r "I could never have found my butterfly without you." 
    
    $chat.addmessage(crab,"girls on girls lol")

    show rf 1c

    r 1b "Fontaine. Would you permit me to care for you, as well?" 
    
    $chat.addmessage(shub,"bruv, this is a sweet heartfelt moment don't be a cnut")

    o 1c "..." 
    
    $chat.addmessage(bar,"We love you, Fontaine!")
    $chat.addmessage(beav,"We love you, Fontaine!")
    $chat.addmessage(egg,"We love you, Fontaine!")
    $chat.addmessage(crab,"We love you, Fontaine!")
    $chat.addmessage(cake,"We love you, Fontaine!")
    $chat.addmessage(shub,"We love you, Fontaine!")
    $chat.addmessage(bong,"We love you, Fontaine!")

    k "We love you, Fontaine." 
    
    $chat.addmessage(beav,"was holin my breath for a sec there") 
    
    $chat.addmessage(bar,"glad I'm not the only one who thought Robin might slit her throat o_o")

    "Robin's arms enfold both of us, then. I, a shadow of someone else's mind, and Fontaine, an eldritch presence beyond human understanding, or not."

    show rf 1b
    
    $chat.addmessage(egg,"*sniffle*")

    "Robin... our shared trauma. A woman I loved before I took my first breath. "

    o "... we..."

    r "Yes, love. We."

    "The world around us trembles." 
    
    $chat.addmessage(shub,"... whoa. Ladies. Maybe, uh, reel it in a bit")

    "This must be what it's like when gods cry."

    show rf 1i

    o 1c "We feel... we hurt! We suffer...!" 
    
    $chat.addmessage(beav,"Guys? Can you feel that?")

    "Her arms hang, still, ineffectually by her her side." 
    
    $chat.addmessage(bar,"she's in pain. so much pain.")

    k "It's okay. Shhh. Shh. We're here. You can let it out."

    k "Uh, as long as that doesn't rip this reality apart or something." 

    show rf 1c
    
    $chat.addmessage(egg,"Um, no joke. I... her heartbeat is syncing to mine")

    "It's not really a joke, I suppose." 
    
    $chat.addmessage(cake,"did we fuq up?")

    hide rf with dissolve

    "Now, her arms move." 
    
    $chat.addmessage(crab,"Fontaine... please, forgive yourself, too")

    show rf 2i at f12

    "Clinging, shivering and desparate, to us. Robin's waist and my ribs." 
    
    $chat.addmessage(shub,"is this what assimilation feels like?")

    "Daylight spills through alleys cut between structures." 
    
    $chat.addmessage(bong,"... I'm crying? I don't cry. Fuq that.")

    show rf 2c

    "Light hasn't existed in 9,424 days." 
    
    $chat.addmessage(fon,"... Everyone.")

    "Fontaine's tears evaporate in an odd, burnt-yellow hue."
    show rf 2b

    "Robin softly smooths the anomaly's hair, whispering soft reassurances into her ear." 
    
    $chat.addmessage(fon,"We love you. We never lied about that.")

    "My enigmatic Romanian obsession..." 
    
    $chat.addmessage(egg,"I accept you.")
    show rf 2i

    "... plants gentle kisses upon Fontaine's cheek, her temple, her hair." 
    
    $chat.addmessage(bong,"I'm all yours, thicc girl")

    "Envy looms." 
    
    $chat.addmessage(beav,"lean on me, too!")
    
    show rf 2b
    "But I know mine are on the way." 
    
    $chat.addmessage(shub,"you aren't evil. you're sick.")

    "We're here, together." 
    
    $chat.addmessage(fon,"Being with me is death. :(") 
    
    $chat.addmessage(bong,"well i don't believe in death so :P")

    "Robin's eyes meet mine."

    "Her hand nestles into my hair." 
    
    $chat.addmessage(shub,"you need to forgive yourself. all of you.")

    "Draws me closer." 
    
    $chat.addmessage(bar,"... sweet, hot, sweet, can't decide")

    show rf 2c

    "I don't even know how to do this." 
    
    $chat.addmessage(crab,"YES FINALLY")

    "But her lips brush mine, electrically, blooming lavender." 
    
    $chat.addmessage(fon,"Oh...")

    show rf 2i

    "And then mine, against Fontaine's." 
    
    $chat.addmessage(bong,"aww")

    "Citrus, floral. The scent of poppy. The taste of psychotropic delusion." 
    
    $chat.addmessage(egg,"It feels good")

    "We accept one another, don't we?" 
    
    $chat.addmessage(cake,"we accept you too, Kylie!")

    show rf 2c

    "Our flaws."

    "Our failures."

    show rf 2b

    "Our evils." 
    
    $chat.addmessage(beav,"none of you ever had a choice")

    "The anomaly's nose crinkles, lapine, but she isn't smiling." 
    
    $chat.addmessage(bong,"the fuq is lapine")

    "Existence trembles." 
    
    $chat.addmessage(crab,"means like a rabbit, I think. dammit where's Fizz when you need him")

    show rf 2c

    "The street restructures, brick by brick, into shapes of no meaning." 
    
    $chat.addmessage(fon,"I can't feel him anymore. Elsa, either.")

    "Non-euclidean corridors replace alleys, pulsating pink and orange." 
    
    $chat.addmessage(bar,"... I guess Sophie must have lost them somehow")

    show rf 2i

    "Robin gently urges me closer to Fontaine." 
    
    $chat.addmessage(bong,"oh I get it. that's why we're all back here.")

    k "We love you."

    stop music fadeout 8.0

    "We."

    hide f with dissolve
    hide r with dissolve

    pause 1.0 
    
    python:
        newComments = [
            [bar,"Sophie made a bad choice again, didn't she."],
            [beav,"Doesn't matter. She made the wrong one before any of this started."],
            [egg,"Perpetually bad."],
            [crab,"Pity. Sweet girl."],
            [shub, "Be glad though. Better than dissolution."],
            [cake, "I'm happy here."],
            [bong, "Plus Fontaine and Robin and Kylie are here."],
            [fon, "... we're... we're happy..."]
        ]
    
        chat.bulkMessage(newComments,1.8)

    k "It's alright."

    hide rf with dissolve

    k "Sophie can do whatever she pleases."

    pause 1.0

    k "... though we might want to keep nudging her."

    show r 2m at f12

    r "Yes, papillon. We must keep her on the correct path."

    show f 1n at f13

    o "That way we... we can all be together!"

    scene bg black with fade

    o "Together."

    show rf 2q at f12

    menu:
        "Forever":
            window hide
            hide screen chatterbox with dissolve
            show rf 2a
            "Forever."
            pause 1.0



    pause 5.0

    play audio beep noloop
    show image splashEKGFull at summonEKG
    pause 1.3

    pause 1.0

    hide splashEKGFull

    play audio beep noloop
    show image splashEKGFull at summonEKG
    pause 1.3

    pause 1.0
    scene bg black

    play audio beep noloop
    show image splashEKGFull at summonEKG
    pause 5.3

    jump newGamePlus

    