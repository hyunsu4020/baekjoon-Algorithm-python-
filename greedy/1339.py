import sys

input = sys.stdin.realin()
n = int(input())

alpha = []          # 단어 저장
alpha_dict = {}     # 단어 내의 알파벳 별로 수를 저장할 딕셔너리
numList = []        # 수를 저장할 리스트

for i in range(n):  # 단어 입력
    alpha.append(input().rstrip())      # rstrip(): 오른쪽 공백 제거

for i in range(n):
    for j in range(len(alpha[i]))       #  입력받은 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict:   #  alpha이 이미 dict에 있으면
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1)
