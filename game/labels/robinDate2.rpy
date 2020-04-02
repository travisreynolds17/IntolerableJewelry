label robinDate2:

    pause(0.5)
    $hideGui()
    scene bg story-9 with fade
    pause 2.0
    pause
    scene bg dressing with fade
    $showGui()
    pause 0.5

    s "~yawn~ Hey chat. I don't know how much longer I'm gonna play this."

    $chat.addmessage(elsa, "Yes, Sophie, please stop!")

    $chat.addmessage(beav, "prolly should take a night off")

    s "Honestly, I'm getting tired and that was pretty unpleasant for a bit. Don't you think?"

    $chat.addmessage(bar, "I think you need rest.")

    $chat.addmessage(cake, "Get some water and sleep, baby girl.")

    # chat begs her to continue, oddly worded
    pause 0.5
    s "You guys are that into this, huh? You really want me to keep playing?"

    s "I guess I ~yawwwwn~ can stick it out a bit longer."

    $chat.addmessage(elsa, "What? No!")

    $chat.addmessage(bar, "uh?")

    s "I'm getting old, you guys."

    $chat.addmessage(beav, "sophie you scarin me")

    s "Oh, shush, all'ya, but thanks for calling me pretty, Egg."

    ki "The night passes, beset by squads of nightmares."

    $chat.addmessage(elsa, "Huh?")

    $getHistory(12)

    $chat.addmessage(sophie, "Chat exists outside the comprehensible spectruM")

    ki "All I wanted to do was put the evening behind me, but it played in my mind. Over and over."

    $chat.history.pop(-1)

    ki "I know I have a date with Robin this evening and, frankly, I would normally be nervous as hell about it."

    ki "I just can't help thinking about Cassandra."

    $chat.addmessage(liv, "Sophie Sophie Sophie!")

    # knock sound

    un "Miss Koenig? Makeup is in thirty minutes!"

    k "Coming, coming."

    ki "I just don't have time to think about her."

    scene bg black with fade

    # ---------------------------------------------------------

    $renpy.notify("Do you really believe that?")

    # ---------------------------------------------------------

    ki "A.M. fades into P.M.. Meetings with show staff. Shoot some B roll of my morning. Makeup. Catering."

    ki "I guess it'll be dubbed over with the interview I did about Cassandra. I don't have time to think about last night now, though, because in a very short time there's an Eastern Bloc Goth Dream Girl in my future."

    $chat.addmessage(elsa, "Liv? poundCake? Beaver? TwixtBar? Fizz?")

    ki "... I hope she likes me in white."

    s "Contrast is good."

    $chat.addmessage(liv, "You look beautiful, Sophie. :) I know you're tired.")

    ki "Okay, nerves. Pack your bags and let's go. Today's a new day."

    scene bg hallway with fade

    show l happy with dissolve

    l "Heya babe. You look nice."

    k "I hope so."

    $chat.addmessage(beav, "Is it time to date Lichelle, then?")

    show l disap

    l "You sound discouraged."

    k "Not really. Last night was just pretty heavy."

    $chat.addmessage(liv, "It isn't time for that yet. :)")

    show l speak

    l "Yeah. She's okay, by the way."

    ki "My heart leaps a bit."

    $chat.addmessage(cake, "sophie an't answering shit")

    l "She'll be feeling that episode for a week, probably. It's cool."

    l "She's rich as shit, so she'll probably go to rehab then bust out an album about it."

    $chat.addmessage(elsa, "Sophie. You still have the card I gave you, right?")

    k "I hope so."

    s "Rehab isn't a good environment for art. I don't think so."

    $chat.addmessage(bar, "What card?")

    ki "In a weird way, my fangirl side is pleased with the idea of inspiring part of a song. Even if it's about something terrible."

    l "Tonight'll be easier for you."

    $chat.addmessage(fizz, "None of your fucking business.")

    k "You think it'll be easier? Because if I'm honest, Robin kind of scares me."

    l "Oh no, she's terrifying. Like I can't read her at all."

    $chat.addmessage(bar, "Dude. This is like the fifth time you've got your panties stuck up your ass.")

    $chat.addmessage(bar, "Calm your stupid ass down.")

    show l flirty

    l "She's hot, though. Wouldn't mind rolling with her with those long legs."

    k "Rolling? Like, uh..."

    $chat.addmessage(fizz, "Or what? You gonna type me to death, prick?")

    l "In jujitsu."

    k "Oh."

    $chat.addmessage(elsa, "Stop it.")

    l "And sex."

    k "Oh!"

    $chat.addmessage(beav, "No use, ElsaLater.")

    l "I'm kidding."

    k "Are you?"

    $chat.addmessage(bar, "You're damn lucky we're not in the same room, son.")

    l "Aren't I?"

    $chat.addmessage(fizz, "Oh yeah, so lucky")

    s "..."

    s "Am we?"

    $chat.addmessage(elsa, "David, I swear to god I'll never speak to you again if you don't calm THE HELL DOWN RIGHT NOW.")

    k "..."

    $chat.addmessage(cake, "listen to the lady David, ease up")

    show l happy

    l "..."

    ki "It's not funny. Not really. No setup, no turn, no punchline."

    $chat.addmessage(liv, "TwixtBar? Can I talk to you? Something you should know. :)")

    ki "But I burst out laughing anyway."

    l "That's better, that's what I wanted to see."

    $chat.addmessage(fizz, "God, nobody cares about you Liv")

    l "This shit is hard enough. Don't get bogged down in the drama, babe."

    $chat.addmessage(liv, "... I'm sorry David. :(")

    k "Alright. I'll do my best."

    l "Cool. Let's get moving, then."

    $chat.addmessage(bar, "Leave her alone.")

    k "Oh? Is Tania still out of commission?"

    $chat.addmessage(liv, "Aww TwixtBar! My hero. :) Private message please?")

    l "Yeah. Turns out her ankle's broken."

    k "Oh no!"

    $chat.addmessage(elsa, "Sophie please pay attention!")

    l "Yup. Sucks."

    k "I feel like I should go see her."

    $chat.addmessage(bar, "BRB")

    l "Nah. She'll be back day after tomorrow for the roundup."

    ki "I find myself a little sadder about that than I expected."

    $chat.addmessage(fizz, "Better brb clown.")

    l "Let's ride."

    ki "Lichelle steps past me, toward the exit doors at the end of the hall."

    $chat.addmessage(cake, "Elsa girl, you know, you okay though?")

    ki "As I turn to follow, though, she pauses and plants a light kiss on my cheek."

    s "She's making moves when the others aren't able to compete. Devious, devious."

    $chat.addmessage(elsa, "I'm okay. I'm not happy. Thank you poundCake.")

    ki "A cold thrill pours from the side of my neck, down my side and directly into my center."

    k "Lichelle!"

    $chat.addmessage(cake, "ma'am")

    show l shy

    l "I'm not apologizing. Couldn't wait."

    s "Wow."

    $chat.addmessage(beav, "I guess with the fightin' over for a minute, y'all missin chicks kissin")

    k "I, uh... you don't have to."

    l "Good, 'cause I'm not."

    $chat.addmessage(cake, "damn")

    k "Great. That's fine then."

    ki "She's already walking to the doors. I find myself keenly aware of the fit of her jeans."

    $chat.addmessage(cake, "dat ayuss")

    ki "After a moment of composing myself, I follow along, barely thinking of Robin or Cassandra at all."

    scene bg black with fade

    ki "Like before, the car ride is uneventful. Lichelle sits across from me, gazing through the window, toying with her necklace."

    $chat.addmessage(beav, "so we keep hearin about that necklace.")

    ki "I find myself taking a little time to consider her. She's a professional fighter, an athlete who makes her living by beating the sense out of other women."

    $horrorChat = horrorTwixt[0]
    show screen chatHorror

    ki "And yet, she's not like I would've guessed. She's... flirty. Warm. Her eyes are friendly, her tone firm but teasing."

    $chat.addmessage(elsa, "Sophie, who is your favorite girl?")

    $horrorChat = horrorTwixt[1]

    ki "I don't think it's fair she gets to spend more time with me than the others, but I'm not sure what the alternative would be."

    $horrorChat = horrorTwixt[2]

    ki "Either way, I spend the rest of the ride looking out the window and wondering what the hell I'm going to have to say to Robin."

    hide screen chatHorror

    $chat.addmessage(cake, "all you gotta say to robin is baby, c'mere")


    pause(0.5)
    $hideGui()
    scene bg story-10 with fade
    pause 2.0
    pause
    scene bg playhouse
    $showGui()
    pause 0.5

    k "Oh my god, is this the place she owns?"

    show l speak with dissolve

    l "Yup. This here is Ganymead Performing Arts Center." 
    
    $chat.addmessage(beav,"Robin's rich af as well")

    k "Why is 'Ganymede' spelled wrong?"

    l "It's wrong? How's it supposed to be spelled?" 
    
    $chat.addmessage(bar,"")

    show l listen

    k "G-A-N-Y-M-E-D-E. It's a moon of Jupiter."

    l "I learned two things today, then." 
    
    $chat.addmessage(fizz,"Sophie. Please pick up your phone.")

    k "Two?"

    l "You smell like lavender and I want to just..." 
    
    $chat.addmessage(elsa,"I'm coming over, Sophie. I'll be there in R13:14-15--")

    show l flirty

    l "... nevermind. Also something about Jupiter."

    ki "She's silly, isn't she?" 
    
    $chat.addmessage(cake,"not the word I'd use")

    s "... are you asking us, Kylie? Why are you asking us?" 
    
    $chat.addmessage(fizz,"Sophie, what are you doing? Are you alone in there?")

    l "Robin's here somewhere. I hope she's gonna do something intense like ride to the stage on a zipline."

    k "I don't think that would be good at all!" 
    
    $chat.addmessage(beav,"My guy. Hell are you still here.")

    l "No?"

    k "No, what if something went wrong?" 
    
    $chat.addmessage(liv,"He cares about Sophie, AngeredBeaver69")

    l "What if it didn't?"

    k "I'd... I guess you have a point." 
    
    $chat.addmessage(beav,"I been listenin though. Man")

    s "It would be cool. One point for Lichelle."

    l "Breathe in, breathe out, babe. Robin's just a flesh and blood goth dimepiece. You'll be fine." 
    
    $chat.addmessage(beav,"I dunno if you're wanted anymore, my guy")

    k "I guess I--"

    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 0.5

    k "What the fu--"

    ki "Abruptly, I recall we're filming a TV show and cut off my swear."

    k "Is this supposed to be happening?" 
    
    $chat.addmessage(fizz,"you're right.")

    pause 1.5

    k "Lichelle?"

    pause 1.5

    ki "I knew it. I knew this was a setup. I knew --"

    play sound "sounds/Lights Out.mp3"
    scene bg playhouse near

    r "You seem unsettled draga mea." 
    
    $chat.addmessage(beav,"Was she your girl? Since she's not payin attention.")

    show r with dissolve

    ki "Her voice pours through the receding darkness, musical and so, so close."

    k "Jesus Christ, Robin! What in the world made you think this was a good idea for a date?" 
    
    $chat.addmessage(fizz,"She was.")

    show r speak

    r "Is your blood not pumping?"

    pause 0.5

    ki "It is. My face is flushed, I feel hot. I'm not scared. I'm not because I could smell her perfume before the lights came up." 
    
    $chat.addmessage(liv,"Oh, she was :(")

    ki "And it's nostalgic. I don't know what it is, but the scent puts me on edge."

    s "~yawn~"

    k "I... you have my heart racing, for sure." 
    
    $chat.addmessage(beav,"What happened? Be honest, bro")

    show r shy

    r "I apologize papillon. Stagecraft is my life, and so I thought I might show you just a bit."

    ki "Her voice thrills me. It's at once dangerous and comfortable, and I can't place it for the life of me." 
    
    $chat.addmessage(fizz,"Why do you care so much?")

    k "What does draga mea mean?"

    show r speak

    r "It means I am fond of you, Kylie."

    k "We just met." 
    
    $chat.addmessage(beav,"Yeah you right. Nobody cares, really.")

    r "Are you sure?"

    k "Uh, yes?"

    r "Mm. Perhaps I'm mistaken my dear, but I feel as though we've been acquainted for quite some time." 
    
    $chat.addmessage(cake,"Now one damn minute. Are you THAT damn David?")

    ki "Wha?"

    s "I'd still keep my guard up. Robin followed us across an ocean just because we liked her cooking, right?" 
    
    $chat.addmessage(fizz,"What?")

    s "Or did that change, too?"

    show r happy

    r "Come, come. We should have our dinner, don't you think?"

    k "Oh, uh, sure. Where are we going?" 
    
    $chat.addmessage(beav,"Sophie's talked about you before, dude. If that's you.")

    r "Right here."

    ki "That's it. She's going to cook me."

    hide r with dissolve

    ki "At least that's what I think. Robin turns and beckons to me, carelessly, as if she's only here in my imagination." 
    
    $chat.addmessage(fizz,"And who am I?")

    ki "Conscious of the camera crew wavering around us, I follow her down the auditorium walkway and to the stage stairs, noticing the smoothness of her steps, the way her hair seems to sway in slow motion."

    ki "She really is otherworldly." 
    
    $chat.addmessage(cake,"you her ex, right? makes plenty of sense now")

    show r speak with dissolve

    r "I hope you don't mind, I turned down Tania's offer to pay for our meal." 
    
    $chat.addmessage(fizz,"First off, she left ME.")

    ki "At center stage there's a table set, ringed with gentle candlelight."

    ki "Wait. The candles are artificial. I suppose fire on stage would be a terrible idea, wouldn't it?" 
    
    $chat.addmessage(liv,"Oh, David. :( ")

    k "Oh, then what are we having?"

    pause 1.0

    show r flirty

    r "Your favorite, of course." 
    
    $chat.addmessage(cake,"seems like you earned it, man")

    ki "How on earth would she know--"

    k "Okay, hang on. Robin, I'm game, but how would you know what I like?" 
    
    $chat.addmessage(fizz,"The hell does that mean?")

    hide r with dissolve

    ki "She moves like a whisper from the stairs to the table, and I follow, curious, nervous."

    ki "She lifts a platter cover from one of the place settings." 
    
    $chat.addmessage(beav,"You can't neglect someone all the damn time and expect them to marry you.")

    show r disap with dissolve

    pause 0.3

    $getHistory(12)

    show screen chatHorror

    pause 0.6

    hide screen chatHorror

    r "Was I wrong, papillon?"

    ki "A chip of ice races along my bloodstream. On the platter there sits R13:14-15." 

    ki "A... a band. Thick rubber. The syringe. It's speckled red."
    
    $chat.addmessage(fizz,"I didn't neglect her. You wanna know the truth?")

    k "Robin, what is that?"

    r "It's your favorite dragon, darling." 
    
    $chat.addmessage(cake,"wouldna ask if I didn't, man")

    k "I don't understand."

    r "Perhaps I should have gone with ecstasy instead." 
    
    $chat.addmessage(beav,"aye")

    s "I don't... guys. I don't feel right."

    show r sad

    r "I remembered your favorite Because we've been friends for so long, papillon." 
    
    $chat.addmessage(fizz,"fine")

    ki "I'm freezing. Why is it so cold in here? Is that... is that just me?"

    ki "But there are cameras. She wouldn't have that... that stuff. Here." 
    
    $chat.addmessage(fizz,"Sophie's a fucking junkie. She has been almost as long as I've known her.")

    r "I'm flattered, of course. Perhaps you wouldn't remember, though, with so much of your favorite dish in your system." 
    
    $chat.addmessage(liv,"Sophie isn't alright, you know. My poor girl :(")

    show r angry

    r "Perhaps you wouldn't recall the party under the streets of Paris. Or the Romanian girl you paid for."  
    
    $chat.addmessage(beav,"jesus")

    k "I don't--"

    ki "But I do. I remember. I remember my freshman year of college and how I took French classes entirely to take a trip to Paris." 
    
    $chat.addmessage(cake,"damn man")
    
    r "You were the first to try my cooking, papillon."

    pause 0.2

    s "Why does my arm hurt?"

    s "What did I pay for?" 
    
    $chat.addmessage(fizz,"Yeah. I'm the one who took her to rehab. I paid for her treatment. I bailed her out of jail. Over and over.")

    show r sad

    r "I was different then. Lesser. "

    ki "No. I do remember. I remember her scent. That's why..." 
    
    $chat.addmessage(liv,"David, that isn't entirely true.")

    k "Oh my god! That... that was you?"

    show r flirty

    ki "Her smile now, it's dark but searching. Meaningful." 
    
    $chat.addmessage(fizz,"The hell do you know?")

    ki "I remember, now. I remember the dance floor, the thump of electronica and the strobes."

    ki "... I remember the drugs. The wine. The hell with it, I'd said, I'll only be in Paris once." 
    
    $chat.addmessage(liv,"Everything, sweet boy.:)") 
    
    $chat.addmessage(sophie,"Chat temporarily cooked into liquid and injected intravenously with the dark-eyed girl who let me kiss her by the fountain")

    ki "... and I remember the girl. Dressed in black, wandering the floors with tears in her eyes and carrying a cigar box full of 'party favors'."

    ki "I remember the man behind her who whispered in my ears. The man who accepted a hundred and fifty dollars from me and my friends. We pooled some cash together."

    $renpy.notify("You can still save her. Sever the strings.")

    s "Oh my god. No. Kylie, no."

    ki "I remember the little room off to the side of the party."

    ki "I remember lying draped across a chair, watching her dance so nervously for the others. Watching her take off her already minimal clothes with shivering hands."

    ki "I watched, unfocused, as the guys coaxed her into touching them. The drugs addled me. I remember wanting them to stop."

    ki "I saw one of the guys hand that man another couple of bills. The door closed, and my friend locked it."

    ki "... the next part didn't last long. I was too euphoric, too leaden to participate much."

    s "... much."

    s "Guys..."

    $temp = reverseString("I never understood pain until now. Oblivion. Blissful, blissful noivilbO. Her kiss paralyzes. She's angelic. I can't taste noivilbO but she loves me and I need noivilbO")

    $chat.addLinearMessage(bar, temp, 0, 3)

    ki "'Why are you crying? Is everything okay?' I had asked the girl shivering in my arms afterward. Knowing nothing."

    ki "The guys had gone out aleady. She had only nodded, eyes sparkling, and said 'It is the first time.' I remember she had a funny accent that didn't fit in Paris."

    ki "I remember the trickle of blood flowing from her, not enough to drip, but enough to redden my lap."

    s "Was it always like this? Did Robin lie to us the first time?"

    $temp = "It was always like this. You were there the entire time."

    $chat.addLinearMessage(egg, temp, 0, 3)

    show r speak

    r "I was fifteen when we met, draga mea."

    k "You what?"

    s "Oh my fucking god."

    r "I'm not angry. Rather the opposite, I am thrilled to have you here, within my reach, once again." 
    
    $chat.addmessage(elsa,"Guys, I'm at her apartment. Sophie's door is barricaded. I called the cops, but they said it could be forty minutes before they get here.")

    show r disap

    r "I remembered you being taller." 
    
    $chat.addmessage(elsa,"David, do something! Get your ass over here!")

    s "Woooooow. Chat, oh my god. Let me get this straight, we took a trip to Paris and went to an underground sex party..."

    s "... and she was only..." 
    
    $chat.addmessage(fizz,"So now I'm supposed to go save her again.")

    # show a sad sophie and then sudden brb

    s "I don't want to play anymore. This stuff hits too close to home."

    s "But I'll leave it up to you guys. I'm sleepy, and this is depressing, but what do you think?" 
    
    $chat.addmessage(fizz,"STOP PLAYING!") 
    
    $chat.addmessage(elsa,"Sophie open your door, please!")

    s "Alright. Another twenty minutes or so, but then we're calling it for the night." 
    
    $chat.addmessage(cake,"it's like she's watchin a different chat") 
    
    $chat.addmessage(beav,"so this is all a stunt, right?")

    scene bg playhouse far with fade

    ki "The silence between us drags on. I don't know what to say." 
    
    $chat.addmessage(liv,"Sophie, did you know? I LOVE you. Stay with me ;)")

    ki "No one was ever supposed to know about that. And..."

    ki "My blood runs, somehow, even colder." 
    
    $chat.addmessage(sophie,"Okay, Oblivion. ;) I LOVE you, too.")


    ki "The camera crew looms around us."

    s "Oh god. The cameras." 
    
    $chat.addmessage(elsa,"What in the actual hell?")

    r "Don't worry, draga mea. There is no way to prove the truth of my story."

    k "What do you want?" 
    
    $chat.addmessage(fizz,"I KNEW IT you're still seeing that bitch")

    r "You. Only you."

    k "Huh? No, no no. I have to go." 
    
    $chat.addmessage(beav,"Uh")

    show r angry with dissolve

    r "Please, don't. It took too long to find you draga mea, please do not make me hunt you down again."

    s "Hunt. She said hunt." 
    
    $chat.addmessage(cake,"Do you know Liv, too?")
    show r speak

    r "It was against my father's wishes I left Bucharest for Paris. He wanted the life of a businesswoman for me, an arbiter in my family's enterprises."

    k "W-what did your family do?" 
    
    $chat.addmessage(fizz,"LIV, you're the leggy bitch from the bar we used to go to.")

    ki "Anything to change the subject."

    r "What you in America call 'the protection racket'." 
    
    $chat.addmessage(fizz,"you were THERE when she overdosed!")

    k "Oh my god."

    s "Oh my god."

    r "My brothers shattered knees and slit throats for them. My sisters ran the gambling parlors." 
    
    $chat.addmessage(liv,"Who do you think I am, sweet boy?")

    ki "She's approaching me now, one step. One step. One."

    r "My mother and father traded in these pitiable chemicals. These powdered fantasies, papillon." 
    
    $chat.addmessage(fizz,"You used to sit outside the bar and wait for her!")

    r "And I, I wanted none of it. So I ran. Ran to Paris to learn to cook, sweet Kylie. I wanted to be a chef, can you imagine?"

    show r heartbroken

    r "Something so foolish? So excerable?" 
    
    $chat.addmessage(liv,"Oh, my, oh no. No, sweet boy.")

    k "Robin, no. It's not foolish to want out of that life!"

    show r sad

    r "And yet. It is difficult to reach Paris without skills. Income. And I at thirteen had none." 
    
    $chat.addmessage(fizz,"you waited for her, and you're the one who sold her that shit")

    r "Only these alien features that drew the eyes of men and women from Belgrade to Zagreb. From Venice to Zurich. At last, to Paris." 
    
    $chat.addmessage(elsa,"David that's impossible")

    s "I'm shaking. She's practiced this speech. Nobody talks like this."

    r "But I had skills, my love." 
    
    $chat.addmessage(liv,"And why is that, my Elsa? Help him understand.")

    r "And I had my father's switchblade."

    r "They helped me make it to Paris." 
    
    $chat.addmessage(elsa,"That girl's dead, David.")

    r "To you."

    k "I don't know what to say." 
    
    $chat.addmessage(fizz,"Wha?")

    show r shy

    r "Say you will meet with me again. And again."

    k "Robin, I... I'm not that person anymore. And I am so, so sorry for what we..." 
    
    $chat.addmessage(elsa,"She died. She was in my support group, too.")

    k "For what I did to you."

    show r heartbroken

    r "No, papillon, you saved me. You gave me purpose again. You were kind to me!" 
    
    $chat.addmessage(beav,"Support for what?")

    show r sad

    r "Am I not pleasing to your eye?"

    k "It's not that, you're..." 
    
    $chat.addmessage(elsa,"... heroin addiction.")

    pause 1.0

    $chat.history.pop(-1)

    pause 1.0 
    
    $chat.addmessage(elsa,"Absolutely nothing.")

    s "... she's broken."

    k "You're ... you're scaring me." 
    
    $chat.addmessage(cake,"The hell?")

    r "Oh? Because I searched for you?"

    k "Because the way you're looking at me makes me feel like you're going to hurt me."

    show r listen

    r "Never. Not you." 
    
    $chat.addmessage(liv,"Elsa, chat with me again?")

    k "This has gone far enough. I don't care about the show anymore, I'm leaving!"

    show r sad

    r "Whatever you like, my dear. I wish only to feed you, and see you smile the way you smiled that day under the streets of Montmartre." 
    
    $chat.addmessage(elsa,"Who ARE you?")

    ki "My heart hurts from hammering in my chest. My arms and legs hang like noodles. She lowers herself to me, kneeling so close I can smell her lipstick, tart and chemical." 
    
    $chat.addmessage(liv,"Oblivion. :) I'll tell you more privately. Don't worry baby, I'll make it hotter than last time. x0x0")

    show l angry at left
    show r listen at right
    with dissolve

    l "Alright, back the fuck up you Bride of Frankenstein looking psycho." 
    
    $chat.addmessage(elsa,"DAMMIT!")

    l "Tania told me not to get involved. She said it wouldn't be fair."

    l "But you're a damn psychopath and you need to back up." 
    
    $chat.addmessage(beav,"the hell just happened")

    ki "Lichelle's presence next to me shatters the tension of the situation. Her flannel overshirt is off, putting her thick musculature on display."

    show r happy with dissolve

    r "I have nothing to discuss with you." 
    
    $chat.addmessage(sophie,"Oh, wow. I wish you guys could see what I'm seeing. ;)")

    l "Don't care. We're gonna head out before you start going full yandere here."

    r "Kylie and I have far too much to discuss, mon pouffiasse." 
    
    $chat.addmessage(cake,"huh? sophie's chatting?")

    l "Kylie. Let's jee tee eff oh."

    menu:
        k "What should I do..?"
        "Go with Lichelle":
            k "O-okay."

            show r heartbroken at right

            r "You're leaving me again?"

            show l speak at left

            l "Dude, she's not obligated to you."

            ki "I'm not sure how I feel that Lichelle's speaking for me. I don't know her all that well."

            ki "And I don't need a knight to save me."

            ki "Stil... it's kind of nice."

            $loveLichelle -= 1
            

        "Robin needs me, doesn't she?":
            k "... Robin's right, though."

            show l disap at left
            show r listen at right

            l "Right? About what? Being a stalker?"

            ki "I turn to Lichelle, hoping my expression carries the apologies I intend."

            k "... everything she said is true. I never thought anything of it. I just..."

            k "I was in college, you know? I wanted to have all the experiences. So I went to France with friends and..."

            l "Did drugs and fucked an underaged prostitute. Really?"

            k "I didn't know she was fifteen! Look at her!"

            show r speak at right

            r "Papillon, the age of consent in France is fifteen."

            l "Like that makes it better!"

            s "Right?"

            r "It makes it legal."

            l "Weren't you a prostitute?"

            r "I never received a single coin for our lovemaking, putain."

            ki "I don't speak French, but I'm positive Robin isn't being as sweet as the words flowing from those dark lips."

            k "... I have to make it up to her, Lichelle."

            l "The hell you do. Did you not notice the giant brick of coke on the table?"

            show r happy at right

            r "It's flour."

            show l disap at left

            l "Then why..."

            r "Stagecraft, darling."

            show l angry at left

            l "Kylie, don't let her bullshit get to you!"

            
            $loveRobin += 1
    # END MENU

    # sound effect of lights shutting off
    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 2.0 
    
    $chat.addmessage(sophie,"Watching Liv and Elsa together, guys. Mmm lol haha :) ;) ")

    s "Again?"

    pause 2.0

    k "Robin? Okay, this is not cool!" 
    
    $chat.addmessage(bong,"")

    pause 1.0

    l "What is this pro wrestling bullshit?"

    pause 1.0

    k "Hello?"

    ki "Silence. Just silence." 
    
    $chat.addmessage(egg,"")

    k "Lichelle? Robin?"

    pause 1.0

    k "Hey! I can't... is someone there? Anybody? This isn't fun anymore!"

    pause 1.0

    ki "And then, a soft brush of something firm against my neck. Something cold, scraping. Something..." 
    
    $chat.addmessage(bar,"")

    ki "... metal."

    ki "A whisper."

    r "{alpha=0.5}I still have the blade.{/alpha}"

    # sound effect of lights
    play sound "sounds/Lights Out.mp3"
    scene bg playhouse far

    pause 0.25

    k "Hey!"

    ki "When the lights come up, Robin is gone. The platters are gone, too. A thousand thoughts ricochet in my mind."

    ki "How did she do that? I couldn't hear anything moving or clattering. I'm stuck between heart-poundingly impressed and horrified."

    show l angry

    l "Alright, gloves off. Robin, I know you can hear me!"

    l "Next time I see you, you're getting smacked up!"

    show l speak

    l "Hey Kylie, you good? She's a psycho, I swear."

    l "Oh. You have, uh, something on your neck."

    ki "My fingers easily find the tiny red ribbon flowing from the side of my neck, but I rub off a little and look at my fingertips anyway."

    ki "My heart's fluttering. It doesn't hurt, not at all."

    k "I'm okay."

    l "Is that blood?"

    k "I... I don't know what I'm feeling right now."

    ki "I ... I think I want more. The rush, the rush engulfs me."

    k "That was some date."

    show l disap

    l "That wasn't a date. That was a horror movie."

    k "I get the feeling Robin isn't much for small talk."

    l "Obviously not, she-"

    # sounds/Lights Out
    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 2.0

    l "God dammit, Robin!"

    ki "The lights are gone. My heart races again. Is she back? I brace for some sensation against my skin, terrified it will come and never come in the same instant."

    pause 1.0

    r "{alpha=0.3}Shhh.{/alpha}"

    pause 0.25

    ki "I hear her whispered voice again, but there's no touch. She showed me already that her power over me is absolute."

    pause 1.0

    ki "It was just a knick. She could have split me from ear to ear if she wanted, couldn't she?"

    pause 1.0

    # robin laugh sound?

    l "Gah! FUCK!"

    r "Goodnight, my darlings."

    ki "Her voice flows from somewhere far away, echoing lightly."

    # sound
    play sound "sounds/Lights Out.mp3"

    scene bg playhouse far
    show l angry
    with dissolve

    # with blood?

    k "Oh my god, Lichelle!"

    s "Holy shit."

    ki "She's staring at me, her eyes wide with shock and pain. There's a slash of blood across her chest, shallow, but running in a neat flowing path."

    l "I'm gonna fucking kill you bitch! I swear to god!"

    k "Are you okay? Should we call the police?"

    l "You better hope they find you before I do!"

    ki "The camera crew moves in, right on cue, and Lichelle to my great surprise doesn't front kick one of them into oblivion."

    ki "Rather she lets a slow breath out and allows them to film her. Her chest rises and falls, heavily."

    ki "One of the straps of her tank top is cut through."

    k "Lichelle. You're okay?"

    ki "She nods."

    l "Yeah. She ruined my top."

    k "That's what you're worried about?"

    ki "Sighing, Lichelle dabs a finger in the darkening red running down her chest."

    l "It's a theatre prop. Fake blood. She put it on you, too."

    k "Oh."

    ki "Except the burning pain tattooing my neck begs to differ."

    show l shy
    # up close if possible

    if loveLichelle == 4:
        # note you have to pick her both times at first roundup and agree with her on both second-play dates.

        k "L-lichele?"

        ki "She's staring at me now, eyes full of purpose."

        l "She's insane."

        ki "A whisper, nothing more."

        l "You're a lawbreaking party chick under that wallflower exterior."

        k "... that's not me."

        l "It's okay if it is."

        ki "She's close now, close enough that if I were a braver woman I could be brushing against her."

        l "I need to wash this off."

        k "Yeah."

        l "Let's get out of here."

        k "Yeah."

        s "Everybody in this game is insane, Lichelle."

    scene bg black with dissolve

    ki "The car ride home lasts an eternal instant. Cassandra's humbled sobbing echoes in between fits of Robin's laughter in the pitch black."

    ki "These two nights wrestle for dominance in my mind. The show has faded into an afterthought."

    ki "I look to Lichelle, sitting with her flannel shirt buttoned over the sticky theatre blood."

    s "~yaaawn~"

    if loveLichelle == 4:
        # option for love scene ending with Lichelle

        ki "She's been the one constant over these few days."

        ki "Streetlights paint her features brightly, then vanish, then paint once more."

        k "Hey, Lichelle..."

        show l listen with dissolve
        l "Hm?"

        ki "Her expression is so far away. She's so fearsome in her way that this vulnerability captivates me in the darkness."

        s "Wow. I can't believe Kylie's thinking about anything other than running the ~yawn~ hell away."

        menu:
            ki "Should I..."

            "Make a move":
                jump endLich
            "Don't make a move":
                k "Mm... nothing. It's nothing."
                l "Cool."

    scene bg hallway with dissolve

    pause 0.25

    show l speak with dissolve

    l "So I'm gonna go get a shower and try not to go kick Robin's ass. You might want to lock your door tonight."

    k "You think she's really dangerous, though?"

    show l disap

    l "She splashed us with fake blood, but I think she was sending a message. Showing us what she could have done if she wanted."

    show l listen

    l "... are you okay?"

    k "I'm fine. I've never had anything like that happen before."

    show l speak

    l "Christ, I hope not. I mean, we're a TV show and no one's ever pulled a stunt like that."

    k "I didn't expect it. I didn't expect her to know me. Or for her to be ... that girl."

    l "I just wonder how many people were hiding in there. No way she moved that table on her own and did all that stuff from the stage."

    k "I have no idea."

    ki "It's hard to think, even now. I feel drained, like all of my energy has been spent dissecting those few minutes in the dark."

    s "... you're all frickin' nuts."

    show l speak

    l "Get some sleep. Hey, it's you and me tomorrow."

    k "Yeah."

    ki "So, so tired."

    k "Please don't let it be a disaster. If we just get fast food and watch TV I'll be just fine."

    show l happy

    l "Don't worry babe. Tomorrow's gonna be nothing like the last two days for you."

    scene bg dressing with dissolve

    ki "I don't even have time to consider much more. I didn't even intend to flop directly on the bed and drag a pillow under my head. It just kind of happened."

    ki "The knick on my neck burns a little still."

    ki "I have a date with Lichelle tomorrow and yet, somehow, I feel so very alone."

    ki "Maybe Tania will have something to tell me when she gets back."

    scene bg black with dissolve

    pause 1.0

    s "... guys. I need to pee, but I don't wanna get up."

    s "Sophie's a sleepy girl. I just don't feel like getting up."

    s "... so we might as well go on."
    # chat chats. One odd thing happens.

    show placeholder at right
    pause 0.1
    hide placeholder

    pause 2.0

    scene bg black with fade

    s "So, who do you guys think between Cassandra and Robin?"

    s "I'm stuck. I feel like Cassandra's all pure and real, and then Robin's all dark and theatrical. Like, how much of what Robin's saying is an act?"

    s "But then, maybe Cassandra isn't really all pure and it's just Robin being all evil that makes me think that."

    s "That story about her dad's knife. She's killed someone, maybe."

    s "Then again, I don't know if I believe her story. It's way too convenient for her to show up here if she and Kylie have that kind of history."

    # chat

    s "Well, anyway, we have one more date to go! Let's go get us a tomboy."

    pause 1.0

    jump common4
