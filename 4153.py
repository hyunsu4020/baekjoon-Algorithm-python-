while True:
    a = list(map(int, input().split()))
    maxNum = max(a)
    if sum(a) == 0:
        break
    a.remove(maxNum)
    if a[0]**2 + a[1]**2 == maxNum**2:
        print("right")
    else:
        print("wrong")
