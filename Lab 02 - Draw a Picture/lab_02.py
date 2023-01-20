"""
This is a drawing for Lab_02.py
"""

# Import arcade Library
import arcade

# Open a window
# From the "arcade" Library, use a function called "open_window"
# Set the dimensions (width, height)
# Set the window title to "Drawing Example"
arcade.open_window(600, 600, "Lab_02")

# Set background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a sunset and sun
arcade.draw_lrtb_rectangle_filled(0, 600, 350, 300, arcade.csscolor.FUCHSIA)
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 250, arcade.csscolor.ORANGE_RED)
arcade.draw_circle_filled(150, 250, 40, arcade.color.ARYLIDE_YELLOW)

# Rectangle for Ocean
arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, arcade.csscolor.BLUE)

# Boat
# Arc is centered at (300, 340) with a width of 110 and a height of -100
# The starting angle is 0, and ending angle is 180.
arcade.draw_arc_filled(300, 275, 125, -150, arcade.csscolor.SIENNA, 0, 180)

# Smoke Stack of Boat
arcade.draw_rectangle_filled(300, 305, 20, 60, arcade.csscolor.GRAY)

# Flag with pole
# Triangle Coordinates
# (300, 390), (300,350), (365, 350)
arcade.draw_triangle_filled(300, 390, 300, 350, 365, 350, arcade.csscolor.RED)
arcade.draw_rectangle_filled(300, 360, 5, 50, arcade.csscolor.SIENNA)

# Cargo on Boat
arcade.draw_polygon_filled(((330, 310), (320, 295), (310, 275), (350, 275), (345, 295)), arcade.csscolor.ORANGE)
arcade.draw_polygon_filled(((270, 310), (280, 295), (290, 275), (250, 275), (255, 295)), arcade.csscolor.ORANGE)

# Draw a simple bird using lines
arcade.draw_line(355, 325, 375, 300, arcade.color.BLACK)
arcade.draw_line(375, 300, 395, 325, arcade.color.BLACK)
arcade.draw_line(405, 325, 425, 300, arcade.color.BLACK)
arcade.draw_line(425, 300, 445, 325, arcade.color.BLACK)
arcade.draw_line(380, 355, 400, 330, arcade.color.BLACK)
arcade.draw_line(400, 330, 420, 355, arcade.color.BLACK)

# Draw text at (150, 450) with a font size of 24 pts.
arcade.draw_text("Ahoy Matey!", 150, 450, arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it
arcade.run()
