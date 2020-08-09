label common1:
    # This one introduces Sophie as a streamer post seizure. She'll mention it, but kind of dreamily.

    # text


    scene bg load-string with fade

    pause 4.0

    play music jazzNoodle fadein 3.0

    scene bg black with fade
    pause 1.0

    show screen mainGameWindow
    show image splashTitle at alphaFade

    show screen leftBtnWindow

    # some chat front load. more later.
    python:
        chat.addmessage(unkn, "R/BG13:14-15 | What? What? I can see?")
        chat.addmessage(cake, "New game?")
        chat.addmessage(shub, "#hentai?")
        chat.addmessage(crab, "#betterBe")
        chat.addmessage(egg, "Hi sweet Sophie")
        chat.addmessage(unkn, "hello")

    s 1a "Hey everyone! Time for some sweet, sweet dating sim action, don't you think?"

    s 1m "So this game is supposed to be a visual novel about one of those dating reality shows. Kind of like The Unmarried Guy."

    s "And you can super tell it's still in beta. Let's get started with One Week Waifu!"

    #sfx: game button confirm sound
    stop music fadeout 2.5

    scene bg black with longFade

    pause 1.5

    scene bg near stage
    with longFade

    play music hallwayChats fadein 1.5

    s 1m "Just like always guys, chat away! Fan club comments go straight to the top, so if you wanna support me join up!"

    s "Lemme see what you guys are saying."

    # start chattin - frontload it a bit
    python:
        chat.addmessage(fizz, "Yay, strim time!")
        chat.addmessage(fizz, "Hi Sophie, whatcha playin?")
        chat.addmessage(
            elsa, "Hey sister! Wait, is this a VN? A DATING SIM?!?")
        chat.addmessage(bong, "Date me Sophie lol I'll be your date")
        chat.addmessage(fon, "I love this game! <B")
        chat.addmessage(beav, "Jeez, why")
        chat.addmessage(fizz, "How are you feeling these days?")
        chat.addmessage(elsa, "Yeah are you still okay????")

    pause 1.0

    show screen chatterbox
    $chatIsOn = True
    pause 1.0

    s "Thanks, Fizz, how are you tonight? Did your test go okay?"

    s 1a "Hi Fontaine! You know this game, too? No spoilers, okay? Also, I don't think we've met, welcome!"

    $chat.addmessage(fon, "It's my favorite game.")

    s 1k "Oh my god, Bong, stop, you horndog. I'm gonna be here all night."

    $chat.addmessage(fizz, "Passed, barely. God.")

    s 1m "Elsa, it's really just a dating sim. I kind of needed something to wind down."

    s "How am I doing? I'm doing fine, I guess. I still have my card, too."

    $chat.addmessage(bong, "u love me lol")

    s 1q "Yup, on the straight and narrow!"

    $chat.addmessage(bar, "really glad your OK. you gonna try to date again?")

    s 1a "Seriously, I've never been better. I'm independent again, no jewelry, I can stream all I want. And I can hang out with you guys!"

    $chat.addmessage(fon, "No spoilers, I can't wait to see if you can make it ;)")

    s "Thanks Twixt. I'm not ready to date in real life just yet, but I'm ready to date in this game we're gonna start playing right now!"

    $chat.addmessage(elsa, "don't date, practice self love")

    $chat.addmessage(bong, "weird u can see chat if I have window closed")
    $chat.addmessage(fon, "No, that's part of the game. Even chat can switch some windows.")

    s "So we already named our protag, and of course I named her Kylie. I'm happy it let me choose to be a girl, by the way."

    $chat.addmessage(bar, "Why Kylie?")

    s 1r "Wait, really, Fontaine? That's interesting! So now all of you get to know how I feel when I get behind on chat and have to catch back up, ha!"

    s 1a "Twixt, it's because Kylie's my middle name. Everyone called me Kylie when I was just an egg."

    s "Okay, chat, I'll catch up with you later!"

    s "And we're going to get started!"

    $renpy.notify("Chat?")

    pause 1.0

    ki "I'm nervous. Of course I am. I've never been on a TV show before."

    ki "There's a lot going on, but I found a hallway to hide away from the production assistants and makeup team for a minute."

    show t 1a at f12 

    t "Hi Kylie!"

    s 1t "Ooh, I like her outfit." 
    
    $chat.addmessage(bong,"hips girl")

    ki "... it was only a matter of time before Tania found me."

    t 1j "Hiding out?"

    k "Yes. Yes I am."

    t 1q "I'm here for you. Anything you need, if it takes less than two minutes, I've got you covered."

    ki "I'm too nervous to make a sex joke." 
    
    $chat.addmessage(fizz,"That's never happened... yes.")

    ki "That's never happened before."

    k "I'm good. I'm good!"

    t 1m "Yes you are! Nothing to worry about hon, not a bit."

    t "So. You ready to go find love or whatever?"

    # quick choice to show how choices work

    $ answer = False

    while answer == False:

        menu:
            "I'm so ready!":
                $ answer = True

            "I'm not ready!":
                t 1a "Take a moment to get yourself together."
                pause 2.0

    # end of choice

    $chat.addmessage(beav, "READY")
    $chat.addmessage(elsa, "nooooooo")
    $chat.addmessage(bong, "red E")
    $chat.addmessage(egg, "What's this game?")
    $chat.addmessage(fon, "BEST game.")
    $chat.addmessage(fizz, "Not as good as Super Threatroid, not possible.")
    $chat.addmessage(beav, "Is it like Lass Effects?")
    $chat.addmessage(bong, "More like L'ASS EFFECTS")
    $chat.addmessage(elsa, "eww")
    $chat.addmessage(egg, "lol")
    $chat.addmessage(beav, "hahahha")
    $chat.addmessage(bar, "C'mon")
    $chat.addmessage(fon, "You're so funny, Oberbong.")
    $chat.addmessage(bong, "doin god's work ma'am")

    t 1m "That's what I want to hear. Now, get in there and find love!"

    k "Or whatever?"

    t 1j "Now you're learning."

    s 1a "I love cheese. I love this game already!"

    stop music fadeout 2.0

    hide t

    pause 1.0 
    scene bg stage with longFade

    play music cheerfulGuitar fadein 2.0

    s 1a "Oh, I like this setup! I wonder what kind of people we're gonna meet?"

    $chat.addmessage(beav, "Assholes.")
    $chat.addmessage(fizz, "Tania's already best girl. 10/10")
    $chat.addmessage(elsa, "I like her hair")
    $chat.addmessage(fon, "I love Tania so much!")

    # checks chat
    pause 1.0

    s "Oh wow, you guys like Tania. Fizz you can't name her best girl yet, we haven't even met the dates!"

    s 1m "Oh, hey Beaver, how's your day? Assholes, sure. Probably."

    pause 0.25
    $chat.addmessage(beav, "Good, yours? How's you? Any moer seizures?")

    s "Yeah, I'm great. I'm happy, doing what I love with people I like!"

    s 1a "Nope, no seizures. I guess my ex was causing them after all."

    pause 0.25
    $chat.addmessage(elsa, "Men are cancer.")

    s "Okay everyone, let's meet our dates!"

    pause 2.0

    show t 1l at fr12

    t "Welcome back to One-Week Waifu! I'm your host Tania Van der Waal, yes that IS my real name, and before the break we were just about to introduce this season's Suitors!"

    ki "I'm trying to catch my breath. I don't think I've ever been this nervous, standing behind the cameras and waiting."

    $chat.addmessage(elsa, "I could never do a dating show.")

    ki "My heart is a blur at this point."

    t 1o "Let's start with the introductions. We're going alphabetically just so nobody gets top billing, besides myself of course!"

    stop music fadeout 2.0

    show t 1a at mt1

    $chat.addmessage(bong, "probly just a casting couch situation neway.")

    
    pause 0.5
    show c 1p at fl12

    t "First off, you know her from the number one single on Quillboard's top 100 rock charts, 'China White', put your hands together for Cassandra Sanna!"

    play music cassPiano fadein 3.0

    $chat.addmessage(elsa, "Quillboard. Also, bong, grow tf up.")

    s 1t "Ooh, she's a cutie."

    python:
        chat.addmessage(egg, "Sexy choker girl.")
        chat.addmessage(bong, "its true. they're all fake anyway")

    c 1o "..."

    ki "I love her choker. Can't say I'm familiar with the song, though."

    $chat.addmessage(fon, "Ugh, no spoilers, but her choker :(")

    t 1o "Generally I'd ask our Suitor to say a few words, but Cassandra... well, I'll let her tell you."

    show c 1m

    ki "Cassandra lifts her hands and whirls them about in patterns I could never hope to translate, but know enough of to recognize as some form of sign language."

    s 1b "Oh, is she deaf? Poor thing!"

    $chat.addmessage(bar, "She's a deaf musician. Wow.")
    $chat.addmessage(bar, "I wonder if there are any of those in reality nowadays?")
    pause 0.2
    $chat.addmessage(beav, "beethoven")
    $chat.addmessage(bar, "Nowadays.")
    pause 0.7
    $chat.addmessage(crab, "Bae-thoven")

    t 2q "Anyone out there able to read ASL? No?"

    show t at justFade

    t "Our next Suitor is, and she's offered to help us out."

    stop music fadeout 2.0

    hide t

    show c 1a at mt1
    pause 0.5

    show r 1j at fr12


    pause 1.0

    t "May I present to you, everyone, the owner, proprieter and face of Ganymead Performing Arts, miss Robin Mia Lupei Godrey!"

    play music robin

    $chat.addmessage(cake, "She looks like my sister")

    ki "Oh. Tall. Jesus."

    show r 1m 

    s 1h "GOTH CHICK! I'm so onboard."

    ki "The woman looming statuesque before me is every inch of six-foot-three. Her hair is voluminous. She's like a goth-chick telephone pole."

    python:
        chat.addmessage(bong, "tell your sister come see me")
        chat.addmessage(cake, "my sister's an asshoel")
        chat.addmessage(fon, "Oh, Robin, I love you <B")

    s 1r "I hear you, Kylie."

    t 2n "Hi Robin!"

    r 1m "Tania. The pleasure is mine, of course."

    $chat.addmessage(elsa, "What a mix of names Robin has. I wonder where she's supposed to be from.")

    ki "Her voice rings musically, with a hint of the tongue-tension common to eastern European nations. I can't quite pin down her accent, though."

    s 1a "Tongue-tension. Chat, I'll let you guys pore over that one." 
    
    $chat.addmessage(bong,"treatin us lke a bunch of preverts")

    t 1l "Would you mind telling us what Cassandra said just now, Robin?"

    r 1m "She said she's excited to be here."

    show c 1g
    pause 0.25

    ki "From the expression on Cassandra's face I sort of doubt that's what she said."

    $chat.addmessage(shub, "She can hear can't talk")
    $chat.addmessage(crab, "Robin tryin to shit her up already")
    $chat.addmessage(elsa, "Trying to what?")

    s "Oh. I guess she's not deaf then. Maybe she's only mute? God, that would be rough in my line of work."

    ki "Robin takes a seat between Tania and Cassandra, crossing one endless leg over the other."

    show c 1a

    t 1p "So Robin, tell us a bit about what you do."

    r 1o "I operate the local performing arts center, draga mea. Dear Cassandra lends her magic to our stage from time to time, but I..."

    $chat.addmessage(bar, "draga what now?")
    $chat.addmessage(fizz, "She's speaking Romanian. It means my darling, more or less.")

    show r 1a

    ki "Her pause is a teasing one. From the wings I can almost feel her authority radiating outward; This is a woman used to controlling the conversation."

    $chat.addmessage(fon, "FizzyFizion you're so smart!")

    r 1o "... I would say the thirsty come to me for water."

    t 1r "That's awfully cryptic, Robin."


    r 1j "Yes, it is."

    $chat.addmessage(bong, "bestGirl. #hentai")


    c 1b "..."

    ki "Cassandra signs something toward them, and Robin chuckles a trill of a chuckle."

    $chat.addmessage(elsa, "Sophie, this isn't really an H-game, is it?")

    r 1o "Cassandra says you should have expected secrets on the first episode, dear."

    $chat.addmessage(cake, "Nah, can't stream H on this site.")

    show r 1a

    stop music fadeout 2.0

    t "I see. Well, one thing that isn't a secret is our last Suitor's black belt. Everyone, give a warm welcome to MMA flyweight Lichelle Carpenter!"

    hide t at f13

    pause 1.0

    show l 1o at fr13
    pause 1.0

    $chat.addmessage(bong, "ooh chocolate")

    l "Hey crew! How are good god you're tall."

    play music lichelle

    $chat.addmessage(elsa, "God you're gross @OberBong.")
    $chat.addmessage(fon, "Aw, Lichelle is so great!")

    show r 1j

    ki "Robin only smiles, a gentle, delicious smile."

    s 1n "Oh, we've got our tomboy! Wait. Which one is the nerd? Could we be dodging tropes today?"

    s 1b "Also, I don't think the game has any sex, people. I couldn't stream it."

    $chat.addmessage(bar, "Pity")

    t "Hello Elle, how have you been? I was sorry to hear how your last fight went!"

    l 1m "First off, I'm great. No shame in getting choked out by the champ."

    l 1j "Might've done better if my cutwoman had been there, though."

    $chat.addmessage(unkn, "Pronounced like El")
    $chat.addmessage(egg, "What's a cutwoman?")

    t "Yeah... I'm sorry about that. I wish I could've gone."

    show c 1s
    $chat.addmessage(fizz, "Tania is a TV host and a cutwoman. Pretty wild.")

    l 1k "Anyway."

    $chat.addmessage(bar, "Fontaine, you like everybody.")

    l "I'm just living life. I'm not in a training camp right now so I can eat what I want and make time to visit a TV show or two."

    $chat.addmessage(fizz, "A cutwoman or a cutman is there to stop a pro fighter's bleeding between rounds.")
    $chat.addmessage(fon, "I love them. Wow, Fizz! Smarty smart. Handsome too?")

    show l at justFade
    show c at justFade 
    show r at justFade 
    stop music fadeout 2.0
    pause 1.0

    t "Well, we're happy to have you here on One-Week Waifu. Now, before we meet our eligible bachelorette, I'd like each of you to let us know what being here means to you. And be honest!"

    play music cheerfulGuitar fadein 0.5

    hide c
    hide l
    hide r

    show t 1l at fr13
    

    pause 0.10

    show c 1o at f12 

    c "..."

    $chat.addmessage(bong, "think Fontaine might be catfishin")

    show r 1j at fl11

    r "Cassandra says, to be honest, she's here to promote her new album."

    hide r at fl11

    $chat.addmessage(egg, "She can't talk, could still be a mumble rapper.")

    ki "Cassandra nods, but her smile is oddly forlorn. I can't help but wonder who let her on stage without an interpreter she can trust."

    $chat.addmessage(elsa, "How awful. The only person speaking for her isn't being honest.")

    hide c at fr12

    show l 1l at fr12

    l "I'm here because Tania's my girl and she asked me to. She keeps trying to set me up on dates anyway, so I might as well be on TV for it."

    s "I admire their honesty if nothing else."

    s 1g "Hey Bong, be nice."

    $chat.addmessage(bong, "sorry Fontaine")
    $chat.addmessage(fon, "Nothing to forgive. I'll prove I'm not catfishing. Check private chat.")

    hide l at fr12
    pause 0.5
    show r 1m at fl12

    r "I am here in search of one perfect soul, my dears."

    ki "Tania's laughing, but there's an edge of nervousness to it. I can't blame her. Robin seems to take her goth attitude very seriously."

    t "Well, if you're lucky that perfect soul is standing right on the other side of the camera."

    $chat.addmessage(bar, "Robin lives her gimmick.")

    s 1b "She talkin' bout ME."

    t "Everyone welcome this season's single lady! Come on out, Kylie!"

    hide r at f12
    
    hide t at f13
    pause 1.4

    show r 1s at fl11
    pause 0.3
    show c 1s at f12
    pause 0.3
    show l 1s at fr13


    $renpy.notify("Chat!")

    ki "Okay. Breathe. It's my time, right? My nerves sing like there are little knives dancing upright on my skin."

    ki "I make my way to the stage, fully aware of the eyes trained on me. Cassandra's side-eye, Lichelle's direct gaze, Robin's --"

    $chat.addmessage(shub, "Robin's jeans.")

    ki "Well, Robin is looking past me, to the stage doors. Detachment must be part of her schtick."

    $chat.addmessage(fizz, "God, I'm gonna have to watch every stream so I don't miss anything.")
    $chat.addmessage(fizz, "Would've done it anyway :D")

    t "Welcome to the show, Kylie!"

    k "Thanks, uh, thank you. It's good to be here."

    t "It is! So, tell us a little bit about yourself?"

    $chat.addmessage(bong, "holy shit guys, Fontaine is for real.")

    k "Sure. Okay, um, I just graduated with a bachelor's in graphic design and I've been putting out feelers to get my career going."

    show r 1j

    s 1a "Ooh, I'm an artist. Nice."

    $chat.addmessage(crab, "oh yeah Bong? what's that mean?")
    $chat.addmessage(elsa, "Oh wow graphic design! Like me!")

    t "That's great! So what made you interested in coming on our show?"

    k "Well, I've been watching since season two..."

    $chat.addmessage(bong, "video chat she's hot af.")

    scene bg stage with fade

    show t 1l at fr13

    t "Wow, that's some story! So, we know you were just off camera while our Suitors introduced themselves."

    $chat.addmessage(fizz, "... really?")
    $chat.addmessage(egg, "He's messing with us. Let's just enjoy Sophie's stream.")

    hide t at f13
    pause 1.4

    show r 1s at fl11
    pause 0.3
    show c 1s at f12
    pause 0.3
    show l 1m at fr13

    t "Given what you heard from them, who has your attention?"

    $chat.addmessage(cake, "brb.")

    s 1a "So it's a dating game, sure, but don't you think it's weird for one person to meet all these others and expect to fall in love with one in a week?"

    s "I think I'd have a hard time with that. So... hey chat. Who do we like?"

    $chat.addmessage(elsa, "If I liked girls, probly the fighter. Imagine holding that person in your arms after a tough loss or a great win :)")
    $chat.addmessage(elsa, "But she might be too aggressive. Robin, then.")

    
    pause 1.0

    s 1m "Wow you guys are talkative today. Hi Shub, Crab, and Cake! My three amigos."

    $chat.addmessage(shub, "Hola, mamacita.")
    $chat.addmessage(crab, "'allo Ms. K")

    s "Hi TweeterEgg! How are you? Did you see what all these ladies said before?"

    $chat.addmessage(fizz, "Cassandra's mysterious. Like it.")

    s 1a "Oh, Elsa, you're such a romantic. Bong, I'm not on the list you perv. Don't any of these cuties get your attention?"

    $chat.addmessage(bar, "Bong is off gallavanting.")

    s "Fizz is all about some Cassandra, Twixt likes Robin. No love for Lichelle guys? I mean she's a badass, she could protect me if I needed it."

    s 1r "Which I don't, just so you know."

    $chat.addmessage(egg, "we got a badass over here")

    $renpy.notify("Even immaterial decisions may matter.")

    s 1a "I guess my answer here won't decide anything major yet, so I'm gonna say..."

    # choice

    $temp = False

    while temp == False:

        menu:
            "Cassandra":

                hide r at fl11
                hide c at f12
                hide l at fr13
                scene bg stage
                show c 2q at f12

                pause 0.5

                show t 2h at fr13

                t "Oh, you like the quiet type eh?"
                c "..."
                $chat.addmessage(fizz, "Good choice.")
                s 1a "I'm super curious how this is gonna play out if she can't talk. Like, maybe I can learn sign language in a week?"
                $temp = True
                $loveCass += 1
                $ which_girl_1 = "Cassandra"

            "Robin":
                hide r at fl11
                hide c at f12
                hide l at fr13
                scene bg stage
                show r 2p at f12

                t "Oh, you like the mysterious type eh?"
                r "I see. Perhaps you have my interest, as well, papillon."
                $chat.addmessage(bar, "Butterfly? Right?")
                s 1a "Oh my god she speaks French! The goth chick called me butterfly! Guys. Chat. We did it. We won."
                $temp = True
                $loveRobin += 1
                $ which_girl_1 = "Robin"

            "Lichelle":
                hide r at fl11
                hide c at f12
                hide l at fr13
                scene bg stage
                show l 1m at f12

                t "Oh, you like the dangerous type eh?"
                l "Don't worry, Kylie! I'm only dangerous if you want me to be."
                ki "She winks. I'm not sure if I believe her."
                $chat.addmessage(elsa, "I dunno about BDSM with a trained fighter though.")
                $temp = True
                $loveLich += 1
                $ which_girl_1 = "Lichelle"

            "You on the menu, Tania?" if loveTania == 0:
                hide r at fl11
                hide c at f12
                hide l at fr13
                show t 2b at f12

                t "Oh, no, that would make filming next season pretty tough!"
                $chat.addmessage(egg, "But she has a progress bar, so...")
                t "But I'm flattered!"
                $loveTania += 1

            "Just one?" if groupThing == False:
                hide r at fl11
                hide c at f12
                hide l at fr13
                show t 2q at f12
                k "Do I have to choose just one?"
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
        

    scene bg stage
    show t 1a at f12
    t "So let's talk a little bit about how this show works!"

    t "Every woman involved in this show is, of course, 20 years old or older -- but not much older, right? -- and each has consented to the format. We're looking for love here, people!"

    $chat.addmessage(elsa, "Me too, Tania, me too. Preach girl.")

    s 1a "Love, huh? Well... not me. But maybe."

    t 1o "Kylie will go on a total of seven dates, one date each day of the week. Each Suitor will have two dates with her, and then one final date with whomever Kylie decides is worthy of her affection!"

    $chat.addmessage(egg, "sounds complex")

    s "That's awfully objectifying. And short-sighted? How are we gonna pack enough drama into one week?"

    $chat.addmessage(crab, "is it objectifying tho? consented, right? nobody held a gun to their heads")

    t 1l "Each suitor has already selected a destination for the date. Meals and accommodations are on us, so hang on to your pocketbook Kylie!"

    $chat.addmessage(elsa, "Just because it's consented to doesn't mean it isn't objectifying.")

    k "How do we decide who goes first?"

    t 1o "Glad you asked. To keep it fair, we'll go alphabetically again!"

    $chat.addmessage(crab, "not trying to offend")

    k "What if we just don't click at all?"

    $chat.addmessage(shub, "then the game can't proceed lololol")

    pause 2.0

    hide t at f13
    pause 0.4

    show r 1m at fl11
    pause 0.3
    show c 1m at f12
    pause 0.3
    show l 1m at fr13

    t "I'd say the chance of that is practically nonexistent!"

    s "I mean, I guess we have to click or the game wouldn't work."

    s "Oh yeah Shub, exactly."

    $chat.addmessage(egg, "Crop of cuties though. Like a little bag of oranges.")

    t "Kylie, Cassandra, Robin, Lichelle, on behalf of everyone at One-Week Waifu, I wish you the best of luck! No matter who Kylie chooses, you'll make the cutest couple wherever you go!"

    s 1n "TOO MUCH SUGAR!"

    $chat.addmessage(cake, "oranges wtf .... oh i getcha")

    k "Thanks, Tania."

    c 1p "..."

    r 1o "I would say the choice is obvious."

    $chat.addmessage(bar, "Obviously, my dark princess! STEP ON ME GODDESS!")

    l 1l "Obviously it's gonna be me!"

    $chat.addmessage(elsa, "lol weirdo")

    t "Thanks for tuning in everybody!"

    stop music fadeout 1.0

    scene bg near stage with fade
    
    show t 1a at f12

    $chat.addmessage(fizz, "Buncha freaks in here and it's great.")

    pause 1.0

    play music hallwayChats fadein 1.0

    t "Hey, Kylie. I hope that wasn't too stressful."

    k "No more than the last time I was in front of three dream girls and thousands of fans."

    $chat.addmessage(fizz, "I'm really curious about Cassandra. Why's Robin mistranslating? Fontaine was sad about her choker. What's up with that?")

    s 1a "Chat, I don't know about you, but I'm ready for a hot date. Let's take a sec to catch up though. Um..."

    $chat.addmessage(elsa, "Cassandra's in a cult. No doubt. Vow of silence. For sure.")

    $chat.addmessage(crab, "Fontaine and Bong been awful quiet")

    s "I know guys, I'm pretty curious about Cassandra. Like, are we gonna find out why she can't talk? Or like... maybe she has some dark secret and she chooses not to speak."

    $chat.addmessage(egg, "Elle's my type unless she has man muscles under that shirt.")

    s "Elsa says Cassandra's in a cult with a vow of silence. Could be, could be!"

    s "Tweeter is interested in Elle, but wants to see her with her shirt off to find out if she has man-muscles. Uh-huh. I'm sure that's all."

    $chat.addmessage(shub, "Tania's right there. She got richgurl money, bet.")

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

    pause 0.2

    k "So Cassandra's first, huh? How are we supposed to communicate?"

    $chat.addmessage(crab, "Solid question, Kylie. Kylie best girl.")

    t 1q "Don'tcha worry about that. She's always got her phone with her and she has this shorthand app that helps her communicate."

    t 1a "And I have an idea for next time we're on stage."

    $chat.addmessage(crab, "see I thought about a phone but can't really show the camera")

    k "I'm worried, though. I don't know anything about them, really. Is every contestant nervous like this?"

    $chat.addmessage(elsa, "I'd be a nervous wreck.")

    t 1o "Oh, god, yeah. Well, except for season four. That dude was just a full-blown sex-pervert. He didn't care who he was with."

    s "I wanna see that season."

    $chat.addmessage(crab, "I wanna BE that season")
    $chat.addmessage(shub, "mah boi")

    t 1a "Just think about why you're really here. It'll come to you."

    $chat.addmessage(elsa, "Tania's so comforting.")

    k "Well, I'm... I'm..."

    s "Hmm... what to say?"

    $chat.addmessage(fizz, "Choice alert!")

    menu:

        k "I should say I'm..."

        "In it for the cash":
            show t 1g
            t "I understand that. At least give us a good show though. This is our first all-female season and we're counting on the 18-35 male-fantasy demographic."
            s "That means she's counting on you guys, Crab, Shub, Cake and Bong."
            $chat.addmessage(bar, "Shit I'm 36.")

        "Looking for The One":
            show t 1b
            t "Oh, honey..."
            $chat.addmessage(elsa, "Her sad face! :(")
            t "Just don't get your hopes up, okay? Don't ever let my producer hear I said this, but we really are just a reality show. No one ever meets the one here."
            ki "Tania's squeezing my hand, lightly. She's... genuinely sad, I think."
            $chat.addmessage(fizz, "Tania must have been a contestant at one point.")

        "Just looking for a thrill.":
            show t 2u
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
            show t 1m
            t "I respect your honesty, kiddo."

            ki "Kiddo? She's like a year older than me, max."
    # end menu

    show t 1s
    t "Don't be too nervous. When the show's finished, you'll have a nice payout in your pocket no matter what happens."

    k "Looking forward to that!"

    t "Yup. So... your first date is with Cassandra. You have a dressing room set up down the hall, and you have about an hour to get ready and get your nerves down."

    $chat.addmessage(fizz, "YES!")

    k "That might not be enough."

    t 1u "You'll be okay. Remember, the worst thing that could possibly happen is nothing, right?"

    $chat.addmessage(bar, "Said that to my college girlfriend, too.!")

    k "I guess so."

    t 1o "You guess correctly! Now, we'll have a car ready to take you to the date destination when you're ready. The crew will be there filming, of course, and we'll have security on site to make sure nobody tries to get involved."

    $chat.addmessage(elsa, "So Kylie's going to get chauffered everywhere!")

    k "I remember season 6. Hey, now that I think about it... I knew I'd seen Lichelle before!"

    s "Ooh, plot twist!"

    $chat.addmessage(beav, "Elle kickin' ass for love!")

    show t 1m

    t "Yup, she used to work security for us."

    ki "I remember that. There was a pick-up artist guy at the bar the couple went to, who wouldn't leave them alone. Lichelle had been about as gentle as a person can be when choking someone out with her thighs. I have to ask her about that."

    t "Any more questions?"

    $chat.addmessage(fizz, "Either that's a triangle choke or we need to be watching season six.")
    $chat.addmessage(cake, "damn. hot in here.")

    $temp = False
    $haveAsked = False  # Just a variable to signify whether you've already asked a question

    while temp == False:
        pause 0.5

        menu:

            "Seriously, what if I don't click with anyone?":
                $haveAsked == True
                show t 1g
                t "Sometimes people just don't mesh. That's one reason we found such wildly different women, so most tastes would be accounted for."

                t 2u "Outside wild kinks, I guess."

                t 1o "Point is, just go with your heart. If you like one of the Suitors after the first date, go after her hard on the second. Be yourself, be... I dunno. Honest."

            "What if I want to end the date early?":
                $haveAsked == True
                t 1q "You're contractually obligated not to, so... even if you don't like the date, you have to get through it."
                
                t 2a "Just try to make it interesting for the audience if that happens."

            "How much of this is staged?":
                $haveAsked == True
                t 1r "I'd guess it's staged to the same degree real life is staged. Nobody's fully authentic on the first two dates, right?"

            "I have no questions.":
                $haveAsked == True
                $ temp = True

        # end of choice

    $chat.addmessage(fizz, "I love Q and A time. Hey Sophie, did you notice chat wasn't working just now?")

    t 1l "Great. Go get ready, and hey Kylie? Listen. If you need to talk to anybody, I'm around."
    
    t "I've been on this show since day one and I'll be happy to listen if you need anything."

    $chat.addmessage(unkn, "R/BG13:14-15")

    s "Tania's nice. I bet the real hosts of these shows are nothing like her."

    k "Thanks, Tania. That actually means a lot."

    t 1l "No problem. Now shoo, go get your game face on and knock Cassandra's socks off!"

    hide t at f12

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

    show c 1p at f12

    ki "Cassandra, the silent musician. Her eyes miss nothing, her features are so perfectly sculpted, her bearing so beautifully coquettish."

    $chat.addmessage(fizz, "I wonder if any of her music is written for the game.")
    ki "I feel some deep well of empathy emanating from her, building behind a dam of muteness."

    show c at mt3

    show l 1m at f12

    ki "Lichelle, the fit girl with the wild smile and hungry eyes. So fierce, so powerful, so dangerous. Some part of me has a tiny, tiny submissive side and Lichelle simply radiates the power to control."

    $chat.addmessage(elsa, "I can relate to that.")

    show l 1a at mt1

    show r 1j at f12 
    ki "Robin, the shadow, graceful and statuesque. Her detachment paired with that accent lend her this ghostly, mysterious vibe that pulls at me, even now as I think about her."
    
    ki "Some part of me is afraid of her, but it's hard to express why."

    $chat.addmessage(bar, "I mean, that's a chick who's in control of her space. Don't fluck with a woman like that.")
    $chat.addmessage(cake, "preach. also, how submissive we talkin, @ElsaLater?")

    ki "They're all otherworldly in their way. I guess I should feel incredibly lucky that the women in front of me are all so desirable."

    $chat.addmessage(elsa, "What about Tania!?!?!")
    scene bg stage with dissolve
    $chat.addmessage(elsa, "Nowhere near enough to submit to Internet edgelords.")

    ki "I should focus on getting ready, though. I wonder what Cassandra has in mind?"

    stop music fadeout 3.0

    scene bg black with dissolve

    $chat.addmessage(cake, "Shame b/c I'm dom AF")

    # checks chat

    s 1a "Hm. I agree, everyone, it's gonna be a tough choice. Like, I like how Robin's all spooky and gothic. She's like a playhouse owner, too, so she's probably good at business and stuff."

    s "Bong, you pick a girl yet?"

    $chat.addmessage(elsa, "Need some dude options!")
    $chat.addmessage(egg, "he picked Fontaine")

    pause 0.5

    s "I guess Bong and Fontaine did both vanish at once. Probably just coincidence, right?"

    $chat.addmessage(bar, "prob!")

    s "Elsa, I guess the game's really supposed to appeal to a certain type of guy, so there aren't any boys to date in this one. Next time, we'll find one that's got guys to play, how's that sound?"

    $chat.addmessage(shub, "Gross! We need to date ALIENS instead.")

    s 1m "Shub, that's okay, we have to make sure everyone has something that works for them. Now that I'm doing better, we'll find a Martian to mate with at some point."

    $chat.addmessage(egg, "Scandalous. Also, all these ladies seem great in their own way!")

    s "Tweeter, you're right. It's like... I feel like it'll be hard to really decide who we like if everyone's good. We only have seven days!"

    s 1d "Oh my god. Seven days to find love. Or hit that. Right Fizz?"

    $chat.addmessage(fizz, "I'm a lover, not a hitter!")
    $chat.addmessage(crab, "or a quitter!")

    s 1a "Okay guys, I'm gonna take a short break. You perverts talk amongst yourselves for a bit!"

    pause 1.0

    show image splashBRB at alphaFade

    python:
        newComments = [

            [bar, "I'm not sure I'm into this game."],
            [elsa, "I think I am. It's only been a few minutes."],
            [fizz, "I'm just in it for Sophie."],
            [cake, "Crushin hard bruv"],
            [shub, "^^^"],
            [egg, "Pretty obvious"],
            [fizz, "NO"],
            [crab, "This game sux"],
            [fon, "NO"],
            [shub, "Hey, Fontaine's back"],
            [fon, "This is the best game."],
            [cake, "So did you really private chat with Bong?"],
            [fon, "Yes. He's a pretty boy."],
            [elsa, "Is he? I kind of imagined him as a greasy neckbeard."],
            [fon, "No."],
            [egg, "Bong said you were HAWT af"],
            [fon, "Oh, I don't know about that. ;)"],
            [fon, "Sophie, where'd you go? You need to play!"]


        ]
        chat.bulkMessage(newComments, 0.75)

    pause

    hide image splashBRB at alphaFade

    pause 1.0

    s "Okay, I'm back! So, let's get this date!"

    $chat.addmessage(crab, "Were you peeing")

    s "Oh, welcome back Fontaine."

    $chat.addmessage(fizz, "Gross.")

    s "If you have to know, yes, I went to the restroom. You guys are freaks."

    scene bg dressing with dissolve

    play music bedroom fadein 1.0

    ki "The dressing room is clean and simple. I'd like to stretch out for a nap, actually; the nerves have taken it out of me."

    $chat.addmessage(beav, "Neat. Streaming while streaming.")

    ki "There are some clothes set aside in the closet. One of the producers and I talked about what I might wear to the dates beforehand."

    $chat.addmessage(elsa, "eww.")
    $chat.addmessage(egg, "l0l")
    $chat.addmessage(bar, "nice")

    ki "So I have a simple black dress with matching shoes for one date, a jeans and teddy bear tee for another, and then a smart blue pantsuit with emerald blouse."

    ki "The dress is awfully revealing. It feels like a silky puddle of nothing in my hands." 
    
    $chat.addmessage(cake,"That's that whiskeyDiq, right Crab?")

    ki "I like the jeans and bear shirt more than I want to admit, but it seems too casual. Laundry-day casual." 
    
    $chat.addmessage(crab,"never happens son")

    ki "The pantsuit is stylish, but I think a suit requires a certain power attitude. Not me, not in the least."

    s 1a "So the game wants us to guess who might like which outfit?"

    $chat.addmessage(elsa, "Little black dress on first date? Nope.")

    s "Either that or this is just filler. Here in the real world I wouldn't make this choice without knowing where we're going."

    $chat.addmessage(fizz, "Jeans and tank is too casual.")
    $chat.addmessage(cake, "pantsuit nope.")

    s "Am I wearing a little black dress to go ice skating? Hey Bong, what do you think?"

    $chat.addmessage(fon, "I want to see you in the little dress.")

    s "Exactly, cake. Not feeling a pantsuit for Cassandra."

    menu:

        ki "So, for Cassandra's date I should wear..."

        "Little Black Dress":
            ki "I think she might like something simple. She's a musician, and a successful one, so she might take us somewhere classy?"
            $chat.addmessage(fon, "Yay!")
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

    show t 1l at f12

    t "Hey, Kylie, looking great!"

    s 1m "I bet she would have said that no matter what we picked."

    $chat.addmessage(shub, "bet")

    k "Thanks. Is the car here? I want-"

    t "Yup! Let's go!"

    $chat.addmessage(elsa, "Tania's in a hurry!")

    k "Oh? You're coming with?"

    $chat.addmessage(egg, "gotta make a show.")

    t 1q "Yeah. We'll actually film a little coverage track, maybe interview the staff about the place you're going. Some b-roll footage, maybe."

    k "Oh."

    $chat.addmessage(cake, "I saw a lot of b-roll in my porn director days")

    t 1l "Let's go!"

    hide t at f12

    $hideGui()

    stop music fadeout 2.0

    # adjust character bios from 0 (unknown) to 1 (standard bios)

    python:
        for i in allBios:
            i.levelUp()

    # collect chat history in appropriate variable.
    $getHistory(0)

    scene bg black with fade

    jump cassDate1
