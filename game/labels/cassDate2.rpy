label cassDate2:

    # Remember, Cassandra's theme is inability to communicate, a voice taken for someone else's purpose

    
    scene bg story-3 with fade
    pause

    scene bg hallway with fade

    pause 0.5

    $showGui()

    # ---------------------------------------------------------

    $renpy.notify("stringSever(firstName) but never sever god")

    # ---------------------------------------------------------

    s "So... okay. If you guys have cooled off, we'll get started again."

    $chat.addmessage(fizz, "We're good. Sorry.")

    $chat.addmessage(cake, "he straight")

    pause 0.4

    s "Good. Then let's move on."

    $chat.addmessage(elsa, "Sophie, taking charge.")

    s "We're going back to the bar with Cassandra, then."

    $chat.addmessage(beav, "getting turnt up")

    pause 0.5

    s "Turnt up? No, nothing like that. Heh. That's silly."

    s "You're silly, AngeredBeaver69." 
    
    $chat.addmessage(fizz,"Elsa.")

    pause 0.1 
    
    $chat.addmessage(elsa,"Shush.")

    s "I wonder why we went to the bar at all the first time? Isn't like we did much there."

    ki "The car ride is ... exhausting. Lichelle sits next to me in the backseat, playing with the little silver cross dangling from her neck, perfectly silent."

    $chat.addmessage(bar, "Freud having a field day with that")

    ki "Now and again she glances at me, her dark eyes filled with purpose."

    ki "Then, back to looking out the window, rubbing the cross between her finger and thumb."

    $chat.addmessage(elsa, "I wonder what it'd be like to date a pro fighter.")

    ki "Streetlights glimmer to life outside, pouring slats of glow over her features."

    ki "Now I know what it feels like to be hunted by an apex predator."

    $chat.addmessage(crab, "you're hittin that missionary and then she's like fluckin' tap or I break your arm :D")

    scene bg bar with fade

    show l 1o at f12

    l "Cassandra's coming in now. I better haul ass or she might think she's being sabotaged."

    $chat.addmessage(beav, "thta's funny considering she's gonna be at robin's place spyin'")

    k "That's probably a good idea. I mean, considering the show and all."

    show l 1j

    ki "She doesn't answer that, but the hint of smile on her face tells me all she wants to convey."

    $chat.addmessage(elsa, "Cassandra said she wasn't actually there, right? Just had it figured.")

    ki "If it weren't for the cameraman filming for b-roll, I think she might pounce on me."

    $chat.addmessage(beav, "oh right")

    s "She's sabotaging Cass no matter what though. I wouldn't want my date to have someone else on her mind."

    scene bg bar with fade

    ki "Breathe. Breathe."

    s "~ yawn ~ yeah, self. You can do it."

    ki "The establishment is an odd one. It's a bar, obviously, but there are regular tables and booths all around the floor."
    
    ki "No one's eating anything, so my guess is this place is..."

    $chat.addmessage(cake, "MEET-CUTE")

    ki "A hookup parlor?"

    $chat.addmessage(cake, "aww man")

    show c 1p at fr12

    ki "She's here. This is real."

    c "..."

    ki "Cassandra's easy to spot. Part of that's because of the film crew moving around to accommodate her, but it's also because she has such a soft presence."

    $chat.addmessage(fon, "My sweet siren :)")

    ki "It's a magnificent contrast to Lichelle's overwhelming power."

    k "Hi, um, Cassandra! Um, how, um... okay."

    show c 1m

    ki "She's smiling. I didn't see that yesterday. Meanwhile, she produces a cellphone from her pocket and shows the screen to me; there's a note app with several entries."
    
    ki "Looks like she came prepared."

    $chat.addmessage(cake, "need to watch for things that changed this time")

    c "< I'm happy to see you, Kylie. I was a little worried you might have a change of heart. I know my silence earlier must have been strange for you. >"

    ki "I wonder if the way she writes mimics the way she would have spoken."

    $chat.addmessage(elsa, "I'm afraid I'll miss a change because I don't remember what she said the first time")

    k "No, no, it's fine! Tania told me a little about how we could communicate and it actually sounds kind of fun, and, uh... yeah."

    c 2n "< So let's get fucking thrashed, how about it? >"

    $chat.addmessage(elsa, "Well, nevermind then")

    ki "I guess the benefit of having to read her words is I have time to consider them."

    $chat.addmessage(bar, "Cass truly beastin this time")

    ki "The downside is I'm not sure if she's joking."

    k "You're kidding, right?"

    $chat.addmessage(fon, ":(")

    c 2m "< Not at all. I wanna show you what a rock star life is really like. >"

    menu:

        s "Rock star life, eh."

        "Have a drink":
            k "All right Cassandra, you're on. Order for both of us and impress me!"

            c 1n "< That's what I wanted to hear! >"

        "Just juice":
            k "I wouldn't mind some cranberry juice."

            c " < Pity about that because I ordered like seventeen shots way ahead. >"

            s "So I have to drink? The game isn't giving me a..."

            s "... fine."

    # end choice

    $chat.addmessage(crab, "Did you notice the chat never works when it's decision time.")

    show c 1l

    ki "The camera crew keeps its distance, far enough that I could probably forget about them after a few days of this."

    $chat.addmessage(elsa, "Kylie's gonna end up drunk and make a bad decision isn't she :(")

    ki "Problem is, this is day one and I feel like a drama student who can't quite get her lines out."

    s "~yawn~ Sorry guys, sorry."

    $chat.addmessage(cake, "you okay Sophie?")

    c 1q "< It's a strange situation we're in. I want to tell you up front that I am serious about this. >"

    ki "I believe her, and still, I'm not sure how to interpret the message."

    s "Yeah Fizz, I'm just tired."

    $chat.addmessage(beav, "You've had a few drinks too, right? I'm guessin?")

    k "I guess this is the part where we tell each other about, uh, each other?"

    ki "God, I'm an idiot."

    s "Kylie's too hard on herself. Yeah, Beaver, I had something. Just to calm down."

    c 1m "< Hey, this is why we're getting stupid in a sec. >"

    pause 1.0

    $chat.addmessage(bar, "don't forget to hydrate")

    k "Okay. So, uh, Cassandra. How'd you end up on the show?"

    ki "Nicely done, self, a fully formed question!"

    c 1r "< Mmm I dunno. I'm bored. There's no inspiration left in my life. >"

    $chat.addmessage(unkn, "what is my function")

    $chat.addmessage(crab, "she different isn't she")

    c "< I figure if I do this I'll have a new batch of experiences. Maybe find my voice again. >"

    ki "Is that... wait, is she talking about her --"

    $chat.addmessage(bar, "If things are different, I wonder if her scars are different, too.")

    show c 1j

    ki "Her smile broadens. It's going to be hard to tell when she's joking, isn't it?"

    ki "I chuckle, but I don't know if it's appropriate."

    $chat.addmessage(elsa, "Maybe Kylie just remembers things differently this time.")

    c "< It was a joke. >"

    $chat.addmessage(beav, "What do you suppose this game is about?")

    k "I, uh, I knew that!"

    c 1g "< The songs used to be personal. Wild. Angry, even. Now I'm wealthy, comfortable. What do I have to be so pissed about? >"

    $chat.addmessage(fon, "Everything :) You'll see, trust me ;)")

    c "< It all feels mechanical now. >"

    ki "I suppose this is as good a time as ever to tell her that I..."

    $chat.addmessage(cake, "fangirl reveal")

    k "I love your newer stuff though."

    show c 1k

    ki "Her expression changes, then, as she accepts this new piece of information. I'm not sure if she hoped I'd be a fan, or hoped for the opposite."

    c "< You're not a fangirl, are you? >"

    k "No, no, maybe? I love your work. Intolerable Jewelry got me through the worst break-up of my life!"

    python:
        newComments = [
            [beav, "ROLL CREDITS I did it"],
            [bar, "Kylie said that twice."],
            [elsa, "Yes, I thought it'd be a different song."],
            [crab, "Roll... fluckit, roll credits!"]
        ]

        chat.bulkMessage(newComments, "random")

    s "Breakups are the worst."

    pause 1.0

    # show sophie crying

    $chat.addmessage(elsa, "Sophie?")

    s "..."

    $chat.addmessage(fizz, "Sophie...")

    $chat.addmessage(crab, "hey what's wrong?")

    s "I'm sorry guys."

    show image splashBRB at alphaFade
    #SFX: Woman crying

    pause 0.8

    python:
        newComments = [
            [cake, "what's wrong?"],
            [beav, "god, that's the saddest sound I ever heard"],
            [unkn, "Resonance"],
            [bar, "Girl you okay?"],
            [fon, "Sophie!!"]
        ]

        chat.bulkMessage(newComments, "random")

    pause(0.5)
    hide c at f12
    $hideGui()
    scene bg story-4 with fade
    pause(2.0)
    pause
    scene bg bar with fade
    pause(0.5)
    $showGui()
    pause(0.5)

    show c 1a at f12

    ki "Her smile falters a little bit. She's typing feverishly, and I wonder whether I've found a way to ruin everything already."

    c 1k "< See, do you know that what song's about? >"

    $chat.addmessage(elsa, "Sophie?")

    k "It's about having like a really attractive ex who you keep wanting because they're so beautiful but you can't stand them, right?"

    ki "She smiles, darkly."

    $chat.addmessage(fizz, "Hey, you okay?")

    c 1t "< You would think. It's about my hood ornament. >"

    s "Her what?"

    $chat.addmessage(cake, "she drives a Rolls-Royce or something")

    k "Your what?"

    c 1u "< Yes, seriously. Not the one on my car, though.>"

    $chat.addmessage(crab, "sophie baby girl do me a favor and answer us")

    ki "Cassandra leans back in her chair, her hands falling to the tabletop. She breathes out, chuckles a mute chuckle."

    $chat.addmessage(fon, "I love this part. :)")

    c "< I have a piercing. Down there, you know. >"

    s "Oh."

    k "Oh. Wait, really?"

    $chat.addmessage(beav, "she has a doorbell lol")

    ki "She nods, slowly."

    k "So the song that got me over him was..."

    $chat.addmessage(elsa, "Ow ow ow ow ow ow ow nope")

    ki "Another nod."

    c 1j "< About my clitoral piercing. >"

    pause 0.4

    c 1t "< Disappointing, huh? >"

    $chat.addmessage(fon, "It's not that painful. ;)")

    k "... no."

    $chat.addmessage(crab, "pics or it didn't happen, Fontaine")

    k "No, I'm glad!"
    
    show c 1h
    
    k "I mean, maybe you didn't mean it the way I interpreted it, but that happens all the time in real relationships!"

    $chat.addmessage(fon, "Private chat me then ;)")

    show c 2s

    k "So it's still meaningful to me."

    $chat.addmessage(cake, "thirsty af")

    pause 0.5

    show c 1b

    pause 0.5

    show c 1m

    c "<I'm really happy to know you're a fan. Might not seem that way, but I like the way you think.>"

    c 1p "< And I like the way you look, too. I made a good choice coming here. >"

    $chat.addmessage(crab, "Shub ain't answering my call.")

    k "I don't want to be a bothersome fangirl. I mean, I am, but not like, you know? Like that."

    c 1j "< You're handling it well. >"

    $chat.addmessage(fon, "Shub-Nickelrath is resting ;)")

    k "On the outside. Inside, I'm screaming like a banshee on fire."

    show c 2u

    ki "I don't want to put her on guard, and it seems to be working. Her finger traces the edge of her phone, lightly, meaningfully."

    $chat.addmessage(elsa, "Sophie, are you seeing this?")

    ki "The drinks arrive, and for a moment the interruption of a server derails our conversation."

    hide c at f12

    ki "She wasn't kidding, either. The platter hosts no less than twelve shot glasses filled with god-knows-what."

    $chat.addmessage(fizz, "Jesus, Fontaine, just post the picture to the chat if you're that obvious.")

    ki "I find myself wringing my hands lightly together. This is so much harder than it looked on TV. Magic of editing, I guess."

    pause 1.0

    show c 1s at f12

    c "< So Kylie. Gun to your head, who would you sleep with first, me or Robin? > "

    $chat.addmessage(fon, "I don't want to get Sophie kicked off Switch :)")

    k "Wow."

    ki "Cassandra pounds a shot. Then another. And another."

    show c 1f
    pause 0.2
    show c 1j

    $chat.addmessage(cake, "Elsa came back fine, man. Fortify.")

    c "< I know you like my work. And I guess you wouldn't be on the show otherwise, but... you like girls, right? >"

    $chat.addmessage(crab, "aight fountain water, put yo money where yo lips is XD")

    ki "The question strikes me as fully appropriate and adorably obvious."

    k "I..."

    $chat.addmessage(fizz, "... lol?")

    ki "I guess someone should have asked this question already. It dawns on me, just now, that nobody ever asked me flat out if I... huh."

    c 1o "< Well, I do. And I think you'd pick me.>"

    $chat.addmessage(elsa, "Sophie please answer us. Can you see the chat?")

    show c 1m

    s "I'm not sure I like Cassandra this time. She's... entitled, I guess."

    ki "Her smile was tempting from the moment it poured across her lips. Now, it's downright mesmerizing."

    $chat.addmessage(beav, "Sophie ghostin us")

    k "I do, too."

    s "Oh. Well, nevermind what I want then. That's fluckin' life, I guess."

    $chat.addmessage(cake, "we earned it")

    c 1n "< I always thought this show was fake. Really, I did. How's a person supposed to fall in love in two dates? >"

    k "I don't know."

    $chat.addmessage(bar, "You two assholes earned it. Thanks.")

    ki "It's easy for me. I know who she is, I've idolized her, even. To her, though, I'm just another face."

    show c 1f
    pause 0.2
    show c 1k

    ki "Cassandra slams another shot, easily, in a practiced way."

    $chat.addmessage(cake, "you right")

    c 1o "< C'mon, drink up. If you think I'm attractive now, just wait 'til shot nine. >"

    ki "Fine, then. I drain the first glass and immediately cough and sputter."

    $chat.addmessage(egg, "")

    k "Good god, what is this?"

    c 1n "< Special ordered Russian vodka. One of my girlfriends was from Marilinsk and turned me on to it. >"

    c 1m "< She was stone cold, Kylie. Two things Russia makes best are vodka and badasses. >"

   

    ki "I take another shot. It's easier than the first."

    s "The second shoot's always easier. The second... shot?" 
    
    $chat.addmessage(bar,"sophie?")

    ki "Two more shots for Cassandra. How is she alive, at all?" 
    
    $chat.addmessage(crab,"goddamn")

    s "~yawn~"

    c 1g "< She died. >"

    s "Oh. Shit." 
    
    $chat.addmessage(cake,"yo crab, you get to see Fontaine's fountain?")

    ki "The warmth blooming in my belly freezes at that. Have I stepped on a land mine, so quickly?"

    k "I'm sorry..."
    
    $chat.addmessage(elsa,"eww!")

    c "< Yeah. I guess she couldn't handle us not being a thing. >" 

    c 1o "< She was great, but I wanted tear shit up. I'm not marrying some dime piece from who-gives-a-shit Russia. >"

    c 1b "< She wanted me to give up everything I liked doing and just be some clean living boring damn nobody. >"

    #attempt deployment of reversed message to chat
    $temp = reverseString("Such beauty, pristine, the pursed lips of a winter rose, my eyes dissolve before this antediluvian construct of form and flesh, my unworthy tongue wrenched gratefully from my throat, god, god forgive me for daring to exist in the same temporal space as her, as her, as heR")

    $chat.addLinearMessage(crab, temp, 0, 3)

    $chat.history.pop(-1)

    k "What happened?"

    s "Why would you ask that, Kylie?" 
    
    $chat.addmessage(elsa,"God.")

    c 1d "< She overdosed. I found her the next day. She left a note on the floor under her. Blamed me. >"

    ki "Another shot, two, three. Cassandra's deep into my side of the platter, now." 
    
    $chat.addmessage(fon,"sorrow")

    k "Oh my god."

    show c 1g

    ki "< She's smiling, mirthlessly. Painfully. >"

    c "< She was right. It was my heroin. Didn't you read my book, fangirl? It's my fault. >" 
    
    $chat.addmessage(fizz,"Stop playing this game, Sophie.") 
    
    $chat.addmessage(crab,"keep playing wow")

    s "..."

    pause 1.0

    s "Guys, I need a break. Just a minute. Again. Sorry."

    show image splashBRB at alphaFade

    pause(0.5)
    $hideGui()
    scene bg story-5 with fade
    pause 2.0
    pause
    scene bg bar with fade
    pause(0.5)
    $showGui()
    pause 0.5

    show c 1c

    s "Sorry. That just got a little too real for me." 
    
    $chat.addmessage(elsa,"Sophie please. Answer, okay?")

    s "Anyway. Sorry. Let's keep going."

    s "I think this game is bad for me."

    pause 0.2

    s "But I keep coming back to it." 
    
    $chat.addmessage(fizz,"Sophie pick up your phone.")

    pause 0.4

    s "How fucking appropriate."

    pause 0.2

    k "It's not your fault."

    ki "She waves the sentiment away."

    c 1d "< It's cool. She did what she had to do. Respect. >"

    s "She's so different this time. Losing someone you... losing someone you care about like that." 
    
    $chat.addmessage(cake,"she needs help, like, pro help")

    s "She must be in so much pain and just medicating it with booze. She has to be."

    k "It doesn't bother you at all?" 
    
    $chat.addmessage(fizz,"I swear to god I'll SWAT you if I have to Sophie")

    c 1m"< Hey. Listen. I wrote a song about it. Let's go to my studio and fuckin' jam it. For Mia."

    show c 1c

    ki "And there it is. The well of feeling she's been holding back for god knows how long breaks apart."

    c "< This is going as bad as anything could possibly go. >" 
    
    $chat.addmessage(elsa,"David don't you dare!")

    c 1b "< It should've been me. Not her. >"

    pause 0.2
    $chat.history.pop(-1)
    pause 0.4
    $chat.history.pop(-1)

    k "No, it's okay! God, Cassandra, that's horrible."

    ki "She reaches for another shot, but I pull the platter away." 
    
    $chat.addmessage(fon,"FizzyFizion. You obviously care about Sophie :)")

    k "Stop! That's not going to help."

    c 1c "..." 
    
    $chat.addmessage(fizz,"I love her.")

    k "Please don't be mad. I think you need to talk about this with someone like... professional." 
    
    $chat.addmessage(elsa,"Asshole!")

    ki "She nods, tears pouring down her cheeks."

    k "Let's get a cab and get out of here." 
    
    $chat.addmessage(fon,"I love her, too. She's the best. :)")

    c 1b "< To my studio. >"

    k "I'm struggling between my inner fangirl and my concerned adult human right now." 
    
    $chat.addmessage(fizz,"You don't even know her.") 
    
    $chat.addmessage(unkn,"R/BG13:14-15")

    c 1q "< I appreciate it, too. >"

    c 1o "< Never meet your heroes, right? I'm sorry I'm disappointing you.>" 
    
    $chat.addmessage(fon,"Private chat, Fizz? I'll tell you how I know her :)")

    k "Oh trust me, you, and, uh... I mean... sorry, I'm a little tongue tied."

    c 1b "< I can help with that. >" 
    
    $chat.addmessage(fizz,"Maybe later. For now, I need to brb.")

    ki "A cool thrill shoots along my skin. Easy, Kylie, she could mean just about anything by that."

    s "But you're drunk, Cassandra. And hurting. I'm not, I'm not gonna let you use me to fill that hole in your heart." 
    
    $chat.addmessage(elsa,"I'm sorry Fizz. I'm the asshole, not you.")

    s "I'm not some bandage for your broken fucking heart!"

    c 1j "< Don't worry. There's a bed at the studio, and bathroom. In case all the shots were too many.>" 
    
    $chat.addmessage(bar,"The hell am I missing here?")

    ki "I'm mostly impressed with how well she types despite swaying all over the place."

    pause(0.5)

    hide c at f12
    $hideGui()
    scene bg story-6 with fade
    pause 2.0
    pause
    scene bg studio with fade
    pause(0.5)
    $showGui()
    pause 0.5

    $getHistory(10)
    $sceneNum = 11

    #----------------------------------------------------------------------------------------------------

    s "Guys. I'm sorry for that."

    pause 0.5

    s "I won't let it happen again. I promise."

    pause 0.5 

    ki "The studio is almost exactly what I would have expected. There's a drum kit, tons of wires, and blinking lights that I guess are part of editing equipment." 
    
    $chat.addmessage(beav,"Cassandra drank at least eight shots in like two minutes. She dead.")

    ki "I'm no expert on music production, and I'm no expert on the odd foam mat and beer smell that permeates the walls and floor."

    show c 1q at fl12

    c "< Sorry about the mess. TBH I wasn't sure if I'd ask you to come here. >" 
    
    $chat.addmessage(bar,"I can do that")

    k "Oh? I kind of thought this was part of the plan from the start."

    c 1t "< I wanted to know if you were just in this for the sex. >" 
    
    $chat.addmessage(beav,"yeah but she little. you probly like a regular size dude")

    k "Oh. Um. You're welcome?"

    ki "I can't help but notice how Cassandra walks as she leads me into the studio. I noticed at the bar, too, but she sort of flows from one long, considerate gaze to another."

    show c 1p

    ki "Her expression loses focus sometimes. It could be just because she's drunk. I wonder, guiltily, if she's somewhere on the autism spectrum."

    ki "Then I remember I don't know enough about it to decide one way or another." 
    
    $chat.addmessage(bar,"Regular sized. lol. I'm a thicc boi, son")

    k "So, uh, Cassandra?"

    c 1s "... ?" 
    
    $chat.addmessage(beav,"dis thicc dicc lol")

    k "Which one do you play?" 
    
    $chat.addmessage(fon,"Really? How thicc? :O")

    ki "She points to a beautifully finished seven-string guitar hanging from a mount on the wall. It has a marbled pattern, swirling in royal blue and aquamarine."

    pause 0.5

    show c 1l

    ki "She points, emphatically, to her phone screen." 
    
    $chat.addmessage(cake,"silence, thot")

    c "< I sing, too. >"

    k "But you can't talk? I thought for sure you had a singer?" 
    
    $chat.addmessage(fon,":(")

    show c 1k

    ki "Her smile sours, just a bit."

    c "< Don't say it out loud. >" 
    
    $chat.addmessage(elsa,"You know, the mechanics of this don't make sense.")

    c "< I sing on all the albums, just not live. Mia used to sing for me on stage. >"

    k "Oh." 
    
    $chat.addmessage(elsa,"Like, wouldn't this Mia sound different from Cassandra?")

    s "Oh god."

    c 1b "< As far as the world knows, I'm just a guitar player and songwriter. >" 
    
    $chat.addmessage(beav,"not if they practice together all the time. sounds like they did all the things together")

    ki "This all feels so rushed. I've adored her music without even knowing what kind of person she might be. There's a camera crew around us, even in this small space."

    ki "What if I talk? She's probably pretty powerful if she's a Quillboard top 10 artist, right? Suddenly I find myself cold, nervous." 
    
    $chat.addmessage(elsa, "Last time Cass sang and then was bleeding. That's not how that works.")

    ki "Or is that excitement?"

    k "Why would you trust me with a secret, though? We really only just met?" 
    
    $chat.addmessage(beav,"wish i coulda watched those rehearasals")

    c 1c "< I don't have time to earn your love, so I have to buy it. >"

    s "... huh." 
    
    $chat.addmessage(elsa,"... that's the saddest thing I've ever heard.")

    k "I promise, then." 
    
    $chat.addmessage(cake,"poor everyone man. fluckin game took a dive ")

    ki "Cassandra's features focus. I thought she would smile, but..."

    c 2b "< Okay. Come with me into the recording booth? >" 

    hide c at fr12
    
    $chat.addmessage(elsa,"Fontaine, how depressing is this gonna get?")

    ki "As Cassandra moves to the booth, snagging a water bottle on the way, one of the camera crew picks up behind her."

    show c 1e at fr13

    c "!!!" 
    
    $chat.addmessage(fon,"No spoilers ;)")

    show c 1i

    ki "-- but she wheels around then, a horrified expression on her face, and crumples to her knees." 

    hide c 1f at d13
    
    $chat.addmessage(bar,"oh no")

    ki "... and promptly begins to heave."

    ki "The cameraman nearest her pauses, looks to Lichelle as if asking what to do next. She's been so quiet I forgot she was with us." 
    
    $chat.addmessage(beav,"she's paying for all those shots, now")

    show l 1m at fl11

    ki "Lichelle, hanging back by the entrance, snatches up a trash can."

    show l 2m

    l "Kylie, here!" 
    
    $chat.addmessage(cake,"Elle to the rescue")

    ki "I turn my head just in time to see the bin come flying at my face and-"

    # klonk sound

    pause(0.5)
    $hideGui()
    scene bg story-7 with fade
    pause 2.0
    pause
    scene bg black with fade:
    pause(0.5)
    $showGui()
    

    scene bg studio with longestFade

    s "This date has gone fully off the rails." 
    
    $chat.addmessage(cake,"KTFO baybay")

    scene bg black with fade


    ki "It's odd, what one notices when one has been clocked with a bin chucked by a professional MMA fighter."

    scene bg studio with longestFade

    ki "For example, I find myself busily studying a scratch in the wood flooring, wondering what on earth could have caused such a small, consistent fissure." 
    
    $chat.addmessage(beav,"been there.")

    ki "And everyone around me sounds like they're underwater."

    ki "And there's something soft and warm under my head."

    show l 1i:
        alpha 0
        linear 0.5 alpha 0.5
        linear 0.5 alpha 0.5
        linear 0.5 alpha 0
        repeat

    l "Hey hey hey, welcome back."

    

    l 1q "I am so, so sorry for that! I really thought you had it, babe." 
    
    $chat.addmessage(elsa,"She calls Kylie babe and I like that. I bet she has a deep, sexy voice.")

    ki "I find myself turning to lay flat, which probably is a bad idea, and realize that warm softness is Lichelle's lap."

    show l 1m:
        linear 0.5 alpha 1.0

    k "Clearly."

    s "Should she have put my head there? I mean I'm probably concussed. Might not want to move my neck."

    scene bg studio with dissolve
    
    $chat.addmessage(bar,"Suspend disbelief Sophie. Even if you aren't talkin to us.")

    show l 2t

    l "You're okay, trust me. I've been KO'd more times than I can remember."

    k "I don't think that's a good thing." 
    
    $chat.addmessage(cake,"lol")

    l 2j"You're doing better than her."

    ki "She nods toward Cassandra. The songstress weeps softly, lying on her side and groaning, the upright trash can anchored next to her." 
    
    $chat.addmessage(unkn,"Nausea. It's always this way, until you get the next one.")

    ki "I feel like I should say something, but nothing comes to mind."

    ki "Cassandra looks so defeated, lying there helpless and fully out of control." 
    
    $chat.addmessage(elsa,"Sophie...")

    ki "Her choker lies next to her on the floor, gleaming elegantly, as if to contrast her."

    l 1b "I guess her secret's out."

    ki "At first I'm not sure what Lichelle means, but a moment of following her gaze snaps me entirely into reality." 
    
    $chat.addmessage(beav,"not lookin forward to this")

    s "Here we are again..."

    ki "Cassandra's neck gleams pale and pretty, a vampire's dream." 
    
    $chat.addmessage(cake,"wha?")

    ki "Except for her scars." 
    
    $chat.addmessage(cake,"oh")

    ki "The pattern is odd. It's almost like perforation."

    k "What..."

    ki "As if she's been jabbed over and over with something sharp." 
    
    $chat.addmessage(elsa,"Who gave you this game Sophie?")

    show window



    ki "But she's weeping."
    ki "She's weeping so musically, somehow, and her eyes are unfocused and she's just so damn broken and I don't know how or why it happened but suddenly there are hot tears in my eyes."
    ki "Her body heaves. Nobody around her moves to help. She's sick."
    ki "Maybe she did this to herself, but where are the people who love her?"
    ki "Her people are here. Staring. One is on his phone playing a game."
    ki "Her fingers claw at nothing."
    ki "Why won't somebody help her?"

    hide window

    nvl clear
    
    $chat.addmessage(elsa,"Kylie :(")

    l 1m "Hey, hey. It's okay. It's okay."

    ki "Lichelle's fingers smooth my hair into even shocks. Even hazy as I am, I can't help but be aware of the power in her hands."

    ki "The weeping ends." 
    
    $chat.addmessage(bar,"it's sweet, but she probly does this all the time with bishes she KOs")

    ki "The sobbing, it... it ended. Cassandra's looking at me, her eyes full of apologies. Yearning, longing, pleading."

    ki "I can only stare back. There's a gulf of something between us. I can't breathe." 
    
    $chat.addmessage(elsa,"It's like the game's showing us what could have been")

    ki "Her eyes lift to Lichelle's, then lower to mine, pleading."

    ki "I want to ask. I want to ask about the scars. I want to ask about her voice. I want..."

    pause 1.0

    ki "I want this silence to end." 
    
    $chat.addmessage(fizz,"back")

    ki "Cassandra drags herself to a sitting position and claps the choker back around her neck. The movement is practiced and swift, and it yanks me out of my mesmerized state."

    show c 1g at f12

    c "< I guess you have questions. >" 
    
    $chat.addmessage(fon,"Welcome back sweet boy :)")

    ki "Gently, Lichelle helps me sit up as well. The room pirouettes around me, but her grip on my shoulders holds me in place."

    k "My hero's puking into a trash can." 

    show c 1b
    
    $chat.addmessage(elsa,"Sweet boy, eh.")

    k "And she smells like a horror movie."

    ki "Cassandra's typing, but I'm having none of it." 
    
    $chat.addmessage(fizz,"Both of you hush. Not here for you.")

    k "Who did that to your neck? What happened to you?"

    ki "She stops typing." 
    
    $chat.addmessage(fon,"You were here for me a minute ago.")

    pause 0.5


    c 1d "N-no body. I did it to myself." 

    show l 1g
    
    $chat.addmessage(cake,"damn boi")

    s "Wait! No she didn't. She did not!"

    ki "Her voice flows painfully, strained, as if something still squeezes her around the throat." 
    
    $chat.addmessage(elsa,"Sophie I don't think you should go any further.")

    c 2c "< Go back. Kylie. I'm sorry. This is stupid. I'm stupid. It's always like this. >"

    show c 2f at d12

    ki "And just like that, she's doubled over again, pouring out her agony into the trash can." 
    
    $chat.addmessage(fon,"Don't underestimate Sophie. :)")

    l 1k "Wow."

    k "Cassandra... dammit, you're not supposed to be like this." 
    
    $chat.addmessage(elsa,"I'm not, I just... Fontaine, she's been through some things and I think this is bad for her.")

    l 1g "I'll get her set up with a fluid IV. She'll be fine. I use them all the time to rehydrate after a weight cut."

    k "That's real?" 
    
    $chat.addmessage(fon,"You care so much, Elsa")

    l 1m "Yup. C'mon babe. I think Cass has been on TV enough today."

    ki "I hate to leave her this way. I guess, at the end of the day, we sleep in our own beds." 
    
    $chat.addmessage(elsa,"Shush.")

    ki "Still, this feels wrong. Dates don't end this way. Right?"

    menu:
        "Hold out my hand":
            ki "Silently, I offer her my hand. I don't know what she'll think, but-"

            show c 2c at f12

            c "..."

            ki "Just like that, her hand nestles into mine, warm to the touch and so very, very soft. Trembling."

            show l 1b at fl22

            ki "Without a word, Lichelle kneels on the other side of her and gathers Cassandra's hair away from her face."

            ki "The camera crew encircles us as Cassandra sobs."
            ki "It probably makes for great trash TV."

            $loveCass += 1

        "Say goodnight":
            k "Goodnight Cassandra."

            ki "The camera crew descends upon her as Lichelle and I make our way to the doors."

            ki "Her sobs crackle with fluid and coughs, but I can't allow myself to care."

            ki "Not yet. Maybe not at all."

            $renpy.notify("You can still save her")

    ki "I wonder, briefly, whether Tania will be pleased or mortified by all this." 
    
    $chat.addmessage(fon,"No, I mean it. You really care.")

    scene bg black with fade

    ki "Lichelle is silent during the ride home. She plays idly with her necklace, gazing out the window."

    ki "On the way to the bar, I got the feeling Lichelle was trying to send signals to me. Small ones. Quick glances." 
    
    $chat.addmessage(cake,"Pretty obvious.")

    ki "Now, it feels like she's in a bubble."

    ki "I can't help but wonder if the night went the way she wanted." 
    
    $chat.addmessage(bar,"Yeah Elsa, are you her family or sumthin?")

    pause 0.2

    k "... you clonked me, Elle."

    show l 1b at f12

    ki "Lichelle's fingertips glide along the surface of the cross." 
    
    $chat.addmessage(elsa,"No. I don't want to talk about it.") 
    
    $chat.addmessage(fon,"I won't ask any more. I'm just so impressed with you, Elsa.")

    l "I did, babe."

    k "I should probably go to a hospital." 
    
    $chat.addmessage(beav,"I Like the idea that Elle sabotaged Cass by crackin' Kylie with a bin")

    l 1g "Probably."

    pause 0.5

    k "Did you mean to?"

    l 1q "Clonk you?" 
    
    $chat.addmessage(beav,"Toldja")

    k "Mm-hm."

    l "Dunno." 
    
    $chat.addmessage(fon,"I think Lichelle meant to do it ;)")

    k "Why would you do that?"

    l 1o "Do you think I did it on purpose?"

    show l 1s

    menu:
        ki "I don't know what to say..."
        "I think you wanted to hurt me":
            k "I do."
            pause 0.2
            l "Why?"
            ki "She's looking sidelong at me. The cross gleams."
            k "I just get that feeling."
            l 1b "Mm."
            pause 0.2
            l 2b "I didn't, you know."
            pause 0.2
            l "I only want to hurt you if you want me to, babe."
            k "Oh."
            ki "But she doesn't ask if I want her to hurt me."
            pause 0.5
            
        "No, I don't":
            k "I don't."
            pause 0.2
            l 1s "Why?"
            ki "She isn't looking at me. Her neckline illuminates and vanishes in the passing streetlight."
            k "I don't think you'd hurt me unless I asked you to."
            l "Mm."
            pause 0.5
            l 1u "You're right about that."
            ki "Even with a headache, my pulse quickens. She keeps fingering that cross."
            ki "It's driving me absolutely mad."
            pause 0.1
            ki "Look at me."
            pause 0.1
            k "Look at me!"
            pause 0.5
            l "I don't need to."
            k "Why not?"
            pause 0.1
            l 1p "I have to pretend Robin gets a fair shot."
            s "She's so confident. Maybe it's just because I'm such a submissive myself, guys, but damn, Lichelle."

    $getHistory(11) 
    
    show image splashBRB at alphaFade
    
    pause(0.5)
    $hideGui()
    scene bg story-8 with fade
    pause 2.0
    pause
    scene bg bar with fade
    pause(0.5)
    
    
    jump realWorld3

    # end cass date
