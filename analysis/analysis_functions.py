import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def colour_range(N: int = 9, colour_map: str = 'viridis'):
    """ Return a range of hex colour codes for a particular colour map.
    
    :param N: number of desired colour codes (default is 9).
    :param colour_map: type of colour map (default is 'viridis').
    :return: list of hex colour codes
    """
    base = plt.cm.get_cmap(colour_map)
    colour_list = base(np.linspace(0, 1, N))
    colour_hex_list=[]
    for i in range (N-1, -1, -1):
         colour_hex_list.append(colors.rgb2hex(colour_list[i]))
    return colour_hex_list

def x_ray_wavelength(x_ray_energy: float = 89.07) -> float:
    """ Calculate X-ray wavelength (in metres) from X-ray energy (in keV) using Planck's equation.
    
    :param x_ray_energy: X-ray energy in keV (default is 89.07 keV).
    :return: X-ray wavelength in metres.
    """ 
    c = 2.99792458e8
    h = 6.62607004e-34
    e = 1.6021766208e-19
    x_ray_wavelength=(h * c) / (x_ray_energy * 1e3 * e)
    return x_ray_wavelength

def calc_dspacing(two_theta: float, x_ray_energy: float = 89.07) -> float:
    """ Calculate d-spacing from 2-theta values using Bragg's law.
    
    :param two_theta: 2-theta value in degrees.
    :param x_ray_energy: X-ray energy in keV (default is 89.07 keV).
    :return: d-spacing in metres.
    """ 
    c = 2.99792458e8
    h = 6.62607004e-34
    e = 1.6021766208e-19
    x_ray_wavelength = (h * c) / (x_ray_energy * 1e3 * e)
    dspacing = x_ray_wavelength / (2 * np.sin(np.array(two_theta) * np.pi / 360))
    return dspacing

def calc_strain(two_theta: np.ndarray, zero_range: int = 1) -> np.ndarray:
    """ Calculate strain from 2-theta values.
    
    :param two_theta: 2-theta value in degrees.
    :param zero_range: Integer used to define a range of points to calculate an average initial 2-theta value
                       (default is 1).
    :return: NumPy array of strain values in degrees.
    """ 
    two_theta = 0.5 * (np.array(two_theta)) * np.pi / 180.0
    two_theta_0 = np.mean(two_theta[0:zero_range])
    print(two_theta_0)
    strain = - (two_theta - two_theta_0) / np.tan(two_theta)
    return strain

def relative_amplitude(amplitude: np.ndarray) -> np.ndarray:
    """ Divide an array of amplitude values by the first value in the array.
    
    :param amplitude: NumPy array of amplitude float values.
    :return: NumPy array of float values.
    """ 
    relative_amplitude = np.array(amplitude) / amplitude[0]
    return relative_amplitude