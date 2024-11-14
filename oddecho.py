n = int(input())
index = 1
for _ in range(n):
    s = str(input())
    if index % 2 == 1:
        print(s)
    index += 1