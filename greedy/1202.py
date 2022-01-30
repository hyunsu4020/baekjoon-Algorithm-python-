import sys, heapq

input = sys.stdin.readline
n, k = map(int, input().split())

arr = []
bag = []
for _ in range(n):
    heapq.heappush(arr, tuple(map(int, input().split())))
for _ in range(k):
    bag.append(int(input()))
bag.sort()

result = 0
temp = []
for i in bag:
    while arr and i >= arr[0][0]:
        heapq.heappush(temp, -heapq.heappop(arr)[1])
    if temp:
        result -= heapq.heappop(temp)
    elif not arr:
        break
print(result)
