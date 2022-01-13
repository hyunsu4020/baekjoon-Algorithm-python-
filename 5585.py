pay = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]

count = 0
for i in coin:
    count += pay // i
    pay %= i
print(count)
