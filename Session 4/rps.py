"""
    File: rps.py
    @Brief: Demonstrates the game of rock, paper and scissors
            This is a very simple version for educational purpose.
            Students are expected to modify and make it better.
            
            Game rules:
            Rock beats scissors,
            Scissors beat paper
            Paper beats rock
    
    @Author: Pradeep Aryal(Keep your name here afterwards)
    Python Version: 3.6.1 
"""

# Globals 
player1 = input("\nEnter first player name: ")
player2 = input("Enter second player name: ")

def play_game(choice1, choice2):
    """Compares between choices of two players
       and returns the winner"""

    global player1, player2

    winner1 = player1 + " wins"
    winner2 = player2 + " wins"
    
    if choice1 == choice2:
        return("Tie")

    if choice1 == "rock":
        if choice2 == "paper":
            return(winner2)
        else:
            return(winner1)

    if choice1 == "paper":
        if choice2 == "scissors":
            return(winner2)
        else:
            return(winner1)

    if choice1 == "scissors":
        if choice2 == "rock":
            return(winner2)
        else:
            return(winner1)

    return("Invalid input!!! Please choose among rock, paper or scissors ") # Invalid choice
        
def main():
    print("Please choose among rock, paper or scissors ")

    while True:
        player1_choice = input("Enter your choice player1: ").lower()
        player2_choice = input("Enter your choice player2: ").lower()

        result = play_game(player1_choice, player2_choice)
        print(result)
        
        play_again = input("\nWould you like to play again yes/no: ")
        if play_again == "yes":
            continue
        else:
            break


if __name__ == "__main__":
    main()

    
    
