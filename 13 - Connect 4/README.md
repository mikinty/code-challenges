# Connect 4

Given an infinitely expanding horizontal board for Connect 4, implement a game
where players 1 and 2 drop in pieces from the top, and play Connect 4 as it is
otherwise played.

So imagine the following state for a game, where we have arbitrarily put some
column numbers and some pieces in:

```
     x  o
     x  o  o o x   x
...  _  _  _ _ _ _ _ ...
    -3 -2 -1 0 1 2 3
```

A winning condition is when one player has 4 pieces in a row, either
horizontally, vertically, or diagonally.

Your game should take in user input, and terminate when one player wins.

## Extensions

Can you make this game work for a general connect-N, where N pieces in a row
wins the game?

How would you make this game work if pieces were inserted in from the bottom?

How would you implement a printing function that is space efficient, i.e. if there are large gaps between pieces, how do you print out something that doesn't have too many empty columns?

How would you implement a UI to run this game and take in user input?