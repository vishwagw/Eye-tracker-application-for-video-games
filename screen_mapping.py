def map_gaze_to_screen(self, gaze_x, gaze_y):
    # Smooth the gaze coordinates
    self.gaze_buffer_x.append(gaze_x)
    self.gaze_buffer_y.append(gaze_y)
    
    # Apply smoothing (moving average)
    smooth_x = np.mean(self.gaze_buffer_x)
    smooth_y = np.mean(self.gaze_buffer_y)
    
    # Map to screen coordinates
    screen_x = int(smooth_x * self.screen_width)
    screen_y = int(smooth_y * self.screen_height)
    
    return screen_x, screen_y

