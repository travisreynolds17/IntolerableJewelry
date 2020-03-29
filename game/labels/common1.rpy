label common1:
    # This one introduces Sophie as a streamer post seizure. She'll mention it, but kind of dreamily.

    # text

    scene bg load-string with fade

    pause 4.0

    scene bg black with fade
    pause 1.0

    

    show screen mainGameWindow
    show image splashTitle at alphaFade

    show screen loveScreen
    show screen leftBtnWindow

    show screen btnWindow

    # some chat front load. more later.
    python:
        chat.addmessage(unkn, "R13:14-15 | What? What? I can see?")
        chat.addmessage(cake, "New game?")
        chat.addmessage(shub, "#hentai?")
        chat.addmessage(crab, "#betterBe")
        chat.addmessage(egg, "Hi sweet Sophie")
        chat.addmessage(unkn, "hello")

    s "Hey everyone! Time for some sweet, sweet dating sim action, don't you think?"

    s "Oh that's right, we were getting ready to meet the host."

    s "So this game is supposed to be a visual novel about one of those dating reality shows. Kind of like The Unmarried Guy."

    s "A fan gifted it to me the other day and it couldn't come at a better time! Let's get started with Intolerable Jewelry!"

    scene bg near stage
    with fade

    s "Just like always guys, chat away! Fan club comments go straight to the top, so if you wanna support me join up!"

    s "Lemme see what you guys are saying."

    # start chattin - frontload it a bit
    python:
        chat.addmessage(fizz, "Yay, strim time!")
        chat.addmessage(fizz, "Hi Sophie, whatcha playin?")
        chat.addmessage(
            elsa, "Hey sister! Wait, is this a VN? A DATING SIM?!?")
        chat.addmessage(bong, "Date me Sophie lol I'll be your date")
        chat.addmessage(liv, "I love this game! <B")
        chat.addmessage(beav, "Jeez, why")
        chat.addmessage(fizz, "How are you feeling these days?")
        chat.addmessage(elsa, "Yeah are you still okay????")

    pause 1.0

    show screen chatterbox
    $chatIsOn = True
    pause 1.0

    s "Thanks, Fizz, how are you tonight? Did your test go okay?"

    s "Hi Liv! You know this game, too? No spoilers, okay? Also, I don't think we've met, welcome!"

    $chat.addmessage(liv, "It's my favorite game.")

    s "Oh my god, Bong, stop, you horndog. I'm gonna be here all night."

    $chat.addmessage(fizz, "Passed, barely. God.")

    s "Elsa, it's really just a dating sim. I kind of needed something to wind down."

    s "How am I doing? I'm doing fine, I guess. I haven't had a seizure since the last one."

    $chat.addmessage(bong, "u love me lol")

    s "I know, I know, I know. I'm funny."

    $chat.addmessage(bar, "really glad your OK. you gonna try to date again?")

    s "Seriously, I've never been better. I'm independent again, no seizures, I can stream all I want. And I can hang out with you guys!"

    $chat.addmessage(liv, "No spoilers, I can't wait to see if you can make it ;)")

    s "Thanks Twixt. I'm not ready to date in real life just yet, but I'm ready to date in this game we're gonna start playing right now!"

    $chat.addmessage(elsa, "don't date, practice self love")

    $chat.addmessage(bong, "weird u can see chat if I have window closed")
    $chat.addmessage(liv, "No, that's part of the game. Even chat can switch some windows.")
    # goes through title screen

    s "So we already named our protag, and of course I named her Kylie. I'm happy it let me choose to be a girl, by the way."

    $chat.addmessage(bar, "Why Kylie?")

    s "Wait, really, Liv? That's interesting! So now all of you get to know how I feel when I get behind on chat and have to catch back up, ha!"

    s "Twixt, it's because Kylie's my middle name. Everyone called me Kylie when I was just an egg."

    s "Okay, chat, I'll catch up with you later!"

    if chatIsOn:
        hide screen chatterbox
        $chatIsOn = False

    pause 1.0

    s "So... we've already got a love meter, it looks like?"

    $renpy.notify("Chat?")

    s "Could also be a life bar. That must be our four girls, right?"

    s "Got some traits on the right, it seems. So is that what each girl is like?"

    python:
        newComments = [

            [shub, "Four girls man."],
            [crab, "I like those odds."]

        ]
        chat.bulkMessage(newComments, 0)

    show t listen at center with moveinright

    t "Okay, are you ready? Everyone's waiting on you. No pressure, right?"

    # quick choice to show how choices work

    $ answer = False

    while answer == False:

        menu:
            "I'm so ready!":
                $ answer = True

            "I'm not ready!":
                t "Take a moment to get yourself together."
                pause 2.0

    # end of choice

    $chat.addmessage(beav, "READY")
    $chat.addmessage(elsa, "nooooooo")
    $chat.addmessage(bong, "red E")
    $chat.addmessage(egg, "What's this game?")
    $chat.addmessage(liv, "BEST game.")
    $chat.addmessage(fizz, "Not as good as Super Threatroid, not possible.")
    $chat.addmessage(beav, "Is it like Lass Effects?")
    $chat.addmessage(bong, "More like L'ASS EFFECTS")
    $chat.addmessage(elsa, "eww")
    $chat.addmessage(egg, "lol")
    $chat.addmessage(beav, "hahahha")
    $chat.addmessage(bar, "C'mon")
    $chat.addmessage(liv, "You're so funny, Oberbong.")
    $chat.addmessage(bong, "doin god's work ma'am")

    t "That's what I want to hear. Now, get in there and find love!"

    s "I love cheese. I love this game already!"

    scene bg stage with longFade

    s "Oh, I like this setup! I wonder what kind of people we're gonna meet?"

    $chat.addmessage(beav, "Assholes.")
    $chat.addmessage(fizz, "Tania's already best girl. 10/10")
    $chat.addmessage(elsa, "I like her hair")
    $chat.addmessage(liv, "I love Tania so much!")

    # checks chat
    if chatIsOn == False:
        show screen chatterbox
        $chatIsOn = True
    pause 1.0

    s "Oh wow, you guys like Tania. Fizz you can't name her best girl yet, we haven't even met the dates!"

    s "Oh, hey Beaver, how's your day? Assholes, sure. Probably."

    pause 0.25
    $chat.addmessage(beav, "Good, yours? How's you? Any moer seizures?")

    s "Yeah, I'm great. I'm happy, doing what I love with people I like!"

    s "Nope, no seizures. I guess my ex was causing them after all."

    pause 0.25
    $chat.addmessage(elsa, "Men are cancer.")

    s "Okay everyone, let's meet our dates!"

    if chatIsOn:
        hide screen chatterbox
        $chatIsOn = False
    pause 2.0

    t "Welcome back to One-Week Waifu! I'm your host Tania Van der Waal, yes that IS my real name, and before the break we were just about to introduce this season's Suitors!"

    ki "I'm trying to catch my breath. I don't think I've ever been this nervous, standing behind the cameras and waiting."

    $chat.addmessage(elsa, "I could never do a dating show.")

    ki "My heart is a blur at this point."

    t "Let's start with the introductions. We're going alphabetically just so nobody gets top billing, besides myself of course!"

    $chat.addmessage(bong, "probly just a casting couch situation neway.")

    show c with moveinright

    t "First off, you know her from the number one single on Quillboard's top 100 rock charts, 'Heroine', put your hands together for Cassandra Sanna!"

    $chat.addmessage(elsa, "Quillboard. Also, bong, grow tf up.")

    s "Ooh, she's a cutie."

    python:
        chat.addmessage(egg, "Sexy choker girl.")
        chat.addmessage(bong, "its true. they're all fake anyway")

    show c shy

    c "..."

    ki "I love her choker. Can't say I'm familiar with the song, though."

    $chat.addmessage(liv, "Ugh, no spoilers, but her choker :(")


    t "Generally I'd ask our Suitor to say a few words, but Cassandra... well, I'll let her tell you."

    show c speak

    ki "Cassandra lifts her hands and whirls them about in patterns I could never hope to translate, but know enough of to recognize as some form of sign language."

    s "Oh, is she deaf? Poor thing!"

    $chat.addmessage(bar, "She's a deaf musician. Wow.")
    $chat.addmessage(bar, "I wonder if there are any of those in reality nowadays?")
    pause 0.2
    $chat.addmessage(beav, "beethoven")
    $chat.addmessage(bar, "Nowadays.")
    pause 0.7
    $chat.addmessage(crab, "Bae-thoven")

    t "Anyone out there able to read ASL? No? Our next Suitor is, and she's offered to help us out."

    show c shy at midToLeft
    pause 0.5

    show r with easeinright
    pause 1.0

    t "May I present to you, everyone, the owner, proprieter and face of Ganymead Performing Arts, miss Robin Louisa Godrey!"

    $chat.addmessage(cake, "She looks like my sister")

    ki "Oh. Tall. Jesus."

    show r happy

    s "GOTH CHICK! I'm so onboard."

    ki "The woman looming statuesque before me is every inch of six-foot-three. Her hair is voluminous. She's like a goth-chick telephone pole."

    python:
        chat.addmessage(bong, "tell your sister come see me")
        chat.addmessage(cake, "my sister's an asshoel")
        chat.addmessage(liv, "Oh, Robin, I love you <B")

    s "I hear you, Kylie."

    t "Hi Robin!"

    show r speak

    r "Tania. The pleasure is mine, of course."

    $chat.addmessage(elsa, "What a mix of names Robin has. I wonder where she's supposed to be from.")

    ki "Her voice rings musically, with a hint of the tongue-tension common to eastern European nations. I can't quite pin down her accent, though."

    s "Tongue-tension. Chat, I'll let you guys pore over that one."

    t "Would you mind telling us what Cassandra said just now, Robin?"

    show r happy

    r "She said she's excited to be here."

    show c disap
    pause 0.25

    ki "From the expression on Cassandra's face I sort of doubt that's what she said."

    $chat.addmessage(shub, "She can hear can't talk")
    $chat.addmessage(crab, "Robin tryin to shit her up already")
    $chat.addmessage(elsa, "Trying to what?")

    s "Oh. I guess she's not deaf then. Maybe she's only mute? God, that would be rough in my line of work."

    ki "Robin takes a seat between Tania and Cassandra, crossing one endless leg over the other."

    show c

    t "So Robin, tell us a bit about what you do."

    show r speak

    r "I operate the local performing arts center, draga mea. Dear Cassandra lends her magic to our stage from time to time, but I..."

    $chat.addmessage(bar, "draga what now?")
    $chat.addmessage(fizz, "She's speaking Romanian. It means my darling, more or less.")

    show r happy

    ki "Her pause is a teasing one. From the wings I can almost feel her authority radiating outward; This is a woman used to controlling the conversation."

    $chat.addmessage(liv, "FizzyFizion you're so smart!")

    show r speak

    r "... I would say the thirsty come to me for water."

    t "That's awfully cryptic, Robin."

    show r happy

    r "Yes, it is."

    $chat.addmessage(bong, "bestGirl. #hentai")

    show c sad

    c "..."

    ki "Cassandra signs something toward them, and Robin chuckles a trill of a chuckle."

    $chat.addmessage(elsa, "Sophie, this isn't really an H-game, is it?")

    show r speak

    r "Cassandra says you should have expected secrets on the first episode, dear."

    $chat.addmessage(cake, "Nah, can't stream H on this site.")

    show r listen

    t "I see. Well, one thing that isn't a secret is our last Suitor's black belt. Everyone, give a warm welcome to MMA flyweight Lichelle 'Elegy' Carpenter!"

    hide t with moveoutright

    pause 1.0

    show l speak at right with moveinleft

    $chat.addmessage(bong, "ooh chocolate")

    l "Hey crew! How are good god you're tall."

    $chat.addmessage(elsa, "God you're gross @OberBong.")
    $chat.addmessage(liv, "Aw, Lichelle is so great!")

    show r happy

    ki "Robin only smiles, a gentle, delicious smile."

    s "Oh, we've got our tomboy! Wait. Which one is the nerd? Could we be dodging tropes today?"

    s "Also, I don't think the game has any sex, people. I couldn't stream it."

    $chat.addmessage(bar, "Pity")

    t "Hello Elle, how have you been? I was sorry to hear how your last fight went!"

    show l happy

    l "First off, I'm great. No shame in getting choked out by the champ."

    l "Might've done better if my cutwoman had been there, though."

    show l listen

    $chat.addmessage(unkn, "Pronounced like El")
    $chat.addmessage(egg, "What's a cutwoman?")

    t "Yeah... I'm sorry about that. I wish I could've gone."

    show l speak
    $chat.addmessage(fizz, "Tania is a TV host and a cutwoman. Pretty wild.")

    l "Anyway."

    $chat.addmessage(bar, "Liv, you like everybody.")

    l "I'm just living life. I'm not in a training camp right now so I can eat what I want and make time to visit a TV show or two."

    $chat.addmessage(fizz, "A cutwoman or a cutman is there to stop a pro fighter's bleeding between rounds.")
    $chat.addmessage(liv, "I love them. Wow, Fizz! Smarty smart. Handsome too?")

    t "Well, we're happy to have you here on One-Week Waifu. Now, before we meet our eligible bachelorette, I'd like each of you to let us know what being here means to you. And be honest!"

    show c speak
    pause 0.10
    show l listen

    c "..."

    $chat.addmessage(bong, "think Liv might be catfishin")

    show r speak

    r "Cassandra says, to be honest, she's here to promote her new album."

    $chat.addmessage(egg, "She can't talk, could still be a mumble rapper.")

    ki "Cassandra nods, but her smile is oddly forlorn. I can't help but wonder who let her on stage without an interpreter she can trust."

    $chat.addmessage(elsa, "How awful. The only person speaking for her isn't being honest.")

    l "I'm here because Tania's my girl and she asked me to. She keeps trying to set me up on dates anyway, so I might as well be on TV for it."

    s "I admire their honesty if nothing else."

    s "Hey Bong, be nice."

    $chat.addmessage(bong, "sorry Liv")
    $chat.addmessage(liv, "Nothing to forgive. I'll prove I'm not catfishing. Check private chat.")

    r "I am here in search of one perfect soul, my dears."

    ki "Tania's laughing, but there's an edge of nervousness to it. I can't blame her. Robin seems to take her goth attitude very seriously."

    t "Well, if you're lucky that perfect soul is standing right on the other side of the camera."

    $chat.addmessage(bar, "Robin lives her gimmick.")

    s "She talkin' bout ME."

    t "Everyone welcome this season's single lady! Come on out, Kylie!"

    $renpy.notify("Chat!")

    ki "Okay. Breathe. It's my time, right? My nerves sing like there are little knives dancing upright on my skin."

    ki "I make my way to the stage, fully aware of the eyes trained on me. Cassandra's side-eye, Lichelle's direct gaze, Robin's --"

    $chat.addmessage(shub, "Robin's belly button.")

    ki "Well, Robin is looking past me, to the stage doors. Detachment must be part of her schtick."

    $chat.addmessage(fizz, "God, I'm gonna have to watch every stream so I don't miss anything.")
    $chat.addmessage(fizz, "Would've done it anyway :D")

    t "Welcome to the show, Kylie!"

    k "Thanks, uh, thank you. It's good to be here."

    t "It is! So, tell us a little bit about yourself?"

    $chat.addmessage(bong, "holy shit guys, Liv is for real.")

    k "Sure. Okay, um, I just graduated with a bachelor's in graphic design and I've been putting out feelers to get my career going."

    s "Ooh, I'm an artist. Nice."

    $chat.addmessage(crab, "oh yeah Bong? what's that mean?")
    $chat.addmessage(elsa, "Oh wow graphic design! Like me!")

    t "That's great! So what made you interested in coming on our show?"

    k "Well, I've been watching since season two..."

    $chat.addmessage(bong, "video chat she's hot af.")

    scene bg stage with fade

    show t

    t "Wow, that's some story! So, we know you were just off camera while our Suitors introduced themselves."

    $chat.addmessage(fizz, "... really?")
    $chat.addmessage(egg, "He's messing with us. Let's just enjoy Sophie's stream.")

    hide t with dissolve
    show c at left
    show r
    show l at right
    with dissolve

    t "Given what you heard from them, who has your attention?"

    $chat.addmessage(cake, "brb.")

    s "So it's a dating game, sure, but don't you think it's weird for one person to meet all these others and expect to fall in love with one in a week?"

    s "I think I'd have a hard time with that. So... hey chat. Who do we like?"

    $chat.addmessage(elsa, "If I liked girls, probly the fighter. Imagine holding that person in your arms after a tough loss or a great win :)")
    $chat.addmessage(elsa, "But she might be too aggressive. Robin, then.")

    # show chat
    if chatIsOn == False:
        show screen chatterbox
        $chatIsOn = True
    pause 1.0

    s "Wow you guys are talkative today. Hi Shub, Crab, and Cake! My three amigos."

    $chat.addmessage(shub, "Hola, mamacita.")
    $chat.addmessage(crab, "'allo Ms. K")

    s "Hi TweeterEgg! How are you? Did you see what all these ladies said before?"

    $chat.addmessage(fizz, "Cassandra's mysterious. Like it.")

    s "Oh, Elsa, you're such a romantic. Bong, I'm not on the list you perv. Don't any of these cuties get your attention?"

    $chat.addmessage(bar, "Bong is off gallavanting. .")

    s "Fizz is all about some Cassandra, Twixt likes Robin. No love for Lichelle guys? I mean she's a badass, she could protect me if I needed it."

    s "Which I don't, just so you know."

    $chat.addmessage(egg, "we got a badass over here")

    $renpy.notify("Not all decisions matter in the grand scheme of things.")

    s "I guess my answer here won't decide anything major yet, so I'm gonna say..."

    # choice

    $temp = False

    while temp == False:

        menu:
            "Cassandra":
                scene bg stage
                show c with dissolve

                t "Oh, you like the quiet type eh?"
                c "..."
                $chat.addmessage(fizz, "Good choice.")
                s "I'm super curious how this is gonna play out if she can't talk. Like, maybe I can learn sign language in a week?"
                $temp = True
                $loveCass += 1
                $ which_girl_1 = "Cassandra"

            "Robin":
                scene bg stage
                show r with dissolve

                t "Oh, you like the mysterious type eh?"
                r "I see. Perhaps you have my interest, as well, papillon."
                $chat.addmessage(bar, "Butterfly? Right?")
                s "Oh my god she speaks French! The goth chick called me butterfly! Guys. Chat. We did it. We won."
                $temp = True
                $loveRobin += 1
                $ which_girl_1 = "Robin"

            "Lichelle":
                scene bg stage
                show l with dissolve

                t "Oh, you like the dangerous type eh?"
                l "Don't worry, Kylie! I'm only dangerous if you want me to be."
                ki "She winks. I'm not sure if I believe her."
                $chat.addmessage(elsa, "I dunno about BDSM with a trained fighter though.")
                $temp = True
                $loveLich += 1
                $ which_girl_1 = "Lichelle"

            "You on the menu, Tania?" if loveTania == 0:

                t "Oh, no, that would make filming next season pretty tough!"
                $chat.addmessage(egg, "But she has a progress bar, so...")
                t "But I'm flattered!"
                $loveTania += 1

            "Just one?" if groupThing == False:
                s "Rawr!"
                t "Calm down girl, the show is Waifu, singular."
                t "But I admire your optimism!"
                python:
                    newComments = [
                        [elsa, "Sophie. Hon."],
                        [egg, "Yes!"],
                        [shub, "Hell yeah"],
                        [cake, "swoon"]
                    ]
                    chat.bulkMessage(newComments, 0)
                $groupThing = True

        # END OF CHOICE
        show screen loveScreen

    scene bg stage
    show t with dissolve
    t "So let's talk a little bit about how this show works!"

    t "Every woman involved in this show is, of course, 20 years old or older -- but not much older, right? -- and each has consented to the format. We're looking for love here, people!"

    $chat.addmessage(elsa, "Me too, Tania, me too. Preach girl.")

    s "Love, huh? Well... not me. But maybe."

    t "Kylie will go on a total of seven dates, one date each day of the week. Each Suitor will have two dates with her, and then one final date with whomever Kylie decides is worthy of her affection!"

    $chat.addmessage(egg, "sounds complex")

    s "That's awfully objectifying. And short-sighted? How are we gonna pack enough drama into one week?"

    $chat.addmessage(crab, "is it objectifying tho? consented, right? nobody held a gun to their heads")

    t "Each suitor has already selected a destination for the date. Meals and accommodations are on us, so hang on to your pocketbook Kylie!"

    $chat.addmessage(elsa, "Just because it's consented to doesn't mean it isn't objectifying.")

    k "How do we decide who goes first?"

    t "Glad you asked. To keep it fair, we'll go alphabetically again!"

    $chat.addmessage(crab, "not trying to offend")

    k "What if we just don't click at all?"

    $chat.addmessage(shub, "then the game can't proceed lololol")

    pause 2.0

    hide t with dissolve
    show c at left
    show r
    show l at right
    with dissolve

    t "I'd say the chance of that is practically nonexistent!"

    s "I mean, I guess we have to click or the game wouldn't work."

    s "Oh yeah Shub, exactly."

    $chat.addmessage(egg, "Crop of cuties though. Like a little bag of oranges.")

    t "Kylie, Cassandra, Robin, Lichelle, on behalf of everyone at One-Week Waifu, I wish you the best of luck! No matter who Kylie chooses, you'll make the cutest couple wherever you go!"

    s "TOO MUCH SUGAR!"

    $chat.addmessage(cake, "oranges wtf .... oh i getcha")

    k "Thanks, Tania."

    c "..."

    r "I would say the choice is obvious."

    $chat.addmessage(bar, "Obviously, my dark princess! STEP ON ME GODDESS!")

    l "Obviously it's gonna be me!"

    $chat.addmessage(elsa, "lol weirdo")

    t "Thanks for tuning in everybody!"

    scene bg near stage
    show t
    with fade

    $chat.addmessage(fizz, "Buncha freaks in here and it's great.")

    pause 1.0

    t "Hey, Kylie. I hope that wasn't too stressful."

    k "No more than the last time I was in front of three dream girls and thousands of fans."

    $chat.addmessage(fizz, "I'm really curious about Cassandra. Why's Robin mistranslating? Liv was sad about her choker. What's up with that?")

    # darken screen, sophie time

    s "Chat, I don't know about you, but I'm ready for a hot date. Let's take a sec to catch up though. Um..."

    $chat.addmessage(elsa, "Cassandra's in a cult. No doubt. Vow of silence. For sure.")

    $chat.addmessage(crab, "Liv and Bong been awful quiet")

    # checks chat

    s "I know guys, I'm pretty curious about Cassandra. Like, are we gonna find out why she can't talk? Or like... maybe she has some dark secret and she chooses not to speak."

    $chat.addmessage(egg, "Elle's my type unless she has man muscles under that shirt.")

    s "Elsa says Cassandra's in a cult with a vow of silence. Could be, could be!"

    s "Tweeter is interested in Elle, but wants to see her with her shirt off to find out if she has man-muscles. Uh-huh. I'm sure that's all."

    $chat.addmessage(shub, "Tania's right there. She got richgurl money, bet. Lively.")

    s "Shub's disappointed Tania's not available. She's got lots of energy, I agree. Her last name sounds like her parents are rich, right, right."

    s "Beaver, what about you? You went quiet on us."

    pause 1.0

    $chat.addmessage(beav, "sorry, was eating soup. um, I like them all. I'd do a Devil's Pentagon with them.")

    $chat.addmessage(fizz, "A who now?")

    s "Hey you never know. Never know with dating sims anymore. We might could make a foursome happen, but I mean, do we really want that? I feel like the logistics would make it tough to pull off."

    s "Like Robin's really tall and Lichelle's kinda short, right?"

    $chat.addmessage(beav, "tell ye when yer older")

    s "Actually, let's not go down this rabbit hole just yet."

    # back to game

    k "So Cassandra's first, huh? How are we supposed to communicate?"

    $chat.addmessage(crab, "Solid question, Kylie. Kylie best girl.")

    t "Don'tcha worry about that. She's always got her phone with her and she has this shorthand app that helps her communicate."

    t "And I have an idea for next time we're on stage."

    $chat.addmessage(crab, "see I thought about a phone but can't really show the camera")

    k "I'm worried, though. I don't know anything about them, really. Is every contestant nervous like this?"

    $chat.addmessage(elsa, "I'd be a nervous wreck.")

    t "Oh, god, yeah. Well, except for season four. That dude was just a full-blown sex-pervert. He didn't care who he was with."

    s "I wanna see that season."

    $chat.addmessage(crab, "I wanna BE that season")
    $chat.addmessage(shub, "mah boi")

    t "Just think about why you're really here. It'll come to you."

    $chat.addmessage(elsa, "Tania's so comforting.")

    k "Well, I'm... I'm..."

    s "Hmm... what to say?"

    $chat.addmessage(fizz, "Choice alert!")

    menu:

        k "I should say I'm..."

        "In it for the cash":
            show t speak
            t "I understand that. At least give us a good show though. This is our first all-female season and we're counting on the horny 18-35 male-fantasy demographic."
            s "That means she's counting on you guys, Crab, Shub, Cake and Bong."
            $chat.addmessage(bar, "Shit I'm 36.")

        "Looking for The One":
            show t sad
            t "Oh, honey..."
            $chat.addmessage(elsa, "Her sad face! :(")
            t "Just don't get your hopes up, okay? Don't ever let my producer hear I said this, but we really are just a reality show. No one ever meets the one here."
            ki "Tania's squeezing my hand, lightly. She's... genuinely sad, I think."
            $chat.addmessage(fizz, "Tania must have been a contestant at one point.")

        "Just looking for a thrill.":
            show t flirty
            t "Oh. So you're a sex-pervert too?"
            python:
                newComments = [
                    [bar, "yep"],
                    [elsa, "100%"],
                    [shub, "yes"],
                    [fizz, "True"],
                    [beav, "yup"],
                    [egg, "yup"]

                ]
                chat.bulkMessage(newComments, 0.6)

            k "No, no, I just... I dunno. I guess I want some excitement in my life before I settle into a cubicle somewhere."
            show t happy
            t "I respect your honesty, kiddo."

            ki "Kiddo? She's like a year older than me, max."
    # end menu

    show t
    t "Don't be too nervous. When the show's finished, you'll have a nice payout in your pocket no matter what happens."

    k "Looking forward to that!"

    t "Yup. So... your first date is with Cassandra. You have a dressing room set up down the hall, and you have about an hour to get ready and get your nerves down."

    $chat.addmessage(fizz, "YES!")

    k "That might not be enough."

    t "You'll be okay. Remember, the worst thing that could possibly happen is nothing, right?"

    $chat.addmessage(bar, "Said that to my college girlfriend, too.!")

    k "I guess so."

    t "You guess correctly! Now, we'll have a car ready to take you to the date destination when you're ready. The crew will be there filming, of course, and we'll have security on site to make sure nobody tries to get involved."

    $chat.addmessage(elsa, "So Kylie's going to get chauffered everywhere!")

    k "I remember season 6. Hey, now that I think about it... I knew I'd seen Lichelle before!"

    s "Ooh, plot twist!"

    $chat.addmessage(beav, "Elle kickin' ass for love!")

    show t happy

    t "Yup, she used to work security for us."

    ki "I remember that. There was a pick-up artist guy at the bar the couple went to, who wouldn't leave them alone. Lichelle had been about as gentle as a person can be when choking someone out with her thighs. I have to ask her about that."

    t "Any more questions?"

    $chat.addmessage(fizz, "Either that's a triangle choke or we need to be watching season six.")
    $chat.addmessage(cake, "damn. hot in here.")

    $temp = False
    $haveAsked = False  # Just a variable to signify whether you've already asked a question

    while temp == False:
        if haveAsked:
            t "Anything else?"
        else:
            k "What should I ask...?"

        menu:

            "Seriously, what if I don't click with anyone?":
                $haveAsked == True
                show t disap
                t "Sometimes people just don't mesh. That's one reason we found such wildly different women, so most tastes would be accounted for."

                t "Outside wild kinks, I guess."

                t "Point is, just go with your heart. If you like one of the Suitors after the first date, go after her hard on the second. Be yourself, be... I dunno. Honest."

            "What if I want to end the date early?":
                $haveAsked == True
                t "You're contractually obligated not to, so... even if you don't like the date, you have to get through it. Just try to make it interesting for the audience if that happens."

            "How much of this is staged?":
                $haveAsked == True
                t "I'd guess it's staged to the same degree real life is staged. Nobody's fully authentic on the first two dates, right?"

            "I have no questions.":
                $haveAsked == True
                $ temp = True

        # end of choice

    $chat.addmessage(fizz, "I love Q and A time. Hey Sophie, did you notice chat wasn't working just now?")

    t "Great. Go get ready, and hey Kylie? Listen. If you need to talk to anybody, I'm around. I've been on this show since day one and I'll be happy to listen if you need anything."

    $chat.addmessage(unkn, "R13:14-15")

    s "Tania's nice. I bet the real hosts of these shows are nothing like her."

    k "Thanks, Tania. That actually means a lot."

    t "No problem. Now shoo, go get your game face on and knock Cassandra's socks off!"

    hide t at moveoutright

    pause 1.0

    s "Oh, chat was busted? Well, we'll add that to the busted subscribe button. Is everything cool now?"

    $chat.addmessage(shub, "Aye!")

    s "Cool. Let's move on. I'm excited guys are you excited?"

    $chat.addmessage(egg, "like an electron in a heightened state!")
    $chat.addmessage(bar, "sleepy, but yea")

    pause 0.5

    scene bg hallway with dissolve

    ki "There's a lot on my mind as I make my way to the dressing room. These women, they're all alluring in their own way. I can definitely appreciate the three-bears strategy."

    $chat.addmessage(beav, "three bears. Robin's too hot. Cass too cold. Elle just right!")

    show c with dissolve

    ki "Cassandra, the silent musician. Her eyes miss nothing, her features are so perfectly Greek, her bearing so beautifully coquettish."

    $chat.addmessage(fizz, "I wonder if any of her music is written for the game.")
    ki "I feel some deep well of empathy emanating from her, building behind a dam of muteness."

    show l with dissolve

    ki "Lichelle, the fit girl with the wild smile and hungry eyes. So fierce, so powerful, so dangerous. Some part of me has a tiny, tiny submissive side and Lichelle just... radiates the power to control."

    $chat.addmessage(elsa, "I can relate to that.")

    show r with dissolve

    ki "Robin, the shadow, graceful and statuesque. Her detachment paired with that accent lend her this ghostly, mysterious vibe that pulls at me, even now as I think about her. Some part of me is afraid of her, but it's hard to express why."

    $chat.addmessage(bar, "I mean, that's a chick who's in control of her space. Don't fluck with a woman like that.")
    $chat.addmessage(cake, "preach. also, how submissive we talkin, @ElsaLater?")

    ki "They're all otherworldly in their way. I guess I should feel incredibly lucky that the women in front of me are all so desirable."

    $chat.addmessage(elsa, "What about Tania!?!?!")
    scene bg stage with dissolve
    $chat.addmessage(elsa, "Nowhere near enough to submit to Internet edgelords.")

    ki "I should focus on getting ready, though. I wonder what Cassandra has in mind?"

    scene bg black with dissolve

    s "Oh my god, me too. Hey chat, how we doin? How's everyone feeling?"

    $chat.addmessage(cake, "Shame b/c I'm dom AF")

    # checks chat

    s "Hm. I agree, everyone, it's gonna be a tough choice. Like, I like how Robin's all spooky and gothic. She's like a playhouse owner, too, so she's probably good at business and stuff."

    s "Bong, you pick a girl yet?"

    $chat.addmessage(elsa, "Need some dude options!")
    $chat.addmessage(egg, "he picked Liv")

    pause 0.5

    s "I guess they did both vanish at once. Probably just coincidence, right?"

    $chat.addmessage(bar, "prob!")

    s "Elsa, I guess the game's really supposed to appeal to like... stereotypical weeb guys, so there aren't any boys to date in this one. Next time, we'll find one that's all guys to play, how's that sound?"
    $chat.addmessage(shub, "Gross! We need to date ALIENS instead.")

    s "Shub, that's okay, we have to make sure everyone has something that works for them. Now that I'm doing better, we'll find a Martian to mate with at some point."

    $chat.addmessage(egg, "Scandalous. Also, all these ladies seem great in their own way!")

    s "Tweeter, you're right. It's like... I feel like it'll be hard to really decide who we like if everyone's good. We only have seven days!"

    s "Oh my god. Seven days to find love. Or hit that. Right Fizzy?"

    $chat.addmessage(fizz, "I'm a lover, not a hitter!")
    $chat.addmessage(crab, "or a quitter!")

    s "Okay guys, I'm gonna take a short break. You guys talk amongst yourselves for a bit!"

    pause 1.0

    show image splashBRB at alphaFade

    python:
        newComments = [

            [bar, "I'm not sure I'm into this game."],
            [elsa, "I think I am. It's only been a few minutes."],
            [fizz, "I'm just in it for Sophie."],
            [cake, "Crushin hard bruv"],
            [shub, "^^^"],
            [elsa, "Pretty obvious"],
            [fizz, "NO"],
            [crab, "This game sux"],
            [liv, "NO"],
            [shub, "Hey, Liv's back"],
            [liv, "This is the best game."],
            [cake, "So did you really private chat with Bong?"],
            [liv, "Yes. He's a pretty boy."],
            [elsa, "Is he? I kind of imagined him as a greasy neckbeard."],
            [liv, "No."],
            [egg, "Bong said you were HAWT af"],
            [liv, "Oh, I don't know about that."],
            [liv, "Sophie, where'd you go? You need to play!"]


        ]
        chat.bulkMessage(newComments, 0.75)

    pause

    hide image splashBRB at alphaFade

    pause 1.0

    s "Okay, I'm back! So, let's get this date!"

    $chat.addmessage(crab, "Were you peeing")

    s "Oh, welcome back Liv."

    s "If you have to know, yes I was peeing. You guys are freaks."

    $chat.addmessage(fizz, "Gross.")

    scene bg dressing with dissolve

    ki "The dressing room is clean and simple. I'd like to stretch out for a nap, actually; the nerves have taken it out of me."

    $chat.addmessage(beav, "Neat. Streaming while streaming.")

    ki "There are some clothes set aside in the closet. One of the producers and I talked about what I might wear to the dates beforehand."

    $chat.addmessage(elsa, "eww.")
    $chat.addmessage(egg, "l0l")
    $chat.addmessage(bar, "nice")

    ki "So I have a simple black dress with matching shoes for one date, a jeans and teddy bear tee for another, and then a smart blue pantsuit with emerald blouse."

    ki "The dress is awfully revealing. It feels like a silky puddle of nothing in my hands."

    ki "I like the jeans and bear shirt more than I want to admit, but it seems too casual. Laundry-day casual."

    ki "The pantsuit is stylish, but I think a suit requires a certain power attitude. Not me, not in the least."

    s "So the game wants us to guess who might like which outfit?"

    $chat.addmessage(elsa, "Little black dress on first date? Nope.")


    s "Either that or this is just filler. Here in the real world I wouldn't make this choice without knowing where we're going."

    $chat.addmessage(fizz, "Jeans and tank is too casual.")
    $chat.addmessage(cake, "pantsuit nope.")

    s "Am I wearing a little black dress to go ice skating? Hey Bong, what do you think?"

    $chat.addmessage(liv, "I want to see you in the little dress.")

    s "Exactly, cake. Not feeling a pantsuit for Cassandra."

    menu:


        ki "So, for Cassandra's date I should wear..."

        "Little Black Dress":
            ki "I think she might like something simple. She's a musician, and a successful one, so she might take us somewhere classy?"
            $chat.addmessage(liv, "Yay!")
            $outfitCurrent = "Dress"
            $outfitBlackDress += 1

        "Jeans and Tee":
            ki "She's a rock star, so I think she might like a punkish getup. I feel good about this."
            $chat.addmessage(crab, "Seems legit. Tear a whole in the jeans.")
            $chat.addmessage(fizz, "*hole.")
            $outfitCurrent = "Jeans"
            $outfitJeans += 1

        "Pantsuit":
            ki "Something modern and classy. Granted, I doubt it'll match Cassandra's style, but contrast is cute sometimes."
            $chat.addmessage(shub, "I'd kinda like to see that combo.")
            $outfitCurrent = "Pantsuit"
            $outfitPantsuit += 1

    # endchoice

    scene bg black with dissolve

    ki "An hour passes like nothing. Like time somehow folded in on itself."

    $chat.addmessage(egg, "Almost like it's a whole new scene.")

    scene bg hallway with dissolve

    show t with dissolve

    t "Hey, Kylie, looking great!"

    s "I bet she would have said that no matter what we picked."

    $chat.addmessage(shub, "bet")

    k "Thanks. Is the car here? I want-"

    t "Yup! Let's go!"

    $chat.addmessage(elsa, "Tania's in a hurry!")

    k "Oh? You're coming with?"

    $chat.addmessage(egg, "gotta make a show.")

    t "Yeah. We'll actually film a little coverage track, maybe interview the staff about the place you're going. Some b-roll footage, maybe."

    k "Oh."

    $chat.addmessage(cake, "I saw a lot of b-roll in my porn director days")

    t "Let's go!"

    $hideGui()

    # collect chat history in appropriate variable.
    $getHistory(0)

    scene bg black with fade

    

    jump cassDate1
