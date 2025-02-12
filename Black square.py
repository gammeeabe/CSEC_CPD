# Read input
a1, a2, a3, a4 = map(int, input().split())
s = input().strip()

# Calorie lookup table
calories = [0, a1, a2, a3, a4]  # Indexing from 1 for direct lookup

# Compute total calories
total_calories = sum(calories[int(c)] for c in s)

# Print the result
print(total_calories)
