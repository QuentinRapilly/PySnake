import numpy as np
from math import cos, pi, floor, ceil


def create_interval_mask(t, lower_bound, upper_bound):
    """
        Return a binary with 1 where lower_bound <= t < upper_bound and 0 elsewhere.
    """
    return (lower_bound <= t)*(t<upper_bound)*1.

def create_basis_function(M):

    def basis_function_t(t):
        abs_t = np.abs(t)

        mask_0 = create_interval_mask(abs_t, 0, 0.5)
        values_0 = mask_0*(np.cos(2*pi*abs_t/M)*cos(pi/M) - cos(2*pi/M))

        mask_1 = create_interval_mask(abs_t, 0.5, 1.5)
        values_1 = mask_1*(np.sin(pi*(3/2-abs_t)/M)*np.sin(pi*(3/2-abs_t)/M))
        
        phi_M_t = 1/(1-cos(2*pi/M))*(values_0 + values_1)

        return phi_M_t

    return basis_function_t

def create_basis_periodic_function(M):

    basis_fct_aux = create_basis_function(M)

    a = 3/2 
    # Pour comprendre le role de a, relire la these sur l'implem 
    # (globalement c'est la moitie du support de la fonction de base)

    n_min = floor(-a/M - (M-1)/M)
    n_max = ceil(1-a/M)

    # j'ai du aggrandir les bornes. Pourquoi, je ne sais pas ... à creuser

    def basis_periodic_function(t):
        phi_t = basis_fct_aux(t-M*n_min)
        for n in range(n_min+1,n_max+1):
            phi_t = phi_t + basis_fct_aux(t-M*n)
        
        return phi_t

    return basis_periodic_function


