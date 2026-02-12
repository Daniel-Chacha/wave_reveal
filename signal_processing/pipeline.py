class SignalProcessingPipeline:
    
    def __init__(self, sensor, range_bins):
        from .range_processing import RangeProcessor
        from .clutter_removal import ClutterRemover
        from .backprojection import BackProjectionReconstructor
        from .depth_extraction import DepthExtractor
        
        self.range_processor = RangeProcessor()
        self.clutter_remover = ClutterRemover()
        self.backprojection = BackProjectionReconstructor(sensor, range_bins)
        self.depth_extractor = DepthExtractor()

    def run(self, raw_data):
        
        compressed = self.range_processor.range_compress(raw_data)
        clean = self.clutter_remover.remove_static_clutter(compressed)
        image = self.backprojection.reconstruct(clean)
        depth = self.depth_extractor.extract(image)
        
        return image, depth
