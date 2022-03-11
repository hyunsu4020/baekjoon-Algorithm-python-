t = int(input())

for _ in range(t):
    n = int(input())
    name = []
    drink = []
    for i in range(n):
        a, b = map(str, input().split())
        name.append(a)
        drink.append(int(b))
    for j in range(n):
        if drink[j] == max(drink):
            print(name[j])
