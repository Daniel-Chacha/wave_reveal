import numpy as np

class BackProjectionReconstructor:
    def __init__(self, sensor, range_bins):
        self.sensor = sensor
        self.range_bins = range_bins

    def reconstruct(self, sar_data, x_extent=0.2, z_extent=0.5, size=128):
        
        x = np.linspace(-x_extent/2, x_extent/2, size)
        z = np.linspace(0, z_extent, size)
        
        image = np.zeros((size, size), dtype=np.complex64)
        
        for ix, xi in enumerate(x):
            for iz, zi in enumerate(z):
                
                pixel_value = 0
                
                for a_idx, aperture_x in enumerate(self.sensor.aperture_positions):
                    
                    sensor_pos = np.array([aperture_x, 0.0, 0.0])
                    pixel_pos = np.array([xi, 0.0, zi])
                    
                    d = np.linalg.norm(pixel_pos - sensor_pos)
                    d_tw = 2 * d
                    
                    r_index = int(d_tw / (self.range_bins[1] - self.range_bins[0]))
                    
                    if r_index < len(self.range_bins):
                        pixel_value += sar_data[a_idx, r_index]
                
                image[iz, ix] = pixel_value
        
        return image
