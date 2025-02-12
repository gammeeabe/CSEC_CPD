import math

# Read input values
Y, W = map(int, input().split())

# Find the maximum value Yakko or Wakko rolled
max_value = max(Y, W)

# Compute favorable outcomes
numerator = 6 - max_value + 1
denominator = 6

# Simplify the fraction
gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

# Print the result
print(f"{numerator}/{denominator}")
