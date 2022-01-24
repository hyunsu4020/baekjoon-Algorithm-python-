import sys

input = sys.stdin.readline
n = int(input())

alpha_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
            'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
            'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
                                                   # 단어 내의 알파벳 별로 수를 저장할 딕셔너리
alpha_list = []     # 단어 저장
numList = []        # 수를 저장할 리스트

sum = 0
for _ in range(n):  # 단어 입력
    numList.append(input().rstrip())      # rstrip(): 오른쪽 공백 제거

for i in numList:
    for j in range(len(i)):
        alpha_dict[i[j]] += 10 ** (len(i)-j-1)

for i in alpha_dict.values():   # dict에 저장된 수들을 모두 리스트에 추가
    if i > 0:
        alpha_list.append(i)

sorted_list = sorted(alpha_list, reverse=True)      # 내림 차순 정렬
for i in range(len(sorted_list)):
    sum += sorted_list[i] * (9-i)   # 첫 부분에 9를 * 내려갈 수록 -1씩 다운해서 *

print(sum)
