n = int(input())
letters = []
res = 0
for _ in range(n):
    letters.append(str(input()))

for i in range(len(letters) - 1, 0, -1):
    curr, prev  = letters[i], letters[i - 1]
    if curr == prev:
        res += 1
print(res)
