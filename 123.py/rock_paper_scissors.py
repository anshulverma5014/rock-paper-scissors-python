import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "Draw 🤝"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You Win 🎉"
    else:
        return "Computer Wins 🤖"

def play_game():
    print("🎮 Rock Paper Scissors Game")
    print("Type 'exit' to quit\n")

    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()

        if user_choice == "exit":
            print("Game Over 👋")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice, try again!\n")
            continue

        computer_choice = get_computer_choice()

        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)
        print(f"🏆 Result: {result}\n")

if __name__ == "__main__":
    play_game()