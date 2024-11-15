birthdays = {}

n = int(input())

for _ in range(n):
    name, rank, birthday = input().split()
    rank = int(rank)

    if birthday in birthdays:
        if rank > birthdays[birthday][1]:
            birthdays[birthday] = (name, rank)
    else:
        birthdays[birthday] = (name, rank)

names = [name for name, _ in birthdays.values()]
names.sort()

print(len(names))
for name in names:
    print(name)
