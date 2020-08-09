label robinDate1:

    # loading screen - Sevever

    scene bg load-sever with fade

    pause 22.0

    scene bg dressing with longFade

    play music2 bedroom fadein 0.4

    $showGui()

    ki "The morning and afternoon faded together. I had a few meetings with staff of the show and we shot some B roll of me going about my morning ritual."

    $chat.addmessage(shub, "was wonderin how the episodes of this show seem so short. hard to fill 45 minutes without B roll.")

    ki "Catering is my favorite part of the show so far. No pressure. Just coffee."

    $chat.addmessage(fizz, "B roll?")

    show c 1a at f12

    ki "I saw Cassandra around lunchtime, surrounded by her entourage. She was trying to get a slice of pecan pie."

    $chat.addmessage(crab, "its like background footage people talk over.")
    show c 1b
    ki "A wispy man took the plate right out of her hand."

    $chat.addmessage(crab, "Like you know how a news story on TV has an interview, then like a shot of traffic and people walking from the neck down happens.")

    ki "You've gained weight, he said, show some discipline."

    $chat.addmessage(elsa, "What a piece of work.")

    ki "She just nodded, sadly, while someone else in her group cut into the pie."

    ki "I felt Tania's hand on my shoulder."

    ki "It's impossible to know the burden someone else bears, she said."

    $chat.addmessage(fizz, "Ain't that the truth.")

    ki "I want to scream at that little man."

    ki "I do too, Tania said, but I don't think it's a problem."

    $chat.addmessage(crab, "Man, let her have some damn pie.")

    $chat.addmessage(shub, "that's the biz tho. she gotta be thin.")

    ki "She gestured with her head, subtly, toward one of the tables."

    stop music2 fadeout 3.0

    play music robin fadein 4.5

    ki "How Robin is so stealthy escapes me. She was sitting there, fingers curled around a coffee mug."

    ki "Her eyes were locked on that wispy little man."

    $chat.addmessage(cake, "this dude gonna turn up missing. you watch.")

    ki "She rose, and the entourage parted for her like the senate before Caesar."

    ki "Her eyes never left that little man's face."

    $chat.addmessage(bar, "This is like that one scene from that movie.")

    show c at mt3

    show r 1d at f12

    r "Your name."

    ki "The little man scoffed a quiet, unconfident scoff."

    $chat.addmessage(shub, "lol yeah. do you feel in control")

    ki "I didn't hear the name he gave. I did notice some of Tania's security officers paying closer attention, though."

    r 1a "Serve her."

    show c 1i

    ki "The little man's mouth hung open."

    ki "Excuse me, he said, I'm her agent, not her something else I didn't hear."

    r 1d "..."

    ki "She didn't answer. Just stared him down."

    ki "It was mesmerizing."

    show c 1q

    ki "Cassandra stood back, meekly."

    show r 1k

    ki "Exactly what will you do if I don't, he said, finding a bit of courage."

    r 2d "You will. Men like you exist to please women like me."

    ki "He stammered something to the effect of \"That's sexist\"."

    r 1j "Explain that to the tiny bulge in your pants."

    ki "... yeah, I looked. I don't feel good about it."

    r 2q "All that blood, flowing away from your little brain. I already own you, darling."

    $chat.addmessage(fon, "Robin wow. Wow, wow. :)")

    $chat.addmessage(shub, "man I'd tell this girl to piss off")

    show c 1b

    ki "Cassandra signed something in the air."

    ki "See, he said, she doesn't need it."

    show c 1k

    ki "Her expression told me he was lying."

    $chat.addmessage(cake, "sure Shub, right after you changed pants ")

    r 1g "Then serve me."

    show c 1h

    $chat.addmessage(shub, "you right")

    ki "He looked like he'd been slapped."

    r 2k "Cut a piece of that pie, place it on a saucer and hand it to me, you pitiful, pitiful clown."

    ki "With her size and accent, I think she missed her calling as a dominatrix."

    ki "Fine, he spat, if it'll get you to go away."

    r 1j "Good boy."

    show c 1q

    ki "I could hear Tania laughing. I'm sure her camera crew caught all of it."

    ki "I wonder if this was staged."

    $chat.addmessage(cake, "Well it's a reality show so")

    ki "The little man hurriedly cut a piece of pecan pie, plated it, and held it out to her."

    r 1m "..."

    ki "Don't you want this, he asked."

    r 2k "From you? Disgusting."

    $chat.addmessage(fizz, "Cold as ice.")

    ki "He'd gone red at this point."

    r 2a "Cassandra."

    show c 1s

    r 2m "Come."

    ki "Just like that, Robin turned on her heel and led a flummoxed Cassandra away."

    hide r at fr12
    pause 1.1
    hide c 1i at fr13

    ki "No one in the entourage attempted to follow."

    ki "The little man looked at each of them in turn."

    ki "Someone take this damn pie, he growled."

    $chat.addmessage(crab, "lol get rekt little boi")

    ki "See, Tania said, sometimes things take care of themselves."

    pause 0.1

    ki "Meeting Cassandra was intimidating. She's my musical idol, after all."

    stop music fadeout 3.0

    ki "Robin is something else entirely."

    $chat.addmessage(fizz, "vampire")

    pause 0.1

    ki "Speaking of Robin... what should I wear on our date? I wish I had a better idea of where we were going."

    pause 0.1

    s 1a "What should we wear this time?"

    play music lichelle fadein 3.0

    $chat.addmessage(fon, "That dress. :) Yum yum.")

    s "I think Robin's a dark-minded lady. A little scary."

    $renpy.notify("Robin seems awfully distracted. Perhaps get her attention.")

    s "She's got that sexy-dangerous thing going."

    python:
        newComments = [
            [bar, "I'd hit it, if I were pixels."],
            [elsa, "It could be a front, though. A black dress might also feel too matchy-matchy."],
            [shub, "go nekkid"],
            [crab, "pantsuit doesn't work for a bad bitch like Robin"],
            [cake, "fluck a pantsuit in general"]
        ]
        chat.bulkMessage(newComments, 0.33)

    menu:

        ki "So, I think Robin might like ..."

        "Little Black Dress":
            $chat.addmessage(elsa, "I hope we don't come across too desparate.")
            ki "It's fairly obvious Robin's color preference is black. Still, I wonder if she'd rather I contrast? Oh well."
            $outfitCurrent = "Dress"
            $outfitBlackDress += 1

        "Jeans and Tee":
            ki "Robin is super refined. Let's try a yin and yang thing."
            s "I can get behind that."
            $outfitCurrent = "Jeans"
            $outfitJeans += 1

        "Pantsuit":
            ki "Robin might respect a power move, right? Perhaps?"
            $outfitCurrent = "Pantsuit"
            $outfitPantsuit += 1

    # endchoice

    $chat.addmessage(bar, "Solid choice.")

    stop music fadeout 2.0

    ki "Okay, nerves. Pack your bags and let's go."

    play music hallwayChats fadein 3.0

    scene bg hallway with fade

    show t 1m at fr12

    t "Hello again, Kylie. Ooh, you look cute!"

    $chat.addmessage(elsa, "Tania's always got our back, it looks like")

    k "I hope so."

    t 1q "You sound discouraged?"

    $chat.addmessage(shub, "it's gonna come out that we can date Tania, rigt?")

    k "Not really. Last night was just pretty heavy."

    $chat.addmessage(cake, "Shub, you gettin into this bro")

    t 1m "It'll be easier for you tonight. Cassandra has a lot going for her but all that typing and screen reading can be draining."

    $chat.addmessage(elsa, "Sophie can prob relate to that dealing with us. Reading, playing AND speaking.")

    k "You think it'll be easier? If I'm honest, Robin kind of scares me."

    $chat.addmessage(bar, "She's a multi-tasking muthaflucka, muthaflucka.")

    t 1a "She's all edges, isn't she? Don't get wrapped up in her aura. Play along with her spooky chick thing and she'll open up to you."

    $chat.addmessage(fon, "You're such a poet, TwixtBar!")

    ki "I wonder what that entails."

    k "As long as she doesn't open ME up."

    t 1t "Oh, you're perfectly safe. Don't you worry about a thing!"

    $chat.addmessage(crab, "TwixtBar, you're next it seems.")

    s 1a "Tania being all suspicious."

    $chat.addmessage(bar, "Yeah no")

    k "Where do you think Robin's going to take me? I feel so damn unprepared."

    t 1a "I mean, I know where she's taking you because we need to know in advance to get permission to film."

    $chat.addmessage(fon, "... you all think poorly of me.")

    k "But you won't tell me."

    t 1q "Nope! Sorry, we need your reaction to be authentic. Aren't you excited about it, though?"

    $chat.addmessage(elsa, "You all should stop being mean to Fontaine.")

    t "I mean, you've seen her in action. She's --"

    k "-- otherworldly."

    $chat.addmessage(shub, "We're just being assholes, ElsaLater, no harm meant.")

    ki "Tania pauses a little at that, as if considering whether to agree."

    t 1a "That's a good way to put it. Don't let her aura scare you off though. She can't help she's tall."

    $chat.addmessage(bar, "I'm married, first off, and second off, I never accept private chat requests. Sorry Fontaine.")

    $chat.addmessage(fon, "I forgive you.")

    k "Should I bring something to stand on for our date?"

    t 2t "Oh? Thinking you might need to be at, let's say, lip level?"

    s "Spicy!"

    ki "I'm actually blushing. Well played, Tania."

    $chat.addmessage(crab, "drama hours in this chat")

    k "I don't know yet. Maybe."

    t 2m "I'm rooting for ya!"

    scene bg black with fade

    $chat.addmessage(cake, "Hey Fontaine.")
    $chat.addmessage(fon, "Yes poundCake?")

    ki "Like before, the car ride is uneventful. Tania sits in the back with me, smiling my way every so often but mostly looks in her phone."

    ki "I find myself taking a little time to consider her. She's the master of ceremonies for this strange, time-crunched dating show. She's attractive, but apparently not at all interested in participating."

    $chat.addmessage(cake, "is your name actually Fontaine? Or like, Brittany. Or something else.")

    ki "I wonder if that's a contractual thing or if she's just off limits somehow?"

    $chat.addmessage(fon, "My real name is Fontaine L'eau.")

    ki "Either way, I spend the rest of the ride looking out the window and wondering what the hell I'm going to have to say to Robin."

    python:
        newComments = [
            [bar, "Like hell."],
            [elsa, "Your handle?"],
            [shub, "your name is fountain water. Bullshit. I'm a call you Claire."],
            [fizz, "Really?"],
            [fon, "It really is. Shub-Nickelrath you can call me whatever you want~~~"]

        ]
        chat.bulkMessage(newComments, 0.7)

    s 1a "Wait, Fontaine, are you for real? Where are you from?"

    $chat.addmessage(fon, "Oh, all over.")

    s "I just ask because it's an unusual first name."

    $chat.addmessage(fizz, "I think it's a great name.")

    $chat.addmessage(fon, "FizzyFizion I think you're great. ;)")

    s "Let's not dwell too much, though. Let's move on!"

    scene bg playhouse far with fade

    k "Oh my god, is this the place she owns?"

    show t 1a at fr12

    t "Yup. This here is Ganymead Performing Arts Center."

    k "Why is 'Ganymede' spelled wrong?"

    $chat.addmessage(bar, "They spelled Ganyme-- yes, that.")

    t "There's a bar at the back of the theater for after parties. Mead, you know."

    $chat.addmessage(elsa, "I'm on the fence. Is that cute or cringe?")

    k "Oh."

    ki "I still don't get it."

    $chat.addmessage(crab, "It's stupid.")
    $chat.addmessage(shub, "it great")
    $chat.addmessage(cake, "dunno")

    s 1m "Portmanteaus are cute, though!"

    t 1q "Robin's here somewhere. Probably hanging by her feet from the rafters taking a nap."

    k "Hanging what now? Oh."

    t 1m "Like a bat."

    $chat.addmessage(fon, "No spoilers, but poor Robin doesn't mean anything by being so spooky :(")

    k "Like a bat, yes. Gotcha."

    $chat.addmessage(elsa, "Fontaine, you've finished this game before right?")

    t 1l "You really are a ball of nerves. Breathe, girl. Remember, the worst thing that can happen is you still get paid at the end."

    $chat.addmessage(fon, "I know how it ends ;)")

    k "I guess I--"

    play sound "sounds/Lights Out.mp3"
    stop music fadeout 0.5
    scene bg black

    pause 0.5

    $chat.addmessage(fizz, "Jesus! I turn my head for one second get flippin' jumpscared.")
    $chat.addmessage(shub, "lol")

    k "What the fu--"

    t "Lights, yes, ha ha, the lights went out! We're an evening TV show, Kylie."

    $chat.addmessage(bar, "dancin in the dark")

    k "Is this supposed to be happening?"

    pause 1.5

    k "Tania?"

    pause 1
    $chat.addmessage(elsa, "Spooky. Fontaine, hold me.")

    ki "I knew it. I knew this was a setup. I knew --"
    $chat.addmessage(fon, "Yes please :)")

    $chat.addmessage(beav, "HELL YEAH")

    play sound "sounds/Lights Out.mp3"
    scene bg playhouse near
    play music robin fadein 1.0

    show r 1m at i12

    r "You seem unsettled draga mea."

    ki "Her voice pours through the receding dark, musical and so, so close."

    $chat.addmessage(crab, "This some rasslin' B.S. right here")

    k "Jesus Christ, Robin! What in the world made you think this was a good idea for a date?"

    r 1q "Is your blood not pumping?"

    $chat.addmessage(cake, "last tiem I scared the hell out of a date it did not end in cuffing.")
    pause 0.5


    ki "It is. My face is flushed, I feel hot. I'm not scared. I could smell her perfume before the lights came up."

    $chat.addmessage(fizz, "Or cuffs in general, right?")

    ki "And it's comforting. I don't know what it is, but the scent puts me at ease."

    $chat.addmessage(elsa, "Sophie I need to brb")

    s 1a "Bet it smells like chloroform. Oh, Elsa, you're fine. We're playing at our own pace here."

    $chat.addmessage(shub, "private chat, eh?")
    $chat.addmessage(elsa, "Shut up, Shub, I'll bring back Bong if I find him.")

    k "I... you have my heart racing, for sure."

    $chat.addmessage(cake, "take pics")

    r 1m "I apologize papillon. Stagecraft is my life, and so I thought I might show you just a bit."

    ki "Her voice thrills me. It's at once dangerous and comfortable, and I can't place the accent for the life of me."

    $chat.addmessage(beav, "Y'know, Egg's been awful quiet too.")

    k "What does draga mea mean?"

    r 1o "It means I am fond of you, Kylie."

    $chat.addmessage(fizz, "Hang on.")

    k "You're pretty fond of Cassandra, too."

    pause 0.1

    show r 1b

    r "I am."

    $chat.addmessage(crab, "hangin low bruv")

    k "I saw you defending her at catering this afternoon."

    pause 0.1

    r 1j "Was I?"

    k "Weren't you?"

    pause 0.1

    r "Cassandra is perfectly capable of standing up for herself."

    k "But she didn't."

    r 1b "No. She did not." 
    
    $chat.addmessage(elsa,"I do think Robin might have overstepped with Cassandra.")

    pause 0.5

    k "..."

    pause 0.5

    r 1g "You'd like me to elaborate." 
    
    $chat.addmessage(bar,"You think? Like she might feel Robin made her look like a little kid.")

    k "... yes."

    pause 0.5

    r 1b "Cassandra must have made quite an impact on you, darling."

    r "Perhaps I'm too late." 
    
    $chat.addmessage(cake,"y'know it is kinda unfair to have to go second.")

    ki "A chill washes over me."

    k "I... no. No, it isn't like that."

    k "I'm drowning, aren't I."

    pause 0.4

    r 1q "Not at all. If either us have drowned, it's me."

    pause 0.2

    ki "... could I be more awkward?"

    r 1b "I owe a great debt to Cassandra. That's all. I also owe a great debt to you."

    k "We just met." 

    r 2m "Are you sure?" 
    
    $chat.addmessage(crab,"dun dun dunnnn")

    k "Uh, yes?"

    r "Mm. Perhaps I'm mistaken my dear, but I feel as though we've been acquainted for quite some time."

    $chat.addmessage(cake, "lol")

    ki "Wha?"

    s 1a "You said it, Kylie."

    $chat.addmessage(elsa, "Fontaine really is gorgeous wow")

    r 2n "Come, come. We should have our dinner, don't you think?"

    $chat.addmessage(shub, "What kinda chat is she sending?")

    k "Oh, uh, sure. Where are we going?"

    $chat.addmessage(elsa, "her eyes are haunting and she's just wow")

    r 2m "Right here."

    $chat.addmessage(beav, "You paying for that chat by the minute?")

    ki "That's it. She's going to cook me."

    show r at justFade

    stop music fadeout 4.0

    ki "Robin turns and beckons to me, carelessly, as if she's only here in my imagination."

    hide r

    $chat.addmessage(fizz, "Yeah I just read back in the chat a ways and Egg really hasn't said a thing for a while.")

    ki "Conscious of the camera crew wavering around us, I follow her down the auditorium walkway and to the stage stairs, noticing the smoothness of her steps, the way her hair seems to sway in slow motion."

    $chat.addmessage(sophie, "Chat currently paused. Feel free to hang around, it's temporary!")
    pause

    ki "She really is otherworldly."

    s 1r "I feel like the game wants me to pick Robin. What do you think, chat?"

    s 1a "Wow, what did I miss? Elsa and Fontaine vanished for a private chat?"

    stop music fadeout 3.0

    s "I feel like my stream became a meet-cute parlor. Ha!"

    pause 1.0

    s 1b "No comment? Oh. Oh! Sorry, I must've paused the chat by accident. Sorry!"

    

    $chat.addmessage(beav, "That's what I think, anway.")

    show r 1m at f12

    play music darkNoodle fadein 2.4

    r 1m "I hope you don't mind, I turned down Tania's offer to pay for our meal."

    $chat.addmessage(fizz, "That's probably what's happening.")

    ki "At center stage there's a table set, ringed with gentle candlelight."

    ki "Wait. The candles are artificial. I suppose fire on stage would be a terrible idea, wouldn't it?"

    $chat.addmessage(shub, "alt babe gets me dinner. Why is this even a contest.")

    k "Oh, then what are we having?"

    pause 1.0

    r 1j "Your favorite, of course."

    ki "How on earth would she know--"

    $chat.addmessage(cake, "big spooky")

    k "Okay, hang on. Robin, I'm game, but how would you know what I like?"

    hide r at f12

    ki "She moves like a whisper from the stairs to the table, and I follow, curious, nervous."

    $chat.addmessage(cake, "AsMR lol")

    ki "She lifts a platter cover from one of the place settings."

    show r 1b at f12

    r "Was I wrong, papillon?"

    $chat.addmessage(crab, "it's some fast food bullshit")

    ki "A chip of ice races along my bloodstream. On the platter there sits a fragrant bowl of coq au vin, warm with the scent of pearl onions and bacon, along with a plank of brie crusted in almond slivers and honey. The scent floats languidly above Robin's delicate perfume."

    $chat.addmessage(fizz, "Fancy.")

    k "How did you know?"

    $chat.addmessage(crab, "not that fancy. friggin french food overrated AF")

    r 1p "Because we've been friends for so long, papillon."

    s 1i "Wait, what."

    $chat.addmessage(cake, "broooooo")

    k "Have we met before? There's no way I wouldn't remember you."

    r 1b "I'm flattered, of course. I served you this dish once before, in a little shop not far from the Seine. I wasn't so tall back then."

    r "You dressed differently, then."

    $chat.addmessage(beav, "Here we go.")

    if outfitCurrent == "Dress":
        ki "She pauses, obviously for effect. Everything she does seems calculated for effect."
        r "You have me at a disadvantage, dear. It's difficult not to stare."
        ki "As if I wasn't self-conscious enough."
        k "It's a little, uh... you don't like the dress?"
        r 1m "I couldn't love it more if I were created expressly to love it, papillon."
        r "So... forgive me if my gaze lingers, won't you?"
        k "Maybe."
        ki "Her smile is warm, briefly. I could be wrong, but I feel like both of us are a little more comfortable than a moment ago."

    if outfitCurrent == "Jeans":
        r "You're a bit more casual, I suppose."
        k "So my other choices were a pantsuit and a dress that was basically a napkin and some strings."
        k "I didn't want to come across too forward, I guess."
        ki "Huh. Self, that was an awfully forthright answer."
        ki "Robin, I discover, has a habit of bending her left wrist and tucking her thumb when she's thinking."
        r 1m "It is the woman beneath the fabric who interests me, darling. Nothing more."

    if outfitCurrent == "Pantsuit":
        r 1m "I am impressed by your style, darling."
        k "Oh? Thank you!"
        r "I wonder what your intention was in choosing such a statement outfit."
        ki "Uh-oh."
        k "Oh, no statement. I just didn't think my other options were... hm."
        r 1j "Were what, dear?"
        k "Classy enough for you, I guess?"
        pause 0.5
        r "Papillon. You overestimate me."

    $chat.addmessage(beav, "Well, hell. I wonder which choice was actually right.")

    k "I don't--"

    $chat.addmessage(bong, "01010100 01101000 01100101 00100000 01100100 01100001 01110100 01100001 00100000 01100110 01100101 01100101 01101100 01110011 00100000 01110011 01101111 00100000 01100111 01101111 01101111 01100100") 
    
    $chat.addmessage(fon,"Shh") 
    
    $chat.addmessage(fon,"Hush now.")

    pause 1

    $getHistory(3)

    ki "But I do. I remember. I remember my freshman year of college and how I took French classes entirely to take a trip to Paris."

    $chat.addmessage(fon, "Sophie, have you ever been to Paris?")

    pause 0.4

    s 1m "You're back fast this time, Fontaine. Yeah, I have been to Paris, I went in college."

    $chat.addmessage(fizz, "Too much coincidence?")

    s 1q"I never took French, though. I took two years of Spanish and promptly forgot all of it."

    stop music fadeout 3.0
    

    r 2b "I was different then. Lesser. But I am a deft hand in the kitchen, papillon."

    $chat.addmessage(elsa, "Back.")

    play music2 robin fadein 3.0

    ki "No. I do remember. I remember her scent. That's why..."

    $chat.addmessage(shub, "Hey ElsaLater came back sooner. XD XD XD")

    k "Oh my god! So that's why you seemed so damn familiar."

    ki "Her expression now, it's dark but searching. Meaningful."

    $chat.addmessage(elsa, "Yup, safe and sound. Obviously.")

    r 1m "Is that alright?"

    $chat.addmessage(cake, "yo Fontaine, Elsa said you're a stone-cold cutie")

    ki "I remember, now. I remember the little bistro overlooking the river and the girl behind the counter who served me a plate of coq au vin with tears in her eyes. I remember how unsettled I felt."

    $chat.addmessage(elsa, "That's NOT what I said")

    ki "'Why are you crying? Is everything okay?' I had asked. She had only nodded, eyes sparkling, and said 'It is the first time.' I remember she had a heavier accent that didn't fit in Paris."

    $chat.addmessage(fon, "Elsa is much cuter than I. ")

    k "I don't remember you being so tall though."

    r 1q "I was fifteen when we met, draga mea."

    $chat.addmessage(shub, "15, eh? is that anime 15 or real life 15?")

    k "Holy god you're only 19?"

    # set Robin's age from default 24 to 19 because's a big ol liar
    $robinBio.setAge(19)

    $chat.addmessage(beav, "anime 15 creeps me out. Man.")

    s "No way. There's no way."

    $chat.addmessage(elsa, "SO ANYWAY Robin knows Kylie from her past? Weird.")

    k "Didn't Tania say everyone was 20? And how do you own this place?"

    r 1m "Your food is getting cold."

    $chat.addmessage(fon, "Robin is so mature for her age. We love her, don't we.")

    k "I'm sorry, I just have a million questions."

    $chat.addmessage(fizz, "Dunno about that, but she dodges questions like they were wrenches.")

    stop music2 fadeout 3.0

    play music darkNoodle fadein 4.0

    r 2l "I know. And I have a few answers for you, as well. But for now, please. Your kind words about my cooking changed everything for me, darling, please let me see if I still deserve them."

    $chat.addmessage(crab, "We? speak for yourself Fontaine. bitch creeps me out.")

    hide r at f12

    ki "We sit, she at one end and I at the other. Tania had to know about this, right? How in the world did this happen?"

    $chat.addmessage(fizz, "Now, now, no casual sexism in the chat :D")

    scene bg playhouse far with fade

    ki "The food is sublime. It isn't as if coq au vin is a life-changing dish but the weight of her story lends fullness to the flavor."

    ki "The brie is tender in that almost-not-quite-creamy sort of way, sweet and crunchy on top from the honey and almonds. Robin is a deft hand, that much is certain."

    $chat.addmessage(beav, "Makes me want a big-ass roast chicken.")

    k "If I eat another bite I'm gonna pop."

    show r 1u at fl12

    r "Please, don't. It took too long to find you again draga mea, I would hate to have to clean you up."

    k "Aren't you eating?"

    $chat.addmessage(fizz, "She's a vampire, isn't she.")

    ki "I hadn't even noticed her platter still sitting covered. Robin sits, legs neatly crossed, leaning on her open palm with a serene expression."

    r 1t "I am devouring you, darling."

    $chat.addmessage(cake, "hell no, vampires can GTFO")

    ki "A nervous chuckle passes my lips."

    r 1u "It was against my father's wishes I left Bucharest for Paris. He wanted the life of a businesswoman for me, a trader in my family's enterprises."

    ki "Her eyes unfocus, slightly. It's as if she's devoting too much energy to the story she's about to tell."

    $chat.addmessage(fizz, "So she's Romanian. Definitely a vampire.")

    k "What did your family do?"

    $chat.addmessage(cake, "lol facts")

    r 1a "Contracting, mostly. It was not to my liking. And so, I spent years in France living with a cousin to study cuisine. Until I met you, papillon."

    $chat.addmessage(fizz, "Why would they make it that obvious?")

    s 1a "Don't you guys think all of this is too easy? Like I get this is a cheesy dating sim and all, but you mean to tell me this girl fell in love with me at first sight?"
    s "Then she tracked me down on this show while also becoming a playhouse owner?"

    $chat.addmessage(crab, "You ever see 'Single White Female'?")

    k "Why would you follow me, though? All I did was praise your skill."

    r 1p "The thirsty come to me for water, remember?"

    $chat.addmessage(fon, "Her sad face is so endearing :(")

    r 1b "You... you brought me water, Kylie."

    k "I don't know what to say."

    $chat.addmessage(elsa, "Aww")

    r 1a "Say you will meet with me again. And again."

    k "It's so much to take in, Robin. I don't even know who you are, not really."

    r 1b "Am I not pleasing to your eye?"

    $chat.addmessage(cake, "everybody's in a hurry but it makes sense being a datin show")

    k "It's not that, you're..."

    s "Exactly my type!"

    $chat.addmessage(bar, "Same")

    k "You're hot. And I'm kind of afraid of you."

    r 1r "Oh? Because I searched for you?"

    $chat.addmessage(shub, "among other things ya gd vampire")

    k "Because the way you're looking at me makes me feel like you're going to cook me."

    r 1u "Perhaps."

    $chat.addmessage(beav, "FLUCKIN CALLED IT")

    show r 1j

    k "See, that's what I mean! I don't know if it's part of your persona or if you're being metaphorical and sexy or if you're going to bite my neck and suck my blood!"

    $chat.addmessage(fizz, "Red herrings everywhere.")

    ki "Oh wow, those words just came tumbling out of my mouth, didn't they."

    r 1a "I'm no vampire, papillon."

    k "So what am I supposed to think?"

    $chat.addmessage(elsa, "I like that Kylie automatically believes in vampires.")

    show r 2s

    ki "She rises then, looming enormous over me, and my skin freezes."

    $chat.addmessage(crab, "'bout time we got some H in this :P")

    r 1u "Whatever you like, my dear. I wish only to feed you, and see you smile the way you smiled that day on the Seine."

    ki "My heart hurts from hammering in my chest. My arms and legs hang like noodles. She lowers herself to me, kneeling so close I can smell her lipstick, tart and chemical."

    # sound effect of lights shutting off
    stop music fadeout 0.4
    play sound "sounds/Lights Out.mp3"
    scene bg black

    $chat.addmessage(cake, "GOD")
    $chat.addmessage(elsa, "ahgp")

    pause 2.0

    s "Oh my god why."

    $chat.addmessage(fon, "hahahaha hahahaha")

    pause 2.0

    k "Robin? Okay, this is not cool!"

    $chat.addmessage(fizz, "I wonder what kind of team Robin has in place making this stuff happen.")

    pause 1.0

    k "Robin?"

    pause 1.0

    $chat.addmessage(shub, "SPOOOP")

    k "Hello?"

    ki "Silence. Just silence."

    $chat.addmessage(elsa, "She's committed to her act if nothing else.")

    k "Tania? Robin?"

    pause 1.0

    $chat.addmessage(crab, "This isn't a horror game is it?")

    k "Hey! I can't... is someone there? Anybody? This isn't fun anymore!"

    $chat.addmessage(fon, "Crablegs, it isn't. You can relax. :)")

    pause 1.0

    play music robin fadein 3.0

    ki "And then, a soft brush of something firm against my cheek. The sound of lips plucking gently away."

    ki "A whisper."

    r "{alpha=0.5}Shh. I'll see you again, papillon.{/alpha}"

    # sound effect of lights
    stop music fadeout 0.2
    play sound "sounds/Lights Out.mp3"
    scene bg playhouse far

    pause 0.25

    $chat.addmessage(fizz, "Hot/Terrifying if that happens in reality.")

    k "Hey!"

    ki "When the lights come up, Robin is gone. The platters are gone, too. A thousand thoughts ricochet in my mind."

    $chat.addmessage(elsa, "I said it before, but imagine if that were a man pulling that trick.")

    ki "How did she do that? I couldn't hear anything moving or clattering. I'm stuck between heart-poundingly impressed and horrified."

    $chat.addmessage(crab, "So are women just as dangerous as men or are women weaker and less dangerous, Elsa?")

    $chat.addmessage(crab, "Can't have it both ways.")

    s 1i "Guys, don't ever pull that on someone on a date! Oh my god."

    show t 1d at f12

    $chat.addmessage(elsa, "I'm just saying if it was me I'd be scared to death if it was a guy.")

    t "Robin, you ass! You and Cassandra both trying to hide the important stuff!"

    $chat.addmessage(cake, "Sorry, crab's always bitchin about gender politics")

    pause 0.02

    $chat.addmessage(shub, "probalby why my boi can't get a date right")

    t 1k "Hey Kylie, you good? I had no idea she was planning that."

    $chat.addmessage(crab, "STFU bothaya.")

    t 1q "Oh. You have, uh, something on your cheek."

    ki "My fingers easily find the smooth lipstick mark, but I rub off a little and look at it anyway."

    $chat.addmessage(beav, "need to be specific about which cheek :D :D :D")

    ki "My heart's fluttering."

    k "I'm okay."

    $chat.addmessage(unkn, "stringSever(firstName)")

    t 1u "You look so out of it."

    k "I... I don't know what I'm feeling right now."

    $chat.addmessage(fizz, "Elsa, how would you feel in Kylie's exact spot?")

    ki "I just know I want more. The rush, the rush engulfs me."

    k "That was some date."

    $chat.addmessage(elsa, "I dunno. I like theatrical stuff, so I'd be smiling I think.")
    $chat.addmessage(elsa, "And Robin's attractive to me, so... yeah.")

    t 1m "I don't think that counts as a date. You talked for like 15 minutes."

    k "I get the feeling Robin isn't much for small talk."

    $chat.addmessage(beav, "Hot.")

    t "She's not. She-"

    # sounds/Lights Out
    play sound "sounds/Lights Out.mp3"
    stop music fadeout 0.2
    scene bg black

    pause 2.0

    $chat.addmessage(fizz, "Didn't get me that time, Robin!")

    t "God dammit, Robin!"

    ki "The lights are gone. My heart races again. Is she back? I brace for some sensation against my skin, terrified it will come and never come in the same instant."

    k "Language, Tania. We-"

    t "We'll edit, don't cover for her!"

    $chat.addmessage(cake, "This must be frustrating for Tania.")

    pause 1.0

    ki "There."

    k "Oh..."

    r "{alpha=0.3}Shhh.{/alpha}"

    ki "It's gentle, and brief. I can smell her perfume again, her hands enfolding my shoulders. Her lips, there and gone, against mine. A brush, nothing more. I'm paralyzed in the moment."

    ki "Her lips linger."

    $renpy.notify("Robin admires honesty. Mislead her at your peril.")

    menu:
        s "What should we do?"
        "Kiss back":
            ki "There's no way I could restrain myself."
            ki "She's too... she's too much. Too everything."
            pause 0.5
            ki "But as I move forward, she pulls back."
            ki "A stab of fear. Was I wrong?"
            ki "But then, her mouth is on mine. Just as I stopped moving she..."
            ki "Her hands are everywhere. Somewhere. Nowhere at all."
            ki "She tastes like sweetened, spiced rum."
            ki "And then, breathlessly, it's over. I can hear a soft gasp from her as our lips part."
            r "{alpha=0.3}Let's do this again, darling.{/alpha}"
            $ loveRobin += 1
            $ kissedRobin = True
            $chat.addmessage(elsa, "... wow.")

        "Hold back":
            ki "The effort it takes to hold back is phenomenal."
            ki "... but I do. Her breath licks warm at my lips, but she's not pursuing."
            ki "She smells heavenly."
            r "{alpha=0.3}I will prove worthy of your kiss, papillon.{/alpha}"
            ki "Her tone, though a whisper, isn't disappointed. If anything, it sounds invigorated."

    t "Robin?"

    $chat.addmessage(elsa, "Okay, yeah. That would be such a rush.")

    pause 1.0

    $chat.addmessage(shub, "teasin' ass goth vampire chef")
    $chat.addmessage(cake, "hot either way")

    pause 1.0

    r "Goodnight, my darlings."

    ki "Her voice flows from somewhere far away, echoing lightly."

    $chat.addmessage(cake, "lol")

    t "Robin! Turn the damn lights back on!"

    

    $chat.addmessage(egg, "")

    # sound
    play sound "sounds/Lights Out.mp3"

    scene bg playhouse far
    
    show t 1d at i12

    ki "I'm breathless, still sitting in the dining chair, when the lights come back up."

    t "That's not funny! Kylie..."

    $chat.addmessage(fon, "Poor Tania. She just has no control.")

    ki "She's staring at me, at my fingertips resting against my lips."

    t "Oh you have got be kidding me. My cameras can't see in the dark!"

    $chat.addmessage(fizz, "It's almost like the dates are intentionally sabotaging the show.")

    t 1k "Oh well. Guys, get in here and get her face. Make sure you can see the lipstick."

    t 1a "We'll cut it into something great. Somehow. Robin, if you're still here somewhere I want to talk to you!"

    $chat.addmessage(elsa, "Hey Robin, I like food too!")

    ki "There's no response. I wonder if she's really gone or if she's nearby, still. Watching."

    ki "It's... exciting."

    $chat.addmessage(beav, "Yeah it is.")

    t 1o "Okay. Kylie, I guess it's time to go then. Can you walk, or are your legs jelly?"

    $chat.addmessage(cake, "wonder what elsa is jelly lol")

    scene bg black with dissolve

    $chat.addmessage(elsa, "Piss off, poundCake. Why straight men thing bi or lesbian women are so attractive blows my mind.")

    ki "The car ride home lasts an eternal instant. Cassandra's voice moved me, deeply. Her trust in me, to show the secret she showed, floored me. And yet, Robin..."

    $chat.addmessage(shub, "But Robin's not real.")

    $chat.addmessage(elsa, "So?")

    ki "She might really have stolen my soul."

    scene bg hallway with dissolve

    play music hallwayChats fadein  2.2

    pause 0.25

    $chat.addmessage(cake, "he means you thnk Robin's attractive, but she's fake so you'll never have a shot at her")
    $chat.addmessage(crab, "just because someone won't sleep with ya doesn't mean she's not attractive. Married girls, movie stars, celibate monks.")

    show t 1o at f12

    t "Hey. I know Robin's got this weird carny spectacle thing going, and I know I said you should open up to her spooky act, but..."

    $chat.addmessage(shub, "family members")

    t 1q "... are you okay?"

    $chat.addmessage(fizz, "lol, you guys are ate up")

    ki "She hadn't spoken at all on the ride back. Why suddenly now?"

    k "I'm fine. I've never had anything like that happen before."

    $chat.addmessage(elsa, "I guess that makes sense. You're still perverts.")

    t 1a "Christ, I hope not. I mean, we're a TV show and no one's ever pulled a stunt like that."

    $chat.addmessage(shub, "yup")

    k "I didn't expect it. I didn't expect her to kiss me. Just, just like that."

    
    $chat.addmessage(crab, "true")
    $chat.addmessage(cake, "it's on my birth certificate, ye ye")

    t 1r "I just wonder how many people were hiding in there. No way she moved that table on her own and did all that stuff from the stage."

    k "I have no idea."

    $chat.addmessage(unkn, "R/BG13:14-15")

    ki "It's hard to think, even now. I feel drained, like all of my energy has been spent dissecting those few minutes in the dark."

    s 1i "Oh my god what if someone else kissed me? I mean, I guess the game made a point to tell us it was her, but still, weird!"

    $chat.addmessage(beav, "like a fishbowl party")

    t 1m "Get some sleep. We'll have a little round-up tomorrow on the main stage, but it'll be later in the day so you can rest."

    k "Yeah."

    hide t at f12

    $chat.addmessage(elsa, "I don't want to know, do I?")

    ki "So, so tired."

    scene bg dressing with dissolve

    $chat.addmessage(beav, "Depends on if Fontaine and Robin are going")

    ki "I don't even have time to consider much more. I didn't even intend to flop directly on the bed and drag a pillow under my head. It just... kind of happened."

    $chat.addmessage(elsa, "Just because I think women are attractive you think I'm lesbian?")

    scene bg black with dissolve

    $chat.addmessage(bar, "I assumed you're a guy pretending to be a gay woman to mess with people.")

    stop music fadeout 4.0

    pause 1.0

    s 1a "Wow, okay. Chat, I think I'm gonna need a minute after that. Like Robin's gorgeous and mysterious and everything and apparently we have a backstory, which is kind of too convenient."

    s "I guess I wish they put more effort into coming up with a reason for Kylie and Robin to bond. Cassandra had her own thing, right?"

    $chat.addmessage(elsa, "Fair. Wrong, but fair.")

    s "But then, I guess maybe the game wants me to avoid picking Robin because she's the obvious choice? But maybe it wants me to think that."

    $chat.addmessage(fizz, "Doesn't seem that obvious to me")

    pause 1.0

    s "Either way, I'll be right back. Try not to get too rowdy without me!"

    show image splashBRB at alphaFade

    pause 1

    show image splashHorror:
        alpha 0.05

    play music onTheNod fadein 1.0

    python:
        # split string into whole words. The create lists, each entry emulating message object.
        newComments = []
        temp = "I theorize the mind of the one fragments the mind of many, forming many and one."
        temp2 = temp.split(" ")
        for i in temp2:
            newComments.append([egg, i])
        chat.bulkMessage(newComments, 0.4)

        newComments = []

    pause 1.0

    python:
        for i in chat.history:
            if i.person == egg:
                chat.history.pop(i)

    $chat.addmessage(crab, "Let me put it this way, Elsa. What's two plus two.")

    pause 2.0

    $chat.addmessage(elsa, "I mean, four. Why.")

    scene bg black with fade

    stop music fadeout 1.0

    $chat.addmessage(shub, "there he goes again lol")

    $chat.addmessage(crab, "So like boobs, right? What's better than two?")

    s 1a "Okay chat, I'm back. So, who do you guys think between Cassandra and Robin?"

    $chat.addmessage(elsa, "... okay fair.")
    $chat.addmessage(fon, "A beautiful man like you, Crablegs. ;)")

    s "I'm stuck. I feel like Cassandra's all pure and real, and then Robin's all dark and theatrical. Like, how much of what Robin's saying is an act?"

    $chat.addmessage(crab, "Right. Also, Fontaine, you have no idea what I look like.")

    s "They're also friends. What happens if I pick one? Is the other hurt?"

    $chat.addmessage(fon, "Wanna hear something really spooky?")

    s "You guys have no opinion on Robin or Cassandra? Or are we all too tied up in lesbian discussions?"

    $chat.addmessage(crab, "finally Sophie speaking my language ;) Also, sure Fontaine.")
    $chat.addmessage(fizz, "Fontaine, I hope you aren't about to turn out to be a hacker spy or something.")

    s 1m "Whatcha got, Fontaine? I'm curious."

    $chat.addmessage(beav, "Robin has my vote. She's freaky.")

    pause 1.0

    $chat.addmessage(fon, "Crablegs is five foot nine. He has a fade haircut. He is Canadian. He is interested in women. He enjoys bluegrass music and has brown eyes.")

    pause 1.0

    python:
        newComments = [
            [elsa, "Wait is she right?"],
            [bar, "dafuq"],
            [beav, "she wannabe Anonymous"],
            [crab, "c'mon girl"],
            [cake, "she right"]
        ]
        chat.bulkMessage(newComments, 0.8)

    pause 1.0

    s 1h "The hell?"

    $chat.addmessage(fon, "Relax, relax. He sent me his dating profile. ;)")

    python:
        newComments = [
            [elsa, "Phew"],
            [bar, "lame"],
            [crab, "Hey, c'mon now, don't be tellin"],
            [fizz, "Stands to reason."],
            [beav, "she right"]
        ]
        chat.bulkMessage(newComments, 0.8)

    pause 1.0

    s 1a "Fontaine, you're devious, you know that?"

    $chat.addmessage(fon, "I try ;)")

    s "You guys feel like going on if I take, like, a half hour break? I'm starting to feel a little uninspired."

    python:
        newComments = [
            [fon, "I'll be here for you anytime, sweet Sophie :)"],
            [shub, "I ain't goin anywhere"],
            [bar, "I gotta do some yoga anyway"],
            [crab, "might be here"],
            [cake, "I'm gonna play some Resident Sequel."]
        ]
        chat.bulkMessage(newComments, 0.8)

    pause 1.0

    s "Cool. Back in a bit!"

    $chat.addmessage(elsa, "Have fun.")

    pause 0.3

    python:
        hideGui()
        getHistory(4)

    
    pause

    jump realWorld1