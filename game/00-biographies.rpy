# this file contains class objects and screens for the character bio section that opens in common4, that way Liv isn't just expositing

python:

    class Biography:
        def __init__(self, char, pic, bio, age, color, trivia):
            self.char = char
            #note: pic is either a pre-defined portrait variables or an image path. 
            self.pic = pic
            self.bio = bio
            self.selected = False
            self.age = 0
            self.color = ""
            self.trivia = ""
            self.level = 0 # biography level determines which type of bio we get. 0 is for before meeting girls. 1 is before first dates.  2 is before second dates. 3 is during the revelation.

    #define default bios. Have 'em for elsa and David, prob won't use
    default cassBio = Biography("Cassandra Sanna", "", "", 22, "Ultramarine", "Cassandra declined a guest appearance on two popular singing competition programs, calling them, 'glittery, self-worshipping karaoke'.")
    default lichBio = Biography("Lichelle Carpenter", "", "", 24, "Carmine Red", "Lichelle defeated three opponents in one night to become R13:14-15 Grand Prix Champion at age 22, overcoming the third despite a broken hand.")
    default robinBio = Biography("Robin Godfrey", "", "", 24, "Royal Purple", "Despite being an open Satanist, Robin identifies her religion as Pastaferianism.")
    default livBio = Biography("Oblivion Leibniz", "", "", "R13:14-15", "China White", "Oblivion is known by many names, but prefers 'Liv'. She loves you more than anyone ever could.")
    default taniaBio = Biography("Tania van der Waal", "", "", 26, "Tuscan Sun", "Tania holds certifications in midwifery, CPR/AED and first aid, and also is an ordained minister.")

    # the different biographies are meant to be displayed as a character
    
    temp = [
        "I don't know this person yet.",
        "Cassandra first appeared as a public figure at age 16 with her appearance in a WhoTube augmented reality series, 'The Subjugation of Cass'. The series, an introspective psychological horror essay expressing her troubled childhood through a lens of ghosts and monsters, caught on with the creepypasta community after a couple of false starts.\n In it, Cassandra displayed her blooming prowess at songwriting, singing, and costumery such that established artist and producer R13:14-15 brought her under her wing.\nBy 21, Cassandra had released three albums, 'The Subjugation of Cass', 'Intolerable Jewelry', and 'Mia Culpa', the single of which released the same day Cassandra appeared on One Week Waifu. The album, a product of a year's work, is a tribute to Cassandra's fiancee, Marina, who passed away due to R13:14-15.\nWhen asked to name the greatest influence on her musical style and career, Cassandra cites Janis Joplin, Jim Morrison, and Jimi Hendrix. When asked for a serious answer, as none of those artists sound even remotely like her electronica/glitch metal style, Cassandra answers 'It's not what we don't have in common that inspires me. It's what we do.'"
        ""
    ]