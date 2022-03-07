n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    b = b - c
    if a < b:
        print("advertise")
    elif a == b:
        print("does not matter")
    else:
        print("do not advertise")
