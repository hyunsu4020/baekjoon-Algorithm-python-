s = int(input())

num = 1
while num * (num + 1) // 2 <= s: # 1부터 num까지 수의 합 공식: num * (num + 1) // 2
    num += 1
    if(num > s):
        num -= 1
print(num - 1)
