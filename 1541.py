arr = input().split('-')

sum = 0
for i in arr[0].split('+'):
    sum += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)

# ex)
# 55 - 50 + 40 - 30 + 20
# -> 55 - (50 + 40) - (30 + 20) 이렇게 괄호를 쳤을때 최솟값이 됩니다.
# arr = ['55', '50+40', '30+20']
