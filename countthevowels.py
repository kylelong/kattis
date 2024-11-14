s = str(input())
s = s.lower()
vowels = "aeiou"
count = sum(1 for c in s if c in vowels)
print(count)