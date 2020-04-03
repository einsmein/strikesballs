# Strikes & Balls

## Rule

Purpose of `strikes & balls` is to guess a 4-digit number with 
minimum number of tries. All digits are different in this game.
After each guess, a player gets a hint of how many digit 
are included and correctly positioned (strike), 
and how many are included but not in the right position (ball).
Based on a sequence of these tries (history), a player can make 
the next guess that would be most informative of what the number is.


## Game-Player Game

The game here is not to guess a number, but to create an algorithm
that would do so most efficiently. To evaluate an algorithm,
it will play 5040 games (all possible combinations). The maximum 
number of tries took in those games is the score of the algorithm.
Obviously the lower the better.


### Implementation

A 4-digit number is represented by a tuple e.g. `(1,2,3,4)`.
A guess with its hint is a tuple of 4-digit number and
a tuple of `(#strikes, #balls)` of that guess e.g.
`((1,2,3,4), (2,1))`. Then sequence of guesses and hints (history)
is a list of those tuples.

A function takes `history`, `memories`, `number of digits` 
as arguments. Based on those, it makes a next guess.
- `history`: A list of tuples. Each tuple element comprises a guess 
and its result e.g. `[((1,2,3,4), (2,1)), ((3,4,5,6), (0,2)), ...]`
- `mem`: An argument that is being passed through to the next guess.
Use it to store any state that could be useful for processing.
To store multiple values, make it a dictionary.

See example in `make_guess.py`, or click `Reset` if you're on a browser version.

> ## NB! Watch out for infinite loop
> Make sure you don't have an infinite loop in your function! 
> JS being single threaded makes it cumbersome to set a timer if possible at all.
> You can do something like this and check time lapse in every loop,
> but that can significantly impact the overall execution time.
>
> ```
> def make_guess(history, mem, num_digit=4):
>     ...
> 
>     from datetime import datetime
>     if not history and not mem:
>         start_time = datetime.utcnow()
>         mem = {"start_time": start_time}
>         return ((0,1,2,3), mem)
> 
>     # Check time lapse in every loop as a fool-proof solution
>     timeout = 30
>     while some_condition:
>         if (datetime.utcnow() - start_time).total_seconds() > timeout:
>             raise RuntimeError("The algorithm is taking longer"\
>                 " than {} seconds to guess {}".format(timeout, num))
>         while another_condition:
>             if (datetime.utcnow() - start_time).total_seconds() > timeout:
>                 raise RuntimeError("The algorithm is taking longer"\
>                     " than {} seconds to guess {}".format(timeout, num))
>     ...
> ```
> 
> If you run locally, one thing you can do is using a background 
> [thread](https://docs.python.org/3/library/threading.html).
> Keep timer in the main thread, then join (kill it)  when time is up.


### Evaluation

#### On a browser
Using this editor, 30 random games (randomly selected 
out of 5040 possible games) are used to evaluate the algorithm. 
Also, the number of guesses for each game is limited to 15.
If your algorithm takes 15 guesses for all those 30 games,
it could take around a minute to run.
The browser version uses [Brython](https://brython.info/) which
implements python 3 in javascript and run completely on the
client side (your browser). Naturally, performance suffers to
certain extent. (See comparison with CPython 
[here](https://brython.info/speed_results.html).)


#### On your machine
You are free to set the number of games and guess limit.
See documentation of `eval` in `game.py`.
To get a score of your algorithm `make_guess`, do

```
import game

game.eval(make_guess)
```



### Extension?
- Generalize base, number of digits
