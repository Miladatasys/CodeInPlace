from graphics import Canvas

# Constants for patch and canvas size
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 2
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Dibuja el patch de sakura en la posición (0, 0)
    draw_sakura_img(canvas, 0, 0)

    # Puedes añadir más imágenes aquí, por ejemplo:
    draw_yukito_img(canvas, PATCH_SIZE, 0)

"""
Función que dibuja la imagen de sakura en un patch
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
Función que dibuja la imagen de yukito en un patch
"""
def draw_yukito_img(canvas, left_x, top_y):
    canvas.create_image_with_size(
        left_x,
        top_y,
        PATCH_SIZE,
        PATCH_SIZE,
        "yukito"
    )

if __name__ == '__main__':
    main()
