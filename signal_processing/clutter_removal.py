import numpy as np

class ClutterRemover:
    def remove_static_clutter(self, data):
        """
        Remove mean across aperture dimension.
        """
        mean_clutter = np.mean(data, axis=0, keepdims=True)
        return data - mean_clutter
