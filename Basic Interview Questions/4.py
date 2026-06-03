# Count Vowels

s = "education"

count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print(count)