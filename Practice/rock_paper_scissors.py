import random
def win(choice,comp):
    if choice == "ROCK" and comp == "SCISSORS":
        return True
    elif choice == "PAPER" and comp == "ROCK":
        return True
    elif choice == "SCISSORS" and comp == "PAPER":
        return True
    else:
        return False
def playerwins(choice):
    choices = {'r':'ROCK', 's':'SCISSORS', 'p':'PAPER'}
    if choice in choices:
      choice = choices.get(choice)
    else:
      choice = input("\nThat's not a valid choice. Try again: ")
    comp = random.choice([choices.get(i) for i in choices.keys()])
    print("\nIt's " + choice  + " vs... " + comp)
    if choices.get(choice) == comp:
        print("\nIt's a draw")
        playerwins(input("\nMake your choice, rock(r), paper (p) or scissors(s)"))
    elif win(choice,comp):
        print("\nThat's a win.")
        return True
    else:
        print("\nNot a win this time.")
        return False

print("Welcome to Rock, Paper and Scissors!\n")
n = int(input("Until what score would you like to play? "))
comp_score = 0
score = 0
while comp_score < n and score < n:
    if playerwins(input("\nMake your choice, rock(r), paper (p) or scissors(s): ")):
        score += 1
    else:
        comp_score += 1
    print("\nYour score: {0}, Computer score: {1}".format(score,comp_score))
    print("________________________________________")
if score == n:
  print("\nYou won!")
else:
  print("\nGame Over!")