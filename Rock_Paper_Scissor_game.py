import random

# Define choices
choices = ["rock", "paper", "scissors"]

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the results
def display_results(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

# Main function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        # Get user's choice
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Get computer's choice
        computer_choice = get_computer_choice()
        
        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        # Display the results
        display_results(user_choice, computer_choice, winner)
        print(f"Score -> You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes or no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    play_game()
