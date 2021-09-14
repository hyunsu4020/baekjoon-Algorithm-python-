n = int(input())

group_words = 0
for _ in range(n):
    words = input()
    error = 0
    for index in range(len(words)-1):
        if words[index] != words[index+1]:
            new_words = words[index+1:]
            if new_words.count(words[index]) > 0:
                error += 1
    if error == 0:
        group_words += 1
print(group_words)
