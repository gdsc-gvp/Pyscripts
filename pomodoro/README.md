# `pomo.py` - code explained

This is a brief explanation of the `pomo.py` program.

## What this program accomplishes

This program creates a Pomodoro stop clock that keeps track of the task you complete in the set Pomodoro cycle. The task you will work on and the time when the cycle began is logged into a text file in the same folder as the script. A `log.txt` file must be present in the folder for the logging to work.

## How the script works

When you run the script, the following will be the output:

```
Enter the number of rounds:
```

This is where you enter the number of cycles you want to work on for a task. Assume I enter 1. Now we see:

```
Select the duration of the pomo:
		1. 25 minutes, 5 minutes.
		2. 50 minutes, 10 minutes.
		Enter one of the above only.
		If you get naughty, I will choose for you.

Enter duration:
```

This is where we select the duration of each cycle in the pomo. The format of the duration is:

cycle duration, break duration.

This means if you choose option 1, you work for 25 minutes and take a 5-minute break. And if you choose option 2, you work for 50 minutes and take a 10-minute break.

If you choose an option other than 1 and 2, the program defaults to option 1 which is 25 minutes and 5 minutes.

Assume we chose 1, now we get the following:

```
Enter task name:
```

After we enter the task name, the timer starts and when it ends, we see a message that says "Break time" and when that is over, we get another saying "Break over."

This is what the script does. Now let's see how it works.

## What is inside

These are the elements of the script.

### Imports

I have used the `datetime` module of the `datetime` library to log the date and time into a log file. I have used the `time` module for the `sleep` function, which is used to emulate a countdown watch.

```python
from datetime import datetime
import time
```

### Methods in the program

`logInfo` and `pomo` are two methods used in this program. Let's see what happens inside these methods.

1. The `logInfo` method:
    
    This method logs the task name and time of starting the task into the `log.txt` file.
    
    ```python
    def logInfo(taskName):
        logFile = open('log.txt', 'a')
        now = datetime.now()
        currentDateAndTime = now.strftime("%B %d, %Y - %H:%M %p")
        log = "Task Name: " + taskName + ", Date and Time: " + currentDateAndTime
        logFile.write(log)
        logFile.write('\n')
    ```
    
    `def logIngo(taskName)` defines the `logInfo` method and conveys that it takes an input `taskName` and logs the information into the `log.txt` file.
    
    `logFile` variable acts as a handle to the `log.txt` file. This is done by the `open` function.
    
    ```python
    # Syntax of open command
    
    variable = open('filename', 'operation')
    ```
    
    Since we want to write the new inputs to the file without deleting the existing data in the file, we use `a` as the operation to append the data to the file. More info on the `open` function [here](https://www.w3schools.com/python/ref_func_open.asp).
    
    After we are done with the file, we access the `now()` class of the `datetime` library with an object `now`. With this, we can get the date and time at any given time in our required format and that is achieved by the following line in the script:
    
    ```python
    currentDateAndTime = now.strftime("%B %d, %Y - %H:%M:%p")
    ```
    
    The `currentDateAndTime` variable stores the date and time in the format:
    
    ```
    October 06, 2021 - 09:14 AM
    ```
    
    We now append this to the `log.txt` file with this command
    
    ```python
    log = "Task Name: " + taskName + ", Date and Time: " + currentDateAndTime
    ```
    
    Which gives the following output
    
    ```
    Task Name: Test Task 1, Date and Time: October 06, 2021 - 09:14 AM
    ```
    
    This is now appended into the `log.txt` file with the `write` command and a new line is added after this so the next log is written in a new line each time.
    
    ```python
    logFile.write(log)
    logFile.write('\n')
    ```
    
2. The `pomo` method
    
    This method emulates the Pomodoro clock. This is the code in this method:
    
    ```python
    def pomo(pomoDuration, breakDuration):
        print('p0m0')
        # work
        while pomoDuration:
            mins = pomoDuration // 60
            secs = pomoDuration % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print (timer, end="\r")
            time.sleep(1)
            pomoDuration -= 1
        print("Break time")
        # break
        while breakDuration:
            mins = breakDuration // 60
            secs = breakDuration % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print (timer, end="\r")
            time.sleep(1)
            breakDuration -= 1
        print("Break over.")
    ```
    
    The first line `def pomo(pomoDuration, breakDuration):` defines the method `pomo` and conveys that it takes two parameters `pomoDuration` and `breakDuration` as inputs. Now, we print a line `p0m0` to indicate that the timer is starting and we enter into a while loop.
    
    ```python
    while pomoDuration:
            mins = pomoDuration // 60
            secs = pomoDuration % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print (timer, end="\r")
            time.sleep(1)
            pomoDuration -= 1
    ```
    
    When the loop starts, we create two new variables `mins` and `secs` defined as follows:
    
    ```python
    mins = pomoDuration // 60
    secs = pomoDuration % 60
    ```
    
    The `//` is the operator for floor division. This rounds the result of the division to the nearest whole number. This is used to get the number of minutes remaining on each iteration.
    
    While the division operator returns the quotient, the modulus or `%` operator is for getting the remainder of a division between two numbers. This is used to get the remaining seconds on the count down timer. In the next line, these two values are formatted to look like "24:49" by this line in the script:
    
    ```python
    timer = '{:02d}:{:02d}'.format(mins, secs)
    ```
    
    This makes the numbers formatted like in a timer. The `:02d` placeholder makes sure that the numbers always have 2 integer places in the digit. The `format` method places our variables `mins` and `secs` in the first and second places. More on the `format` method [here](https://www.w3schools.com/python/ref_string_format.asp). Now, we print our `timer` variable such that it updates itself in the same line instead of printing each second in a new line with the "carriage return" (`\r`):
    
    ```python
    print(timer, end="\r")
    ```
    
    Then we use the `sleep` class to make the program stop for a second and emulate a count down timer. This method is part of the `time` library we imported in the beginning.
    
    ```python
    time.sleep(1)
    ```
    
    After the completion of this loop, we print "Break time" and start the break timer. The break loop is identical to the pomo loop and hence, no explanation is needed. And on completion of this loop, we print "Break Over".
    
    ### Inputs and driver code
    
    Now that we defined our required methods, we use these in the following code. These are the following things we will do to use all the code written:
    
    1. **Input "cycles"**
        
        We take the input for how many cycles the user wants to take for a given task.
        
        ```python
        rounds = int(input("Enter the number of rounds"))
        ```
        
    2. **Print instructions**
        
        We now print the instructions for selecting the duration of each cycle and take that input into `durationChoice`. The default is 25 minutes.
        
        ```python
        print("""Select the duration of the pomo:
                1. 25 minutes, 5 minutes.
                2. 50 minutes, 10 minutes.
                Enter one of the above only.
                If you get naughty, I will choose for you.
            """)
        durationChoice = int(input("Enter duration: "))
        ```
        
    3. **`pomoDuration` and `breakDuration`** 
        
        We create two variables `pomoDuration` and `breakDuration` with an initial value zero(0) and assign them their value depending on the choice made in the previous step
        
        ```python
        pomoDuration = 0
        breakDuration = 0
        if durationChoice == 2:
            pomoDuration = 50*60
            breakDuration = 10*60
        else:
            pomoDuration = 25*60
            breakDuration = 5*60
        ```
        
    4. **Start pomo**
    We start the countdown timer by entering a `for` loop with the number of cycles as `range`. Inside the `for` loop, we take the task name as input and use the methods to start the program.
        
        ```python
        for i in range(rounds):
            # Take info required for log
            taskName = input("Enter task name: ")
            logInfo(taskName)
            pomo(pomoDuration, breakDuration)
        ```
        

## Conclusion

This is how the code works. Hope the explanation is understandable and useful.
