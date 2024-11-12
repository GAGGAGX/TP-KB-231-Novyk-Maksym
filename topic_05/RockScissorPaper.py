from random import choice

listChoice = ['stone', 'scissors', 'paper']

def inp():
    while True:
        per = input("stone, scissors, paper\nEnter your choice: ").lower().strip()
        if per in listChoice:
            return per
        else:
            print("Selection error.\n")

def game(per):
    botChoice = choice(listChoice)
    winList = ['stonescissors', 'scissorspaper', 'paperstone']
    if per == botChoice:
        print("Draw.")
    else:
        if (per+botChoice) in winList:
            print("You win!")
        else:
            print("You lose.")


per = inp()
game(per)

