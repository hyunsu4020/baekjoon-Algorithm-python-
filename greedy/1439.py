# 72ms
s = input()
zero = s.split("1")       
one = s.split("0")

zero = len(zero) - zero.count("")
one = len(one) - one.count("")

if zero > one:
    print(one)
else:
    print(zero)

# ************************************
    
# 76ms
import sys

input = sys.stdin.readline().strip

s = input()
zero = s.split("1")
one = s.split("0")

zero = len(zero) - zero.count("")
one = len(one) - one.count("")

if zero > one:
    print(one)
else:
    print(zero)
