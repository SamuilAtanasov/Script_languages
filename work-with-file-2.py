import os

def count_letters(filename):
    vowels = set("AaEeOoUuIi")
    consonants_count = 0
    vowels_count = 0
    symbols_count = 0
    try:
        with open(filename, "r", encoding = "utf-8") as f:
            text = f.read()
        for ch in text:
            if ch.isalpha():
                if ch in vowels:
                    vowels_count += 1
                else:
                    consonants_count += 1
            else:
                symbols_count += 1
        print(f"Vowels : {vowels_count}")
        print(f"Consonants : {consonants_count}")
        print(f"Other symbols: {symbols_count}")
    except FileNotFoundError:
        print("The file is not found!")

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "vowels.txt")
count_letters(input_file)