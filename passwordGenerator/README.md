# `passwordGenerator.py` - code explained

This is a brief explanation of the `passwordGenerator.py` program.

## What this program accomplishes

This program generates alpha-numeric passwords with symbols and stores them in a file of your choice if you want it to.

## How the script works

When you run the script, the following will be the output:

```
Enter the length of the password you wish to generate:
```

Assume you want a password of length 8 characters. So you enter 8 in the above prompt and you get the following output:

```
Generated password:
aCh}C/5N
```

Then you are asked if you want to store the password in a file.

```
Do you wish to log this password into a file?
Enter 'yes' if you do:
```

If we enter 'yes' here, we get the following output:

```
Enter the file name:
```

We are asked to enter the name of the file we want to store it in. If the file doesn't already exist, it is created upon entering. Suppose we enter a file name `log.txt`, we see an output that indicates the password is stored in the file of our choice.

```
Done!
```

This is what the script does. Now let's see how it works.

## What's inside

These are the elements of the script

### Imports

I have used the `choice` class of the `secrets` library to make the program return one random character from the list of characters.

```python
import secrets
```

You can find the difference between `random` and `secrets` [here](https://www.youtube.com/watch?v=xzlfXSBzhx8).

### Methods

This program has two methods, `generate` and `logger`. Let's see what these do.

1. **The `generate` method**
This method generates the password. We can decide the length of the password.

```python
def generate(length):
    char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    password = ''
```

`def generate(length)` defines the `generate` method and conveys that it takes an input `length` and generates a password. The `char_list` is the list of characters the password will be made of. I obtained this list using the `printable` class of the `string` library and omitted the characters that are not suitable for the task. Those are  `[\t, \n, \r, \x0b, \x0c]`. Then, I initialized an empty string `password` where I store the password.

```python
for i in range(length):
        password += secrets.choice(char_list)
    return password
```

After that, I created a `for` loop to generate the password. On each iteration of the loop, one random character from the `char_list` is appended to the `password` string using the `choice` class of the `secrets` library. And finally, the generated string is returned.

1. The `logger` method
This method writes the generated password to a file of your choosing.

```python
def logger():
    filename = input("Enter the file name: ")
```

The line `def logger():` defines the `logger` method. Next, we create a variable `filename` and take a string input from the user. Then, we create a handle for the file under this name with the line

```python
file = open(filename, 'a')
```

This opens a file with that name or creates a new file under the given name if if doesn't exists already and enables the `a` operation which is `append`. Now, we write the generated password with to the chosen file and add an empty line with these commands.
Here, the variable `generateOutput` is a global variable and hence doesn't throw an error inspite of not being in the method.

```python
file.write(generateOutput)
file.write('\n')
```

Now, we print an indication that the writing is done and close the opened `file` handle.

```python
print("Done!")
file.close()
```

### Inputs and driver Code

Now that we defined the required methods, we use these in the following code. These are the following things we will do to use all the code written:

```python
length = int(input("Enter the length of the password you wish to generate: "))
```

This takes the length of the password we want to generate as input. Now, we use the `generate` method and store the output in the `generateOutput` variable and print it.

```python
generateOutput = generate(length)
print("Generated password:\n" + generateOutput)
```

Now, we ask the user if they want to store the password in a file.

```python
logging = input("Do you wish to log this password into a file?\nEnter 'yes' if you do: ").lower()
```

We use `lower()` function to avoid unnessasary complexities in comparision.

Then, we use a simple `if` condition to call our `logger` function.

```python
if logging == "yes":
    logger()
```

## Conclusion

This is how the code works. Hope the explanation is understandable and useful.
