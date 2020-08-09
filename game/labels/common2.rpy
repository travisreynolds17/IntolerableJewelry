label common2:

    # because the previous label, lichDate, had multiple choices to get us here, we're going to hide the GUI and show the definition screen on this label instead of at the end of the last.
    # this way it works as a catch-all.
    stop music fadeout 2.0
    $hideGui()

    scene bg load-dating with fade
    pause

    scene bg stage with fade

    play music cheerfulGuitar fadein 3.0

    pause 0.66
    $showGui()
    $chatPause = False

    show t 1m at fr12

    t "Hi everyone and welcome back to One Week Waifu!"

    $chat.addmessage(fizz, "Anybody ever watch these shows in real life?")

    t "So, something goes awry every single season on this show, doesn't it?"

    $chat.addmessage(elsa, "From time to time.")

    t 1a "That's part of the fun, right?"

    $chat.addmessage(crab, "hell no")

    $chat.addmessage(shub, "pssshhh no")

    $chat.addmessage(beav, "All the time. Car crash TV is fun.")

    t 2l "So, we've changed up our schedule a little bit this time as Lichelle has some personal stuff to take care of."

    $chat.addmessage(fizz, "I wonder, does Tania know why Elle is gone? Or is she being diplomatic?")

    t "But don't worry! We're going to keep up with her and she may just return on another season!"

    ki "I'm impressed with Tania's ability to sell a vague cover story."

    $chat.addmessage(bar, "Kylie, you should be in our chat.")

    t 1o "So, we've decided to move things up a little."

    t "Everyone please welcome back Cassandra and Robin!"

    $chat.addmessage(elsa, "It's odd to see them now. I feel like we got pretty intimate with both of them.")

    show t 1a at mt3
    pause 0.2
    show r 2a at fl12
    pause 0.1

    show c 1p at fl11

    t "Welcome back ladies!"

    $chat.addmessage(shub, "I wanna get intimate with both of them.")

    r "Of course."

    c "..."

    $chat.addmessage(fon, "Me, too, Shub-Nickelrath :)")

    ki "I wonder if Tania had time to put her idea for Cassandra in place yet."

    $chat.addmessage(shub, "Yo Elsa, what'd you two chat about. you n Fontaine")

    t 1q "I hope it wasn't too much trouble for you to come back so soon."

    $chat.addmessage(elsa, "Why?")

    r 1m "Nothing troubles me, dearest."

    $chat.addmessage(shub, "cuz she private messagin me and I wanna know if I'm gonna get catfished")

    c 1b "..."

    t "Oh, right! Cassandra, would you mind showing off the new toy I gave you?"

    $chat.addmessage(elsa, "She was asking about what I do at the group I run.")

    show c 1p

    ki "A small smile on Cassandra's face heralds the appearance of her cell phone. She makes a dramatic, overemphasized motion to tap the screen."

    $chat.addmessage(crab, "boobs?")

    c "< It was no trouble Tania. Thank you for reaching out. Hello, Robin. You look lovely this evening. >"

    $chat.addmessage(beav, "wonder what kind of setup Tania has for Cassandra")

    ki "Her words flow, not from the phone, but from a pair of wireless speakers set on either side of the stage."

    $chat.addmessage(fon, "LOL")

    $chat.addmessage(elsa, "Yes, crab, if you have to know. We talked about our boobs and compared sizes.")

    ki "I wonder why we didn't do this sooner?"

    r 1j "Oh, thank you Cassandra. Yes, I do."

    $chat.addmessage(shub, "Cool. BRB")

    $chat.addmessage(fizz, "Bye Shub. Watch for fangs.")

    t "Great, it works! So, shall we talk about what's happened so far?"

    $chat.addmessage(crab, "wait really?")

    c 1g "< Kylie won't be joining us? >"

    $chat.addmessage(elsa, "No.")

    t 1a "She'll be in the wings for now."

    ki "Cassandra's disappointed face reads plainly. I guess she's used to expressing herself visually."

    $chat.addmessage(cake, "cass being sad about it is a good sign for Kylie")

    r 1h "Oh, dear. Does our little butterfly have you wound around her fingers already, then?"

    c 1j "< Maybe. Maybe not. >"

    $chat.addmessage(fizz, "Robin being sassy.")

    r 1k "I never expected you to be so easy to attain."

    $chat.addmessage(elsa, "Um, excuse me whore, but you're the one who kissed me in the dark!")

    $chat.addmessage(elsa, "Kissed Kylie.")

    ki "If I were watching this at home, I would be chucking popcorn at the screen and shouting about Robin being rude."

    ki "Having met her and spoken with her, I feel like these words are calculated rather than bitchy."

    $chat.addmessage(crab, "that makes sense tho. they're competitors")

    stop music fadeout 1.0

    c 2o "< Are you feeling disadvantaged, Robin? Maybe you should shut the lights off and vanish again.>"

    show c 2a

    play music competition fadein 1.0

    $chat.addmessage(cake, "o shit bitch :D :D")

    s 1j "Whoa! Stalker much?"

    $chat.addmessage(elsa, "Cassandra was at the theater?!?")

    show r 1e
    pause 0.2

    show r 1a

    ki "Robin's placid features flicker for a heartbeat. It's hard to tell, but I thought I saw..."

    ki "Rage?"

    $chat.addmessage(fizz, "Whoa.")

    r "You were spying on us, then? I had no idea you had a voyeuristic streak, darling."

    ki "And right back to pristine deconstruction."

    $chat.addmessage(beav, "I bet she'd be hell on wheels in a rap battle")

    t 1h "Cassandra, is that true? And how did you know where we were going?"

    c 1k "< I knew because Robin is boring. I've been at Ganymead when she was practicing her act. Of course I wasn't spying. >"

    $chat.addmessage(bar, "Makes sense, tho. Robin said Cassandra played there.")

    c "< I'm just not an idiot. >"

    s "Cass is fired up."

    $chat.addmessage(beav, "Catfight? I thought they were friends")

    r 2m "I would never call you an idiot, dear."

    r "A hopeless addict, perhaps, a pitiful pity party committed to a {i}ponosit{/i} choker that screams for the attention it supposedly protects against."

    show t 1i

    show c 1i

    $chat.addmessage(elsa, "Oh my god o.o")

    ki "The temperature in the room is plummeting."

    c 1d "Cassandra is typing, her features flushed."

    $chat.addmessage(cake, "yep, Robin's a class 1A bitch")

    r 1j "Quickly, darling. We wouldn't want half of a witty retort to go to waste."

    $chat.addmessage(crab, "roasting a mute is full-on savage")

    t 1q "Robin, let's, uh, let Cassandra have her turn."

    r 1m "If you insist on being bored, be my guest, darling. I'm here for neither of you."

    $chat.addmessage(fizz, "Must be something deeper going on here.")

    show t 1c

    ki "Tania looks legitimately hurt by that."

    t "Robin, I... I thought we were friends. What's gotten into you?"

    $chat.addmessage(crab, "Hell no. You be good to Tania you asshat")

    pause 0.1

    r 1d "I have been searching for Kylie for half a decade!"

    show t 1h
    pause 0.2
    show c 1h

    ki "Her shout snaps Cassandra out of typing for a second."

    t 2h "Wait. Kylie specifically?"

    $chat.addmessage(bar, "I thought she knew.")

    ki "Robin, for once, doesn't answer."

    c 1d "< I'm not an addict and you're a trash actress. And a cheapskate. I make ten times the money playing anywhere else in this country than at your stupid theater! >"

    show t 1b

    $chat.addmessage(beav, "legit rock star")

    c 1e "< And unlike you I'm not proud of my scars because I didn't give them to myself! >"

    show r 1c

    show t 1i

    $chat.addmessage(elsa, "oh god")

    $chat.addmessage(fizz, "O.O")

    ki "I've had enough. Robin's demeanor breaks, then, and it's not the fury I expected to see."

    stop music fadeout 3.0

    k "Stop it!"

    show r 1b
    show c 1k
    show t 2r

    $chat.addmessage(bar, "Get 'em, Kylie!")

    k "Stop fighting! This isn't how this is supposed to go!"

    play music kylieFightsBack

    t 1q "Oh, uh, welcome back Kylie-"

    $chat.addmessage(elsa, "I'm glad she's doing something. Game should've given us a choice though?")

    k "Tania, hush for a second!"

    t 1h "O-okay."

    $chat.addmessage(cake, "hey now K dawg. Be nice to Tania")

    ki "They're all looking at me now. I wonder, absently, if this will make for good TV."

    k "First off, I like you all."

    $chat.addmessage(fizz, "fair")

    k "Second, Cassandra, you look hot. Robin, you look amazing. Tania, you already {i}know{/i} you look good."

    s 1b "What an odd thing to say."

    $chat.addmessage(unkn, "R/BG13:14-15")

    show t 1a

    ki "A little smile forms on Tania's lips. I don't know if that helped ease the tension, though."

    k "I don't know how much of this behavior is for the show, but I'd rather go home alone than see two people who mean so much to me tear each other apart."

    $chat.addmessage(fizz, "Taking a stand!")

    k "Cassandra, I have loved your music for as long as I can remember."

    show c 1q
    k "I didn't tell you this the other day, but I have like seven posters of you and a signed guitar I have no idea how to play!"

    $chat.addmessage(crab, "fangirl level 3")

    k "You showed me your secret and let me hear your real voice. Not this machine, not a text. Your voice cut me into little pieces!"

    show c 1t

    k "You... you are everything I imagined you to be and so much more, you're so warm and comfortable and your eyes destroy me."

    $chat.addmessage(beav, "Did Kylie just spill the beans?")

    k "But you don't need to justify yourself or your scars to anyone! You don't have to be a badass all the time!"

    s 1i "Oh god, Beaver, I think we screwed up!"

    show c 1b

    k "Robin, I... I wish I knew what our first encounter meant to you. I wish I knew, because I might've treated you differently!"

    show r 1b

    $chat.addmessage(cake, "hindsight kids")

    pause 0.5

    k "You kissed me. In the dark. Just like that, like it was the easiest thing in the world for you. But I felt it!"

    $chat.addmessage(bar, "this is the part where Kylie's theme music would fade in") 
    
    $chat.addmessage(fon,"That happened right before Tania welcomed Kylie back. ;)")

    show t 1q
    show c 1h

    k "I felt those years in that kiss! I could feel you shaking!"

    k "You don't have to pretend to be so refined and in control!"

    $chat.addmessage(elsa, "Preach, sister")

    k "And you know what else? I have no idea where Lichelle is, but I was looking forward to learning about her, too!"

    show c 1b
    show t 1m
    pause 0.1
    show r 1b

    s 1a "This is quite a diatribe."

    $chat.addmessage(fon, "Back. This part breaks my heart :(")

    k "So..."

    t "Kylie..."

    $chat.addmessage(unkn, "stringSever(firstName)")

    k "So stop fighting! I'm not worth it. I'm not!"

    $chat.addmessage(fizz, "Yes you are, Kylie!")

    r 1c "Papillon, I... I'm sorry."

    c 1g "< Me, too. I'm sorry, Kylie. >"

    $chat.addmessage(cake, "Nothing like a good ol' fashioned run down to fix stuff up")

    t 1b " ... "

    k "Don't apologize to me. Apologize to each other!"

    $chat.addmessage(crab, "yes MOM")

    pause 1.0

    c 1q "< I'm sorry, Robin. I shouldn't have brought up your scars. >"

    r 1k "You shouldn't have, no. And I should not have called you an addict."

    $chat.addmessage(bar, "Kiss and make up")

    pause 0.5

    r 1b "Kylie. I have loved you for a quarter of my life. I could not let this chance slip past!"

    $chat.addmessage(elsa, "#hentai?")

    k "And I've idolized Cassandra almost as long!"

    $chat.addmessage(cake, "See Elsa? Now you're getting it")

    c 1h "..."

    r 1h "..."

    $chat.addmessage(beav, "H training lol")

    t 1l "Oh, wow."

    pause 0.7

    k "But that's not the same thing, is it? Cassandra, you were an idol to me. Someone I could love from afar. Knowing you, now..."

    $chat.addmessage(fizz, "Feels like a climactic choice is coming, doesn't it?")

    k "And having met you again, Robin, and experiencing your feelings like that..."

    $chat.addmessage(bar, "It really does.")

    k "We can stop the show right now."

    show r 1l
    show c 1r

    s "What?"

    $chat.addmessage(fon, "My heart! It's breaking!")

    t 1i "Kylie, wait a second."

    k "I've already made up my mind!"

    $chat.addmessage(crab, "pick Robin! worship her panties!")

    $chat.addmessage(cake, "Taaania! Taaania! WTF bro")

    s 1i "I haven't decided!"

    stop music fadeout 3.0

    k "Cassandra. Robin."

    $chat.addmessage(elsa, "Yes!")

    show r 1i

    k "I..."

    show c 1i

    $chat.addmessage(bar, "No!")

    k "I choose..."

    # SFX
    scene bg bsod

    pause 2.0

    python:
        newComments = [
            [elsa, "FLUCK!"],
            [bar, "lovely."],
            [fizz, "How frustrating"],
            [fon, "Noooooo! :)"],
            [cake, "this bullshit, this is a setup"],
            [crab, "well, hell. "],
        ]
        chat.bulkMessage(newComments, "random")
    s 1d "Double U tee eff!"

    s "Hang on. Hang on chat, hang right the hell on."

    scene bg black
    pause 1.0

    s 1d "Reloading."

    scene bg stage with fade
    pause 0.8
    scene bg bsod

    pause 1.0

    s 1e "Guys. I'm so pissed right now."

    $chat.addmessage(elsa, "Reload!")

    s 1d"I have to reload my last save and it's... quite a ways back. Hang on."

    s "Almost all of my saves are missing."

    $chat.addmessage(beav, "This has to be part of the game.")

    scene bg black

    s 1b "We gotta go all the way back to the first spot. Right before... aw hell!"

    $chat.addmessage(crab, "be some shit if it isn't")

    s "Sorry guys. We'll have to do the dates again. But that's fine, right? Maybe I can make some different choices."

    s "If we get any further and the game is bugged, I'm gonna lose my mind."

    s "But I'm gonna stop and recharge first."

    $chat.addmessage(elsa, "Sophie? You there?")

    s 1a "I'm restless. What am I doing."

    $chat.addmessage(fizz, "Didn't you just recharge like a minute ago?")

    show image splashBRB at alphaFade

    pause 1.0

    # takes a break. Weird shit while she's away.

    $hideGui()

    show screen chatterbox

    python:
        newComments = [
            [elsa, "I'm worried about Sophie."],
            [fizz, "Should I go check on her?"],
            [cake, "You know her IRL?"],
            [fizz, "We used to be close."],
            [crab, "used to be?"],
            [elsa, "Don't worry about it. Fizz, private message comin"],
            [beav, "Hope she's ok. She comes back I'm bout to tell her to get some sleep."]
        ]
        chat.bulkMessage(newComments, "random")
    pause
    $getHistory(7)
    

    pause 1.0

    $showGui()
    hide screen chatterbox

    s 1a "Alright guys. Let's reload this ish."

    s "Guys?"

    pause 0.8

    s 1b "Alone. Again. If you care at all, I'll be back in thirty."

    $hideGui()

    scene bg black with longFade

    pause 1.0

    jump realWorld2
