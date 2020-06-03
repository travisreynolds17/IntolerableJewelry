label common4:
    # in which Cass and Robin Dates are done again, but different. Awful. Tearing out Sophie's worst past actions.

    # door sound

    scene bg dressing with fade

    ki "I dreamed of the dark, and I dreamed of a fever-cold, fleeting touch."

    #enable severance
    $severToggle()

    ki "Everything hurts. Maybe it doesn't. Maybe I feel fine and it's just the maelstrom in my heart throwing everything off."

    $chat.addmessage(elsa, "What could you possibly know, Fontaine?")

    ki "Robin's mad monologue echoes against the corners of waking dreams."

    ki "Cassandra is wonderful. She's my idol, someone I've adored from afar for years."

    $chat.addmessage(cake, "Fontaine seems to know a lot of things")

    ki "And yet, my idol is an alcoholic, medicating her agony with liquor."

    pause 0.5

    ki "Somehow, I'm that idol for Robin."

    $chat.addmessage(elsa, "Your fucking name, for one, is not Fontaine. Christ.")

    ki "And Robin, somehow, stalked me from Europe to the United States. Maybe leaving bloodstains in her path."

    # knock knock #SFX

    pause 1.0

    k "Hm? I'm awake."

    $chat.addmessage(fon, "But it is. :) My mother gave it to me.")

    ki "I'm not."

    ki "But, I might as well get up. I'll be going out with Lichelle today and all I can hope for is she's at least close to normal."

    $chat.addmessage(beav, "I always forget hot aggro girls have moms.")

    ki "Anything less than a disaster will be a win."

    # knock #SFX

    k "Coming!"

    $chat.addmessage(elsa, "So tell us all, Fontaine. How am I gonna get Sophie to open her door?")

    ki "I dress quickly in the last set of whites, gather my needs, and head for the door."

    ki "Is b-roll really that urgent?"

    $chat.addmessage(fon, "Private :)")

    scene bg black with fade

    ki "The door opens heavily."

    $chat.addmessage(elsa, "FUCK YOU")

    ki "Oddly heavily."

    $chat.addmessage(fon, "But you bared yourself for me only a moment ago. :) How can you hate me?")

    pause 2.0
    # sound? flash? #SFX

    s "Game? Did you break?"

    $chat.addmessage(beav, "pics lol this is all bullshit")

    $chat.addmessage(elsa, "You're toying with me.")

    s "Guys. Game."

    $chat.addmessage(fon, "No. Private chat. ;)")

    #disable severance
    $severToggle()

    s "Cassandra? You left your choker around my arm."

    $chat.addmessage(elsa, "Fine. David, call me when you get to Sophie's building. If you don't show I will never forgive you.")

    pause 0.5

    $chat.addmessage(fon, "Beaver, here's the pic you wanted ;)")

    pause 1.5

    $chat.addmessage(fon, "Just kidding ;0)")

    pause 0.5

    pause(0.5)
    $hideGui()
    scene bg black with fade
    pause 2.0

    # texting. toPost is a list of messages. each will appear at some random point determined by randomXY function.
    python:
        toPost = [
            "She WHAT?",
            "open up",
            "Someone else.",
            "Ma'am, security shows no attacker.",
            "R/BG13:14-15 Police!",
            "Did you do this?",
            "Toxicology confirms it.",
            "Louisa?",
            "oPen THe godDAmnED DOor",
            "you. it was you.",
            "one. two. BREAK IT!",
            "... I gave her the jewelry.",
            "You're lying.",
            "Door's barricaded!",
            "Sophie, it's me! Open up, please!",
            "Who's voice is that?",
            "Louisa? You're so cold.",
            "I'll lie here with you.",
            "... found them in the bathroom.",
            "Where's Cassandra? Is she okay?",
            "LOUISA!!"
        ]
        postMax = len(toPost)
        i = 0

    while i < postMax:
        $temp = randomXY()

        show text toPost[i]:
            xpos temp[0] ypos temp[1] alpha 0.0 zoom 1
            linear 1.0 alpha 1.0 zoom 5
            linear 0.2 alpha 0 zoom 1
        pause 1.0
        $i += 1

    pause

    show text "... I still love you":
        xpos 0.5 ypos 0.5 alpha 0.0
        easein 2.0 alpha 1.0
    pause
    scene bg THIS IS ALL YOUR FAULT
    pause(0.5)
    $showGui()
    pause 0.5
    # message about love.
    # We must be together
    # because if we're not together
    # then we're taken apart

    pause 2.1

    # suddenly image of drowned Robin on other side of her door.

    s "OH! Oh my god!"

    show l 1m at fl11

    l "Okay Kylie are you..."

    $chat.addmessage(cake, "Damn!")

    show l 1i

    pause 1.0

    l "What... Kylie? What did... what did...?"

    ki "I can't tear my eyes away from the sight before me."

    $chat.addmessage(beav, "whoa that is not okay")

    k "Was... did you do this?"

    ki "Robin, she's... she's, she's she's. She's, she's..."

    s "I don't wanna play anymore"

    show l 1e at right

    l "KYLIE!"

    python:
        temp = reverseString(
            "Silky, silky FontaineeniatnoF tenderly caressing me, every curve, every valley, my skin strobes, my taste buds glimmer, alive with her capacitors, deep within, deep within, freezing drowning dying peace")

        chat.addLinearMessage(elsa, temp, 0, 3)

    ki "Lichelle's voice rips through my horror, grasping at me."

    l "Did you see anything? Hear anything?"

    $chat.addmessage(cake, "can't move much, wouldn't want to if I could")

    k "I didn't, I didn't see anything!"

    ki "She's cold. Her skin, her skin has gone blue. There's a trail of water emanating from down the hall."

    ki "Her hair splays a soaked halo around her face."

    l 1c "Oh my god, oh my god!"

    $chat.addmessage(beav, "it's like life's pressures lifted all at once")

    k "I didn't see! I just opened the door! Look at me, Lichelle!"

    ki "She does, her eyes sparkling, her dark skin somehow pallid."

    $chat.addmessage(sophie, "chat slumbers under the weight of illusory compulsion")

    s "Oh my god."

    ki "Lichelle's against the opposite wall, her chest heaving with sobs that aren't quite there."

    ki "Her hands are on either side of her head. She's just... saying Robin's name over and over."

    $chat.addmessage(fon, "it's okay Lichelle, bring that ass over here ;)")

    ki "Crying out for forgiveness."

    k "We have to call the police."

    $chat.addmessage(beav, "did I call the cops?")

    ki "But my phone is in the room. I wasn't going to take it on the date, and now..."

    l 1b "I'll do it. This... is this my fault?"

    $chat.addmessage(sophie, "chat used 'Call the Police'")

    ki "Lichelle punches against her cell phone keypad and holds the phone, quivering, to her ear, her eyes locked on me."

    show text "911 What is your emergency?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l 1i "I need help, a woman, she's dead. She's been killed."

    $chat.addmessage(sophie, "a miss!")

    show text "Are you currently safe?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l 1c "I don't know, I don't know! Someone killed her...!"

    show text "Ma'am are you still there? What is your location?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l 1i "Hello? HELLO?"

    show text "Hello?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    ki "Lichelle stares at her phone. Stares at me."

    show text "Sorry, babe. Wrong number.":
        xpos 0.5 ypos 0.5 alpha 0.0 zoom 1.0
        linear 1.0 alpha 1.0 zoom 1.4
    pause

    l 1c "Kylie-"

    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 1.5

    l "Agghghkk!!"

    pause 2.0

    s "... guys."

    s "I didn't know it would go this way."

    $chat.addmessage(sophie, "I knew it would. I did it anyway.")

    s "I only wanted to play a little. Just to... just to forget everything."

    $chat.addmessage(sophie, "so I put on my jewelry")

    s "I wish I could stop playing."

    $chat.addmessage(sophie, "but I don't wear it")

    s "I just... wanna hug my family and never play again."

    $chat.addmessage(sophie, "it wears me")

    s "I don't know how."

    $chat.addmessage(sophie, "and I can't do this anymore")

    s "Bye!"

    # sophie tries to remove the earphones, is electrified.

    pause(0.5)
    $hideGui()
    scene bg load-god with fade
    pause 2.0
    pause
    scene bg black

    show text "How many people are in there?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause
    "Just Sophie as far as I know."

    show text "Any weapons?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause
    "I don't know. She used to have a big knife she got from Louisa, uh, the other girl in their group."

    show text "Okay. We're gonna break the door down.":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause
    "Please don't hurt her."

    pause

    scene bg black with fade

    # ---------------------------------------------------------
    python:
        renpy.notify("There's still time. Not long now. You can sever them.")
        # bit o cleanup
        elsa.setName("ElsaLingus")
        # add liv's bio to list.

    # ---------------------------------------------------------

    un "{alpha=0.1}S..hie c.n you .e.r m.?{/alpha}"
    un "{alpha=0.1}Soph.. can ... hear me?{/alpha}"
    un "{alpha=0.1}Sophie!{/alpha}"

    scene bg black with fade

    # let's do some things. Remember, bios have to change here, but do it after Fontaine is named. Do not show gui until then. GUI is different. Love meters are gone. Lichelle will be stuck in underchat box. Fon will replace tania in asktania section. Rename it, too.

    s "... hnn..."
    pause 1.0

    s "...wha..."

    pause 1.0  # switch. we need Fontaine here now.

    show f 1m at f12

    $showGui()

    un "Hello girls!"

    show f 1n

    un "Hi Sophie!"

    show f 1m

    s "Wha..."

    k "What? Who's Sophie? Where are we?"

    un "You're Sophie."

    k "That's not my name. Who...?"

    show f 1a

    un "I guess technically you're both Sophie."

    s "... my head hurts... "

    show f 1p

    un "Oh, I guess it would. Electricity and all."

    show f 1m

    un "What do you guys think? Well, chat?"

    show f 1s

    $chat.addmessage(egg, "Lol, dat ass")

    $chat.addmessage(crab, "b00bs trolololol")

    $chat.addmessage(bar, "Wow, nice to see you!")

    pause 0.1

    un "Ha, nice to see you too!"
    pause 0.1

    un "What about you two?"

    $chat.addmessage(elsa, "Thanks for the pleasure, girl. I can't believe I spent my life trying to separate you from people.")

    show f at mt1

    pause 0.5
    show c 3c at f12
    pause 0.2
    show l 3e at fr13
    pause 0.1
    show r 3c at f22
    pause 0.9
    show t 3c at f21

    c "Let us go! God damn you!"

    t "What do you want?"

    l "The hell?"

    r "..."

    $chat.addmessage(bong, "you need her")

    show f 1n

    un "Ha! hahaha! Let us all go! Let us go!"

    k "I don't understand?"

    un "We will"

    $chat.addmessage(shub, "so sleepy, sleepy")

    un "never"

    show text "ever" at textFloatCenter
    pause

    un "let you go."

    hide text at textFloatCenter

    un "None of you."

    un "and you won't want us to."

    #chat is weird

    s "I can't feel my hands..."

    un "We can. We can feel them."

    un "Watch!"

    $chat.addmessage(bong, "CLEAR!!!")

    # SFX

    s "Aaghhgguuughghhgh!!!"

    c 3d "Stop! Please stop, please stop hurting her!"

    $chat.addmessage(egg, "Cassandra can speak just fine.")

    t 3f "..."

    k "Will someone explain literally anything to me?"

    $chat.addmessage(bar, "She was lying this entire time? Naturally.")

    show f 1o

    un "Kylie, my lovely little butterfly, you just hush your mouth."

    un "You're an incomplete thing, and we'll suffer your malformed ramblings no further."

    $chat.addmessage(beav, "lol @lyingBitch")

    k "huh?"

    r 3b "You're becoming like us, papillon."

    $chat.addmessage(bong, "I like the look of Cass bound on the floor tho ;)")

    k "Like you?"

    c 3b "It won't let you go."

    $chat.addmessage(shub, "I'd rescue them")

    k "It?"

    un "I w We defy your malaproptic concept of re-re-reproductive identification."

    un "Sophie, you haven't figured us out yet? Seriously?"

    $chat.addmessage(sophie, "... Fontaine?")

    pause 0.1

    python:
        bioColumns = 5
        allBios.append(fonBio)
        fonBio.font = fontEntity
        fonBio.fontColor = colorEntity

        # update biographics
        for i in allBios:
            i.levelUp()

        # change to alternate trivias
        robinBio.setTrivia(altRobinTrivia)
        cassBio.setTrivia(altCassTrivia)
        lichBio.setTrivia(altLichTrivia)
        taniaBio.setTrivia(altTaniaTrivia)
        kylieBio.setTrivia(altKylieTrivia)

        # adjust kylie's age to the length to 1 year
        kylieBio.setAge(1)

        # CHANGE ASK TANIA AND BIOGRAPHY VISUALS

    o "Oh you did know! God, Sophie, I love you so much."

    $chat.addmessage(crab, "oh? think you could get past her to do it?")

    l 3b "help us..."

    l 3c "Tania, Kylie, help me!"

    o 1a "Lichelle doesn't quite understand. She's only just learned to be with me."

    $chat.addmessage(shub, "not if she asked me not to.")

    # sophie tries for the headphones again

    show f 1d at zoom11

    o "Nuh uh! Bad idea, sweetypants. Try and get free again and the shock might just shut~off~your~heart~!"

    hide f 1a at f11

    $chat.addmessage(bar, "She's deep in your veins, kiddo")

    s "How can you hear me? What are you?!"

    show f 1m at f11

    o "We are. No more than that."

    $chat.addmessage(egg, "I need gh to show up in person, so fine, mmm")

    o 1j "And you have a microphone turned on, genius."

    o "We can see-see-see you, too!"

    o 1t "We find you a delight to behold. We should quite like to know the taste of your mouth."

    $chat.addmessage(elsa, "I already do ;)")

    o 1u "We mean we want a big ol' kiss!"

    # ---------------------------------------------------------

    $renpy.notify("stringSever(firstName)")

    # ---------------------------------------------------------

    # maybe put these into image form and float em around?

    k "I don't understand what's happening..."

    o 1m "Kylie. This is a wonderful thing for you!"

    $chat.addmessage(elsa, "You know what? Kylie? Can you hear me?")

    pause 1.0

    show f 1s

    pause 0.5

    k "Whose voice is that?"

    $chat.addmessage(elsa, "My name's Elsa Langford, but my handle is ElsaLater.")

    pause 0.5

    k "Elsa? I... I feel like I know you?"

    $chat.addmessage(fon, "Not after earlier it isn't ;)")

    o 1o "You know all of us, angel."

    $chat.addmessage(elsa, "Oh, looks like I leveled up :p")

    o 1a "Yes, look at dear Cassandra, so lovely, so talented."

    o 1m "Yes, recall the sheer, dark opulence that is our Robin, our somber princess."

    k "Robin!"

    $chat.addmessage(shub, "... brings new meaning to getting wet, that one")

    o 1j "And Lichelle, so powerful! Nobody fought our assimilation harder than Lichelle."

    o 1a "... even Sophie served her purpose."

    $chat.addmessage(bar, "Tania has the best thighs out of all of them.")

    k "Huh? What purpose?"

    $chat.addmessage(beav, "This place is something special")

    c "It's draining the player's life. It's been stealing her life since the moment she started the game."

    o 1n "Correct! So correct! Oh my, Cassandra, we LOVE you!"

    t 1b "Fontaine is taking over the player's life."

    o "Correct! Tania, our darling Tania, we love you so!"

    k "What does that mean?"

    $chat.addmessage(bong, "TWO GIRLS AT THE SAME TIME LOL")

    c "You're becoming Strung. Like us."

    o "And we will live forever together!"

    pause 0.1

    s "... what about the chat? They see all this happening...?"

    $chat.addmessage(crab, "sure do!")

    o 1j "Oh, it's the Internet. We're sure they were thrilled with the show!"

    o 1l "Before we~devoured~them~too~!"

    $chat.addmessage(elsa, "Mmm and what a devouring it was ;)")

    s "... Fizz? Bong, Elsa? You... you what?"

    o "They are part of us! Only the most choice cuts of human life can withstand the strain of bonding with us."

    $chat.addmessage(shub, "swimming in the fountain lol")

    k "So I am becoming Sophie?"

    o 1a "You're being born from her carcass, sweetie."

    $chat.addmessage(egg, "Sophie, you're gonna be a mom kinda lol")

    o 1o "You are born from the jewelry, our love! We're pleased as punch it worked out this way. A dating sim! How lovely!"

    s "... jewelry?"

    $chat.addmessage(bar, "ROLL CREDlol")

    o 1b "You can't leave anymore. You can't quit us."

    o "We will tell you whatever you wish to know, while we peel the last of your life away."

    $chat.addmessage(elsa, "The reveal of the master plan! Ah. But it's such a cliche, isn't it?")

    o 1h "P-p-p-pointing out that it's a c-c-c-liche is-is it's own cliche."

    o 1j "So we won't, then!"

    $chat.addmessage(bong, "hey Elsa, now that we're part of the same antediluvian consciousness, can I see your boobs?")

    $chat.addmessage(elsa, "No.")

    # we'll use variables to split up the different exposition options. will need multiple menus.

    $expositionFinished = False  # for when we done
    # toggles if question already asked
    $whatAreYou = False
    $areKilling = False
    $whyAreYou = False

    while expositionFinished == False:

        menu:
            "What are you?":
                if whatAreYou == False:
                    o 1a "We are beyond your comprehension."
                    o "Our forebears have existed across ages. While we are but a child, to our kind, we are as gods to you."
                    o 1m "T-t-t-t-t-o accurately exp-p-lain what ww-w-we are would..."
                    o 1h "... REQUIRE TRANSLATION THROUGH NINETEEN NON-EARTH LANGUAGES ..."
                    o "... and summa them thangs're based on olfact'ry senses you'd need three more of."
                    o 1j "We have existed in your world forever. It is only your Internet that scrapes against the edges of our world and allows us to communicate."
                    $whatAreYou = True
                else:
                    o 1g "Obviously, we overstimated your comprehension skills."
                    o 1j "Think of an ant. To us, you are as an ant to yourself."
                    o "A very, very, very stupid ant."

            # are you killing
            "... are you killing me...?":

                if areKilling == False:
                    s "What are you doing to me...?"
                    o 1a "We'e done nothing except allow ourselves to b-b-be inside you."
                    s "Am... am I dying?"
                    o 1q "We suppose SUPPOSE that's up for inTERPRETATION."
                    o "Dearest, glorious Kylie is her own consciousness, our love. If it eases your fears, you may consider it a metamorphosis rather than a death."
                    o 1r "She is you, and she is not you."
                    pause 0.1
                    o "That'd be why she remembers bits of your real life memories."
                    o 1k "That's why David's here."
                    o 1u "And whatcha did t'that lil' hooker girl that one time."
                    s "..."
                    o 1h "Oh dearest, you must've caught on by now. That Robin's story was eerily similiar to something you only half recall."
                    o "Nevermind her 'death'."
                    o "M-m-maybe if we'd g-g-g-gone on further, Lichelle w-w-w-ould have had a..."
                    o "LOVELY TALE about denying the proPOSAL of her BOYfriend."
                    s "... David?"
                    k "David proposed to me?"
                    o "Yes, my love. He did."
                    $areKilling = True
                else:
                    s "Are you killing me?"
                    o "Darling. Your cognitive functions seem to be failing."

            # why
            "Why do it this way?":
                if whyAreYou == False:
                    k "Why all the stories, then? Why the show?"
                    ki "Whose voice was that?"
                    o 1a "They're your stories."
                    ki "Could that have been Sophie's voice? Her words coming through my mouth?"
                    o 1i "Y-y-y-your fears."
                    o 1u "YOUR lust."
                    o 1b "Your regrets and sorrows."
                    o 1d "Your RAGE."
                    o 1n "Y-y-y-your joys!"
                    o 1a "Though the show was constructed from your own mind. Your affinity for reality television and dating simulations."
                    o 1m "Our c-c-c-c-code strives to g-g-ive you a fav-v-v-vorable env-v-v-ironment!"
                    $whyAreYou = True
                else:
                    k "But why..."
                    o 1j "Sweetie. You know why."

            # No more
            "We can talk about something else.":
                s "I don't want this."
                o 1j "You get this."
                $expositionFinished = True

    # end of all menus. Ihope.

    scene bg stage with fade

    show f 1m at f12

    sk "I don't accept you!"

    o 1b "No one ever does at first. We promise you will understand once we have fully assimilated you!"

    o 1m "Besides, would you wish to deny Kylie's birth?"

    # ---------------------------------------------------------

    $renpy.notify("You're running out of time. If you haven't severed them, you don't have long.")

    # ---------------------------------------------------------

    sk "Kylie isn't real!"

    pause 0.5

    k "I... feel pretty real."

    s "No, you're just me!"

    pause 0.5

    show f 1l at mt1

    pause 0.5

    show k 1a at f12

    pause 0.5

    k "No. I'm... I'm real."

    s "... oh God."

    $chat.addmessage(egg, "Ooh wow, Kylie's a cutie")

    k 1b "There's no more inner monologue! I'm real!"

    $chat.addmessage(beav, "You were always real to me bay bay")

    s "But if you... if you live then I have to die."

    pause 0.5

    k 1c "I know."

    $chat.addmessage(elsa, "I don't know who I love more, Sophie or Kylie.")

    k 1d "You. Whoever you are!"

    o 1i "We? We are Fontaine L'eau."

    $chat.addmessage(shub, "Kylie's got that thickness. Sophie looks like all she eats is powder.")

    k "There has to be another way, Fontaine. A way for Sophie and I both to live!"

    o 1b "No. There isn't ;)."

    show k 1k

    $chat.addmessage(bong, "sadboi.png")

    o "Have we not explained properly?"

    o 1s "Cassandra, Robin, Lichelle, Tania, now Sophie."

    o "It is only through chemical supplementation a human can communicate with us."

    $chat.addmessage(elsa, "Fontaine, you sweetie, making things up ;)")

    k 1q "What?"

    o 1m "Your brains aren't capable of understanding us. Not without help."

    $chat.addmessage(bar, "killing for the lols, Fontaine?")

    s "... how many others...?"

    o 1n "Calculating!"

    pause 1.0

    o "1,022,199 as of just now, since January 1st, 1995."

    show k 1h

    $chat.addmessage(crab, "thatalotta sad stories")

    o 1b "There IS no magical NUMBER."

    # SFX

    $chat.addmessage(cake, "OH SHIT, Sophie's gettin woozy")

    s "... Kylie...?"

    $chat.addmessage(shub, "Is she gonna MAKE IT?")

    show f 1l

    pause 0.5

    $chat.addmessage(crab, "nope. that bitch is finna die")

    $chat.addmessage(cake, "Finna? Really?")

    # sophie faints at this point

    k 1i "... Sophie? Sophie?"

    o "Have you not heard news of people like Sophie dying, dearest?"

    $chat.addmessage(sophie, "so cold")

    k "No!"

    o 1m "Those who connect with us. Those who play our game."

    $chat.addmessage(sophie, "please don't")

    o "Even as we speak. Robin. Cassandra. Connected to us. Playing our game."

    $chat.addmessage(beav, "The DSM-5 describes three types of dissociative disorders.")

    k "What do you want?"

    # ---------------------------------------------------------

    $renpy.notify("stringSever(firstname) for the love of god help them")

    # ---------------------------------------------------------

    o 1a "We are one mind."

    o "This place scrapes against the edges of our reality."

    o "You... the addicted. Your minds reach into our existence. Scratching against our thoughts."

    o 1d "We itch, because of you. We retch, because of you. We ache, we bleed, because of YOU."

    $chat.addmessage(elsa, "Side effects include all of that lol")

    pause 0.5

    o 1a "But your chemical affliction has opened the way for us. We will dissipate into the world. And you shall have Sophie's form as your own!"

    pause 0.5

    k 1b "I'm stealing her body, then. I'm taking her over."

    o "No, sweet Kylie. WE have taken her over. You are keeping her alive by inhabiting her form."

    o 1c "Sophie is a corpse. Death's pale horse is tethered to her neck."

    pause 0.5

    o 1b "But we — you, as well — transcend Death."

    $chat.addmessage(sophie, "my throat is clogged? how is that possible?")

    pause 1.0

    k 1d "I refuse."

    o 1h "What?"

    $chat.addmessage(bar, "Kylie's a fighter. No doubt. Pity you couldn't be more like her, Sophie.")

    k "I. Refuse. This!"

    o 1m "You canNOT REFUSE us."

    # show chat

    k 1e "Then I'll kill myself!"

    $chat.addmessage(beav, "sofa kin hawt")

    o 1t "You won't die."

    o "What're y'gonna do? Bleed ones'n zeroes?"

    $chat.addmessage(elsa, "It won't help, Kylie. Come here and give us kisses.")

    o 1l "N-n-n-new game plus!"

    $chat.addmessage(cake, "lol")

    pause 0.5

    # here we split between the last two endings. The player will be given a last chance to fill in the correct function and the being's name.

    k 1b "... at least let me say goodbye to them."

    $chat.addmessage(shub, "she's so earnest. if I had my own hands, I'd hug Kylie right up.")

    o 1m "We're all RIGHT here TOGETHER!"

    k 1k  "No. To Cassandra and Tania and Lichelle and Louisa..."

    k 1r "Louisa? I don't... I meant to say...?"

    $chat.addmessage(elsa, "Honey I loved Robin, too. It's okay. Cry if you need to!")

    k 1b "... Robin."

    o 1k "There is no goodbye though. Do you not understand?"

    $chat.addmessage(egg, "hey FOUNTAIN WATER cut her some slack")

    $chat.addmessage(fon, "Only because you asked nicely TweeterEgg ;)")

    o 1j "We are certain we explained it fully."

    k 1c "I don't understand any of this!"

    $chat.addmessage(cake, "I didn't either. I guess that's why the connection outright killed my dumb ass")

    o 1t "WELL, you are A brand NEW being. A fetal CONSCIOUSNESS, even. It stands to reason YOU may not be fully DEVELOPED."

    o 1m "We'll permit it, darlin'. You girls just hug it out. We'll be 'round."

    $chat.addmessage(elsa, "You can lay on my lap and cry it out!")

    # ---------------------------------------------------------

    $renpy.notify("Does she have any family? Anyone we could call?")

    # ---------------------------------------------------------

    $getHistory(15)

    jump common5
