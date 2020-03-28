label c5taniaInterview:
    
    k "What about Tania?"

    r "She'll be back. She always comes back."

    k "What does that mean?"

    l "You mean we have to see that every time this goes around?"

    c "< Tania's got some kind of special connection with the entity. >"

    c "< That's what we figure anyway. >"

    r "Tania is always the victim."

    c "< Every time. >"

    k "But why?"

    r "Guessing at the entity's motivation is fruitless, darling."

    k "I've never seen anything like what happened to her."

    k "... I guess I wouldn't have."

    l "It was awful."

    c "< What happened to her this time? >"

    k "I don't wanna think about it."

    c "< That bad, huh? >"

    r "I'm sorry you had to see something awful, papillon. And you saw it too, Lichelle?"

    l "Yeah. She got... ugh. She was in pieces."

    r "Oh, Tania. She never reaches this point,  you know. We've never been able to speak to her without the entity's influence guiding her."

    k "... are we sure she's one of us? Like... not a computer program?"

    "Robin opens her mouth to speak, but stops."

    "Cassandra glances at her, to Lichelle, and back."

    r "I... actually, I don't know."

    c "< Holy shit. I never even thought about it. >"

    l "I got no answers, girls."

    r "I suppose she could be part of all this. We have no way of knowing."

    if loveTania > 3:
        k "I liked her a lot."
        c "< She is delightful in her way.>"
        k "... I mean, like... a lot."
        r "Oh."
        l "Oh."
        c "..."
        k "I don't know if I'd rather she was just a program."
        r "Either she's fiction designed to manipulate us or she's the most tortured soul of all."
        k "She'll for sure be back?"
        c "< She's always been here when I have. Well. Her and Robin.>"
        k "... you're real, right Robin?"
        r "I hope so. I suppose none of us have any way of knowing, do we?"
        l "I don't wanna think about it. It's making my head hurt."
        
    
    $taniaDone[0] = True
