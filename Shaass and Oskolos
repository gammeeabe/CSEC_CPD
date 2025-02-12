# Read inputs
n = int(input())  # number of wires
a = list(map(int, input().split()))  # list of bird counts on each wire
m = int(input())  # number of shots

# Process each shot
for _ in range(m):
    xi, yi = map(int, input().split())  # wire xi, bird position yi
    xi -= 1  # Convert 1-based to 0-based index
    yi -= 1  # Convert 1-based to 0-based index
    
    # Calculate the number of birds to move
    birds_to_move_up = yi
    birds_to_move_down = a[xi] - (yi + 1)
    
    # Move birds to the appropriate wires
    if xi > 0:
        a[xi - 1] += birds_to_move_up
    if xi < n - 1:
        a[xi + 1] += birds_to_move_down
    
    # The current wire loses all birds
    a[xi] = 0

# Print the final number of birds on each wire
for birds in a:
    print(birds)
