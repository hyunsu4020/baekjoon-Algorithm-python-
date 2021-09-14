t = int(input())

for x in range(t):
    cnt, word = input().split()
    for i in word:
        print(i*int(cnt), end = '') # end = '' 옆으로 붙임
    print() # 줄넘김 *\n은 아래쪽으로 한칸 띄우기라서 둘이 다르다
            # 줗넘김은 HTML의 <br>하고 같다
