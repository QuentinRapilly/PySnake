from skimage.io import imread
import argparse
import sys

sys.path.append(".")

from models.subdivision_snake.subdivision_snake import SubdivisionSnake3D
from gui.draw_snake import draw_snake_on_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input_image", help="Input image on which to draw the snake")
    parser.add_argument("-r", "--ratio", type=float, help="Cell/image size ratio")
    args = parser.parse_args()

    r = args.ratio

    snake = SubdivisionSnake3D(r)

    try :
        image = imread(args.input_image)
    except Exception as e:
        print("Something went wrong while reading the image")
        print(e)

    snake.load_image(image)
    snake.init_vertices_positions()
    snake.init_facets()

    
    draw_snake_on_image(image, snake)
