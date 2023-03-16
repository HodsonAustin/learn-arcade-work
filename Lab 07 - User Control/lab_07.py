import arcade
import
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

class Boundary(arcade.Sound):
    def __init__(self, file_name):
        super().__init__(file_name)

class Bubble:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """

        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_circle_outline(self.position_x, self.position_y, self.radius, arcade.csscolor.BLACK, 3)
        arcade.draw_circle_outline(self.position_x + 7, self.position_y + 10, self.radius - 20, arcade.csscolor.BLACK, 2)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class Cloud:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the clouds with the instance variables we have. """

        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x - 50, self.position_y + 50, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x + 50, self.position_y + 50, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x - 50, self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x + 50, self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x, self.position_y + 75, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Create our ball
        self.bubble = Bubble(50, 50, 0, 0, 25, arcade.color.WHITE)

        # Create our cloud
        self.cloud = Cloud(100, 50, 0, 0, 40, arcade.color.WHITE)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        # Draw a sunset and sun
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 350, 300, arcade.csscolor.FUCHSIA)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 300, 250, arcade.csscolor.ORANGE_RED)
        arcade.draw_circle_filled(150, 250, 40, arcade.color.ARYLIDE_YELLOW)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 250, 0, arcade.csscolor.BLUE)
        # Draw bubble
        self.bubble.draw()

        # Draw cloud
        self.cloud.draw()



    def update(self, delta_time):
        self.bubble.update()
        self.cloud.update()

    # def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
    #     if button == arcade.MOUSE_BUTTON_LEFT:


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.bubble.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.bubble.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.bubble.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.bubble.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bubble.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.bubble.change_y = 0


    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.cloud.position_x = x
        self.cloud.position_y = y


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()