"""
For this problem, we have provided three circles: one is red, one 
is blue, and one is white (making it hidden since the background 
is white). Modify the code to change the white circle's color 
to instead be purple so we can see it! You can go online to find 
lots of different hex codes for all sorts 
of colors for later projects! :)

(Hint: Purple is the color we get when we mix/add red 
and blue together. What do we think the hex code would 
look like with that information?)
"""

from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    """
    Notice how we just added the "#990000" and "#000099" hex 
    codes together to make "#990099"?
    This is because we are literally adding the amounts of red 
    and blue we want to make purple!
    """

    canvas.create_oval(CANVAS_WIDTH/2 - 75, 225, CANVAS_WIDTH/2 + 75, 375, color="#990099")


    # Draw a red circle
    canvas.create_oval(25, 25, 175, 175, color="#990000")
    
    # Draw a plus sign
    canvas.create_line(190, 100, 210, 100)
    canvas.create_line(200, 90, 200, 110)
    
    # Draw a blue circle
    canvas.create_oval(CANVAS_WIDTH/2 + 25, 25, CANVAS_WIDTH/2 + 175, 175, color="#000099")
    
    # Draw an arrow
    canvas.create_line(200, 170, 200, 210)
    canvas.create_line(200, 210, 190, 190)
    canvas.create_line(200, 210, 210, 190)
    

if __name__ == '__main__':
    main()