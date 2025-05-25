def run_game():
    while True:
        print("\nWelcome to War!")
        print("1. Start New Game")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            player1_name = input("Enter your name: ")
            # The game object will be created and run in game.py
            # so we just need to pass the player name to the game logic
            return player1_name
        elif choice == "2":
            print("Exiting...")
            return None
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    player1_name = run_game()
    if player1_name:
        # This part will be moved to game.py
        pass
