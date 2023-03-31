"""
Artwork and sounds from https://kenney.nl
"""

import arcade
import random

BOX_BUFFER = 30

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Hitman game"

MOVEMENT_SPEED = 3
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
            wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_237.png",
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
                wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_129.png",
                                     SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create obstacles in the room
    for x in (250, SCREEN_WIDTH - 250):
        # Loop for boxes going across
        for y in range(60, SCREEN_HEIGHT - 60, 90):
            wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_367.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = y
            room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.
    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("/users/yello/dev/sprites/silver.png", 1.0)

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
    room.background = arcade.load_texture("/users/yello/dev/sprites/Tiles/tile_09.png")

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

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - BOX_BUFFER):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, BOX_BUFFER):
            if (x != BOX_BUFFER * 15 and x != BOX_BUFFER * 14) or y != 0:
                wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_237.png", 1.0)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - BOX_BUFFER):
        # Loop for each box going across
        for y in range(BOX_BUFFER, SCREEN_HEIGHT - BOX_BUFFER, BOX_BUFFER):
            # Skip making a block 4 and 5 blocks up
            if (y != BOX_BUFFER * 8 and y != BOX_BUFFER * 9) or x != 0:
                wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_129.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create obstacles in the room
    for x in range(250, SCREEN_WIDTH - 250, 50):
        # Loop for boxes going across
        for y in range(90, SCREEN_HEIGHT - 60, 75):
            if y % 2 == 0:
                wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_367.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                room.wall_list.append(wall)

    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("/users/yello/dev/sprites/silver.png", 1.0)

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

    room.background = arcade.load_texture("/users/yello/dev/sprites/Tiles/tile_96.png")

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

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (BOX_BUFFER, SCREEN_HEIGHT):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, BOX_BUFFER):
            if x != BOX_BUFFER * 15 and x != BOX_BUFFER * 14 or y != SCREEN_HEIGHT or y == BOX_BUFFER:
                wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_129.png", SPRITE_SCALING)
                wall.left = x
                wall.top = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - BOX_BUFFER):
        # Loop for each box going across
        for y in range(BOX_BUFFER, SCREEN_HEIGHT - BOX_BUFFER, BOX_BUFFER):
            wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_237.png", 1.0)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create obstacles in the room
    for x in range(90, SCREEN_WIDTH - 90, 75):
        # Loop for boxes going across
        for y in range(90, SCREEN_HEIGHT - 90, 75):
            if y % 2 == 0 and x % 2 == 0:
                wall = arcade.Sprite("/users/yello/dev/sprites/Tiles/tile_367.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                room.wall_list.append(wall)

    for i in range(NUMBER_OF_COINS):
        coin = arcade.Sprite("/users/yello/dev/sprites/silver.png", 1.0)

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

    room.background = arcade.load_texture("/users/yello/dev/sprites/Tiles/tile_01.png")

    return room


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sound variables
        self.coin_collect = arcade.load_sound("/users/yello/dev/learn-arcade-work/silver.wav")

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.score = 0

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("/users/yello/dev/sprites/Hitman 1/hitman1_gun.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()
        self.rooms[self.current_room].coin_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update_player_speed(self):

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
            self.player_sprite.angle = 90
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
            self.player_sprite.angle = 270
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
            self.player_sprite.angle = 180
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
            self.player_sprite.angle = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        self.rooms[self.current_room].coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.rooms[self.current_room].coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_collect, .1)
            self.score += 25

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_y < 0 and self.current_room == 1:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH/2
            self.player_sprite.center_y = SCREEN_HEIGHT - BOX_BUFFER
        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 2:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH/2
            self.player_sprite.center_y = 0


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
