class HybridController:
    def __init__(self):
        self.eye_control = True
        self.sensitivity = 1.0
        self.dead_zone = 0.1  # Reduce jitter
    
    def update_input(self, gaze_x, gaze_y, keyboard, mouse):
        if self.eye_control:
            # Use gaze for camera/look control
            self.handle_gaze_input(gaze_x, gaze_y)
            # Use traditional input for movement/actions
            self.handle_traditional_input(keyboard, mouse)