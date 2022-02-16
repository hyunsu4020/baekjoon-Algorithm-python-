n, p = map(int, input().split())
person = list(map(int, input().split()))

sum = n * p
result = 0
for i in range(5):
    result = person[i] - sum
    print(result)
