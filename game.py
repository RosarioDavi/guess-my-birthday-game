from random import randint

player_name = input("Hi what is your name?")
guess_number = 1
month_number = randint(1,12)
year_number = randint(1942,2004)

for guess_number in range(1,6):
    month_number
    year_number
    print("Guess:", player_name, "were you born in", month_number, "/", year_number, "?")

    respone = input("yes or no? ")

    if respone == "yes":
        print("I knew it!")
    else:
        print("Drat! Lemme try again!")