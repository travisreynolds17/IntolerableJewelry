

# label common1:
    #This one introduces Sophie as a streamer post seizure. She'll mention it, but kind of dreamily.

    #text
    

    #loading screen - String

    # scene bg load-string with fade

    # pause 4.0

    scene bg near stage
    with fade

    #just a test
    python:
        loveCass = 3
        loveLich = 2
        loveRobin = 5
        loveTania = 10
        loveEntity = 0

        # call a love check
        

    show screen mainGameWindow

    show screen loveScreen

    show screen btnWindow 

    show screen sophieChat
    
    $soph.addmessage(sophie,"Hey guys, welcome back. So last time... what happened last time?")

    $soph.addmessage(sophie,"Oh that's right, we were getting ready to meet the host.")

    $soph.addmessage(sophie,"So this game is supposed to be a visual novel about one of those dating reality shows. Kind of like The Unmarried Guy.")
        

    $soph.addmessage(sophie,"Just like always guys, chat away! Fan club comments go straight to the top, so if you wanna support me join up!")


    # sophie checks chat. 

    $soph.addmessage(sophie,"Oh. Hey guys, looks like the subscribe button's not working right. We'll fix it later.")

    # start chattin - frontload it a bit
    python:
        chat.addmessage(fizz, "Yay, strim time!")
        chat.addmessage(fizz, "Hi Sophie, whatcha playin?")
        chat.addmessage(elsa, "Hey sister! Wait, is this a VN? A DATING SIM?!?")
        chat.addmessage(bong, "Date me Sophie lol I'll be your date")
        chat.addmessage(liv, "I love this game! <B")
        chat.addmessage(beav, "Jeez, why")
        chat.addmessage(fizz, "How are you feeling these days?")
        chat.addmessage(elsa, "Yeah are you still okay????")

    show screen chatterbox
    $chatIsOn = True
    pause 2.0

    $soph.addmessage(sophie,"Thanks, Fizz, how are you tonight? Did your test go okay?")

    $soph.addmessage(sophie,"Hi Liv! You know this game, too? No spoilers, okay? Also, I don't think we've met, welcome!")

    $chat.addmessage(liv, "It's my favorite game.")

    $soph.addmessage(sophie,"Oh my god, Bong, stop, you horndog. I'm gonna be here all night.")

    $chat.addmessage(fizz, "Passed, barely. God.")

    $soph.addmessage(sophie,"Elsa, it's really just a dating sim. I kind of needed something to wind down.")

    $soph.addmessage(sophie,"How am I doing? I'm doing fine, I guess. I haven't had a seizure since the last one.")

    $chat.addmessage(bong, "u love me lol")

    $soph.addmessage(sophie,"I know, I know, I know. I'm funny.")

    $chat.addmessage(bar, "really glad your OK. you gonna try to date again?")

    $soph.addmessage(sophie,"Seriously, I've never been better. I'm independent again, no seizures, I can stream all I want. And I can hang out with you guys!")

    $chat.addmessage(liv, "No spoilers, I can't wait to see if you can make it ;)")

    $soph.addmessage(sophie,"Thanks Twixt. I'm not ready to date in real life just yet, but I'm ready to date in this game we're gonna start playing right now!")

    $chat.addmessage(elsa, "don't date, practice self love")

    $chat.addmessage(bong, "weird u can see chat if I have window closed")
    $chat.addmessage(liv, "No, that's part of the game. Even chat can switch some windows.")
    #goes through title screen 

    $soph.addmessage(sophie,"So we already named our protag, and of course I named her Kylie. I'm happy it let me choose to be a girl, by the way.")

    $chat.addmessage(bar, "Why Kylie?")

    $soph.addmessage(sophie,"Wait, really, Liv? That's interesting! So now all of you get to know how I feel when I get behind on chat and have to catch back up, ha!")
    
    $soph.addmessage(sophie,"Twixt, it's because Kylie's my middle name. Everyone called me Kylie when I was just an egg.")

    $soph.addmessage(sophie,"Okay, chat, I'll catch up with you later!")

    if chatIsOn:
        hide screen chatterbox
        $chatIsOn = False

    pause 1.0

    $soph.addmessage(sophie,"So... where were we?")

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

    $soph.addmessage(sophie,"I love cheese. I love this game already!")

   
    scene bg stage with longFade
   
    
    $soph.addmessage(sophie,"Oh, I like this setup! I wonder what kind of people we're gonna meet?")

    $chat.addmessage(beav, "Assholes.")
    $chat.addmessage(fizz, "Tania's already best girl. 10/10")
    $chat.addmessage(elsa, "I like her hair")
    $chat.addmessage(liv, "I love Tania so much!")

    #checks chat
    if chatIsOn == False:
        show screen chatterbox
        $chatIsOn = True
    pause 1.0

    $soph.addmessage(sophie,"Oh wow, you guys like Tania. Fizz you can't name her best girl yet, we haven't even met the dates!")

    $soph.addmessage(sophie,"Oh, hey Beaver, how's your day? Assholes, sure. Probably.")

    pause 0.25
    $chat.addmessage(beav, "Good, yours? How's you? Any moer seizures?")

    $soph.addmessage(sophie,"Yeah, I'm great. I'm happy, doing what I love with people I like!")

    $soph.addmessage(sophie,"Nope, no seizures. I guess my ex was causing them after all.")

    pause 0.25
    $chat.addmessage(elsa, "Men are cancer.")

    $soph.addmessage(sophie,"Okay everyone, let's meet our dates!")

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
    
    $soph.addmessage(sophie,"Ooh, she's a cutie.")

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

    $soph.addmessage(sophie,"Oh, is she deaf? Poor thing!")

    $chat.addmessage(bar, "She's a deaf musician. Wow.")
    $chat.addmessage(bar, "I wonder if there are any of those in reality nowadays?")
    $chat.addmessage(beav, "beethoven")
    $chat.addmessage(bar, "Nowadays.")
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

    $soph.addmessage(sophie,"GOTH CHICK! I'm so onboard.")

    ki "The woman looming statuesque before me is every inch of six-foot-three. Her hair is voluminous. She's like a goth-chick telephone pole."

    $soph.addmessage(sophie,"I hear you, Kylie.")

    t "Hi Robin!"

    show r speak

    r "Tania. The pleasure is mine, of course."

    ki "Her voice rings musically, with a hint of the tongue-tension common to eastern European nations. I can't quite pin down her accent, though."

    $soph.addmessage(sophie,"Tongue-tension. Chat, I'll let you guys pore over that one.")

    t "Would you mind telling us what Cassandra said just now, Robin?"
    
    show r happy

    r "She said she's excited to be here."

    show c disap
    pause 0.25

    ki "From the expression on Cassandra's face I sort of doubt that's what she said."

    $soph.addmessage(sophie,"Oh. I guess she's not deaf then. Maybe she's only mute? God, that would be rough in my line of work.")

    ki "Robin takes a seat between Tania and Cassandra, crossing one endless leg over the other."

    show c

    t "So Robin, tell us a bit about what you do."

    show r speak

    r "I operate the local performing arts center, draga mea. Dear Cassandra lends her magic to our stage from time to time, but I..."

    show r happy

    ki "Her pause is a teasing one. From the wings I can almost feel her authority radiating outward; This is a woman used to controlling the conversation."

    show r speak

    r "... I would say the thirsty come to me for water."

    t "That's awfully cryptic, Robin."

    show r happy

    r "Yes, it is."

    show c sad

    c "..."

    ki "Cassandra signs something toward them, and Robin chuckles a trill of a chuckle."

    show r speak

    r "Cassandra says you should have expected secrets on the first episode, dear."

    show r listen

    t "I see. Well, one thing that isn't a secret is our last Suitor's black belt. Everyone, give a warm welcome to MMA flyweight and fitness instructor Lichelle Carpenter!"

    hide t with moveoutright

    pause 1.0

    show l speak at right with moveinleft

    l "Hey crew! How are good god you're tall."

    show r happy

    ki "Robin only smiles, a gentle, delicious smile."

    $soph.addmessage(sophie,"Oh, we've got our tomboy! Wait. Which one is the nerd? Could we be dodging tropes today?")

    t "Hello Lichelle, how have you been? I was sorry to hear how your last fight went!"

    show l happy

    l "Other than that - thanks for reminding me, by the way - things are good! I went up against the champ and I came up short, but I'll come back stronger than ever."

    show l listen 

    t "I believe you. So, what are you doing these days?"

    show l speak

    l "I'm just living life. I'm not in a training camp right now so I can eat what I want and make time to visit a TV show or two."

    t "Well, we're happy to have you here on One-Week Waifu. Now, before we meet our eligible bachelorette, I'd like each of you to let us know what being here means to you. And be honest!"

    show c speak
    pause 0.10
    show l listen

    c "..."

    show r speak

    r "Cassandra says, to be honest, she's here to promote her new album."

    ki "Cassandra nods, but her smile is oddly forlorn. I can't help but wonder who let her on stage without an interpreter she can trust."

    l "I'm here because Tania's my girl and she asked me to. She keeps trying to set me up on dates anyway, so I might as well be on TV for it."

    $soph.addmessage(sophie,"I admire their honesty if nothing else.")

    r "I am here in search of one perfect soul, my dears."

    ki "Tania's laughing, but there's an edge of nervousness to it. I can't blame her. Robin seems to take her goth attitude very seriously."

    t "Well, if you're lucky that perfect soul is standing right on the other side of the camera."

    $soph.addmessage(sophie,"She talkin' bout ME.")

    t "Everyone welcome this season's single lady! Come on out, Kylie!"

    ki "Okay. Breathe. It's my time, right? My nerves sing like there are little knives dancing upright on my skin."

    ki "I make my way to the stage, fully aware of the eyes trained on me. Cassandra's side-eye, Lichelle's direct gaze, Robin's --"

    ki "Well, Robin is looking past me, to the stage doors. Detachment must be part of her schtick."

    t "Welcome to the show, Kylie!"

    k "Thanks, uh, thank you. It's good to be here."

    t "It is! So, tell us a little bit about yourself?"

    k "Sure. Okay, um, I just graduated with a bachelor's in graphic design and I've been putting out feelers to get my career going."

    $soph.addmessage(sophie,"Ooh, I'm an artist. Nice.")

    t "That's great! So what made you interested in coming on our show?"

    k "Well, I've been watching since season two..."

    scene bg near stage with fade

    show t

    t "Wow, that's some story! So, we know you were just off camera while our Suitors introduced themselves."

    

    hide t with dissolve
    show c at left
    show r
    show l at right
    with dissolve

    t "Given what you heard from them, who has your attention?"

    $soph.addmessage(sophie,"So it's a dating game, sure, but don't you think it's weird for one person to meet all these others and expect to fall in love with one in a week?")

    $soph.addmessage(sophie,"I think I'd have a hard time with that. So... hey chat. Who do we like?")

    #show chat

    $soph.addmessage(sophie,"Hi TweeterEgg! How are you? Did you see what all these ladies said before?")

    $soph.addmessage(sophie,"Oh, Elsa, you're such a romantic. Bong, I'm not on the list you perv. Don't any of these cuties get your attention?")

    $soph.addmessage(sophie,"Fizz is all about some Cassandra, Twixt likes Robin. No love for Lichelle guys? I mean she's a badass, she could protect me if I needed it.")

    $soph.addmessage(sophie,"Which I don't, just so you know.")

    $soph.addmessage(sophie,"I guess my answer here won't decide anything major yet, so I'm gonna say...")

    #choice

    $temp = False

    while temp == False:

        

        menu:
            "Cassandra":
                scene bg stage
                show c with dissolve

                t "Oh, you like the quiet type eh?"
                c "..."
                $soph.addmessage(sophie,"I'm super curious how this is gonna play out if she can't talk. Like, maybe I can learn sign language in a week?")
                $temp = True
                $loveCass += 1
                $ which_girl_1 = "Cassandra"

            "Robin":
                scene bg stage
                show r with dissolve

                t "Oh, you like the mysterious type eh?"
                r "I see. Perhaps you have my interest, as well, papillon."
                $soph.addmessage(sophie,"Oh my god she speaks French! The goth chick called me butterfly! Guys. Chat. We did it. We won.")
                $temp = True
                $loveRobin += 1
                $ which_girl_1 = "Robin"

            "Lichelle":
                scene bg stage
                show l with dissolve

                t "Oh, you like the dangerous type eh?"
                l "Don't worry, Kylie! I'm only dangerous if you want me to be."
                ki "She winks. I'm not sure if I believe her."
                $temp = True
                $loveLich += 1
                $ which_girl_1 = "Lichelle"

            "You on the menu, Tania?" if loveTania == 0:
                t "Oh, no, that would make filming next season pretty tough!"
                t "But I'm flattered!"
                $loveTania += 1
                

            "Just one?" if groupThing == False:
                $soph.addmessage(sophie,"Rawr!")
                t "Calm down girl, the show is Waifu, singular."
                t "But I admire your optimism!"
                $groupThing = True
                
            # END OF CHOICE

    scene bg stage
    show t with dissolve
    t "So let's talk a little bit about how this show works!"

    t "Every woman involved in this show is, of course, 20 years old or older -- but not much older, right? -- and each has consented to the format. We're looking for love here, people!"

    $soph.addmessage(sophie,"Love, huh? Well... not me. But maybe.")

    t "Kylie will go on a total of seven dates, one date each day of the week. Each Suitor will have two dates with her, and then one final date with whomever Kylie decides is worthy of her affection!"

    $soph.addmessage(sophie,"That's awfully objectifying. And short-sighted? How are we gonna pack enough drama into one week?")

    t "Each suitor has already selected a destination for the date. Meals and accommodations are on us, so hang on to your pocketbook Kylie!"

    k "How do we decide who goes first?"

    t "Glad you asked. To keep it fair, we'll go alphabetically again!"

    k "What if we just don't click at all?"

    pause 3.0

    hide t with dissolve
    show c at left
    show r
    show l at right
    with dissolve

    t "I'd say the chance of that is practically nonexistent!"

    $soph.addmessage(sophie,"I mean, I guess it has to be or the game wouldn't work.")

    t "Kylie, Cassandra, Robin, Lichelle, on behalf of everyone at One-Week Waifu, I wish you the best of luck! No matter who Kylie chooses, you'll make the cutest couple wherever you go!"

    $soph.addmessage(sophie,"TOO MUCH SUGAR!")

    k "Thanks, Tania."

    c "..."

    r "I would say the choice is obvious."

    l "Obviously it's gonna be me!"

    t "Thanks for tuning in everybody!"

    scene

    scene bg near stage
    show t
    with fade

    t "Hey, Kylie. I hope that wasn't too stressful."

    k "No more than the last time I was in front of three dream girls and thousands of fans."

    #darken screen, sophie time

    $soph.addmessage(sophie,"Chat, I don't know about you, but I'm ready for a hot date. Let's take a sec to catch up though. Um...")

    #checks chat

    $soph.addmessage(sophie,"I know guys, I'm pretty curious about Cassandra. Like, are we gonna find out why she can't talk? Or like... maybe she has some dark secret and she chooses not to speak.")

    $soph.addmessage(sophie,"Elsa says Cassandra's in a cult with a vow of silence. Could be, could be!")

    $soph.addmessage(sophie,"Tweeter is interested in Lichelle, but wants to see her with her shirt off to find out if she has man-muscles. Uh-huh. I'm sure that's all.")

    $soph.addmessage(sophie,"Bong's disappointed Tania's not available. She's got lots of energy, I agree. Her last name sounds like her parents are rich, right, right.")

    $soph.addmessage(sophie,"Beaver, what about you? You went quiet on us.")

    pause 2.0

    $soph.addmessage(sophie,"Hey you never know. Never know with dating sims anymore. We might could make a foursome happen, but I mean, do we really want that? I feel like the logistics would make it tough to pull off.")

    $soph.addmessage(sophie,"Like Robin's really tall and Lichelle's kinda short, right?")

    $soph.addmessage(sophie,"Actually, let's not go down this rabbit hole just yet.")

    # back to game

    k "So Cassandra's first, huh? How are we supposed to communicate?"

    t "Don'tcha worry about that. It was kinda tough on stage, but she's always got her phone with her and she has this shorthand app that helps her communicate."

    t "And I have an idea for next time we're on stage."

    k "I'm worried, though. I don't know anything about them, really. Is every contestant nervous like this?"

    t "Oh, god, yeah. Well, except for season four. That dude was just a full-blown sex-pervert. He didn't care who he was with."

    $soph.addmessage(sophie,"I wanna see that season.")

    t "Just think about why you're really here. It'll come to you."

   

    k "Well, I'm... I'm..."

    $soph.addmessage(sophie,"Hmm... what to say?")

    menu:
        
        k "I should say I'm..."
        

        "In it for the cash":
            t "I understand that. At least give us a good show though. This is our first all-female season and we're counting on the horny 18-35 male-fantasy demographic."

        "Looking for The One":
            t "Oh, honey... just don't get your hopes up, okay? Don't ever let my producer hear I said this, but we really are just a reality show. No one ever meets the one here."
            ki "Tania's squeezing my hand, lightly. She's... genuinely sad, I think."

        "Just looking for a thrill.":
            t "Oh. So you're a sex-pervert too?"
            k "No, no, I just... I dunno. I guess I want some excitement in my life before I settle into a cubicle somewhere."
            t "I respect your honesty, kiddo."

            ki "Kiddo? She's like a year older than me, max."
    # end menu

    t "Don't be too nervous. When the show's finished, you'll have a nice payout in your pocket no matter what happens."

    k "Looking forward to that!"

    t "Yup. So... your first date is with Cassandra. You have a dressing room set up down the hall, and you have about an hour to get ready and get your nerves down."

    k "That might not be enough."

    t "You'll be okay. Remember, the worst thing that could possibly happen is nothing, right?"

    k "I guess so."

    t "You guess correctly! Now, we'll have a car ready to take you to the date destination when you're ready. The crew will be there filming, of course, and we'll have security on site to make sure nobody tries to get involved."

    k "I remember season 6. Hey, now that I think about it... I knew I'd seen Lichelle before!"

    $soph.addmessage(sophie,"Ooh, plot twist!")

    t "Yup, she used to work security for us."

    ki "I remember that. There was a pick-up artist guy at the bar the couple went to, who wouldn't leave them alone. Lichelle had been as gentle as a person can be when choking someone unconscious. I have to ask her about that."

    t "Any more questions?"

    $temp = False
    $haveAsked = False # Just a variable to signify whether you've already asked a question
    
    while temp == False:
        if haveAsked:
            t "Anything else?"
        else:
            k "What should I ask...?"

        menu:

            "Seriously, what if I don't click with anyone?":
                $haveAsked == True
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

        #end of choice

    t "Great. Go get ready, and hey Kylie? Listen. If you need to talk to anybody, I'm around. I've been on this show since day one and I'll be happy to listen if you need anything."

    $soph.addmessage(sophie,"Tania's nice. I bet the real hosts of these shows are nothing like her.")

    ki "Thanks, Tania. That actually means a lot."

    t "No problem. Now shoo, go get your game face on and knock Cassandra's socks off!"

    scene bg hallway with dissolve

    ki "There's a lot on my mind as I make my way to the dressing room. These women, they're all alluring in their own way. I can definitely appreciate the three-bears strategy."

    show c at right with dissolve

    ki "Cassandra, the silent musician. Her eyes miss nothing, her features are so perfectly Greek, her bearing so beautifully coquettish." 
    ki "I feel some deep well of empathy emanating from her, building behind a dam of muteness."

    show l with dissolve

    ki "Lichelle, the fit girl with the wild smile and hungry eyes. So fierce, so powerful, so dangerous. Some part of me has a tiny, tiny submissive side and Lichelle just... radiates the power to control."

    show r at left with dissolve
    
    ki "Robin, the shadow, graceful and statuesque. Her detachment paired with that accent lend her this ghostly, mysterious vibe that pulls at me, even now as I think about her. Some part of me is afraid of her, but it's hard to express why."

    ki "They're all otherworldly in their way. I guess I should feel incredibly lucky that the women in front of me are all so desirable."

    scene bg stage with dissolve

    ki "I should focus on getting ready, though. I wonder what Cassandra has in mind?"

    scene bg black with dissolve

    $soph.addmessage(sophie,"Oh my god, me too. Hey chat, how we doin? How's everyone feeling?")

    #checks chat

    $soph.addmessage(sophie,"Hm. I agree, everyone, it's gonna be a tough choice. Like, I like how Robin's all spooky and gothic. She's like a playhouse owner, too, so she's probably good at business and stuff.")

    $soph.addmessage(sophie,"Bong, you pick a girl yet?")

    $soph.addmessage(sophie,"Not me. Seriously, get in the game sicko.")

    $soph.addmessage(sophie,"Elsa, I guess the game's really supposed to appeal to like... stereotypical weeb guys, so there aren't any boys to date in this one. Next time, we'll find one that's all guys to play, how's that sound?")

    $soph.addmessage(sophie,"Bong, that's okay, we have to make sure everyone has something that works for them. I'll play more things you might enjoy, too, now that I'm doing better.")

    $soph.addmessage(sophie,"Tweeter, you're right. It's like... I feel like it'll be hard to really decide who we like if everyone's good. We only have seven days!")

    $soph.addmessage(sophie,"Oh my god. Seven days to find love. Or hit that. Right Fizzy?")

    $soph.addmessage(sophie,"Okay guys, I'm gonna take a short break. You guys talk amongst yourselves for a bit!")

    scene bg brb with dissolve

    #chat talks a little about stuff. Bong is sex pervert. 

    scene bg hallway with dissolve

    $soph.addmessage(sophie,"Okay, I'm back! So, let's get this date!")

    $soph.addmessage(sophie,"If you have to know, yes I was peeing. You guys are freaks.")

    scene bg dressing with dissolve

    ki "The dressing room is clean and simple. I'd like to stretch out for a nap, actually; the nerves have taken it out of me."

    ki "There are some clothes set aside in the closet. One of the producers and I talked about what I might wear to the dates beforehand."

    ki "So I have a simple black dress with matching shoes for one date, a jeans and tank top combo for another, and then a smart blue pantsuit with emerald blouse."

    $soph.addmessage(sophie,"So the game wants us to guess who might like which outfit?")

    $soph.addmessage(sophie,"Either that or this is just filler. Here in the real world I wouldn't make this choice without knowing where we're going.")

    $soph.addmessage(sophie,"Am I wearing a little black dress to go ice skating? Hey Bong, what do you think?")

    #bong is a perv

    $soph.addmessage(sophie,"Exactly.")

    menu:

        ki "So, for Cassandra's date I should wear..."

        "Little Black Dress":
            ki "I think she might like something simple. She's a musician, and a successful one, so she might take us somewhere classy?"

        "Jeans and Tank":
            ki "She's a rock star, so I think she might like a punkish getup. I feel good about this."

        "Pantsuit":
            ki "Something modern and classy. Granted, I doubt it'll match Cassandra's style, but contrast is cute sometimes."

    #endchoice

    scene bg black with dissolve

    ki "An hour passes like nothing. Like time somehow folded in on itself."

    scene bg hallway with dissolve

    show t with dissolve

    t "Hey, Kylie, looking great!"

    $soph.addmessage(sophie,"I bet she would have said that no matter what we picked.")

    k "Thanks. Is the car here? I want-"

    t "Yup! Let's go!"

    k "Oh? You're coming with?"

    t "Yeah. We'll actually film a little coverage track, maybe interview the staff about the place you're going. Some b-roll footage, maybe."

    k "Oh."

    t "Let's go!"

    scene bg black with fade

    jump cassDate1

