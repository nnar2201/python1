import random
some_values = ('a', 'b', 3)
print(some_values)
print(some_values[0])
print(some_values[2])
print(some_values[1])
print(some_values[0:2])


a = 10
tup = (9, a, 11)
print(tup)
print(tup[1] == 10)
print(tup[1])



values = ['a', 'b', 3]
print(values)
print(values[1:])
print(values[2] == 3)


values = values + [4, 5]
print(values)
values.append([6, 7])
print(values)


a = 6
a *= 3
print(a)


def roll_two_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1 + dice2)



roll_two_dice()



import string
def guess_letter():
    r = random.choice(string.ascii_letters)
    print(r)


guess_letter()

