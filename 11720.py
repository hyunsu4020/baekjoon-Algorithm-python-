# sum 함수 사용
num = int(input())
print(sum(map(int, input())))

# for문을 이용
n = input()
num = input()
total = 0
for x in num:
    total += int(x)
print(total)

# for문을 이용 2
n = int(input())
num = input()
total = 0
for i in range(n):
    total += int(num[i])
print(total)
