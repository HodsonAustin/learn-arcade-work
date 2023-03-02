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

    room0 = Room("You are in a cozy bedroom, where a neatly made bed is the centerpiece. A small desk and chair sit "
                 "in the corner, and a lamp casts a warm glow on the room. To the east is a door that leads to "
                 "the South Hall.", None, 1, None, None)
    room1 = Room("You find yourself in a long hallway, lined with paintings and family photographs. To the west is "
                 "Bedroom 2, while to the north, the hall leads to the North Hall. To the east, you see the entrance "
                 "to the elegant dining room, and to the south, a door leads outside.", 4, 2, None, 0)
    room2 = Room("You step into a grand dining room, with a large table surrounded by chairs. The walls are adorned "
                 "with ornate patterns, and a chandelier hangs from the ceiling. To the west is the entrance to "
                 "the South Hall, and to the north, you see the entrance to the kitchen.", 5, None, None, 1)
    room3 = Room("You enter a spacious bedroom, with a four-poster bed dominating the room. The walls are painted a "
                 "calming blue, and a large wardrobe sits in the corner. To the east is the entrance to the "
                 "North Hall.", None, 4, None, None)
    room4 = Room("You find yourself in a spacious hallway, with intricate designs etched into the walls. To the west "
                 "is Bedroom 1, while to the north, a door leads to the Balcony, and to the east, the hall leads "
                 "to the Kitchen.", 6, 5, 1, 3)
    room5 = Room("You step into a well-lit kitchen, with pots and pans hanging from the walls. A large stove sits in "
                 "the corner, and a table is set up for preparing meals. To the west is the entrance to the "
                 "North Hall, and to the south, you see the entrance to the Dining Room.", None, None, 2, 4)
    room6 = Room("You step onto a balcony, with a breathtaking view of the surrounding countryside. The air is crisp "
                 "and fresh, and a gentle breeze rustles your hair. To the south is the entrance to the "
                 "North Hall.", None, None, 4, None)

    """Appending rooms to our list"""

    room_list.append(room0)
    room_list.append(room1)
    room_list.append(room2)
    room_list.append(room3)
    room_list.append(room4)
    room_list.append(room5)
    room_list.append(room6)

    """Setting starting room"""

    current_room = 0

    """Creating while function to run our game, with if statements to handle player movement between rooms."""

    while not done:

        """With each If/else statement is a check on if the rooms cardinal value is true, then it will set the 
        current_ room to that value. Our starting room_0 description and input below"""

        if current_room == 0:
            print()
            print(room_list[0].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas "
                               "or type quit to exit.")

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

        """room_6 description and player input below"""

        if current_room == 6:
            print()
            print(room_list[6].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if room_list[6].north:
                    current_room = room_list[6].north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if room_list[5].west:
                    current_room = room_list[6].west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if room_list[5].south:
                    current_room = room_list[6].south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if room_list[5].east:
                    current_room = room_list[6].east
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "quit":
                done = True
            else:
                print("I don't understand your input")


if __name__ == "__main__":
    main()
