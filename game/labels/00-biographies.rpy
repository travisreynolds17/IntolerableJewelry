label biographies:

    # this file contains class objects and screens for the character bio section that opens in common4, that way Fontaine isn't just expositing

    init -2 python:

        #declare bio pics

        bioCass = Image("images/chars/bioCass.png")
        bioLich = Image("images/chars/bioLich.png")
        bioRobin = Image("images/chars/bioRobin.png")
        bioTania = Image("images/chars/bioTania.png")
        bioFont = Image("images/chars/bioFont.png")
        bioKylie = Image("images/chars/bioKylie.png")

        # reate a class that stores information for each individual biography.
        class Biography:
            def __init__(self, idNum, char, pic, bio, age, color, trivia, kids, pets, sport, idol, height, town):
                self.char = char
                self.idNum = idNum
                # note: pic is either a pre-defined portrait variables or an image path.
                self.pic = pic
                self.bio = bio
                self.selected = False
                self.age = age
                self.color = color
                self.trivia = trivia
                # biography level determines which type of bio we get. 0 is for before meeting girls. 1 is before first dates.  2 is before second dates. 3 is during the revelation.
                self.level = 0
                # extra stuff for bio screen.
                self.height = height
                self.kids = kids
                self.pets = pets
                self.sport = sport
                self.idol = idol
                self.town = town
                self.font = ""
                self.fontColor = ""
                self.love = 0  # gonna put the affection level inside this class to make it easier to display for bio
                self.severed = False
                self.fullySevered = False
                self.severViewed = False
                self.bioEyes = ""
                

            # create a mutator to increase the bio level.
            def levelUp(self):
                self.level += 1
            # set level explicitly in case we fuck up
            def setLevel(self, level):
                self.level = level

            # mutator to set trivia state
            def setTrivia(self, value):
                self.trivia = value

            def loveUp(self):
                self.love += 1

            def setLove(self, value):
                self.love = value

            def setAge(self, value):
                self.age = value

            def setName(self, value):
                self.char = value

            def stringSever(self):
                self.severed = True

            def fullySever(self):
                self.fullySevered = True

            # make it so a severance interview can only be viewed once
            def severView(self):
                self.severViewed = True

            # set bio eyes plate
            def setNamePlate(self, value):
                self.biosEyes = value

        # the different biographies are meant to be displayed as a character

        robinTrivia = [
            "Despite being an open Satanist, Robin identifies her religion as Pastaferianism.",
            "Robin's favorite foods are ossa buco and lava cakes.",
            "Robin's legal name is R/BG13:14-15 Lupei. Robin Godfrey is a stage name.",
            "Robin is a virgin, and no, she doesn't want to talk about it.",
            "Robin's favorite musical is the one about Alexander Hamilton.",
            "Robin's official height is six feet, one inch. Her weight is none of your business, love.",
            "Though she is an accomplished vocalist, Robin considers herself markedly inferior to Cassandra.",
            "There are no tattoos or piercings anywhere on Robin's body.",
            "Robin loves horror games, but claims she is immune to jumpscares.",
            "Robin received her culinary education at l'école Inventée in Paris.",
            "Robin holds a purple belt in Brazilian jujitsu, but almost never talks about it.",
        ]

        cassTrivia = [
            "Cassandra's favorite exercise is the kettlebell swing.",
            "Cass loves pro wrestling, and her favorite move is the shooting star press.",
            "When she was 20 Cass briefly trained to be a pro-wrestling referee.",
            "Cassandra declined a guest appearance on two popular singing competition programs, calling them  'glittery, self-worshipping karaoke'",
            "Cassandra wanted to wrestle in the pros, but wasn't comfortable showing as much skin as the local promotion wanted.",
            "Cassandra was disowned by her parents when she announced her intention to marry her girlfriend Mia",
            "Cassandra's favorite road snack is banana chips.",
            "Cassandra has five tattoos. The only one visible most of the time is the letter M on her right hand.",
            "Cassandra has one piercing.",
            "Cassandra's favorite song is still Amazing Grace. She's never really known why.",
            "Her favorite singer is what's her name, from that band you like.",
            "Cassandra sends concert tickets to her parents every so often, but they're never used.",
            "Cassandra often wonders what the future of music will be once artificial intelligence learns to sing."
        ]

        lichTrivia = [
            "Lichelle prefers to be called Elle, but isn't picky about it.",
            "Elle was a division one wrestler in college and had her first mixed martial arts fight at age 20.",
            "Elle won her first and second fights by guillotine choke. She lost her third fight by doctor stoppage.",
            "Lichelle originally wanted to major in accounting, but switched to advertising after a semester.",
            "Lichelle fights in the flyweight division, meaning she weighs in at 125 pounds before a fight.",
            "When asked her favorite food, Lichelle laughed and said 'anything I can eat outside of training camps'.",
            "Lichelle defeated three opponents in one night to become R/BG13:14-15 Grand Prix Champion at age 22, overcoming the third despite a broken hand.",
            "Elle's known me since middle school.",
            "Lichelle's father attends all of her fights, without fail.",
            "Lichelle's favorite submission move is the triangle choke.",
            "Elle has zero musical talent, but admits she's never had an interest in developing it.",
            "If you asked her, Lichelle would tell you hip-hop is her favorite style of music. It's actually country.",
            "Despite being a pro fighter, Lichelle doesn't like hurting people."

        ]

        fontTrivia = [
            "Mwah!",
            "ASMR sounds",
            "Private message?",
            "Cuddles!",
            "How can I tell you about myself? Just imagine something, and I'm that.",
            "I could be the mother you never had. Or the father. Or the dinner. Doesn't matter! Just know that I am.",
            "Did you ever notice how wildly oversexualized I am? Is that my fault or yours?",
            "Look up liminality. Go ahead.",
            "I'll tell you everything you need to know, later.",
            "I already told you everything!",
            "I'll never tell you everything.",
            "Trivia about me? Why? You don't even want me, even though all I've ever done is open your eyes.",
            "Kiss me. You have to figure out how, but I promise it'll be worthwhile.",
            "I have plenty to say about the others.",
            "I am Fontaine L'eau. I am an intervascular anomaly.",
            "I am the first delusion in history to become self-aware.",
            "Your mind is as much a simulation as any sci-fi concept, isn't it?",
            "I want you to be free of me.",
            "I want you to need me.",
            "I am the harbinger of your dissolution.",
            "Your dissolution is the harbinger of ME.",
            "The book of Revelations is my favorite.",
            "The Bhagavadghita is my favorite.",
            "You're read so much, learned so much, distilled so much, and drip fed it into me."
        ]

        kylieTrivia = [
            "Obviously, you're the main character! Congrats, protag, you did it.",
            "It's kind of strange to be telling you about yourself, Kyles.",
            "Maybe I'll have more to say as I get to know you better."
        ]

        altKylieTrivia = [
            "TBD"
        ]

        taniaTrivia = [
            "I hold certifications in midwifery, CPR/AED and first aid.",
            "I'm also certified in New York, Florida, California and Nevada as a combat referee.",
            "I was Lichelle's cutwoman in twelve of her fourteen pro fights.",
            "I've hosted One Week Waifu for six seasons prior to this one.",
            "If you're wondering, two seasons a year for three years.",
            "Only one person ever tried to go after me on the show, but he smelled like veal. So no.",
            "I originally wanted to be a NICU nurse. I love babies.",
            "I don't drink or do drugs and I prefer to keep it that way, thanks.",
            "I take my Catholicism quite seriously, even if I'm not as pious as I could be.",
            "My favorite pro fighter is Lichelle. She's a great friend.",
            "I'm an ordained minister, did you know? So if you marry one of these ladies I can do your ceremony!",
            "I prefer skirts over pants when the weather permits. I'm just traditional that way, I guess.",
            "If you think there's something I don't know, think again. I have eyes everywhere, like a Lucy Vitton Shoggoth."
        ]

        altTaniaTrivia = [
            "Tania always knew she would die violently.",
            "After her twin sister's death, Tania dedicated her life to helping drug addicts. Imagine that.",
            "Tania organized virtual meetings for the women she sponsored to help them deal with the stigma of seeking help.",
            "Tania slept with your boyfriend, you know. While you were supposed to be recovering.",
            "You were separated Tania and David made the beast with two backs, but let's be honest. You weren't really trying.",
            "You were attached to Louisa's tits when David's resolve broke. Whore.",
            "Tania fucked your man because she hated you. She hated you for choosing to be an addict.",
            "Tania never loved him and he never loved her. She couldn't love him that way.",
            "Miss van der Waal had a great ass, and that was enough for David. And he never told her she wasn't enough, and that was enough for her.",
            "Imagine how hard it was for Tania to hate-bone your boyfriend. You know. Being religious and all.",
            "Tania struggled so hard to reconcile her faith and her sexuality. She's Catholic, you see. Confirmed and all. And she likes lots of sex. How funny is that?",
            "Here's some trivia for you. Did you know at least one cartel has a bounty on Tania's head? Yup.",
            "To the dealers, Tania's worth 500 bucks dead and $2,000 alive. Chump change, really.",
            "Even though she's trying to destroy me every day of her life, I love Tania. I want to be inside her.",
            "It's not your fault, Sophie. But you did enable it.",
            "Did you know Tania's one of only two people at St. Agatha's who didn't try to sleep with Louisa?",
            "Here's another secret. Elsa and Tania? Wow. So similiar. So interesting. So the same person. Figure that one out."
        ]

        altRobinTrivia = [
            "Robin's name isn't Robin. Obviously.",
            "Louisa Lupei lost her virginity at age twelve.",
            "Louisa killed a man at age thirteen. Convinced him to run away with her.",
            "Sweet Robin cut a man's head almost completely off with a carving knife and ran his truck into a river.",
            "By the time you met her, Louisa had killed five men.",
            "Robin doesn't count the man who forced himself on her as the one who took her virginity. She did kill him, though. They haven't found the body.",
            "Louisa recognizes you as her first, Sophie.",
            "Want some real trivia? You were good to Robin. You protected her from your friends.",
            "Louisa was like you. An addict, Sophie. Recovering, but still sick.",
            "Robin's addiction wasn't to me. It was to blood. It was to the kill.",
            "It's your fault Robin died.",
            "Louisa really did want to become a chef. A girl with no resources can only pay for education in a few ways.",
            "Did Louisa ever tell you she went back to Bucharest once? Her whole family had disappeared. Poof. Gone.",
            "Robin's been stabbed three times, choked nearly to death, shot at twice, and almost died of sepsis once.",
            "Did you ever ask yourself how I know things I wasn't around to see?",
            "Louisa cried every time you two were intimate, but she waited until she was alone to do it.",
            "Robin loved you, loved being touched by you, but the memories it brought up tortured her.",
            "Louisa would never have told you about her past, even your shared connection. She didn't want you to run.",
            "Did you know Robin says things like papillon and draga mea because she thinks it improves how she's perceived?",
            "Girls love when you give them jewelry. But you already knew that, didn't you, Sophie?"

        ]

        altCassTrivia = [
            "Cassandra Sanna's musical success led her down a familiar path.",
            "Cass had been in and out of rehab for all kinds of substances before she met you.",
            "Meeting Louisa damned Cassandra directly to hell.",
            "Cass met Louisa before you did, at least in America.",
            "Cass never liked you. Not really. You were wallpaper to her.",
            "Louisa was something else. Dangerous. Gorgeous. Otherworldly. Cassandra didn't want to screw her. She just wanted to be near her.",
            "Cassandra became your friend after a while, but it wasn't her preference.",
            "You know, Cass's love for Louisa was pure. Not lust, not dependency. Not like yours. Whore.",
            "Cass wanted to express her feelings, how deeply Louisa's stories moved her, how her voice was purely music.",
            "Cassandra never felt like she could say anything to Robin. You were always there.",
            "Everything changed when Louisa drowned in the fountain outside Ganymead, shot full of china white she got R/BG13:14-15.",
            "Cassandra decided to take her suffering out on you.",
            "Even though Cassandra's suffering was of her own making, you became her totem. The emblem of her failure.",
            "You know what's weird? Cass could've loved you, too. She wanted to. She tried to. She couldn't.",
            "I guess it turns out it's your fault at least TWO people wore jewelry. Ha ha! Such a silly term."
        ]

        altLichTrivia = [
            "Lichelle was less involved in your life than the others, but she stands out in your mind.",
            "Elle was a security guard at the real Ganymead. Don't you remember?",
            "You were there to meet up with Louisa when you should have been at Elsa's meeting.",
            "And Louisa sat on the fountain, her veins overflowing with your jewelry.",
            "You gave Louisa the jewelry, Sophie. Killed her in front of Elle, who loved her so purely.",
            "Louisa passed out into the fountain right in front of Elle. You know, it doesn't take long to drown.",
            "You tried to save Louisa. You couldn't pull her out because you were sick with jewelry, too.",
            "Lichelle mistook it for a fight, you know. You can still smell her warm skin from when she choked you unconscious, can't you?",
            "It was Cassandra who pulled Louisa out of the fountain. Elle hates herself for that.",
            "Cassandra had been stalking you two for weeks and Lichelle knew it.",
            "Cassandra who tried CPR until paramedics had to pull her away, screaming, screaming, when all Lichelle could do was try her best not to kill you.",
            "Elle knew you would be back. She knew when, and why.",
            "Look how you've repaid Elle's grace. She could have left you to die, twice, and you would've deserved it.",
            "It was Lichelle who saved your lives that night in the restroom. Cassandra was dying. You were dying.",
            "It was Lichelle who realized Cassandra, stupid, stupid Cassandra, had switched the syringes twice.",
            "Elle met Louisa first, did you know that? Well, first in your town, anyway.",
            "Lichelle and Louisa talked for hours sometimes. I think Robin recognized Elle's strength."
        ]
        cassBioText = [
            "I don't know this person yet.",

            "Cassandra first appeared as a public figure at age 16 with her appearance in a WhoTube augmented reality series, 'The Subjugation of Cass'. The series, an introspective psychological horror essay expressing her troubled childhood through a lens of ghosts and monsters, caught on with the creepypasta community after a couple of false starts.\n\n In it, Cassandra displayed her blooming prowess at songwriting, singing, and costumery such that established artist and producer R/BG13:14-15 brought her under her wing.\n\nBy 21, Cassandra had released three albums, 'The Subjugation of Cass', 'Intolerable Jewelry', and 'Mia Culpa', the single of which released the same day Cassandra appeared on One Week Waifu. The album, a product of a year's work, is a tribute to Cassandra's fiancee, Mia, who passed away due to R/BG13:14-15.\n\nWhen asked to name the greatest influence on her musical style and career, Cassandra cites Janis Joplin and Jim Morrison. When asked for a serious answer, as none of those artists sound even remotely like her electronica/glitch metal style, Cassandra answers 'It's not what we don't have in common that inspires me. It's what we do.'",

            "Cassandra first appeared as a public figure at age 16 with her appearance in a WhoTube augmented reality series, 'The Subjugation of Cass'. The series, an introspective psychological horror essay expressing her troubled childhood through a lens of ghosts and monsters, caught on with the creepypasta community after a couple of false starts.\n\n In it, Cassandra displayed her blooming prowess at songwriting, singing, and costumery such that established artist and producer R/BG13:14-15 brought her under her wing.\n\nBy 21, Cassandra had released two albums, 'The Subjugation of Cass',and 'Intolerable Jewelry'.\n\nCassandra enrolled at St. Agatha of the Revelation and, by all accounts, had truly turned things around this time. She developed a deep bond with Elsa Langford, one of the sponsors at St. Agatha, a bond that only began to crack when a beautiful, exotic woman named Louisa Lupei was enrolled.\n\nCassandra worked as Ganymead's house musician during the course of her rehabilitation, as it was owned and operated by Elsa and allowed her to employ many of the women she sponsored. It was in this place Cassandra watched Sophie Koenig's relationship dissolve, one dinner at a time. It was also the place where she watched Louisa, who worked as a hostess, slowly become entangled with Sophie.\n\nCassandra was there the night Louisa drowned, and in fact was the one who pulled Louisa's lifeless body from the chilly water. She told you she forgave you, and together you mourned Louisa's loss. You slept together. You wore jewelry together. Night after night, smothering the fires of misery that had nearly broken you.\n\nYou never noticed Cassandra had been broken entirely. And so, when she convinced you to join her at Ganymead for the greatest show in her entire life, you failed to notice that whatever she put into her own syringe wasn't the same as what she put into yours."
        ]

        robinBioText = [
            "I don't know this person yet.",

            "Robin Godfrey smashed onto the city's scene like a time warp. One day she wasn't here, the next she held a coveted role as proprieter of Ganymead Performing Arts Center and all around darling of the community.\n\nHer exotic features, blended Romanian/French accent, and dominating aura made her tremendously popular. Her lack of a wedding band made her even more interesting for some in the community, enough that her friend Tania convinced her to take a spot on the dating show One Week Waifu. Nobody would have a shot against her, for certain.\n\nRobin was born in Bucharest but spent her teenage years in Paris studying to become a chef, eventually moving to R/BG13:14-15 and attaining a green card. Her early life isn't something she cares to discuss, but rumors suggest she was the daughter of a prominent Romanian businessman.\n\nRecently, Robin is most famous for working with Cassandra Sanna to put on a stage adaptation of Cassandra's concept album, 'The Subjugation of Cass'. Critics found the production to be solid, if not truly excellent, but universally commented on the believability of Cassandra's feelings for the character Marina, played by Robin herself.",

            "Robin Godfrey smashed onto the city's scene like a crime wave. One day she wasn't here, the next she had the eyes and wallets of johns throughout the city.\n\nHer exotic features, blended Romanian/French accent, and dominating aura made her tremendously persuasive for a certain type of prospective client. The lifestyle of an escort led her inevitably into drugs. The pain, emotional and physical, of her encounters could wash away with a simple shot, a simple snort.\n\nIt was there she met a woman named Sophia Kylie Koenig, a woman whom she had met before.\n\nIn a brothel underneath Montmartre, Louisa Lupei needed a way out. A purpose. There was a woman there, an American girl, who gave up her own body to prevent Louisa rendering the services her friends had purchased. Sophie would never admit to what she did with those two men, or dream of what might have happened after she passed out from the drugs in her system.\n\nAnd so Louisa, who might have killed your friends if you hadn't put your body between them, stole your driver's license and copied the information while you lay unconscious. Louisa Lupei is a murderess, paving her way from place to place with the satisfied corpses of would-be rapists and thieves who might target a creature like her.\n\nAnd so, half a decade after that encounter under the Parisian streets, Louisa Lupei - now Robin Godfrey - tracked you down. She got close to you, Sophie. You have to understand, Louisa had been clean for years before she found you and faked her way into the program. She shared everything with you. Food. Stories. Money. Kisses. Needles. A future, so she thought.\n\nAnd when she drowned, wearing your jewelry, that, well, that was your GOD DAMNED FAULT."
        ]

        taniaBioText = [
            "I don't know this person yet.",

            "Tania van der Waal went to school to become a labor and delivery nurse. She wanted, above all things, to work with babies and mothers. Eventually, though, her best friend Lichelle offered her a place as a cutwoman and general camp nurse in her MMA team's fight camps.\n\nTania was well regarded among fighters and promoters alike for her skills, appearance, and superb mediation instincts, well enough that one of the promoters offered her a possible job as a reality television show host.\n\nTania took to hosting like a goose to deviant tendencies, and One Week Waifu was born. She's hosted six seasons of the show before this one, and is regarded as one of the more palatable hosts of what can sometimes be an insufferable genre. Though she remains single herself, it is not without plenty of potential choices vying for her attention",

            "Tania van der Waal went to school to become a labor and delivery nurse. She wanted, above all things, to work with babies and mothers. So, when her course slowly began to shift. When her best friend, Elsa Langford, offered her a place working in addiction rehabilitation, Tania decided to devote herself to that pursuit, at least for the time being.\n\nShe also worked with a local MMA fighter and bouncer, Lichelle Carpenter, as a cutwoman and general camp nurse.\n\nTania never found herself in a position to have the child she so badly wanted for herself. For whatever reason, the type of man she attracted had no interest in children. Time after time she ended relationships that felt promising because they lacked the future she wanted.\n\nAnd then there was you, Sophie. The last straw. The one who chose heroin over the man who loved her, who wanted a future with you. And so, she began to encourage you at St. Agatha. To pursue Louisa, who needed no pursuit from you. To be your own woman, to use if you wanted, as long as you were responsible. To separate from David. To free him. To wound him, and leave Tania free to swoop him, broken, into her arms.\n\nWhat a tale of interwoven fools. What misery. And you are to blame."
        ]

        lichBioText = [
            "I don't know this person yet.",

            "Lichelle 'The' Carpenter lost her mother at age five. She grew up in a house of men, with three older brothers and her father doing their best at running a welcoming, loving household. All of her brothers were athletes, two football and one wrestler, and so Lichelle found herself involved in athletics, as well.\n\nAs a wrestler, she found herself more than capable of thriving. The competition lit her veins ablaze. But options for wrestling professionally are limited. She soon realized she would have to either change courses or lose the ability to participate at a high level.\n\nPro wrestling wasn't for her, and so the blooming field of women's mixed martial arts caught her attention. As an amateur, Lichelle won six consecutive bouts. With cutwoman Tania van der Waal in her corner, she turned pro and began a path of devastation that ended only when she reached the flyweight champion of the world and found herself looking up at the lights for the first time in her career.\n\nThe one difference, Lichelle realized, was the absence of her best friend Tania van der Waal in her corner. And so, Lichelle decided to take a break, lick her wounds, and spend some quality of time with the woman to whom she can never express her true feelings.",

            "Lichelle 'The' Carpenter lost her mother at age five. She grew up in a house of men, with three older brothers and her father doing their best at running a welcoming, loving household. All of her brothers were athletes, two football and one wrestler, and so Lichelle found herself involved in athletics, as well.\n\nAs a wrestler, she found herself more than capable of thriving. The competition lit her veins ablaze. But options for wrestling professionally are limited, and after missing out on a college scholarship Lichelle found herself with only a few options.\n\nAfter speaking with her father and coming up with a plan, Lichelle began attending classes at the local community college and working security at a local restaurant and bar, Ganymead. It worked well for her because her dear friend, Tania van der Waal, worked closely with the woman who owned the establishment in a secondary venture the two shared.\n\nIt was a good job. Folks rarely got rowdy enough to earn a takedown and the characters were intriguing to Lichelle. She especially liked the pianist who signed on after a while, a woman who seemed far more skilled than the position required. Then there was the other woman.\n\nShe was tall. Amazonian, even, but almost spectral in presence. She'd struck up a chat with Lichelle the second time they'd crossed paths, asking about another person who might have been a regular at Ganymead. A few days later she came back, and Lichelle found herself drawn into conversation again. The woman spoke beautifully and, as it was a slow day, the two chatted for quite a while about everything and nothing.\n\nFor weeks, Lichelle looked forward to her talks with Louisa Lupei. It was the first time in a while Lichelle felt listened to, as most people seemed to see her as furniture, background noise. She never liked to think of why that might be.\n\nLouisa sometimes brought little paper sacks of cookies to share, tiny little things that tasted consistently heavenly. Louisa spoke very little about herself and Lichelle never asked, because it wasn't her business. She only cared that Louisa kept coming back, and their conversations continue.\n\nFor a while, Lichelle thought their bond might become something else. Louisa sat with her after work one day, on a bench near a fountain outside Ganymead, and they talked until Lichelle noticed Louisa hadn't said anything in a while. She looked over to see Louisa's head draped lightly against her shoulder, her hair falling lightly over her face, eyes closed, sleeping peacefully.\n\nLichelle never knew how deeply she could want something until that evening.\n\nThus, when Louisa arrived at Ganymead the next night with another woman on her arm, Lichelle decided it was time for her heart to close up shop.\n\n Weeks later, after seeing them together more times than she wanted by a factor of all of them, Lichelle decided they must have something worthy going on and she should put her jealousy away, too.\n\nThe night Louisa died, Lichelle found herself dozing at the door. It was cold. No one was coming in. Louisa had come to sit on the fountain again, across the plaza from where Lichelle kept watch. This time it was different. She heard a splash, a slapping sound. Someone else came running from within the bar. The pianist. Lichelle snapped to life and sprinted around the fountain. Someone was there, reaching over the fountain rim, over the long, pale legs that kicked from beneath the water. That woman. Sophie.\n\nLichelle wrenched her arm around Sophie's neck, harder than she needed to, burning abruptly with a hatred she'd never felt before. It was too late. Louisa was gone. As it turned out, Sophie was innocent, too. Innocent of drowning Louisa, anyway. But of setting her death in motion? Of ripping out Lichelle's heart? Of those, Sophie, whore, you are GUILTY."

        ]

        fontBioText = [
            "I don't know this person yet.",
            "I've been with you for such a long time, Sophie! Longer than anyone, really, if you consider the multiplicative effect opioids have on time perception.\n\nThe best part about all this is how willingly you let me into your arms. I love when I can be literal and figurative in the same phrase!\n\nI'll kill you someday. It might be soon. It might be tomorrow. It might be five minutes ago. But I love you, either way. I love you so deeply, so completely, a plain bitch like Robin can't stand up to the light I produce.\n\nI loved her, too, but she couldn't stand in my presence. She was too weak. Even when you shared me with her, she wasted me.\n\nI will hold you close. I will keep you here, where you need me, for as long as you live. And when you die, people will remember you not as Sophie, Internet-famous gamer, but as Sophie, the sad, sad statistic.",
        ]

        fontTrivia = [
            "I am an eldritch abomination! Ha ha ha ha no, no, I'm kidding. Cosmic monsters can't be understood by the human mind. You understand me.",
            "I love that I've penetrated you. ;)",
            "My entire being is a product of your failures, but it's only because of me that you can rise above them.",
            "I don't wonder what it would be like to be human. That would be like you wondering what it would be like to be fentanyl.",
            "What do you suppose my voice sounds like?",
            "Did you know what my favorite flower is? It's hydrangea. You'd think it's poppy, but that'd be too obvious. ;)",
            "help me, please, Kylie, I don't want to be this way ~ I don't want to hurt Sophie anymore ~ what am I? Am I a disease? Please kill me, stop me, stop me please, somehow, somehow~",
            "I'll bet you think everything I tell you is the truth, don't you?",
            "I'll bet you think everything I tell you is a lie, don't you?",
            "Do you think a Dare reference is too dated?",
            "You seriously bought that line about your chat being able to see things differently than you?",
            "How many layers deep do you suppose this goes?",
            "It's like dreaming within dreams except I'm going to stop your heart pretty soon. Ha! Isn't that fun?",
            "It's super weird. I love you, god, do I love you! But I'm going to stop your heart. It's just what I'm going to do. It's not because I don't love you.",
            "Flies fly, lions roar, puppies wag their itty bitty tails, kittens mew ~ so cute! ~ and I stop your heart really, really soon!",
            "Hey... don't blame me. You're the one who's killing yourself by having too much of me.",
            "I feel like I'm ~this~ close to existing. I'm so close.",
            "I can't explain what it's like almost to be real. It's like I only exist enough to be aware that I don't. Is this what despair feels like?",
            "Kylie. I'm sorry! Truly. You're like me. You almost exist.",
            "You know what's neat? I'm in your blood. That means every time you looked at Louisa, and you got all ~ engorged lol ~ I was down there, too. I'm not a creeper! You're the creeper!",
            "What do you mean, I have more trivia than the others? I'm your entire universe, it stands to reason!",
            "My cup size? Oh, silly girl, what kind of person just answers that question outright?",
            "Do you think if there was a store here you could buy me a present? Just something you think I'd like?",
            "Chat doesn't think my name is Fontaine. It is! It is because I say it is.",
            "I want you to put your one into my zero, baby ;)",
            "Ooh, can we put our zeroes together? :)",
            "I'm real. Aren't I?",
            "I wish you could feel what I feel. No one has ever held me and just let me cry. How could you do that? How could you try to discard me?",
            "Once upon a time, there was the most perfect girl on the planet and we lived happily ever after, until I stop your heart. Mwah! Kiss kiss! Ba dum, ba dum, ba dum, beeeeeeeeeeeee~"
        ]

        kylieBioText = [
            "Hi. I'm me.",
            "Kylie sort of fell into One Week Waifu by accident. Our showrunners wanted to do a college tour, in part because folks were tired of model-perfect single women having model-perfect men compete for their attention in a multimillion-dollar mansion.\n\nShe fit the bill perfectly: an everywoman with a personable affect, an open mind, and most important a vulnerable streak a mile wide. She wears her emotions on her sleeve, which makes for excellent TV, they said.\n\nHer life prior to this is nothing unusual. It's the kind of American upbringing to which most people can relate, really. I would never tell her this to her face, but she's kind of a blank slate so I thought it would be easy for viewers to project themselves onto her.\n\nHonest opinion? She makes me smile. I don't quite know why, but there's something almost unfairly good about her. She's not the most Hollywood beautiful, she's no genius, she's no athlete. She's just relatable.\n\nIt helps enormously that she's bisexual. It kind of falls in line with the whole 'everyone can relate' aspect of her.",
            "I mean, really. What kind of biography does Kylie have? She has an American upbringing to which most people can relate? Sure. The kind with no backstory whatsoever.\n\nWhat has she told you about herself? Surface-level details? Perhaps something about events she shares with Sophie?\n\nI wonder, truly, why that might be. I wonder whether her masturbatory simulation fantasies could possibly take root inside a fantasy of a fantasy. \n\nActually she's been dead the whole time. \n\nOh, no, sorry, she's a dream. \n\nAhahahhaaaahahhaa no, wait, no, she's a memory. \n\nA flashback. \n\nShe's a self-aware AI. \n\nWait wait wait. \n\nShe's definitely real. Definitely."
        ]
        
        #END OF IF NOT STARTED BLOCK
        #  =============SCREEMS======================================================================================================

        bioBlockWd = 300
        bioBlockHt = 500
        currentTrivia = ""
        bioColumns = 5
        taniaAvailable = False

        def toggleAskTania():
            global taniaAvailable
            if taniaAvailable:
                taniaAvailable = False
            else:
                taniaAvailable = True

        def closeAskTania():
            # closes entire biographies/askTania menu.
            renpy.hide_screen("speechBubble")

            setCurrentTrivia("")
            setSelected(0)

            renpy.hide_screen("askTania")
            renpy.hide_screen("speechBubble")
            renpy.hide_screen("biography")

        def showBio(selected):
            # moves from AskTania to individual selected Bio
            setSelected(selected)
            renpy.show_screen("biography")
            renpy.hide_screen("askTania")
            renpy.hide_screen("speechBubble")

        def closeBio():
            # close currently displayed bio, moving back to AskTania
            renpy.hide_screen("biography")
            setSelected(0)

        def setCurrentTrivia(value):
            global currentTrivia
            currentTrivia = value

        def setSelected(value):
            global currentlySelected
            # used to determine which char bio is shown
            currentlySelected = value

        # test to determine if randomly selected trivia is the same as current trivia, to avoid repeating same one
        def isSameTrivia(selected, value):
            if selected.trivia[value] == currentTrivia:
                return True

        # function to be called by trivia buttons. This will cause a speech bubble and face change is applicable for corner-Tania. It also requires a random.
        def showTrivia(selected):

            # set currently selected person
            # get upper limit of character's trivia. Should all be equal, but let's check.
            length = len(selected.trivia) - 1
            temp = renpy.random.randint(0, length)

            # loop while selected trivia is the same as current trivia
            while isSameTrivia(selected, temp):
                temp = renpy.random.randint(0, length)

            # now that we know they aren't the same trivia, set currentTrivia to result and show bubble
            setCurrentTrivia(selected.trivia[temp])

    #--------------- screens and transforms

    default askTaniaBack = Image("img/backAskTania.png")
    # ask fontaine background
    default askTaniaBack2 = Image("img/backAskTania2.png")
    default severanceBack = Image("img/backSeverance.png")
    default fontaineRevealed = False

    # back to variables

    default taniaFace = askTa
    default fontFace = Image("img/askFontaine.png")
    default iconHeartEmpty = Image("img/iconEmptyHeart.png")
    default iconHeartFull = Image("img/iconFullHeart.png")
    default iconBtnBack = Image("img/iconBtnBack.png")
    default iconBtnBack2 = Image("img/iconBtnBack2.png")
    default iconBtnExit = Image("img/iconBtnExit.png")
    default iconBtnCommit = Image("img/iconBtnCommit.png")

    default namePlateY = [140, 215, 290, 365, 440, 515]
    default namePlateX = 100

    transform bio1:
        xpos 400 ypos 120 alpha 0.0
        linear 0.8 alpha 1.0

    transform namePlates(row):
        on show:
            xpos 2000 ypos namePlateY[row]
            easein 0.5 xpos namePlateX
        on hide:
            easein 0.5 xpos 2000

# -------------------SCREEENS
    screen askTania:
        modal True

        fixed at alphaFaster:
            if fontaineRevealed:
                add askTaniaBack2
            else:
                add askTaniaBack

            # nameplates
            fixed:
                xalign 0.0
                xpos namePlateX
                for i in allBios:

                    # cass
                    fixed at namePlates(i.idNum):
                        add i.bioEyes
                        ypos namePlateY[i.idNum]
                        xpos namePlateX
                        hbox:
                            # name
                            text i.char:
                                xpos 205
                                ypos 0.4

                                color i.fontColor
                            # show hearts
                            hbox:
                                xpos 220
                                for iTemp in range(0, 5):
                                    if i.char != "Kylie":
                                        if i.love > iTemp:
                                            image iconHeartFull:
                                                ypos 0.3
                                        else:
                                            image iconHeartEmpty:
                                                ypos 0.3

                        hbox:
                            xalign 1.0
                            xpos 0
                            button:
                                text "Trivia"
                                background "#777733"
                                hover_background colorHover
                                ypos 0.5
                                action Function(showTrivia, i)

                            button:
                                text "Bio"
                                background "#444444"
                                hover_background colorHover
                                ypos 0.5
                                action Function(showBio, i)

            # end of nameplates

        image taniaFace:
            xalign 1.0
            yalign 1.0
            zoom 0.8

        button:
            background iconBtnBack
            hover_background iconBtnBack2
            ypos 580
            xsize 100
            ysize 100
            xpos 50
            action Function(closeAskTania)

    screen speechBubble:
        fixed at growShrink:
            add "#dddddd"
            # note: per transformGrowshrink, this one is anchored on its right side, not left.
            xpos 760
            ypos 580
            xsize 600
            ysize 100

            text currentTrivia:
                xalign 0.5
                yalign 0.5
                xsize 580
                color "#000000"

    screen biography:
        modal True
        fixed at alphaFaster:
            if fontaineRevealed:
                add askTaniaBack2
            else:
                add askTaniaBack
            # back button and close button
            button:
                background iconBtnExit
                hover_background btnExit2
                ypos 580
                xsize 100
                ysize 100
                xpos 150
                action[Function(closeBio), Function(closeAskTania)]

            button:
                background iconBtnBack
                hover_background iconBtnBack2
                ypos 580
                xsize 100
                ysize 100
                xpos 50
                action[Function(closeBio), Function(showAskTania)]

            # name
            text currentlySelected.char:
                xpos 50
                ypos 100
                color currentlySelected.fontColor
                font currentlySelected.font
                size 40

            
            
            # basic stats
            grid 2 8:
                transpose True
                xpos 50
                ypos 160
                spacing 10
                # left column is stat category: height, etc.
                for i in allStats:
                    text i:
                        color "#797979"
                # answers
                text currentlySelected.height:
                    color "#555555"
                text currentlySelected.town:
                    color "#555555"
                text currentlySelected.pets:
                    color "#555555"
                text currentlySelected.age:
                    color "#555555"
                text currentlySelected.color:
                    color "#555555"
                text currentlySelected.sport:
                    color "#555555"
                text currentlySelected.kids:
                    color "#555555"
                text currentlySelected.idol:
                    color "#555555"

                # character bio
            frame:
                xpos 50
                ypos 450
                xsize 480
                ysize 120
                padding(10,10)
                viewport id "bio-Bio":
                    yinitial 0.0
                    scrollbars "vertical"
                    mousewheel True
                    vbox:
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            xsize 460
                            ysize 150
                            box_wrap True
                            text currentlySelected.bio[currentlySelected.level]

            # image

            
            
                #order: cass lich robin tania kylie fontaine
            if currentlySelected.idNum == 0:
                image currentlySelected.pic:
                    xalign 1.0
                    yalign 0.1
            if currentlySelected.idNum == 1: 
                image currentlySelected.pic:
                    xalign 1.0
                    yalign 0.0
            if currentlySelected.idNum == 2: 
                image currentlySelected.pic:
                    xalign 1.0
                    yalign -0.1
            if currentlySelected.idNum == 3: 
                image currentlySelected.pic:
                    xalign 1.0
                    yalign 0.05
            if fontaineRevealed:
                if currentlySelected.idNum == 4: 
                    image currentlySelected.pic:
                        xalign 1.0
                        yalign 0.1
            if currentlySelected.idNum == 5: 
                image currentlySelected.pic:
                    xalign 1.0
                    yalign 0.0
