import time
import random
from words import words
from hangman import lives_visual
import string
import msvcrt
from sys import stdout


def delay_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        time.sleep(0.05)


print('''\033[1;33;40m  __                                           
|  |--.---.-.-----.-----.--------.---.-.-----.
|     |  _  |     |  _  |        |  _  |     |
|__|__|___._|__|__|___  |__|__|__|___._|__|__|
                  |_____|     \033[0m\n''')
delay_print('''\033[1;30;40m *************GAME INSTRUCTIONS**************
> The player guess the letter to get the correct word.
> The player have 30 seconds to guess the correct word.
> The player have 7 lives to guess the correct word.

\033[1;32;40m******************ENJOY!*****************\033[0m\n''')

print("\033[1;32;40m Press any key to start \033[0m")
msvcrt.getch()


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

# main function of hangman


def hangman():

    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    start_time = time.time()
    time_limit = 30

    while len(word_letters) > 0 and lives > 0:
        print(
            f"You have {lives} lives left and you have used these letters: {used_letters}")
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual[lives])
        print(f"Current word: {word_list}")

        elapsed_time = time.time() - start_time
        remaining_time = time_limit - elapsed_time
        print(f"Remaining time: {remaining_time:.0f} seconds")

        if time.time() - start_time > time_limit:
            print("Time's up!!")
            print(f"Sorry the word is {word}")
            return

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"\nletter {user_letter} is not in the word.")

        elif user_letter in used_letters:
            print("\nYou have already used that letter. Guess another letter.")

        else:
            print("\nThat is not a valid letter.")

    if lives == 0:
        print(lives_visual[lives])
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"LUCKY! You guessed the word {word} !!")


if __name__ == '__main__':
    hangman()
