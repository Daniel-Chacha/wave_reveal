import numpy as np

class StripmapSARSimulator:
    def __init__(self, sensor, geometry, mask_model=None,
                 num_range_bins=256,
                 max_range=0.5):
        
        self.sensor = sensor
        self.geometry = geometry
        self.mask_model = mask_model
        
        self.c = 3e8
        self.lambda_c = sensor.lambda_c
        
        self.num_range_bins = num_range_bins
        self.max_range = max_range
        
        self.range_bins = np.linspace(0, max_range, num_range_bins)
        self.dr = self.range_bins[1] - self.range_bins[0]

    def simulate(self):
        
        X, Y, Z = self.geometry.generate_surface()
        
        # Flatten surface into point cloud
        points = np.stack([X.flatten(), Y.flatten(), Z.flatten()], axis=1)
        
        raw_data = np.zeros(
            (self.sensor.num_aperture_positions, self.num_range_bins),
            dtype=np.complex64
        )
        
        for i, aperture_x in enumerate(self.sensor.aperture_positions):
            
            # Sensor position (stripmap along x)
            sensor_pos = np.array([aperture_x, 0.0, 0.0])
            
            for point in points:
                
                # Distance from sensor to point
                d = np.linalg.norm(point - sensor_pos)
                
                if d > self.max_range:
                    continue
                
                # Two-way distance
                d_tw = 2 * d
                
                # Compute range bin
                r_index = int(d_tw / self.dr)
                
                if r_index >= self.num_range_bins:
                    continue
                
                # Phase term
                phase = (4 * np.pi * d) / self.lambda_c
                
                # Amplitude decay
                amplitude = 1 / (d**2 + 1e-6)
                
                # Apply mask if exists
                if self.mask_model:
                    amplitude, phase = self.mask_model.modify(amplitude, phase)
                
                raw_data[i, r_index] += amplitude * np.exp(1j * phase)
        
        return raw_data
