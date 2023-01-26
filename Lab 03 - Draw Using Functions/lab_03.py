# Imported arcade library
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
def draw_water():
    arcade.draw_rectangle_filled(500, 0, SCREEN_WIDTH, -500, arcade.csscolor.BLUE)

# Defining a function to draw a bubble at (x, y)
def draw_bubble(x, y):
    arcade.draw_arc_outline(x, y, 50, 50, arcade.csscolor.BLACK, 0, 360, 3)
    arcade.draw_arc_outline(x + 7, y + 10, 10, 10, arcade.csscolor.BLACK, 0, 360, 2)

# Defining a function to animate bubbles vertically
def animate_v1(delta_time):
    arcade.start_render()

    draw_water()

    draw_bubble(100, 400)
    draw_bubble(200, 200)
    draw_bubble(300, 800)
    draw_bubble(400, 500)
    draw_bubble(500, 400)
    draw_bubble(600, 700)
    draw_bubble(700, 100)
    draw_bubble(800, 400)
    draw_bubble(900, 200)

    draw_bubble(150, animate_v1.draw_bubble_y +150)
    draw_bubble(350, animate_v1.draw_bubble_y)
    draw_bubble(550, animate_v1.draw_bubble_y + 300)
    draw_bubble(750, animate_v1.draw_bubble_y + 50)
    draw_bubble(75, animate_v1.draw_bubble_by + 150)
    draw_bubble(250, animate_v1.draw_bubble_by)
    draw_bubble(450, animate_v1.draw_bubble_by + 300)
    draw_bubble(650, animate_v1.draw_bubble_by + 50)
    animate_v1.draw_bubble_y += 2
    animate_v1.draw_bubble_by += 1

animate_v1.draw_bubble_y = 0
animate_v1.draw_bubble_by = 100

# Defining main function
def main():
    arcade.open_window(1000, 1000, "The Function drawing")

    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    arcade.schedule(animate_v1, 1 / 60)

    arcade.run()

main()
