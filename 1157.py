words = input().upper() # 입력값 대문자로 변환
unique_words = list(set(words)) # 중복값 제외 ex) 2, 2 -> 2

cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])      # unique_words 와 cnt_list의 알파벳 index 위치는 동일하기 떄문에
