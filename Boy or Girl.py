# Read the username
username = input().strip()

# Count distinct characters
distinct_chars = len(set(username))

# Determine the output based on even or odd count
if distinct_chars % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
