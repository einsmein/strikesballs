num_digit = 4

def main(make_guess):
    try:
        num = gen_num()
        history = []
        while not history or history[-1][1][0] < num_digit:
            if len(history) > 5:
                raise RuntimeError("YOU SUCK")
            guess = make_guess(history)
            hint = eval_guess(guess, num)
            history += [(guess, hint)]
            print("*", history, guess, hint)
            print(not history or history[-1][1][0] < num_digit)

    except Exception as exc:
        print(exc)

# history [((1,2,3,4), (2,1)), ((3,4,5,6), (0,2)), ...]
#          ((guessed), (s,b))

def gen_num():
    num = 1234
    num = [ num // 10 ** (3-i) % 10 for i in range(num_digit)]
    return tuple(num)

def eval_guess(guess, num):
    strike = 0
    ball = 0
    for i in range(num_digit):
        if guess[i] == num[i]:     # strike
            strike += 1
        elif guess[i] in num:      # ball
            ball += 1
    return (strike, ball)

def test(f):
    f(1)

if __name__ == "__main__":
    main()

# def get_digits(number):
#     return [ number // 10 ** (3-i) % 10 for i in range(num_digit)]

