label biographies:

    # this file contains class objects and screens for the character bio section that opens in common4, that way Liv isn't just expositing

    init python:

        class Biography:
            def __init__(self, char, pic, bio, age, color, trivia):
                self.char = char
                #note: pic is either a pre-defined portrait variables or an image path. 
                self.pic = pic
                self.bio = bio
                self.selected = False
                self.age = 0
                self.color = ""
                self.trivia = []
                self.triviaPointer = 0
                self.level = 0 # biography level determines which type of bio we get. 0 is for before meeting girls. 1 is before first dates.  2 is before second dates. 3 is during the revelation.

        

        # the different biographies are meant to be displayed as a character

        robinTrivia = [
            "Despite being an open Satanist, Robin identifies her religion as Pastaferianism.",
            "Robin's favorite foods are ossa buco to eat and lava cakes to prepare.",
            "Robin's legal name is R13:14-15 Lupei. Robin Godfrey is a stage name.",
            "Robin is a virgin, and no, she doesn't want to talk about it.",
            "Her favorite musical is the one about Alexander Hamilton.",
            "Robin's official height is six feet, one inch. Her weight is none of your business, love.",
            "Though she is an accomplished vocalist, Robin considers herself markedly inferior to Cassandra.",
            "There are no tattoos or piercings anywhere on Robin's body.",
            "Robin loves horror games, but claims she is immune to jumpscares.",
            "She received her culinary education at l'école Inventée in Paris.",
            "Robin holds a purple belt in Brazilian jujitsu, but almost never talks about it.",
        ]

        cassTrivia = [
            "Cassandra's favorite exercise is the kettlebell swing.",
            "Cass loves pro wrestling, and her favorite move is the shooting star press.",
            "When she was 20 Cass briefly trained to be a pro-wrestling referee.",
            "Cassandra declined a guest appearance on two popular singing competition programs, calling them, 'glittery, self-worshipping karaoke'"
            "She wanted to wrestle, but wasn't comfortable showing as much skin as the local promotion wanted.",
            "She was disowned by her parents when she announced her intention to marry Marina",
            "Cassandra's favorite road snack is banana chips.",
            "Cassandra has five tattoos. The only visible one most of the time is the letter M on her right hand.",
            "She has one piercing.",
            "She would tell you her favorite movie is Moonlight, but she's never really sure.",
            "Her favorite singer is what's her name, from that band you like.",
            "Cassandra sends concert tickets to her parents every so often, but they're never used.",
            "She often wonders what the future of music will be once artificial intelligence learns to sing."
        ]

        lichTrivia = [
            "Lichelle prefers to be called Elle, but isn't picky about it.",
            "She was a division one wrestler in college and had her first mixed martial arts fight at age 20.",
            "She won her first and second fights by guillotine choke. She lost her third fight by doctor stoppage.",
            "Lichelle originally wanted to major in accounting, but switched to advertising after a semester.",
            "Lichelle fights in the flyweight division, meaning she weighs in at 125 pounds.",
            "When asked her favorite food, Lichelle laughed and said 'anything I can eat outside of training camps'.",
            "Lichelle defeated three opponents in one night to become R13:14-15 Grand Prix Champion at age 22, overcoming the third despite a broken hand.",
            "She's known Tania since middle school.",
            "Lichelle's father attends all of her fights, without fail.",
            "Lichelle's favorite submission move is the triangle choke.",
            "She has zero musical talent, but admits she's never had an interest in developing it.",
            "If you asked her, Lichelle would tell you rap is her favorite style of music. It's actually country.",
            "Despite being a pro fighter, Lichelle doesn't like hurting people",

        ]

        taniaTrivia = [
            "Tania holds certifications in midwifery, CPR/AED and first aid.",
            "She's also certified in New York, Florida, California and Nevada as a cutwoman.",
            "Tania was Lichelle's cutwoman in twelve of her fourteen pro fights.",
            "Tania has hosted One Week Waifu for six seasons prior to this one.",
            "Only one contestant has attempted to pursue Tania, but Tania shot it down immediately.",
            "Tania originally wanted to be a NICU nurse.",
            "She's never drank alcohol or done any drug and prefers to keep it that way, thanks.",
            "Tania only has nine and a half fingers after a severe car accident.",
            "Her favorite fighter is Lichelle. Her second favorite is Rocky Balboa.",
            "Tania is an ordained minister and oversaw her sister's wedding and funeral.",
            "She prefers skirts over pants when the weather permits.",
            "Tania always knows more than she lets on."
        ]

        altTaniaTrivia = [
            "Tania always knew she would die violently.",
            "After her sister's death, she dedicated her life to helping drug addicts.",
            "She organized virtual meetings for the women she sponsored to help them deal with the stigma of seeking help.",
            "Tania slept with your boyfriend, you know. While you were supposed to be recovering.",
            "Technically you were separated, but let's be honest. You weren't really trying.",
            "You were attached to Louisa's tits by then. Whore.",
            "Tania fucked him because she hated you. She hated you for choosing to be an addict.",
            "She never loved him and he never loved her, but they needed something for their mutual suffering.",
            "She had a great ass, and that was enough for him. And he never told her she wasn't enough, and that was enough for her.",
            "It's not your fault, Sophie. But you did enable it."
        ]

        altRobinTrivia = [
            "Robin's name isn't Robin. Obviously.",
            "Louisa Lupei lost her virginity at age twelve.",
            "She killed that man at age thirteen. Convinced him to run away with her.",
            "She cut his head almost completely off and left him in a burned truck.",
            "By the time you met her, she had killed five men.",
            "She doesn't count the man who forced himself on her as the one who took her virginity. She doesn't recognize his existence.",
            "She recognizes you as her first. Want some real trivia?",
            "You were good to her. You protected her from your friends.",
            "But she was like you. An addict, Sophie. Recovering, but still sick.",
            "And it's your fault she died."
            
        ]

        altCassTrivia = [
            "Cassandra Sanna's musical success led her down a familiar path.",
            "She'd been in and out of rehab for all kinds of substances before she met you.",
            "Well. The important part was she met Louisa.",
            "Except you and Louisa were already sleeping together, weren't you.",
            "She never liked you. Not really. You were wallpaper to her.",
            "But Louisa was something else. Dangerous. Gorgeous. Otherworldly.",
            "She became your friend after a while, but it wasn't her preference.",
            "She loved Louisa, though. She wanted to express her feelings.",
            "But she never felt like she could say anything.",
            "And when Louisa drowned in the fountain outside Ganymead, shot full of china white she got from you,"
            "Cassandra decided to take her suffering out on you.",
            "Even though her suffering was of her own making."
        ]

        altLichTrivia = [
            "Lichelle was less involved in your life than the others, but she stands out in your mind.",
            "She was a security guard at Ganymead. Don't you remember?",
            "When you were there to meet up with Louisa when you should have been at Elsa's meeting.",
            "And Louisa sat on the fountain, her veins overflowing with jewelry.",
            "You gave her the jewelry, Sophie.",
            "She passed out into the fountain. You know, it doesn't take long to drown.",
            "But you tried to save her. But you couldn't pull her out.", 
            "Lichelle mistook it for a fight, you know. You can still smell her warm skin from when she choked you unconscious, can't you?",
            "It was Cassandra who pulled Louisa out of the fountain.",
            "Cassandra who had been stalking you two for weeks.",
            "Cassandra who tried CPR until paramedics had to pull her away, screaming, screaming.",
            "Cassandra who realized what happened and cast her sights, in an instant, on you.",
            "And it was Lichelle who found the two of you in Ganymead's bathroom stall.",
            "It was Lichelle who saved your life that night.",
            "And look how you've repaid her."
        ]
        cassBioText = [
            "I don't know this person yet.",

            "Cassandra first appeared as a public figure at age 16 with her appearance in a WhoTube augmented reality series, 'The Subjugation of Cass'. The series, an introspective psychological horror essay expressing her troubled childhood through a lens of ghosts and monsters, caught on with the creepypasta community after a couple of false starts.\n In it, Cassandra displayed her blooming prowess at songwriting, singing, and costumery such that established artist and producer R13:14-15 brought her under her wing.\nBy 21, Cassandra had released three albums, 'The Subjugation of Cass', 'Intolerable Jewelry', and 'Mia Culpa', the single of which released the same day Cassandra appeared on One Week Waifu. The album, a product of a year's work, is a tribute to Cassandra's fiancee, Marina, who passed away due to R13:14-15.\nWhen asked to name the greatest influence on her musical style and career, Cassandra cites Janis Joplin and Jim Morrison. When asked for a serious answer, as none of those artists sound even remotely like her electronica/glitch metal style, Cassandra answers 'It's not what we don't have in common that inspires me. It's what we do.'",

            "Cassandra first appeared as a public figure at age 16 with her appearance in a WhoTube augmented reality series, 'The Subjugation of Cass'. The series, an introspective psychological horror essay expressing her troubled childhood through a lens of ghosts and monsters, caught on with the creepypasta community after a couple of false starts.\n In it, Cassandra displayed her blooming prowess at songwriting, singing, and costumery such that established artist and producer R13:14-15 brought her under her wing.\nBy 21, Cassandra had released two albums, 'The Subjugation of Cass',and 'Intolerable Jewelry'.\nCassandra enrolled at St. Agatha of the Revelation and, by all accounts, had truly turned things around this time. She developed a deep bond with Elsa Langford, one of the sponsors at St. Agatha, a bond that only began to crack when a beautiful, exotic woman named Louisa Marina Lupei was enrolled.\nCassandra worked as Ganymead's house musician during the course of her rehabilitation, as it was owned and operated by Elsa and allowed her to employ many of the women she sponsored. It was in this place Cassandra watched Sophie Koenig's relationship dissolve, one dinner at a time. It was also the place where she watched Louisa, who worked as a hostess, slowly become entangled with Sophie.\nCassandra was there the night Louisa drowned, and in fact was the one who pulled Louisa's lifeless body from the chilly water. She told you she forgave you, and together you mourned Louisa's loss. You slept together. You wore jewelry together. Night after night, smothering the fires of misery that had nearly broken you.\nYou never noticed Cassandra had been broken entirely. And so, when she convinced you to join her at Ganymead for the greatest show in her entire life, you failed to notice that whatever she put into her own syringe wasn't the same as what she put into yours."
        ]

        robinBioText = [
            "I don't know this person yet.",

            "Robin Godfrey smashed onto the city's scene like a time warp. One day she wasn't here, the next she held a coveted role as proprieter of Ganymead Performing Arts Center and all around darling of the community.\nHer exotic features, blended Romanian/French accent, and dominating aura made her tremendously popular. Her lack of a wedding band made her even more interesting for some in the community, enough that her friend Tania convinced her to take a spot on the dating show One Week Waifu.Nobody would have a shot against her, for certain.\nRobin was born in Bucharest but spent her teenage years in Paris studying to become a chef, eventually moving to R13:14-15 and attaining a green card. Her early life isn't something she cares to discuss, but rumors suggest she was the daughter of a prominent Romanian businessman.\nRecently, Robin is most famous for working with Cassandra Sanna to put on a stage adaptation of Cassandra's concept album, 'The Subjugation of Cass'. Critics found the production to be solid, if not truly excellent, but universally commented on the believability of Cassandra's feelings for the character Marina, played by Robin herself.",

            "Robin Godfrey smashed onto the city's scene like a crime wave. One day she wasn't here, the next she had the eyes and wallets of johns throughout the city.\nHer exotic features, blended Romanian/French accent, and dominating aura made her tremendously persuasive for a certain type of prospective client. The lifestyle of an escort led her inevitably into drugs. The pain, emotional and physical, of her encounters could wash away with a simple shot, a simple snort.\nIt was there she met a woman named Sophia Kylie Koenig, a woman whom she had met before.\nIn a brothel underneath Montmartre, Louisa Lupei needed a way out. A purpose. There was a woman there, an American girl, who gave up her own body to prevent Louisa rendering the services her friends had purchased. Sophie would never admit to what she did with those two men, or dream of what might have happened after she passed out from the drugs in her system.\nAnd so Louisa, who might have killed your friends if you hadn't put your body between them, stole your driver's license and copied the information while you lay unconscious. Louisa Lupei is a murderess, paving her way from place to place with the satisfied corpses of would-be rapists and thieves who might target a creature like her.\nAnd so, half a decade after that encounter under the Parisian streets, Louisa Lupei - now Robin Godfrey - tracked you down. She got close to you, Sophie. You have to understand, Louisa had been clean for years before she found you and faked her way into the program. She shared everything with you. Food. Stories. Money. Kisses. Needles. A future, so she thought.\nAnd when she drowned, wearing your jewelry, that, well, that was your GOD DAMNED FAULT."
        ]

        taniaBioText = [
            "I don't know this person yet.",

            "Tania van der Waal went to school to become a labor and delivery nurse. She wanted, above all things, to work with babies and mothers. Eventually, though, her best friend Lichelle offered her a place as a cutwoman and general camp nurse in her MMA team's fight camps.\nTania was well regarded among fighters and promoters alike for her skills, appearance, and superb mediation instincts, well enough that one of the promoters offered her a possible job as a reality television show host.\nTania took to hosting like a goose to deviant tendencies, and One Week Waifu was born. She's hosted six seasons of the show before this one, and is regarded as one of the more palatable hosts of what can sometimes be an insufferable genre. Though she remains single herself, it is not without plenty of potential choices vying for her attention",

            "Tania van der Waal went to school to become a labor and delivery nurse. She wanted, above all things, to work with babies and mothers. So, when her course slowly began to shift. When her best friend, Elsa Langford, offered her a place working in addiction rehabilitation, Tania decided to devote herself to that pursuit, at least for the time being.\nShe also worked with a local MMA fighter and bouncer, Lichelle Carpenter, as a cutwoman and general camp nurse.\nTania never found herself in a position to have the child she so badly wanted for herself. For whatever reason, the type of man she attracted had no interest in children. Time after time she ended relationships that felt promising because they lacked the future she wanted.\nAnd then there was you, Sophie. The last straw. The one who chose heroin over the man who loved her, who wanted a future with you. And so, she began to encourage you at St. Agatha. To pursue Louisa, who needed no pursuit from you. To be your own woman, to use if you wanted, as long as you were responsible. To separate from David. To free him. To wound him, and leave Tania free to swoop him, broken, into her arms.\nWhat a tale of interwoven fools. What misery. And you are to blame."
        ]

        lichBioText = [
            "I don't know this person yet.",

            "Lichelle 'The' Carpenter lost her mother at age five. She grew up in a house of men, with three older brothers and her father doing their best at running a welcoming, loving household. All of her brothers were athletes, two football and one wrestler, and so Lichelle found herself involved in athletics, as well.\nAs a wrestler, she found herself more than capable of thriving. The competition lit her veins ablaze. But options for wrestling professionally are limited. She soon realized she would have to either change courses or lose the ability to participate at a high level.\nPro wrestling wasn't for her, and so the blooming field of women's mixed martial arts caught her attention. As an amateur, Lichelle won six consecutive bouts. With cutwoman Tania van der Waal in her corner, she turned pro and began a path of devastation that ended only when she reached the flyweight champion of the world and found herself looking up at the lights for the first time in her career.\nThe one difference, Lichelle realized, was the absence of her best friend Tania van der Waal in her corner. And so, Lichelle decided to take a break, lick her wounds, and spend some quality of time with the woman to whom she can never express her true feelings.",

            "Lichelle 'The' Carpenter lost her mother at age five. She grew up in a house of men, with three older brothers and her father doing their best at running a welcoming, loving household. All of her brothers were athletes, two football and one wrestler, and so Lichelle found herself involved in athletics, as well.\nAs a wrestler, she found herself more than capable of thriving. The competition lit her veins ablaze. But options for wrestling professionally are limited, and after missing out on a college scholarship Lichelle found herself with only a few options.\nAfter speaking with her father and coming up with a plan, Lichelle began attending classes at the local community college and working security at a local restaurant and bar, Ganymead. It worked well for her because her dear friend, Tania van der Waal, worked closely with the woman who owned the establishment in a secondary venture the two shared.\nIt was a good job. Folks rarely got rowdy enough to earn a takedown and the characters were intriguing to Lichelle. She especially liked the pianist who signed on after a while, a woman who seemed far more skilled than the position required. Then there was the other woman.\nShe was tall. Amazonian, even, but almost spectral in presence. She'd struck up a chat with Lichelle the second time they'd crossed paths, asking about another person who might have been a regular at Ganymead. A few days later she came back, and Lichelle found herself drawn into conversation again. The woman spoke beautifully and, as it was a slow day, the two chatted for quite a while about everything and nothing.\nFor weeks, Lichelle looked forward to her talks with Louisa Lupei. It was the first time in a while Lichelle felt listened to, as most people seemed to see her as furniture, background noise. She never liked to think of why that might be.\nLouisa sometimes brought little paper sacks of cookies to share, tiny little things that tasted consistently heavenly. Louisa spoke very little about herself and Lichelle never asked, because it wasn't her business. She only cared that Louisa kept coming back, and their conversations continue.\nFor a while, Lichelle thought their bond might become something else. Louisa sat with her after work one day, on a bench near a fountain outside Ganymead, and they talked until Lichelle noticed Louisa hadn't said anything in a while. She looked over to see Louisa's head draped lightly against her shoulder, her hair falling lightly over her face, eyes closed, sleeping peacefully.\nLichelle never knew how deeply she could want something until that evening.\nThus, when Louisa arrived at Ganymead the next night with another woman on her arm, Lichelle decided it was time for her heart to close up shop.\n Weeks later, after seeing them together more times than she wanted by a factor of all of them, Lichelle decided they must have something worthy going on and she should put her jealousy away, too.\nThe night Louisa died, Lichelle found herself dozing at the door. It was cold. No one was coming in. Louisa had come to sit on the fountain again, across the plaza from where Lichelle kept watch. This time it was different. She heard a splash, a slapping sound. Someone else came running from within the bar. The pianist. Lichelle snapped to life and sprinted around the fountain. Someone was there, reaching over the fountain rim, over the long, pale legs that kicked from beneath the water. That woman. Sophie.\nLichelle wrenched her arm around Sophie's neck, harder than she needed to, burning abruptly with a hatred she'd never felt before. It was too late. Louisa was gone. As it turned out, Sophie was innocent, too. Innocent of drowning Louisa, anyway. But of setting her death in motion? Of ripping out Lichelle's heart? Of those, Sophie, whore, you are GUILTY."

        ]

        #define default bios. Do this at end so bio variables will be in place
        cassBio = Biography("Cassandra Sanna", "img/cassBio.png", "", 22, "Ultramarine", [])
        lichBio = Biography("Lichelle Carpenter", "", "", 25, "Carmine Red", [])
        robinBio = Biography("Robin Godfrey", "", "", 24, "Royal Purple", [])
        livBio = Biography("Oblivion Leibniz", "", "", "R13:14-15", "China White", "Oblivion is known by many names, but prefers 'Liv'. She loves you more than anyone ever could.")
        taniaBio = Biography("Tania van der Waal", "", "", 26, "Tuscan Sun", [])

        allBios = [cassBio, lichBio, robinBio, livBio, taniaBio]

        #=============SCREEMS======================================================================================================

        bioBlockWd = 300
        bioBlockHt = 500
        bioBlockPointer = 0 # holds which bio block is currently highlighted. May not need.
        currentTrivia = "" #holds trivia to be shown at center screen or somewhere else later
        currentBio = "" #holds bio to be showed in full-screen biography frame

        bioBlocks = []

        def showTrivia(person, direction):
            global person.triviaPointer
            currentTrivia = person.trivia[triviaPointer]
            renpy.show(currentTrivia, center)
            if direction == "plus":
                person.triviaPointer += 1
            else:
                person.triviaPointer -= 1

        def closeBioScreen():
            currentTrivia = 0
            for i in allBios:
                i.triviaPointer = 0
            #close all screens. Maybe in a list with a for loop?

        def summonBio(person):
            currentBio = person
            renpy.show_screen()

        
                
    #--------------- screens and transforms

    transform bio1:
        xpos 400 ypos 120 alpha 0.0
        linear 0.8 alpha 1.0


    screen biographies:
        modal True
        #cassandra
        fixed at bio1:
            text cassBio.char:
                xalign 0.1
                yalign 0.1
            image cassBio.pic:
                xalign 0.8
                yalign 0.8
            hbox:
                xalign 0.1
                yalign 0.8
                button:
                    #placeholder, use icons later
                    text "B"
                    action Function(showTrivia, cassBio, "minus")
                text "Trivia"
                button:
                    text "F"
                    action Function(showTrivia, cassBio, "plus")
                button:
                    text "Bio"
                    action Function(summonBio, cassBio)

    screen showBio:

        frame:
            viewport id "bioBox":

                mousewheel True
                side_area(10, 0, bioBlockWd, bioBlockHt)
                scrollbars "vertical"

                vbox:
                    for i in currentBio:
                        text i.char:
                            font nameFont
                        text i.bio:
                            font messageFont