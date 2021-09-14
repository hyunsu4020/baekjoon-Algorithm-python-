word = input()
alpabet = list(range(97, 123))

for x in alpabet:
    print(word.find(chr(x)))
# find함수는 index를 출력하다가 찾는 문자가 문자열에 포함되지 않으면 -1을 출력합니다.
