import numpy as np

class RadarSensor:
    def __init__(self,
                 fc=77e9,
                 bandwidth=1e9,
                 num_aperture_positions=32,
                 aperture_length=0.2):
        
        self.c = 3e8
        self.fc = fc
        self.bandwidth = bandwidth
        self.lambda_c = self.c / fc

        self.num_aperture_positions = num_aperture_positions
        self.aperture_positions = np.linspace(
            -aperture_length/2,
            aperture_length/2,
            num_aperture_positions
        )

        self.range_resolution = self.c / (2 * bandwidth)

    def info(self):
        return {
            "carrier_frequency": self.fc,
            "bandwidth": self.bandwidth,
            "wavelength": self.lambda_c,
            "range_resolution": self.range_resolution
        }
