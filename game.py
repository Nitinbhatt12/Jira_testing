import csv
import random

def load_countries(filename):
    countries = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming each row has one country name
            countries.append(row[0].strip())
    return countries

def display_word(word, guessed_letters):
    return ''.join([letter if letter.lower() in guessed_letters else '-' for letter in word])

def main():
    countries = load_countries("countries.csv")
    secret_country = random.choice(countries).lower()
    guessed_letters = set()

    print("Welcome to the Country Guessing Game!")
    while True:
        print("Current word:", display_word(secret_country, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            guessed_letters.add(guess)
        else:
            print("Please enter a single valid letter.")

        if all(letter in guessed_letters for letter in secret_country):
            print("Congratulations! You guessed the country:", secret_country.title())
            break

if __name__ == "__main__":
    main()
