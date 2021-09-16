# A = 올라감(낮), B = 미끄러짐, V = 높이(m)
# 낮부터 시작이니 낮 다음은 새벽으로 생각하면됨 즉, B*(day - 1)
A, B, V = map(int, input().split())

day = 0
meter = 0
while True:
    day += 1
    if (A*day)-(B*(day-1)) == V:
        break
print(day)  # 시간초과 발생 따라서 아래 코드가 제일 빠름

# A*day-B*(day-1) == V:
# A*day-B*day+B == V
# day(A-B) + B == V
# day == (V - B)/(A - B)
A, B, V = map(int, input().split())
day = (V - B)/(A - B)
print(int(day)) if day == int(day) else int(day) + 1 #삼항연산자
