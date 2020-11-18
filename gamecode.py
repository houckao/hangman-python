import random
from words import possible_word


def random_word():
    word = random.choice(possible_word)
    return word.upper()


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs, feet
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |    _/ \\_
                   -
                """,
                # head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head, neck, and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head and neck
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    tries = 8
    guesses = set()
    game_word = random_word()
    player_word = ""
    for x in range(len(game_word)):
        player_word += "-"

    while tries >= 0:
        print(display_hangman(tries))
        print("\t\t\t\t\t" + player_word)

        if len(guesses) != 0:
            print("\nGuesses: ", end="")
            print(guesses)

        print("\nEnter your letter guess below. To solve the word, type 'solve'")

        guess = input()
        guess = guess.upper()
        if guess == "SOLVE":
            print("Enter your word guess below")
            word_guess = input()
            if word_guess.upper() == game_word:
                print("Congratulations, you win!")
                break
            else:
                print("Incorrect solution")
                continue
        elif len(guess) != 1 or guess in guesses:
            print("Invalid input")
            continue
        elif guess in game_word:
            guesses.add(guess)
            temp_word = game_word
            for i in range(game_word.count(guess)):
                player_word = player_word[:temp_word.index(guess)] + guess + \
                              player_word[temp_word.index(guess) + 1:]

                temp_word = temp_word.replace(guess,"-", 1)
        else:
            guesses.add(guess)
            tries -= 1

        if player_word == game_word:
            print("Congratulations, you win!")
            break

    print("GAME FUCKING OVER")


main()

