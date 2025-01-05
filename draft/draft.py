
def get_word() -> str:
    """Prompts the player in order  to choose a word for the game."""
    word = input("Enter the word to guess: ").strip().lower() 
    return word

def get_lives() -> int:
    """Prompts the player to choose the number of lives.
    to specify how many lives the guesser have to try to guess the word  during the game."""
    lives = int(input("Enter the number of lives: "))
    return lives

def get_guess(suggested_letters: list[str]) -> str:
    """Prompts the user for a guess, checks if it's valid and returns the guessed letter"""
    while True:
        # check if user gives more than one letter, prompt again
        guess = input("guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter, Invalid Input")
        elif guess in suggested_letters:
            print("You already guessed this letter.")
        else:
            return guess

def assess_guess(secret_word: str, guessed_letter: str, lives_left: int) -> int:
    """Assesses the guess and returns the current lives of the player depending on the outcome of the guess."""
    if guessed_letter in secret_word:
        print(f"Correct guess: {guessed_letter}")
    else:
        print(f"Incorrect guess: {guessed_letter}")
        lives_left = lives_left-1
       
    return lives_left

def display_word(secret_word: str, suggested_letters: list) -> bool:
    """Displays the word with guessed letters and underscores for unguessed ones."""
    displayed_word = [letter if letter in suggested_letters else '_' for letter in secret_word]
    print(" ".join(displayed_word))
    return '_' not in displayed_word

def main():
    """Main game loop."""
    secret_word = get_word()
    lives = get_lives()
    suggested_letters = []
    
    while lives > 0:
        print(f"Lives left: {lives}")
        if display_word(secret_word, suggested_letters):
            print("You guessed the word!")
            break
        guess = get_guess(suggested_letters)
        suggested_letters.append(guess)
        lives = assess_guess(secret_word, guess, lives)
    else:
        print(f"Game over! The word was {secret_word}")


# # Call main() to start the game
# if __name__ == "__main__":
#     main()

