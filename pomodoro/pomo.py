from datetime import datetime
import time

# Log the taken information
def logInfo(taskName):
    logFile = open('log.txt', 'a')
    now = datetime.now()
    currentDateAndTime = now.strftime("%B %d, %Y - %H:%M %p")
    log = "Task Name: " + taskName + ", Date and Time: " + currentDateAndTime
    logFile.write(log)
    logFile.write('\n')

# Pomodoro function
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

rounds = int(input("Enter the number of rounds: "))
print("""Select the duration of the pomo:
        1. 25 minutes, 5 minutes.
        2. 50 minutes, 10 minutes.
        Enter one of the above only.
        If you get naughty, I will chose for you.
    """)
durationChoice = int(input("Enter duration: "))
# default pomo duration is 25 mins
pomoDuration = 0
breakDuration = 0
if durationChoice == 2:
    pomoDuration = 50*60
    breakDuration = 10*60
else:
    pomoDuration = 25*60
    breakDuration = 5*60
    
for i in range(rounds):
    # Take info required for log
    taskName = input("Enter task name: ")
    logInfo(taskName)
    pomo(pomoDuration, breakDuration)
