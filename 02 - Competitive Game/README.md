# Challenge 2 - Competitive Game
Suppose you have an `int` array and you're going to play a 2 player game. 

The game goes as follows:
- player A takes a subset of the array with an odd sum and removes it
- player B then takes a subset of the array with an even sum and removes it
- each player can take a max of 3 numbers per turn
- if a player can't make a move that player loses

The question: How do you tell who will win if they both play optimally? 

_Note: Player A ALWAYS goes first_
_Note: Each player has to take AT LEAST ONE number each time_

## Program specifications
- __Input__: `int` array
- __Output__: the player that wins