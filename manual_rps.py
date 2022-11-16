# %%

import random
rps_list = ['rock', 'paper', 'scissors']

def get_computer_choice(list):
    return random.choice(list)

def get_user_choice():
    user_choice = str(input('enter rock, paper or scissors'))
    return user_choice
# %%
p1_choice = get_computer_choice(rps_list)
p2_choice = get_user_choice()

if p1_choice == p2_choice:
    print('its a tie')
elif p1_choice == 'rock' and p2_choice == 'paper':
    print('you win')
elif p1_choice == 'rock' and p2_choice == 'scissors':
    print('you lost')
elif p1_choice == 'paper' and p2_choice == 'scissors':
    print('you win')
elif p2_choice == 'rock' and p1_choice == 'paper':
    print('you win')
elif p2_choice == 'rock' and p1_choice == 'scissors':
    print('you win')
elif p2_choice == 'paper' and p1_choice == 'scissors':
    print('you lost')
# %%
