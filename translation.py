n = int(input())
words = list(map(str, input().split()))
translations = int(input())
maps = {}
for _ in range(translations):
    k, v = list(map(str, input().split()))
    maps[k] = v
for w in words:
    print(maps[w], end=" ")