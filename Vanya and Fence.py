# Read input values
n, h = map(int, input().split())
a = list(map(int, input().split()))

# Calculate minimum road width
width = sum(1 if height <= h else 2 for height in a)

# Print result
print(width)
