import numpy as np
from time import time

if __name__=="__main__":
    from sys import path 
    path.append("/home/qrapilly/Documents/Code/MesProjets/PySnake/src/models")

    import napari

from base_snake import BasicSnake
from tools.basis_function import create_basis_function, create_basis_periodic_function
from tools.compute_init_cp import create_init_control_points



class ParametricSnake3D(BasicSnake):

    def __init__(self, name : str,M1 : int, M2 : int, cell_img_ratio : float = 0.5) -> None:
        super().__init__(name, cell_img_ratio)

        self.M1 = M1
        self.M2 = M2

        self.phi1 = create_basis_periodic_function(M1)
        self.phi2 = create_basis_function(M2)

    
    def set_control_points(self, control_points):

        self.control_points = control_points


    def init_control_points(self, verbose : bool = False):

        self.control_points = create_init_control_points(self.M1, self.M2, verbose=verbose)

    def points_on_surface(self, u : np.array, v : np.array, verbose : bool = False):

        n_u, n_v = len(u), len(v)

        k = np.expand_dims(np.arange(0, self.M1, step=1),0)
        l = np.expand_dims(np.arange(-1, self.M2+2, step=1),0)

        if verbose :
            print("shape of k : {}".format(k.shape))
            print("shape of l : {}".format(l.shape))

        phi_1 = self.phi1(self.M1*u-k)
        phi_2 = self.phi2(self.M2*v-l)

        if verbose :
            print("shape of phi_1 : {}".format(phi_1.shape))
            print("shape of phi_2 : {}".format(phi_2.shape))


        phi_1_extended = np.expand_dims(phi_1, (1,3))
        phi_2_extended = np.expand_dims(phi_2, (0,2))

        if verbose :
            print("shape of phi_1_extended : {}".format(phi_1_extended.shape))
            print("shape of phi_2_extended : {}".format(phi_2_extended.shape))

        phi_kl = phi_1_extended*phi_2_extended

        if verbose :
            print("shape of phi_kl : {}".format(phi_kl.shape))

        sigma = np.sum(np.expand_dims(self.control_points,(0,1))*np.expand_dims(phi_kl,(4)), axis=(2,3))

        if verbose :
            print("Shape of sigma : {}".format(sigma.shape))

        return sigma


    def get_sampled_surface(self, points_per_dim : tuple[int, int], verbose : bool = False):
        
        n_u, n_v = points_per_dim

        u = np.expand_dims(np.linspace(0, n_u/(n_u+1), n_u),1)
        v = np.expand_dims(np.linspace(0, 1, n_v),1)

        if verbose :
            print("shape of u : {}".format(u.shape))
            print("shape of v : {}".format(v.shape))

        sample_points = self.points_on_surface(u,v, verbose = verbose)
        
        # TODO : construire les facets

        return sample_points


if __name__ == "__main__":

    snake = ParametricSnake3D("test_snake", M1=8, M2=4)

    print("## Control points initialisation ...")
    tic = time()
    snake.init_control_points(verbose = True)
    tac = time()
    print("Step done in {}s\n".format(tac-tic))

    print("## Sampling of the surface ...")
    tic = time()
    points = snake.get_sampled_surface(points_per_dim=(10, 10), verbose=True)
    tac = time()
    print("Step done in {}s\n".format(tac-tic))
    a,b,c = points.shape

    reshaped_points = np.reshape(points,(a*b,c))*10

    #R = np.sum(points*points, axis = 2)

    #eps = 0.05
    #print((np.abs(R-1)<eps))

    viewer = napari.view_points(reshaped_points, ndisplay=3, size=1)

    napari.run()