A, B, C = map(int, input().split())

if C - B <= 0:
    print("-1")
else:
    N = -A/(B-C)
    N = N + 1
    print(int(N))
    
# 알고리즘 식!!!
# A + B*N < C*N
# B*C < C*N - A
# B*C - C*N < -A
# (B-C)N < -A
# N < -A/(B-C)
