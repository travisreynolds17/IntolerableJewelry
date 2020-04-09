label cassDate1:

    # Remember, Cassandra's theme is inability to communicate, a voice taken for someone else's purpose

    # loading screen function

    scene bg load-function with fade

    pause 4.0

    scene bg bar with longFade

    # show
    $showGui()

    s "Oh, hey, we're getting trashed before the date! Always drink responsibly, kids."

    $chat.addmessage(elsa, "A bar's kind of blah as a first date.")

    $chat.addmessage(fizz, "So are we like living on this set? Seems like that shoulda come up.")

    $chat.addmessage(cake, "gunna be 10 percent hotter now")

    ki "It's pretty obvious she's more than just the host. In fact, it looks like the crew is a lot smaller than I would have imagined. I guess they're just that efficient."

    t "Alright Kylie. Cassandra's just arrived. You okay?"

    $chat.addmessage(liv, "I hope you love Cassandra as much as I do")

    k "I might as well be."

    t "Great. Good luck, okay? Cassandra's a great girl, I think you'll get along well."

    $chat.addmessage(cake, "Liv did you kidnap Bong")

    scene bg bar with fade

    ki "Breathe. Breathe."

    $chat.addmessage(elsa, "This place looks like somewhere I went for my 21st birthday")

    $chat.addmessage(shub, "lol@alcohjolism")

    s "Breathe, self! You can do this!"

    ki "The establishment is an odd one. It's a bar, obviously, but there are regular tables and booths all around the floor. No one's eating anything, so my guess is this place is..."

    ki "I guess a meet-cute parlor?"

    $chat.addmessage(cake, "whats a meet cute")

    show c with dissolve

    ki "She's here. This is real."

    $chat.addmessage(elsa, "It's like an adorable first date in a rom com")

    c "..."

    $chat.addmessage(crab, "in other words, some ol' bullshit")

    ki "Cassandra's easy to spot. Part of that's because of the film crew moving around to accommodate her, but it's also because she has such a soft presence."

    k "Hi, um, Cassandra! Um, how, um... okay."

    $chat.addmessage(bar, "so eloqent")
    pause 0.1
    $chat.addmessage(bar, "*eloquent")

    ki "She's smiling. I didn't see that yesterday. Meanwhile, she produces a cellphone from her pocket and shows the screen to me; there's a note app with several entries. Looks like she came prepared."

    $chat.addmessage(egg, "i had laryngitis once and had to do that")

    c "<I'm happy to see you, Kylie. I was a little worried you might have a change of heart. I know my silence earlier must have been strange for you.>"

    $chat.addmessage(elsa, "Breaking my heart!")

    ki "I wonder if the way she writes mimics the way she would have spoken."

    $chat.addmessage(unkn, "R/BG13:14-15")

    k "No, no, it's fine! Tania told me a little about how we could communicate and it actually sounds kind of fun, and, uh... yeah."

    c "< Can I get you a drink? Am nervous too, so def getting one. >"

    $chat.addmessage(bar, "ill have a manhattan")

    ki "There's a difference in her prepared text and what she types on the fly. It must be exhausting to type out everything she has to say."

    pause 0.7

    c "< By the way... >"

    if outfitCurrent == "Dress":
        c "< You're braver than me to come out in a dress so revealing. >"
        s "Oh, crap."
        k "... oh."
        ki "Cassandra's eyes widen a little bit. She waves a hand, frantically."
        c "< No it's cute. I just mean you must be confident. >"
        ki "... well, I WAS confident anyway."
        s "We screwed up, guys. Maybe?"

    if outfitCurrent == "Jeans":
        c "< A teddy bear shirt, eh? >"
        s "Dangit. I think we might've messed up."
        k "Yeah... they  only gave me a few options."
        c "< I love it. >"
        k "What?"
        s "What?"
        c "< What can I say? I'm a rock star, but I like cute things. That shirt is cute and you're cute in it.>"
        pause 0.5
        k "... thank you!"

    if outfitCurrent == "Pantsuit":
        c "< Nice suit. >"
        s "Yeah, in hindsight, seems like a bad choice for a rock star."
        k "You don't like it."
        c "< I just feel under dressed compared to you. >"
        ki "... should've seen that one coming."

    menu:

        s "Whaddaya say, chat? Like if it were me, I'd want to be sober for sure, but..."

        "Have a drink":
            k "I'll have a --"

            ki "You know, I shouldn't be drinking. Not now. Not when there are two other people to meet."

            k "I'd just like some cranberry juice if that's okay."

            $chat.addmessage(shub, "Pssh")
            $chat.addmessage(cake, "weakesauce")

            s "Oh, come on! If you're gonna give me the choice, why shouldn't my choice matter?"

            $chat.addmessage(shub, "maybe it's like a life reclection")

            s "I mean... really!"

        "Just juice":
            k "I wouldn't mind some cranberry juice."

            c "..."

            $chat.addmessage(egg, "oof, DISAPPOINTED")

            ki "Her smile exists in a way that barely makes sense to me. I wonder if I let her down just now."

    # end choice

    ki "There's a tablet mounted to the table, and Cassandra swipes at it a few times to place our drink orders. I don't see any food on the menu, so I suppose my earlier observation was accurate."

    $chat.addmessage(fizz, "Sophie, what's your favorite drink?")

    ki "The camera crew keeps its distance, far enough that I could probably forget about them after a few days of this."

    $chat.addmessage(elsa, "Yeah, Sophie! I like cosmos myself")
    $chat.addmessage(shub, "sex on the beach, not a meme, for real")

    ki "Problem is, this is day one and I feel like a drama student who can't quite get her lines out."

    s "I'd be nervous if it were me. Cassandra's a star, after all."

    s "Oh, um, guys I would say my favorite drink is a negroni. Gin and vermouth, it's mature I guess."

    c "< It's a strange situation we're in. I want to tell you up front that I am serious about this. >"

    $chat.addmessage(elsa, "mmm classy")

    ki "I believe her, and still, I'm not sure how to interpret the message."

    k "I guess this is the part where we tell each other about, uh, each other?"

    $chat.addmessage(egg, " This is where I would fumble lol")

    ki "God, I'm an idiot."

    s "God, I'm adorable."

    $chat.addmessage(fizz, "You're both right")

    c "< It would have been easier if we were both drunk already. >"

    k "Maybe."

    pause 1.0

    k "Okay. So, uh, Cassandra. How'd you end up on the show?"

    $chat.addmessage(cake, "she's in the script lol")

    ki "Nicely done, self, a fully formed question!"

    $chat.addmessage(crab, "lol")

    c "< I am looking for inspiration. I guess I lost my voice somewhere along the way. >"

    ki "Is that... wait, is she talking about her --"

    $chat.addmessage(egg, "Metaphor")

    ki "Her smile broadens. It's going to be hard to tell when she's joking, isn't it?"

    s "My question is, how does the TV show know what she's saying?"

    $chat.addmessage(bar, "RIGHT?")

    ki "I chuckle, but I don't know if it's appropriate."

    c "< It was a joke. >"

    k "I, uh, I knew that!"

    $chat.addmessage(elsa, "Kylie's a ditz, isn't she")

    c "< My songs just aren't the same anymore, Kylie. I thought going on this show and meeting someone new in this weird pressure cooker of an environment might draw something out of me.> "

    ki "I suppose this is as good a time as ever to tell her that I..."

    $chat.addmessage(egg, "Don't like girls")

    k "I love your new stuff though."

    $chat.addmessage(fizz, "Huh. We've just been assuming Kylie likes women, though. What if she's faking?")

    ki "Her expression changes, then, as she accepts this new piece of information. I'm not sure if she hoped I'd be a fan, or hoped for the opposite."

    c "< So you know my work? >"

    k "I love your work. Intolerable Jewelry got me through the worst break-up of my life!"

    python:
        newComments = [
            [crab, "name drop"],
            [fizz, "Had to say the title at some point"],
            [elsa, "We did it guys!"],
            [shub, "ROLL CREDITS"],
            [cake, "that title is dumb"],
            [liv, "I love the album tho"],
            [bar, "liv you way too into this"],
            [beav, "roll cred-- shit"]

        ]
    $chat.bulkMessage(newComments, 0.6)

    s "So wait, if I'm a super fan doesn't that mean I should choose Cassandra? That doesn't seem fair to the others."

    $chat.addmessage(egg, "You would think")

    ki "Her smile falters a little bit. She's typing feverishly, and I wonder whether I've found a way to ruin everything already."

    $chat.addmessage(elsa, "God, maybe she really needed to meet someone who didn't know her.")

    c "< Writing it did the same for me. >"

    show c happy

    c "<I'm really happy to know you're a fan. I'm also really happy you're not asking for an autograph.>"

    $chat.addmessage(elsa, "There you go")

    $chat.addmessage(egg, "Yeah you right")

    ki "The thought had crossed my mind."

    k "I don't want to be a bothersome fangirl. I mean, I am, but not like, you know? Like that."

    $chat.addmessage(fizz, "I am a fan of yours, Sophie")

    c "< You're handling it well. >"

    $chat.addmessage(cake, "OBVIOUSLY")

    k "On the outside. Inside, I'm screaming like a teenager at one of your shows."

    show c flirty

    ki "I don't want to put her on guard, and it seems to be working. Her finger traces the edge of her phone, lightly, meaningfully."

    ki "The drinks arrive, and for a moment the interruption of a server derails our conversation. Cassandra downs a shot of tequila and makes a face, leaving two more shots on the table."

    $chat.addmessage(shub, "Cass BEASt yo")

    ki "I find myself wringing my hands lightly together. This is so much harder than it looked on TV. Magic of editing, I guess."

    pause 0.5
    show c listen
    pause 1.0

    c "< I didn't think it would be this hard.> "

    $chat.addmessage(egg, "not a word, Crablegs")

    k "I was thinking the same thing."

    $chat.addmessage(crab, "aww")

    c "< So... I have a question. >"

    $chat.addmessage(fizz, "lol")

    c "< I know you like my work. And I guess you wouldn't be on the show otherwise, but... you like girls, right? >"

    ki "The question strikes me as fully appropriate and adorably obvious."

    $chat.addmessage(shub, "Actually a resonable flucking question.")

    k "I..."

    ki "I guess someone should have asked this question already. It dawns on me, just now, that nobody ever asked me flat out if I... huh."

    $chat.addmessage(crab, "I like girls, Elsa")

    c "< Well, I do. >"

    $chat.addmessage(elsa, "Sucks for them.")

    ki "Her smile was bashful from the moment it poured across her lips. Now, it's downright vulnerable."

    k "I do, too."

    $chat.addmessage(cake, "lol roasted crablegs")

    c "< I always thought this show was fake. Really, I did. How's a person supposed to fall in love in two dates? >"

    k "I don't know."

    $chat.addmessage(beav, "Falling in love in two dates is easy. Just date me twice.")

    ki "It's easy for me. I know who she is, I've idolized her, even. To her, though, I'm just another face."

    $chat.addmessage(beav, "I'm turnin women into waterslideds")

    $chat.addmessage(liv, "Yes, you do! You're so charming, AngeredBeaver69.")

    ki "Cassandra slams another shot, easily, in a practiced way."

    $chat.addmessage(shub, "dafuq")

    c "< I have an idea, though. >"

    $chat.addmessage(egg, "boobs")

    k "Oh?"

    $chat.addmessage(bar, "Is this where we R as a society")

    c "< I rented a little studio, not too far from here. Would you like to be on my next album? >"

    s "Oh, wow! Chat, we're gonna be rock stars! Also, you guys raise some valid points. It's definitely a good idea to find out if Kylie likes girls before asking her to date three or four of them."

    k "Wait what."

    c "..."

    $chat.addmessage(cake, "Kan we even sing?")

    k "Really?"

    $chat.addmessage(egg, "I can sing")

    ki "She nods, her smile returning."

    $chat.addmessage(elsa, "Really, egg? Baritone?")

    k "Oh my god, yes!"

    k "Oh, I, but I can't play anything."

    $chat.addmessage(cake, "falsetto lol")

    $chat.addmessage(egg, "yis baritone")

    c "< That's no problem. I can teach you. >"

    k "I'm trying my best not to go full fangirl right now, you know that, right?"

    $chat.addmessage(cake, "OBVIOUSLY")

    c "< I appreciate it, too. >"

    c "< I'm hoping I can get you to like me for more than my discography.>"

    $chat.addmessage(bar, "what's so obvious at that")

    k "Oh trust me, you, and, uh... I mean... sorry, I'm a little tongue tied."

    c "< I can help with that. >"

    $chat.addmessage(cake, "#hentai")

    $chat.addmessage(liv, ":(")

    s "Ooh, spicy."

    ki "A cool thrill shoots along my skin. Easy, Kylie, she could mean just about anything by that."

    $chat.addmessage(beav, "Could mean she wants t'smash th'ass")

    ki "Cassandra takes the last shot and throws it back like it was water. I'm kind of impressed."

    # FILL OUT LATER? MAYBE NOT> THEY LEAVE

    s "I'm pretty excited about this. You know what's weird though? Cassandra's supposed to be a rock star, right, but what does she do exactly?"

    $chat.addmessage(fizz, "Never said, though. I hope she's a drummer.")

    $chat.addmessage(shub, "no feckin way. she's gotta ply bass")

    s "If she's a badass guitar chick the game is over. Cassandra wins. What do you guys think?"

    # chat is blank
    $temporaryChat = chat.history
    $chat.history == []

    # screen effect - blank chat, then return chat

    $chatSelected = True
    show screen chatterbox

    python:
        newComments = [

        ]
        for i in "I have come to the conclusion that non-orgasmic coitus rewards genetic passivity":
            temp = [bong, i]
            newComments.append(temp)
        chat.bulkMessage(newComments, 0.025)
        temp = ""
        chat.delmessages()

    pause 1.0

    s "Huh. I think something went goofy on me. Hang on."

    pause 0.5

    $chat.history = temporaryChat

    $chat.addmessage(fizz, "She plays kazoo.")

    s "There we go. Everything's better, right?"

    $chat.addmessage(liv, "Everything is amazing ;)")

    s "There we are. Fizz thinks she's a pro kazoo player, right, right."

    $chat.addmessage(egg, "feuckin right")

    s "Tweeter, you wanted to drink, too? I getcha, I getcha."

    $chat.addmessage(beav, "drink from the lady fountain :D :D :D")

    s "Beaver. Oh my god."

    s "I'm betting she's like an electronica DJ. She just makes beats and spins records in a microwave, right?"

    $chat.addmessage(bar, "That would be the worst")

    scene bg studio with longFade

    $getHistory(1)

    ki "The studio is almost exactly what I would have expected. There's a drum kit, tons of wires and blinking lights that I guess are part of editing equipment."

    $chat.addmessage(unkn, "I am undone")
    $chat.addmessage(shub, "This looks like my studio")

    ki "I'm no expert on music production, and I'm no expert on the odd foam mat and beer smell that permeates the walls and floor."

    $chat.addmessage(cake, "BLUEGRASS BOIS")

    c "< Sorry about the mess. TBH I wasn't sure if I'd ask you to come here. >"

    $chat.addmessage(cake, "yeehaw")

    k "Oh? I kind of thought this was part of the plan from the start."

    $chat.addmessage(egg, "bluegrass is stupid, twangy toothless funk")

    $chat.addmessage(shub, "the hell you know")

    c "< I wanted to know if you were just in this for a minute of fame. >"

    $chat.addmessage(beav, "bluegrass is good sometimes")

    k "Oh. Um. You're welcome?"

    $chat.addmessage(elsa, "I like Wagon Spokes, it's a good song")

    ki "I can't help but notice how Cassandra walks as she leads me into the studio. I noticed at the bar, too, but she sort of flows from one long, considerate gaze to another."

    $chat.addmessage(egg, "I like bluegrass girls not bluebrass music :D")

    ki "Her expression loses focus sometimes. I wonder, guiltily, if she's somewhere on the autism spectrum."

    ki "Then I remember I don't know enough about it to decide one way or another."

    s "Wise Kylie!"

    $chat.addmessage(liv, "Oh, TweeterEgg, you want a date?")

    $chat.addmessage(egg, "maybe")

    k "So, uh, Cassandra?"

    c "... ?"

    $chat.addmessage(shub, "don't do it bro Bong never came back")

    k "Which one do you play?"

    $chat.addmessage(liv, "Oberbong went to sleep. :)")

    ki "She points to a beautifully finished seven-string guitar hanging from a mount on the wall. It has a marbled pattern, swirling in royal blue and aquamarine."

    $chat.addmessage(cake, "Why sleep. You drug him or something")

    s "Guitar girl! Robin and Lichelle better be badasses or this game's already over."

    pause 0.5

    $chat.addmessage(crab, "you guys have a lil' one on one")

    $chat.addmessage(liv, "Yes, we did. :)")

    ki "She then points toward the microphone behind a glass divider."

    s "Hey chat, I... wait, what. Liv. Hang on, what."

    $chat.addmessage(shub, "wait how?")

    python:
        newComments = [
            [elsa, "Oh god, comeo on"],
            [bar, "Really?"],
            [beav, "nice"],
            [unkn, "please"],
            [bar, "Like phone sex?"],
            [elsa, "sheesh"]

        ]
        chat.bulkMessage(newComments, 0.09)

    s "Whatcha mean, Liv? Don't get us kicked off Switch."

    $chat.addmessage(liv, "We had a lovely conversation. ;) ")

    python:
        newComments = [
            [elsa, "Oh. Okay."],
            [beav, "still could be boning?"],
            [egg, "Let's have a conversation"],
            [crab, "tease"],
            [shub, "Coulda been worse"]

        ]
        chat.bulkMessage(newComments, 0.09)

    s "Oh. I see. Hey Liv, I gotta ask you to calm down just a little with the innuendo. I wanna make sure we keep it clean enough to stay online, okay?"

    $chat.addmessage(liv, "As you wish, love :)")

    pause 1.0

    s "Cool. So Kylie was just offered a role in Cassandra's band! Somehow."

    $chat.addmessage(egg, "Ooh, private chat, brb")

#    $renpy.notify("soon")

    ki "Wait. What?"

    k "You sing?"

    $chat.addmessage(crab, "wait what")

    $chat.addmessage(fizz, "Have fun, Egg.")

    ki "She nods."

    k "But you can't talk? I thought for sure you had a singer?"

    $chat.addmessage(bar, "What's weird is we'd usually just assume the artist would be a frontman.")

    ki "Her smile sours, just a bit."

    $chat.addmessage(elsa, "Frontwoman.")

    c "< It seems wrong, doesn't it? It'll make sense in a second. I want to show you something. >"

    c "< But first, Kylie. Only a handful of people have seen what I'm about to show you.>"

    $chat.addmessage(bar, "Right, sorry.")

    c "< I need you to be quiet about what you see. Can you do that? >"

    s "Hold on, that's not fair! You can't ask someone to keep a secret they know nothing about."

    ki "This all feels so rushed. I've adored her music without even knowing what kind of person she might be. There's a camera crew around us, even in this small space."

    $chat.addmessage(fizz, "Secrecy is no good.")

    ki "What if I talk? She's probably pretty powerful if she's a Quillboard top 10 artist, right? Suddenly I find myself cold, nervous."

    $chat.addmessage(cake, "you never had a wife didja")

    ki "Or is that excitement?"

    k "Why would you trust me with a secret, though? We really only just met."

    c "< I don't have time not to trust you if I want you to like me. >"

    $chat.addmessage(elsa, "Oh, my heart")

    s "... huh."

    s "Wow, uh, that's... huh. Chat, how am I supposed to feel about that? It's pretty sad, isn't it?"

    $chat.addmessage(bar, "Just like that, to have to extend so much trust so fast")

    # chat

    s "Twixt, I fully agree. God, can you imagine having only two nights to win someone over?"

    $chat.addmessage(crab, "boobs lol B00Bs")

    s "Imagine feeling like you have to show someone your biggest secret just to keep from missing out on one chance."

    s "Oh my god, guys."

    $chat.addmessage(elsa, "Wow. Just wow.")

    k "I promise, then."

    ki "Cassandra's features focus. I thought she would smile, but..."

    $chat.addmessage(bar, "Good choice Kylie")

    c "< Okay. Come with me into the recording booth? >"

    ki "As Cassandra moves to the booth, snagging a water bottle on the way, one of the camera crew picks up behind her. Only then does it occur to me that we're going to be on TV--"

    $chat.addmessage(bong, "")

    c "!!!"

    ki "-- but she wheels around and shoots a fearsome glare at the crew, shaking her head violently."

    $chat.addmessage(fizz, "Jesus, that's a death look")

    ki "The cameraman nearest her pauses, looks to Tania as if asking what to do next. She'd been so quiet before I nearly forgot she was with us."

    $chat.addmessage(shub, "Boner killed")

    ki "Tania, hanging back by the entrance, whispers something into her lapel mic. The cameraman backs off."

    ki "She beckons to me."

    $chat.addmessage(cake, "Me, too baby")

    k "Coming!"

    scene bg booth with fade

    ki "The recording booth is... cozy. Padded walls and not a lot of space mean Cassandra and I are standing pretty close together."

    ki "Close enough I can smell her shampoo. Coconut and... hibiscus? Maybe?"

    $chat.addmessage(cake, "Not about the boner")

    ki "Through the window I notice a man moving to sit in front of the great console. It must be someone from Cassandra's team."

    c "< Put these on. >"

    $chat.addmessage(bar, "Put these on if you want to live")

    ki "She retrieves a set of thickly padded earphones from a rung on the wall and hands them to me. They're heavy, obviously professional gear, but what I notice most about them is how her fingertips graze my hand when I take them."
    $chat.addmessage(elsa, "Aww... but imagine how creepy this would be if she was a guy.")

    ki "She dons her own pair. I feel my heart thumping harder."

    $chat.addmessage(crab, "sexist ass")

    s "Oh, dating sim protags fall in love so fast."

    $chat.addmessage(fizz, "She's not wrong though.")

    s "At least we have a good reason this time!"

    $chat.addmessage(cake, "beta enablin' ass")

    ki "Cassandra knocks on the window, gives a thumbs up to her man outside."

    ki "A gentle chillstep beat flows through the earphones, softly electronic with a melody of smooth, tinkling piano. Cassandra begins to nod, capturing the rhythm."

    $chat.addmessage(shub, "Hey, I like chillstep")

    ki "She moves in a seamless flow from heels to head, ethereal, a waveform made flesh."

    $chat.addmessage(cake, "It's my experience that an orifice should be filled.")

    python:
        newComments = [
            [elsa, "Gross! Jesus!"],
            [bar, "Context"],
            [crab, "bro"],
            [fizz, "Grow up man"],
            [shub, "truer words never spkoen bruv"],
            [beav, "It's true but we don't say it :D"]
        ]
        chat.bulkMessage(newComments, 0.35)

    ki "She lifts her hands and deftly undoes the clasp of her choker."

    ki "It tumbles free."

    k "Oh..."

    s "Oh!"

    c "Undone in a time of need / heroin my heroine / set me set me free"

    ki "She's singing, sharp and clear. Her voice strikes me, pierces right through me. It's gorgeous. It's operatic but somehow dark and dangerous."

    $chat.addmessage(beav, "Heavy subject.")

    ki "It's the voice I've cried to, sang with, danced to."

    $chat.addmessage(elsa, "Hey Sophie... are you okay reading about that?")

    ki "But even a voice like that can't tear my focus from the scars."

    $chat.addmessage(cake, "wait why, Sophie you chase the dragon?")

    $chat.addmessage(elsa, "shit, sorry Sophie")

    s "Oh my god, the poor girl! Oh, Cassandra, what happened to you?"

    $chat.addmessage(shub, "Wait, really. You a fuckin doper lol")

    ki "The coarse, leathery trail snakes unevenly around her neck, roughly to the base of her skull. There are larger patches here and there, almost like... like, I don't know what."

    $chat.addmessage(crab, "let's not talk about that, like if my ass is being the mature one in the room you know it's bad")

    k "What..."

    $chat.addmessage(fizz, "Ignore this, Sophie")

    ki "But she's singing. She's singing so purely, and her eyes are focused and she's just so damn different and I don't know how or why it happened but suddenly there are tears in my eyes and I don't know if it's her song or the ligature marks on her neck or--"

    c "Until the world burns, the world burns me away ~"

    $chat.addmessage(unkn, "help me")

    $chat.addmessage(beav, "ligature. Someone tried to strangle her")

    ki "I'm trapped, now. Trapped inside her song, in this little room, inside a web of questions I can't answer."

    ki "The song ends."

    $chat.addmessage(elsa, "Sophie...")

    ki "The song, it... it ended. She's looking at me, her eyes full of questions. Yearning, longing, pleading."

    ki "I can only stare back. There's a gulf of something between us. I can't breathe."

    pause 1.0

    s "Chat. I need a minute."

    show image splashBRB at alphaFade

    pause 1.0

    python:
        newComments = [
            [cake, "hey is she okay? I'm foolin' but I feel like she's not okay"],
            [fizz, "Assholes."],
            [bar, "Am I missing something?"],
            [elsa, "I screwed up. I'm sorry Sophie!"],
            [crab, "Wait, what happened?"],
            [shub, "this got awful real"],
            [bar, "Sophie?"],
            [liv, "Sophie what happened?"]
        ]
        chat.bulkMessage(newComments, 0.37)

    pause 1.0

    $chat.addmessage(liv, "WHAT DID YOU DO TO HER")

    pause 1.0

    $chat.addmessage(beav, "Calm the fuck down please.")

    $chat.addmessage(liv, "I'm sorry : (")

    pause 1.0

    $chat.addmessage(elsa, "It's okay. I'm the one who said something stupid.")

    pause

    hide image splashBRB at alphaFade

    s "Hey guys. Sorry. We're not gonna talk about anything except the game for a bit."

    s "I'm pausing chat for a few minutes. If you wanna stick around, I'm really happy about that. If you wanna leave, no worries okay?"

    s "So let's move on. Cassandra just showed me her singing and her scars, but I'm not really sure what the significance is yet."

    $chat.addmessage(sophie, "Chat currently paused. Feel free to hang around, it's temporary!")
    pause

    ki "The back of her hand gently brushes my cheek, glittering with a teardrop she's wiped away."

    ki "I want to ask. I want to ask about the scars. I want to ask about her voice. I want..."

    pause 1.0

    ki "I want this silence to last forever."

    # knocking sound

    ki "At the sound, Cassandra whips the choker back around her neck and fastens it. The movement is practiced and swift, and it yanks me out of my mesmerized state."

    c "< I guess you have questions. >"

    ki "The door cracks open."

    k "I do, but... how can I ask them with a camera crew around?"

    c "< You can go out with me again. And maybe we can have another private moment. >"

    ki "I can only nod, and brush what's left of my tears away. I don't know how she got to me so fast."

    s "..."

    k "Wait, is... we're not done, are we? I was just..."

    ki "Tania's head pokes through the crack."

    t "Hey you two! So, uh, I know I said to be true to yourselves and everything, but we don't have a show if the leads disappear."

    c "..."

    k "..."

    c "< Kylie. I'm a simple girl at heart. You don't have to impress me. Just be willing to hold my hand or hug me even when it isn't private. >"

    ki "My heart drops. I wasn't even thinking about how much this must have taken out of her."

    c "< My voice... it's beside the point. I needed you to know that I'm broken, but I'm healing. I'm not perfect. I'm a work in progress.>"

    c "< Is that okay? It's fine if not. >"

    $chat.addmessage(unkn, "R/BG13:14-15. ")

    k "Hey. Are you okay?"

    c "..."

    k "You have, uh..."

    ki "There's blood on her lip. Not much. Just a slight discoloration."

    s "Wait. Has she got mysterious plot device coughing disease?"

    s "She's not gonna die, is she? That's bullshit if she does! You can't break my heart like that, game."

    ki "Cassandra covers her mouth, quickly, with one hand. When she withdraws it, the stain is gone."

    c "< Thanks for that. >"

    k "No, no. Thank you for... uh, that."

    k "Next time, though?"

    ki "She nods, again, almost imperceptibly. This feels wrong. Dates don't end this way. Right?"

    s "Okay, chat. We should be unlocked again. I'm really sorry, again, for the pause. Everything's fine."

    $chat.addmessage(elsa, "Sophie I'm so so sorry.")

    s "Nothing to be sorry about Elsa. Just let's move on, yeah?"

    $chat.addmessage(crab, "Hey I know I'm kind of a shitstarter, but I hope you're good.")
    $chat.addmessage(liv, "I'm glad you're okay Sophie :D")
    $chat.addmessage(shub, "Yeah")

    $renpy.notify("Cassandra is a simple girl at heart.")

    menu:
        "Hold out my hand":
            ki "Silently, I offer her my hand. I don't know what she'll think, but-"

            c "..."

            ki "Just like that, her hand nestles into mine, warm to the touch and so very, very soft."

            $chat.addmessage(fizz, "Oh, looks like that was the right choice.")

            $loveCass += 1
            $heldHands = True

        "Say goodnight":
            k "Goodnight Cassandra."

            ki "Her smile is all I need."

    ki "The night was not what I thought it would be."

    $chat.addmessage(beav, "Seems like that ended quickly.")

    ki "I get that we have to rush. I understand. Even so, I feel like Cassandra's entire life story was punched directly through my forehead."

    $chat.addmessage(cake, "they didn't talk at all on the rid eto the studio?")

    t "That was good stuff tonight, Kylie. I wish we could have seen whatever you two talked about in the booth, but..."

    k "Nope, sworn to secrecy."

    $chat.addmessage(crab, "coulda hit it right there")

    t "What do you think of her? Did the woman match the idol? Between us."

    $chat.addmessage(bar, "Is anything just between you, though, if Tania runs the show?")

    s "No way. Don't answer. She has a hidden microphone somewhere. Don't do it, me!"

    k "I haven't decided."

    $chat.addmessage(fizz, "A non-answer is still an answer!")

    ki "Of course I have, but it's none of Tania's business right now."

    $chat.addmessage(elsa, "So secretive ")

    ki "The rest of the ride progresses in silence. I have so much to sort out right now, I... I just need to sleep."

    $hideGui()

    # collect chat history in appropriate variable.
    $getHistory(2)

    scene bg black with fade

    jump robinDate1

    # end cass date
