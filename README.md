# texas-holdem-python
experimenting with simulating games of texas holdem in python

Current: simulates a game of texas hold em, does not calculate the winning hand yet. 
playHand() correctly follows the order of events in a hand and returns the winner, or 0 if multiple players are still in at the end
actionPhase() correctly gets actions from all players starting at index 0, correctly handles betting (fold, check/call, raise)

Next TODO: write function to calculate the winning hand if multiple players don't fold
Next TODO: write additional modes/getAction() in player class to allow cpu players using random actions or machine learning
Next TODO: modify print statements/functions to make output look better for user
Next TODO: make a gui to display the game so it looks prettier than standard output
