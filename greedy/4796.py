import sys

input = sys.stdin.readline

case = 0
result = 0
while True:
    L, P, V = map(int, input().split())     # P일중 L일 동안만 사용가능, V일짜리 휴가
    if L == 0 and P == 0 and V == 0:        # 빠른 속도를 위해 종료값을 위에 작성
        break
    a = V // P
    b = V % P
    case += 1
    if L < b:
        b = L
    result = a*L+b
    print("Case %d: %d" %(case, result))
