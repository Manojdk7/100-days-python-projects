import random
from hangman_words import word_list
from hangman_art import stages, logo

def play_hangman():
    """Main hangman game function"""
    print(logo)
    
    # Initialize game variables
    chosen_word = random.choice(word_list)
    lives = 6
    guessed_letters = []
    game_over = False
    
    while not game_over:
        # Get player guess
        print(f"\n****You have {lives} lives left.****")
        guess = input("Guess a letter: ").lower()
        
        # Check if letter already guessed
        if guess in guessed_letters:
            print(f"You have already guessed the letter '{guess}'.")
            continue
        
        guessed_letters.append(guess)
        
        # Build display word
        display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        
        print("Word: " + display)
        
        # Check if guess is correct
        if guess not in chosen_word:
            lives -= 1
            print(f"The letter '{guess}' is not in the word. You lose a life.")
        
        # Check win/lose conditions
        if "_" not in display:
            game_over = True
            print("You won!")
        elif lives == 0:
            game_over = True
            print(f"You lose. The word was: {chosen_word}")
        
        print(stages[lives])

# Run the game
if __name__ == "__main__":
    play_hangman()
