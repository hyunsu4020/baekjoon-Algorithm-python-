odd = []
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        odd.append(n)
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)
