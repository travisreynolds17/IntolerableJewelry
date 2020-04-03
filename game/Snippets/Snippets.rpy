    # texting. toPost is a list of messages. each will appear at some random point determined by randomXY function.
    python:
      toPost = [
          "She WHAT?",
          "open up",
          "Someone else.",
          "Ma'am, security shows no attacker.",
          "R13:14-15 Police!",
          "Did you do this?",
          "Toxicology confirms it.",
          "Louisa?",
          "oPen THe godDAmnED DOor",
          "you. it was you.",
          "ONE. TWO. BREAK IT!",
          "... I gave her the jewelry.",
          "You're lying.",
          "Door's barricaded!",
          "Sophie, it's me! Open up, please!",
          "Who's voice is that?",
          "Louisa? You're so cold.",
          "I'll lie here with you.",
          "... found them in the bathroom.",
          "Marry me?"
      ]
      postMax = len(toPost)
      i = 0

    while i < postMax:
      $temp = randomXY()

      show text toPost[i]:
          xpos temp[0] ypos temp[1] alpha 0.0 zoom 1
          linear 1.0 alpha 1.0 zoom 5
          linear 0.2 alpha 0 zoom 3
      pause 1.0
      $i += 1

    show text "I love you, Louisa":
        xpos 600 ypos 400 alpha 0.0
        linear 2.0 alpha 0.7
        linear 5.0  alpha 0
    pause