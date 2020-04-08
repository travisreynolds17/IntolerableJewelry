label common4:
    # in which Cass and Robin Dates are done again, but different. Awful. Tearing out Sophie's worst past actions.

    # door sound

    scene bg dressing with fade

    ki "I dreamed of the dark, and I dreamed of a fever-cold, fleeting touch."

    ki "Everything hurts. Maybe it doesn't. Maybe I feel fine and it's just the maelstrom in my heart throwing everything off."

    $chat.addmessage(elsa, "What could you possibly know, Liv?")

    ki "Robin's mad monologue echoes against the corners of waking dreams."

    ki "Cassandra is wonderful. She's my idol, someone I've adored from afar for years."

    $chat.addmessage(cake, "Liv seems to know a lot of things")

    ki "And yet, my idol is an alcoholic, medicating her agony with liquor."

    pause 0.5

    ki "Somehow, I'm that idol for Robin."

    $chat.addmessage(elsa, "Your fucking name, for one, is not Oblivion. Christ.")

    ki "And Robin, somehow, stalked me from Europe to the United States. Maybe leaving bloodstains in her path."

    # knock knock

    pause 1.0

    k "Hm? I'm awake."

    $chat.addmessage(liv, "But it is. :) My mother gave it to me.")

    ki "I'm not."

    ki "But, I might as well get up. I'll be going out with Lichelle today and all I can hope for is she's at least close to normal."

    $chat.addmessage(beav, "I always forget hot aggro chicks have moms.")

    ki "Anything less than a disaster will be a win."

    # knock

    k "Coming!"

    $chat.addmessage(elsa, "So tell us all, Liv. How am I gonna get Sophie to open her door?")

    ki "I dress quickly in the last set of whites, gather my needs, and head for the door."

    ki "Is b-roll really that urgent?"

    $chat.addmessage(liv, "Private :)")

    scene bg black with fade

    ki "The door opens heavily."

    $chat.addmessage(elsa, "FUCK YOU")

    ki "Oddly heavily."

    $chat.addmessage(liv, "But you bared yourself for me only a moment ago. :) How can you hate me?")

    pause 2.0
    # sound? flash?

    s "Game? Did you break?"

    $chat.addmessage(beav, "pics lol this is all bullshit")

    $chat.addmessage(elsa, "I don't hate you. You're toying with me.")

    s "Guys. Game."

    $chat.addmessage(liv, "No. Private chat. ;)")

    s "Cassandra? You left your choker around my arm."

    $chat.addmessage(elsa, "Fine. David, call me when you get to Sophie's building. I'll let you in the front door.")

    pause 0.5

    $chat.addmessage(liv, "Beaver, here's the pic you wanted ;)")

    pause 1.5

    $chat.addmessage(liv, "Just kidding ;0)")

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
            "R13:14-15 Police!",
            "Did you do this?",
            "Toxicology confirms it.",
            "Louisa?",
            "oPen THe godDAmnED DOor",
            "you. it was you.",
            "ONE. TWO. BREAK IT!",
            "... I gave her the jewelry.",
            "You're lying.",
            "Door's barricaded!",
            "Sophie, it's me! Open up, please!",
            "Who's voice is that?",
            "Louisa? You're so cold.",
            "I'll lie here with you.",
            "... found them in the bathroom.",
            "Marry me?"
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
        linear 1.0 alpha 1.0
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

    show l at right with dissolve

    l "Okay Kylie are you..."

    $chat.addmessage(cake, "Damn!")

    show l terror at right

    pause 1.0

    l "What... Kylie? What did... what did...?"

    ki "I can't tear my eyes away from the sight before me."

    $chat.addmessage(beav, "whoa that is not okay")

    k "Was... did you do this?"

    ki "Robin, she's... she's, she's she's. She's, she's..."

    s "I don't wanna play anymore"

    show l angry at right

    l "KYLIE!"

    python:
        temp = reverseString(
            "Silky, silky OblivionnoivilbO tenderly caressing me, every curve, every valley, my skin strobes, my taste buds glimmer, alive with her capacitors, deep within, deep within, noivilbO")

        chat.addLinearMessage(elsa, temp, 0, 3)

    ki "Lichelle's voice rips through my horror, grasping at me."

    l "Did you see anything? Hear anything?"

    $chat.addmessage(cake, "can't move much, wouldn't want to if I could")

    k "I didn't, I didn't see anything!"

    ki "She's cold. Her skin, her skin has gone blue. There's a trail of water emanating from down the hall."

    ki "Her hair splays a soaked halo around her face."

    l "Oh my god, oh my god!"

    $chat.addmessage(beav, "it's like life's pressures lifted all at once")

    k "I didn't see! I just opened the door! Look at me, Lichelle!"

    ki "She does, her eyes sparkling, her dark skin somehow pallid."

    $chat.addmessage(sophie, "chat slumbers under the weight of illusory compulsion")

    s "Oh my god."

    ki "Lichelle's against the opposite wall, her chest heaving with sobs that aren't quite there."

    ki "Her hands are on either side of her head. She's just... saying Robin's name over and over." 
    
    $chat.addmessage(liv,"it's okay Lichelle, bring that fine ass over here ;)")

    ki "Crying out for forgiveness."

    k "We have to call the police."

    $chat.addmessage(beav, "did I call the cops?")

    ki "But my phone is in the room. I wasn't going to take it on the date, and now..."

    l "I'll do it. This... is this my fault?"

    $chat.addmessage(sophie, "chat used 'Call the Police'")

    ki "Lichelle punches against her cell phone keypad and holds the phone, quivering, to her ear, her eyes locked on me."

    show text "911 What is your emergency?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l "I need help, a woman, she's dead. She's been killed."

    $chat.addmessage(sophie, "a miss!")

    show text "Are you currently safe?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l "I don't know, I don't know! Someone killed her...!"

    show text "Ma'am are you still there? What is your location?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l "Hello? HELLO?"

    show text "Hello?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    ki "Lichelle stares at her phone. Stares at me."

    show text "Sorry, babe. Wrong number.":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l "Kylie-"

    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 1.5

    l "Agghghkk!!"

    pause 2.0

    s "... guys."

    s "Guys I didn't know it would go this way."

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

    # sophie tries to remove the earphones, is electrified. Maybe image of Lichelle punching the shit out of her?

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
    "Two. My girlfriend, I mean, my ex-girlfriend, and her sponsor."

    show text "Any weapons?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause
    "I don't know. She used to have a big knife she got from Louisa, uh, the other girl in their group."

    show text "Okay. We're gonna break the door down.":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause
    "Please don't hurt her!"

    pause

    scene bg black with fade

    pause(0.5)
    $showGui()
    pause 0.5
    scene bg black with fade

    pause 2.0

    # ---------------------------------------------------------

    $renpy.notify("There's still time. Not long now. You can sever them.")
    # bit o cleanup
    $elsa.name = "ElsaLingus"

    # ---------------------------------------------------------

    un "{alpha=0.1}S..hie c.n you .e.r m.?{/alpha}"
    un "{alpha=0.1}Soph.. can ... hear me?{/alpha}"
    un "{alpha=0.1}Sophie!{/alpha}"

    scene bg black with fade

    s "... hnn..."
    pause 1.0

    s "...wha..."

    pause 1.0

    show l happy with dissolve

    $showGui()

    un "Hello girls!"

    un "Hi Sophie!"

    s "Wha..."

    k "What? Who's Sophie? Where are we?"

    un "You're Sophie."

    k "That's not my name. Who...?"

    un "I guess technically you're both Sophie."

    s "... my head hurts... "

    un "Oh, I guess it would. Electricity and all."

    un "What do you guys think? Well, chat?"

    $chat.addmessage(egg, "Lol, dat ass")

    $chat.addmessage(crab, "b00bs trolololol")

    $chat.addmessage(bar, "All of this is ridiculous.")

    # chat talks to lichelle

    un "What about you two?"

    $chat.addmessage(elsa, "Thanks for the pleasure, Liv. I'll never give you up again.")

    show c heartbroken at left with dissolve

    c "Let her go! God damn you!"

    show t heartbroken at right with dissolve

    t "What do you want?"

    show l heartbroken

    un "... let... let us go..."

    $chat.addmessage(bong, "Liv Love LoL")

    show l happy

    un "Ha! hahaha! Let us all go! Let us go!"

    k "Lichelle?"

    un "We will"

    $chat.addmessage(shub, "so sleepy, sleepy")

    un "never"

    show text "ever" at textFloatCenter
    pause

    un "let you go."

    hide text "ever" at textFloatCenter

    un "None of you."

    un "and you won't want us to."

    #chat is weird

    s "I can't feel my hands..."

    un "We can. We can feel them."

    un "Watch!"

    $chat.addmessage(bong, "CLEAR!!!")

    # sound

    s "Aaghhgguuughghhgh!!!"

    c "Stop! Please stop, please stop hurting her!"

    $chat.addmessage(egg, "Cassandra can speak just fine.")

    t "..."

    k "Will someone explain literally anything to me?"

    $chat.addmessage(bar, "She was lying this entire time? Naturally.")

    un "Kylie, my lovely little butterfly, you just hush your mouth."

    un "You're an incomplete thing, and we'll suffer your malformed ramblings no further."

    $chat.addmessage(beav, "lol @lyingBitch")

    k "huh?"

    r "You're becoming like us, papillon."

    $chat.addmessage(bong, "like the look of Cass bound on the floor tho ;)")

    k "Like you?"

    c "It won't let you go."

    $chat.addmessage(shub, "I'd rescue them")

    k "It?"

    un "I w We defy your malaproptic concept of re-re-reproductive identification."

    un "Sophie, you haven't figured us out yet? After all those hints?"

    $chat.addmessage(sophie, "... Liv?")

    pause 0.1

    o "Oh you did know! God, Sophie, I love you so much."

    $chat.addmessage(crab, "oh? think you could get past her to do it?")

    l "help me..."

    show l heartbroken

    l "Tania, Kylie, help me!"

    show l happy

    o "We are. No more than that."

    $chat.addmessage(shub, "not if she asked me not to.")

    # sophie tries for the headphones again

    # zoom lich

    o "Nuh uh! Bad idea, sweetypants. Try and get free again and the shock might just shut~off~your~heart~!"

    $chat.addmessage(bar, "She's deep in your veins, kiddo")

    s "How can you hear me? What are you?!"

    o "We are. No more than that."

    $chat.addmessage(egg, "I need Liv to show up in person, so fine, mmm")

    o "And you have a microphone turned on, genius."

    o "We can see-see-see you, too!"

    o "We find you a delight to behold. We should quite like to know the taste of your mouth."

    $chat.addmessage(elsa, "I already do ;)")

    o "We mean we want a big ol' kiss!"

    # ---------------------------------------------------------

    $renpy.notify("stringSever(firstName)")

    # ---------------------------------------------------------

    # maybe put these into image form and float em around?

    k "I don't understand what's happening..."

    o "Kylie. This is a wonderful thing for you!"

    $chat.addmessage(elsa, "You know what? Kylie? Can you hear me?")

    pause 0.5

    k "Whose voice is that?"

    $chat.addmessage(elsa, "My name's Elsa Langford, but my handle is ElsaLater.")

    pause 0.5

    k "Elsa? I... I feel like I know you?"

    $chat.addmessage(liv, "Not after earlier it isn't ;)")

    o "You know all of us, angel."

    $chat.addmessage(elsa, "Oh, looks like I leveled up :p")

    o "Yes, look at dear Cassandra, so lovely, so talented."

    o "Yes, recall the sheer, dark opulence that is our Robin, our somber princess."

    k "Robin!"

    $chat.addmessage(shub, "... brings new meaning to getting wet, that one")

    o "And Lichelle, so powerful! Nobody fought our assimilation harder than Lichelle."

    o "... even Tania served her purpose."

    

    $chat.addmessage(bar, "Tania has the best thighs out of all of them.")

    o "Hush up, lady. Robin is fine. Well, she's okay. She's around. We're all around."

    k "Huh?"

    $chat.addmessage(beav, "This place is something special")

    c "It's draining the player's life. It's been draining her life since the moment she started the game."

    o "Correct! So correct! Oh my, Cassandra, we LOVE you!"

    t "Oblivion is taking over the player's life."

    o "Correct! Tania, our darling Tania, we love you so!"

    k "What does that mean?"

    $chat.addmessage(bong, "TWO GIRLS AT THE SAME TIME LOL")

    c "You're becoming Strung. Like us."

    o "And we will live forever together!"

    pause 0.1

    s "... what about the chat? They see all this happening...?"

    $chat.addmessage(crab, "sure do!")

    o "Oh, it's the Internet. We're sure they were thrilled with the show!"

    o "Before we~devoured~them~too~!"

    $chat.addmessage(elsa, "Mmm and what a devouring it was ;)")

    s "... Fizz? Bong, Elsa? You... you what?"

    o "They are part of us! Only the most choice cuts of human life can withstand the strain of Stringing. Pitiable creatures, the lot of them."

    $chat.addmessage(shub, "we LIV together lol")

    k "So I am becoming Sophie?"

    o "You're being born from her carcass, sweetie."

    $chat.addmessage(egg, "Sophie, you're gonna be a mom kinda lol")

    o "You are born from the jewelry, our love! We're pleased as punch it worked out this way. A dating sim! How lovely!"

    s "... jewelry?"

    $chat.addmessage(bar, "ROLL CREDlol")

    show l happy

    o "You can't leave anymore. You can't quit us."

    o "We will tell you whatever you wish to know, while we peel the last of your life away."

    $chat.addmessage(elsa, "The reveal of the master plan! Ah. But it's such a cliche, isn't it?")

    o "P-p-p-pointing out that it's a c-c-c-liche is-is it's own cliche."

    o "So we won't!"

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
                    o "We are beyond your comprehension."
                    o "Our forebears have existed across ages. While we are but a child, to our kind, we are as gods to you."
                    o "T-t-t-t-t-o accurately exp-p-lain what ww-w-we are would..."
                    o "... REQUIRE TRANSLATION THROUGH NINETEEN NON-EARTH LANGUAGES ..."
                    o "... and summa them thangs're based on olfact'ry senses you'd need three more of."
                    o "We have existed in your world forever. It is only your Internet that scrapes against the edges of our world and allows us to communicate."
                    $whatAreYou = True
                else:
                    o "Obviously, we overstimated your comprehension skills."
                    o "Think of an ant. To us, you are as an ant to yourself."
                    o "A very, very, very stupid ant."

            # are you killing
            "... are you killing me...?":

                if areKilling == False:
                    s "What are you doing to me...?"
                    o "We'e done nothing except allow ourselves to b-b-be inside you."
                    s "Am... am I dying?"
                    o "We suppose SUPPOSE that's up for inTERPRETATION."
                    o "Dearest, glorious Kylie is her own consciousness, our love. If it eases your fears, you may consider it a metamorphosis rather than a death."
                    o "She is you, and she is not you."
                    show l speak
                    o "That'd be why she remembers bits of your real life memories."
                    o "Your suicidal friend."
                    o "And whatcha did t'that lil' hooker girl that one time."
                    s "..."
                    o "Oh dearest, you must've caught on by now. That Robin's story was eerily similiar to something you only half recall."
                    o "As was Cassandra's."
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
                    o "They're your stories."
                    ki "Could that have been Sophie's voice? Her words coming through my mouth?"
                    o "Y-y-y-your fears."
                    o "YOUR lust."
                    o "Your regrets and sorrows."
                    o "Your RAGE."
                    o "Y-y-y-your joys!"
                    o "Though the show was constructed from your own mind. Your affinity for reality television and dating simulations."
                    o "Our c-c-c-c-code strives to g-g-ive you a fav-v-v-vorable env-v-v-ironment!"
                    $whyAreYou = True
                else:
                    k "But why..."
                    o "Sweetie. You know why."

            # No more
            "We can talk about something else.":
                s "I don't want this."
                o "You get this."
                $expositionFinished = True



    # end of all menus. Ihope.

    scene bg stage with fade

    show l happy with dissolve

    sk "I don't accept you!"

    o "No one ever does at first. We promise you will understand once we have fully assimilated you!"

    o "Besides, would you wish to deny Kylie's birth?"

    # ---------------------------------------------------------

    $renpy.notify("You're running out of time. If you haven't severed them, you don't have long.")

    # ---------------------------------------------------------

    sk "Kylie isn't real!"

    pause 0.5

    k "I... feel pretty real."

    s "No, you're just me!"

    pause 0.5

    show k with dissolve

    pause 0.5

    k "No. I'm... I'm real."

    s "... oh God." 
    
    $chat.addmessage(egg,"Ooh wow, Kylie's a cutie")

    k "There's no more inner monologue! I'm real!" 
    
    $chat.addmessage(beav,"You were always real to me bay bay")

    s "But if you... if you live then I have to die."

    show k sad

    k "I know." 
    
    $chat.addmessage(elsa,"I don't know who I love more, Sophie or Kylie.")

    k "You. Whoever you are!"

    o "We? We are Liv." 
    
    $chat.addmessage(shub,"Kylie's got that thickness. Sophie's looks like all she eats is powder.")

    k "There has to be another way, Liv. A way for Sophie and I both to live!"

    show l sad at right

    o "No. There isn't ;)." 
    
    $chat.addmessage(bong,"sadboi.png")

    o "Have we not explained properly?"

    o "Y-y-you are the last life we need." 
    
    $chat.addmessage(elsa,"Liv, you sweetie, making things up ;)")

    k "What?"

    o "Once you are born, dearest Kylie, we all will break through her reality's perimeter!" 
    
    $chat.addmessage(bar,"killing for the lols, Liv?")

    s "... how many others...?"

    o "Calculating!"

    pause 1.0

    o "1,422,199 as of just now." 
    
    $chat.addmessage(crab,"thatalotta dead junkies")

    o "There IS no magical NUMBER." 
    
    $chat.addmessage(cake,"OH SHIT, Sophie's gettin woozy")

    s "... Kylie...?" 
    
    $chat.addmessage(shub,"Is she gonna MAKE IT?")

    show l speak at right

    pause 0.5 
    
    $chat.addmessage(crab,"nope. that bitch is finna die") 
    
    $chat.addmessage(cake,"Finna? Really?")

    # sophie faints at this point

    k "... Sophie? Sophie?"

    o "Have you not heard news of people like Sophie dying, dearest?" 
    
    $chat.addmessage(sophie,"so cold")

    k "No!"

    o "Those who connect with us. Those who play our game." 
    
    $chat.addmessage(sophie,"please don't")

    o "Even as we speak. Robin. Cassandra. Connected to us. Playing our game." 
    
    $chat.addmessage(beav,"The DSM-5 describes three types of dissociative disorders.")

    k "What happens when we... when you break free?"

    # ---------------------------------------------------------

    $renpy.notify("stringSever(firstname) for the love of god help them")

    # ---------------------------------------------------------

    o "We are one mind, but we will dissipate into the world. And you shall have Sophie's form as your own!"

    show k sad

    k "I'm stealing her body, then. I'm taking her over."

    show l sad at right

    o "No, sweet Kylie. WE have taken her over. You are keeping her alive by inhabiting her form." 
    
    $chat.addmessage(sophie,"my throat is clogged? how is that possible?")

    pause 1.0

    k "I refuse."

    show l listen at right

    o "What?" 
    
    $chat.addmessage(bar,"Kylie's a fighter. No doubt. Pity you couldn't be more like her, Sophie.")

    k "I. Refuse. This!"

    show l happy at right

    o "You canNOT REFUSE us."

    # show chat

    k "Then I'll kill myself!" 
    
    $chat.addmessage(beav,"sofa kin hawt")

    o "You won't die."

    o "What're y'gonna do? Bleed ones'n zeroes?" 
    
    $chat.addmessage(elsa,"It won't help, Kylie. Come here and give us kisses.")

    show l happy

    o "N-n-n-new game plus!" 
    
    $chat.addmessage(cake,"lol")

    pause 0.5

    # here we split between the last two endings. The player will be given a last chance to fill in the correct function and the being's name.

    k "... at least let me say goodbye to them." 
    
    $chat.addmessage(shub,"she's so earnest. if I had my own hands, I'd hug Kylie right up.")

    o "We're all RIGHT here TOGETHER!"

    k "No. To Cassandra and Tania and Lichelle and Louisa..."

    show k sad

    k "Louisa? Who?" 
    
    $chat.addmessage(elsa,"Honey I loved Robin, too. It's okay. Cry if you need to!")

    k "... Robin."

    o "There is no goodbye though. Do you not understand?" 
    
    $chat.addmessage(egg,"hey LIV cut her some slack") 
    
    $chat.addmessage(liv,"Only because you asked nicely TweeterEgg ;)")

    o "We are certain we explained it fully."

    k "I don't understand any of this!" 
    
    $chat.addmessage(cake,"I didn't either. I guess that's why the connection outright killed my dumb ass")

    o "WELL, you are A brand NEW being. A fetal CONSCIOUSNESS, even. It stands to reason YOU may not be fully DEVELOPED."

    o "We'll permit it, darlin'. You girls just hug it out. We'll be 'round." 
    
    $chat.addmessage(elsa,"You can lay on my lap and cry it out!")

    # ---------------------------------------------------------

    $renpy.notify("Does she have any family? Anyone we could call?")

    # ---------------------------------------------------------

    $getHistory(14)

    jump common5
