while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif a > b:
        print("Yes")
    elif b > a:
        print("No")
    else:
        print("No")
