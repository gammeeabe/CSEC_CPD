def gravity_flip():
    # Read input
    n = int(input())  # Number of columns
    cubes = list(map(int, input().split()))  # List of cubes in each column
    
    # Sort cubes in ascending order
    cubes.sort()
    
    # Print the sorted list
    print(" ".join(map(str, cubes)))

# Run the function
gravity_flip()
