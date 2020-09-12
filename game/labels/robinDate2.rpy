label robinDate2:

    pause(0.5)
    $hideGui()
    scene bg story-9 with fade
    pause
    show image story9Edit with dissolve
    pause
    scene bg dressing with fade
    
    $showGui()
    pause 0.5

    play music bedroom fadein 3.0

    s 1j "~yawn~ I don't know how much longer I'm gonna play this."

    $chat.addmessage(elsa, "Yes, Sophie, please stop!")

    $chat.addmessage(beav, "prolly should take a night off")

    s "Honestly, I'm getting tired and that was pretty unpleasant for a bit. Don't you think?"

    $chat.addmessage(bar, "I think you need rest.")

    $chat.addmessage(cake, "Get some water and sleep, baby girl.")

    # chat begs her to continue, oddly worded
    pause 0.5
    s 1b "You guys are that into this, huh? You really want me to keep playing?"

    s 1j "I guess I ~yawwwwn~ can stick it out a bit longer."

    $chat.addmessage(elsa, "What? No!")

    $chat.addmessage(bar, "uh?")

    s "I'm getting a little nauseous. Aching."

    $chat.addmessage(beav, "sophie you scarin me")

    s 1t "Oh, shush, all'ya, but thanks for calling me pretty, Egg."
    pause 0.1

    pause 1.0

    ki "The night passes, beset by squads of nightmares."

    $chat.addmessage(elsa, "Huh?")

    $getHistory(12)

    $chat.addmessage(sophie, "Chat exists outside the comprehensible spectruM")

    ki "All I wanted to do was put the evening behind me, but it played in my mind. Over and over."

    $chat.history.pop(-1)

    ki "I know I have a date with Robin this evening and, frankly, I would normally be nervous as hell about it."

    ki "I just can't help thinking about Cassandra."

    $chat.addmessage(fon, "Sophie Sophie Sophie!")

    # SFX 

    stop music fadeout 5.0

    un "Miss Koenig? Makeup is in thirty minutes!"

    k "Coming, coming."

    

    ki "I just don't have time to think about her."

    scene bg black with fade

    

    # ---------------------------------------------------------

    $renpy.notify("Do you really believe that?")

    # ---------------------------------------------------------

    ki "A.M. fades into P.M.. Meetings with show staff. Shoot some B roll of my morning. Makeup. Catering."

    ki "I guess it'll be dubbed over with the interview I did about Cassandra. I don't have time to think about last night now, though, because in a very short time there's an Eastern Bloc Dream Girl in my future."

    $chat.addmessage(elsa, "Fontaine? poundCake? Beaver? TwixtBar? Fizz?")

    ki "... I hope she likes me in white."

    s 1r "Contrast is good."

    $chat.addmessage(fon, "You look beautiful, Sophie. :) I know you're tired.")

    ki "Okay, nerves. Pack your bags and let's go. Today's a new day."

    scene bg hallway with fade

    play music hallwayChats fadein 1.0

    show l 1m at fr12

    l "Heya babe. You look nice."

    k "I hope so."

    $chat.addmessage(beav, "Is it time to date Lichelle, then?")

    l 1g "You sound discouraged."

    k "Not really. Last night was just pretty heavy."

    $chat.addmessage(fon, "It isn't time for that yet. :)")

    l 1k "Yeah. She's okay, by the way."

    ki "My heart leaps a bit."

    $chat.addmessage(cake, "sophie an't answering shit")

    l "She'll be feeling that episode for a week, probably. It's cool."

    l 1j "She's rich as hell, so she'll probably go to rehab then write an album about it."

    $chat.addmessage(elsa, "Sophie. You still have the card I gave you, right?")

    k "I hope so."

    s 1j "Rehab isn't a good environment for art. I don't think so."

    $chat.addmessage(bar, "What card?")

    ki "In a weird way, my fangirl side is pleased with the idea of inspiring part of a song. Even if it's about something terrible."

    l 1m "Tonight'll be easier for you."

    $chat.addmessage(fizz, "None of your fucking business.")

    k "You think it'll be easier? Because if I'm honest, Robin kind of scares me."

    l 1r "Oh no, she's terrifying. Like I can't read her at all."

    $chat.addmessage(bar, "Dude. This is like the fifth time you've got your panties stuck up your ass.")

    $chat.addmessage(bar, "Calm your stupid ass down.")

    l 2u "She's hot, though. Wouldn't mind rolling with her with those long legs."

    k "Rolling? Like, uh..."

    $chat.addmessage(fizz, "Or what? You gonna type me to death, prick?")

    l 2t "In jiu jitsu."

    k "Oh."

    $chat.addmessage(elsa, "Stop it.")
    pause 1.0
    l 2m "And sex."

    k "Oh!"

    $chat.addmessage(beav, "No use, ElsaLater.")

    l 1j "I'm kidding."

    k "Are you?"

    $chat.addmessage(bar, "You're damn lucky we're not in the same room, son.")

    l 1r "Aren't I?"

    $chat.addmessage(fizz, "Oh yeah, so lucky")

    s 1t "..."

    s "Am we?"

    $chat.addmessage(elsa, "David, I swear to god I'll never speak to you again if you don't calm THE HELL DOWN RIGHT NOW.")

    k "..."

    $chat.addmessage(cake, "listen to the lady David, ease up")

    l 1m "..."

    ki "It's not funny. Not really. No setup, no turn, no punchline."

    $chat.addmessage(fon, "TwixtBar? Can I talk to you? Something you should know. :)")

    ki "But I burst out laughing anyway."

    l 1a "That's better, that's what I wanted to see."

    $chat.addmessage(fizz, "God, nobody cares about you Fontaine")

    l 1o "This shit is hard enough. Don't get bogged down in the drama, babe."

    $chat.addmessage(fon, "... I'm sorry David. :(")

    k "Alright. I'll do my best."

    l 1m "Cool. Let's get moving, then."

    $chat.addmessage(bar, "Leave her alone.")
    pause 0.4

    k "Oh? Is Tania still out of commission?"

    $chat.addmessage(fon, "Aww TwixtBar! My hero. :) Private message please?")

    l 1b "Yeah. Turns out her ankle's broken."

    k "Oh no!"

    $chat.addmessage(elsa, "Sophie please pay attention!")

    l 1k "Yup. Sucks."

    k "I feel like I should go see her."

    $chat.addmessage(bar, "BRB")

    l 1a "Nah. She'll be back day after tomorrow for the roundup."

    ki "I find myself a little sadder about that than I expected."

    $chat.addmessage(fizz, "Better brb clown.")

    l "Let's ride."
    pause 0.1

    ki "Lichelle steps past me, toward the exit doors at the end of the hall."

    $chat.addmessage(cake, "Elsa girl, you know, you okay though?")

    ki "As I turn to follow, though, she pauses and plants a light kiss on my cheek."

    s 1b "She's making moves when the others aren't able to compete. Devious, devious."

    $chat.addmessage(elsa, "I'm okay. I'm not happy. Thank you poundCake.")

    ki "A cold thrill pours from the side of my neck, down my side and directly into my center."

    k "Lichelle!"

    $chat.addmessage(cake, "ma'am")


    l 1p "I'm not apologizing. Couldn't wait."

    s 1r "Wow."

    $chat.addmessage(beav, "I guess with the fightin' over for a minute, y'all missin kissin")
    pause 0.1

    k "I, uh... you don't have to."

    l 1t "Good, 'cause I'm not."

    $chat.addmessage(cake, "damn")

    k "Great. That's fine then."

    ki "She's already walking to the doors. I find myself keenly aware of the fit of her jeans."

    $chat.addmessage(cake, "dat ayuss")

    hide l at f12

    stop music fadeout 4.0

    ki "After a moment of composing myself, I follow along, barely thinking of Robin or Cassandra, or anything much at all."

    scene bg black with longFade

    play music lichelle fadein 1.0

    show image carLightsLight at carLights
    show image carLightsBack with dissolve:
        xpos 0 ypos 0
    
    pause 2.0

    show image carLich with dissolve:
        xpos 0 ypos 0

    ki "Like before, the car ride is uneventful. Lichelle sits across from me, gazing through the window, toying with her necklace."

    $chat.addmessage(beav, "so we keep hearin about that necklace.") 
    
    $chat.addmessage(beav,"I don't see a necklace on her.")

    ki "I find myself taking a little time to consider her. She's a professional fighter, an athlete who makes her living by beating the sense out of other women."

    $horrorChat = horrorTwixt[0]
    show screen chatHorror

    ki "And yet, she's not like I would've guessed. She's... flirty. Warm. Her eyes are friendly, her tone firm but teasing."

    $chat.addmessage(elsa, "Sophie, who is your favorite girl?")

    $horrorChat = horrorTwixt[1]

    ki "I don't think it's fair she gets to spend more time with me than the others, but I'm not sure what the alternative would be."

    $horrorChat = horrorTwixt[2]
    stop music fadeout 3.0
    ki "Either way, I spend the rest of the ride looking out the window and wondering what the hell I'm going to have to say to Robin."

    hide carLich with dissolve

    hide screen chatHorror

    $chat.addmessage(cake, "all you gotta say to robin is baby, c'mere")

    pause(0.5)
    $hideGui()
    scene bg story-10 with fade
    pause 2.0
    pause
    scene bg playhouse far
    $showGui()
    pause 0.5

    
    k "Oh my god, is this the place she owns?"
    play music darkNoodle

    show l 1a at fr12

    l "Yup. This here is Ganymead Performing Arts Center."

    $chat.addmessage(beav, "Robin's rich af as well")

    k "Why is 'Ganymede' spelled wrong?"

    l 1r "It's wrong? How's it supposed to be spelled?"

    $chat.addmessage(bar, "")

    show l 1s

    k "G-A-N-Y-M-E-D-E. It's a moon of Jupiter."

    l 1m "Oh. Oh, right, that's right. The other one was, uh..."

    pause 0.1

    l 1o "Io? Right?"

    $chat.addmessage(fizz, "Sophie. Please pick up your phone.")

    k "Io is one. There's also Europa, Callisto, Valetudo-"

    l 1l "Vale Tudo? Really?"

    $chat.addmessage(elsa, "I'm coming over, Sophie. I'll be there in R/BG13:14-15--")

    k "Uh, yeah. I think so. You seem upbeat about it."

    l 1m "Vale Tudo's a combat sport in Brazil."

    pause 0.1

    k "I didn't know that. Is it like what you do?" 
    
    $chat.addmessage(cake,"glad Elle's not acting like a dumb meathead.")

    l 1a "Lil' bit. There aren't as many rules as there are in most American MMA organizations."

    pause 0.1

    k "I don't know much about fighting." 
    
    $chat.addmessage(cake,"MMA gets a bad rap like that.")

    l 1l "I can talk about it for weeks, babe. If you wanna know." 
    
    $chat.addmessage(beav,"you like Complex Women, poundCake?")

    k "I wouldn't know what to ask-"

    l 1t "Maybe I'll just show you."
    pause 1.0

    ki "Lichelle is shameless, isn't she?"

    $chat.addmessage(cake, "not the word I'd use")

    s 1u "... are you asking us, Kylie? Why are you asking us?"

    $chat.addmessage(fizz, "Sophie, what are you doing? Are you alone in there?")

    l 1l "Robin's here somewhere. I hope she's gonna do something intense like ride to the stage on a zipline."

    k "I don't think that would be good at all!"

    $chat.addmessage(beav, "My guy. Hell are you still here.")

    l 2r "No?"

    k "No, what if something went wrong?"

    $chat.addmessage(fon, "He cares about Sophie, AngeredBeaver69. I love him for that.")

    l 2l "What if it didn't?"

    k "I'd... I guess you have a point."

    $chat.addmessage(beav, "I been listenin though. Man")

    s 1b "Guh. Feels bad, man."
    pause 0.1

    l 1a "Breathe in, breathe out, babe. Robin's just a flesh and blood spooky-ass dimepiece. You'll be fine."

    $chat.addmessage(beav, "I dunno if you're wanted anymore, my guy")

    k "I guess I--"

    stop music fadeout 0.4

    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 1.5

    k "What the fu--"

    ki "Abruptly, I recall we're filming a TV show and cut off my swear."

    k "Is this supposed to be happening?"

    $chat.addmessage(fizz, "you're right.")

    pause 1.5

    k "Lichelle?"

    pause 1.5

    ki "I knew it. I knew this was a setup. I knew --"

    play sound "sounds/Lights Out.mp3"
    scene bg playhouse near

    play music robin

    r "You seem unsettled draga mea."

    $chat.addmessage(beav, "Was she your girl? Since she's not payin attention, tell us.")

    show r 1a at f12
    
    ki "Her voice pours through the receding darkness, musical and so, so close."

    k "Jesus Christ, Robin! What in the world made you think this was a good idea for a date?"

    $chat.addmessage(fizz, "She was.")

    r 1o "Is your blood not pumping?"

    show r 1a

    pause 0.5

    ki "It is. My face is flushed, I feel hot. I'm not scared. I could smell her perfume before the lights came up."

    $chat.addmessage(fon, "Oh, she was :(. WAS. :(")

    ki "And it's nostalgic. I don't know what it is, but the scent puts me on edge."

    s 1j "~yawn~"

    k "... I could smell you."

    $chat.addmessage(beav, "What happened? Be honest, bro")

    show r 2p
    stop music fadeout 3.0

    r "I apologize papillon. Stagecraft is my life, and so I thought I might show you just a bit."
    
    
    play music darkNoodle fadein 5.0

    r 2q "My lavender betrayed me."

    pause 0.2

    k "I like it."

    show r 2m

    r "Lovely."

    ki "Her voice thrills me. It's at once dangerous and familiar, and I can't place it for the life of me."

    $chat.addmessage(fizz, "Why do you care so much?")

    k "What does draga mea mean?"

    r 2a "It means I am fond of you, Kylie."

    k "We just met."

    $chat.addmessage(beav, "Yeah you right. Nobody cares, really.")

    r 2j "Are you sure?"

    k "Uh, yes?"

    r 1o "Mm. Perhaps I'm mistaken my dear, but I feel as though we've been acquainted for quite some time."

    show r 1a

    $chat.addmessage(cake, "Now one damn minute. Are you THAT damn David?")

    ki "Wha?"

    s 1c "I didn't forget you Louisa~"

    $chat.addmessage(fizz, "What?")

    r 1m "Come, come. We should have our dinner, don't you think?"

    k "Oh, uh, sure. Where are we going?"

    $chat.addmessage(beav, "Sophie's talked about you before, dude. If that's you.")

    r "Right here."

    ki "That's it. She's going to cook me."

    hide r with dissolve

    ki "At least that's what I think. Robin turns and beckons to me, carelessly, as if she's only here in my imagination."

    $chat.addmessage(fizz, "And who am I?")

    ki "Conscious of the camera crew wavering around us, I follow her down the auditorium walkway and to the stage stairs, noticing the smoothness of her steps, the way her punkish hair seems to sway in slow motion."

    ki "She really is otherworldly."

    $chat.addmessage(cake, "you her ex, right? the control freak. makes plenty of sense now")

    show r 1o at f12

    r "I hope you don't mind, I turned down Tania's offer to pay for our meal."

    show r 1j

    $chat.addmessage(fizz, "First off, she left ME. Second, I'm not a control freak.")

    ki "At center stage there's a table set, ringed with gentle candlelight."

    ki "Wait. The candles are artificial. I suppose fire on stage would be a terrible idea, wouldn't it?"

    $chat.addmessage(fon, "Oh, David. :( ")

    k "Oh, then what are we having?"

    pause 1.0

    show r 2u 

    r "Your favorite, of course."

    scene bg black with longFade

    $chat.addmessage(cake, "seems like you earned it, man")

    ki "How on earth would she know--"

    stop music fadeout 3.0

    k "Okay, hang on. Robin, I'm game, but how would you know what I like?"

    $chat.addmessage(fizz, "The hell does that mean?")

    show image platterCover at showPlatter with dissolve

    ki "She moves like a whisper from the stairs to the table, and I follow, curious, nervous."

    play music onTheNod fadein 7.0

    ki "She lifts a platter cover from one of the place settings."

    hide platterCover with dissolve
    show platter at showPlatter with dissolve

    $chat.addmessage(beav, "You can't neglect someone all the damn time and expect them to marry you. You can't tell them they have to stop doing things they like.")

    show r 1g at fl12

    pause 0.3

    $getHistory(13)

    show screen chatHorror

    pause 1.6

    hide screen chatHorror

    stop music2
     

    r 1b "Was I wrong, papillon?" 

    show r at justFade with dissolve
    
    $chat.addmessage(beav,"you told her she had to give up strims")

    pause 0.1

    $chat.addmessage(fizz, "That's bullshit. You wanna know the truth?")

    ki "A chip of ice races along my bloodstream. On the platter, plain as day, there sits R/BG13:14-15."
    hide r

    $chat.addmessage(fizz, "Sophie's a fucking junkie. She has been almost as long as I've known her.")

    ki "A... a belt? The syringe. It's speckled red. There's, there's yellow on the spoon. Dark." 
    
    $chat.addmessage(beav,"dude")

    k "Robin, what is that?"

    show r 1b at f14

    r "It's your favorite jewelry, darling." 
    
    $chat.addmessage(cake,"nah man, that's not a thing")

    k "I don't understand."

    r 1c "You don't have to, it... it's not for, for..."

    show r 1i
    pause 0.3
    show r 1m

    r "It's our shared history, dearest."

    s 1f "I don't... guys. I don't feel right."

    show r 2b

    r "I remembered your favorite because we've been friends for so long, papillon." 
    
    $chat.addmessage(fizz,"I loved her. I STILL love her.")

    ki "I'm freezing. Why is it so cold in here? Is that... is that just me?"

    ki "But there are cameras. She wouldn't have that... that stuff. Here." 
    
    $chat.addmessage(fizz,"But I couldn't watch her kill herself with that shit.")

    r "I'm flattered, of course. Perhaps you wouldn't remember, though, with so much of your favorite dish in your system."

    $chat.addmessage(fon, "Sophie isn't alright, you know. My poor girl :(")

    r 1d "Perhaps you wouldn't recall the party under the streets of Paris. Or the Romanian girl you paid for."

    $chat.addmessage(beav, "jesus")

    k "I don't--"

    ki "But I do. I remember. I remember my freshman year of college and how I took French classes entirely to justify a trip to Paris."

    $chat.addmessage(cake, "damn man")

    r 1e "You were the first to try my cooking, papillon."

    pause 0.2

    s "Why does my arm hurt?"

    s "What did I pay for?"

    $chat.addmessage(fizz, "Yeah. I'm the one who took her to rehab. I paid for her treatment. I bailed her out of jail. Over and over.")

    show r 1d

    pause 0.2

    r 1b "I was different then. Lesser. "

    ki "No. I do remember. I remember her scent. That's why..."

    $chat.addmessage(fon, "David, that isn't entirely true.")

    k "Oh my god! That... that was you?"

    show r 1u

    ki "Her smile now, it's dark but searching. Meaningful."

    $chat.addmessage(fizz, "The hell do you know?")

    ki "I remember, now. I remember the dance floor, the thump of electronica and the strobes."

    ki "It's as if I'm remembering something for the first time, recollection spreading like neural contagion."

    ki "... I remember the powder. The wine. The hell with it, I'd said, I'll only be in Paris once."

    $chat.addmessage(fon, "Everything, sweet boy.:)")

    pause 0.3

    $chat.addmessage(sophie, "Chat temporarily cooked into liquid and injected intravenously with the phantasmal girl who let me kiss her by the fountain")

    ki "... and I remember the girl. Dressed in sheer black, wandering the floors with frozen eyes."

    scene bg black with fade

    ki "I remember the man behind her who whispered in my ears. The man who accepted a hundred and fifty dollars from me and my friends."

    $renpy.notify("You can still save her. Sever the strings.")

    s 1c "Oh my god. No. Kylie, no. I'm gonna puke."

    ki "I remember the little room off to the side of the party." 
    
    $chat.addmessage(fizz,"stop this game Sophie, I swear to God I'll never bother you again")

    nvl show

    ki "I remember lying draped across a chair, watching her dance so nervously for the others. Watching her take off her already minimal clothes with shivering hands."

    ki "I watched, unfocused, as the guys coaxed her into touching them. The drugs addled me. I remember wanting them to stop."

    ki "I saw one of the guys hand that man another couple of bills. The door closed, and my friend locked it."

    ki "... the next part didn't last long. I was too euphoric, too leaden to participate much."

    nvl hide

    nvl clear

    s "... much."

    s "Guys..."

    $temp = reverseString("\nI never understood pain until now. Louisa. Blissful, blissful Louisa. Her kiss paralyzes. She's angelic. I can't taste the fountain but she loves me and I need Louisa")

    $chat.addLinearMessage(bar, temp, 0, 3)


    ki "'Why are you crying? Is everything okay?' I had asked the girl shivering in my arms afterward. Knowing nothing."

    ki "The guys had gone out aleady. She had only nodded, eyes sparkling, and said 'It is the first time.' I remember she had a funny accent that didn't fit in Paris."

    ki "I remember the trickle of blood flowing from her, not enough to drip, but enough to redden my lap."


    s "Was it always like this?"

    $temp = "It was always like this. You were there the entire time.\n"

    stop music fadeout 3.0

    $chat.addLinearMessage(egg, temp, 0, 3)

    scene bg playhouse far with fade

    play music robin

    show r 1b at f12
    r 1b "I was fifteen when we met, draga mea."

    k "You what?"

    s 1c "Oh my fucking god."

    r 1a "I'm not angry. Rather the opposite, I am thrilled to have you here, within my reach, once again."

    $chat.addmessage(elsa, "Guys, I'm at her apartment. Sophie's door is barricaded. I called the cops, but they said it could be fifteen minutes before they get here.")

    r 1j "I remembered you being taller."

    $chat.addmessage(elsa, "David, do something! Get your ass over here!")

    s 1b "I remember..."

    s 1c "... and she was only..."

    $chat.addmessage(fizz, "So now I'm supposed to go save her again.")

    # show a sad sophie and then sudden brb

    s 1q "I don't want to play anymore."

    s "But, blugh. I'll leave it up to you guys.?"

    $chat.addmessage(fizz, "STOP PLAYING!")

    $chat.addmessage(elsa, "Sophie open your door, please!")

    s 1a "Alright. I'll play."

    $chat.addmessage(cake, "it's like she's watchin a different chat")

    $chat.addmessage(beav, "so this is all a stunt, right?")

    scene bg playhouse far with fade

    show r 1b at f12

    ki "The silence between us drags on. I don't know what to say."

    $chat.addmessage(fon, "Sophie, did you know? I LOVE you. Stay with me ;)")

    ki "No one was ever supposed to know about that. And..."

    ki "My blood runs, somehow, even colder."

    $chat.addmessage(sophie, "Okay, Fontaine. ;) I LOVE you, too, heh heh.")

    ki "The camera crew looms around us."

    s 1h "Oh god. The cameras."

    $chat.addmessage(elsa, "What in the actual hell?")

    r 2b "Don't worry, draga mea. There is no way to prove the truth of my story."

    k "What do you want?"

    $chat.addmessage(fizz, "Dammit! Leave her alone Fontaine!")

    r 2c "You. Only you."

    k "Huh? No, no no. I have to go."

    $chat.addmessage(beav, "Uh")

    show r 2i 

    r "Please, don't. It took too long to find you draga mea, please do not make me hunt you down again."

    s 1f "Hunt. She said hunt."

    $chat.addmessage(cake, "Do you know Fontaine, too?")
    
    r 1b "It was against my father's wishes I left Bucharest for Paris. He wanted the life of a businesswoman for me, an arbiter in my family's enterprises."

    k "W-what did your family do?"

    $chat.addmessage(fizz, "Fontaine. Tell me your real name. Not fucking fountain water. Who are you?")

    ki "Anything to change the subject." 
    
    $chat.addmessage(fon,"Louisa.")

    r 1j "What you in America call 'the protection racket'."

    $chat.addmessage(fizz, "Yeah? I don't have any damn thing to say to you, then.")

    k "Oh my god."

    s 1b "Oh my god."

    r 1m "My brothers shattered knees and slit throats for them. My sisters ran the gambling parlors."

    $chat.addmessage(fon, "No? Oh, I'm sad. You aren't?")

    ki "She's approaching me now, one step. One step. One."

    r 1n "My mother and father traded in these pitiable chemicals. These powdered fantasies, papillon."

    $chat.addmessage(fizz, "This is a dream. I'm dreaming.")

    r 1n "And I, I wanted none of it. So I ran. Ran to Paris to learn to cook, sweet Kylie. I wanted to be a chef, can you imagine?"

    pause 0.5

    show r 2c

    r "Something so foolish? So excerable?"

    $chat.addmessage(fon, "Oh, my, oh no. No, sweet boy.")

    k "Robin, no. It's not foolish to want out of that life!"

    r 1b "I have lived by my knives, my love."

    r "In the homes of the men who took me in."

    $chat.addmessage(fizz, "You're really her, then.")

    r 1k "I leveraged these alien features that drew the eyes of men and women from Belgrade to Zagreb. From Venice to Zurich. At last, to Paris."

    $chat.addmessage(elsa, "David that's impossible")

    s "I'm shaking. She's practiced this speech. Nobody talks like this."

    r 1b "My knives belonged in a kitchen, Kylie. My cooking was meant to overjoy, the richness of coq au vin, the simple pleasure of pomme frites."

    $chat.addmessage(fon, "And why is that, my Elsa? Help him understand.")

    r 1d "Not the liquid stupidity of {i}l'héroïne{/i}."

    $chat.addmessage(cake, "you guys hearing Robin right now? she's deep in it.")

    r 1b "Except... ratatouille couldn't get me to Paris."

    $chat.addmessage(elsa, "That girl's dead, David.") 
    
    $chat.addmessage(elsa,"Louisa died.")

    $renpy.notify("But David must have known that already...")

    r "Bisque couldn't bring me to you."

    k "I don't know what to say."

    $chat.addmessage(fizz, "Wha?")

    show r 2p

    r "Say you will meet with me again. And again."

    k "Robin, I... I'm not that person anymore. And I am so, so sorry for what we..."

    $chat.addmessage(elsa, "Louisa drowned, David. In the fountain outside R/BG13:14-15. She was in my support group, too.")

    pause 0.5

    k "For what I did to you."

    show r 1c

    r "No, papillon, you saved me. You gave me purpose. You were kind to me!"

    $chat.addmessage(beav, "Support for what?")

    pause 0.1

    show r 1b

    r "Am I not pleasing to your eye?"

    k "It's not that, you're..."

    $chat.addmessage(elsa, "... heroin addiction.")

    pause 1.0

    $chat.history.pop(-1)
    #SFX?

    pause 1.0

    $chat.addmessage(elsa, "Absolutely nothing.")

    s "... she's broken."

    r 1c "Have... I grown too old? Too ugly?"

    k "No, I-"

    $chat.addmessage(cake, "The hell?")

    r 1e "I would have killed time itself then, to stay the way you wanted me!"

    k "Because the way you're looking at me makes me feel like you're going to hurt me."

    pause 0.5

    show r 1d

    pause 0.3

    show r 1b

    r "Never. Not you."

    $chat.addmessage(fon, "Elsa, chat with me again?")

    r "Under the streets of Montmartre, you saved me. My body, my soul."

    $chat.addmessage(elsa, "Who ARE you?")

    pause 0.5

    r 2c "When you held me, shielded me. You let me weep, you let me bleed. You never judged my weakness."

    ki "My heart hurts from hammering in my chest. My arms and legs hang like earthworms. She lowers herself to me, so close I can smell her lipstick, tart and chemical."

    $chat.addmessage(fon, "Fontaine L'eau. Named for the place of my birth. :) x0x0")

    pause 0.5

    show r 1h at mt3
    show l 1d at fl11

    stop music fadeout 2.0

    l "Alright, back the fuck up."

    play music battle

    $chat.addmessage(elsa, "Fountain water. Oh my god.")

    l "Tania told me not to get involved. She said it wouldn't be fair."

    l 1k "But you're a damn psychopath and you need to back up."

    $chat.addmessage(beav, "the hell just happened")

    ki "Lichelle's presence next to me shatters the tension of the situation. Her body looms tense, volatile."

    r 1j "I have nothing to discuss with you."

    $chat.addmessage(sophie, "Oh, wow. I wish you guys could see what I'm seeing. ;)")

    l 1d "Don't care. We're gonna head out before you start going full yandere here."

    ki "I'm a little surprised Lichelle knows about yanderes, but maybe I shouldn't be?"

    r 1o "Kylie and I have far too much to discuss, mon pouffiasse."

    show r 1j

    $chat.addmessage(cake, "huh? sophie's chatting?")

    l 2k "Kylie. I'ma leave this to you, babe."

    k "What?"

    l 2d "Do I beat this chick's ass or what?"

    $chat.addmessage(sophie, "CHAT feverish, signs of SEPSIS")

    $renpy.notify("Robin is far more dangerous than she lets on, Kyles.")

    menu:
        k "Huh? I don't... what...?"
        "Fuck Her Up, Lichelle":

            l 1e "..."

            ki "Robin seems... shorter, suddenly."

            r 1b "You're making an inadvisable choice, Lichelle."

            pause 0.1

            ki "Menacing."

            ki "I've made my decision."

            k "... help me Elle!"

            l 1d "Gladly."

            ki "Lichelle seems far too ready for this."

            ki "The first steps she takes toward Robin are just... steps."

            ki "Then, a gallop. A bouncing boxer's step."

            ki "I don't even know if Robin knows how to fight."

            pause 0.1

            ki "It wouldn't have mattered anyway."

            ki "It only takes one punch. One feinted jab disguising a left cross."

            pause 0.1

            ki "A murderball, right down the center."

            stop music fadeout 0.4

            play sound "sounds/Lights Out.mp3"
            scene bg black

            pause 0.5

            # find a way to display dialogue of gutteral noise on both sides

            # scene - image of Robin slashing Lichelle
            pause 2.4

            
            #ARTART
            #scene - black

            ki "It was never supposed to be like this."

            $hideGui()

            pause 2.0

            play music [robinChoir, robin, robinChoir, robin] noloop

            show image litEye with dissolve

            pause 2.0

            show image splashLichFight with dissolve

            

            k "LICHELLE!"

            

            r "..."

            ki "I don't know where the butterfly knife came from."

            $chat.addmessage(fon, "Robin! You did it. :) You did so well.")

            

            l "... gghhhk..."

            $chat.addmessage(fon, "You made a difficult choice, Kylie. :) So Proud!")

            #show a combined image of Robin choking lichelle witha knife in her hand

            pause 0.1

            ki "Somehow, Robin is wrapped around Lichelle like a spider, the blade edge gleaming milky against her sienna skin."

            r "Kylie. I have not taken her life."

            pause 0.1

            r "I will. If you desire it."

            s 1c "No, no. No."

            $renpy.notify("Override. Menu: 'Kill Her', 'Spare Her' removed. $SparedElle = True")

            r "For you, draga mea, I spare her. Lichelle, certainly you despise me."

            ki "Robin maintains the blade's touch on Lichelle's neck as she unfolds, flowing to a safe distance."

            l "... yeah no shit..."

            show r 2f at fl11

            r "Understand this was a consequence of your choice. Should you attempt reprisal, next time, I will carve you to the bone."

            hide litEye
            hide splashLichFight with dissolve

            ki "Her tone lacks music."

            s 1f "Louisa, you cut me..."

            k "Robin! Disappear. Just disappear!"

            show r 2b

            r "Kylie?"

            k "DISAPPEAR!!!"

            pause 0.5

            show r 1c

            pause 1.5

            show r 1b

            pause 0.5

            # lights out

            $lichBio.loveUp()
            $fuckUpRobin = True
            $showGui()

        "Don't you dare touch Robin!":
            $fuckUpRobin = False
            k "... Robin's right, though."

            show l 1r at f13
            show r 1r at f11

            l 1k "Right? About what? Being a stalker?"

            ki "I turn to Lichelle, hoping my expression carries the apologies I intend."

            k "... everything she said is true. I never thought anything of it. I just..."

            k "I was in college, you know? I wanted to have all the experiences. So I went to France with friends and..."

            l "Did drugs and fucked an underaged prostitute. Really?"

            k "I... I didn't know."

            r 1j "Papillon, the age of consent in France is fifteen. "

            l 1d "Like that makes it better!"

            s 1q "Right?"

            r 1b "She is not at fault."

            l 1e "Weren't you a prostitute?"

            r 1c "I never received a single coin for our encounter, putain."

            s 1b "Maybe Robin didn't. Someone did."
            pause 0.1

            ki "I don't speak French, but I'm positive Robin isn't being as sweet as the words flowing from those dark lips."

            k "... I have to make it up to her, Lichelle."

            l 1k "The hell you do. Did you not notice the giant sack of H on the table?"

            show r 1m

            r "It's sugar."

            l 1d "Then why..."

            r 1a "Stagecraft, darling."

            show l 1d

            k "... ha."

            show l 1r

            pause 0.5

            k "Ahaahahahaa! Robin. Robin!"

            show r 1m

            s 1f "the lights"

            k "How beautiful. How perfect!"

            ki "And Robin only smiles."

            show l 1k

            ki "Lichelle relaxes."

            ki "If I hadn't been looking directly at Robin, I wouldn't have noticed her sliding the butterfly knife back into her sash."

            $robinBio.loveUp()
    # END MENU

    # sound effect of lights shutting off
    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 2.0

    $chat.addmessage(sophie, "Watching Fontaine and Elsa together, guys. Mmm lol haha jk :) ;) ")

    s 1b "Again?"

    pause 2.0

    k "Robin? Okay, this is not cool!"

    $chat.addmessage(bong, "")

    pause 1.0

    l "What is this pro wrestling bullshit?"

    pause 1.0

    k "Hello?"

    ki "Silence. Just silence."

    $chat.addmessage(egg, "")

    k "Lichelle? Robin?"

    pause 1.0

    k "Hey! I can't... is someone there? Anybody? This isn't fun anymore!"

    pause 1.0

    ki "And then, a soft brush of something firm against my neck. Something cold, scraping. Something..."

    $chat.addmessage(bar, "")

    ki "... metal."

    ki "A whisper."

    r "{alpha=0.5}I still have my father's blade.{/alpha}"

    # sound effect of lights
    stop music fadeout 0.4
    play sound "sounds/Lights Out.mp3"
    scene bg playhouse far

    pause 0.25

    k "Hey!"

    ki "When the lights come up, Robin is gone. The platters are gone, too. A thousand thoughts ricochet in my mind."

    ki "How did she do that? I couldn't hear anything moving or clattering. I'm stuck between heart-poundingly impressed and horrified."

    

    l "Alright, gloves off. Robin, I know you can hear me!"

    l 1e "Next time I see you, you're getting fucked up!"

    $chat.addmessage(fizz, "Elsa. Don't you leave with that... that thing!")

    show l 1o at f12

    pause 0.5

    l "Hey Kylie, you good? She's a psycho, I swear."

    pause 0.5

    l 1h "Oh. You have, uh, something on your neck."

    ki "My fingers easily find the tiny red ribbon flowing from the side of my neck, but I rub off a little and look at my fingertips anyway."

    $chat.addmessage(elsa, "Why not? You did.")

    ki "My heart flutters."

    k "I'm okay."

    l 2i "Is that blood?"

    $chat.addmessage(fizz, "What happened to that girl?")

    k "I... I don't know what I'm feeling right now."

    ki "I ... I think I want more. The rush, the rush engulfs me."

    $chat.addmessage(elsa, "Why do you care?")

    k "That was some date."

    show l 1k

    l "That wasn't a date. That was a horror movie."

    k "I get the feeling Robin isn't much for small talk."

    $chat.addmessage(fon, "Pleeeease Elsa I'm waiting for you :)")

    l "Obviously not, she-"

    # sounds/Lights Out
    play sound "sounds/Lights Out.mp3"
    scene bg black

    pause 2.0

    l "God dammit, Robin!"

    ki "The lights are gone. My heart races again. Is she back? I brace for some sensation against my skin, terrified it will come and never come in the same instant."

    $chat.addmessage(elsa, "She drowned. In the fountain. I told you.")

    pause 1.0

    r "{alpha=0.3}Shhh.{/alpha}"

    pause 0.25

    ki "I hear her whispered voice again, but there's no touch. She showed me already that her power over me is absolute."

    pause 1.0

    ki "It was just a knick. She could have split me from ear to ear if she wanted, couldn't she?"

    $chat.addmessage(fizz, "Elsa, how? How the fuck does someone drown in a fountain?")

    pause 1.0

    # robin laugh sound?

    l "Gah! FUCK!"

    r "Goodnight, my darlings."

    $chat.addmessage(elsa, "... she overdosed. Sophie was there, David.")

    ki "Her voice flows from somewhere far away, echoing lightly."

    # sound
    play sound "sounds/Lights Out.mp3"

    scene bg playhouse far
    show l 3i at f12
    

    # with blood?

    k "Oh my god, Lichelle!"

    play music onTheNod 

    s 1c "Holy shit."

    $chat.addmessage(elsa, "Not that you give a shit.")

    ki "She's staring at me, her eyes wide with shock and pain. There's a slash of blood across her chest, shallow, but running in a neat flowing path."

    l 3e "I'm gonna fucking kill you bitch! I swear to god!"

    k "Are you okay? Should we call the police?"

    $chat.addmessage(fizz, "Look, I didn't know.")

    l "You better hope they find you before I do!"

    ki "The camera crew moves in, right on cue, and Lichelle to my great surprise doesn't front kick one of them into oblivion."

    $chat.addmessage(elsa, "It's always a perfect excuse, isn't it. Not to know.")

    ki "Rather she lets a slow breath out and allows them to film her. Her chest rises and falls, heavily." 
    
    $chat.addmessage(elsa,"I'm sure you have an excuse for not being here. Sophie hasn't answered me.")

    ki "A swipe of blood saturates her top."

    k "Lichelle. You're okay?"

    ki "She nods."

    $chat.addmessage(cake, "What do you do, Elsa?")

    l 3k "Yeah. She ruined my shirt."

    k "That's what you're worried about?"

    $chat.addmessage(elsa, "I run St. Agatha's Revelation.")

    ki "Sighing, Lichelle dabs a finger in the darkening red running down her chest."

    $chat.addmessage(beav, "And that is?")

    l 3d "It's a theatre prop. Fake blood. She put it on you, too."

    k "Oh."

    stop music fadeout 5.0

    ki "Except the burning pain tattooing my neck begs to differ."

    $chat.addmessage(elsa, "It's a mission here in R/BG13:14-15. We're a rehabilitation program for addicts of all types.")

    show l 3q
    # up close if possible

    if lichBio.love == 4:
        # note you have to pick her both times at first roundup and agree with her on both second-play dates.

        k "Elle?"

        show l 3m at zoom12

        ki "She's staring at me now, eyes full of purpose."

        l "She's insane."

        ki "A whisper, nothing more."

        l 3n "You're a criminal rave bitch under that wallflower exterior."

        k "... that's not me."

        l 3p "It's okay if it is."

        ki "She's close now, close enough that if I were a braver woman I could be brushing against her."

        l 3u "I need to wash this off."

        k "Yeah."

        l "Let's get out of here."

        k "Yeah."

    scene bg black with dissolve

    "It doesn't matter. Lichelle's okay. The night is... what it is."

    "Part of me feels far too upbeat about all this."

    show image carLightsLight at carLights
    show image carLightsBack with dissolve:
        xpos 0 ypos 0

    play music lichelle 
    
    pause 2.0

    show image carLich with dissolve:
        xpos 0 ypos 0

    ki "The car ride home lasts an eternal instant. Cassandra's humbled sobbing echoes in between fits of Robin's cold laughter in the pitch black."

    ki "Lichelle wears the same placid expression she wore on the way to the theater."

    ki "Astonishingly."

    $chat.addmessage(beav, "Heroin?")

    ki "These two nights wrestle for dominance in my mind. The show has faded into an afterthought."

    ki "I look to Lichelle, sitting with her sleeveless top mired in sticky theatre blood."

    $renpy.notify("Where'd the blood go?")

    $chat.addmessage(elsa, "Yeah.")

    $chat.addmessage(fon, "Elsa, I'm starting without you ;)")

    s 1j  "~yaaawn~"

    if lichBio.love == 4:
        # option for love scene ending with Lichelle

        ki "She's been the one constant over these few days."

        ki "Streetlights paint her features brightly, then vanish, then paint once more."

        k "Hey, Lichelle..."

        show l 2s at f11
        l "Hm?"

        ki "Her expression is so far away. She's so fearsome in her way that this vulnerability captivates me in the darkness."

        $renpy.notify("give in, babe. You need me.")

        s "Wow. I can't believe Kylie's thinking about anything other than running the ~yawn~ hell away."

        menu:
            ki "Should I..."

            "Make a move":
                k "Lichelle. What if we ended the show right now?"
                play audio heart noloop
                show image glitchGui at frameGlitch
                k "Mm... nothing. It's nothing."
                l 1g "Cool."
            "Don't make a move":
                k "Mm... nothing. It's nothing."
                l 1g "Cool."

    scene bg hallway with fade

    pause 0.25

    show l 1o at f12

    l "So I'm gonna go get a shower and try not to go kick Robin's ass. You might want to lock your door tonight."

    k "You think she's really dangerous, though?"

    $chat.addmessage(fizz, "That's not the place I took Sophie.")

    show l 1g

    if fuckUpRobin:
        l "Babe, I fight professionally. She coulda killed me."
        l 1k "I messed up."
        k "You seem awfully calm about that, Elle."
        l "Nothing to do about it now. Just don't turn your back on her."
        k "It doesn't make sense that she could do that to you."

        l 1d "No. No, it does not."
    else:
        l 1k "She splashed us with fake blood, but I think she was sending a message. Showing us what she could have done if she wanted."

    pause 1.0

    show l 2s



    l "... are you okay?"

    k "I'm fine. I've never had anything like that happen before."

    $chat.addmessage(elsa, "I know. Louisa met her at Michael of Le Sabre and they got close.")

    show l 1o

    l "I'd hope not."

    show l 1m

    $chat.addmessage(elsa, "Louisa brought her to our program because Le Sabre was corrupt.")

    k "I didn't expect it. I didn't expect her to know me. Or for her to be ... that girl."

    l 2r "I just wonder how many people were hiding in there. No way she moved that table on her own and did all that stuff from the stage."

    k "I have no idea."

    $chat.addmessage(beav, "Corrupt?")

    ki "It's hard to think, even now. I feel drained, like all of my energy has been spent dissecting those few minutes in the dark."

    $chat.addmessage(elsa, "Louisa used to say everyone there was either selling jewelry or wearing it.")

    s 1b "... you're all frickin' nuts."

    show l 1q

    l "Get some sleep. Hey, it's you and me tomorrow."

    $chat.addmessage(fizz, "Jewelry. Meaning heroin.")

    k "Yeah."

    ki "So, so tired."

    $chat.addmessage(elsa, "Yeah. Usually. Sophie got people using that term.")

    k "Please don't let it be a disaster. If we just get fast food and watch TV I'll be fine."

    show l 1m

    l "Don't worry babe. Tomorrow's gonna be nothing like the last two days for you."

    $chat.addmessage(beav, "and You were looking after Louisa, too?")

    scene bg dressing with dissolve

    stop music fadeout 2.0
    play music2 bedroom fadein 3.0

    ki "I don't even have time to consider much more. I didn't even intend to flop directly on the bed and drag a pillow under my head. It just kind of happened."

    $chat.addmessage(elsa, "Louisa was my friend. She was recovering, you know? She was.")

    ki "The knick on my neck burns a little still."

    ki "I have a date with Lichelle tomorrow and yet, somehow, I feel so very alone."

    $chat.addmessage(fizz, "I owe you so many apologies, Elsa. I'm so sorry. I had no idea.")

    ki "Maybe Tania will have something to tell me when she gets back."

    scene bg black with dissolve

    pause 1.0

    s 1b "... guys. I need to pee, but I don't wanna get up."

    $chat.addmessage(elsa, "Yeah. Thanks. Thank you.")

    s 1j "Sophie's a sleepy girl. I just don't feel like getting up."

    pause 0.5

    s "... so we might as well go on."

    scene bg black with fade

    s 1j "This game. All these lights?"

    $chat.addmessage(cake, "Elsa, you still at Sophie's place? damn cops ever gonna show?")

    s 1b "I like Cassandra. She reminds me of someone."

    s 1m "Robin, she reminds me of someone, too."

    $chat.addmessage(elsa, "I'm here, yeah. I can hear her talking. She's not answering the door.")

    s 1i "That story about her dad's knife. She's killed someone, maybe."

    $chat.addmessage(fon, "Definitely :) Elsa, I know how to get Sophie to answer the door.")

    s 1j "I don't have to pee. Anymore."

    $chat.addmessage(fon, "Come back to me, you won't regret it. :)")

    pause 1.0

    $getHistory(14)

    stop music2 fadeout 4.0

    pause(0.5)
    $hideGui()
    scene bg load-run with fade
    pause 2.0
    pause
    pause(0.5)
    
    

    jump common4
