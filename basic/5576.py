w = []
k = []

w_sum = 0
k_sum = 0
for _ in range(10):
    a = int(input())
    w.append(a)
for _ in range(3):
    w_sum += max(w)
    w.remove(max(w))
for _ in range(10):
    b = int(input())
    k.append(b)
for _ in range(3):
    k_sum += max(k)
    k.remove(max(k))
print(w_sum, k_sum)
