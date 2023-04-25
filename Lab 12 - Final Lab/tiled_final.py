# Assets from freesound.org, opengameart.org and kenney.nl

import arcade
import tiled_rooms
import explosions
import missiles
import math
import random

# Variables to be used later

BOX_BUFFER = 30

SPRITE_SCALING = .5
SPRITE_SCALING_LASER = .6
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 16
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "The Persistent"

MOVEMENT_SPEED = 4
BULLET_SPEED = 10
NUMBER_OF_COINS = 10

explosion_texture_count = 60


# Main function
class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)
        self.physics_engine_enemies = []

        # Sprite lists
        self.current_room = 2
        self.last_room = 0
        self.explosions_list = []

        # Set up the player
        self.tiled_rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.physics_engine_enemy = None
        self.score = 0
        self.ammunition = 8
        self.magazine = 3
        self.health = 100
        self.special = 1
        self.lives = 3

        # Track coins collected
        self.coins_collected = 0

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Preload the animation frames. We don't do this in the __init__
        # of the explosion sprite because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []

        # Initialize variables
        self.last_sound_time = 0
        self.play_sound = False

        # Create a variable for the start menu, death screen, and completion screen.
        self.INFO_START = True
        self.GAME_START = False
        self.GAME_WIN = False

        # Create a few variables for our explosions.
        columns = 9
        count = 150
        sprite_width = 111
        sprite_height = 111

        # Load the explosions from a sprite sheet
        self.explosion_texture_list = arcade.load_spritesheet("explosionBig.png", sprite_width,
                                                              sprite_height, columns, count)

        # Load sounds. Sounds from freesound.org
        self.coin_bing = arcade.load_sound("silver.wav")
        self.reload = arcade.load_sound("reload.mp3")
        self.shot = arcade.load_sound("shot.wav")
        self.dryfire = arcade.load_sound("dryfire.wav")
        self.collecting_ammo = arcade.load_sound("collecting_ammo.wav")
        self.rocket_shot = arcade.load_sound("rocket_shot.wav")
        self.missile_explosion = arcade.load_sound("missile_explode.ogg")
        self.zombie_bite = arcade.load_sound("zombie_bite.wav")
        self.zombie_spit = arcade.load_sound("spit.wav")
        self.impact = arcade.load_sound("impact.wav")

    # Set up our rooms and player
    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("hitman1_gun.png", SPRITE_SCALING * 1.2)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.tiled_rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = tiled_rooms.setup_room_1()
        self.tiled_rooms.append(room)

        room = tiled_rooms.setup_room_2()
        self.tiled_rooms.append(room)

        room = tiled_rooms.setup_room_3()
        self.tiled_rooms.append(room)

        room = tiled_rooms.setup_room_4()
        self.tiled_rooms.append(room)

        room = tiled_rooms.setup_room_5()
        self.tiled_rooms.append(room)

        room = tiled_rooms.setup_room_6()
        self.tiled_rooms.append(room)

        room = tiled_rooms.setup_room_7()
        self.tiled_rooms.append(room)

        # Our starting room number
        self.current_room = 0

        self.last_room = -1

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.tiled_rooms[self.current_room].wall_list)
        # Create a list of physics engines for the enemies in this room
        for i in self.tiled_rooms[self.current_room].enemy_list:
            physics_engine_enemy = arcade.PhysicsEngineSimple(i, self.tiled_rooms[self.current_room].wall_list)
            self.physics_engine_enemies.append(physics_engine_enemy)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Start screen
        if self.INFO_START and not self.GAME_START and self.health >= 0:
            # Draw the title/start screen
            arcade.draw_text("The Persistent",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 250, arcade.color.WHITE,
                             font_size=50, anchor_x="center")
            arcade.draw_text("You have been hired to exterminate some target zombies.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 150, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("Something seems strange about these zombies.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 100, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("They spit a black ichor that dissolves what it touches.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 50, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("WASD to move. Pick up coins to increase your score",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("Click to shoot. Look for ammo boxes for more ammo and rockets",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 - 50, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("Press spacebar to shoot rockets and R to reload.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 - 100, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("Press spacebar to continue",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 - 300, arcade.color.WHITE,
                             font_size=20, anchor_x="center")

        # Info screen
        if not self.INFO_START and not self.GAME_START and self.health >= 0 and self.lives == 3:
            # Draw the title/start screen
            arcade.draw_text("Keep track of your lives",
                             150,
                             SCREEN_HEIGHT - 150, arcade.color.WHITE,
                             font_size=14, anchor_x="center")
            arcade.draw_text("Press spacebar to start",
                             SCREEN_WIDTH / 2,
                             25, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("You will win when you defeat all special enemies.",
                             275,
                             150, arcade.color.GOLD,
                             font_size=14, anchor_x="center")
            arcade.draw_text("They can be identified by their unique color.",
                             275,
                             130, arcade.color.GOLD,
                             font_size=14, anchor_x="center")
            arcade.draw_text("You can track the remaining enemies below.",
                             275,
                             110, arcade.color.GOLD,
                             font_size=14, anchor_x="center")
            arcade.draw_text("Ammo and rockets below",
                             SCREEN_WIDTH - 125,
                             150, arcade.color.GOLD,
                             font_size=14, anchor_x="center")
            arcade.draw_text("Watch out for black spit on",
                             SCREEN_WIDTH - 125,
                             130, arcade.color.GOLD,
                             font_size=14, anchor_x="center")
            arcade.draw_text("the ground as it hurts",
                             SCREEN_WIDTH - 125,
                             110, arcade.color.GOLD,
                             font_size=14, anchor_x="center")
            # Draw the HUD
            output = f"Score: {round(self.score)}"
            arcade.draw_text(output, 40, 70, arcade.color.WHITE, 14)
            ammunition = f"Ammo: {self.ammunition}/{self.magazine}"
            arcade.draw_text(ammunition, SCREEN_WIDTH - 125, 90, arcade.color.WHITE, 14)
            ammunition = f"Rockets: {self.special}"
            arcade.draw_text(ammunition, SCREEN_WIDTH - 125, 70, arcade.color.WHITE, 14)
            lives = f"Lives remaining: {self.lives}"
            arcade.draw_text(lives, 40, SCREEN_HEIGHT - 125, arcade.color.RED, 20)
            remaining_enemies = f"Enemies remaining: {len(self.tiled_rooms[self.current_room].smart_enemy_list)}"
            arcade.draw_text(remaining_enemies, 40, 90, arcade.color.WHITE, 14)

        # Draw when the game starts
        elif not self.INFO_START and self.GAME_START:
            # Draw the game
            self.tiled_rooms[self.current_room].scene.draw()
            self.tiled_rooms[self.current_room].coin_list.draw()
            self.tiled_rooms[self.current_room].bullet_list.draw()
            self.tiled_rooms[self.current_room].enemy_bullet_list.draw()
            self.tiled_rooms[self.current_room].ammo_box_list.draw()
            self.tiled_rooms[self.current_room].explosions_list.draw()
            self.tiled_rooms[self.current_room].missile_list.draw()
            self.player_list.draw()
            if self.tiled_rooms[self.current_room].enemy_list is not None:
                self.tiled_rooms[self.current_room].enemy_list.draw()

            # Draw the HUD
            output = f"Score: {round(self.score)}"
            arcade.draw_text(output, 40, 70, arcade.color.BLACK, 14)
            ammunition = f"Ammo: {self.ammunition}/{self.magazine}"
            arcade.draw_text(ammunition, SCREEN_WIDTH - 125, 90, arcade.color.BLACK, 14)
            ammunition = f"Rockets: {self.special}"
            arcade.draw_text(ammunition, SCREEN_WIDTH - 125, 70, arcade.color.BLACK, 14)
            health = f"Health: {round(self.health)}/100"
            arcade.draw_text(health, 40, SCREEN_HEIGHT - 100, arcade.color.RED, 20)
            lives = f"Lives remaining: {self.lives}"
            arcade.draw_text(lives, 40, SCREEN_HEIGHT - 125, arcade.color.RED, 20)
            if self.tiled_rooms[self.current_room].enemy_list is not None:
                remaining_enemies = f"Enemies remaining: {len(self.tiled_rooms[self.current_room].smart_enemy_list)}"
                arcade.draw_text(remaining_enemies, 40, 90, arcade.color.BLACK, 14)
            remaining_coins = f"Coins: {self.coins_collected}"
            arcade.draw_text(remaining_coins, SCREEN_WIDTH - 300, SCREEN_HEIGHT - 100, arcade.color.GOLD, 20)

        # Death Screen
        if not self.GAME_START and self.health <= 0 <= self.lives:
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                         SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.BLACK)

            arcade.draw_text("You have died",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 250, arcade.color.WHITE,
                             font_size=50, anchor_x="center")
            arcade.draw_text("Keep a look out for ammo boxes",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 150, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("Use rockets to your advantage, as they can take out large groups of enemies.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 100, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("You get one additional rocket everytime you pick up ammo.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 50, arcade.color.WHITE,
                             font_size=20, anchor_x="center")
            arcade.draw_text("Press spacebar to restart at the cost of one life",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 - 300, arcade.color.WHITE,
                             font_size=20, anchor_x="center")

        # Handle when out of lives.
        if self.GAME_START and self.health <= 0 >= self.lives:
            # Draw the death screen
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                         SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.BLACK)

            arcade.draw_text("You have lost the game.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 250, arcade.color.WHITE,
                             font_size=50, anchor_x="center")
        # Game won screen
        if self.GAME_START and self.health >= 0 <= self.lives and self.GAME_WIN:
            # Draw the death screen
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                         SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.BLACK)

            arcade.draw_text("You have won the game.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2 + 100, arcade.color.WHITE,
                             font_size=50, anchor_x="center")
            arcade.draw_text("Congrats!.",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2, arcade.color.WHITE,
                             font_size=50, anchor_x="center")
            output = f"Score: {round(self.score)}"
            arcade.draw_text(output, 40, 70, arcade.color.WHITE, 14)

    # Player movement and angle
    def update_player_speed(self):
        # No movement if start menu showing
        if not self.GAME_START:
            # Calculate speed based on the keys pressed
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

        if self.GAME_START:
            # Stop moving when a key is released
            if not self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = 0
            if not self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = 0

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

    # Move on key press
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key in [arcade.key.W, arcade.key.S, arcade.key.A, arcade.key.D] and self.GAME_START:
            if key == arcade.key.W:
                self.up_pressed = True
            elif key == arcade.key.S:
                self.down_pressed = True
            elif key == arcade.key.A:
                self.left_pressed = True
            elif key == arcade.key.D:
                self.right_pressed = True
            self.update_player_speed()
        elif key == arcade.key.R and self.GAME_START:
            if self.magazine >= 1 and self.ammunition <= 7:
                self.ammunition = 8
                self.magazine -= 1
                arcade.play_sound(self.reload, .2)
        elif key == arcade.key.SPACE and self.INFO_START and not self.GAME_START and self.health >= 0:
            self.INFO_START = False
        elif key == arcade.key.SPACE and not self.INFO_START and not self.GAME_START and self.health >= 0:
            self.GAME_START = True
        elif key == arcade.key.SPACE and not self.INFO_START and not self.GAME_START and self.health <= 0:
            self.health = 125
            self.lives -= 1
        elif key == arcade.key.SPACE and not self.INFO_START and self.GAME_START:
            if self.special >= 1:
                # Create a missile
                missile = missiles.Missile("missile.png", SPRITE_SCALING_LASER)
                missile.angle = self.player_sprite.angle
                # Position the missile
                missile.center_x = self.player_sprite.center_x
                missile.bottom = self.player_sprite.top
                self.special -= 1
                self.tiled_rooms[self.current_room].missile_list.append(missile)
                arcade.play_sound(self.rocket_shot, .1)

        elif key == arcade.key.SPACE and self.health <= 0 <= self.lives and not self.GAME_START:
            self.health = 100
            self.current_room = 0
            self.GAME_START = True

    # Stop moving on key release
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

    # Shoot bullets on click
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked and if there is ammunition.
        """
        if self.GAME_START and self.ammunition >= 1:
            # Create a bullet
            bullet = arcade.Sprite("bullet.png", SPRITE_SCALING_LASER)

            bullet.angle = self.player_sprite.angle

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top
            if self.player_sprite.angle == 90:
                self.tiled_rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_x += 5
                bullet.change_y += BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(self.shot, .2)

            elif self.player_sprite.angle == 270:
                self.tiled_rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_x -= 5
                bullet.center_y -= 20
                bullet.change_y -= BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(self.shot, .2)

            elif self.player_sprite.angle == 180:
                self.tiled_rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_y -= 10
                bullet.change_x -= BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(self.shot, .2)

            elif self.player_sprite.angle == 0:
                self.tiled_rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_y -= 20
                bullet.change_x += BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(self.shot, .2)
        elif self.ammunition == 0:
            arcade.play_sound(self.dryfire, .2)

    # noinspection PyGlobalUndefined
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        global enemy, missile, enemy_hit_list

        # Call update on all sprites
        self.physics_engine.update()
        for physics_engine_enemy in self.physics_engine_enemies:
            physics_engine_enemy.update()

        self.tiled_rooms[self.current_room].coin_list.update()
        self.tiled_rooms[self.current_room].bullet_list.update()
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            self.tiled_rooms[self.current_room].enemy_list.update()
        self.tiled_rooms[self.current_room].ammo_box_list.update()
        self.tiled_rooms[self.current_room].explosions_list.update()
        self.tiled_rooms[self.current_room].missile_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.tiled_rooms[self.current_room].coin_list)
        ammo_box_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.tiled_rooms[self.current_room].ammo_box_list)
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                  self.tiled_rooms[self.current_room].enemy_list)
        enemy_bullet_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                     self.tiled_rooms[
                                                                         self.current_room].enemy_bullet_list)

        # Loop through all explosions and enemies to check for collisions
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                if arcade.check_for_collision_with_list(enemy, self.tiled_rooms[self.current_room].explosions_list):
                    # Remove enemy and explosion
                    enemy.remove_from_sprite_lists()

        # Loop through all enemies to check for bullet collisions and remove enemies if necessary
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                bullet_hit_list = arcade.check_for_collision_with_list(enemy,
                                                                       self.tiled_rooms[self.current_room]
                                                                       .bullet_list)
                for bullet in bullet_hit_list:
                    enemy.health -= 50
                    self.score += 30
                    bullet.remove_from_sprite_lists()
                    arcade.play_sound(self.impact, .2)
                    if enemy.health <= 0:
                        enemy.remove_from_sprite_lists()

        # Loop through all missiles to check for collisions with enemies and create explosions if necessary
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for missile in self.tiled_rooms[self.current_room].missile_list:
                hit_list = arcade.check_for_collision_with_list(missile, self.tiled_rooms[self.current_room].enemy_list)
                if hit_list:
                    # Create explosion
                    explosion = explosions.Explosion(self.explosion_texture_list)
                    explosion.center_x = hit_list[0].center_x
                    explosion.center_y = hit_list[0].center_y
                    explosion.update()
                    self.tiled_rooms[self.current_room].explosions_list.append(explosion)
                    arcade.play_sound(self.missile_explosion, 0.1)

                    # Remove missile and enemy if necessary
                    missile.remove_from_sprite_lists()
                    for enemy in hit_list:
                        enemy.health -= 50
                        self.score += 100
                        if enemy.health <= 0:
                            enemy.remove_from_sprite_lists()

        # Remove missiles from the last room
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for missile in self.tiled_rooms[self.last_room].missile_list:
                missile.remove_from_sprite_lists()

        # Loop through each bullet to check for wall collision
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for bullet in self.tiled_rooms[self.current_room].bullet_list:
                bullet_hit_list = arcade.check_for_collision_with_list(bullet,
                                                                       self.tiled_rooms[self.current_room].wall_list)
                for _ in bullet_hit_list:
                    bullet.remove_from_sprite_lists()

        # Loop through each colliding sprite, remove it, and add to the score.
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                arcade.play_sound(self.coin_bing, .1)
                self.score += 25
                self.coins_collected += 1

        # Check for collision with ammo boxes
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for ammo_box in ammo_box_hit_list:
                ammo_box.remove_from_sprite_lists()
                arcade.play_sound(self.collecting_ammo, 1.5)
                self.magazine += 2
                self.special += 1

        # Check for collision with enemies and player
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for enemy in enemy_hit_list:
                if self.health >= 0:
                    self.health -= .3
                    self.score -= .01
                else:
                    pass

        # Check for collision with enemy vomit and player
        if self.tiled_rooms[self.current_room].enemy_list is not None:
            for i in enemy_bullet_hit_list:
                if self.health >= 0:
                    self.health -= 1
                    self.score -= .01
                else:
                    pass
        # Draw the explosions
        for explosion in self.tiled_rooms[self.current_room].explosions_list:
            explosion.update()
            explosion.draw()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.

        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)
            self.player_sprite.center_x = 0

        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.last_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)

            self.player_sprite.center_x = SCREEN_WIDTH

        elif self.player_sprite.center_y < 0 and self.current_room == 1:
            self.current_room = 2
            self.last_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)

            self.player_sprite.center_y = SCREEN_HEIGHT

        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 2:
            self.current_room = 1
            self.last_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)

            self.player_sprite.center_y = 0

        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 2:
            self.current_room = 3
            self.last_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)

            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_y < 0 and self.current_room == 2:
            self.current_room = 5
            self.last_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)

            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)
            self.player_sprite.center_y = SCREEN_HEIGHT
        elif self.player_sprite.center_y < 0 and self.current_room == 3:
            self.current_room = 4
            self.last_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)
                self.player_sprite.center_y = SCREEN_HEIGHT
        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 4:
            self.current_room = 3
            self.last_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y < 0 and self.current_room == 4:
            self.current_room = 6
            self.last_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []

            self.player_sprite.center_y = SCREEN_HEIGHT

        elif self.player_sprite.center_x < 0 and self.current_room == 4:
            self.current_room = 5
            self.last_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 5:
            self.current_room = 4
            self.last_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 5:
            self.current_room = 2
            self.last_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            # Create a list of physics engines for the enemies in this room
            self.physics_engine_enemies = []
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                physics_engine_enemy = arcade.PhysicsEngineSimple(enemy,
                                                                  self.tiled_rooms[self.current_room].wall_list)
                self.physics_engine_enemies.append(physics_engine_enemy)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 6:
            self.current_room = 4
            self.last_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.tiled_rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH / 2
            self.player_sprite.center_y = 0

        # Use the distance formula to calculate how close enemies are to player before they engage
        if self.GAME_START:
            if self.tiled_rooms[self.current_room].enemy_list is not None:
                for Enemy in self.tiled_rooms[self.current_room].enemy_list:
                    # Position the start at the Enemy's current location
                    start_x = Enemy.center_x
                    start_y = Enemy.center_y

                    # Get the destination location for the player
                    dest_x = self.player_sprite.center_x
                    dest_y = self.player_sprite.center_y

                    # Calculate the distance between the Enemy and the player
                    a_diff = dest_x - start_x
                    b_diff = dest_y - start_y
                    distance_fmla = math.sqrt(a_diff ** 2 + b_diff ** 2)

                    # If the distance is less than or equal to 50, engage the player
                    if distance_fmla <= 300:
                        Enemy.follow_sprite(self.player_sprite)

        # loop through the missiles to heat seek or move off-screen.
        for Missile in self.tiled_rooms[self.current_room].missile_list:
            if self.tiled_rooms[self.current_room].enemy_list:
                Missile.follow_sprite(enemy)
            else:
                if self.player_sprite.angle == 90:
                    missile.change_y += 3
                    missile.angle = self.player_sprite.angle - 90
                elif self.player_sprite.angle == 270:
                    missile.change_y -= 3
                    missile.angle = self.player_sprite.angle - 90
                elif self.player_sprite.angle == 180:
                    missile.change_x -= 3
                    missile.angle = self.player_sprite.angle - 90
                elif self.player_sprite.angle == 0:
                    missile.change_x += 3
                    missile.angle = self.player_sprite.angle - 90

        # Loop through each enemy that we have
        if self.GAME_START:
            if self.tiled_rooms[self.current_room].enemy_list is not None:
                for enemy in self.tiled_rooms[self.current_room].smart_enemy_list:

                    # Have a random 1 in 200 change of shooting each 1/60th of a second
                    odds = 1000

                    # Adjust odds based on delta-time
                    adj_odds = int(odds * (1 / 60) / delta_time)

                    if random.randrange(adj_odds) == 0:
                        enemy_vomit = arcade.Sprite("vomit.png", SPRITE_SCALING_LASER)
                        enemy_vomit.center_x = enemy.center_x
                        enemy_vomit.center_y = enemy.center_y
                        self.tiled_rooms[self.current_room].enemy_bullet_list.append(enemy_vomit)
                        arcade.play_sound(self.zombie_spit, .2)

        # If statement to assist with death
        if self.health <= 0:
            self.GAME_START = False

        # Win condition
        if len(self.tiled_rooms[0].smart_enemy_list) == 0 and len(self.tiled_rooms[1].smart_enemy_list) == 0 and \
                len(self.tiled_rooms[2].smart_enemy_list) == 0 and len(self.tiled_rooms[3].smart_enemy_list) == 0 and \
                len(self.tiled_rooms[4].smart_enemy_list) == 0 and len(self.tiled_rooms[5].smart_enemy_list) == 0:
            self.GAME_WIN = True


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
