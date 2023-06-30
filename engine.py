from Human_month import Human_month
from Word import Word
from Leet_upper import Leet_upper
from Leet_lower import Leet_lower
from Lowercase import Lowercase
from Uppercase import Uppercase
from First_letter_uppercase import First_letter_uppercase
from Strip_accents import Strip_accents
from Date import Date
from itertools import permutations, combinations

class Engine:
    
    def __init__(self, words, dates, options):
        self.options = options
        self.words = words
        self.dates = dates
        self.array_possibilities = []
        self.tmp_array = []
        self.run()

    def run(self):
        if self.options["word"]:
            self.array_possibilities.append(Word(self.words).display_word())

            if self.options["leet_upper"]:
                self.array_possibilities.append(Leet_upper(self.words).leet_upper())
            if self.options["leet_lower"]:
                self.array_possibilities.append(Leet_lower(self.words).leet_lower())
            if self.options["lowercase"]:
                self.array_possibilities.append(Lowercase(self.words).lowercase())
            if self.options["uppercase"]:
                self.array_possibilities.append(Uppercase(self.words).uppercase())
            if self.options["first_letter_uppercase"]:
                self.array_possibilities.append(First_letter_uppercase(self.words).first_letter_uppercase())
            if self.options["Strip_accent"]:
                self.array_possibilities.append(Strip_accents(self.words).strip_accents())

        if self.options["date"]:

            self.tmp_array.append(Date(self.dates[0]).display_date())
            if self.options["jour"]:
                self.tmp_array.append(Date(self.dates[0]).display_day())
            if self.options["mois"]:
                self.tmp_array.append(Date(self.dates[0]).display_month())
            if self.options["annee"]:
                self.tmp_array.append(Date(self.dates[0]).display_year())
            if self.options["langue"]:
                if self.options["fr"]:
                    self.tmp_array.append(Human_month(self.dates[0]).display_human_month('fr'))
                else:
                    self.tmp_array.append(Human_month(self.dates[0]).display_human_month())
            self.array_possibilities.append(self.tmp_array)

# Demande des mots à l'utilisateur
words = input("Entrez les mots (séparés par des espaces) : ").split()

# Demande de date à l'utilisateur
dates = input("Entrez les dates (dd/mm/yyyy) : ").split()

# Demande des options à afficher
options = {
    "word": input("Afficher les mots ? (O/N) : ").lower() == "o",
    "date": input("Afficher les dates ? (O/N) : ").lower() == "o"
}

if options["word"]:
    options["leet_upper"] = input("Afficher les mots en Leet (majuscule) ? (O/N) : ").lower() == "o"
    options["leet_lower"] = input("Afficher les mots en Leet (minuscule) ? (O/N) : ").lower() == "o"
    options["lowercase"] = input("Afficher les mots en minuscules ? (O/N) : ").lower() == "o"
    options["uppercase"] = input("Afficher les mots en majuscules ? (O/N) : ").lower() == "o"
    options["first_letter_uppercase"] = input("Afficher les mots avec la première lettre en majuscule ? (O/N) : ").lower() == "o"
    options["Strip_accent"] = input("Afficher les mots sans accents ? (O/N) : ").lower() == "o"

if options["date"]:
    options["jour"] = input('Afficher seulement le jour ? (O/N) : ').lower() == "o"
    options["mois"] = input('Afficher seulement le mois ? (O/N) : ').lower() == "o"
    options["annee"] = input('Afficher seulement l annee ? (O/N) : ').lower() == "o"
    options["langue"] = input('Afficher les mois en langage humain ? (O/N) : ').lower() == "o"
    if options["langue"]:
        options["fr"] = input('Afficher les mois en français ? (O/N) : ').lower() == "o"
        
# Création de l'instance de la classe Engine
e = Engine(words, dates, options)

# Obtention de toutes les possibilités de mots
all_possibilities = []

for possibilities in e.array_possibilities:
    all_possibilities.extend(possibilities)

# # Génération de toutes les combinaisons de mots
combinations_result = []
for r in range(1, min(6, len(all_possibilities))):  # Limite à 5 mots maximum
    combinations_result.extend(combinations(all_possibilities, r))

# Génération de toutes les permutations de mots
permutations_result = []
for r in range(1, min(6, len(all_possibilities))):  # Limite à 5 mots maximum
    permutations_result.extend(permutations(all_possibilities, r))

# Affichage des combinaisons et permutations
print("Combinaisons:")
for combination in combinations_result:
    if len(combination) <= 5:  # Limite à 5 mots maximum
        print(''.join(combination))

print("Permutations:")
for permutation in permutations_result:
    if len(permutation) <= 5:  # Limite à 5 mots maximum
        print(''.join(permutation))
