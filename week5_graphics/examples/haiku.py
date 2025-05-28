"""
This program writes this haiku onto the screen in three lines, 
in the front 'Courier'. The lines of text should all be aligned 
on the left side but not overlap each other
"""

from graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
FIRST_LINE_LEFT_X = 50
FIRST_LINE_TOP_Y = 50
FONT_SIZE = 24

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
   
    # Create first line of text using the constants above
    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y,
        "An old silent pond...",
        color = "blue",
        font = "Courier",
        font_size = FONT_SIZE)
    
    # Second line of text, moved down by based on our font size
    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + FONT_SIZE,
        "A frog jumps into the pond...",
        color = "blue",
        font = "Courier",
        font_size = FONT_SIZE)

    # Third line of text 
    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + 2 * FONT_SIZE,
    "Splash! Silence again...",
    color = "blue",
    font = "Courier",
    font_size = FONT_SIZE
    )

if __name__ == '__main__':
    main()