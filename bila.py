s = str(input())
res = ''
size = len(s)
for c in range(0, size - 1):
    if s[c] != s[c + 1]:
        res += s[c]
    else:
        continue
print(res + s[size - 1])
    