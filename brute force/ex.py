dwarf = []
for _ in range(9):
    a = int(input())
    dwarf.append(a)

one = 0
two = 0
for i in range(9):
    for j in range(i+1, 9):
        if sum(dwarf) - (dwarf[i] + dwarf[j]) == 100:
            one = dwarf[i]
            two = dwarf[j]
dwarf.remove(one)
dwarf.remove(two)
print('\n'.join(map(str, sorted(dwarf))))
