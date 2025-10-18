def calibration_routine(self):
    calibration_points = [
        (0.1, 0.1), (0.5, 0.1), (0.9, 0.1),
        (0.1, 0.5), (0.5, 0.5), (0.9, 0.5),
        (0.1, 0.9), (0.5, 0.9), (0.9, 0.9)
    ]
    
    calibration_data = []
    for point in calibration_points:
        # Display target and record gaze data
        screen_x = int(point[0] * self.screen_width)
        screen_y = int(point[1] * self.screen_height)
        pyautogui.moveTo(screen_x, screen_y)
        
        # Collect gaze samples
        samples = self.collect_calibration_samples()
        calibration_data.append((point, samples))
    
    return self.calculate_calibration_matrix(calibration_data)