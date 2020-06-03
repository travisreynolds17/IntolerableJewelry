label realWorld2:
    # later, this art needs to be of a snowy fountain outside a town square. 
    scene bg resta with fade

    "Somehow I find myself back outside the bar."

    "Sketch pad in hand, I'm waiting on the benches for something interesting to come by."

    "Something meaningful. Anything."

    "From within the building, I can hear a woman singing, a piano. It's impossible to make out the words."

    "Her voice rings crystal clear, but the words are muddled."

    "Is that snow?"

    "Near the door, a bouncer puffs on a casual cigarette."

    "From the scent, a {i}very{/i} casual cigarette."

    "I find myself scratching her onto paper, in that crisp suit and vest combo common to bouncers, bartenders and stylish lesbians."

    "At least, common to their depictions."

    pause 1.0

    "She wears her hair in neat, tight cornrows. I wonder if she would wear it differently were her job less prone to getting in fights."

    show screen chatterbox
    pause 0.5
    $chat.addmessage(unkn, "I prolly would, babe.")

    pause 0.5
    "Who said that?"

    pause 0.5

    $chat.addmessage(unkn, "Why are you watching us?")

    "Guess it was my imagination."

    pause 0.5

    $chat.addmessage(bong, "help me")

    pause 0.3

    hide screen chatterbox

    "The long-legged woman sets her cushion on the fountain rim."

    "The ice in my drink clinks musically."

    "Her hair spills over her shoulders like papal mercy."

    "Is that snow?"

    "She's undone her buttons, swaying in the light."

    "Tonight, a third. Such magical times. Snowflakes sizzle and die against her chest, leaving little glittering paths that snake between her breasts."

    "I remember my Vonnegut."

    "So it goes."

    pause 0.5

    "Someone's drowning her."

    pause 0.5

    "When did that start?"

    "Her long legs stream up from the fountain, kicking wildly, a climactic eruption of foam and spray billowing from the fountain."

    "There's something inhuman about a drowning. Can't see the victim's face. Only limbs akimbo."

    "Oh. I'm bleeding into my sleeve. I wonder when that started."

    "Could be anyone's arms and legs, really."

    "The bouncer moves like murder."

    "Her beautiful brown arms wrench around the neck, squeezing, a sultry, pythonic embrace."

    "I smell iron."

    "Someone wearing a glittery onyx dress appears from within the bar."

    "I can see her screaming, but... but I can't hear her."

    "Dragging she of the long legs from the fountain."

    "The warm shot tasted mature."

    "She must be freezing in the snow, drenched in fountain water."

    "Beautiful in her pallor, jewelry gleaming."

    "Onyx Dress pushes against her chest."

    "Breaking ribs. Two, more? Oh. CPR."

    "The python relaxes. No one important lies jolting in the snow."

    "Long legs's mouth never erupts in steam and retch."

    "What are those lights?"

    "My sketch pad is ruined."

    "Whose shoes are those? By the fountain."

    "It got wet in the snow."

    "I should've done something."

    "Why does my arm hurt?"

    "She finally looked at me."

    "The bouncer stands over Legs and Onyx."

    "It's your fault my neck hurts, bouncer."

    "I wasn't doing anything."
    
    "I couldn't pull her out."

    "You could have pulled her out."

    "Instead you choked me."

    "You ruined my sketch pad."

    "You let Legs freeze."

    "Even though it's my fault."

    menu:
        "I forgive you":
            "I want you to know."
            "Even if you never hear me."
            "I don't blame you."
            "I only blame me."
            "For everything."
            "If you hate me"
            "I accept that."
            "I hate me, too."
            $stringSever(lichBio)
        
        "I can't forgive you":
            "You could have saved her."
            "You're strong enough."
            "You wanted to hurt me."
            "You're addicted to violence."
            "You left Onyx to do try."
            "Onyx is little."
            "Legs is big."
            "Stupid."
            "I blame you."

    scene bg black with fade

    jump common3
    return
