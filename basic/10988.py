a = input()
b = a[::-1]

while 1 <= len(a) <= 100 and a.isupper() == False:
    if a == b:
        print(1)
        break
    else:
        print(0)
        break
