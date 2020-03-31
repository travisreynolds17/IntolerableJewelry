label cassDate2:

# Remember, Cassandra's theme is inability to communicate, a voice taken for someone else's purpose

    $sceneNum = 10
    scene bg story-3 with fade
    pause 2.0
    pause

    scene bg hallway with fade

    pause 0.5

    $showGui()

    #---------------------------------------------------------

    $renpy.notify("stringSever(firstName) but never sever god") 

    #---------------------------------------------------------

    s "So... okay. If you guys have cooled off, we'll get started again." 
    
    $chat.addmessage(fizz,"We're good. Sorry.") 
    
    $chat.addmessage(cake,"he straight")

    pause 0.4

    s "Good. Then let's move on." 
    
    $chat.addmessage(elsa,"Sophie, taking charge.")

    s "We're going back to the bar with Cassandra, then." 
    
    $chat.addmessage(beav,"getting turnt up")

    s "I wonder why we went to the bar at all the first time? Isn't like we did much there."

    ki "The car ride is ... exhausting. Lichelle sits next to me in the backseat, playing with the little silver cross dangling from her neck, perfectly silent." 
    
    $chat.addmessage(bar,"Freud having a field day with that")

    ki "Now and again she glances at me, her dark eyes filled with purpose."

    ki "Then, back to looking out the window, rubbing the cross between her finger and thumb." 
    
    $chat.addmessage(elsa,"I wonder what it'd be like to date a pro fighter.")

    ki "Streetlights glimmer to life outside, pouring slats of light over her features."

    ki "Now I know what it feels like to be hunted by an apex predator." 
    
    $chat.addmessage(crab,"you're hittin that missionary and then she's like fluckin' tap or I break your arm :D")

    scene bg bar with fade

    show l with fade

    l "Cassandra's coming in now. I better haul ass or she might think she's being sabotaged." 
    
    $chat.addmessage(beav,"thta's funny considering she's gonna be at robin's place spyin'")

    k "That's probably a good idea. I mean, considering the show and all."

    ki "She doesn't answer that, but the hint of smile on her face tells me all she wants to convey." 
    
    $chat.addmessage(elsa,"Cassandra said she wasn't actually there, right? Just had it figured.")

    ki "If it weren't for the cameraman filming for b-roll, I think she might pounce on me." 
    
    $chat.addmessage(beav,"oh right")

    s "She's sabotaging Cass no matter what though. I wouldn't want my date to have someone else on her mind."

    

    scene bg bar with fade

    ki "Breathe. Breathe."

    s "~ yawn ~ yeah, self. You can do it."

    ki "The establishment is an odd one. It's a bar, obviously, but there are regular tables and booths all around the floor. No one's eating anything, so my guess is this place is..." 
    
    $chat.addmessage(cake,"MEET-CUTE")

    ki "A hookup parlor?" 
    
    $chat.addmessage(cake,"aww man")

    show c with dissolve

    ki "She's here. This is real."

    c "..."

    ki "Cassandra's easy to spot. Part of that's because of the film crew moving around to accommodate her, but it's also because she has such a soft presence." 
    
    $chat.addmessage(liv,"My sweet siren :)")

    ki "It's a magnificent contrast to Lichelle's overwhelming power."

    k "Hi, um, Cassandra! Um, how, um... okay."

    ki "She's smiling. I didn't see that yesterday. Meanwhile, she produces a cellphone from her pocket and shows the screen to me; there's a note app with several entries. Looks like she came prepared." 
    
    $chat.addmessage(cake,"need to watch for things that changed this time")

    c "< I'm happy to see you, Kylie. I was a little worried you might have a change of heart. I know my silence earlier must have been strange for you. >"

    ki "I wonder if the way she writes mimics the way she would have spoken." 
    
    $chat.addmessage(elsa,"I'm afraid I'll miss a change because I don't remember what she said the first time")

    k "No, no, it's fine! Tania told me a little about how we could communicate and it actually sounds kind of fun, and, uh... yeah."

    c "< So let's get fucking thrashed, how about it? >" 
    
    $chat.addmessage(elsa,"Well, nevermind then")

    ki "I guess the benefit of having to read her words is I have time to consider them." 
    
    $chat.addmessage(bar,"Cass truly beastin this time")

    ki "The downside is I'm not sure if she's joking."

    k "You're kidding, right?" 
    
    $chat.addmessage(liv,":(")

    c "< Not at all. I wanna show you what a rock star life is really like. >"

    menu:

        s "I don't want Kylie to drink. If I get drunk here, it'll be all over TV, right? Still..."


        "Have a drink":
            k "All right Cassandra, you're on. Order for both of us and impress me!"

            c "< That's what I wanted to hear! >"


        "Just juice":
            k "I wouldn't mind some cranberry juice."

            c " < Pity about that because I ordered like seventeen shots way ahead. >"

            s "So I have to drink? The game isn't giving me a..."

            s "... fine."

    # end choice 
    
    
    $chat.addmessage(crab,"Did you notice the chat never works when it's decision time.")

    ki "The camera crew keeps its distance, far enough that I could probably forget about them after a few days of this." 
    
    $chat.addmessage(elsa,"Kylie's gonna end up drunk and make a bad decision isn't she :(")

    ki "Problem is, this is day one and I feel like a drama student who can't quite get her lines out."

    s "~yawn~ Sorry guys, sorry." 
    
    $chat.addmessage(fizz,"you okay Sophie?")

    c "< It's a strange situation we're in. I want to tell you up front that I am serious about this. >"

    ki "I believe her, and still, I'm not sure how to interpret the message."

    s "Yeah Fizz, I'm just tired." 
    
    $chat.addmessage(beav,"You've had a few drinks too, right?")

    k "I guess this is the part where we tell each other about, uh, each other?"

    ki "God, I'm an idiot."

    s "Me, too. Yeah, Beaver, I had a few. Just to calm down."

    c "< Hey, this is why we're getting stupid in a sec. >"

    pause 1.0 
    
    $chat.addmessage(bar,"don't forget to hydrate")

    k "Okay. So, uh, Cassandra. How'd you end up on the show?"

    ki "Nicely done, self, a fully formed question!" 

    c "< Mmm I dunno. I'm bored. There's no inspiration left in my life. >" 
    
    $chat.addmessage(unkn,"what is my function") 
    
    $chat.addmessage(crab,"she different isn't she")

    c "< I figure if I do this I'll have a new batch of experiences. Maybe find my voice again. >"

    ki "Is that... wait, is she talking about her --" 
    
    $chat.addmessage(bar,"If things are different, I wonder if her scars are different, too.")

    ki "Her smile broadens. It's going to be hard to tell when she's joking, isn't it?"

    ki "I chuckle, but I don't know if it's appropriate." 
    
    $chat.addmessage(elsa,"Maybe Kylie just remembers things differently this time.")

    c "< It was a joke. >" 
    
    $chat.addmessage(beav,"What do you suppose this game is about?")

    k "I, uh, I knew that!"

    c "< The songs used to be personal. Wild. Angry, even. Now I'm wealthy, comfortable. What do I have to be so pissed about? > " 
    
    $chat.addmessage(liv,"Everything :) You'll see, trust me ;)")

    c "< It all feels mechanical now. >"

    ki "I suppose this is as good a time as ever to tell her that I..." 
    
    $chat.addmessage(cake,"fangirl reveal")
    
    k "I love your new stuff though."

    ki "Her expression changes, then, as she accepts this new piece of information. I'm not sure if she hoped I'd be a fan, or hoped for the opposite."

    c "< You're not a fangirl, are you? >"

    k "No, no, maybe? I love your work. Intolerable Jewelry got me through the worst break-up of my life!" 
    
    python:
        newComments = [
            [beav,"ROLL CREDITS I did it"],
            [bar,"Kylie said that twice."],
            [elsa,"Yes, I thought it'd be a different song."],
            [crab,"Roll... fluckit, roll credits!"]
        ]
    
        $chat.bulkMessage(newComments,"random")

    s "Breakups are the worst." 

    pause 1.0

    # show sophie crying

    
    
    $chat.addmessage(elsa,"Sophie?")

    s "..." 
    
    $chat.addmessage(fizz,"Sophie...") 
    
    $chat.addmessage(crab,"hey what's wrong?")

    s "I'm sorry guys."

    show image splashBRB at alphaFade

    pause 0.8 
    
    python:
        newComments = [
            [cake,"what's wrong?"],
            [beav,"god, that's the saddest sound I ever heard"],
            [bar,"Girl you okay?"],
            [liv,"Sophie!!"]
        ]
    
        $chat.bulkMessage(newComments,"random")

    pause(0.5)
    $hideGui()
    scene bg story-4 with fade
    pause(2.0)pause
    scene bg bar with fade
    pause(0.5)
    $showGui()
    pause(0.5)

    ki "Her smile falters a little bit. She's typing feverishly, and I wonder whether I've found a way to ruin everything already."

    c "< See, do you know that what song's about? >"

    k "It's about having like a really attractive ex who you keep wanting because they're so beautiful but you can't stand them, right?"

    ki "She smiles, darkly."

    c "< You would think. It's about my hood ornament. >"

    s "Her what?"

    ki "Your what?"

    k "Seriously?"

    c "< Yes, seriously. Not the one on my car, though.>"

    s "Seriously!"

    ki "Cassandra leans back in her chair, her hands falling to the tabletop. She breathes out, chuckles a mute chuckle."

    c "< I have a piercing. Down there, you know. >"

    s "Oh."

    k "Oh. Wait, really?"

    ki "She nods, slowly."

    k "So the song that got me over Taylor was..."

    ki "Another nod."

    c "< About my clitoral piercing. >"

    c "< Disappointing, huh? >"

    k "... no."

    k "No, I'm glad! I mean, maybe you didn't mean it the way I interpreted it, but that happens all the time in real relationships!"

    show c listen

    k "So it's still meaningful to me."

    show c happy

    c "<I'm really happy to know you're a fan. Might not seem that way, but I like the way you think.>"

    c "< And I like the way you look, too. I made a good choice coming here. >"

    k "I don't want to be a bothersome fangirl. I mean, I am, but not like, you know? Like that."
    
    c "< You're handling it well. >"

    k "On the outside. Inside, I'm screaming like a banshee on fire."

    show c flirty

    ki "I don't want to put her on guard, and it seems to be working. Her finger traces the edge of her phone, lightly, meaningfully."

    ki "The drinks arrive, and for a moment the interruption of a server derails our conversation."

    ki "She wasn't kidding, either. The platter hosts no less than twelve shot glasses filled with god-knows-what."

    ki "I find myself wringing my hands lightly together. This is so much harder than it looked on TV. Magic of editing, I guess."

    pause 0.5
    show c listen
    pause 1.0

    c "< So Kylie. Gun to your head, who would you sleep with first, me or Robin? > "

    k "Wow."

    ki "Cassandra pounds a shot. Then another. And another."

    c "< Too fast? Drink up! >"

    c "< I know you like my work. And I guess you wouldn't be on the show otherwise, but... you like girls, right? >"

    ki "The question strikes me as fully appropriate and adorably obvious."

    k "I..."

    ki "I guess someone should have asked this question already. It dawns on me, just now, that nobody ever asked me flat out if I... huh."

    c "< Well, I do. And I think you'd pick me.>" 

    s "Guys, what do you think? I'm not sure I like Cassandra this time. She's... entitled, I guess."

    ki "Her smile was tempting from the moment it poured across her lips. Now, it's downright mesmerizing."

    k "I do, too."

    s "Oh. Well, nevermind what I want then."

    c "< I always thought this show was fake. Really, I did. How's a person supposed to fall in love in two dates? >"

    k "I don't know."

    ki "It's easy for me. I know who she is, I've idolized her, even. To her, though, I'm just another face."

    ki "Cassandra slams another shot, easily, in a practiced way."

    c "< C'mon, drink up. If you think I'm attractive now, just wait 'til shot nine. >"

    ki "Fine, then. I drain the first glass and immediately cough and sputter."

    k "Good god, what is this?"

    c "< Straight-up Russian vodka. One of my girlfriends was from Marilinsk and turned me on to it. >"

    c "< She was stone cold, Kylie. Two things Russia makes best are vodka and badasses. >"

    ki "I take another shot. It's easier than the first."

    k "Was?"

    ki "Two more shots for Cassandra. How is she alive, at all?"

    s "I would be on the floor. Vodka kicks my butt, people."

    c "< She died. >"

    s "Oh. Shit."

    ki "The warmth blooming in my belly freezes at that. Have I stepped on a land mine, so quickly?"

    k "I'm sorry..."

    c "< Yeah. I guess she couldn't handle us not being a thing. >"

    c "< She was great, but I just wanted to have fun. I'm not marrying some dime piece from who-gives-a-shit Russia. >"

    k "What happened?"

    s "Why would you ask that, Kylie?"

    c "< Hung herself. I found her the next day. She left a note on the floor under her. Blamed me. >"

    ki "Another shot, two, three. Cassandra's deep into my side of the platter, now."

    k "Oh my god."

    s "..."

    pause 1.0

    s "Guys, I need a break. Just a minute."

    #chat - brb

    s "Sorry. That just got a little too real for me."

    s "Anyway. Sorry. Let's keep going."

    ki "She waves the sentiment away."

    c "< It's cool. She did what she had to do. Respect. >"

    s "Oh my god, she's so different this time. Was she like this before? I mean, was this her story before?"

    s "She must be in so much pain and just medicating it with booze. She has to be."

    k "It doesn't bother you at all?"

    c "< Hey. Listen. I wrote a song about it. Let's go to my studio and fuckin' jam it. For Marina."

    show c heartbroken

    ki "And there it is. The well of feeling she's been holding back for god knows how long breaks apart."

    c "< This is going as bad as anything could possibly go. >"

    k "No, it's okay! God, Cassandra, that's horrible."

    ki "She reaches for another shot, but I pull the platter away."

    k "Stop! That's not going to help."

    c "..."

    k "Please don't be mad. I think you need to talk about this with someone like... professional."

    ki "She nods, tears pouring down her cheeks."

    k "Let's get a cab and get out of here."

    c "< To my studio. >"

    k "I'm struggling between my inner fangirl and my concerned adult human right now."

    c "< I appreciate it, too. >"

    c "< Never meet your heroes, right? I'm sorry I'm disappointing you.>"

    k "Oh trust me, you, and, uh... I mean... sorry, I'm a little tongue tied."

    c "< I can help with that. >"

    ki "A cool thrill shoots along my skin. Easy, Kylie, she could mean just about anything by that."

    s "But you're drunk, Cassandra. And hurting. There's just no way I'm picking you right now."

    s "Or is that the worst thing I could possibly do?"

    c "< Don't worry. There's a bed at the studio, and bathroom. In case all the shots were too many.>"

    ki "I'm mostly impressed with how well she types despite swaying all over the place."

    scene bg studio with fade

    s "I sincerely hope they had a driver."
    
    ki "The studio is almost exactly what I would have expected. There's a drum kit, tons of wires and blinking lights that I guess are part of editing equipment."

    ki "I'm no expert on music production, and I'm no expert on the odd foam mat and beer smell that permeates the walls and floor."

    c "< Sorry about the mess. TBH I wasn't sure if I'd ask you to come here. >"

    k "Oh? I kind of thought this was part of the plan from the start."

    c "< I wanted to know if you were just in this for the sex. >"

    k "Oh. Um. You're welcome?"

    ki "I can't help but notice how Cassandra walks as she leads me into the studio. I noticed at the bar, too, but she sort of flows from one long, considerate gaze to another."

    ki "Her expression loses focus sometimes. It could be just because she's toasted, but I wonder, guiltily, if she's somewhere on the autism spectrum."

    ki "Then I remember I don't know enough about it to decide one way or another."

    k "So, uh, Cassandra?"

    c "... ?"

    k "Which one do you play?"

    ki "She points to a beautifully finished seven-string guitar hanging from a mount on the wall. It has a marbled pattern, swirling in royal blue and aquamarine."


    pause 0.5

    ki "She points, emphatically, to her phone screen."

    c "< I sing, too. >"

    k "But you can't talk? I thought for sure you had a singer?"

    ki "Her smile sours, just a bit."

    c "< Don't say it out loud. >"

    c "< I sing on all the albums, just not live. Marina used to sing for me on stage. >"

    k "Oh."

    s "Oh god."

    c "< As far as the world knows, I'm just a guitar player and songwriter. >"


    ki "This all feels so rushed. I've adored her music without even knowing what kind of person she might be. There's a camera crew around us, even in this small space."

    ki "What if I talk? She's probably pretty powerful if she's a Quillboard top 10 artist, right? Suddenly I find myself cold, nervous."

    ki "Or is that excitement?"

    k "Why would you trust me with a secret, though? We really only just met?"

    c "< I don't have time to earn your trust, so I have to buy it. >"

    s "... huh."

    s "That feels so much more empty than last time."

    k "I promise, then."

    ki "Cassandra's features focus. I thought she would smile, but..."

    c "< Okay. Come with me into the recording booth? >"

    ki "As Cassandra moves to the booth, snagging a water bottle on the way, one of the camera crew picks up behind her. Only then does it occur to me that we're going to be on TV--"

    c "!!!"

    ki "-- but she wheels around then, a horrified expression on her face, and crumples to her knees."

    ki "... and promptly begins to heave."

    ki "The cameraman nearest her pauses, looks to Lichelle as if asking what to do next. She's been so quiet I forgot she was with us."

    ki "Lichelle, hanging back by the entrance, snatches up a trash can."

    l "Kylie, here!"

    ki "I turn my head just in time to see the bin come flying at my face and-"

    #klonk sound

    scene bg studio with fade

    #woozy transition

    s "This date has gone off the rails, guys."

    #wooze

    ki "It's odd, what one notices when one has been clocked with a bin chucked by a professional MMA fighter."

    ki "For example, I find myself busily studying a scratch mark in the wood flooring, wondering what on earth could have caused such a small, consistent fissure."

    ki "And everyone around me sounds like they're underwater."

    ki "And there's something soft and warm under my head."

    l "Hey hey hey, welcome back."

    show l happy

    l "I am so, so sorry for that! I really thought you had it, babe."

    ki "I find myself turning to lay flat, which probably is a bad idea, and realize that warm softness is Lichelle's lap."

    k "Clearly."

    s "Should she have put my head there? I mean I'm probably concussed. Might not want to move my neck."

    

    show l flirty

    l "You're okay, trust me. I've been KO'd more times than I can remember."

    k "I don't think that's a good thing."

    l "You're doing better than her."

    ki "She nods toward Cassandra, lying on her side and groaning with the upright trash can next to her."

    ki "I feel like I should say something, but nothing comes to mind."

    ki "Cassandra looks so defeated, lying there helpless and fully out of control."

    ki "Her choker lies next to her on the floor, gleaming elegantly, as if to contrast her."

    l "I guess her secret's out."

    ki "At first I'm not sure what Lichelle means, but a moment of following her gaze snaps me entirely into reality."

    s "Here we are again, guys..."

    ki "Cassandra's neck gleams pale and pretty, a vampire's dream."

    ki "Except for her scars."

    ki "The coarse, leathery trail snakes unevenly around her neck, roughly to the base of her skull. There are larger patches here and there, almost like... like, I don't know what."

    k "What..."

    ki "But she's weeping. She's weeping so musically, somehow, and her eyes are unfocused and she's just so damn different broken and I don't know how or why it happened but suddenly there are tears in my eyes and I don't know if it's her cries or the ligature marks on her neck or--"

    l "Hey, hey. It's okay. It's okay."

    ki "Lichelle's fingers smooth my hair into even shocks. Even hazy as I am, I can't help but be aware of the power in her hands."

    ki "The weeping ends."

    ki "The sobbing, it... it ended. She's looking at me, her eyes full of apologies. Yearning, longing, pleading."

    ki "I can only stare back. There's a gulf of something between us. I can't breathe."

    ki "Her eyes lift to Lichelle's, then lower to mine, pleading."

    ki "I want to ask. I want to ask about the scars. I want to ask about her voice. I want..."

    pause 1.0

    ki "I want this silence to end."

    ki "Cassandra drags herself to a sitting position and claps the choker back around her neck. The movement is practiced and swift, and it yanks me out of my mesmerized state."

    c "< I guess you have questions. >"

    ki "Gently, Lichelle helps me sit up as well. The room pirouettes around me, but her grip on my shoulders holds me in place."

    k "I just got dropped by a trash can and my hero is puking in a trash can six feet away."

    k "And she smells like a horror movie."

    ki "Cassandra's typing, but I'm having none of it."

    k "Who did that to your neck? What happened to you?"

    ki "She stops typing."

    c "N-no body. I did it to myself."

    s "Wait! No she didn't. She did not!"

    ki "Her voice flows painfully, strained, as if something still squeezes her around the throat."

    c "< Go back. Kylie. I'm sorry. This is stupid. I'm stupid. It's always like this. >"

    ki "And just like that, she's doubled over again, pouring out her agony into the trash can."

    l "Wow."

    k "Cassandra... dammit, you're not supposed to be like this."

    l "I'll get her set up with a fluid IV. She'll be fine. I use them all the time to rehydrate after a weight cut."

    k "That's real?"

    l "Yup. C'mon babe. I think Cass has been on TV enough today."

    ki "I hate to leave her this way. I guess, at the end of the day, we sleep in our own beds."


    ki "Still, this feels wrong. Dates don't end this way. Right?"

    menu: 
        "Hold out my hand":
            ki "Silently, I offer her my hand. I don't know what she'll think, but-"

            c "..."

            ki "Just like that, her hand nestles into mine, warm to the touch and so very, very soft. Trembling."

            ki "Without a word, Lichelle kneels on the other side of her and gathers Cassandra's hair away from her face."

            ki "The camera crew encircles us as Cassandra sobs."
            ki "It probably makes for great trash TV."
            

            $loveCass +=1

        "Say goodnight":
            k "Goodnight Cassandra."

            ki "The camera crew descends upon her as Lichelle and I make our way to the doors."

            ki "Her sobs crackle with fluid and coughs, but I can't allow myself to care."

            ki "Not yet. Maybe not at all."

            $loveCass -=1

    ki "I wonder, briefly, whether Tania will be pleased or mortified by all this."

    scene bg black with fade

    ki "Lichelle is silent during the ride home. She plays idly with her necklace, gazing out the window."

    ki "On the way to the bar, I got the feeling Lichelle was trying to send signals to me. Small ones. Quick glances."

    ki "Now, it feels like she's in a bubble."

    ki "I can't help but wonder if the night went the way she wanted."

    k "... you clonked me."

    ki "Lichelle fingertips glide along the surface of the cross."

    l "I did, babe."

    k "I should probably go to a hospital."

    l "Probably."

    pause 0.5

    k "Did you mean to?"

    l "Clonk you?"

    k "Mm-hm."

    l "Dunno."

    k "Why would you do that?"

    l "Do you think I did it on purpose?"

    menu:
        s "I'm not sure guys."
        "Yes":
            k "I do."
            pause 0.2
            l "Why?"
            ki "She's looking sidelong at me. The cross gleams."
            k "I just get that feeling."
            l "Mm."
            pause 0.2
            l "I didn't, you know."
            pause 0.2
            l "I only want to hurt you if you want me to, babe."
            k "Oh."
            ki "But she doesn't ask if I want her to hurt me."
            pause 0.5
            s "Wow. Maybe I'm just susceptible to stuff like this, but wow."
        "No":
            k "I don't."
            pause 0.2
            l "Why?"
            ki "She isn't looking at me. Her neckline illuminates and vanishes in the passing streetlight."
            k "I don't think you'd hurt me unless I asked you to."
            l "Mm."
            pause 0.5
            l "You're right about that."
            ki "Even with a headache, my pulse quickens. She keeps fingering that cross."
            ki "It's driving me absolutely mad."
            ki "Look at me."
            k "Look at me!"
            pause 0.5
            l "I don't need to."
            k "Why not?"
            pause 0.1
            l "I have to pretend Robin gets a fair shot."
            s "She's so confident. Maybe it's just because I'm such a submissive myself, guys, but damn, Lichelle."

        


    jump robinDate2

    #end cass date