# `rps.py` - code explained

This is a brief explanation of the `rps.py` program.

## What this program accomplishes

This program creates a little rock-paper-scissors game. You can choose how many times you want to play and tells individual scores of you and the computer at the end.

## How the script works

When you run the script, the following will be the output:

```
How many times do you want to play? Enter a number:
```

This is where you enter the number of rounds you want to play. Assume I enter 3. Now we see:

```
play:
```

This is where we play our option and choose between rock, paper and scissors. Assume we chose "rock". After that, we get a response from the computer and a result. If we won, the result would be:

```
You win.
```

If the computer won, the result would be:

```
I win.
```

If it's a draw, the result would be:

```
It's a draw :(
```

This repeats three times (since we selected to play 3 rounds) and then we get a total score as follows:

```
You = 2 ; Me = 1
```

This is what the script does. Now let's see how it works.

## What's inside

These are the elements of the script.

### Imports

I have used the `choice` class of the `random` library to make the computer return one of the options rock, paper, scissors.

```python
import random
```

### Variables

Then I have declared three variables `compwin`, `userwin` and `draww` to hold string values. I did this since I use these and compare these in one place and didn't want to risk spelling mistakes.

```python
compwin = "I win."
userwin = "You win."
draww = "It's a draw :("
```

Then I initialized two more variables `userWin` and `computerWin` which are used as counters to keep track of how many times each won. These are initialized with a value of zero.

```python
userWin = 0
computerWin = 0
```

### Methods

I have used two methods, `computerThrowHand` and `game`.

1. **The `computerThrowHand` method:**
    
    This method returns one of rock, paper and scissors and acts as the computer playing.
    
    ```python
    def computerThrowHand(options):
          return random.choice(options)
    ```
    
    `def computerThrowHand(options)` defines the `computerThrowHand` method and conveys that it takes an input `options` (which is a list) and returns one of the elements in that list. The `choice` class of the `random` library is used to accomplish this.
    
2. **The `game` method:**
    
    This method takes the user's hand and computer's hand as inputs and determines the result. The entire method is an `else-if` ladder and doesn't require further explanation.
    
    ```python
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
    ```
    

### Inputs and driver code

Now that we defined the required methods, we use these in the following code. These are the following things we will do to use all the code written:

1. **Input "rounds"**
We take the input for how many rounds the player wants to play against the computer.
    
    ```python
    rounds = int(input("How many times do you want to play? Enter a number: "))
    ```
    
2. **The game loop**
Now we define a `for` loop which runs for `rounds` number of times.
    
    ```python
    for i in range(rounds):
    ```
    
    In this loop, we initialize a list `options` with rock, paper and scissors as its elements.
    
    ```python
    options = ['rock', 'paper', 'scissors']
    ```
    
    Now, we take the user input:
    
    ```python
    option = input("play:").lower()
    ```
    
    We use the `lower` function to convert the input text into lowercase to avoid writing multiple cases for comparison.
    
    Now, we enter the game:
    
    ```python
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
    ```
    
    First, we check if the input we got is valid i.e. if the input is one of "rock", "paper" or "scissors". Then, we get the computer's play into a variable named `res` and we print it. Now, we initialize another variable `wl` to hold the result of the round we get from the `game` method and we print it. Now, we compare `wl` to `userwin` and `compwin` and count the results into the predefined variables `userWin` and `computerWin`.
    
    If the input is invalid, the output will be "Try again".
    
3. **Final result**
    
    In the end, we get the result of all the rounds combined. Only the win and lose rounds are accounted for and not the draw rounds.
    

## Counclusion

This is how the code works. Hope the explanation is understandable and useful.
