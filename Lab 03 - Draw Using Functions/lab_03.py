# Imported arcade library

import arcade

# Set variables to be used in later functions

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
A = 6
B = 9
C = 3
D = 10
# Function for drawing the clouds

def draw_cloud(x, y):
    arcade.draw_circle_filled(x, y, 50, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 50, y + 50, 50, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 50, y + 50, 50, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 50, y, 50, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 50, y, 50, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x, y + 75, 50, arcade.csscolor.WHITE)

# Function for drawing the water

def draw_water():
    arcade.draw_rectangle_filled(500, 0, SCREEN_WIDTH, -500, arcade.csscolor.BLUE)

# Defining a function to draw a bubble at (x, y)

def draw_bubble(x, y):
    arcade.draw_circle_filled(x, y, 25, arcade.csscolor.WHITE)
    arcade.draw_circle_outline(x, y, 25, arcade.csscolor.BLACK, 3)
    arcade.draw_circle_outline(x + 7, y + 10, 5, arcade.csscolor.BLACK, 2)

# Drawing a sun in the sky

def draw_sun(x, y):
    arcade.draw_circle_filled(x, y, 150, arcade.csscolor.ORANGE)

# Defining a function to draw our bubbles, as well as animate them

def animate_v1(delta_time):
    arcade.start_render()

    draw_water()

    draw_sun(100, 1000)

    draw_bubble(0, 250)
    draw_bubble(50, 260)
    draw_bubble(100, 250)
    draw_bubble(125, 175)
    draw_bubble(150, 260)
    draw_bubble(200, 250)
    draw_bubble(250, 260)
    draw_bubble(300, 250)
    draw_bubble(325, 100)
    draw_bubble(350, 260)
    draw_bubble(400, 250)
    draw_bubble(450, 200)
    draw_bubble(450, 260)
    draw_bubble(500, 250)
    draw_bubble(550, 260)
    draw_bubble(575, 125)
    draw_bubble(600, 250)
    draw_bubble(650, 260)
    draw_bubble(700, 250)
    draw_bubble(750, 260)
    draw_bubble(800, 250)
    draw_bubble(810, 190)
    draw_bubble(850, 260)
    draw_bubble(900, 250)
    draw_bubble(950, 260)
    draw_bubble(1000, 250)

    draw_bubble(550, animate_v1.draw_bubble_a + 125)
    draw_bubble(250, animate_v1.draw_bubble_a + 200)

    draw_bubble(150, animate_v1.draw_bubble_b + 150)
    draw_bubble(750, animate_v1.draw_bubble_b+ 150)

    draw_bubble(800, animate_v1.draw_bubble_w + 50)
    draw_bubble(350, animate_v1.draw_bubble_w + 250)


    draw_bubble(650, animate_v1.draw_bubble_x + 50)
    draw_bubble(75, animate_v1.draw_bubble_x + 250)

    draw_bubble(925, animate_v1.draw_bubble_y)

    draw_bubble(450, animate_v1.draw_bubble_z)

    # Giving different values for Y to increase by, so I can have different speeds of bubble movement.

    animate_v1.draw_bubble_y += 6
    animate_v1.draw_bubble_z += 3
    animate_v1.draw_bubble_x += 9
    animate_v1.draw_bubble_w += 6
    animate_v1.draw_bubble_a += 9
    animate_v1.draw_bubble_b += 6

    # If statements to reset bubbles to bubble line for repeating animation.

    if animate_v1.draw_bubble_a >= 1000:
        animate_v1.draw_bubble_a = 0

    if animate_v1.draw_bubble_b >= 1000:
        animate_v1.draw_bubble_b = 0

    if animate_v1.draw_bubble_w >= 1000:
        animate_v1.draw_bubble_w = 0

    if animate_v1.draw_bubble_x >= 1000:
        animate_v1.draw_bubble_x = 0

    if animate_v1.draw_bubble_y >= 1000:
        animate_v1.draw_bubble_y = 0

    if animate_v1.draw_bubble_z >= 1000:
        animate_v1.draw_bubble_z = 0

# Setting values for Y coordinates / variables.

animate_v1.draw_bubble_y = 0
animate_v1.draw_bubble_z = 130
animate_v1.draw_bubble_x = 250
animate_v1.draw_bubble_w = 100
animate_v1.draw_bubble_a = 50
animate_v1.draw_bubble_b = 50

# Defining second animation for clouds
def animate_v2(delta_time):

    draw_cloud(animate_v2.a - 200, 900)
    draw_cloud(animate_v2.c - 400, 750)

    draw_cloud(animate_v2.b + 400, 800)
    draw_cloud(animate_v2.d + 800, 1700)



    animate_v2.a += D
    animate_v2.b += D
    animate_v2.c += D
    animate_v2.d += D

    if animate_v2.a >= 2000:
        animate_v2.a = 0

    if animate_v2.b >= 2000:
        animate_v2.b = 0

    if animate_v2.c >= 2000:
        animate_v2.c = 0

    if animate_v2.d >= 2000:
        animate_v2.d = 0

# defining variables to be used by clouds
animate_v2.a = -500
animate_v2.b = -500
animate_v2.c = -500
animate_v2.d = -500
animate_v2.e = -500




# Defining main function
def main():
    arcade.open_window(1000, 1000, "The Function drawing")

    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    arcade.schedule(animate_v2, 1 / 60)

    arcade.schedule(animate_v1, 1 / 60)

    arcade.run()

# Running the main function
main()
