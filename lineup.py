n = int(input())

names = []
for _ in range(n):
    names.append(input())

dec = True
inc = True
for i in range(0, len(names) - 1):
    if names[i] < names[i + 1]:
        dec = False
    elif names[i] > names[i + 1]:
        inc = False

if dec:
    print("DECREASING")
elif inc:
    print("INCREASING")
else:
    print("NEITHER")