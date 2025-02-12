# Read input strings
s = input().strip()
t = input().strip()

# Initial position (1-based index)
position = 0  

# Process each instruction
for instruction in t:
    if s[position] == instruction:
        position += 1  # Move forward

# Output final position (1-based)
print(position + 1)
