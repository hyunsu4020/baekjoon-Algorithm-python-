# 1       1칸  1
# 2 ~ 7   2칸  6
# 8 ~ 19  3칸  12
# 20 ~ 37 4칸  18
# 38 ~ 61 5칸  24
# 알고리즘: num | room | 6*cnt
# num[0]    | room = 1 | cnt = 0
# num[1:8]  | room = 2 | cnt = 1
# num[9:20] | room = 3 | cnt = 2

num = int(input())

line = 1
max_num = 1

if num == 1:
    print(1)
else:
    while True:
        max_num += (6 * line)
        line += 1
        if num <= max_num:
            print(line)
            break
