k = int(input())
friends = input()
mine = input()

same = 0
questions = len(friends)

for n in range(questions):
    if friends[n] == mine[n]:
        same += 1


if same == 0:
    print(questions - k)
else:
    print(questions - abs(k - same))