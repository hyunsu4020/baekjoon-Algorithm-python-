import sys, math

n, m = map(int, sys.stdin.readline().split())

six = []
one = []
for _ in range(m):
    a, b = map(int, input().split())
    six.append(a)
    one.append(b)
    six.append(b*6)
print(min(min(six)*math.ceil(n/6), min(six)*(n//6) + min(one)*(n%6)))
# ceil 함수는 실수를 입력하면 올림 하여 정수를 반환하는 함수이다
# ex) math.ceil(3.14) == 4, math.ceil(-3.14) == -3
