"""
Missile Follow Path

This example has Missile sprites follow a set path.

Artwork from https://kenney.nl
"""

import arcade
import math

# --- Constants ---
SPRITE_SCALING = .5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Follow Path"
SPRITE_SPEED = 5


class Missile(arcade.Sprite):
    """
    This class represents the Missile on our screen.
    """
    def follow_sprite(self, enemy):

        # Position the start at the Missile's current location
        start_x = self.center_x
        start_y = self.center_y

        # Get the destination location for the bullet
        dest_x = enemy.center_x
        dest_y = enemy.center_y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Set the Missile to face the player.
        self.angle = math.degrees(angle) - 90

        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        if self.center_y < enemy.center_y:
            self.center_y += min(SPRITE_SPEED, enemy.center_y - self.center_y)
        elif self.center_y > enemy.center_y:
            self.center_y -= min(SPRITE_SPEED, self.center_y - enemy.center_y)

        if self.center_x < enemy.center_x:
            self.center_x += min(SPRITE_SPEED, enemy.center_x - self.center_x)
        elif self.center_x > enemy.center_x:
            self.center_x -= min(SPRITE_SPEED, self.center_x - enemy.center_x)
