

def minimax(state, turn):
    state = state.copy()
    best = -1
    best_val = -10
    for i in range(9):
        if (state[i] == -1):
            state[i] = 1
            val = minimax_helper(state, turn +1)

            
            if (val > best_val):
                best_val = val
                best = i
            state[i] = -1
    print(best_val)
    return best



def minimax_helper(state, turn):
    state = state.copy()

    win = check_winner(state)
    if (win == -1 or win == 1 or turn > 8):
        return win
    
    best_val = -10
    for i in range(9):
        if (state[i] == -1):
            state[i] = turn % 2
            val = minimax_helper(state, turn + 1)


            if (val > best_val and turn % 2 == 1):
                best_val = val
            if ((val < best_val and turn % 2 == 0) or best_val == -10):
                best_val = val

            state[i] = -1
    return best_val




def check_winner(state):
    # Define the winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # Check for a winner
    for combo in winning_combinations:
        if (state[combo[0]] == state[combo[1]] and state[combo[1]] == state[combo[2]] and state[combo[1]] != -1):
            return (state[combo[0]] % 2) * 2 - 1 # Return the winning player (-1 or 1)

    # If no winner, return 0
    return 0