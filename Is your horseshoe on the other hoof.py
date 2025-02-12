# Read input values and convert them to a set
horseshoes = set(map(int, input().split()))

# Compute and print the number of horseshoes Valera needs to buy
print(4 - len(horseshoes))
