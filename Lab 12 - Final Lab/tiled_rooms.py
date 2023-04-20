import arcade
import random
import enemies

TILE_SCALING = 1

# Player starting position
PLAYER_START_X = 64
PLAYER_START_Y = 225

# Layer Names from our TileMap
LAYER_NAME_WALLS = "walls"
LAYER_NAME_DEBRIS = "debris"
LAYER_NAME_GROUND = "ground"

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
NUMBER_OF_AMMO_BOX = 2
NUMBER_OF_ENEMIES = 5


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.coin_list = None
        self.bullet_list = None
        self.enemy_bullet_list = None
        self.ammo_box_list = None
        self.enemy_list = None
        self.smart_enemy_list = None
        self.explosions_list = []
        self.missile_list = None
        self.tile_map = None

        # This holds the background images. If you don't want to be changing
        # background images, you can delete this part.
        self.background = None


def setup_room_1():
    """
    Create and return room 1.
    """
    room = Room()

    # Set up tile map

    room.map_name = "room_1.tmx"

    # Layer specific options are defined based on Layer names in a dictionary
    # Doing this will make the SpriteList for the platforms layer
    # use spatial hashing for detection.
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
    }
    # Read in the tiled map
    room.tile_map = arcade.load_tilemap(room.map_name, TILE_SCALING, layer_options)

    # Initialize Scene with our TileMap, this will automatically add all layers
    # from the map as SpriteLists in the scene in the proper order.
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    # --- Other stuff
    # Set the background color
    if room.tile_map.background_color:
        arcade.set_background_color(room.tile_map.background_color)

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()
    room.smart_enemy_list = arcade.SpriteList()
    room.enemy_bullet_list = arcade.SpriteList()

    # Get the "walls" SpriteList from the scene and assign it to the Room's wall_list attribute
    room.wall_list = room.scene[LAYER_NAME_WALLS]

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

    for i in range(NUMBER_OF_AMMO_BOX):
        ammo_box = arcade.Sprite("ammo_box.png", 1.0)

        # Boolean variable if we successfully placed the ammo_box
        box_placed_successfully = False

        # Keep trying until success
        while not box_placed_successfully:
            # Position the ammo_box
            ammo_box.center_x = random.randrange(SCREEN_WIDTH)
            ammo_box.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the ammo_box is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(ammo_box, room.wall_list)

            # See if the ammo_box is hitting another coin
            box_hit_list = arcade.check_for_collision_with_list(ammo_box, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(box_hit_list) == 0:
                # It is!
                box_placed_successfully = True

        # Add the ammo_box to the lists
        room.ammo_box_list.append(ammo_box)

    for i in range(NUMBER_OF_ENEMIES):
        enemy = enemies.Enemy("zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the enemy is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the enemy to the lists
        room.enemy_list.append(enemy)

    for i in range(round(NUMBER_OF_ENEMIES/2)):
        enemy = enemies.SmartEnemy("smart_zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the enemy is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the enemy to the lists
        room.enemy_list.append(enemy)
        room.smart_enemy_list.append(enemy)

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    # Set up tile map

    room.map_name = "room_2.tmx"

    # Layer specific options are defined based on Layer names in a dictionary
    # Doing this will make the SpriteList for the platforms layer
    # use spatial hashing for detection.
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
    }
    # Read in the tiled map
    room.tile_map = arcade.load_tilemap(room.map_name, TILE_SCALING, layer_options)

    # Initialize Scene with our TileMap, this will automatically add all layers
    # from the map as SpriteLists in the scene in the proper order.
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    # --- Other stuff
    # Set the background color
    if room.tile_map.background_color:
        arcade.set_background_color(room.tile_map.background_color)

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()
    room.smart_enemy_list = arcade.SpriteList()
    room.enemy_bullet_list = arcade.SpriteList()

    # Get the "walls" SpriteList from the scene and assign it to the Room's wall_list attribute
    room.wall_list = room.scene[LAYER_NAME_WALLS]

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

    for i in range(NUMBER_OF_AMMO_BOX):
        ammo_box = arcade.Sprite("ammo_box.png", 1.0)

        # Boolean variable if we successfully placed the ammo_box
        box_placed_successfully = False

        # Keep trying until success
        while not box_placed_successfully:
            # Position the ammo_box
            ammo_box.center_x = random.randrange(SCREEN_WIDTH)
            ammo_box.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the ammo_box is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(ammo_box, room.wall_list)

            # See if the ammo_box is hitting another coin
            box_hit_list = arcade.check_for_collision_with_list(ammo_box, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(box_hit_list) == 0:
                # It is!
                box_placed_successfully = True

        # Add the ammo_box to the lists
        room.ammo_box_list.append(ammo_box)

    for i in range(round(NUMBER_OF_ENEMIES*2)):
        enemy = enemies.Enemy("zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the ammo_box is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the ammo_box to the lists
        room.enemy_list.append(enemy)
    for i in range(round(NUMBER_OF_ENEMIES)):
        enemy = enemies.SmartEnemy("smart_zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the enemy is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the enemy to the lists
        room.enemy_list.append(enemy)
        room.smart_enemy_list.append(enemy)

    return room

def setup_room_3():
    """
    Create and return room 3.
    """
    room = Room()

    # Set up tile map

    room.map_name = "room_3.tmx"

    # Layer specific options are defined based on Layer names in a dictionary
    # Doing this will make the SpriteList for the platforms layer
    # use spatial hashing for detection.
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
    }
    # Read in the tiled map
    room.tile_map = arcade.load_tilemap(room.map_name, TILE_SCALING, layer_options)

    # Initialize Scene with our TileMap, this will automatically add all layers
    # from the map as SpriteLists in the scene in the proper order.
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    # --- Other stuff
    # Set the background color
    if room.tile_map.background_color:
        arcade.set_background_color(room.tile_map.background_color)

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()
    room.smart_enemy_list = arcade.SpriteList()
    room.enemy_bullet_list = arcade.SpriteList()

    # Get the "walls" SpriteList from the scene and assign it to the Room's wall_list attribute
    room.wall_list = room.scene[LAYER_NAME_WALLS]

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

    for i in range(NUMBER_OF_AMMO_BOX):
        ammo_box = arcade.Sprite("ammo_box.png", 1.0)

        # Boolean variable if we successfully placed the ammo_box
        box_placed_successfully = False

        # Keep trying until success
        while not box_placed_successfully:
            # Position the ammo_box
            ammo_box.center_x = random.randrange(SCREEN_WIDTH)
            ammo_box.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the ammo_box is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(ammo_box, room.wall_list)

            # See if the ammo_box is hitting another coin
            box_hit_list = arcade.check_for_collision_with_list(ammo_box, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(box_hit_list) == 0:
                # It is!
                box_placed_successfully = True

        # Add the ammo_box to the lists
        room.ammo_box_list.append(ammo_box)

    for i in range(round(NUMBER_OF_ENEMIES*2)):
        enemy = enemies.Enemy("zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the ammo_box is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the ammo_box to the lists
        room.enemy_list.append(enemy)
    for i in range(round(NUMBER_OF_ENEMIES)):
        enemy = enemies.SmartEnemy("smart_zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the enemy is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the enemy to the lists
        room.enemy_list.append(enemy)
        room.smart_enemy_list.append(enemy)

    return room

def setup_room_4():
    """
    Create and return room 4.
    """
    room = Room()

    # Set up tile map

    room.map_name = "room_4.tmx"

    # Layer specific options are defined based on Layer names in a dictionary
    # Doing this will make the SpriteList for the platforms layer
    # use spatial hashing for detection.
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
    }

    # Read in the tiled map
    room.tile_map = arcade.load_tilemap(room.map_name, TILE_SCALING, layer_options)

    # Initialize Scene with our TileMap, this will automatically add all layers
    # from the map as SpriteLists in the scene in the proper order.
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    # --- Other stuff
    # Set the background color
    if room.tile_map.background_color:
        arcade.set_background_color(room.tile_map.background_color)

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.smart_enemy_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()
    room.enemy_bullet_list = arcade.SpriteList()

    # Get the "walls" SpriteList from the scene and assign it to the Room's wall_list attribute
    room.wall_list = room.scene[LAYER_NAME_WALLS]

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

    for i in range(NUMBER_OF_AMMO_BOX):
        ammo_box = arcade.Sprite("ammo_box.png", 1.0)

        # Boolean variable if we successfully placed the ammo_box
        box_placed_successfully = False

        # Keep trying until success
        while not box_placed_successfully:
            # Position the ammo_box
            ammo_box.center_x = random.randrange(SCREEN_WIDTH)
            ammo_box.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the ammo_box is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(ammo_box, room.wall_list)

            # See if the ammo_box is hitting another coin
            box_hit_list = arcade.check_for_collision_with_list(ammo_box, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(box_hit_list) == 0:
                # It is!
                box_placed_successfully = True

        # Add the ammo_box to the lists
        room.ammo_box_list.append(ammo_box)

    for i in range(NUMBER_OF_ENEMIES):
        enemy = enemies.Enemy("smart_zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the ammo_box is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the ammo_box to the lists
        room.enemy_list.append(enemy)
        room.smart_enemy_list.append(enemy)

    return room


def setup_room_5():
    """
    Create and return room 5.
    """
    room = Room()

    # Set up tile map

    room.map_name = "room_5.tmx"

    # Layer specific options are defined based on Layer names in a dictionary
    # Doing this will make the SpriteList for the platforms layer
    # use spatial hashing for detection.
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
    }

    # Read in the tiled map
    room.tile_map = arcade.load_tilemap(room.map_name, TILE_SCALING, layer_options)

    # Initialize Scene with our TileMap, this will automatically add all layers
    # from the map as SpriteLists in the scene in the proper order.
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    # --- Other stuff
    # Set the background color
    if room.tile_map.background_color:
        arcade.set_background_color(room.tile_map.background_color)

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.smart_enemy_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()
    room.enemy_bullet_list = arcade.SpriteList()

    # Get the "walls" SpriteList from the scene and assign it to the Room's wall_list attribute
    room.wall_list = room.scene[LAYER_NAME_WALLS]

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

    for i in range(NUMBER_OF_AMMO_BOX):
        ammo_box = arcade.Sprite("ammo_box.png", 1.0)

        # Boolean variable if we successfully placed the ammo_box
        box_placed_successfully = False

        # Keep trying until success
        while not box_placed_successfully:
            # Position the ammo_box
            ammo_box.center_x = random.randrange(SCREEN_WIDTH)
            ammo_box.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the ammo_box is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(ammo_box, room.wall_list)

            # See if the ammo_box is hitting another coin
            box_hit_list = arcade.check_for_collision_with_list(ammo_box, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(box_hit_list) == 0:
                # It is!
                box_placed_successfully = True

        # Add the ammo_box to the lists
        room.ammo_box_list.append(ammo_box)

    for i in range(NUMBER_OF_ENEMIES):
        enemy = enemies.Enemy("zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the ammo_box is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the ammo_box to the lists
        room.enemy_list.append(enemy)

    for i in range(round(NUMBER_OF_ENEMIES)):
        smart_enemy = enemies.SmartEnemy("smart_zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            smart_enemy.center_x = random.randrange(SCREEN_WIDTH)
            smart_enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(smart_enemy, room.wall_list)

            # See if the enemy is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(smart_enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the enemy to the lists
        room.enemy_list.append(smart_enemy)

        room.smart_enemy_list.append(smart_enemy)

    return room


def setup_room_6():
    """
    Create and return room 6.
    """
    room = Room()

    # Set up tile map

    room.map_name = "room_6.tmx"

    # Layer specific options are defined based on Layer names in a dictionary
    # Doing this will make the SpriteList for the platforms layer
    # use spatial hashing for detection.
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
    }

    # Read in the tiled map
    room.tile_map = arcade.load_tilemap(room.map_name, TILE_SCALING, layer_options)

    # Initialize Scene with our TileMap, this will automatically add all layers
    # from the map as SpriteLists in the scene in the proper order.
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    # --- Other stuff
    # Set the background color
    if room.tile_map.background_color:
        arcade.set_background_color(room.tile_map.background_color)

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.smart_enemy_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()
    room.enemy_bullet_list = arcade.SpriteList()

    # Get the "walls" SpriteList from the scene and assign it to the Room's wall_list attribute
    room.wall_list = room.scene[LAYER_NAME_WALLS]

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

    for i in range(NUMBER_OF_AMMO_BOX):
        ammo_box = arcade.Sprite("ammo_box.png", 1.0)

        # Boolean variable if we successfully placed the ammo_box
        box_placed_successfully = False

        # Keep trying until success
        while not box_placed_successfully:
            # Position the ammo_box
            ammo_box.center_x = random.randrange(SCREEN_WIDTH)
            ammo_box.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the ammo_box is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(ammo_box, room.wall_list)

            # See if the ammo_box is hitting another coin
            box_hit_list = arcade.check_for_collision_with_list(ammo_box, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(box_hit_list) == 0:
                # It is!
                box_placed_successfully = True

        # Add the ammo_box to the lists
        room.ammo_box_list.append(ammo_box)

    for i in range(NUMBER_OF_ENEMIES):
        enemy = enemies.Enemy("zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the ammo_box is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the ammo_box to the lists
        room.enemy_list.append(enemy)

    for i in range(round(NUMBER_OF_ENEMIES)):
        enemy = enemies.SmartEnemy("smart_zombie.png", SPRITE_SCALING)

        # Boolean variable if we successfully placed the enemy
        enemy_placed_successfully = False

        # Keep trying until success
        while not enemy_placed_successfully:
            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the enemy is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(enemy, room.wall_list)

            # See if the enemy is hitting another coin
            enemy_hit_list = arcade.check_for_collision_with_list(enemy, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(enemy_hit_list) == 0:
                # It is!
                enemy_placed_successfully = True

        # Add the enemy to the lists
        room.enemy_list.append(enemy)

        room.smart_enemy_list.append(enemy)

    return room


def setup_room_7():
    """
    Create and return room 7.
    """
    room = Room()

    # Set up tile map

    room.map_name = "room_7.tmx"

    # Layer specific options are defined based on Layer names in a dictionary
    # Doing this will make the SpriteList for the platforms layer
    # use spatial hashing for detection.
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
    }

    # Read in the tiled map
    room.tile_map = arcade.load_tilemap(room.map_name, TILE_SCALING, layer_options)

    # Initialize Scene with our TileMap, this will automatically add all layers
    # from the map as SpriteLists in the scene in the proper order.
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    # --- Other stuff
    # Set the background color
    if room.tile_map.background_color:
        arcade.set_background_color(room.tile_map.background_color)

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.coin_list = arcade.SpriteList()
    room.bullet_list = arcade.SpriteList()
    room.explosions_list = arcade.SpriteList()
    room.ammo_box_list = arcade.SpriteList()
    room.missile_list = arcade.SpriteList()
    room.enemy_bullet_list = arcade.SpriteList()

    # Get the "walls" SpriteList from the scene and assign it to the Room's wall_list attribute
    room.wall_list = room.scene[LAYER_NAME_WALLS]

    # If you want coins or monsters in a level, then add that code here.
    for i in range(NUMBER_OF_COINS * 5):
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

    for i in range(NUMBER_OF_AMMO_BOX * 5):
        ammo_box = arcade.Sprite("ammo_box.png", 1.0)

        # Boolean variable if we successfully placed the ammo_box
        box_placed_successfully = False

        # Keep trying until success
        while not box_placed_successfully:
            # Position the ammo_box
            ammo_box.center_x = random.randrange(SCREEN_WIDTH)
            ammo_box.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the ammo_box is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(ammo_box, room.wall_list)

            # See if the ammo_box is hitting another coin
            box_hit_list = arcade.check_for_collision_with_list(ammo_box, room.ammo_box_list)

            if len(wall_hit_list) == 0 and len(box_hit_list) == 0:
                # It is!
                box_placed_successfully = True

        # Add the ammo_box to the lists
        room.ammo_box_list.append(ammo_box)

    return room
