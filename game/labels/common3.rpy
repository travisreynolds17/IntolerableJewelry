label common3:
    # repeats end of common1, with some stuff changed. 

    # game devouring Sophie's life bit by bit. Dates are now different. 


    scene bg near stage
    with fade

    

    scene bg near stage with fade

    show t

    t "Wow, that's some story! So, we know you were just off camera while our Suitors introduced themselves."

    

    hide t with dissolve
    show c at left
    show r
    show l at right
    with dissolve

    t "Given what you heard from them, who has your attention?"

    s "Okay. Well, I guess we're going from here again!"

    s "I was sure I'd saved more recently. What can ya do."

    #choice

    $temp = False

    while temp == False:

        s "I wonder if I should stick with the girl I was thinking about last time."

        menu:
            "Cassandra":
                scene bg stage
                show c with dissolve

                t "Oh, you like the quiet type eh?"
                c "..."
                s "I still wanna know how she got those marks. Like, I thought it was a suicide attempt, but she said only Robin gave scars to herself."
                s "Oh. That means someone else did that to her?"

                $temp = True
                $loveCass += 1
                $ which_girl_1 = "Cassandra"

            "Robin":
                scene bg stage
                show r with dissolve

                t "Oh, you like the mysterious type eh?"
                r "I'm glad. I've been waiting for you for so, so long."
                if $which_girl_1 == "Robin":
                    s "Wow, I missed that the first time. I thought she was just being spooky!"
                else:
                    s "Wow! I guess if I picked her before that would've been a big clue about our past!"
                # chat tells her that's not what Robin said the first time, but the message vanishes
                $temp = True
                $loveRobin += 1
                $ which_girl_1 = "Robin"

            "Lichelle":
                scene bg stage
                show l with dissolve

                t "Oh, you like the dangerous type eh?"
                l "Don't worry, Kylie! I'm only dangerous if you want me to be."
                ki "She winks. I'm not sure if I believe her."
                s "I wonder if that was a good choice, now that I think about it."
                s "If she's not even going to be around for the second round, maybe there's another way to spend time with her."
                $temp = True
                $loveLich += 1
                $ which_girl_1 = "Lichelle"

            "You on the menu, Tania?" if loveTania == 0:
                t "We talked about this already, Kylie."
                ki "Jeez, I guess not."
                s "We did? Oh, I guess it was in the hallway before the show."
                $loveTania += 1

            
                
            # END OF CHOICE

    scene bg stage
    show l with dissolve
    t "So let's talk a little bit about how this show works!"

    s "Oh yes, let's. Makes for such an exciting stream!"

    t "Every woman involved in this show is, of course, 20 years old or older -- but not much older, right? -- and each has consented to the format. We're looking for love here, people!"

    s "Uh huh, yup. Yup yup. Love and stuff."

    t "Kylie will go on a total of seven dates, one date each day of the week. Each Suitor will have two dates with her, and then one final date with whomever Kylie decides is worthy of her body!"

    s "... eww."

    t "Each suitor has already selected destination for the date. Meals and accommodations are on us, so hang on to your pocketbook Kylie!"

    k "How do we decide who goes first?"

    t "Glad you asked. To keep it fair, we'll go alphabetically again!"

    s "Hang on a minute. I just realized we didn't go alphabetically before. We went Cass, Robin and then Lichelle?"

    s "Guys, L comes before R, right?"

    k "What if we just don't click at all?"

    pause 3.0

    hide t with dissolve
    show c at left
    show r
    show l at right
    with dissolve

    t "I'd say you don't have a chance at all!"

    s "Tell me about it, Tania."

    t "Kylie, Cassandra, Robin, Lichelle, on behalf of everyone at One-Week Waifu, I wish you the best of luck! Let's see who makes it to the end!"

    k "Thanks, Tania."

    c "..."

    r "I would say the choice is obvious."

    l "Obviously it's gonna be me!"

    t "Thanks for tuning in everybody!"

    scene

    scene bg near stage
    show t
    with fade

    t "Hey, Kylie. I hope that wasn't too stressful."

    #darken screen, sophie time

    s "Oh, not stressful at all. It's not like I did this before or anything!"

    k "So Cassandra's first, huh? How are we supposed to communicate?"

    t "Don'tcha worry about that. It was kinda tough on stage, but she's always got her phone with her and she has this shorthand app that helps her communicate."

    t "And I have an idea for next time we're together."

    k "I'm worried, though. I don't know anything about them, really. Is every contestant nervous like this?"

    s "That's not even true, Kylie! You know exactly who Cassandra is at the very least."

    s "And you've definitely met Robin, even if it was a long time ago."

    s "So is the game just written with holes in it, or is Kylie lying? It's hard to tell sometimes."

    t "Oh, god, yeah. Well, except for season four. That girl was just a full-blown serial killer. Made the news and everything."

    k "Well, I'm... I'm..."

    menu:

        s "Hmm... what to say?"

        "In it for the cash":
            t "You say that, but somebody this season is gonna get your heart. I just know it."

        "Looking for The One":
            show t sad 
            t "Oh, honey... you won't have to look. These women are all looking for you."
            ki "Tania's squeezing my hand, lightly. She's... genuinely sad, I think."
            ki "Maybe jealous?"

        "Just looking for a thrill.":
            t "Oh. So you're a sex-pervert?"
            k "No, no, I just... I dunno. I guess I want some excitement in my life before I settle into a cubicle somewhere."
            t "You never know. The cubicle may never come."

            ki "Tania's got a dark streak, doesn't she?"
    # end menu

    t "Don't be too nervous. When the show's finished, you'll never have to worry about money again."

    k "Looking forward to that!"

    t "Yup. So... your first date is with Cassandra. You have a dressing room set up down the hall, and you have about an hour to get ready and get your nerves down."

    k "That might not be enough."

    t "Stop playing this game!"

    ki "Her sudden tonal shift catches me off guard."

    k "Wha?"

    t "You're not believing in yourself. Quit being a victim and be a waifu!"

    k "I'm not a victim, I just... no. You're right!"

    t "Of course!"

    k "Yeah!"

    t "Yeah!"

    s "Getting them hype girl hours! I have no idea what I just said."

    t "Any more questions?"

    $temp = False
    
    while temp == False:
        s "What to say..."

        menu:

            "Seriously, what if I don't click with anyone?":
                t "You will. You've got practice at this."
            
            "What if I want to end the date early?":
                t "The dates will end when they end."

            "How much of this is staged?":
                t "Nothing is real, really."
                s "How philosophical."

            "I have no questions.":
                $ temp = True

        #end of choice

    t "Great. Go get ready, and hey Kylie? Listen. If you need to talk to anybody, I'm around. I've been on this show forever and I'll be happy to listen if you need anything."

    k "Thanks, Tania. That actually means a lot."

    t "No problem. Now, go get ready. I guarantee your life is about to change!"

    scene bg hallway with dissolve

    ki "There's a lot on my mind as I make my way to the dressing room. These women, they're each alluring in their own way. I can definitely appreciate the three-bears strategy."

    show c at right with dissolve

    ki "Cassandra, the silent musician. Her eyes miss nothing, her features are so perfectly Greek, her bearing so beautifully coquettish. I sense some deep well of feeling emanating from her, building up behind a dam of muteness."

    ki "It feels unfair, since I'm a superfan and all, but then maybe my fandom will drive her away?"

    s "See? She's lying to Tania then."

    s "Maybe she wants to appear impartial?"

    show l with dissolve

    ki "Lichelle, the fit girl with the wild smile and hungry eyes. So fierce, so powerful, so dangerous. Some part of me has had a tiny, tiny submissive side and Lichelle just... radiates the power to control."

    s "Such a waste of a bondage opportunity!"

    show r at left with dissolve
    
    ki "Robin, the shadow, graceful and statuesque. Her detachment paired with that accent lend her a ghostly, mysterious vibe that pulls at me, even now as I think about her. Some part of me is afraid of her, but it's hard to express why."

    s "Maybe because I remember her deep down and she's actually a stalker."

    ki "They're all otherworldly in their way. I guess I should feel incredibly lucky that the women in front of me are all so desirable."

    scene bg stage with dissolve

    ki "I should focus on getting ready, though. I wonder what Cassandra has in mind?"

    scene bg black with dissolve

    s "I know we just took a break guys, but I'm getting pretty tired. I'm gonna pee. You guys chill for a sec."

    scene bg brb with dissolve

    pause 2.0

    show t with dissolve

    t "{alpha=0.1}Hey, I'm getting dressed.{/alpha}"
    t "{alpha=0.1}Just a minute, dude!{/alpha}"
    pause 1.0
    t "{alpha=0.1}Alright motherfucker, what do you want?{/alpha}"
    hide t with dissolve

    #dragging metal sound. killing sound? Poor Tania. Don't worry, she'll be okay! This isn't real. Is it?

    #---------------------------------------------------------

    call severInput

    #---------------------------------------------------------

    scene bg hallway with dissolve

    s "Back. So, let's speed through these dates and get back to where we were?"

    scene bg dressing with dissolve

    ki "The dressing room is clean and simple. I'd like to stretch out for a nap, actually. The nerves have taken it out of me."

    ki "There are some clothes in the closet and... I'm a little disappointed. They're all white sundresses, basically cut the same way."

    pause 1.0

    s "Hey! That's different, right? There were different outfits before."

    s "Gasp, dudes! Was the game supposed to crash? Is this part of the plan?"

    s "Oh, okay! Jeez, I wish they'd warned me a little bit. I just about said to hell with it and called it a night."

    scene bg black with dissolve

    ki "An hour passes like nothing, like time somehow folded in on itself."

    s "I know, right?"

    ki "Dressed in the fluttery, pristine whites, I leap to my feet at the sound of a knock on the door."

    show l with dissolve

    l "Hey babe. You ready to go?"

    ki "To my surprise, Lichelle stands before me, a bright grin on her face."

    k "Oh, uh, sure? I guess?"

    l "You were expecting someone else."

    k "Um... well, yeah. I thought Cassandra was first."

    l "She is. Tania just rolled the hell out of her ankle about ten minutes ago, though, so I'm here to whisk you off to the bar or whatever."

    s "Huh. Poor Tania."

    k "Oh. Well... is that okay?"

    l "Should be. Why?"

    k "Well, I thought we weren't supposed to really talk until our date."

    l "You worried I'll try to get in your panties in the car?"

    ki "Fire floods into my face."

    l "Haha! Don't worry babe, I'll wait my turn. Tania and I go way back and I know what she needs from the crew, so it makes sense that I go with."

    k "Okay. Well, in that case, I'm ready whenever you are."

    l "Cool. "

    ki "But her eyes betray her words."

    l "We going? Or you just gonna stand there and tempt me?"

    k "T-tempt you?"

    pause 1.0

    show l happy

    l "I'm just teasing. Get in the car, babe. At least give Cass and spooky-amazon a chance."

    l "Based on the way you're breathing right now, it might already be too late."

    s "She's a no bullstuff kind of girl, guys."

    k "... don't get ahead of yourself."

    ki "I say this, knowing full well I'm on jellied legs, grateful for the wall behind me."

    ki "Lichelle only smiles."

    l "Let's go. Cass'll be waiting."

    s "This show would have to be the worst experience ever. I'm exhausted just reading it."

    s "Just imagine being as thirsty as Kylie seems to be and having all these dream girl archetypes trying to woo you..."

    s "... and also, to have to last through the whole week without acting on anything."

    jump cassDate2