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
