""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 3.0
SPRITE_SCALING_COIN = 2.5
SPRITE_SCALING_RAT = 2.5

COIN_COUNT = 50
RAT_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

silver_sound = arcade.load_sound("/users/yello/dev/silver.wav")
rat_sound = arcade.load_sound("/users/yello/dev/rat.ogg")


class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1
        self.angle += 1

        # If we rotate past 360, reset it back a turn.
        if self.angle > 359:
            self.angle -= 360

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class Rat(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the rat to a random spot at the edge of the screen
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.center_x = random.randrange(SCREEN_WIDTH+20, SCREEN_WIDTH + 100)

    def update(self):

        # Move the rat
        self.center_x -= 1

        # See if the rat has gone off the left of the screen.
        # If so, reset it.
        if self.left < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.rat_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rat_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("/users/yello/dev/sprites/knight.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("/users/yello/dev/sprites/silver.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(RAT_COUNT):

            # Create the rat instance
            # Coin image from kenney.nl
            rat = Rat("/users/yello/dev/sprites/rat.png", SPRITE_SCALING_RAT)

            # Position the rat
            rat.center_x = random.randrange(SCREEN_WIDTH)
            rat.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the rat to the lists
            self.rat_list.append(rat)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.rat_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.ORANGE_RED, 14)

        if len(self.coin_list) == 0:
            # Put the text on the screen.
            arcade.draw_text("GAME OVER", 325, 350, arcade.color.BLACK, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

        if len(self.coin_list) == 0:
            self.player_sprite.center_x = 400
            self.player_sprite.center_y = 300

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.coin_list.update()
        self.rat_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        rats_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rat_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 10
            arcade.play_sound(silver_sound, .05)

        for rat in rats_hit_list:
            rat.remove_from_sprite_lists()
            self.score -= 25
            arcade.play_sound(rat_sound, .5)

        if len(self.coin_list) == 0:
            Coin.center_y = 0
            Rat.center_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
