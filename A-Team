# Read the number of problems
n = int(input())

# Initialize counter for implementable problems
count = 0

# Process each problem
for _ in range(n):
    # Read the three friends' opinions
    p, v, t = map(int, input().split())
    
    # If at least two friends are sure, count the problem
    if p + v + t >= 2:
        count += 1

# Print the result
print(count)
