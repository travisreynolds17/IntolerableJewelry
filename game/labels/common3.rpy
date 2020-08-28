label common3:
    # repeats end of common1, with some stuff changed. Some cleanup:
    # update left window button from come fund me to input request
    $chat.delmessages()
    $leftBtnTxt[1] = "Function"

    # set current scene for chat history purposes
    $sceneNum = 8

    stop music fadeout 4.0

    scene bg story-2 with fade
    pause

    scene bg stage
    with fade

    pause 0.5

    play music cheerfulGuitar fadein 3.0

    $showGui()

    pause 0.5

    s 1b "Hey guys, I'm back. If you're still around."

    s "I'm really sorry about that. Maybe I'm not as okay as I thought I was."

    $chat.addmessage(elsa, "You can reach out to me if you need to!")

    s "I'm going to get through this game, we're gonna have a great time."

    $chat.addmessage(fizz, "I was worried. You didn't answer your phone.")

    s "Thanks, Elsa. After we finish this game, I think I might give you a call."

    $chat.addmessage(elsa, "I would love that.")

    s "Fizz, we don't do that anymore. We talked about this. You can be here, but personal life is off limits."

    $chat.addmessage(fizz, "I was just worried.")

    $chat.addmessage(cake, "No means no, bro")

    s "So let's get back to it. The good news here is we know what's coming, so we can tailor our choices a little bit better."

    $chat.addmessage(crab, "Hey Sophie. You're a stone cold killer, don't get too nervous about things.")

    pause 0.5

    show t 1a at f12

    t "Wow, that's some story! So, we know you were just off camera while our Suitors introduced themselves."

    $chat.addmessage(fon, "I love you Sophie. I need you to love you, too :)")

    hide t at f12
    pause 0.3
    show c 1m at f11
    show r 1m at f12
    show l 1m at f13

    t "Given what you heard from them, who has your attention?"

    s 1a "Okay. Well, I guess we're going from here again!"

    $chat.addmessage(cake, "Gonna be heckin weird pretending like we don't know things")

    s 1a "Should we bother with Lichelle or Tania? I mean... maybe we missed something last time."
    s 1b "I'm worried they're bad end routes or something."
    $temp = False
    $taniaPicked = False

    while temp == False:

        hide t
        hide r 
        hide c 
        hide l 
        with dissolve
       
        menu:
            "Cassandra":
                scene bg stage
                show c 1b at f12
                pause 0.3
                show t 1h at fr13

                t "Oh, you like the quiet type eh?"
                show t 1a
                c "..."
                s 1b "I still wanna know how she got those marks. Like, I thought it was a suicide attempt, but she said only Robin gave scars to herself."
                pause 0.1
                s 1i "Oh. That means someone else did that to her?"

                $temp = True
                $cassBio.loveUp()
                $ which_girl_1 = "Cassandra"

            "Robin":
                scene bg stage
                show r 1m at f12
                pause 0.3
                show t 1h at fr13

                t "Oh, you like the mysterious type eh?"
                r "I'm glad. I've been waiting for you for so, so long."
                show t 1a
                if which_girl_1 == "Robin":
                    s "Wow, I missed that the first time. I thought she was just being spooky!"
                else:
                    s "Wow! I guess if I picked her before that would've been a big clue about our past!"
                # chat tells her that's not what Robin said the first time, but the message vanishes
                $temp = True
                $robinBio.loveUp()
                $ which_girl_1 = "Robin"

            "Lichelle":
                show l 1l at f12
                pause 0.3
                show t 1h at fr13

                t "Oh, you like the dangerous type eh?"

                show t 1m
                l "Don't worry, Kylie! I'm only dangerous if you want me to be."
                ki "She winks. I'm not sure if I believe her."
                s 1b "I wonder if that was a good choice, now that I think about it."
                s "If she's not even going to be around for the second round, maybe there's another way to spend time with her."
                $temp = True
                $lichBio.loveUp()
                $ which_girl_1 = "Lichelle"

            "You on the menu, Tania?" if taniaPicked == False:
                t "We talked about this already, Kylie."
                ki "Jeez, I guess not."
                s "We did? Oh, I guess it was in the hallway before the show."
                $taniaPicked = True
                $taniaBio.loveUp()
                

            # END OF CHOICE

    scene bg stage with longFade

    stop music fadeout 3.0

    show t 1m at f12

    t "So let's talk a little bit about how this show works!"

    play music2 jazzNoodle

    $chat.addmessage(bar, "Sophie completely missing the affection screen still has progress")

    s 1a "Oh yes, let's. Makes for such an exciting stream!"

    $chat.addmessage(fizz, "Hey TwixtBar, you're right.")

    t 1o "Every woman involved in this show is, of course, 20 years old or older -- but not much older, right? -- and each has consented to the format. We're looking for love here, people!"

    $chat.addmessage(elsa, "Hey! Robin's 19. Tania should know that if they were friends.")

    s "Uh huh, yup. Yup yup. Love and stuff."

    t 1a "Kylie will go on a total of seven dates, one date each day of the week. Each Suitor will have two dates with her, and then one final date with whomever Kylie decides to smash!"

    $renpy.notify("I'm sorry")

    $chat.addmessage(beav, "Ha, I didn't notice Tania being pervy from the start.")

    s "... eww."

    t 2a "Each suitor has already selected a destination for the date. Meals and accommodations are on us, so hang on to your pocketbook Kylie!"

    k "How do we decide who goes first?"

    $chat.addmessage(fizz, "They should have a catfight.")

    t 2l "Glad you asked. To keep it fair, we'll go alphabetically again!"

    pause 0.1

    s "Hang on a minute. I just realized we didn't go alphabetically before. We went Cass, Robin and then Lichelle?"

    $chat.addmessage(crab, "tania sucks at alphabets")

    s "Guys, L comes before R, right?"

    $chat.addmessage(cake, "lol")

    k "What if we just don't click at all?"

    pause 1.0

    hide t at f12
    pause 0.4
    show r 1a at f12
    pause 0.1
    show c 1a at fl11
    pause 0.2
    show l 1a at fr13

    t "I'd say you don't have a chance at all!"

    s "Tell me about it, Tania."

    $chat.addmessage(elsa, "It's interesting how the things she says might mean something we don't expect.")

    t "Kylie, Cassandra, Robin, Lichelle, on behalf of everyone at One-Week Waifu, I wish you the best of luck! Let's see who makes it to the end!"

    k "Thanks, Tania."

    $chat.addmessage(bar, "Maybe we can get Tania's super erotic MP4 to play this time.")

    c 1p "..."

    r 1j "I would say the choice is obvious."

    $chat.addmessage(crab, "I still want her to step on me.")

    l 1n "Obviously it's gonna be me!"

    hide r at f12
    hide c at f11
    hide l at f13

    pause 0.3

    show t 1m at f12

    stop music2 fadeout 3.0

    t "Thanks for tuning in everybody!"

    scene bg near stage with longFade

    play music hallwayChats fadein 3.0
    show t 1a at f12

    t "Hey, Kylie. I hope that wasn't too stressful."

    $chat.addmessage(beav, "imagine if Kylie was aware she'd done this before")

    # darken screen, sophie time

    s 1j "Nothing's stress right now, um... Talia? Hang on. Tania."

    $chat.addmessage(fon, "I think Kylie could withstand something like that!")

    k "So Cassandra's first, huh? How are we supposed to communicate?"

    $chat.addmessage(crab, "Fluckin smoke signals lol")

    t 2o "Don'tcha worry about that. It was kinda tough on stage, but she's always got her phone with her and she has this shorthand app that helps her communicate."

    t 2a "And I have an idea for next time we're together."

    $chat.addmessage(elsa, "lol")

    k "I'm worried, though. I don't know anything about them, really. Is every contestant nervous like this?"

    s 1h "Kylie, hey girl. You're a god damn liar, me."

    $chat.addmessage(fizz, "Suppose Tania knows Kylie's aware of Cassandra?")

    s 1j "You know Cassandra and Robin both."

    s "So is the game just written with holes in it, or is Kylie lying? It's hard to tell sometimes."

    $chat.addmessage(crab, "Hey Fontaine does this gaem do this second go-through on purpose?")

    pause 0.1

    t 1q "Oh, god, yeah. Well, except for season seven. That girl was just a full-blown serial killer. Made the news and everything."

    $chat.addmessage(fon, "It plays out exactly the way it should, Crablegs. You're so introspective! ;)")

    k "Well, I'm... I'm..."

    menu:

        k "I should tell Tania I'm..."

        "In it for the cash":
            t 2j "You say that, but somebody this season is gonna get your heart. I just know it."
            

        "Looking for The One":

            t 1b "Oh, honey... you won't have to look. These women are all looking for you."
            ki "Tania's squeezing my hand, lightly. She's... genuinely sad, I think."
            ki "Maybe jealous?"

        "Just looking for a thrill.":
            t 1u "Oh. So you're a sex-pervert?"
            k "No, no, I just... I dunno. I guess I want some excitement in my life before I settle into a cubicle somewhere."
            t 1j "You never know. The cubicle may never come."
            $taniaBio.setLove(1)

            ki "Tania's got a dark streak, doesn't she?"
    # end menu

    t 1a "Don't be too nervous. When the show's finished, you'll never have to worry about money again."

    $chat.addmessage(cake, "answer was different this time Sophie")

    k "Looking forward to that!"

    t 1m "Yup. So... your first date is with Cassandra. You have a dressing room set up down the hall, and you have about an hour to get ready and get your nerves down."

    if taniaEnd > 0:
        $chat.addmessage(bar, "coulda been some sweet girl-on-girl in that room.")

    k "That might not be enough."

    $chat.addmessage(crab, "Shame.")

    if taniaEnd > 0:

        $chat.addmessage(fon, "Sophie, spoilers? Minor ones, but it's important for Crablegs to know.")
        pause 0.3
        s 1j "Heh heh, spoiled crab legs. Do it, Fontaine."
        pause 0.3

        $chat.addmessage(cake, "Fill us in lol")

        $chat.addmessage(fon, "Anyone who wants to know, check Kylie's Recaps. :P")

        $chat.addmessage(fon, "Scene seven :)")

        s "Okay. Hang on."

        pause 2.0

        $chat.addmessage(elsa, "Oh my god! What a sweet ending!")

        s 1n "Aww wow. That's nice."

        $chat.addmessage(crab, "HLA! HLA! HLA!")

        $chat.addmessage(cake, "Crab your wish is granted lol")

        s 1j "It's beautiful, actually. Everything's beautiful."

        $chat.addmessage(fizz, "Sophie, you good? Kind of spacey rn?")

        pause 0.1

        s "I'm good. Super good."

    k "I just don't know what I have to offer any of them."

    t 1i "Take some goddamn responsibility!"

    show t 1m

    ki "Her sudden tonal shift catches me off guard."

    k "Wha?"

    $chat.addmessage(beav, "lol meta")

    t 1o "You're not believing in yourself. Quit being a victim and be a Waifu!"

    k "I'm not a victim, I just... no. You're right!"

    $chat.addmessage(fizz, "Motivational Speaker Powers Engaged!")

    t 1n "Of course!"

    k "Yeah!"

    $chat.addmessage(elsa, "Yeah!")

    t 2n "Yeah!"

    s 1a "Getting them hype girl hours! I have no idea what I just said."

    $chat.addmessage(bar, "Sophie, never do that again. lol.")

    t "Any more questions?"

    $chat.addmessage(cake, "Yeah, Tania, what that mouth do XD XD")

    $chat.addmessage(fon, "Pity you didn't see what would've happened if you asked Tania out before. ;)")

    $temp = False

    while temp == False:
        s "What to say..."

        menu:

            "Seriously, what if I don't click with anyone?":
                t 1a "You will. You've got practice at this."

            "What if I want to end the date early?":
                t 1j "The dates will end when they end."

            "How much of this is staged?":
                t 1r "Nothing is real, really."
                s "How philosophical."

            "I have no questions.":
                $ temp = True

        # end of choice

    t 1m "Great. Go get ready, and hey Kylie? Listen. If you need to talk to anybody, I'm around. I've been on this show forever and I'll be happy to listen if you need anything."

    $chat.addmessage(elsa, "On this show forever. Are we in a time loop?")

    k "Thanks, Tania. That actually means a lot."

    t 1a "No problem. Now, go get ready. I guarantee your life is about to change!"

    scene bg hallway with dissolve

    ki "There's a lot on my mind as I make my way to the dressing room. These women, they're each alluring in their own way. I can definitely appreciate the three-bears strategy."

    $chat.addmessage(crab, "three bears and yet all women.")

    show c 1a at f13

    ki "Cassandra, the silent musician. Her eyes miss nothing, her features are so perfectly Greek, her bearing so beautifully coquettish."

    ki "I sense some deep well of feeling emanating from her, building up behind a dam of muteness."

    $chat.addmessage(cake, "hot AF")

    ki "It feels unfair, since I'm a superfan and all, but then maybe my fandom will drive her away?"

    s 1b "See? She's lying to Tania then. Such a faker."

    $chat.addmessage(beav, "what a cnut")

    s "Maybe she wants to appear impartial?"

    $chat.addmessage(elsa, "Beaver, don't be such a beaver.")

    show l 1a at f12

    ki "Lichelle, the fit girl with the wild smile and hungry eyes."

    ki "So fierce, so powerful, so dangerous. Some part of me has a tiny, tiny submissive side and Lichelle just... radiates the power to control."

    $chat.addmessage(cake, "hot. A. F.")

    s 1t "Wanna be tied up, Kylie?"

    show r 1a at f11

    ki "Robin, the shadow, graceful and statuesque. Her detachment paired with that accent lend her a ghostly, mysterious vibe that pulls at me, even now as I think about her."

    ki "Some part of me is afraid of her, but it's hard to express why."

    s 1b "Robin looks like someone I..."

    pause 0.2

    s 1c "Like someone I used to know."

    $chat.addmessage(fizz, "Now that you mention it... hey Elsa, doesn't Robin look like Louisa?")

    ki "They're all otherworldly in their way. I guess I should feel incredibly lucky that the women in front of me are all so desirable."

    stop music fadeout 3.0

    $chat.addmessage(elsa, "I've been thinking that the whole time. I was hoping not to draw attention to it.")

    scene bg stage with dissolve

    $chat.addmessage(fizz, "Sorry.")

    ki "I should focus on getting ready, though. I wonder what Cassandra has in mind?"

    $chat.addmessage(elsa, "Cassandra's planning to break my heart :(")

    scene bg black with dissolve

    pause 0.5

    s 1c "I know we just took a break guys, but I'm getting pretty tired. I'm gonna pee. You guys chill for a sec."

    $getHistory(8)
    $sceneNum = 9

    show image splashBRB at alphaFade

    pause 2.0

    $hideGui()

    hide image splashBRB at summonChat

    pause 1.0

    scene bg hallway:
        alpha 0.3

    show t 1h at f12

    #SFX - knocking
    t "{alpha=0.1}Hey, I'm getting dressed.{/alpha}"
    t "{alpha=0.1}Just a minute, dude!{/alpha}"

    show t 1d
    pause 1.0
    t "{alpha=0.1}Alright motherfucker, what do you want?{/alpha}"
    hide t at f12


    # ---------------------------------------------------------

    $renpy.notify("Sever the strings that bind us.")

    # ---------------------------------------------------------

    pause 0.5

    scene bg dressing with dissolve

    pause 0.5

    $showGui()

    pause 0.5

    # sophie with tiny pupils

    s 1j "Back. So, let's speed through these dates and get back to where we were?"

    
    $chat.addmessage(fizz, "You okay? Your eyes.")

    scene bg dressing with dissolve

    play music bedroom fadein 3.0


    ki "The dressing room is clean and simple. I'd like to stretch out for a nap, actually. The nerves have taken it out of me."

    #enable severance
    $severToggle()

    $chat.addmessage(cake, "pity that bed's for sleepin")

    ki "There are some clothes in the closet and... I'm a little disappointed. They're all white sundresses, basically cut the same way."

    $chat.addmessage(cake, "another new thing.")

    pause 1.0

    s 1t "Hey! That's different, right? Heh heh. There were different outfits before."

    $chat.addmessage(crab, "there's been a bunch of new things, Sophie, you just missed 'em") 
    
    $chat.addmessage(fon,"I think Sophie might be blissfully unaware rn ;)\n||--===>-")

    s 1i "Gasp, you guys! Was the game supposed to crash? Is this part of the plan?"

    $chat.addmessage(elsa, "I think so") 
    
    $chat.addmessage(bar,"cripes, Sophie, you dense.")

    s 1a "Oh, okay! Jeez, I wish they'd warned me a little bit. I just about said to hell with it and called it a night."

    s 1m "What a surprise! Ha!"

    #disable severance
    $severToggle()

    scene bg black with dissolve

    stop music fadeout 3.0

    ki "An hour passes like nothing, like time somehow folded in on itself."

    $chat.addmessage(fon, "I didn't want to ruin the surprise, it was hard to keep quiet :)")

    #SFX Knock

    ki "Dressed in the fluttery, pristine whites, I leap to my feet at the sound of a knock on the door."

    $chat.addmessage(elsa, "From lil' black dress, suit, and punky chick to Sunday school.")

    show l 1a at f12

    l "Hey babe. You ready to go?"

    play music lichelle fadein 3.0

    $chat.addmessage(cake, "gasp it's Elle!")

    ki "To my surprise, Lichelle stands before me, a little smile on her face."

    k "Oh, uh, sure? I guess?"

    $chat.addmessage(bar, "This is way different then.")

    l 1l "You were expecting someone else."

    s 1a "So was I!"

    $chat.addmessage(beav, "preach")

    k "Um... well, yeah. I thought Cassandra was first."

    l 1m "She is. Tania just rolled the hell out of her ankle about twenty minutes ago, so I'm here to whisk you off to the bar or whatever."

    $chat.addmessage(bar, "Tania no! I'll nurse you to health.")

    s 1b "Huh. Poor Tania. "

    k "Oh. Well... is that okay?"

    $chat.addmessage(fizz, "Sudden change of plans by the lady who no-showed last time.")

    l 1q "Should be. Why?"

    k "Well, I thought we weren't supposed to really talk until our date."

    l 1t "You worried I'll try to get in your panties in the car?"

    $chat.addmessage(crab, "dude. she doesn't play")

    ki "Fire floods into my face."

    l 1m "Haha! Don't worry babe, I'll wait my turn. Tania and I go way back and I know what she needs from the crew, so it makes sense that I go with."

    k "Okay. Well, uh, in that case, I'm ready whenever you are."

    $chat.addmessage(elsa, "Kylie's flustered.")

    l 1t "Cool. "

    ki "But her eyes betray her words."

    $chat.addmessage(fon, "My Elle is an apex predator :)")

    l "We going? Or you just gonna stand there and tempt me?"

    k "T-tempt you?"

    $chat.addmessage(cake, "hot in here")

    pause 1.0

    show l 1m 

    l "I'm just teasing. Get in the car, babe. At least give Cass and spooky-bitch a chance."

    pause 0.5

    l 1u "Based on the way you're breathing right now, it might already be too late." 
    
    $chat.addmessage(fizz,"Might be too late. Anyone else notice the affection levels?")

    s 1t "Wow. Heh heh."

    k "... don't get ahead of yourself."

    $chat.addmessage(beav, "Kylie standing her ground")

    ki "I say this, knowing full well I'm on jellied legs, grateful for the door frame around me."

    ki "Lichelle only smiles."

    $chat.addmessage(cake, "lol Kylie likes chocolate too")

    l 1j "Let's go. Cass'll be waiting."

    $chat.addmessage(fizz, "Don't be a racist, man.")

    s "This show makes me feel all... itchy. NO. Not that. Heh heh."

    $chat.addmessage(cake, "Hey fizz, won't you sYoAssTFUp. Nothing racist about that.")

    s 1a "Just imagine being as thirsty as Kylie seems to be and having all these dream girl archetypes trying to woo you..."

    $chat.addmessage(fizz, "Calling a black woman chocolate is racist, full stop.")

    s "... and also, to have to last through the whole week without acting on anything."

    $chat.addmessage(crab, "lol this gonna be good")

    $chat.addmessage(elsa, "Not real comfortable with this.")

    pause 0.5

    s 1b "Hey no fighting. I wanna see you boys rassle with my eyes, not my, uh, reading eyes."

    $chat.addmessage(fizz, "How's it not racist to refer to someone as chocolate?")

    $chat.addmessage(beav, "This kind of thing never ends well.")

    s 1j "I guess they're all reading eyes and seeing eyes."

    pause 0.5

    $chat.addmessage(cake, "1. chocolate is a color 2. it's a compliment 3. I'm black, shithead")

    pause 1.5

    $chat.addmessage(crab, "lolololololol")

    $chat.addmessage(fon, "Right, right, skin color. Humans have that. How boring. :( Let's not fight?")

    s 1b "Hey. Hey no."

    $chat.addmessage(fizz, "Just because you think it's okay doesn't")

    pause 0.4

    $getHistory(9)

    $chat.addmessage(sophie, "Chat is paused temporarily!")

    pause 0.5

    s 1c "I might cry. I might actually cry."

    s "No more fighting! We're gonna go on a nice date with a nice girl and that's that."

    s "Nice girl! Nice date! Okay?"

    pause 0.5

    $hideGui()

    stop music fadeout 3.0

    jump cassDate2
