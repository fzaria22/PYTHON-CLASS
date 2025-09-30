import random
while True:
    user_input = input(
        'Do you want to roll the Dice? (y/n) or (yes/no):').strip().lower()

    if user_input in ['yes', 'y']:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'{dice1} and {dice2}')
        break
    elif user_input in ['no', 'n']:
        print('Thank you')
        break
    else:
        print('Invalid input, please enter y/n or yes/no')
