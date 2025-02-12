# Read the 5x5 matrix
matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the position of '1'
for r in range(5):
    for c in range(5):
        if matrix[r][c] == 1:
            # Calculate Manhattan distance to the center (3,3)
            moves = abs(r - 2) + abs(c - 2)
            print(moves)
            break
