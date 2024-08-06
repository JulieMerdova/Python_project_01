"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Julie Merdova
email: julie.talpova@gmail.com
discord: julie.merdova
"""

# Vyžádá si od uživatele přihlašovací jméno a heslo,
# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
registrovani = {"bob": "123", 
                "ann": "pass123", 
                "mike": "password123",
                "liz": "pass123"
                }
from task_template import TEXTS
import re

def starts_with_upper(word):
    return len(word) > 0 and word[0].isupper()

def main():
    jmeno = input("username:")
    heslo = input("password:")
    # pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
    # pokud není registrovaný, upozorni jej a ukonči program.**
    if jmeno in registrovani and registrovani[jmeno] == heslo:
        print("Welcome to the app,", jmeno.capitalize(),".")
        print("We have 3 texts to be analyzed.")
    else:
        print("unregistered user, terminating the program..") 
        return
    # Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
    # Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
    # pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

    print("-" * 35)
    text_cislo = input("Enter a number btw. 1 and 3 to select:")
    
    if text_cislo.isdigit():  # kontrola, zda obsahuje pouze číslice
        text_cislo = int(text_cislo)
        if 1 <= text_cislo <= len(TEXTS):
            vybrany_text = TEXTS[text_cislo - 1] 
            # vybrat text podle vybraného čísla, mínus 1, protože index od 0..
            print("You selected text number", text_cislo)
            
            # výpočet jednotlivých statistik:

            words = vybrany_text.split()
            pocet_slov = 0
            pocet_kapitalek = 0
            pocet_upper_slov = 0
            pocet_lower_slov = 0
            pocet_cisel = 0
            suma_vsech_cisel = 0

            word_lengths = {}
            uppercase_words = []
            capitalized_words = []

            for word in words:
                # očištění text od nealfanumerických znaků
                cleaned_word = ''.join(char for char in word if char.isalnum())            
                pocet_slov += 1
                if starts_with_upper(cleaned_word):
                    capitalized_words.append(cleaned_word)
                    pocet_kapitalek += 1
                if cleaned_word.isupper() and cleaned_word.isalpha():
                    uppercase_words.append(cleaned_word)
                    pocet_upper_slov += 1
                if cleaned_word.islower():
                    pocet_lower_slov += 1
                if cleaned_word.isdigit():
                    pocet_cisel += 1
                    suma_vsech_cisel += int(word)

                # délka slov pro graf
                length = len(cleaned_word)
                if length > 0:
                    if length not in word_lengths:
                        word_lengths[length] = 1
                    else:
                        word_lengths[length] += 1
            
            print("There are", pocet_slov,"words in the selected text.")
            print("There are", pocet_kapitalek,"titlecase words.")
            print("There are", pocet_upper_slov,"uppercase words.")
            print("There are", pocet_lower_slov,"lowercase words.")
            print("There are", pocet_cisel,"numeric strings.")
            print("The sum of all the numbers", suma_vsech_cisel)

            # vykreslení grafu
            print("\nWord Length Frequency:")
            print("\nLEN|  OCCURENCES  |NR.")
            print("-" * 35)
            for length in sorted(word_lengths):
                occurrences = "*" * word_lengths[length]
                print("{:>3}|{:<14}|{}".format(length, occurrences, word_lengths[length]))
            # vypsání words starting with a capital letter
            if capitalized_words:
                print("\nWords starting with a capital letter:")
                print(", ".join(capitalized_words))
            else:
                print("\nNo words starting with a capital letter in the text.")
        else:
            print("invalid number, terminating the program..")
    else:
        print("invalid input, terminating the program..")
if __name__ == "__main__":
    main()

        