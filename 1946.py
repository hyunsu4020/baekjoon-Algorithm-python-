import sys
input = sys.stdin.readline      # 시간 초과 오류를 방지하기 위해
t = int(input())                # input = sys.stdin.readline

for i in range(t):
    count = 1
    rank = []
    n = int(input())
    for j in range(n):
        a, b = map(int, input().split())
        rank.append([a, b])

    rank.sort()
    max = rank[0][1]

    for k in range(1,n):
        if max > rank[k][1]:
            count += 1
            max = rank[k][1]
    print(count)
