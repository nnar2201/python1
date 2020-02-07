
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            print('Citrus, Fruit')
        else:
            print('NOT Citrus, Fruit')
    else:
        if food in starchy:
            print('Starchy, NOT Fruit')
        else:
            print('NOT Starchy, NOT Fruit')


food_id('apple')
food_id('orange')

if food_id('orange') != 'Citrus, Fruit':
    print("ok")


def food_id_test():
    works = True
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not good
    '''


if food_id('orange') != 'Citrus, Fruit':
    works = 'orange bug in food id()'
    print("1good")
else:
    works = False
if food_id('banana') != 'NOT Citrus, Fruit':
    works = 'banana bug in food_id()'
    print("2good")
else:
    works = False

    # Add tests so that all lines of code are visited during test

if works == True:
    print("All good!")
    print(True)
else:
    print(works)
    print(False)
food_id_test()


def f(x):
    if isinstance(x, int):
        print('integer')
    else:
        print('not an integer')
    if (x % 2) == 0:
        print('x is even')
    else:
        print('x is odd')
    if (x % 3) == 0 and (x % 2) == 0:
        print('x is a multiple of 6')
    else:
        print('x is even')


f(12)





import random
n = random.randint(1, 10)
answer = "nothing"
while n != 0:
    while answer != "you guessed it!":
        guess = int(input("Enter an integer from 1 to 10: if you enter 0 the game will be over."))
        if guess < n:
            answer = "guess is low"
        elif guess > n:
            answer = "guess is high"
        else:
            answer = "you guessed it!"
        print(answer)
