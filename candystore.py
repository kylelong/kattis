from collections import defaultdict

n, q = list(map(int, input().split()))
initials = defaultdict(list)

for _ in range(n):
    name = input()
    first, last = name.split()
    first_initial = first[0]
    last_initial = last[0]
    initial = first_initial + last_initial
    initials[initial].append(name)

for _ in range(q):
    s = input()
    if s in initials:
        if len(initials[s]) == 1:
            print(initials[s][0])
        else:
            print("ambiguous")
    else:
        print("nobody")
