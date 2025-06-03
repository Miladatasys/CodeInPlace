from graphics import Canvas

def main():
    # Create a canvas object
    canvas = Canvas(400, 400)

    # Draw the first car at position (10, 10)
    draw_car(canvas, 10, 10)

    # Draw the second car at position (100, 100)
    draw_car(canvas, 100, 100)

def draw_car(canvas, x, y):
    # Draw the body of the car
    canvas.create_rectangle(x, y, x + 50, y + 20)

    # Draw the top of the car
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
