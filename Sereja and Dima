# Read number of cards
n = int(input().strip())

# Read the list of cards
cards = list(map(int, input().split()))

# Initialize scores for Sereja and Dima
sereja_score = 0
dima_score = 0

# Start simulating the game
turn_sereja = True  # Sereja goes first

# While there are cards left to take
while cards:
    # Take the larger of the leftmost or rightmost card
    if cards[0] > cards[-1]:
        selected_card = cards.pop(0)
    else:
        selected_card = cards.pop()
    
    # Add the selected card to the current player's score
    if turn_sereja:
        sereja_score += selected_card
    else:
        dima_score += selected_card
    
    # Switch turns
    turn_sereja = not turn_sereja

# Print the final scores
print(sereja_score, dima_score)
