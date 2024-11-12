import random


# Rock beats Scissors (Rock crushes Scissors)
# Scissors beats Paper (Scissors cut Paper)
# Paper beats Rock (Paper covers Rock)

def get_user_choice():

    print("Enter your choice user: Rock, Paper, or Scissor")
    choice = input().lower()

    while choice not in ['rock', 'paper', 'scissor']:
        print("Invalid choice! Please choose Rock, Paper, or Scissor.")
        choice = input().lower()
    
    return choice


def get_comp_choice():
        return random.choice(['rock', 'paper', 'scissor'])


def determine_winner(user_choice, comp_choice):
     
    if user_choice==comp_choice:
        return "its a draw between both user and computer"
    elif(((user_choice=='rock' and comp_choice=='scissor')) or ((user_choice=='scissor') and (comp_choice=='paper'))
                or ((user_choice=='paper') and (comp_choice=='rock'))):
         return "you win!!!!!!!!!"
    else:
         return "computer Wins!!!!!"        

    

def play_game():
    print("\n")

    print("lets play rock paper scissor game!!!!!")
    print("\n")

    user_choice=get_user_choice()
    comp_choice=get_comp_choice()
    print("\n")
    print(f"your choice is: {user_choice.capitalize()}")
    print(f"computer selects randomly: {comp_choice.capitalize()}")
    print("\n")

    result = determine_winner(user_choice, comp_choice)
    print(result)


play_game()