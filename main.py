import random

lives = 9
words = ['scratch', 'Michael', 'bisciut']
secret_word = random.choice(words)
clue = list('???????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(geussed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if geussed_letter == secret_word[index]:
            clue[index] = geussed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    geuss = input('Guess a letter or the whole word: ')
    if geuss in secret_word:
        update_clue(geuss, secret_word, clue)
    else:
        print('lose a life')
        lives = lives - 1
    if guessed_word_correctly:
        print('You won')
    if lives == 0:
        print('Game Over')
    if geuss == secret_word:
        guessed_word_correctly = True
