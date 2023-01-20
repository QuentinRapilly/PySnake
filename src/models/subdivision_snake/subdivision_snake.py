import numpy as np

from ..base_snake import BasicSnake

class SubdivisionSnake3D(BasicSnake):

    def __init__(self, cell_img_ratio : float = 0.25, name : str = "Default_snake") -> None:

        super().__init__(name, cell_img_ratio)

        self.vertices = []
        self.normal_triangles = []
        self.normal_vertices = []
        self.facets = []



    def init_vertices_positions(self, init_x_y_z : np.array = None):
        assert(self.is_img_loaded)

        if init_x_y_z == None :
            self.init_x_y_z = self.img_shape//2
        else :
            self.init_x_y_z = init_x_y_z

        control_points = self.vertices_init = np.array([
            [-0.5, 0, 0],
            [0.5, 0, 0],
            [0, -0.5, 0],
            [0, 0.5, 0],
            [0, 0, -0.5],
            [0, 0, 0.5]
        ])

        self.control_points = control_points*self.img_shape*self.cell_img_ratio + self.init_x_y_z

        self.vertices.append(self.control_points)
    
    def get_current_nb_vertices(self):
        return len(self.vertices[-1])

    def init_facets(self):
        self.facets_init = np.array([
            [0,4,3],
            [0,4,2],
            [0,5,2],
            [0,5,3],
            [1,4,3],
            [1,4,2],
            [1,5,2],
            [1,5,3]
        ])

        self.facets.append(self.facets_init)

    def get_last_vertices(self):
        return self.vertices[-1]

    def get_last_facets(self):
        return self.facets[-1]


    def set_current_vertices(self, data):
        assert data.shape == self.vertices[-1].shape

        self.vertices[-1] = data