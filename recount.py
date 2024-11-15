import sys

votes = {}
for line in sys.stdin:
    if line != "***":
        name = line.strip()
        votes[name] = votes.get(name, 0) + 1

max_vote = max(votes.values())

winners = [name for name, value in votes.items() if value ==  max_vote]

if len(winners) == 1:
    print(winners[0])
else:
    print("Runoff!")