# Read the input word
s = input().strip()

# Count uppercase and lowercase letters
uppercase_count = sum(1 for c in s if c.isupper())
lowercase_count = len(s) - uppercase_count

# Convert based on majority case
if uppercase_count > lowercase_count:
    print(s.upper())
else:
    print(s.lower())
