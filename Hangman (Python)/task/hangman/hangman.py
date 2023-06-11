import random
import string

print("H A N G M A N")
words_to_guess = ["python", "java", "swift", "javascript"]
wins, losses = 0, 0

while True:
    menu_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if menu_choice == "play":
        word_to_guess = random.choice(words_to_guess)
        guessed_letters = []
        lives = 8
        hint = "-" * len(word_to_guess)
        while lives > 0:
            print("\n" + hint)
            letter = input("Input a letter:")
            if len(letter) != 1:
                print("Please, input a single letter.")
            elif letter not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in guessed_letters:
                print("You've already guessed this letter.")
            elif letter in word_to_guess:
                guessed_letters.append(letter)
                index = -1
                while True:
                    index = word_to_guess.find(letter, index + 1)
                    if index == -1:
                        break
                    hint = hint[:index] + letter + hint[index + 1:]
                if hint == word_to_guess:
                    print(f"You guessed the word {word_to_guess}!")
                    break
            else:
                guessed_letters.append(letter)
                print("That letter doesn't appear in the word.")
                lives -= 1

        if lives >= 0 and hint == word_to_guess:
            print("You survived!")
            wins += 1
        else:
            print("\n" + hint)
            print("\nYou lost!")
            losses += 1
    elif menu_choice == "results":
        print(f"You won: {wins} times")
        print(f"You lost: {losses} times")
    elif menu_choice == "exit":
        break
