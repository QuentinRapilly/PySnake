import numpy as np

class BasicSnake:

    def __init__(self, name, cell_img_ratio) -> None:
        
        self.is_img_loaded = False

        self.name = name


        self.cell_img_ratio = cell_img_ratio  # define the ratio size_of_a_cell/size_of_the_image


    def load_image(self, image):
        self.img = image
        
        self.img_shape = np.array(self.img.shape)

        self.cell_size_X = int(self.img_shape[0]*self.cell_img_ratio)
        self.cell_size_Y = int(self.img_shape[1]*self.cell_img_ratio)
        self.cell_size_Z = int(self.img_shape[2]*self.cell_img_ratio)

        self.is_img_loaded = True


    def get_name(self):
        return self.name
