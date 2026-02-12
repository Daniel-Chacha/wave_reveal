import numpy as np

class DepthExtractor:
    def extract(self, image, z_extent=0.5):
        
        magnitude = np.abs(image)
        
        size = magnitude.shape[0]
        z = np.linspace(0, z_extent, size)
        
        depth_map = np.zeros(magnitude.shape[1])
        
        for x_idx in range(magnitude.shape[1]):
            column = magnitude[:, x_idx]
            max_idx = np.argmax(column)
            depth_map[x_idx] = z[max_idx]
        
        return depth_map
