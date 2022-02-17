cook = []
s = 0
for i in range(5):
    a = list(map(int, input().split()))
    s = sum(a)
    cook.append(s)
print(cook.index(max(cook)) + 1, max(cook))
