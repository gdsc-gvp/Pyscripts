import random

compwin = "I win."
userwin = "You win."
draww = "It's a draw :("

userWin = 0
computerWin = 0

def computerThrowHand(options):
    return random.choice(options)

def game(option, res):
    # rock

    if(option == 'rock' and res == 'rock'):
        return draww
    elif(option == 'rock' and res == 'paper'):
        return compwin
    elif(option == 'rock' and res == 'scissors'):
        return userwin
    
    # paper
    
    elif(option == 'paper' and res == 'rock'):
        return userwin
    elif(option == 'paper' and res == 'paper'):
        return draww
    elif(option == 'paper' and res == 'scissors'):
        return compwin
    
    #scissors
    
    elif(option == 'scissors' and res == 'rock'):
        return compwin
    elif(option == 'scissors' and res == 'paper'):
        return userwin
    elif(option == 'scissors' and res == 'scissors'):
        return draww


rounds = int(input("How many times do you want to play? Enter a number: "))

for i in range(rounds):
    options = ['rock', 'paper', 'scissors']
    option = input("play: ").lower()
    if option in options:
        res = computerThrowHand(options)
        print(res)
        wl = game(option, res)
        print(wl)
        if wl == userwin:
            userWin += 1
        elif wl == compwin:
            computerWin += 1
        else:
            pass
    else:
        print("Try again")
print("You =", userWin, "; Me =", computerWin)
