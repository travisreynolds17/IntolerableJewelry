label c5taniaInterview:
    
    $taniaDone[0] = False

    while taniaDone[0] == False:
        menu:
            t "I think an 'ask Tania' reference right now would be sad. "

            "Will we see each other again?" if taniaDone[1] == False:
                t "Yup. I think we're all pretty much inseparable."

                k "You're that sure about it?"

                t "I can understand why you might not be. This stuff's all new to you. I understand."

                k "You do?"

                t "Yeah."

                "Kylie holds her tongue. Tania seems to be chewing her own, gently, considering how to continue."

                "Whether to continue."

                t "I have dreams."

                k "Dreams?"

                t "I'm the only one who does. I asked around. It's just me."

                pause 0.5

                t "Isn't it?"

                k "... no."

                t "I knew it. When I came to get you when you were s'posed to meet up with Lichelle, you were twitching. Lashing out."

                t "Kylie. I need you not to judge me for the next thing I'm about to say."

                pause 0.5

                k "Oh, uh, okay."

                "Tania crosses her legs. It's more of a struggle for her than she would admit."

                t "I've watched the others sleep. They don't move around like you do. They just shut down."

                k "... why are you watching them sleep."

                "It's a statement, not a question."

                t "For science."

                k "Tania."

                t "..."

                t "... I don't know."

                t "I know it's horrible, but something drives me to look out for them. Like I'm their mom or something."

                k "... I guess I understand."

                t "I don't know how you could."

                k "You're right. I don't. But I don't judge you for it."

                t "Thanks, kiddo."

                if loveTania > 3:
                    k "..."
                    t "What?"
                    k "... can I hug you?"
                    t "Uh, sure. If you wanna."
                    "The urge came, was fulfilled, and receded. Kylie breathed Tania in, comforted in the scent of apples and cinnamon."

                $taniaDone[1] = True
            
            "Who are you? Really." if taniaDone[2] == False:
                t "It's hard to answer that one, Kyles."
                
                t "If you believe Fontaine, we're all born from the lives of some streamer who picked up this game."

                t "Can I ask you something?"

                k "I don't have many answers."

                t "What is the name of the game Sophie was playing?"

                pause 0.5

                k "Intolerable Jewelry."

                pause 0.5

                k "Wait. That's Cassandra's song, though."

                t "You love that song, right?"

                k "I do."

                t "How's it go, again?"

                k "Well, it..."

                pause 0.7

                k "Oh. I don't know."

                t "Mm-hm."

                t "For me, the game was called 'Lullaballet'. It was a dancing game."

                k "You can dance?"

                t "I took ballet for all the years when I was a lil' baby."

                k "You still have the leotard?"

                t "Hey now. Don't make fun."

                k "I'm not, I'm impressed."

                pause 0.5

                t "Ahem."

                t "My point is, how the hell do I know what that game was called? I never played it."

                t "You never played Intolerable Jewelry. Sure, it's Cassandra's song, but what does her song have to do with you? The plot, I mean."

                k "Plot?"

                t "Fontaine says we're just manifestations of that. Some soup boiled up from our player's mind, which in turn birthed the content of the game, which..."

                k "Stop, stop. My head hurts."

                pause 0.5

                t "Sorry."

                pause 0.5

                k "It's okay. Do you believe her?"

                t "Dunno. As far as I know she's never lied to us. She's been honest in a way that pisses me off, most of the time."

                t "Like she'll tell you something that's true, deep down you know it, but she says it in such a self-aggrandizing way it makes you want to drive nails into her goddamn eyes."

                k "Tania!"

                t "What?"

                k "I didn't know you had such a violent streak."

                pause 0.5

                t "Maybe when you've been through this cycle a few more times, and watched everything you've worked for get discarded over and over, you'll understand."

                t "I'm sorry if I'm critical. I'm just tired."

                t "I'm tired of starting at nowhere and ending at nowhere."

                t "I'm tired of being the god damned host. Or the sponsor. Or the MC."

                "She's crying. Kylie's unsure when that started."

                t "I... I wish it was ME who Fontaine murdered, for once."

                t "I..."

                menu:
                    "Embrace her":
                        "Kylie finds her arms around Tania's quaking shoulders. Just like that."
                        "It isn't like she imagined. Tania doesn't quietly hug back."
                        t "Kylie..."
                        "Instead, she shatters. Her sobs come violently, uncrontrollably. Painful, gasping sobs that shake her entire body."
                        k "How many times have you done this?"
                        "She's choking on them, now. Out of the corner of her eye Kylie notices Cassandra putting a gentle hand on Lichelle's shoulder, keeping her seated."
                        t "... two hundred fifty-four."
                        "Icicles scream within Kylie's bloodstream."
                        k "I can't... I don't know what to say."
                        t "Nothing either of us has to say matters."
                        "The moment passes. Tania gathers her composure."
                        pause 0.5
                        t "Look. We don't have a lot of time. I'm sorry to make this about me. Let's just move on."
                        "Kylie nods, quietly. She wonders how she knows there was no other choice but to hold Tania, just now."
                $taniaDone[2] = True

            "I have to tell you something. (Confess)" if taniaDone[3] == False and loveTania == 5:
                k "There's something I want to say."

                t "It's your show, kiddo. Season 7 of One Week Waifu, right?"

                k "I guess it is."

                k "So here goes."

                pause 0.5

                t "I'm waiting."

                "She's smiling, but the smile has no light behind it."

                k "I don't know if I understand how feelings work."

                k "Before now, I've never had them. Not my own, right? I guess?"

                t "Mm-hm."

                k "So it's stupid for me to think I know what's going on in my heart."

                t "Yup, yup."

                k "I think I might love you."

                t "Sure, sure."

                "The excited warmth, the nervousness, bursts within Kylie's chest. The warmth pours away from her center."

                k "Is... I don't know. Is that how someone's supposed to react to a confession?"

                t "Maybe?"

                k "... is this what despair feels like?"

                pause 0.5

                t "What do you think?"

                k "I DON'T KNOW!"

                pause 0.5

                k "I'm sorry-"

                t "Hey. No. Don't be sorry. You're working through things you have no way of understanding."

                pause 0.5

                t "Look. You're cute. You're a firecracker. A firecracker under a weighted blanket, but whatever. You're endearing."

                t "From my perspective though, you're like a little kid. And I don't want to feel like your mom."

                pause 0.5

                k "..."

                t "Hey. You might not think this right now, but that's a positive thing."

                k "Is it?"

                t "Yeah. Did you ever notice I never flirt with the others? Even in a dating sim?"

                k "I thought you were just being a good host."

                t "Psh. They're like my children, Kylie. I love them. I care about them."

                t "But I don't want them. You know."

                pause 0.5

                t "What I'm getting at is I... I want you to mature a little."

                t "Really get to know yourself. Figure out what makes Kylie tick."

                pause 0.5

                t "After that. If you're still sure you love me, I..."

                pause 0.5

                t "... I'll be waiting. For you."

                k "I feel sick."

                t "Is that how someone's supposed to react to a confession?"

                pause 0.5

                k "Maybe."

                k "Thanks, Tania."

                t "Hey. I'm always here for you, Kyles."

                $taniaDone[3] = True

            "How are you doing, though?" if taniaDone[4] == False:
                if taniaDone[3] == True:
                    t "I'm real excited about the kind of person you'll become. It's been a bit since we had a new person who survived becoming Strung."
                    k "Huh?"
                    t "Oh, don't worry about it. You're here, that's what counts."
                else:
                    t "I'm relaxed. Robin'll be back, good as new, in the next one. Meanwhile, I'm sitting around replaying seasons one through six in my memories."
                    t "I kind of love trash TV."
                    k "That's good?"
                    t "Yup."
                    
                $taniaDone[4] = True

            "Are we really stuck here? Is any of this real?" if taniaDone[5] == False:
                t "R/BG13:14-15"
                $taniaDone[5] = True

            "Can you give me a minute?":
                t "We'll be back right after these words from our sponsor."
                k "What?"
                t "I can't believe I got you with that again."
                $taniaDone[0] = True

   