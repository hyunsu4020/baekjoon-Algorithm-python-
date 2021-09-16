x = int(input())

line = 1
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x
print(a, b, sep = "/")

# 1 | 1/1                 (1)
# 2 | 1/2 2/1             (2,3)
# 3 | 3/1 2/2 1/3         (4,5,6)
# 4 | 1/4 2/3 3/2 4/1     (7,8,9,10)
# 5 | 5/1 4/2 3/3 2/4 1/5 (11,12,13,14,15)
#                     .
#                     .
#                     .
