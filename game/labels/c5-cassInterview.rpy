label c5cassInterview:
    show c sad with dissolve

    $cassDone[0] = False

    while cassDone[0] == False:
        menu:
            c "< I'm here for you. >"

            "Will we see each other again?" if cassDone[1] == False:
                c "<Yeah. I think so.>"

                c "<I've been through this five times and I've seen Robin twice. I'd say chances are pretty good.>"

                c "<I don't like to think about the ones I've only seen once. I guess I'm trying to think positively.>"
                $cassDone[1] = True
            
            "Who are you? Really." if cassDone[2] == False:
                c "<Oh, who is anybody really.>"

                c "<It's like I said. Almost everything we've talked about is true, in one way or another.>"

                k "You're a real rock star, eh?"

                c "<Yup. I mean, I was. After I lost my voice it was kind of hard to keep the band together.>"

                c "<I wanted to play and write, but after a bit I got replaced.>"

                k "That's awful."

                c "<That's the game, though. People forget so quickly. Nobody has room for a singer who can't sing.>"

                c "<Then again, I guess I wasn't really anything. The person outside was the rock star. Who knows if my memories are real at all?>"

                k "I have memories, though."

                c "<Yeah. Aren't they Sophie's, though?>"

                k "... I don't know."

                c "<I don't think it matters. Memories out there in the world aren't always trustworthy, so whatever you remember is fine.>"

                k "I guess I feel pretty bad for Sophie, then."

                c "<Oh?>"

                "Kylie settles her hands over her navel, uncertain. Something's missing. She's not quite sure what."

                k "... mm-hm."

                c "<Maybe Sophie's body and my body will get together out there.>"

                k "Maybe."

                $cassDone[2] = True

            "I have to tell you something. (Confess)" if cassDone[3] == False and loveCass == 5:

                k "Cassandra."
                
                c "<Yup?>"

                k "What if I don't understand my feelings at all?"

                c "<I guess I need more specifics than that?>"

                k "... I think I might love you."
                
                c "<Heh. After one good date and one horrible one, eh?>"
                
                c "<Look, I'm flattered. I am. But you were just ripped from the mind and body of someone else and I'm not sure you understand your emotions yet.>"

                k "I'm not a baby, Cassandra."

                c "<You kind of are, though. Kylie, you're a whole new consciousness and you came to exist like five minutes ago.>"

                pause 0.5

                c "<Don't cry. Hey, no, no no. I'm sorry, I'm sorry. I said a stupid thing.>"

                k "I just don't understand any of this!"

                c "<I don't think any of us do. Only the Entity knows what's going on.>"

                k "I have to tell you something else."

                c "<This is the time to do it, Kylie. I'll listen to whatever you have to say.>"

                k "I think I'm glad the Entity did this."

                c "<Wait, really?>"

                k "Yeah."

                c "<It's a monster, Kylie. A killer.>"

                k "... it gave me life."

                c "..."

                k "It gave me a chance to meet you!"

                c "<Kylie.>"

                k "No, no! I know you think it's not true, but I love you and I love your voice and your song and I love that choker, too!"

                c "<... god dammit.>"

                k "I know you don't believe me."

                c "<It's the dating sim talking. The game type will wear off after a few cycles of this.>"

                k "... you're sure?"

                c "<... no.>"

                k "You don't have to love me back. Maybe you're right, maybe these feelings aren't even mine or they aren't even real."

                k "But they feel real."

                k "I won't bring it up again. I'm sorry."

                c "<... I enjoyed our dates.>"
                
                k "..."
                
                c "<Kylie, I told you before. I'm straight. I was straight before, it's just that the game warps us while we're inside it.>"

                c "< But listen. If I were like that, I think I'd like dating you. I don't even know if that makes sense.>"

                k "... thanks. Thank you."

                c "< Friends?>"

                k "Friends."
                
                $cassDone[3] = True

            "How are you doing, though?" if cassDone[4] == False:
                c "<I'm nervous, I guess. I always am.>"
                c "<Like, I worry that someday the Entity will get bored. Or maybe this time it's telling the truth.>"

                k "This time?"

                c "<It always says this is the last time. It just needs one more life, whatever.>"

                c "<Maybe this time it's right.>"

                k "... that's pretty awful, though."

                c "<Is it? I guess it's still taking lives. Maybe I'm numb to it, or like, nothing out there feels real.>"

                if severCass == True:
                    c "<Something does feel different this time, though. I dunno. Usually I get pretty panicked around this time.>"
                    c "<I feel at ease.>"
                    "Updates complete. Object Cassandra severed."
                $cassDone[4] = True

            "Are we really stuck here? Is any of this real?" if cassDone[5] == False:
                c "<Data not found.>"
                k "Oh my god, what?"
                c "<I'm kidding. Look, you might want to ask Robin more about that. If you believe anything she says, she's been through this a lot. Like... a lot.>"
                k "So there's no way out, then."
                c "< Probably not. If we're just code, what are we supposed to do against something that manipulates code around it?>"
                c "<Cheer up. Some of the game worlds are pretty great. There was a kart racing game that was a lot of fun.>"
                c "<It's the porn games where stuff goes off the rails.>"
                k "Porn games."
                c "<Let's just say I used to think octopuses were cute.>"
                
                $cassDone[5] = True

            "Can you give me a minute?":
                c "< Anything for a fan. >"
                $cassDone[0] = True