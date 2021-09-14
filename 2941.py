croatia_alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = input()

for x in croatia_alpabet:
    words = words.replace(x, '*')
print(len(words))
