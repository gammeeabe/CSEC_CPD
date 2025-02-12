# Read input
n = int(input().strip())  # Number of stones
s = input().strip()  # The stone colors in a row

# Initialize counter for removals
removal_count = 0

# Iterate over the string and count adjacent duplicates
for i in range(1, n):
    if s[i] == s[i-1]:  # If adjacent stones are the same
        removal_count += 1

# Print the result
print(removal_count)
