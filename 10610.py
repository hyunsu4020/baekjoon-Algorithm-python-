t = list(input())
t.sort(reverse=True)

sum = 0
for i in t:
    sum += int(i)
if sum % 3 != 0 or "0" not in t:
    print(-1)
else:
    print(''.join(t))
# join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서
# 하나의 문자열로 바꾸어 반환하는 함수입니다.
