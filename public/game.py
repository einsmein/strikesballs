import random

import config
import gen_num


def eval(make_guess, print_f=None, num_games=None, num_guess=None):
    """
    Use `make_guess` function to play 50 randomly selected numbers.

    args:
    - make_guess: A funtion that makes the next guess based on previous guesses.
        See `make_guess.py` for more details.
    - print_f: A function of a signature `print_f(i, guess, hint, mem)`
        where i: the number of guesses so far
              guess: this round guess
              hint: the number of strikes and balls for this guess
              mem: an object to store states of your choice
        This function will be called at the end of every guess, useful for debugging.

    Note: In addition to using print_f, it is possible to call `print` directly in
          `make_guess`. The output will be displayed on the console.
          It is also possible to directly call print instead of using `print_f` for debugging.
          The only difference is that `make_guess` doesn't know evaluation of the current move
          (But it will be added to history and show up in the next move.)
          I suggest using `print_f` for convenience and cleaner code.
    """

    nums = gen_num.generate()
    if num_games:
        nums = random.sample(nums, num_games)
    if not print_f:
        print_f = _print_f

    for num in nums:
        history = []
        mem = None
        while not history or history[-1][1][0] < config.NUM_DIGIT:
            if num_guess and len(history) >= num_guess:
                raise RuntimeError("Your algorithm is taking longer" \
                    " than {} moves to guess {}".format(num_guess, num))
            guess, mem = make_guess(history, mem, config.NUM_DIGIT)
            hint = eval_guess(guess, num)
            if print_f:
                print_f(len(history), guess, hint, mem)
            history += [(guess, hint)]


def eval_guess(guess, num):
    strike = 0
    ball = 0
    for i in range(config.NUM_DIGIT):
        if guess[i] == num[i]:     # strike
            strike += 1
        elif guess[i] in num:      # ball
            ball += 1
    return (strike, ball)


def _print_f(i, guess, hint, mem):
    print("[{}] guess: {}, sb: {}, mem: {}".format(i, guess, hint, mem))


if __name__ == "__main__":
    main()

