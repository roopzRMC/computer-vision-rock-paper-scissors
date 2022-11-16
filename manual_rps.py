# %%

import random
rps_list = ['rock', 'paper', 'scissors']

def get_computer_choice(list):
    return random.choice(list)

def get_user_choice():
    user_choice = str(input('enter rock, paper or scissors'))
    return user_choice
# %%
