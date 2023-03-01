"""Creating a class for my rooms to be used later"""


class Room:
    def __init__(self, description, north, east, south, west):
        self.description = str(description)
        self.north = north
        self.east = east
        self.south = south
        self.west = west


""" Defining my main function to contain rooms and game"""


def main():
    """Creating an array and variable to be used later"""
    room_list = []
    done = False

    """Creating rooms with attributes"""

    room0 = Room("You find yourself in a dimly lit cave. The walls are damp and the air is musty. To the south, you \n"
                 "see a large metal door flanked by torches. To the north, the cave extends deeper into darkness. \n"
                 "The only other option is to explore the damp cave walls to your east and west.", 2, None, None, None)
    room1 = Room("As you enter the room, your eyes adjust to the flickering light of several torches mounted on \n"
                 "the walls. The room is filled with rough cut tables and overturned chairs, suggesting that it was \n"
                 "once a dining area. A pungent odor permeates the air. You notice a door to the north and can \n"
                 "return to the split in the caves by heading east.", 4, 2, None, None)
    room2 = Room("You come to a fork in the cave network. The path to the north is blocked, so you can either \n"
                 "continue east or west deeper into the cave. Alternatively, you can head back south towards \n"
                 "the exit.", None, 3, 0, 1)
    room3 = Room("You enter a small chamber with rough-hewn walls. The flickering torches on the walls barely \n"
                 "illuminate the area, leaving much of it shrouded in shadow. You see two passages leading out \n"
                 "of the room to the north and west.", 5, None, None, 2)
    room4 = Room("The door leads into a small chamber. The air is damp and musty, and the silence is broken only \n"
                 "by the sound of water droplets hitting the ground. A passage to the south leads back out into the \n"
                 "foul smelling room.", None, None, 1, None)
    room5 = Room("As you enter the room, you're met with a cold gust of air. The walls are rough and jagged, and the \n"
                 "torches flicker dimly, casting deep shadows across the room. The only exit is a narrow passage to \n"
                 "the south.", None, None, 3, None)

    """Appending rooms to our list"""

    room_list.append(room0)
    room_list.append(room1)
    room_list.append(room2)
    room_list.append(room3)
    room_list.append(room4)
    room_list.append(room5)

    """Setting starting room"""

    current_room = 0

    """Creating while function to run our game, with if statements to handle player movement between rooms."""

    while not done:

        print("You have entered a long rumored goblin cave. You can leave out the door to the south, or you can \n"
              " adventure deeper. You can quit at any time by typing \"quit\"")

        """With each If/else statement is a check on if the rooms cardinal value is true, then it will set the 
        current_ room to that value. Our starting room_0 description and input below"""

        if current_room == 0:
            print()
            print(room_list[0].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")

            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if room_list[0].north:
                    current_room = room_list[0].north
                else:
                    print("You can not go that way.")

            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if room_list[0].west:
                    current_room = room_list[0].west
                else:
                    print("You can not go that way.")

            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if room_list[0].east:
                    current_room = room_list[0].east
                else:
                    print("You can not go that way.")

            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                print("You have exited the cave.")
                done = True
            elif user_input.casefold() == "quit":
                done = True
            else:
                print("I don't understand your input")

        """room_1 description and player input"""

        if current_room == 1:
            print()
            print(room_list[1].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if room_list[1].north:
                    current_room = room_list[1].north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if room_list[1].west:
                    current_room = room_list[1].west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if room_list[1].south:
                    current_room = room_list[1].south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if room_list[1].east:
                    current_room = room_list[1].east
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "quit":
                done = True
            else:
                print("I don't understand your input")

        """room_2 description and player input below"""

        if current_room == 2:
            print()
            print(room_list[2].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if room_list[2].north:
                    current_room = room_list[2].north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if room_list[2].west:
                    current_room = room_list[2].west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if room_list[2].south:
                    current_room = room_list[2].south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if room_list[2].east:
                    current_room = room_list[2].east
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "quit":
                done = True
            else:
                print("I don't understand your input")

        """room_3 description and player input below"""

        if current_room == 3:
            print()
            print(room_list[3].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if room_list[3].north:
                    current_room = room_list[3].north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if room_list[3].west:
                    current_room = room_list[3].west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if room_list[3].south:
                    current_room = room_list[3].south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if room_list[3].east:
                    current_room = room_list[3].east
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "quit":
                done = True
            else:
                print("I don't understand your input")

        """room_4 description and player input below"""

        if current_room == 4:
            print()
            print(room_list[4].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if room_list[4].north:
                    current_room = room_list[4].north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if room_list[4].west:
                    current_room = room_list[4].west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if room_list[4].south:
                    current_room = room_list[4].south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if room_list[4].east:
                    current_room = room_list[4].east
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "quit":
                done = True
            else:
                print("I don't understand your input")

        """room_5 description and player input below"""

        if current_room == 5:
            print()
            print(room_list[5].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if room_list[5].north:
                    current_room = room_list[5].north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if room_list[5].west:
                    current_room = room_list[5].west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if room_list[5].south:
                    current_room = room_list[5].south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if room_list[5].east:
                    current_room = room_list[5].east
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "quit":
                done = True
            else:
                print("I don't understand your input")


main()
