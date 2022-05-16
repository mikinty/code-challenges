# Tetris

Implement a Tetris game.

This problem can be pretty open-ended, especially depending on what language you're using, but in increasing completeness:

1. Implement the logic of the tetris game, which includes generating pieces, and having them drop one row at a time
  - We can assume a tetris board is 10x20 for now, and there are only 7 types of pieces. You can find these pieces [here](https://tetris.fandom.com/wiki/Tetromino).
3. Implement the ability to rotate the current active piece
4. Implement row clearing logic, so when a row is full, it clears. Make sure to update the player's score as well
5. Implement the hard-drop ability, which drops the current active piece to as far bottom as possible
6. Implement graphics for the game