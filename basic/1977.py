m = int(input())
n = int(input())

num = []
for i in range(m, n+1):
    if i == int(i ** 0.5) ** 2:
        num.append(i)
        
if len(num) == 0:       # 완전 제곱수가 없는 경우
    print(-1)
else:
    print(sum(num))
    print(min(num))
