import arcade
import random

BOX_BUFFER = 30

SPRITE_SCALING = 0.5
SPRITE_SCALING_LASER = .6
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "lab_09"

MOVEMENT_SPEED = 5
NUMBER_OF_COINS = 10


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.coin_list = None

        # This holds the background images. If you don't want to be changing
        # background images, you can delete this part.
        self.background = None


def setup_room_1():
    """
    Create and return room 1.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - BOX_BUFFER):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, BOX_BUFFER):
            wall = arcade.Sprite("tile_237.png",
                                 1.0)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - BOX_BUFFER):
        # Loop for each box going across
        for y in range(BOX_BUFFER, SCREEN_HEIGHT - BOX_BUFFER, BOX_BUFFER):
            # Skip making a block 8 and 9 blocks up on the right side
            if (y != BOX_BUFFER * 9 and y != BOX_BUFFER * 8) or x == 0:
                wall = arcade.Sprite("tile_129.png",
                                     SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create obstacles in the room
    for x in (250, SCREEN_WIDTH - 250):
        # Loop for boxes going across
        for y in range(60, SCREEN_HEIGHT - 60, 90):
            wall = arcade.Sprite("tile_367.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = y
            room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.
    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("silver.png", 1.0)

        # Boolean variable if we successfully placed the coin
        coin_placed_successfully = False

        # Keep trying until success
        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)

            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True

        # Add the coin to the lists
        room.coin_list.append(coin)

    # Load the background image for this level.
    room.background = arcade.load_texture("tile_09.png")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - BOX_BUFFER):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, BOX_BUFFER):
            if (x != BOX_BUFFER * 15 and x != BOX_BUFFER * 14) or y != 0:
                wall = arcade.Sprite("tile_237.png", 1.0)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - BOX_BUFFER):
        # Loop for each box going across
        for y in range(BOX_BUFFER, SCREEN_HEIGHT - BOX_BUFFER, BOX_BUFFER):
            # Skip making a block 4 and 5 blocks up
            if (y != BOX_BUFFER * 8 and y != BOX_BUFFER * 9) or x != 0:
                wall = arcade.Sprite("tile_129.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create obstacles in the room
    for x in range(250, SCREEN_WIDTH - 250, 50):
        # Loop for boxes going across
        for y in range(90, SCREEN_HEIGHT - 60, 75):
            if y % 2 == 0:
                wall = arcade.Sprite("tile_367.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                room.wall_list.append(wall)

    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("silver.png", 1.0)

        # Boolean variable if we successfully placed the coin
        coin_placed_successfully = False

        # Keep trying until success
        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)

            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True

    room.background = arcade.load_texture("tile_96.png")

    return room


def setup_room_3():
    """
    Create and return room 3.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (BOX_BUFFER, SCREEN_HEIGHT):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, BOX_BUFFER):
            if x != BOX_BUFFER * 15 and x != BOX_BUFFER * 14 or y != SCREEN_HEIGHT or y == BOX_BUFFER:
                wall = arcade.Sprite("tile_129.png", SPRITE_SCALING)
                wall.left = x
                wall.top = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - BOX_BUFFER):
        # Loop for each box going across
        for y in range(BOX_BUFFER, SCREEN_HEIGHT - BOX_BUFFER, BOX_BUFFER):
            wall = arcade.Sprite("tile_237.png", 1.0)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create obstacles in the room
    for x in range(90, SCREEN_WIDTH - 90, 75):
        # Loop for boxes going across
        for y in range(90, SCREEN_HEIGHT - 90, 75):
            if y % 2 == 0 and x % 2 == 0:
                wall = arcade.Sprite("tile_367.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                room.wall_list.append(wall)

    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("silver.png", 1.0)

        # Boolean variable if we successfully placed the coin
        coin_placed_successfully = False

        # Keep trying until success
        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)

            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True

    room.background = arcade.load_texture("tile_01.png")

    return room
