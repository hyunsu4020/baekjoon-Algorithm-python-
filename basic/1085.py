x, y, w, h = map(int, input().split())
min = min(x, y, w-x, h-y)
print(min)
