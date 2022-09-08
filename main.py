import random
from hangman_art import logo 
from hangman_words import word_list 
from hangman_art import stages

print(logo)
print('Hello to Hangman are you ready for the challenge?')
ready = input('Enter "y" for yes or "n" for no!\n').lower()
if ready == 'y':
    print('Okeee lets go...')
elif ready == 'n':
    print("Come again when you are ready.")
else:
    print("That's not a valid input") 
guess = 0
lives = 6
chosen_word = random.choice(word_list)
display = []
for i in range(len(chosen_word)):
    display.append('_')
print(display)
while lives != -1:
    if '_' not in display:
        print('You won!')
        break
    guess = input('Enter your guess here:\n')
   
    if guess in chosen_word:
        for i, x in enumerate(chosen_word): 
            if x == guess:
                #guess_index = chosen_word.index(x)
                display[i] = guess
                print(display)
    else:
        print(f'You guessed {guess}. That letter is not in the word.')
        print(stages[lives])
        lives -= 1    
else:
    print('You lost!')        


         