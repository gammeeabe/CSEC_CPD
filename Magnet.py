def count_magnet_groups():
    n = int(input().strip())  # Read number of magnets
    prev_magnet = input().strip()  # Read the first magnet
    groups = 1  # Initialize groups count
    
    for _ in range(n - 1):
        current_magnet = input().strip()
        if current_magnet != prev_magnet:
            groups += 1
        prev_magnet = current_magnet  # Update the previous magnet
    
    print(groups)

# Run the function
count_magnet_groups()
