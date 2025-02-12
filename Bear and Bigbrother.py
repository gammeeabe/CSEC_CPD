# Read input values
a, b = map(int, input().split())

# Initialize year counter
years = 0

# Simulate the weight growth each year
while a <= b:
    a *= 3
    b *= 2
    years += 1

# Print the result
print(years)
