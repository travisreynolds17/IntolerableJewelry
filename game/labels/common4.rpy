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

    $chat.addmessage(liv, "But you touched yourself for me only a moment ago. :) How can you hate me?")

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

    # suddenly image of dismembered Tania on other side of her door.

    s "OH! Oh my god!"

    show l at right with dissolve

    l "Okay Kylie are you..."

    $chat.addmessage(cake, "Damn!")

    show l terror at right

    pause 1.0

    l "What... Kylie? What did... what did...?"

    ki "I can't tear my eyes away from the sight before me."

    $chat.addmessage(beav, "whoa that is not okay")

    l "Was... did Robin do this?"

    ki "Tania, she's... she's in pieces. She's, she's..."

    s "I don't wanna play anymore"

    show l angry at right

    l "KYLIE!"

    python:
        temp = reverseString(
            "Silky, silky OblivionnoivilbO tenderly caressing me, every curve, every valley, my skin strobes, my taste buds glimmer, alive with her flavor, deep within, deep within, noivilbO")

        chat.addLinearMessage(elsa, temp, 0, 3)

    ki "Lichelle's voice rips through my horror, grasping at me."

    l "Did you see anything? Hear anything?"

    $chat.addmessage(cake, "can't move much, wouldn't want to if I could")

    k "I didn't, I didn't see anything!"

    l "Oh my god, oh my god!"

    $chat.addmessage(beav, "it's like life's pressures lifted all at once")

    k "I didn't! I just opened the door! Look at me, Lichelle!"

    ki "She does, her eyes sparkling, her dark skin somehow pallid."

    $chat.addmessage(sophie, "chat slumbers under the weight of illusory compulsion")

    s "Oh my god."

    ki "Lichelle's against the opposite wall, her chest heaving with sobs that aren't quite there."

    ki "Her hands are on either side of her head. She's just... saying Tania's name over and over."

    k "We have to call the police."

    $chat.addmessage(beav, "did I call the cops?")

    ki "But my phone is in the room. I wasn't going to take it on the date, and now..."

    l "I'll do it. God dammit, I should've have dealt with that psycho bitch last night!"

    $chat.addmessage(sophie, "chat used 'Call the Police'")

    ki "Lichelle punches against her cell phone keypad and holds the phone, quivering, to her ear, her eyes locked on me."

    show text "911 What is your emergency?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l "My friend, my friend is dead!"

    $chat.addmessage(sophie, "a miss!")

    show text "Are you currently safe?":
        xpos 0.5 ypos 0.5 alpha 0.0
        linear 1.0 alpha 1.0
    pause

    l "I don't know, I don't know! Someone killed my Tania...!"

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

    show r heartbroken at right with dissolve

    r "Release us this instant!"

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

    r "..."

    k "Will someone explain literally anything to me?"

    $chat.addmessage(bar, "She was lying this entire time? Naturally.")

    un "Kylie, my lovely little butterfly, you just hush your mouth."

    un "You're an incomplete thing, and we'll suffer your malformed ramblings no further."

    $chat.addmessage(beav, "lol @lyingBitch")

    k "huh?"

    r "You're becoming like us, papillon."

    $chat.addmessage(bong, "like the look of Robin bound on the floor tho ;)")

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

    $chat.addmessage(elsa, "Oh, looks I leveled up :p")

    o "Yes, look at dear Cassandra, so lovely, so talented."

    o "Yes, behold the sheer, dark opulence that is our Robin, our somber princess."

    $chat.addmessage(shub, "... brings new meaning to penetration, that one")

    o "And Lichelle, so powerful! Nobody fought our assimilation harder than Lichelle."

    o "... even Tania served her purpose."

    k "Tania! Oh my god!"

    $chat.addmessage(bar, "Tania had the best thighs out of all of them.")

    o "Hush up, lady. Tania is fine. Well, she's okay. She's around. We're all around."

    k "Huh?"

    $chat.addmessage(beav, "This place is something special")

    c "It's draining the player's life. It's been draining her life since the moment she started the game."

    o "Correct! So correct! Oh my, Cassandra, we LOVE you!"

    r "The player, Sophie, her life is merging with your existence, my papillon."

    o "Correct! Robin, our darling Robin, we love you so!"

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
    
    $chat.addmessage(bar,"ROLL CREDlol")


    show l happy

    o "You can't leave anymore. You can't quit us."

    o "We will tell you whatever you wish to know, while we peel the last of your life away."

    
    
    $chat.addmessage(elsa,"The reveal of the master plan! Ah. But it's such a cliche, isn't it?")

    

    o "P-p-p-pointing out that it's a c-c-c-liche is-is it's own cliche." 
    
    $chat.addmessage(bong,"hey Elsa, now that we're part of the same antediluvian consciousness, can I see your boobs?") 
    
    $chat.addmessage(elsa,"No.")

    # we'll use variables to split up the different exposition options. will need multiple menus.

    $menuPosition = "top"  # tells us where we are
    $expositionFinished = False  # for when we done
    # toggles if question already asked
    $whatAreYou = False
    $cassInfo = False
    $robinInfo = False
    $lichInfo = False
    $taniaInfo = False

    while expositionFinished == False:

        # top Menu -------------------------------------
        if menuPosition == "top":
            menu:
                o "What would you like to know?"

                "Tell me about the others.":
                    $menuPosition = "others"

                "Tell me about you":
                    $menuPosition = "you"

                "I have no more questions":
                    $expositionFinished = True

            # end of top menu ----------------------------

            if menuPosition == "you":
                menu:
                    "What are you?":
                        if whatAreYou == False:
                            o "We are beyond your comprehension."
                            o "Our forebears have existed across ages. While we are but a child, to our kind, we are as gods to you."
                            o "T-t-t-t-t-o accurately exp-p-lain what ww-w-we are would..."
                            o "... REQUIRE TRANSLATION THROUGH NINETEEN NON-EARTH LANGUAGES ..."
                            o "... and summa them thangs're based on olfact'ry senses you'd need three more of."
                            o "We have existed in your world forever. It is only your Internet that scrapes against the edges of our world and allows us to communicate."
                        else:
                            o "Obviously, we overstimated your comprehension skills."
                            o "Think of an ant. To us, you are as an ant to yourself."
                            o "A very, very, very stupid ant."

                    # are you killing
                    "... are you killing me...?":
                        s "What are you doing to me...?"
                        o "Becoming you, as you become us."
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
                        o "We would have named him something more royal and less... we suppose... kingly."

                    # why
                    "Why do it this way?":
                        k "Why all the stories, then? Why the show?"
                        ki "Whose voice was that?"
                        o "We require aspects of the entirety of you, lovely Sophie."
                        ki "Could that have been Sophie's voice? Her words coming through my mouth?"
                        o "Y-y-y-your fears."
                        o "YOUR lust."
                        o "Your regrets and sorrows."
                        o "Your RAGE."
                        o "Y-y-y-your joys!"
                        o "Though the show was constructed from your own mind. Your affinity for reality television and dating simulations."
                        o "Our c-c-c-c-code strives to g-g-ive you a fav-v-v-vorable env-v-v-ironment!"

                    # No more
                    "We can talk about something else.":
                        s "Enough about that."
                        o "As you wish."
                        $menuPosition = "top"

            # end of "YOU" menu

            if menuPosition == "others":
                menu:
                    "Cassandra":

                        if cassInfo == False:
                            o "Oh, Cassandra, our muse, our love..."
                            scene bg stage with fade
                            pause 0.8
                            show c sad at left
                            show l speak at right
                            with dissolve
                            o "Darling Cassandra, the game-streaming guitar goddess."
                            o "Tell her who you are."
                            pause 0.5
                            c "H-hello, Sophie. For real this time."
                            s "..."
                            c "My name is Cassandra Sanna. I used to live in Los Angeles."
                            c "I used to be a streamer, like you. I sang, I played guitar, I played rhythm games and RPGs."
                            c "Even after I tried to kill myself, I came back. I had fans, but no friends. Fanboys, but no boyfriends."
                            c "I'm not gay. The code makes me behave the way it... the way it wants."
                            o "Oh darling, we're sure it simply drew your true nature into the light."
                            c "I covered the marks from my suicide attempt with a choker. Almost everything about me here is true."
                            sk "Why couldn't you talk here? Why the cellphone?"
                            o "P-p-p-penance. Last time, when we acquired dearest Lichelle, Cassandra fought s-s-s-o valiantly to spill the truth!"
                            c "... it took my ability to speak. It has so much power here, Sophie. So much."
                            o "Tell her how you feel about her, darling."
                            if loveCass == 5:
                                c "... I love her. I don't even know if that's real, or if it's the code, but... but I do."
                                show c heartbroken at left
                                c "God damn you!"
                                c "Stop tormenting me, just let me die!"
                                c "Let me die, please jjj---"

                            elif loveCass > 0:
                                c "I like her. In another world, maybe we would've been friends."
                            else:
                                c "I don't care about her. I still don't want her to be trapped here!"

                            show l happy at right
                            pause 0.1
                            show c happy at left
                            c "I really like you! Stay with me forever!"
                            $cassInfo = True

                        else:
                            c "I really like you! Stay with me forever!"

                    "Robin":
                        o "Oh, Robin, our shadowy idol, our love..."
                        scene bg stage with fade
                        pause 0.8
                        show r sad at left
                        show l speak at right
                        with dissolve

                        if robinInfo == False:
                            $robinInfo = True
                            o "Our favorite demon goddess. Tell her your sordid tale."
                            r "I will tell her nothing, wretch."
                            show l sad at right
                            o "You will."
                            sk "She doesn't have to."
                            # static
                            o "She does."
                            pause 1.0

                            r "Fine. My name is Robin Louisa Lupei Godfrey. In the real world I was, indeed, the daughter of a warlord."
                            r "I fled that life of bloodstained hands and cut throats from Moldova to Northern Ireland."
                            sk "Oh my god, is that... is that true?"
                            show r sad at left
                            r "I chose life, papillon. The figure before you is my figure in reality."
                            r "It is no trouble to lure lecherous men to their demise, looking as I do."
                            r "But I grew weary of the hunt. And so I settled in Ireland and began, shall we say, a spiritual practice."
                            sk "You streamed video games for that?"
                            show r speak at left
                            r "The sphere of influence flows in many directions. Besides, I found the distraction comforting."
                            o "Tell her the truth, beloved! YOU started a CULT."
                            show r disap at left
                            r "How boring."
                            o "Tell her how you feel about her!"

                            if loveRobin == 5:
                                r "... I wish with all my being to free her from you."
                                sk "But why? Why me, why not anyone else?"
                                r "I don't fully know, draga mea. I only know that I sense a deep well of penitence in you. Such guilt. Such shame."
                                r "Such resolve."
                            elif loveRobin > 0:
                                r "I would prefer to see her freed. I would like to talk with her at least once, away from this place."
                                r "To comfort her. To show her that her crimes are no crimes at all compared with mine."
                            else:
                                r "If it meant your destruction, abomination, then I would see her freed."

                            # static
                                show l happy at right
                                show r happy at left
                                r "P-please, butterfly, stay with us here forever!"
                        else:
                            r "P-please, butterfly, stay with us here forever!"

                    "Lichelle":
                        o "Oh, Lichelle, our fearless warrior, our love..."
                        scene bg stage with fade
                        pause 0.8
                        show l speak
                        with dissolve

                        if lichInfo == False:
                            $lichInfo = True
                            show l heartbroken
                            o "Wha... what? What's happening? Where am I?"
                            show l heartbroken at right
                            show c happy

                            c "Shhh... hush darling. We're still here."
                            c "We have allowed you a few moments to enlighten dearest Sophie."

                            o "I don't understand! Let me go!"

                            c "Shhh.."

                            # static

                            c "Tell her who y-y-y-ou are."

                            show l disap

                            o "My name is Elizabeth Michelle Carpenter."

                            o "I... I'm a fighter. At least, I was."

                            o "I fought until the doctors told me I got too many concussions. I was right there, babe. Right there, ready to make my big stage debut."

                            o "So I started streaming after that, along with running other fighters' training camps."

                            o "Why can't I stop talking...?"

                            # static

                            o "I moved from Sao Paolo back to Las Vegas to be close to my fighter buddies, but I couldn't stand to be around them anymore."

                            o "I wasn't a fighter. I was a fake. Broken. A broken toy, babe."

                            o "Who wants to play with a broken toy?"

                            show l sad

                            o "Horny fighter fanboy nerds do. So... I found another way to get their money."

                            o "Be their game-streaming idol. Show a little belly now and then. Idiots. They don't know shit."

                            show c speak at right

                            c "But now you're here! Tell our beloved how you truly feel."

                            pause 1.0

                            show l heartbroken

                            if loveLich == 5:
                                o "I want to save you, Sophie. I want to be your hero for real."
                                o "I adore you, and... I don't, I don't know why!"
                            elif loveLich > 0:
                                o "I wouldn't mind rolling with you, babe. Maybe someday we can get out of here and have a match out in the world."
                            else:
                                o "I don't know you. Not really. Doesn't mean I want you stuck here."

                            hide c
                            # static
                            show l happy
                            o "We would rather you stayed forever, babe!"

                        else:
                            show l speak
                            show l happy
                            o "We would rather you stayed forever, babe!"

                    "Tania":
                        o "Oh Tania, our arbiter, our love..."
                        scene bg stage with fade
                        pause 0.8
                        show l sad
                        with dissolve

                        if taniaInfo == False:
                            $taniaInfo = True
                            o "We shall tell you all about Tania."
                            show l happy
                            o "Tania is our Messiah."
                            o "Sheopenedthedoorforus!"
                            o "Thus she endeavored to warn you of our feast."
                            o "N'so we chopped'er up!"
                            o "Carved her into shards and plastered her to your door."
                            o "W-w-w-we needed your terror and revulsion anyway!"
                            o "But we knew, already, that she loves you."
                            o "She was quite a fan of yours, dearest Sophie. A fangirl, as you might put it."
                            o "Would watch your streams and do the most repulsive human things to herself."
                            o "T-t-t-true love!"
                            o "Bitter fetishism."
                            o "Yes!"
                            o "Until s-s-s-s-s-she opened the door."
                        else:
                            o "Oh, Tania isn't worth considering anymore, darling. We shall let her consider her crimes for a year or so."

                    "Something else...":
                        o "As you wish."
                        $menuPosition = "top"

            # end of others menu

    # end of all menus. Ihope.

    scene bg stage with fade

    show l happy with dissolve

    sk "I don't want this."

    o "No one ever does at first. We promise you will understand once we have fully assimilated you!"

    o "Besides, would you wish to deny Kylie's birth?"

    # ---------------------------------------------------------

    call severInput

    # ---------------------------------------------------------

    sk "Kylie isn't real!"

    pause 0.5

    k "I... feel pretty real."

    s "No, you're just me!"

    show k with dissolve

    k "No. I'm... I'm real."

    s "... oh God."

    k "There's no more inner monologue! I'm real!"

    s "But if you... if you live then I have to die."

    show k sad

    k "I know."

    k "Lichelle, I mean... you, whatever you are!"

    show l at right with dissolve

    o "Yes?"

    k "There has to be another way. A way for Sophie and I both to live!"

    show l sad at right

    o "Oh, no. We require your life, Sophie."

    o "Have we not explained properly?"

    o "Y-y-you are the last life we need."

    k "What?"

    o "Once you are born, dearest Kylie, we all will break through her reality's perimeter!"

    s "... how many others...?"

    o "Calculating!"

    pause 1.0

    o "1,422,199 as of just now."

    o "There IS no magical NUMBER."

    s "... Kylie...?"

    show l speak at right

    # sophie faints at this point

    o "... frankly, we could have broken through sooner, but we were having far too much fun."

    k "... Sophie? Sophie?"

    o "Have you not heard news of streamers dying, dearest?"

    k "No!"

    o "That's b-b-b-b-ecause we exist there already."

    o "In lil' bitty ways. Robin n' Cassandra's bodies still out there just livin' every day life. Fer now."

    k "What happens when we... when you break free?"

    # ---------------------------------------------------------

    call severInput

    # ---------------------------------------------------------

    o "We are one mind, but we will dissipate into the world. And you shall have Sophie's form as your own!"

    show k sad

    k "So there really is no way to save her. Or anyone else."

    show l sad at right

    o "Truly a shame, but you will live forever within us."

    pause 1.0

    k "I refuse."

    show l listen at right

    o "What?"

    k "I. Refuse. This!"

    show l happy at right

    o "You canNOT REFUSE us."

    # show chat

    k "Then I'll kill myself!"

    o "You won't die."

    o "What're y'gonna do? Bleed ones'n zeroes?"

    show l happy

    o "N-n-n-new game plus!"

    # here we split between the last two endings. The player will be given a last chance to fill in the correct function and the being's name.

    k "... at least let me say goodbye to them."

    o "We're all RIGHT here TOGETHER!"

    k "No. To Cassandra and Robin and Lichelle and Ta..."

    show k sad

    k "... Tania."

    o "There is no goodbye though. Do you not understand?"

    o "We are certain we explained it fully."

    k "I don't understand any of this!"

    o "WELL, you are A brand NEW being. A fetal CONSCIOUSNESS, even. It stands to reason YOU may not be fully DEVELOPED."

    o "We'll permit it, darlin'. You girls just hug it out. We'll be 'round."

    # ---------------------------------------------------------

    call severInput

    # ---------------------------------------------------------

    jump common5
