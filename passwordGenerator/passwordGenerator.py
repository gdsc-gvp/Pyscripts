import secrets

def generate(length):
    char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    password = ''
    for i in range(length):
        password += secrets.choice(char_list)
    return password

def logger():
    filename = input("Enter the file name: ")
    file = open(filename, 'a')
    file.write(generateOutput)
    file.write('\n')
    print("Done!")
    file.close()

length = int(input("Enter the length of the password you wish to generate: "))
generateOutput = generate(length)
print("Generated password:\n" + generateOutput)
logging = input("Do you wish to log this password into a file?\nEnter 'yes' if you do: ").lower()
if logging == "yes":
    logger()
