t = int(input())

for _ in range(t):
    a_sum = 0
    b_sum = 0
    for _ in range(9):
        a, b = map(int, input().split())
        a_sum += a
        b_sum += b
    if a_sum == b_sum:
        print("Draw")
    elif a_sum > b_sum:
        print("Yonsei")
    else:
        print("Korea")
