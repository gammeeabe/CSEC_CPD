# Read the number of teams
n = int(input().strip())

# Store home and guest uniform colors
teams = [tuple(map(int, input().split())) for _ in range(n)]

# Count the number of times a home team has to change uniform
count = 0

# Iterate through all pairs of teams (i as home, j as guest)
for i in range(n):
    for j in range(n):
        if i != j:  # Ensure it's a valid match
            # Compare home team's home uniform with guest team's guest uniform
            if teams[i][0] == teams[j][1]:  
                count += 1

# Print the result
print(count)
