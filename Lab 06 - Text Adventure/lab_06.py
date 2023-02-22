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

    room0 = Room("You are in a cave. To your South is a large metal door with torches on either side of it.\n To your North leads deeper into the cave. To your East and West are damp cave walls.", 2, None, None, None)
    room1 = Room("You have entered a well lit part of the cave filled with rough cut tables and turned over chairs. \nIt appears this must be a dining area. There is a foul smell emanating from the room.\n There is a door to the north or you go back to the split in the caves to the East.", 5, 2, None, None)
    room2 = Room("You are at a split in the cave network and are unable to continue north. You may go East or West deeper into the cave \n or you can go south back towards the exit.", None, 3, 0, 1)
    room3 = Room("You are in a room. There is a passage to the North and West.", 5, None, None, 2)
    room4 = Room("You are in a room. There is a passage to the South.", None, None, 1, None)
    room5 = Room("You are in a room. There is a passage to the South.", None, None, 3, None)

    """Appending rooms to our list"""

    room_list.append(room0)
    room_list.append(room1)
    room_list.append(room2)
    room_list.append(room3)
    room_list.append(room4)
    room_list.append(room5)

    """Setting starting room"""

    current_room = room_list[0]

    """Creating while function to run our game, with if statements to handle player movement between rooms."""

    while not done:
        if current_room == room_list[0]:
            print()
            print(room_list[0].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            # if user_input.casefold() == "go n" or user_input.casefold() == "go north":
            #     next_room = room_list[0].north
            #     current_room = next_room
            # if user_input.casefold() == "go w" or user_input.casefold() == str("go west"):
            #     print("You can not go that way.")
            # if user_input.casefold() == "go s" or user_input.casefold() == str("go south"):
            #     print("You have exited the cave")
            #     done = True
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if current_room.north:
                    current_room = current_room.north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if current_room.west:
                    current_room = current_room.west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if current_room.east:
                    current_room = current_room.east
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                print("You have exited the cave.")
                done = True
            else:
                print("I don't understand your input")

        if current_room == 1:
            print()
            print(room_list[1].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if current_room.north:
                    current_room = current_room.north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if current_room.west:
                    current_room = current_room.west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if current_room.south:
                    current_room = current_room.south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if current_room.east:
                    current_room = current_room.east
                else:
                    print("You can not go that way.")
            else:
                print("I don't understand your input")

        if current_room == 2:
            print()
            print(room_list[2].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if current_room.north:
                    current_room = current_room.north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if current_room.west:
                    current_room = current_room.west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if current_room.south:
                    current_room = current_room.south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if current_room.east:
                    current_room = current_room.east
                else:
                    print("You can not go that way.")
            else:
                print("I don't understand your input")
        if current_room == 3:
            print()
            print(room_list[3].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if current_room.north:
                    current_room = current_room.north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if current_room.west:
                    current_room = current_room.west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if current_room.south:
                    current_room = current_room.south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if current_room.east:
                    current_room = current_room.east
                else:
                    print("You can not go that way.")
            else:
                print("I don't understand your input")

        if current_room == 4:
            print()
            print(room_list[4].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if current_room.north:
                    current_room = current_room.north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if current_room.west:
                    current_room = current_room.west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if current_room.south:
                    current_room = current_room.south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if current_room.east:
                    current_room = current_room.east
                else:
                    print("You can not go that way.")
            else:
                print("I don't understand your input")

        if current_room == 5:
            print()
            print(room_list[5].description)
            user_input = input("What would you like to do? You may say \"go\" with a direction to change areas.")
            if user_input.casefold() == "go n" or user_input.casefold() == "go north":
                if current_room.north:
                    current_room = current_room.north
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go w" or user_input.casefold() == "go west":
                if current_room.west:
                    current_room = current_room.west
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go s" or user_input.casefold() == "go south":
                if current_room.south:
                    current_room = current_room.south
                else:
                    print("You can not go that way.")
            elif user_input.casefold() == "go e" or user_input.casefold() == "go east":
                if current_room.east:
                    current_room = current_room.east
                else:
                    print("You can not go that way.")
            else:
                print("I don't understand your input")


main()
