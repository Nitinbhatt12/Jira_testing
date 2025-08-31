import csv
import random

def load_countries(filename):
    countries = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            countries.append(row[0].strip())
    return countries

def display_word(word, guessed_letters):
    return ''.join([letter if letter.lower() in guessed_letters else '-' for letter in word])

def main():
    countries = load_countries("countries.csv")
    secret_country = random.choice(countries).lower()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 5

    print("Welcome to the Country Guessing Game!")
    print("You have 5 chances to guess wrong letters.\n")

    while wrong_guesses < max_wrong:
        print("Current word:", display_word(secret_country, guessed_letters))
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        guess = input("Guess a letter: ").lower()

        if not (guess.isalpha() and len(guess) == 1):
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_country:
            wrong_guesses += 1
            print(f"Wrong guess! ({wrong_guesses}/{max_wrong})")

        if all(letter in guessed_letters for letter in secret_country):
            print("\n🎉 Congratulations! You guessed the country:", secret_country.title())
            break
    else:
        print("\n❌ Game Over! The country was:", secret_country.title())

if __name__ == "__main__":
    main()
