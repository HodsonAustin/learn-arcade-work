# Assets from freesound.org and kenney.nl

import arcade
import rooms

BOX_BUFFER = 30

SPRITE_SCALING = 0.5
SPRITE_SCALING_LASER = .6
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Hitman game"

MOVEMENT_SPEED = 5
BULLET_SPEED = 10
NUMBER_OF_COINS = 10

coin_bing = arcade.load_sound("silver.wav")
reload = arcade.load_sound("reload.mp3")
shot = arcade.load_sound("shot.wav")
dryfire = arcade.load_sound("dryfire.wav")


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sound variables
        self.coin_collect = coin_bing

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.score = 0
        self.ammunition = 8
        self.magazine = 3

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("hitman1_gun.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = rooms.setup_room_1()
        self.rooms.append(room)

        room = rooms.setup_room_2()
        self.rooms.append(room)

        room = rooms.setup_room_3()
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
        self.rooms[self.current_room].bullet_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        ammunition = f"Ammo: {self.ammunition}/{self.magazine}"
        arcade.draw_text(ammunition, SCREEN_WIDTH - 100, 20, arcade.color.WHITE, 14)

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

        if key == arcade.key.W:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.A:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = True
            self.update_player_speed()
        elif key == arcade.key.R:
            if self.magazine >= 1:
                self.ammunition = 8
                self.magazine -= 1
                arcade.play_sound(reload, .2)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.A:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = False
            self.update_player_speed()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked and if there is ammunition.
        """
        if self.ammunition >= 1:

            # Create a bullet
            bullet = arcade.Sprite("bullet.png", SPRITE_SCALING_LASER)

            bullet.angle = self.player_sprite.angle

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top
            if self.player_sprite.angle == 90:
                self.rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_x += 5
                bullet.change_y += BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(shot, .2)

            elif self.player_sprite.angle == 270:
                self.rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_x -= 5
                bullet.center_y -= 20
                bullet.change_y -= BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(shot, .2)

            elif self.player_sprite.angle == 180:
                self.rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_y -= 10
                bullet.change_x -= BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(shot, .2)

            elif self.player_sprite.angle == 0:
                self.rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_y -= 20
                bullet.change_x += BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(shot, .2)
        elif self.ammunition == 0:
            arcade.play_sound(dryfire, .2)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        self.rooms[self.current_room].coin_list.update()
        self.rooms[self.current_room].bullet_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.rooms[self.current_room].coin_list)
        # Loop through each bullet
        for bullet in self.rooms[self.current_room].bullet_list:
            bullet_hit_list = arcade.check_for_collision_with_list(bullet,
                                                                   self.rooms[self.current_room].wall_list)
            for hit_wall in bullet_hit_list:
                bullet.remove_from_sprite_lists()

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
