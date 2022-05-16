# Challenge 24

Challenge 24 is a math game where you are given 4 numbers, usually integers, and
you have to perform 3 operations on the 4 numbers, with any combination of
parentheses, to achieve 24. For example, if we are given the numbers

```text
4, 1, 5, 8
```

We can get to 24 by doing (5^(8/4) - 1) = 25 - 1 = 24. There are variations of
the game where only *, /, -, and + are allowed, but in general any arithmetic
operation is allowed.

The goal of this problem is to implement a function that takes in 4 numbers, and
outputs either:

- True if there is a solution
- False if there is not a solution

## Extension

Can you also print out the parenthesized-solution? I.e. print out how to get to
the answer (so someone can verify it)