import random
from hangman_stages import hangman_stages

# Word list
words = ['python', 'doremon', 'nobita', 'jerry', 'computer', 'logic']
word = random.choice(words)
word_completion = "_" * len(word)
guessed = False
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
while not guessed and tries > 0:
    print(hangman_stages[tries - 1])  
    print(word_completion)
    print("\n")

    guess = input(" guess a letter: ").lower()

    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess not in word:
            print("wrong guess")
            tries -= 1
            guessed_letters.append(guess)
        else:
            print("right guess")
            guessed_letters.append(guess)
            word_completion = "".join(
                [letter if letter in guessed_letters else "_" for letter in word]
            )

            if "_" not in word_completion:
                guessed = True
    else:
        print(" Please try again.")
if guessed:
    print("Congratulations! you guessed the word")
else:
    print(hangman_stages[0])
    print(f"tries end  The word was '{word}'.")
