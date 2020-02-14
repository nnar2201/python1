type('tr' + str(5))

f = 'My school is the best'
print(f[0])
print(f[2])
print(f[8])
print(f[20])
print(f[1])

print(f[0:5])
print(f[5:21])
print(f[:5])
print(f[17:21])

print(f[:13] + 'awesome!')

print(len(f))

g = 'theater'
print(len(g))

x = 'test goo' in 'Greatest good for the greatest number!'
print(x)


def how_eligible(essay):
    n = 0
    n = essay.count(',') + essay.count('?') + essay.count('"') + essay.count('!')

    print(n)


how_eligible('This? "Yes." No, not really!')
how_eligible('Really, not a compound sentence.')
