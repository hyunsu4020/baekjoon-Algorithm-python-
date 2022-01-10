n = int(input())
p = list(map(int, input().split()))

p.sort()

sum = 0
for i in range(n):
    for j in range(i+1):
        sum += p[j]
print(sum)

# 1 2 3 3 4 배열 정렬

# sum + 1 = 1   반복문 계산
# 1 + 1 + 2 = 4
# 4 + 1 + 2 + 3 = 10
# 10 + 1 + 2 + 3 + 3 = 19
# 19 + 1 + 2 + 3 + 3 + 4 = 32
