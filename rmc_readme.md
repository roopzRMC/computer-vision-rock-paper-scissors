# Computer Vision Practicals Readme
> Conda environment set up


* Leveraging a pre-built yml file I was able to create a new conda environment for tensorflow
* Using an M2 Mac meant installing some additional packages via developer.apple.com
* The main mistake made was to create a test file called tensorflow.py as this meant that python used this file to reference the tensorflow library and NOT the actual tensorflow library

> Using the terminal

* using an alias in terminal is a method of short handing certain commands in terminal eg

```
alias note = 'echo $1 > ~/note.txt'
```
where $1 is the argument and > is to overwrite and >> is to append

* aliases do not persist and to adjust this behaviour, you can add aliases to the local bash rc file or (if using zsh) the zshrc file

```
nano ~/.zshrc
```

> Dictionaries
* Dicts consists of key , value pairs
* They are mutable
    * However the keys are unique but the values can be overwritten
* Dictionaries can contains other dictionaries or lists

### Deleting
* can be achieved using the del command with the key 
* pop can be used to remove the last item

### Operations
* .values() shows values of all keys
* .keys() shows all keys
* .item() shows all key value pairs


> XOR Gates

A logic gate which gives TRUE when only one of the inputs is TRUE but NOT when both are TRUE

These can be build using a combo of NAND and OR gates

* Used for simple addition in digital circuits
* checking for odd versus even
* error checks

> Loops

### For loop

* A for loop takes an iterable item eg a dict or list or range object
```
for k,v in dict.items()
```

* break and continue statements can also be used in for loops

### Built-in functions

* zip -> pairs values together to a list of tuple and these can be unpacked in a for loop

* enumerate -> indexes the supplied value and can be used in conjunction with zip

### List comprehensions

* these can bake a loop statement in to 1 line

```
cube = [i**3 for i in range(1,11)]
```

* {} are used for set operations with list comprehensions or dictionary comprehensions

> Error and Exception Handling

In python once there is an error the code execution STOPS. Error handling is enabled to allow blocks of code to run despite errors

```
TRY:
# block of code intended to be run
EXCEPT:
# if error above in the try section then this block is executed
FINALLY:
# runs regardless of any error

```

It is best practice to use except with a specific error type

```
except TypeError:

except NameError:
```

* Using the debugger built in to the IDE can help you step through the code to determine more complex bugs in the program that are not necessarily causing an error to be thrown

> Lambda functions

These are short version of normal functions and can be defined on a single line

```
# a standard function such as
def square_func(y):
    return y ** 2

# becomes

square_func = lambda y: y ** 2
```
- They can also accept 2 or more args

```
sum_func = lambda x, y: x + y
```

- Lambda functions can also be passed to higher order functions such as
    - sorted()
    - filter()
    - map()

```
sorted(list, key = lambda x: x[1])
```

- Lambda functions can also be used to apply functions to an iterable

```
func = lambda x, y :x ** y
list(map(func, [1,2,3,4], [1,3,3]))

```

> Updating RPS Game

### Creating the interation

- Waiting for a trigger
    - using the input() function, a while loop is instantiated which will continuously until the s and enter keys are pressed
    - once pressed it triggers a countdown set at 3 seconds so that the LAST prediction made via the keras model is the one that is set as the user choice
    - This is housed in a get_prediction() function

- Game Logic
     - leveraging the computer_play() function in which a random selection is made from the rock, paper, scissors list - this function contains the rules of the game via a succession of if/else statements
     - the game is executed on the basis of a 2 condition while loop (where both the user and computer scores MUST be less than three to ensure the best of 3 wins)
     - the get_prediction() method is called each time triggering the counter for achieving a good quality prediction

     
     ![](screenshots/game_terminal_op.png)