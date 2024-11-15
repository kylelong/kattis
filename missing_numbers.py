# Step 1: Read input
n = int(input())
numbers = {int(input()) for _ in range(n)}

min_num, max_num = min(numbers), max(numbers)

missing_numbers = sorted(set(range(1, max_num + 1)) - numbers)
if missing_numbers:
    for n in missing_numbers:
        print(n)
else:
    print("good job")
