# readonly section

def make_guess(history, mem, num_digit=4):
    """
    Algorithm that makes the next guess based on previous guesses (history).

    args:
    - history: A list of tuples. Each tuple element comprises a guess and its result
            [((1,2,3,4), (2,1)), ((3,4,5,6), (0,2)), ...]
    - mem: An argument that is being passed through to the next guess.
        It can be used to store any state that could be useful for processing.
        To store multiple values, make it a dictionary.
    """


    if not history and not mem:
        return ((0,1,2,3), 0)
    # for move in history:
    move = list(history[-1][0])
    strike = history[-1][1][0]
    ball = history[-1][1][1]

    if mem == num_digit:
        raise RuntimeError("I'm out of guess")

    pos = mem
    for _ in range(num_digit):
        tmp = move[pos]
        new = tmp + 1
        move[pos] = -1
        while new in move and new < 9:
            new += 1
        if new in move or new > 9:
            move[pos] = tmp
            pos = (pos + 1) % num_digit
        else:
            move[pos] = new
            return (tuple(move), mem)

    mem += 1
    for i in range(num_digit):
        move[(mem + i) % num_digit] = i

    return (tuple(move), mem)

def print_f(i, guess, hint, mem):
    """
    A function of a signature `print_f(i, guess, hint, mem)`
        where i: the number of guesses so far
              guess: this round guess
              hint: the number of strikes and balls for this guess
              mem: an object to store states of your choice
        This function will be called at the end of every guess, useful for debugging.
    """

    print("[{}] guess: {}, sb: {}, mem: {}".format(i, guess, hint, mem))

