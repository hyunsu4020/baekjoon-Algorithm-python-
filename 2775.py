t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]
    for _ in range(k):
        for m in range(1, n):
            people[m] += people[m-1]
    print(people[n-1])
