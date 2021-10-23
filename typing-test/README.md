# `typingTest.py` - code explained

This is a brief explanation of the `typingTest.py` program.

## What this program accomplishes

This program outputs a paragraph of 20 sentences for the user to type into the CLI and then measures the typing speed of the user based on how accurately they typed the given paragraph.

## How the script works

When you run the script, the following will be the output:

```
Typing Test.
You have 60 seconds to type the text given.
Type "start" below to start your test.

Enter your response here: 
```

After we type "start" in the terminal, we get a paragraph we need to type. After 60 seconds, we see the following:

```
Time up.
Press enter to get your results.
```

After we press enter, we get our results as follows.

```
Your typing speed is: 35 WPM
```

This is what the script does. Now let's see how it works.

## What's inside

These are the elements of the script.

### Imports

I have used the following libraries in this script.

```python
import requests
from threading import Timer
```

The `requests` library is imported to use the `get` class of the library, which fetches the paragraph from a website called [metaphorpsum.com](http://metaphorpsum.com). The `Timer` class of the `threading` library is imported to help us terminate the input after 60 secs.

### Methods

1. **The `getParagraph` method**
This method, as the name suggests, gets the paragraph from the internet.

```python
def getParagraph():
    paraSource = "http://metaphorpsum.com/sentences/20"
    response = requests.get(paraSource)
    return response.text
```

We define the method with `def getParagraph()`. Then we initialize a variable with the URL we need to get using the `get` class of the `requests` library. Now, we initialize another variable `response` and get the paragraph we require and return it as plain text in the last line.

1. The `typingTest` method
This method conducts the actual typing test. We first define the method with the following statement:

```python
def typingTest(confirmation):
```

This indicates that the method takes an argument named `confirmation`. This variable is where we store the input of the user when we ask if they want to start the typing test. If their input reads "start", we enter the typing test.

```python
if confirmation == 'start':
        para = getParagraph()
        print(para)
```

Now, we call our `getParagraph()` method and store the output into the `para` variable.

```python
				timeout = 59
```

Now, we initialize a variable `timeout` to store the duration of the test as an integer. This is to use in the `Timer` class.

```python
				timeCheck = Timer(timeout, print, ['\nTime up.\nPress enter to get your results.'])
```

Now, we initialize `timeCheck` as an object to the `Timer` class give the duration and termination message as arguments. After this, we can get into the process.

```python
				timeCheck.start()
        test = list(map(str, input("Type the above in under 60 secs.\n\n").strip().split()))
        timeCheck.cancel()
```

The first line of the above code snippet (`timeCheck.start()`) suggests that the line immediately after it is the process that is to be monitored. The line that is to be monitored takes the paragraph as input from the user and splits it into a list word-by-word, ignoring spaces. The last line in the above snippet indicates that the process being monitored will be terminated after the completion of the given time. Then a new line is printed just to make the output a bit readable.

```python
				print("\n")
```

Now, we create a variable `paraAsList` to convert the fetched paragraph into a word list for comparison.

```python
				paraAsList = para.split()
        count = 0
        for word in test:
            if word in test and word in paraAsList:
                count += 1
```

Then, we initialize a variable `count` to monitor the number of words that are correctly input into the `test` list. Then, in the `for` loop that iterates through the `test` list, we check if a word is in both `test` and `paraAsList` lists, we increment the `count` variable by 1. This gets us the number of words correctly typed into the CLI by the user. Now, the final output is printed as

```python
				print("Your typing speed is:", count, "WPM.")
```

If the `confirmation` is not "start", the program will return "Error" and terminate itself.

```python
			else:
				print("Error")
```

### Inputs and driver code

Now that we defined all the methods we need, let us go ahead and use it in our program.

First, we print the basic instructions of the test:

```python
print("""
Typing Test.
You have 60 seconds to type the text given.
Type "start" below to start your test.
""")
```

Now, we initialize the `confirmation` variable we discussed before and take input.

```python
confirmation = input("Enter your response here: ").lower()
```

The `lower()` function is used to avoid confusion while comparing strings.

Now, we finally call our methods.

```python
typingTest(confirmation)
```

## Conclusion

This is how this script works. Hope the explanation is understandable and useful.
