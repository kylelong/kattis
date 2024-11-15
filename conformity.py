
n = int(input())

courses = {}

for _ in range(n):
    selection = tuple(sorted(map(int, input().split())))
    courses[selection] = courses.get(selection, 0) + 1

max_freq = max(courses.values())


result = sum(count for count in courses.values() if count == max_freq)

print(result)

    