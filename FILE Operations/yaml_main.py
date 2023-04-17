import yaml
import random
import getpass

# with open("yaml_file.yml", 'r') as f:
#     data = yaml.safe_load(f)
#
# print(data)

with open("yaml_main_file.yml", 'r') as f:
    data = yaml.safe_load(f)

range_min = data['range']['min']
range_max = data['range']['max']
guesses_allowed = data['guesses']
mode = data['mode']

solved = False

if mode == 'single':
    correct_number = random.randint(range_min, range_max)
elif mode == 'multi':
    correct_number = int(getpass.getpass('Player 2, please enter the number to guess: '))
else:
    print('Invalid data')
    exit()

for i in range(guesses_allowed):
    guess = int(input('Enter your guess : '))
    if guess == correct_number:
        print(f'Correct! You needed {i + 1} tries!')
    elif guess < correct_number:
        print('Too low!')
    else:
        print('Too high!')

if not solved:
    print('You lost. The number was', correct_number)
