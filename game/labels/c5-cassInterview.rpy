label c5cassInterview:
    stop music fadeout 2.0
    show c 1b at f12
    pause 1.0
    play music sadCass fadein 2.5


    $cassDone[0] = False

    while cassDone[0] == False:
        menu:
            c "< I'm here for you. >"

            "Will we see each other again?" if cassDone[1] == False:
                c 2a "<Yeah. I think so.>"

                c "<I've been through this five times and I've seen Robin twice. I'd say chances are pretty good.>"

                c "<I don't like to think about the ones I've only seen once. I guess I'm trying to think positively.>"
                $cassDone[1] = True
            
            "Who are you? Really." if cassDone[2] == False:
                c 1q "<Oh, who is anybody really.>"

                c "<It's like I said. Almost everything we've talked about is true, in one way or another.>"

                k "You're a real rock star, eh?"

                c 2a "<Yup. I mean, I was. After I lost my voice it was kind of hard to keep the band together.>"

                c "<I wanted to play and write, but after a bit I got replaced.>"

                k "That's awful."

                c 1b "<That's the game, though. People forget so quickly. Nobody has room for a singer who can't sing.>"

                c 2r "<Then again, I guess I wasn't really anything. The person outside was the rock star. Who knows if my memories are real at all?>"

                k "I have memories, though."

                c "<Yeah. Aren't they Sophie's, though?>"

                k "... I don't know."

                c 2a "<I don't think it matters. Memories out there in the world aren't always trustworthy, so whatever you remember is fine.>"

                k "I guess I feel pretty bad for Sophie, then."

                c 1a "<Oh?>"

                "Kylie settles her hands over her navel, uncertain. Something's missing. She's not quite sure what."

                k "... mm-hm."

                c 1m "<Maybe Sophie's body and my body will get together out there.>"

                k "Maybe."

                $cassDone[2] = True

            "I have to tell you something. (Confess)" if cassDone[3] == False and loveCass == 5:

                k "Cassandra."
                
                c 2o "<Yup?>"

                k "What if I don't understand my feelings at all?"

                c "<I guess I need more specifics than that?>"

                k "... I think I might love you."
                
                c 2j "<Heh. After one good date and one horrible one, eh?>"
                
                c "<Look, I'm flattered. I am. But you were just ripped from the mind and body of someone else and I'm not sure you understand your emotions yet.>"

                k "I'm not a baby, Cassandra."

                c 2a "<You kind of are, though. Kylie, you're a whole new consciousness and you came to exist like five minutes ago.>"

                pause 0.5

                c 1b "<Don't cry. Hey, no, no no. I'm sorry, I'm sorry. I said a stupid thing.>"

                k "I just don't understand any of this!"

                c "<I don't think any of us do. Only Fontaine knows what's going on.>"

                k "I have to tell you something else."

                c 1r "<This is the time to do it, Kylie. I'll listen to whatever you have to say.>"

                k "I think I'm glad Fontaine did this."

                c 2o "<Wait, really?>"

                k "Yeah."

                c "<It's a monster, Kylie. A killer.>"

                k "... it gave me life."

                c 2b "..."

                k "It gave me a chance to meet you!"

                c "<Kylie.>"

                k "No, no! I know you think it's not true, but I love you and I love your voice and your song and I love that choker, too!"

                c 2c "<... god dammit.>"

                k "I know you don't believe me."

                c 1b "<It's the dating sim talking. The game type will wear off after a few cycles of this.>"

                k "... you're sure?"

                c "<... no.>"

                k "You don't have to love me back. Maybe you're right, maybe these feelings aren't even mine or they aren't even real."

                k "But they feel real."

                k "I won't bring it up again. I'm sorry."

                c 2r "<... I enjoyed our dates.>"
                
                k "..."
                
                c 1r "<Kylie. I'm straight. I was straight before, it's just that the game warps us while we're inside it.>"

                c "< But listen. If I weren't. I mean... if I were bi or whatever, I think I'd like dating you. I don't even know if that makes sense.>"

                k "... thanks. Thank you."

                c 2m "< Friends?>"

                k "Friends."

                
                
                $chat.addmessage(fon,"Imagine your first broken heart to be among the first emotions you ever get to feel. Oh, Kylie. :(")
                
                $cassDone[3] = True

            "How are you doing, though?" if cassDone[4] == False:
                c 1q "<I'm nervous, I guess. I always am.>"
                c "<I don't know if you noticed, but we're all more or less here because of our association with Robin.>"

                k "Really?"

                c "<She's the center point. We're like a Venn diagram of failure.>"

                c 2r "<I guess Fontaine might be the centerpiece, though.>"

                k "... that's pretty awful, though."

                c 2a "<Is it? I guess it's still taking lives. Maybe I'm numb to it, or like, nothing out there feels real.>"

                if cassBio.severed:
                    c "<Something does feel different this time, though. I dunno. Usually I get pretty panicked around now.>"
                    c 1m "<I feel at ease.>"
                    "Updates complete. Object Cassandra severed."
                $cassDone[4] = True

            "Are we really stuck here? Is any of this real?" if cassDone[5] == False:
                c 1a "<You might want to ask Tania more about that. If you believe anything she says, she's been through this a lot. Like... a lot.>"
                k "So there's no way out, then."
                c 2o "< Probably not. If we're just code, what are we supposed to do against something that manipulates code around it?>"
                k "You really think we're in a simulation?"
                c 2m "<That's what makes sense to me.>"
                c 1m "<Cheer up. Some of the game worlds are pretty great. There was a kart racing game that was a lot of fun.>"
                c 1r "<It's the porn games where stuff goes off the rails.>"
                k "Porn games."
                c 2u "<Let's just say I used to think octopuses were cute.>"
                
                $cassDone[5] = True

            "Can you give me a minute?":
                stop music fadeout 2.0
                c 1a "< Anything for a fan. >"
                play music bedroom fadein 0.5
                $cassDone[0] = True