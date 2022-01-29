import sys

input = sys.stdin.readline().strip

a, b = map(int, input().split())

cnt = 1
while True:
    if a == b:
        break
    elif a > b:
        cnt = -1
        break
    elif b % 10 == 1:
        b = b // 10
        cnt += 1
    elif b % 2 == 0:
        b = b // 2
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)
