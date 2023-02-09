# Importing random to be used later in our functions.
import random


# Defining the main function.
def main():

    # Setting variables to be used later.
    miles_traveled = 0
    distance_natives_traveled = -20
    drinks_in_canteen = 3
    thirst = 0
    camel_tiredness = 0

    # Print the start of the game.
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and escape the area before the natives catch you.")

    # Setting our done variable to false, so it can be used in our while function
    done = False

    # While statement to handle user input and responses.
    while not done:

        # Options to select from as the player.
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit")

        # Setting a variable and requiring user input to set it.
        user_choice = input(" What would you like to do? ")

        # If statements to handle input and responses.

        if user_choice.capitalize() == "A":
            print("You take a drink from your canteen!")
            thirst = 0
            drinks_in_canteen -= 1
            distance_natives_traveled += random.randint(7, 15)

        elif user_choice.capitalize() == "B":
            print("You keep the camel running at a moderate pace.")
            miles_traveled += random.randint(5, 15)
            print("You have traveled", miles_traveled, "miles!")
            thirst += 1
            camel_tiredness += 1
            distance_natives_traveled += random.randint(7, 15)

            # Random chance of Oasis
            if random.randrange(20) == 1:
                print("You have found an Oasis!")
                thirst *= 0
                camel_tiredness = 0
                drinks_in_canteen = 3

        elif user_choice.capitalize() == "C":
            print("Full speed ahead!")
            miles_traveled += random.randint(12, 20)
            print("You have traveled", miles_traveled, "miles!")
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            distance_natives_traveled += random.randint(7, 15)

            # Random chance of Oasis
            if random.randrange(20) == 1:
                print("You have found an Oasis!")
                thirst = 0
                camel_tiredness = 0
                drinks_in_canteen = 3

        elif user_choice.capitalize() == "D":
            print("You have found a spot to rest for the night.")
            print("Your camel is happy!")
            camel_tiredness = 0
            distance_natives_traveled += random.randint(7, 15)

        # elif for if the user would like to quit.
        elif user_choice.capitalize() == "Q":
            done = True

        elif user_choice.capitalize() == "E":
            print("Miles traveled:", miles_traveled)
            print("Drinks in canteen:", drinks_in_canteen)
            print("The natives are", int(miles_traveled - distance_natives_traveled), "miles behind you.")

        # If statements to handle thirst, death, being caught, as well as winning the game.
        if 4 < thirst < 6:
            print("You are thirsty.")
        elif thirst >= 6:
            print("You have died of thirst!")
            done = True
        if 5 < camel_tiredness < 8:
            print("Your camel is getting tired")
        elif camel_tiredness > 8:
            print("Your camel has died from exertion.")
            done = True
        if distance_natives_traveled >= miles_traveled and miles_traveled < 200:
            print("You have been caught by the natives.")
            print("They leave you in the desert to die.")
            done = True
        elif int(miles_traveled - distance_natives_traveled) <= 15 and camel_tiredness < 8:
            print("The natives are getting close")
        elif miles_traveled >= 200 and camel_tiredness < 8 and thirst < 6:
            print("You have escaped with the camel and won the game!")
            print("Congratulations")
            done = True
        elif miles_traveled >= 200 and camel_tiredness >= 8 and thirst >= 6:
            print("You have escaped the area, however you killed the camel in the process.")
            print("You have lost.")
            done = True


main()
