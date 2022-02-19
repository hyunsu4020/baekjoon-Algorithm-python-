n = int(input())

arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
    arr.sort()
for i in range(n):
    if a != arr[0:]:
        print(arr[i])
