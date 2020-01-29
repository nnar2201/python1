a = 3
b = a**2
print(b)

c = a + 1 >= 2 and a**2 != 5
print(c)

d = a**2 >= 9 and not a>3
print(d)

e = a+2 == 5 or a-1 != 3
print(e)

f = x, y = (65, 40)
g = x
print(g)

h = 50 < x and x < 80 and 30 <= y and y <= 45
print(h)

i = 50 > x and x >= 21 and 30 >= y and 5 < y
print(i)

j = l, k = (90, 115)
m = 50 < x and x <= 210 and 30 <= y and 150 > y
print(m)




def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
age_limit_output(10)
age_limit_output(16)




def report_grade(percent):
    if percent >= 80:
         print("Good Job")
    if percent < 80:
        print("You fail")
report_grade(79)
report_grade(85)



n = 't' in 'string'
print(n)
o = 'T' in 'string'
print(o)
p = 3 in [1,2,3]
print(p)
q = '3' in [1,2,3]
print(q)




def letter_in_word(letter, word):
    if letter in word:
        print("true")
    else:
        print("false")
letter_in_word('t', 'secret hangman phrase')




def hint(color, secret):
    if color in secret:
        print("The color IS in the secret sequence of colors.")
    else:
        print("The color IS NOT in the secret sequence of colors.")
secret = ['red', 'red', 'yellow', 'yellow', 'black']
hint('red', secret)
hint('green', secret)