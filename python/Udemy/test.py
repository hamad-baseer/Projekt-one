full_message = ''

while True:

    message = input("Say something: ")

    if (message == "\end"):
        print(full_message)
        break
        full_message = full_message + message.capitalize() + " "