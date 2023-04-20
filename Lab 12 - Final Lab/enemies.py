"""
Enemy Follow Path

This example has enemy sprites follow a set path.

Artwork from https://kenney.nl
"""

import arcade
import math

# --- Constants ---
SPRITE_SCALING = .5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Follow Path"
SPRITE_SPEED = 1.5


class Enemy(arcade.Sprite):
    """
    This class represents the Enemy on our screen.
    """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.health = 50

    def follow_sprite(self, player_sprite):

        # Position the start at the enemy's current location
        start_x = self.center_x
        start_y = self.center_y

        # Get the destination location for the bullet
        dest_x = player_sprite.center_x
        dest_y = player_sprite.center_y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Set the enemy to face the player.
        self.angle = math.degrees(angle)

        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        if self.center_y < player_sprite.center_y:
            self.center_y += min(SPRITE_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(SPRITE_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(SPRITE_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(SPRITE_SPEED, self.center_x - player_sprite.center_x)


class SmartEnemy(Enemy):
    """
    This class represents the Enemy on our screen.
    """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.health = 75

