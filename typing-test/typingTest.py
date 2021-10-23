import requests
from threading import Timer

def getParagraph():
    paraSource = "http://metaphorpsum.com/sentences/20"
    response = requests.get(paraSource)
    return response.text

def typingTest(confirmation):
    if confirmation == 'start':
        para = getParagraph()
        print(para)
        timeout = 59
        timeCheck = Timer(timeout, print, ['\nTime up.\nPress enter to get your results.'])
        timeCheck.start()
        test = list(map(str, input("Type the above in under 60 secs.\n\n").strip().split()))
        timeCheck.cancel()
        print("\n")
        paraAsList = para.split()
        count = 0
        for word in test:
            if word in test and word in paraAsList:
                count += 1
        print("Your typing speed is:", count, "WPM.")
    else:
        print("Error.")


print("""
Typing Test.
You have 60 seconds to type the text given.
Type "start" below to start your test.
""")

confirmation = input("Enter your response here: ").lower()
typingTest(confirmation)
