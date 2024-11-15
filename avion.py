import sys

count = 0
res = []
for line in sys.stdin:
    count += 1
    if "FBI" in line:
        res.append(count)

res.sort()
if len(res) > 0:
    for n in res:
        print(n, end=" ")
else:
    print("HE GOT AWAY!")
