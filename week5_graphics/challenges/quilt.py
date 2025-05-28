from graphics import Canvas

# Constants
PATCH_SIZE = 100
NUM_COLS = 4
NUM_ROWS = 2
CANVAS_WIDTH = PATCH_SIZE * NUM_COLS
CANVAS_HEIGHT = PATCH_SIZE * NUM_ROWS

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            x = col * PATCH_SIZE
            y = row * PATCH_SIZE

            if (row + col) % 2 == 0:
                draw_sakura_img(canvas, x, y)
            else:
                draw_kerberos_img(canvas, x, y)

"""
SAKURA PATCH
"""
def draw_sakura_img(canvas, left_x, top_y):
    canvas.create_image_with_size(
        left_x,
        top_y,
        PATCH_SIZE,
        PATCH_SIZE,
        "sakura"
    )

"""
KERO PATCH
"""
def draw_kerberos_img(canvas, left_x, top_y):
    canvas.create_image_with_size(
        left_x,
        top_y,
        PATCH_SIZE,
        PATCH_SIZE,
        "kerberos"  
    )

if __name__ == '__main__':
    main()
