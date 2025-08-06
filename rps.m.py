import random
def get_user_choice():
    choice=input("Enter your  choice (rock,paper,scissors):")
    while choice not in ['rock','paper','scissors']:
        choice=input("invalid input.please choose rock,paper,or scissors:")
    return choice
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])
def determine_winner(user,computer):
    if user==computer:
        return "tie"
    elif(user=="rock" and computer=="scissors") or (user=="scissors" and computer=="paper") or (user=="paper" and computer=="rock"):
        return "user"
    else:
        return "computer"
def play_game():
    user_score=0
    computer_score=0
    while True:
        user=get_user_choice()
        computer=get_computer_choice()
        print(f"\nYou chose:{user}")
        print(f"computer chose:{computer}")
        result=determine_winner(user,computer)
        if result=="tie":
              print("It's a tie!")
        elif result=="user":
            print("You win this round!")
            user_score +=1
        else:
            print("computer wins this round!")
            computer_score +=1
        print(f"\nscore->You:{user_score},computer:{computer_score}")
        play_again=input("\nDo you want to play again?(yes/no):")
        if play_again !="yes":
            print("\nThanks for playing!")
play_game()
        
        
