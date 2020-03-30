label robinDate1:

    # loading screen - Sevever

    scene bg load-sever with fade

    pause 4.0

    scene bg dressing with longFade

    $showGui()

    ki "The night passes in temporal nonexistence."

    $chat.addmessage(fizz, "Edgy.")

    ki "I thought it would sound cool when I thought of the phrase, but I guess it's douchier than all that."

    $chat.addmessage(bar, "I kind of like that she's a dork.")

    s "Whoops. I think the game devs left a comment in."

    ki "The morning and afternoon faded together. I had a few meetings with staff of the show and we shot some B roll of me going about my morning ritual."

    $chat.addmessage(shub, "was wonderin how the episodes of this show seem so short. hard to fill 45 minutes without B roll.")

    ki "I guess it'll be dubbed over with the interview I did about Cassandra. I don't have time to think about last night now, though, because in a very short time there's an Eastern Bloc Goth Dream Girl in my future."

    $chat.addmessage(fizz, "B roll?")

    $chat.addmessage(crab, "its like background footage people talk over.")

    ki "Speaking of Robin... what should I wear on our date? I wish I had a better idea of where we were going."

    $chat.addmessage(crab, "Like you know how a news story on TV has an interview, then like a shot of traffic and people walking from the neck down happens.")

    s "Hey guys. Wow, crab, you know your stuff! So what should we wear this time?"

    $chat.addmessage(liv, "That dress. :) Yum yum.")

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

    ki "Okay, nerves. Pack your bags and let's go."

    scene bg hallway with fade

    show t happy with dissolve

    t "Hello again, Kylie. Ooh, you look cute!"

    $chat.addmessage(elsa, "Tania's always got our back, it looks like")

    k "I hope so."

    show t disap

    t "You sound discouraged?"

    $chat.addmessage(shub, "it's gonna come out that we can date Tania, rigt?")

    k "Not really. Last night was just pretty heavy."

    $chat.addmessage(cake, "Shub, you gettin into this bro")

    show t speak

    t "It'll be easier for you tonight. Cassandra has a lot going for her but all that typing and screen reading can be draining."

    $chat.addmessage(elsa, "Sophie can prob relate to that dealing with us. Reading, playing AND speaking.")

    k "You think it'll be easier? Because if I'm honest, Robin kind of scares me."

    $chat.addmessage(bar, "She's a multi-tasking muthaflucka, muthaflucka.")

    t "She's all edges, isn't she? Don't get wrapped up in her aura. Play along with her spooky chick thing a little bit and she'll open up to you."

    $chat.addmessage(liv, "You're such a poet, TwixtBar!")

    ki "I wonder what that entails."

    k "As long as she doesn't open ME up."

    show t flirty

    t "Oh, you're perfectly safe. Don't you worry about a thing!"

    $chat.addmessage(crab, "TwixtBar, you're next it seems.")

    s "Tania being all suspicious."

    $chat.addmessage(bar, "Yeah no")

    k "Where do you think Robin's going to take me? I feel so damn unprepared."

    show t speak

    t "I mean, I know where she's taking you because we need to know in advance to get permission to film."

    $chat.addmessage(liv, "... you all think poorly of me.")

    k "But you won't tell me."

    show t flirty

    t "Nope! Sorry, we need your reaction to be authentic. Aren't you excited about it, though?"

    $chat.addmessage(elsa, "You all should stop being mean to Liv.")

    t "I mean, you've seen her. She's --"

    k "-- otherworldly."

    $chat.addmessage(shub, "We're just being assholes, ElsaLater, no harm meant.")

    ki "Tania pauses a little at that, as if considering whether to agree."

    show t listen

    t "That's a good way to put it. I know she's intimidating but I think mostly it's just because she's so tall."

    $chat.addmessage(bar, "I'm married, first off, and second off, I never accept private chat requests. Sorry Liv.")

    $chat.addmessage(liv, "I forgive you.")


    k "Could be. Should I bring something to stand on for our date?"

    show t flirty

    t "Oh? Thinking you might need to be at, let's say, lip level?"

    s "Spicy!"

    ki "I'm actually blushing. Well played, Tania."

    $chat.addmessage(crab, "drama hours in this chat")

    k "I don't know yet. Maybe."

    t "I'm rooting for ya!"

    scene bg black with fade

    $chat.addmessage(cake, "Hey Liv.")
    $chat.addmessage(liv, "Yes poundCake?")

    ki "Like before, the car ride is uneventful. Tania sits in the back with me, smiling my way every so often but mostly looks in her phone."

    ki "I find myself taking a little time to consider her. She's the master of ceremonies for this strange, time-crunched dating show. She's attractive, but apparently not at all interested in participating."

    $chat.addmessage(cake, "is your name actually Liv? Or like, Olivia. Or something else.")

    ki "I wonder if that's a contractual thing or if she's just off limits somewhow?"

    $chat.addmessage(liv, "My name is Oblivion.")

    ki "Either way, I spend the rest of the ride looking out the window and wondering what the hell I'm going to have to say to Robin."

    python:
        newComments = [
            [bar, "Like hell."],
            [elsa, "Your handle?"],
            [shub, "edgelord?"],
            [fizz, "Really?"],
            [liv, "Yes. But I like Liv."]

        ]
        chat.bulkMessage(newComments, 0.7)

    s "Wait, Liv, are you for real? Your real legal name is Oblivion."

    $chat.addmessage(liv, "Yes. Oblivion Leibniz.")

    s "That's crazy."

    $chat.addmessage(fizz, "I think it's a great name.")

    s "Let's not dwell too much, though. Let's move on!"

    scene bg playhouse far with fade

    k "Oh my god, is this the place she owns?"

    show t speak with dissolve

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

    s "Portmanteaus are cute, though!"

    show t

    t "Robin's here somewhere. Probably hanging by her feet from the rafters somewhere taking a nap."

    k "Hanging what now? Oh."

    show t speak

    t "Like a bat."

    $chat.addmessage(liv, "No spoilers, but poor Robin doesn't mean anything by being so spooky :(")

    k "Like a bat, yes. Gotcha."

    $chat.addmessage(elsa, "Liv, you've finished this game before right?")

    show t happy

    t "You really are a ball of nerves. Breathe, girl. Remember, the worst thing that can happen is you still get paid at the end."

    $chat.addmessage(liv, "I know how it ends ;)")

    k "I guess I--"

    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 0.5

    $chat.addmessage(fizz, "Jesus! I turn my head for one second get flippin' jumpscared.")
    $chat.addmessage(shub, "lol")

    k "What the fu--"

    t "Lights, yes, the lights went out! We're a TV show, remember, uh, Kylie."

    $chat.addmessage(bar, "dancin in the dark")

    k "Is this supposed to be happening?"

    pause 1.5

    k "Tania?"

    pause 1
    $chat.addmessage(elsa, "Spooky. Liv, hold me.")

    ki "I knew it. I knew this was a setup. I knew --"
    $chat.addmessage(liv, "Yes please :)")

    $chat.addmessage(beav, "HELL YEAH")

    play sound "sounds/Lights Out.mp3"
    scene bg playhouse near

    r "You seem unsettled draga mea."

    show r with dissolve

    ki "Her voice pours through the dark as it recedes, musical and so, so close."

    $chat.addmessage(crab, "This some rasslin' B.S. right here")

    k "Jesus Christ, Robin! What in the world made you think this was a good idea for a date?"

    show r speak

    r "Is your blood not pumping?"

    $chat.addmessage(cake, "last tiem I scared the hell out of a date it did not end in cuffing.")
    pause 0.5

    ki "It is. My face is flushed, I feel hot. I'm not scared. I'm not because I could smell her perfume before the lights came up."

    $chat.addmessage(fizz, "Or cuffs in general, right?")

    ki "And it's comforting. I don't know what it is, but the scent puts me at ease."

    $chat.addmessage(elsa, "Sophie I need to brb")

    s "Bet it smells like chloroform. Oh, Elsa, you're fine. We're playing at our own pace here."

    $chat.addmessage(shub, "private chat, eh?")
    $chat.addmessage(elsa, "Shut up, Shub, I'll bring back Bong if I find him.")

    k "I... you have my heart racing, for sure."

    $chat.addmessage(cake, "take pics")

    show r shy

    r "I apologize papillon. Stagecraft is my life, and so I thought I might show you just a bit."

    ki "Her voice thrills me. It's at once dangerous and comfortable, and I can't place it for the life of me."

    $chat.addmessage(beav, "Y'know, Egg's been awful quiet too.")

    k "What does draga mea mean?"

    show r speak

    r "It means I am fond of you, Kylie."

    $chat.addmessage(fizz, "Hang on.")

    k "We just met."

    r "Are you sure?"

    $chat.addmessage(crab, "hangin low bruv")

    k "Uh, yes?"

    r "Mm. Perhaps I'm mistaken my dear, but I feel as though we've been acquainted for quite some time."

    $chat.addmessage(cake, "lol")

    ki "Wha?"

    s "You said it, Kylie."

    $chat.addmessage(elsa, "she really is gorgeous wow")

    show r happy

    r "Come, come. We should have our dinner, don't you think?"

    $chat.addmessage(shub, "What kinda chat is she sending?")

    k "Oh, uh, sure. Where are we going?"

    $chat.addmessage(elsa, "her eyes are haunting and she's just wow")

    r "Right here."

    $chat.addmessage(beav, "You paying for that chat by the minute?")

    ki "That's it. She's going to cook me."

    hide r with dissolve

    ki "At least that's what I think. Robin turns and beckons to me, carelessly, as if she's only here in my imagination."

    $chat.addmessage(fizz, "Yeah I just read back in the chat a ways and Egg really hasn't said a thing for a while.")

    ki "Conscious of the camera crew wavering around us, I follow her down the auditorium walkway and to the stage stairs, noticing the smoothness of her steps, the way her hair seems to sway in slow motion."

    $chat.addmessage(sophie, "Chat currently paused. Feel free to hang around, it's temporary!")
    pause

    ki "She really is otherworldly."

    s "I feel like the game wants me to pick Robin. What do you think, chat?"

    s "Wow, what did I miss? Elsa and Liv vanished for a private chat?"

    s "I feel like my stream became a meet-cute parlor. Ha!"

    pause 1.0

    s "No comment? Oh. Oh! Sorry, I must've paused the chat by accident. Sorry!"

    $chat.addmessage(beav, "That's what I think, anway.")

    show r speak with dissolve

    r "I hope you don't mind, I turned down Tania's offer to pay for our meal."

    $chat.addmessage(fizz, "That's probably what's happening.")

    ki "At center stage there's a table set, ringed with gentle candlelight."

    ki "Wait. The candles are artificial. I suppose fire on stage would be a terrible idea, wouldn't it?"

    $chat.addmessage(shub, "goth girl gets me dinner. Why is this even a contest.")

    k "Oh, then what are we having?"

    pause 1.0

    show r flirty

    r "Your favorite, of course."

    ki "How on earth would she know--"

    $chat.addmessage(cake, "big spooky")

    k "Okay, hang on. Robin, I'm game, but how would you know what I like?"

    hide r with dissolve

    ki "She moves like a whisper from the stairs to the table, and I follow, curious, nervous."

    $chat.addmessage(cake, "AsMR lol")

    ki "She lifts a platter cover from one of the place settings."

    show r disap with dissolve

    r "Was I wrong, papillon?"

    $chat.addmessage(crab, "it's some fast food bullshit")

    ki "A chip of ice races along my bloodstream. On the platter there sits a fragrant bowl of coq au vin, warm with the scent of pearl onions and bacon, along with and a plank of brie crusted in almond slivers and honey. The scent floats languidly above Robin's delicate perfume."

    $chat.addmessage(fizz, "Fancy.")

    k "How did you know?"

    $chat.addmessage(crab, "not that fancy. friggin french food overrated AF")

    show r shy

    r "Because we've been friends for so long, papillon."

    s "Wait, what."

    $chat.addmessage(cake, "broooooo")

    k "Have we met before? There's no way I wouldn't remember you."

    r "I'm flattered, of course. I served you this dish once before, in a little shop not far from the Seine. I wasn't so tall back then."

    r "You dressed differently, then."

    $chat.addmessage(beav, "Here we go.")

    if outfitCurrent == "Dress":
        ki "She pauses, obviously for effect. Everything she does seems calculated for effect."
        r "You have me at a disadvantage, dear. It's difficult not to stare."
        ki "As if I wasn't self-conscious enough."
        k "It's a little, uh... you don't like the dress?"
        r "I couldn't love it more if I were created expressly to love it, papillon."
        r "So... forgive me if my gaze lingers, won't you?"
        k "Maybe."
        ki "Her smile is warm, briefly. I could be wrong, but I feel like both of us are a little more comfortable than a moment ago."

    if outfitCurrent == "Jeans":
        k "So my other choices were a pantsuit and a dress that was basically a napkin and some strings."
        k "I didn't want to come across wrong, I guess."
        ki "Huh. Self, that was an awfully forthright answer."
        ki "Robin, I discover, has a habit of tilting her head owlishly when she's considering her words."
        r "It is the woman beneath the fabric who interests me, darling. Nothing more."

    if outfitCurrent == "Pantsuit":
        r "I am impressed by your style, darling."
        k "Oh? Thank you!"
        r "I wonder what your intention was in choosing such a statement outfit."
        ki "Uh-oh."
        k "Oh, no statement. I just didn't think my other options were... hm."
        r "Were what, dear?"
        k "Classy enough for you, I guess?"
        pause 0.5
        r "Papillon. You overestimate me."

    $chat.addmessage(beav, "Well, hell. I wonder which choice was actually right.")

    k "I don't--"

    $chat.addmessage(bong, "01010100 01101000 01100101 00100000 01100100 01100001 01110100 01100001 00100000 01100110 01100101 01100101 01101100 01110011 00100000 01110011 01101111 00100000 01100111 01101111 01101111 01100100")

    pause 1

    $getHistory(3)

    ki "But I do. I remember. I remember my freshman year of college and how I took French classes entirely to take a trip to Paris."

    $chat.addmessage(liv, "Sophie, have you ever been to Paris?")

    pause 0.4

    s "You're back fast this time, Liv. Yeah, I have been to Paris, I went in college."

    $chat.addmessage(fizz, "Too much coincidence?")

    s "I never took French, though. I took two years of Spanish and promptly forgot all of it."

    show r sad

    r "I was different then. Lesser. But I am a deft hand in the kitchen, papillon."

    $chat.addmessage(elsa, "Back.")

    ki "No. I do remember. I remember her scent. That's why..."

    $chat.addmessage(shub, "Hey ElsaLater came back sooner. XD XD XD")

    k "Oh my god! So that's why you seemed so damn familiar."

    ki "Her smile now, it's dark but searching. Meaningful."

    $chat.addmessage(elsa, "Yup, safe and sound. Obviously.")

    show r happy

    r "Is that alright?"

    $chat.addmessage(cake, "yo Oblivion, Elsa said you're a stone-cold cutie")

    ki "I remember, now. I remember the little bistro overlooking the river and the girl behind the counter who served me a plate of coq au vin with tears in her eyes. I remember how unsettled I felt."

    $chat.addmessage(elsa, "That's NOT what I said")

    ki "'Why are you crying? Is everything okay?' I had asked. She had only nodded, eyes sparkling, and said 'It is the first time.' I remember she had a funny accent that didn't fit in Paris."

    $chat.addmessage(liv, "Please call me Liv :) Elsa is much cuter than I. ")

    k "I don't remember you being so tall though."

    show r speak

    r "I was fifteen when we met, draga mea."

    $chat.addmessage(shub, "15, eh? is that anime 15 or real life 15?")

    k "Holy god you're only 19?"

    $chat.addmessage(beav, "anime 15 creeps me out. Man.")

    s "No way. There's no way."

    $chat.addmessage(elsa, "SO ANYWAY Robin knows Kylie from her past? Weird.")

    k "Didn't Tania say everyone was 20? And how do you own this place?"

    show r listen

    r "Your food is getting cold."

    $chat.addmessage(liv, "Robin is so mature for her age. We love her, don't we.")

    k "I'm sorry, I just have a million questions."

    $chat.addmessage(fizz, "Dunno about that, but she dodges questions like they were wrenches.")

    show r speak

    r "I know. And I have a few answers for you, as well. But for now, please. Your kind words about my cooking changed everything for me, darling, please let me see if I still deserve them."

    $chat.addmessage(crab, "We? speak for yourself Liv. bitch creeps me out.")

    hide r with dissolve

    ki "We sit, she at one end and I at the other. Tania had to know about this, right? How in the world did this happen?"

    $chat.addmessage(fizz, "Now, now, no casual sexism in the chat :D")

    scene bg playhouse far with fade

    ki "The food is sublime. It isn't as if coq au vin is a life-changing dish but the weight of her story lends fullness to the flavor."

    ki "The brie is tender in that almost-not-quite-creamy sort of way, sweet and cruncy on top from the honey and almonds. Robin is a deft hand, that much is certain."

    $chat.addmessage(beav, "Makes me want a big-ass roast chicken.")

    k "If I eat another bite I'm gonna pop."

    show r flirty with dissolve

    r "Please, don't. It took too long to find you again draga mea, I would hate to have to clean you up."

    k "Aren't you eating?"

    $chat.addmessage(fizz, "She's a vampire, isn't she.")

    ki "I hadn't even noticed her platter still sitting covered. Robin sits, legs neatly crossed, leaning on her open palm with a serene expression."

    r "I am devouring you, darling."

    $chat.addmessage(cake, "hell no, vampires can GTFO")

    ki "A nervous chuckle passes my lips."

    show r speak

    r "It was against my father's wishes I left Bucharest for Paris. He wanted the life of a businesswoman for me, a trader in my family's enterprises."

    ki "Her eyes unfocus, slightly. It's as if she's devoting too much energy to the story she's about to tell."

    $chat.addmessage(fizz, "So she's Romanian. Definitely a vampire.")

    k "What did your family do?"

    $chat.addmessage(cake, "lol facts")

    r "Contracting, mostly. It was not to my liking. And so, I spent years in France living with a cousin to study cuisine. Until I met you, papillon."

    $chat.addmessage(fizz, "Why would they make it that obvious?")

    s "Don't you guys think all of this is too easy? Like I get this is a cheesy dating sim and all, but you mean to tell me this girl fell in love with me at first sight?"
    s "Then she tracked me down on this show while also becoming a playhouse owner?"

    $chat.addmessage(crab, "You ever see 'Single White Female'?")

    k "Why would you follow me, though? All I did was praise your skill."

    show r sad

    r "The thirsty come to me for water, remember?"

    $chat.addmessage(liv, "Her sad face is so endearing :(")

    r "You... you brought me water, Kylie."

    k "I don't know what to say."

    $chat.addmessage(elsa, "Aww")

    show r shy

    r "Say you will meet with me again. And again."

    k "It's so much to take in, Robin. I don't even know who you are, not really."

    show r sad

    r "Am I not pleasing to your eye?"

    $chat.addmessage(cake, "everybody's in a hurry but it makes sense being a datin show")

    k "It's not that, you're..."

    s "Exactly my type!"

    $chat.addmessage(bar, "Same")

    k "You're hot. And I'm kind of afraid of you."

    r "Oh? Because I searched for you?"

    $chat.addmessage(shub, "among other things ya vampire")

    k "Because the way you're looking at me makes me feel like you're going to cook me."

    show r flirty

    r "Perhaps."

    $chat.addmessage(beav, "FLUCKIN CALLED IT")

    k "See, that's what I mean! I don't know if it's part of your persona or if you're being metaphorical and sexy or if you're going to bite my neck and suck my blood!"

    $chat.addmessage(fizz, "Red herrings everywhere.")

    ki "Oh wow, those words just came tumbling out of my mouth, didn't they."

    show r sad

    r "I'm no vampire, papillon."

    k "So what am I supposed to think?"

    $chat.addmessage(elsa, "I like that Kylie automatically believes in vampires.")

    show r listen

    ki "She rises then, looming enormous over me, and my skin freezes. Her dress opens from just below her sternum in a diamond pattern that ends just below her navel."

    ki "And now, that pale, warm skin is inches from me."

    $chat.addmessage(crab, "'bout time we got some H in this :P")

    r "Whatever you like, my dear. I wish only to feed you, and see you smile the way you smiled that day on the Seine."

    ki "My heart hurts from hammering in my chest. My arms and legs hang like noodles. She lowers herself to me, kneeling so close I can smell her lipstick, tart and chemical."

    # sound effect of lights shutting off
    play sound "sounds/Lights Out.mp3"
    scene bg black

    $chat.addmessage(cake, "GOD")
    $chat.addmessage(elsa, "ahgp")

    pause 2.0

    s "Oh my god why."

    $chat.addmessage(liv, "hahahahahahahaha")

    pause 2.0

    k "Robin? Okay, this is not cool!"

    $chat.addmessage(fizz, "I wonder what kind of team Robin has in place making this stuff happen.")

    pause 1.0

    k "Robin?"

    pause 1.0

    $chat.addmessage(shub, "SPPOOPP")

    k "Hello?"

    ki "Silence. Just silence."

    $chat.addmessage(elsa, "She's committed to her act if nothing else.")

    k "Tania? Robin?"

    pause 1.0

    $chat.addmessage(crab, "This isn't a horror game is it?")

    k "Hey! I can't... is someone there? Anybody? This isn't fun anymore!"

    $chat.addmessage(liv, "Crablegs, it isn't. You can relax. :)")

    pause 1.0

    ki "And then, a soft brush of something firm against my cheek. The sound of lips plucking gently away."

    ki "A whisper."

    r "{alpha=0.5}Shh. I'll see you again, papillon.{/alpha}"

    # sound effect of lights
    play sound "sounds/Lights Out.mp3"
    scene bg playhouse far

    pause 0.25

    $chat.addmessage(fizz, "Hot/Terrifying if that happens in reality.")

    k "Hey!"

    ki "When the lights come up, Robin is gone. The platters are gone, too. A thousand thoughts ricochet in my mind."

    $chat.addmessage(elsa, "I said it before, but imagine if that a man pulling that trick.")

    ki "How did she do that? I couldn't hear anything moving or clattering. I'm stuck between heart-poundingly impressed and horrified."

    $chat.addmessage(crab, "So are women just as dangerous as men or are women weaker and less dangerous, Elsa?")

    $chat.addmessage(crab, "Can't have it both ways.")

    s "Guys, don't ever pull that on someone on a date! Oh my god."

    show t angry with dissolve

    $chat.addmessage(elsa, "I'm just saying if it was me I'd be scared to death if it was a guy.")

    t "Robin, you ass! You and Cassandra both trying to hide the important stuff!"

    show t speak

    $chat.addmessage(cake, "Sorry, crab's always bitchin about gender politics")

    pause 0.02

    $chat.addmessage(shub, "probalby why my boi can't get a date right")

    t "Hey Kylie, you good? I had no idea she was planning that."

    $chat.addmessage(crab, "STFU bothaya.")

    t "Oh. You have, uh, something on your cheek."

    ki "My fingers easily find the smooth lipstick mark, but I rub off a little and look at my fingertips anyway."

    $chat.addmessage(beav, "need to be specific about which cheek :D :D :D")

    ki "My heart's fluttering."

    k "I'm okay."

    $chat.addmessage(unkn, "stringSever(firstName)")

    t "You look so out of it."

    k "I... I don't know what I'm feeling right now."

    $chat.addmessage(fizz, "Elsa, how would you feel in Kylie's exact spot?")

    ki "I just know I want more. The rush, the rush engulfs me."

    k "That was some date."

    $chat.addmessage(elsa, "I dunno. I like theatrical stuff, so I'd be smiling I think.")
    $chat.addmessage(elsa, "And Robin's attractive to me, so... yeah.")

    show t flirty

    t "I don't think that counts as a date. You talked for like 15 minutes."

    k "I get the feeling Robin isn't much for small talk."

    $chat.addmessage(beav, "Hot.")

    t "She's not. She-"

    # sounds/Lights Out
    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 2.0

    $chat.addmessage(fizz, "Didn't get me that time, Robin!")

    t "God dammit, Robin!"

    ki "The lights are gone. My heart races again. Is she back? I brace for some sensation against my skin, terrified it will come and never come in the same instant."

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

    # robin laugh sound? In the second date Kylie will feel hands on her, too, but a flicker will show them to be monsters of some kind.

    r "Goodnight, my darlings."

    ki "Her voice flows from somewhere far away, echoing lightly."

    $chat.addmessage(cake, "lol")

    t "Robin! Turn the damn lights back on!"

    ki "I'm breathless, still sitting in the dining chair, when the lights come back up."

    $chat.addmessage(egg, "")

    # sound
    play sound "sounds/Lights Out.mp3"

    scene bg playhouse far
    show t angry
    with dissolve

    t "That's not funny! Kylie..."

    $chat.addmessage(liv, "Poor Tania. She just has no control.")

    ki "She's staring at me, at my fingertips resting against my lips."

    t "Oh you have got be kidding me. My cameras can't see in the dark!"

    $chat.addmessage(fizz, "It's almost like the dates are intentionally sabotaging the show.")

    show t disap

    t "Oh well. Guys, get in here and get her face. Make sure you can see the lipstick."

    ki "Right... a TV show."

    show t happy

    t "We'll cut it into something great. Somehow. Robin, if you're still here somewhere I want to talk to you!"

    $chat.addmessage(elsa, "Me, too. Hey Robin, I like food too!")

    ki "There's no response. I wonder if she's really gone or if she's nearby, still. Watching."

    ki "It's... exciting."

    $chat.addmessage(beav, "Yeah it is.")

    show t speak

    t "Okay. Kylie, I guess it's time to go then. Can you walk, or are your legs jelly?"

    $chat.addmessage(cake, "wonder what elsa is jelly lol")

    scene bg black with dissolve

    $chat.addmessage(elsa, "Piss off, poundCake. Why straight men thing bi or lesbian women are so attractive blows my mind.")

    ki "The car ride home lasts an eternal instant. Cassandra's voice moved me, deeply. Her trust in me, to show the secret she showed, floored me. And yet, Robin..."

    $chat.addmessage(shub, "But Robin's not real.")

    $chat.addmessage(elsa, "So?")

    ki "She might really have stolen my soul."

    scene bg hallway with dissolve

    pause 0.25

    $chat.addmessage(cake, "he means you thnk Robin's attractive, but she's fake so you'll never have a shot at her")
    $chat.addmessage(crab, "just because someone won't sleep with ya doesn't mean she's not attractive. Married girls, movie stars, celibate monks.")

    show t speak with dissolve

    t "Hey. I know Robin's got this weird carny spectacle thing going, and I know I said you should open up to her spooky act, but..."

    $chat.addmessage(shub, "family members")

    show t listen

    t "... are you okay?"

    $chat.addmessage(fizz, "lol, you guys are ate up")

    ki "She hadn't spoken at all on the ride back. Why suddenly now?"

    k "I'm fine. I've never had anything like that happen before."

    $chat.addmessage(elsa, "I guess that makes sense. You're still perverts.")

    show t

    t "Christ, I hope not. I mean, we're a TV show and no one's ever pulled a stunt like that."

    k "I didn't expect it. I didn't expect her to kiss me. Just, just like that."

    $chat.addmessage(shub, "yup")
    $chat.addmessage(crab, "true")
    $chat.addmessage(cake, "it's on my birth certificate, ye ye")

    t "I just wonder how many people were hiding in there. No way she moved that table on her own and did all that stuff from the stage."

    k "I have no idea."

    $chat.addmessage(unkn, "R13:14-15")

    ki "It's hard to think, even now. I feel drained, like all of my energy has been spent dissecting those few minutes in the dark."

    s "Oh my god what if someone else kissed me? I mean, I guess the game made a point to tell us it was her, but still, weird!"

    $chat.addmessage(beav, "like a fishbowl party")

    show t speak

    t "Get some sleep. We'll have a little round-up tomorrow on the main stage, but it'll be later in the day so you can rest."

    k "Yeah."

    $chat.addmessage(elsa, "I don't want to know, do I?")

    ki "So, so tired."

    scene bg dressing with dissolve

    $chat.addmessage(beav, "Depends on if Liv and Robin are going")

    ki "I don't even have time to consider much more. I didn't even intend to flop directly on the bed and drag a pillow under my head. It just... kind of happened."

    $chat.addmessage(elsa, "Just because I think women are attractive you think I'm lesbian?")

    scene bg black with dissolve

    $chat.addmessage(bar, "I assumed you're a guy pretending to be a gay woman to mess with people.")

    pause 1.0

    s "Wow, okay. Chat, I think I'm gonna need a minute after that. Like Robin's gorgeous and mysterious and everything and apparently we have a backstory, which is kind of too convenient."

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

    $chat.addmessage(shub, "there he goes again lol")

    $chat.addmessage(crab, "So like boobs, right? What's better than two?")

    s "Okay chat, I'm back. So, who do you guys think between Cassandra and Robin?"

    $chat.addmessage(elsa, "... okay fair.")
    $chat.addmessage(liv, "A beautiful man like you, Crablegs. ;)")

    s "I'm stuck. I feel like Cassandra's all pure and real, and then Robin's all dark and theatrical. Like, how much of what Robin's saying is an act?"

    $chat.addmessage(crab, "Right. Also, Liv, you have no idea what I look like.")

    s "But then, maybe Cassandra isn't really all pure and it's just Robin being all evil that makes me think that."

    $chat.addmessage(liv, "Wanna hear something really spooky?")

    s "You guys have no opinion on Robin or Cassandra? Or are we all too tied up in lesbian action?"

    $chat.addmessage(crab, "finally Sophie speaking my language ;) Also, sure Liv.")
    $chat.addmessage(fizz, "Liv, I hope you aren't about to turn out to be a hacker spy or something.")

    s "Whatcha got, Liv? I'm curious."

    $chat.addmessage(beav, "Robin has my vote. She's freaky. ")

    s "Well, anyway, we have one more date to go! Let's go get us a tomboy."

    $chat.addmessage(liv, "Crablegs is five foot nine. He has a fade haircut. He is Canadian. He is interested in women. He enjoys bluegrass music and has brown eyes.")

    pause 1.0

    python:
        newComments = [
            [elsa, "Wait is she right?"],
            [bar, "dafuq"],
            [beav, "she wannabe Anonymous"],
            [crab, "okay how the hell"],
            [cake, "she right"]
        ]
        chat.bulkMessage(newComments, 0.8)

    pause 1.0

    s "The hell?"

    $chat.addmessage(liv, "Relax, relax. He sent me his dating profile. ;)")

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

    s "Liv, you're devious, you know that?"

    $chat.addmessage(liv, "I try ;)")

    s "You guys feel like going on if I take, like, a half hour break? I know it's a lot, but this is heavy stuff for me."

    python:
        newComments = [
            [liv, "I'll be here for you anytime, sweet Sophie :)"],
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
