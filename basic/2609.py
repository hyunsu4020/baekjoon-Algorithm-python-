# 함수 만들어서 사용
a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

# math 함수 사용
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
