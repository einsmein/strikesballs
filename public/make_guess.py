def make_guess(history, num_digit=4):
    # for move in history:
    if not history:
        return (0,1,2,3)
    move = history[-1]
    strike = move[1][0]
    ball = move[1][1]
    if strike < num_digit:
        guess = []
        pos = num_digit - 1
        while pos >= 0:
            if move[0][pos] < 9:
                guess = [move[0][pos] + 1] + guess
                break
            else:
                guess = [move[0][pos]] + guess
                pos -= 1

        while len(guess) < num_digit:
            guess = [move[0][num_digit - len(guess) - 1]] + guess

    return tuple(guess)
