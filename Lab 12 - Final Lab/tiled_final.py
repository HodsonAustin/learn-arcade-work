# Assets from freesound.org, opengameart.org and kenney.nl

import arcade
import tiled_rooms
import explosions
import missiles
import math


BOX_BUFFER = 30

SPRITE_SCALING = .5
SPRITE_SCALING_LASER = .6
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 16
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Hitman game"

MOVEMENT_SPEED = 3
BULLET_SPEED = 10
NUMBER_OF_COINS = 10

explosion_texture_count = 60

coin_bing = arcade.load_sound("silver.wav")
reload = arcade.load_sound("reload.mp3")
shot = arcade.load_sound("shot.wav")
dryfire = arcade.load_sound("dryfire.wav")
collecting_ammo = arcade.load_sound("collecting_ammo.wav")


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sound variables
        self.physics_engine_enemies = []
        self.coin_collect = coin_bing

        # Sprite lists
        self.current_room = 0
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

        columns = 9
        count = 150
        sprite_width = 111
        sprite_height = 111

        # Load the explosions from a sprite sheet
        self.explosion_texture_list = arcade.load_spritesheet("explosionBig.png", sprite_width,
                                                              sprite_height, columns, count)

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")
        self.coin_bing = arcade.load_sound("silver.wav")
        self.reload = arcade.load_sound("reload.mp3")
        self.shot = arcade.load_sound("shot.wav")
        self.dryfire = arcade.load_sound("dryfire.wav")
        self.collecting_ammo = arcade.load_sound("collecting_ammo.wav")
        self.rocket_shot = arcade.load_sound("rocket_shot.wav")
        self.missile_explosion = arcade.load_sound("missile_explode.ogg")
        self.zombie_bite = arcade.load_sound("zombie_bite.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("hitman1_gun.png", SPRITE_SCALING)
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

        # Our starting room number
        self.current_room = 0

        self.last_room = -1

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.tiled_rooms[self.current_room].wall_list)
        # Create a list of physics engines for the enemies in this room
        for enemy in self.tiled_rooms[self.current_room].enemy_list:
            physics_engine_enemy = arcade.PhysicsEngineSimple(enemy, self.tiled_rooms[self.current_room].wall_list)
            self.physics_engine_enemies.append(physics_engine_enemy)
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw our Scene
        self.tiled_rooms[self.current_room].scene.draw()

        # Draw all the walls in this room
        self.tiled_rooms[self.current_room].scene.draw()
        self.tiled_rooms[self.current_room].coin_list.draw()
        self.tiled_rooms[self.current_room].bullet_list.draw()
        self.tiled_rooms[self.current_room].ammo_box_list.draw()
        self.tiled_rooms[self.current_room].enemy_list.draw()
        self.tiled_rooms[self.current_room].explosions_list.draw()
        self.tiled_rooms[self.current_room].missile_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 40, 40, arcade.color.WHITE, 14)
        ammunition = f"Ammo: {self.ammunition}/{self.magazine}"
        arcade.draw_text(ammunition, SCREEN_WIDTH - 125, 60, arcade.color.WHITE, 14)
        ammunition = f"Rockets: {self.special}"
        arcade.draw_text(ammunition, SCREEN_WIDTH - 125, 40, arcade.color.WHITE, 14)
        health = f"Health: {round(self.health)}/100"
        arcade.draw_text(health, 40, SCREEN_HEIGHT - 75, arcade.color.RED, 20)
        remaining_enemies = f"Enemies remaining: {len(self.tiled_rooms[self.current_room].enemy_list)}"
        arcade.draw_text(remaining_enemies, 40, 75, arcade.color.RED_DEVIL, 14)
        remaining_coins = f"Coins remaining: {len(self.tiled_rooms[self.current_room].coin_list)}"
        arcade.draw_text(remaining_coins, SCREEN_WIDTH - 300, SCREEN_HEIGHT - 75, arcade.color.GOLD, 20)

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
            if self.magazine >= 1 and self.ammunition <= 7:
                self.ammunition = 8
                self.magazine -= 1
                arcade.play_sound(reload, .2)
        elif key == arcade.key.SPACE:
            if self.special >= 1:

                # Create a missile
                missile = missiles.Missile("missile.png", SPRITE_SCALING_LASER)

                missile.angle = self.player_sprite.angle

                # Position the missile
                missile.center_x = self.player_sprite.center_x
                missile.bottom = self.player_sprite.top
                self.special -= 0
                self.tiled_rooms[self.current_room].missile_list.append(missile)
                arcade.play_sound(self.rocket_shot, .1)
        else:
            pass

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
                self.tiled_rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_x += 5
                bullet.change_y += BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(shot, .2)

            elif self.player_sprite.angle == 270:
                self.tiled_rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_x -= 5
                bullet.center_y -= 20
                bullet.change_y -= BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(shot, .2)

            elif self.player_sprite.angle == 180:
                self.tiled_rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_y -= 10
                bullet.change_x -= BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(shot, .2)

            elif self.player_sprite.angle == 0:
                self.tiled_rooms[self.current_room].bullet_list.append(bullet)
                bullet.center_y -= 20
                bullet.change_x += BULLET_SPEED
                self.ammunition -= 1
                arcade.play_sound(shot, .2)
        elif self.ammunition == 0:
            arcade.play_sound(dryfire, .2)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        global enemy, missile

        # Call update on all sprites
        self.physics_engine.update()
        for physics_engine_enemy in self.physics_engine_enemies:
            physics_engine_enemy.update()

        self.tiled_rooms[self.current_room].coin_list.update()
        self.tiled_rooms[self.current_room].bullet_list.update()
        self.tiled_rooms[self.current_room].enemy_list.update()
        self.tiled_rooms[self.current_room].ammo_box_list.update()
        self.tiled_rooms[self.current_room].explosions_list.update()
        self.tiled_rooms[self.current_room].missile_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.tiled_rooms[self.current_room].coin_list)
        ammo_box_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.tiled_rooms[self.current_room].ammo_box_list)
        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.tiled_rooms[self.current_room].enemy_list)

        # Loop through all explosions and enemies to check for collisions
        if self.tiled_rooms[self.current_room].enemy_list:
            for enemy in self.tiled_rooms[self.current_room].enemy_list:
                if arcade.check_for_collision_with_list(enemy, self.tiled_rooms[self.current_room].explosions_list):
                    # Remove enemy and explosion
                    enemy.remove_from_sprite_lists()

        # Loop through all enemies to check for bullet collisions and remove enemies if necessary
        for enemy in self.tiled_rooms[self.current_room].enemy_list:
            enemy_bullet_hit_list = arcade.check_for_collision_with_list(enemy,
                                                                         self.tiled_rooms[self.current_room]
                                                                         .bullet_list)
            for bullet in enemy_bullet_hit_list:
                enemy.health -= 25
                self.score += 30
                bullet.remove_from_sprite_lists()
                if enemy.health <= 0:
                    enemy.remove_from_sprite_lists()

        # Loop through all missiles to check for collisions with enemies and create explosions if necessary
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
        for missile in self.tiled_rooms[self.last_room].missile_list:
            missile.remove_from_sprite_lists()

        # Loop through each bullet
        for bullet in self.tiled_rooms[self.current_room].bullet_list:
            bullet_hit_list = arcade.check_for_collision_with_list(bullet,
                                                                   self.tiled_rooms[self.current_room].wall_list)
            for _ in bullet_hit_list:
                bullet.remove_from_sprite_lists()

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(coin_bing, .1)
            self.score += 25

        for ammo_box in ammo_box_hit_list:
            ammo_box.remove_from_sprite_lists()
            arcade.play_sound(collecting_ammo, .5)
            self.magazine += 2
            self.special += 1

        for enemy in enemy_hit_list:
            self.health -= .5
            self.score -= .5

            # Play sound if play_sound is True
            if self.play_sound:
                arcade.play_sound(self.zombie_bite, .2)

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
            self.player_sprite.center_x = SCREEN_WIDTH/2
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_x < SCREEN_WIDTH and self.current_room == 3:
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
            self.player_sprite.center_x = SCREEN_WIDTH/2
            self.player_sprite.center_y = 0

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
            if distance_fmla <= 250:
                Enemy.follow_sprite(self.player_sprite)

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


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
