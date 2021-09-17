# H = 층수, W = 방 개수, N = 몇번째 손님
# 1층 elevator가 정문이라 칠때
# 두 방과의 거리는 항상 1
# YXX or YYXX 는 Y = 층수, X = 엘베로부터 시작되는 번호
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    a = N%H
    b = N//H + 1
    if a <= 0:
        a = H
        b -= 1
    print(a*100+b)
