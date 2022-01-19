n = int(input())

rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
mathod = []
for i in range(len(rope)):
    mathod.append(rope[i] * (i+1))
print(max(mathod))
