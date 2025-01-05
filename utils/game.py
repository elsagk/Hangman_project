from typing import List, Optional
import random

class Hangman:
    def __init__(self, 
                 possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions'],
                 word_to_find: Optional[List[str]] = None,
                 lives: int = 5,
                 correctly_guessed_letters: Optional[List[str]] = None,
                 wrongly_guessed_letters: Optional[List[str]] = None,
                 turn_count: int = 0,
                 error_count: int = 0):
        self.possible_words = possible_words
        self.word_to_find = word_to_find or list(random.choice(self.possible_words))
        self.lives = lives
        self.correctly_guessed_letters = correctly_guessed_letters or ['_' for _ in self.word_to_find]
        self.wrongly_guessed_letters = wrongly_guessed_letters or []
        self.turn_count = turn_count
        self.error_count = error_count

    def play(self):
        """Handle the player's guess and update the game state."""
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            if guess in self.correctly_guessed_letters or guess in self.wrongly_guessed_letters:
                print("You already guessed this letter. Try again.")
                continue
            break

        self.turn_count += 1
        if guess in self.word_to_find:
            print("Correct!")
            for i, letter in enumerate(self.word_to_find):
                if letter == guess:
                    self.correctly_guessed_letters[i] = guess
        else:
            print("Wrong guess!")
            self.wrongly_guessed_letters.append(guess)
            self.lives -= 1
            self.error_count += 1

    def start_game(self):
        """Start the Hangman game."""
        while self.lives > 0:
            print(f"Turn: {self.turn_count + 1}")
            print(f"Word: {' '.join(self.correctly_guessed_letters)}")
            print(f"Lives: {self.lives}")
            print(f"Wrong guesses: {', '.join(self.wrongly_guessed_letters)}")
            
            if '_' not in self.correctly_guessed_letters:
                self.well_played()
                return

            self.play()

        self.game_over()

    def game_over(self) -> None:
        """Handle the game over state."""
        print("Game over...")

    def well_played(self) -> None:
        """Handle the victory state."""
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")


