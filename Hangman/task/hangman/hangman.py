# Write your code here
import random
import string

words = ['python', 'java', 'kotlin', 'javascript']

word = random.choice(words)
hidden = '-' * len(word)

guessedLetters = set()

print('H A N G M A N')
print()

while True:
    attempts = 8
    answer = input('Type "play" to play the game, "exit" to quit: ')
    if answer == "exit":
        break
    elif answer == "play":
        while attempts > 0:
            print(hidden)
            letter = input('Input a letter: ')

            if len(letter) != 1:
                print("You should input a single letter")
            elif letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
            elif letter in guessedLetters:
                print("You've already guessed this letter")
            elif letter in hidden:
                print('No improvements')
                attempts -= 1
                if attempts == 0:
                    print("You lost!")
                    break
            else:
                count = word.count(letter)
                if count > 0:
                    index = word.find(letter)
                    for _ in range(count):
                        hidden = hidden[:index] + letter + hidden[index+1:]
                        index = word.find(letter, index+1)
                else:
                    print("That letter doesn't appear in the word")
                    attempts -= 1
                    if attempts == 0:
                        print("You lost!")
                        break
                if hidden == word:
                    print(hidden)
                    print("You guessed the word!")
                    print("You survived!")
                    break

            guessedLetters.add(letter)
            print()
    else:
        continue
