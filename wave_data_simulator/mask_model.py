import numpy as np

class MaskMaterial:
    
    MATERIALS = {
        "cotton": {"epsilon_r": 1.6, "loss": 0.02, "thickness": 0.002},
        "polyester": {"epsilon_r": 2.9, "loss": 0.04, "thickness": 0.002},
        "wool": {"epsilon_r": 1.4, "loss": 0.03, "thickness": 0.003}
    }
    
    def __init__(self, material="cotton", fc=77e9):
        self.params = self.MATERIALS[material]
        self.fc = fc
        self.c = 3e8
        self.lambda_c = self.c / fc
        
    def modify(self, amplitude, phase):
        
        epsilon_r = self.params["epsilon_r"]
        loss = self.params["loss"]
        thickness = self.params["thickness"]
        
        # Phase shift inside dielectric
        delta_phase = (2 * np.pi / self.lambda_c) * thickness * np.sqrt(epsilon_r)
        
        # Attenuation
        attenuation = np.exp(-loss * thickness)
        
        new_amplitude = amplitude * attenuation
        new_phase = phase + delta_phase
        
        return new_amplitude, new_phase
