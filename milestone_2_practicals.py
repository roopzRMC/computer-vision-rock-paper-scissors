# %%
one_deep_dictionary = {'start here':1,'k1':[1,2,3,
{'k2':[1,2,{'k3':['keep going',{'further':[1,2,3,4,
[{'k4':'Python'}]]}]}]}]}

# %%
one_deep_dictionary
# %%
## index to the point where you print python from the one_deep
one_deep_dictionary['k1'][3]['k2'][2]['k3'][1]['further'][4][0]['k4']
# %%
# Test evaluated data type of the following

print(type(99 > 5))

# %%
print(type(0 == False))

# %%
print(type(1 == True))


# %%
print(type(6.2 < 7))

# %%
print(type(9 >= 9))

# %%
print(type(False < True))
# %%
99>5
# %%
## Creating an XOR gate
A = True
B = False

# %%
def or_gate(A, B):
    if (A == True or B == True):
        return True
    else:
        return False
# %%
C = or_gate(A, B)
# %%
def and_gate(A, B):
    if (A==True and B==True):
        return True
    else:
        return False
# %%
D = and_gate(A, B)
# %%
D_NOT = not D
# %%
print(D_NOT)
# %%
XOR = C and D_NOT
# %%
print(XOR)
# %%
# XOR can also be represented with the ^
XOR2 = A ^ B
print(XOR2)

# %%
'AAA' > 'BBB'
# %%
'B' > 'A'
# %%
'AAB' > 'AAA'
# %%
'aaa' > 'AAA'
# %%
ord('a')
# %%
ord('A')
# %%
## Comparing integers
x = 10
n = int(input(f'specify an integer please'))
if n > x:
    print(f'{n} is greater than {x}')
else:
    print(f'too small sonny')
# %%
## Shopping list / nested dictionary

shop = {'tomatoes': 18,
'washing sponges': 20,
'juice': 4.5,
'foil': 4,
'sugar': 2000,
'prices': {
    'tomatoes': 0.87,
    'sugar': 1.09,
    'washing sponges': 0.29,
    'juice': 1.89,
    'foil': 1.29
},
'pack_sizes': {
    'tomatoes': 6,
    'sugar': 500,
    'washing sponges': 10,
    'juice': 1.5,
    'foil': 30
}}
# %%
shop['pack_sizes']
# %%
shop['tomatoes']/shop['pack_sizes']['tomatoes']
# %%
my_items = list(shop.keys())
# %%
shop['tomatoes']*shop['prices']['tomatoes']
# %%
my_items
# %%
costs = []
for i in range(0, 5):
    ## calculate number of packs required for item
    print((shop[my_items[i]]/shop['pack_sizes']['tomatoes']*shop['prices'][my_items[i]]))
# %%
## Loops
## while loop to print 1 to 50
i = 1
while i < 51:
    print(i)
    i += 1

# %%
## for loop to print 1 to 50

for i in range(1, 51):
    print(i)
# %%
## Count even numbers with a while loop
i = 0
while (i < 51):
    if i%2 == 0:
        print(i)
        i +=1
    else:
        i +=1
    

# %%
even_list = []
for i in range(1, 101):
    if i%2 == 0:
        even_list.append(i)
print(sum(even_list))
# %%
odd_list = []
for i in range(1,101):
    if i%2 != 0:
        odd_list.append(i)
print(sum(odd_list))
    # %%
odd_list
# %%
"""
Write a program that prints the numbers from 1 to 100.

For multiples of three print "Fizz" instead of the number
For multiples of five print "Buzz"
For numbers which are multiples of both three and five print "FizzBuzz"

"""
for i in range(1, 101):
    if i%5 == 0 and i%3 ==0:
        print(f'FizzBuzz {i}')
    elif i%5 == 0:
        print(f'Buzz {i}')
    elif i%3 ==0:
        print(f'Fizz {i}')
    else:
        print(i)
# %%
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
if list_1 == list_2:
    print('The lists are the same.')
else:
    print('The lists are different.')
# %%
## Simple rock paper scissors

import random
"""
The program asks two inputs from the user: player1 and player2. The inputs can be either 'rock', 'paper' or 'scissors'.

Code the logic of the game to see who wins. Print the result in the format: "Player 1 wins" or "Player 2 wins"
If one of the inputs is not "rock", "paper" or "scissors", print "Invalid input"
If both inputs are the same, print "It's a tie"
Create two new variables, num_player_one_wins and num_player_two_wins, and use them to keep track of the number of wins each player has
Put the code inside a while loop that runs until one of the players has won three rounds
"""

rps_list = ['rock', 'paper', 'scissors']

num_player_one_wins = 0

num_player_two_wins = 0

while num_player_one_wins < 3 and num_player_two_wins < 3:
    p1_choice = random.choice(rps_list)
    p2_choice = random.choice(rps_list)

    print(f'Player 1 plays {p1_choice}')
    print(f'Player 2 plays {p2_choice}')

    if p1_choice == p2_choice:
        print('its a tie')
    elif p1_choice == 'rock' and p2_choice == 'paper':
        print('p2 wins')
        num_player_two_wins +=1
    elif p1_choice == 'rock' and p2_choice == 'scissors':
        print('p1 wins')
    elif p1_choice == 'paper' and p2_choice == 'scissors':
        print('p2 wins')
        num_player_one_wins +=1
    elif p2_choice == 'rock' and p1_choice == 'paper':
        print('p2 wins')
        num_player_one_wins +=1
    elif p2_choice == 'rock' and p1_choice == 'scissors':
        print('p2 wins')
        num_player_two_wins +=1
    elif p2_choice == 'paper' and p1_choice == 'scissors':
        print('p1 wins')
else:
    if num_player_one_wins > num_player_two_wins:
        print(f'player 1 wins with score {num_player_one_wins} to {num_player_two_wins}')
    else:
        print(f'player 2 wins with score {num_player_two_wins} to {num_player_one_wins}')


# %%
## Budget calculator
# Each element is the product code, the individual price, and the quantity.
order_list = [("tom", 0.87, 4),
              ("sug", 1.09, 3),
              ("ws", 0.29, 4),
              ("juc", 1.89, 1),
              ("fo", 1.29, 2)]

# This dictionary gives the full name of each product code.
names = {"tom": "Tomatoes",
         "sug": "Sugar",
         "ws": "Washing Sponges",
         "juc": "Juice",
         "fo": "Foil"}

budget = 10.00
running_total = 0
receipt = []

# %%
"""
Use a for loop to iterate through the order_list
At each iteration:
Add the items to the receipt list
Add the total cost of the item to the running_total variable
Subtract the total cost of the item from the budget variable
If at some point the budget variable is less than 0, print the message "You have exceeded your budget by {budget}." and break the loop

"""
# %%

for i in range(0, len(order_list)):
    while budget >= 0:
        receipt.append(order_list[i][0])
        running_total += order_list[i][1] * order_list[i][2]
        print(f'running_total is {running_total}')
        budget = 10 - running_total
        print(f'budget is {budget}')
    else:
        print('budget exceeded')
        break
        

# %%
#creating a list comprehension squaring even arguments and orr arguments after adding one to them

my_list = [1,5,8,6,21]

lc_list = [(i+1) ** 2 if i%2 !=0 else i**2 for i in my_list]

print(lc_list)
# %%
computing_skills_dict = {'name':'rupert',
            'skills': ['python', 'r', 'music']}

music_skills_dict = {'name':'rupert',
            'skills': ['piano', 'clarinet'] }
# %%
skills_list = [computing_skills_dict, music_skills_dict]
# %%
skills_list[1]
# %%
## find the last letter of first skill of last dictionary - should be o!

skills_list[1]['skills'][0][4]
# %%
shop_dict = {"tom":0.87, "sug":1.09, "ws":0.29, "cc":1.89, "ccz":1.29}

names_dict = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "cc":"Coca-Cola", "ccz":"Coca-Cola Zero"}
# %%
## Using a dictionary comprehension and using another dictionary to look up the value
filtered_shop = {names_dict[k]: v for k, v in shop_dict.items() if v > 1.00}
# %%

