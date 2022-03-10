n = int(input())

a_sum = 100
b_sum = 100
if 1 <= n <= 15:
    for _ in range(n):
        a, b = map(int, input().split())
        if a < b:
            a_sum -= b
        elif a > b:
            b_sum -= a
        elif a == b:
            continue
    print(a_sum)
    print(b_sum)
