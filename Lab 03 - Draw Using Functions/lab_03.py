# Imported arcade library

import arcade

# Set variables tied to screen width and height to be used in later functions

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Function for drawing our water
def draw_water():
    arcade.draw_rectangle_filled(500, 0, SCREEN_WIDTH, -500, arcade.csscolor.BLUE)

# Defining a function to draw a bubble at (x, y)
def draw_bubble(x, y):
    arcade.draw_circle_filled(x, y, 25, arcade.csscolor.WHITE)
    arcade.draw_arc_outline(x, y, 50, 50, arcade.csscolor.BLACK, 0, 360, 3)
    arcade.draw_arc_outline(x + 7, y + 10, 10, 10, arcade.csscolor.BLACK, 0, 360, 2)


# Defining a function to draw our bubbles, as well as animate them
def animate_v1(delta_time):
    arcade.start_render()

    draw_water()

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

    draw_bubble(750, animate_v1.draw_bubble_w + 50)
    draw_bubble(350, animate_v1.draw_bubble_w + 250)


    draw_bubble(650, animate_v1.draw_bubble_x + 50)
    draw_bubble(75, animate_v1.draw_bubble_x + 250)

    draw_bubble(925, animate_v1.draw_bubble_y)

    draw_bubble(450, animate_v1.draw_bubble_z)

    # Giving different values for Y to increase by, so I can have different speeds of bubble movement.

    animate_v1.draw_bubble_y += 6
    animate_v1.draw_bubble_z += 12
    animate_v1.draw_bubble_x += 9
    animate_v1.draw_bubble_w += 12
    animate_v1.draw_bubble_a += 15
    animate_v1.draw_bubble_b += 18



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

# Defining main function
def main():
    arcade.open_window(1000, 1000, "The Function drawing")

    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    arcade.schedule(animate_v1, 1 / 60)

    arcade.run()

# Running the main function

main()
