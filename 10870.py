n = int(input())

fibo = [0, 1]
for i in range(2, n+1):
    sum = fibo[i-1] + fibo[i-2]
    fibo.append(sum)
print(fibo[n])
