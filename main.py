import random

user_wins = 0
computer_win = 0

options = ['Rock', 'Paper', 'Scissors']





while True:
    user_input = input("Enter 'Rock', 'Paper' or 'Scissors' or Enter Q to quit: ")
    if user_input == 'Q':
        break

    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print(f'Computer pick {computer_pick}')
    if user_input == 'Rock' and computer_pick == 'Scissors':
        print('User wins!')
        user_wins += 1
    elif user_input == 'Paper' and computer_pick == 'Scissors':
        print('Computer wins')
        computer_win += 1
    elif user_input == 'Scissors' and computer_pick == 'Scissors':
        print('It is a draw')
    elif user_input == 'Rock' and computer_pick == 'Paper':
        print('Computer wins')
        computer_win += 1
    elif user_input == 'Paper' and computer_pick == 'Paper':
        print('It is a draw')
    elif user_input == 'Paper' and computer_pick == 'Rock':
        print('User wins')
        user_wins += 1
    elif user_input == 'Scissors' and computer_pick == 'Paper':
        print('User wins')
        user_wins += 1
    elif user_input == 'Scissors' and computer_pick == 'Rock':
        print('Computer wins')
        computer_win += 1
    elif user_input == 'Rock' and computer_pick == 'Rock':
        print('It is a draw')
    else:
         pass