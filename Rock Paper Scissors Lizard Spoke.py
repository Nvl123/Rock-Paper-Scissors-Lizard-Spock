import random

print("""
====================================
  Rock Paper Scissors Lizard Spock
====================================    
      
1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
-------------------------------------      
6) Show The rules
7) Exit
      
""")

game_choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
    4: "Lizard",
    5: "Spock"}

exit_game = True
computer_choice = random.randint(1, 5)

while exit_game == True:

    user_choice = (input("Enter your choice: "))

    try:
        user_choice = int(user_choice)

        if user_choice > 7 or user_choice < 1:
            raise ValueError("Invalid choice Please choise between 1 to 7")

    except ValueError:
        print(f"{user_choice} must be a number, please try again.")
        continue

    computer_choice = random.randint(1, 5)

    if user_choice == 7:
        print("Exiting the game...")
        exit_game = False
        break
    elif user_choice == 6:
        print("""
        Rules:
        1) Rock crushes Scissors
        2) Scissors cuts Paper
        3) Paper covers Rock
        4) Rock crushes Lizard
        5) Lizard poisons Spock
        6) Spock smashes Scissors
        7) Scissors decapitates Lizard
        8) Lizard eats Paper
        9) Paper disproves Spock
        10) Spock vaporizes Rock
        """)
        print("Let's play again! \n")
        continue

    elif user_choice == computer_choice:
        print(f"your choice {game_choices[user_choice]} and computer choice {game_choices[computer_choice]}")
        print("It's a tie!")
        print("------------------------------------- \n")
        continue
    elif user_choice == 1 and computer_choice == 2: 
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Paper covers Rock")
        print("------------------------------------- \n")

    elif user_choice == 1 and computer_choice == 3:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Rock crushes Scissors")
        print("------------------------------------- \n")

    elif user_choice == 1 and computer_choice == 4:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Rock crushes Lizard")
        print("------------------------------------- \n")

    elif user_choice == 1 and computer_choice == 5:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Spock vaporizes Rock")
        print("------------------------------------- \n")

    elif user_choice == 2 and computer_choice == 1:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Paper covers Rock")
        print("------------------------------------- \n")

    elif user_choice == 2 and computer_choice == 3:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Scissors cuts Paper")
        print("------------------------------------- \n")

    elif user_choice == 2 and computer_choice == 4:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Lizard eats Paper")
        print("------------------------------------- \n")

    elif user_choice == 2 and computer_choice == 5:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Paper disproves Spock")
        print("------------------------------------- \n")

    elif user_choice == 3 and computer_choice == 1:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Rock crushes Scissors")
        print("------------------------------------- \n")

    elif user_choice == 3 and computer_choice == 2:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Scissors cuts Paper")
        print("------------------------------------- \n")

    elif user_choice == 3 and computer_choice == 4:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Scissors decapitates Lizard")
        print("------------------------------------- \n")

    elif user_choice == 3 and computer_choice == 5:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Spock smashes Scissors")
        print("------------------------------------- \n")

    elif user_choice == 4 and computer_choice == 1:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Rock crushes Lizard")
        print("------------------------------------- \n")

    elif user_choice == 4 and computer_choice == 2:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Lizard eats Paper")
        print("------------------------------------- \n")

    elif user_choice == 4 and computer_choice == 3:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Scissors decapitates Lizard")
        print("------------------------------------- \n")

    elif user_choice == 4 and computer_choice == 5:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Lizard poisons Spock")
        print("------------------------------------- \n")

    elif user_choice == 5 and computer_choice == 1:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Spock vaporizes Rock")
        print("------------------------------------- \n")

    elif user_choice == 5 and computer_choice == 2:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Paper disproves Spock")
        print("------------------------------------- \n")

    elif user_choice == 5 and computer_choice == 3:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You win! Spock smashes Scissors")
        print("------------------------------------- \n")

    elif user_choice == 5 and computer_choice == 4:
        print(f"your choice {game_choices[user_choice]} : computer choice {game_choices[computer_choice]}")
        print("You lose! Lizard poisons Spock")
        print("------------------------------------- \n")
    else:
        print(f"{user_choice} is Invalid choice, please try again.")
        print("------------------------------------- \n")



