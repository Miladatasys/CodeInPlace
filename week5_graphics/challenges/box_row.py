from graphics import Canvas
"""
400px wide x 200px High
Each box size: 400 / 5: 80px wide and 80px tall
"""
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES #80x80 pixels

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    """
    Milestone #1:   Draw 5 boxes that sit side by side 
                    at the bottom of the canvas 
    """
    for i in range(N_BOXES): 
        """
        Milestone #2:   Breakdown the coordinates
        """ 
        # Calculate the left boundary of each box by multiplying 
        # the index i with the box size, with each box being directly 
        # adjacent on the x-axis.
        left_x = i * BOX_SIZE
        right_x = left_x + BOX_SIZE

        # Vertical position is fixed: boxes are at the bottom
        bottom_y = CANVAS_HEIGHT
        top_y =  bottom_y - BOX_SIZE

        """
        Milestone #3: Create the canvas
        """
        canvas.create_rectangle(
            left_x, # horizontal start
            top_y,  # vertical start
            right_x,# horizontal end
            bottom_y,# vertical end,
            "white",
            "black"
        )

if __name__ == '__main__':
    main()
    