alpabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0
for i in alpabet_list:
    for x in i:
        for n in word:
            if x == n:
                time += alpabet_list.index(i) + 3
print(time)
