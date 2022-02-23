buger = []
for i in range(3):
    a = int(input())
    buger.append(a)
juice = []
for i in range(2):
    b = int(input())
    juice.append(b)

result = min(buger) + min(juice) - 50
print(result)
