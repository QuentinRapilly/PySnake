import napari
import numpy as np

from src.models.base_snake import BasicSnake


def draw_snake_on_image(img, snake : BasicSnake, editable : bool = True):

    viewer = napari.view_image(img, ndisplay=3)
    
    vertices, faces = snake.get_last_vertices(), snake.get_last_facets()
    values = values = np.linspace(0,1,(len(vertices)))

    name = snake.get_name()

    snake_params = (vertices, faces, values)

    points_layer = viewer.add_points(vertices, ndim=3, name="{}_vertices".format(name))
    surface_layer = viewer.add_surface(snake_params ,name=name, colormap="turbo", opacity=0.8)

    def click_drag(layer, event):
        if layer.mode == "select":
            dragged = False
            yield
            # on move
            while event.type == 'mouse_move':
                dragged = True
                yield
            # on release
            if dragged and len(layer.selected_data) > 0:
                surface_layer.vertices = layer.data
                snake.set_current_vertices(layer.data)

    if editable:
        points_layer.mouse_drag_callbacks.append(click_drag)

    

    napari.run()


