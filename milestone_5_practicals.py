# %%
import os
os.getcwd()
# %%
"""



"""
# lamdba function function that returns the square of an input
squared_lambda = lambda x: x ** 2
# %%
squared_lambda(9)
# %%
# A lambda function that takes in a number and returns that number cubed
cubed_lambda = lambda x: x ** 3
# %%
cubed_lambda(3)
# %%
# A lambda function that takes two numbers and returns the sum of those numbers

sum_lambda = lambda x, y: x + y     
# %%
sum_lambda(5,3)
# %%
# A lambda function that takes two numbers and returns the product of those numbers

product_lambda = lambda x, y: x * y
# %%
product_lambda(8,6)
# %%

"""
Create a list with 5 tuples, where each tuple contains a name and a number. Then, using the sort function, create a lambda function for each of the following bullet points:

"""

ls_tup = [('yaz', 2), ('quentin', 3), ('jeremy', 6), ('richard', 4), ('james', 2)]
# %%
ls_tup
# %%
# Sort the list by the number in each tuple
sorted(ls_tup, key=lambda x: x[1])
# %%
#Sort the list by the length of the name in each tuple
sorted(ls_tup, key=lambda x: len(x[0]))

# %%
# Sort the list by the length of the name in each tuple, but in reverse order
sorted(ls_tup, key=lambda x: len(x[0]), reverse=True)
# %%
"""
Create a list of 5 numbers


"""

my_list = [4,7,6,9,2]
# %%
# Create a lambda function that squares a number. Then use map to square each number in the list
print(list(map(squared_lambda,my_list)))
# %%
# Create a lambda function that cubes a number. Then use map to cube each number in the list
print(list(map(cubed_lambda, my_list)))
# %%
# 
"""
Create a lambda function that takes in a number and returns that number squared if it is even, and cubed if it is odd. 
Then use map to apply the function to each number in the list
"""

weird_lambda = lambda x: x**2 if x%2 == 0 else x**3
# %%
print(list(map(weird_lambda, my_list)))
# %%
## Lambda functions with filter
"""

Create a list of 10 strings

Create a lambda function that takes in a string and returns True if the string is longer than 5 characters, and False if it is not. 
Then use filter and the lambda function to filter out all strings that are longer than 5 characters

Create a lambda function that takes in a string and returns True if the string is longer than 5 characters and starts with a vowel, 
and False if it is not. Then use filter and the lambda function to filter out all strings that are longer than 5 characters and start with a vowel
"""
string_list = ['sennheiser', 'akg', 'abyss', 'hifiman', 've', 'tinn', 'final', 'beyerdynamic', 'modhouse', 'audeze']
# %%
lenfive_lambda = lambda x: False if len(x) > 5 else True
# %%
print(list(filter(lenfive_lambda, string_list)))
# %%
