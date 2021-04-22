import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word


def play(word):
    dashes = "-" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    guessed = False
    print(dashes)
    while not guessed and tries > 0:
        user_guess = input("Enter a character or word ")

        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                print(f"You have already guessed {user_guess}")
            elif user_guess in word:
                print(f"Good Job, {user_guess} is in word")
                guessed_letters.append(user_guess)
                word_as_list = list(dashes)
                indices = [pos for pos, letter in enumerate(word) if letter == user_guess]
                for index in indices:
                    word_as_list[index] = user_guess
                dashes = "".join(word_as_list)
                print(dashes)

                if "-" not in dashes:

                    guessed = True
            else:
                print(f"{user_guess} is not a right guess")
                tries = tries - 1
                guessed_letters.append(user_guess)
                print(dashes)
                print(display_hangman(tries))

        elif len(user_guess) == len(word) and user_guess.isalpha():
            if user_guess in guessed_words:
                print(f"You have already guessed {user_guess}")
            else:
                print(f"{user_guess} is the right guess")
                guessed = True
        else:
            tries = tries - 1
            print(display_hangman(tries))
    if guessed:
        print("Congratulations You won")
    else:
        print("You lost " + word + " was the word given")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
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
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
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
    word = get_word()
    # print(word)
    play(word)

    while input("Would you like to play again(Y/N)").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == '__main__':
    main()
