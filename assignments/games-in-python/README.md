
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game using Python strings, loops, conditionals, and user input. You will practice managing game state as players guess letters and work to reveal a hidden word.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Use the provided list of words to choose a random secret word, then create the variables needed to track the player's guesses and remaining incorrect attempts.

#### Requirements
Completed program should:

- Randomly select one word from the predefined `words` list.
- Create a collection to store letters guessed by the player.
- Set a maximum number of incorrect guesses and track the guesses remaining.

### 🛠️	Build the Guessing Loop

#### Description
Create a loop that displays the player's progress, accepts one letter at a time, and updates the game until the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Display the secret word with guessed letters visible and unguessed letters shown as underscores, such as `_ _ _ _ _ _`.
- Accept letter guesses and update the displayed progress after each valid guess.
- Decrease the remaining attempts only when the player guesses a letter that is not in the secret word.
- End the game with a clear win message when the word is guessed or a clear lose message when attempts are exhausted.
