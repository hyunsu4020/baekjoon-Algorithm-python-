# 우선순위 큐
import sys
import heapq        # 우선순위 큐

input = sys.stdin.readline
n = int(input())
card = []

for i in range(n):
    heapq.heappush(card, int(input()))

if len(card) > 1:
    result = 0
    while len(card) > 1:
        num1 = heapq.heappop(card)          # card에서 가장 작은 항목을 반환
        num2 = heapq.heappop(card)          # card에서 그 다음 가장 작은 항목을 반환
        result += num1 + num2
        heapq.heappush(card, num1 + num2)   # num1 + num2 값을 card로 push
                                            # 결국 마지막 값 하나가 남아서 while문 종료
    print(result)
else:
    print(0)


# 메모리 초과 코드 - 출력값은 제대로 나오지만 입력값 수의 크기가 너무 광범위하기 때문에 메모리 초과가 발생
import sys

input = sys.stdin.readline
n = int(input())
card = []

for i in range(n):
    card.append(int(input()))

card.sort()
result = 0
for i in range(len(card)-1):
    result += card[i] + card[i+1]
    card[i+1] = result
print(result)
