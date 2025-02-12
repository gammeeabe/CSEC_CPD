# Read input string
s = input().strip()

# Initialize starting position at 'a'
current = 'a'
total_moves = 0

# Iterate through each character in the string
for char in s:
    # Compute the direct distance and wrap-around distance
    direct = abs(ord(char) - ord(current))
    wrap_around = 26 - direct  # Wrapping around the alphabet
    
    # Add the minimum of the two distances
    total_moves += min(direct, wrap_around)
    
    # Move the pointer to the current character
    current = char

# Print the result
print(total_moves)
