from graphics import Canvas

# Constant defining the size of the canvas
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    # Create a canvas with specified width and height
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    """
    Draw a red rectangle representing the top half of the Indonesian flag
    Parameters are: left_x, top_y, right_x, bottom_y, color
    (0, 0) is the top-left corner
    (450, 150) covers the top half (width=450, height=150)
    """
    rect = canvas.create_rectangle(0, 0, 450, 150, 'red')
    print(rect)
if __name__ == '__main__':
    main()