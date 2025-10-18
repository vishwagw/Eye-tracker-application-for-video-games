def optimize_performance(self):
    # Reduce processing resolution
    self.process_width = 320
    self.process_height = 240
    
    # Frame skipping
    self.process_every_n_frames = 2
    
    # Use GPU acceleration if available
    if self.has_gpu:
        self.enable_gpu_processing()