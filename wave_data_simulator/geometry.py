import numpy as np

class FaceGeometry:
    def __init__(self, size=64, scale=0.2):
        self.size = size
        self.scale = scale

    def generate_surface(self):
        x = np.linspace(-self.scale/2, self.scale/2, self.size)
        y = np.linspace(-self.scale/2, self.scale/2, self.size)
        X, Y = np.meshgrid(x, y)

        # Head ellipsoid
        Z = 0.1 * np.exp(-(X**2 + Y**2) * 40)

        # Nose
        Z += 0.03 * np.exp(-((X)**2 + (Y - 0.02)**2) * 200)

        return X, Y, Z
