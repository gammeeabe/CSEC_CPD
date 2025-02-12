# Read input
n = int(input().strip())  # Number of events
events = list(map(int, input().split()))  # List of events

# Initialize variables
available_officers = 0
untreated_crimes = 0

# Process events
for event in events:
    if event > 0:
        available_officers += event  # Recruit officers
    else:  # Crime occurs
        if available_officers > 0:
            available_officers -= 1  # Assign officer to crime
        else:
            untreated_crimes += 1  # No officer available

# Output result
print(untreated_crimes)
