import sys

n = int(sys.stdin.readline())

pos = []
neg = []
result = 0
for i in range(n):
    a = int(input())
    if a == 1:
        result += 1
    elif a > 1:
        pos.append(a)
    else:
        neg.append(a)

pos.sort()
neg.sort(reverse=True)      # 오름차순
while len(pos) > 0:
    if len(pos) == 1:
        result += pos.pop()
    else:
        result += pos.pop() * pos.pop()
while len(neg) > 0:
    if len(neg) == 1:
        result += neg.pop()
    else:
        result += neg.pop() * neg.pop()
print(result)
