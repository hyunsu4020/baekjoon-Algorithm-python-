v = int(input())
vote = input()

if 1 <= v <= 15:
    if len(vote) == v:
        a = vote.count('A')
        b = vote.count('B')
        if a == b:
            print("Tie")
        elif a > b:
            print("A")
        elif a < b:
            print("B")

     
