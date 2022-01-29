def weather(temperature):
    if temperature >= 15 and temperature < 25:
        return "warm"
    elif temperature >= 25:
        return "hot"
    else:
        return "cold"


user_input = int(input("Enter the current temperature: "))
print(weather(user_input))
