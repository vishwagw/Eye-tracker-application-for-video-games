def estimate_gaze_direction(self, eye_points, frame):
    # Create mask for eye region
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
    points = np.array(eye_points, dtype=np.int32)
    cv2.fillPoly(mask, [points], 255)
    
    # Extract eye region and find iris
    eye_region = cv2.bitwise_and(frame, frame, mask=mask)
    gray_eye = cv2.cvtColor(eye_region, cv2.COLOR_BGR2GRAY)
    
    # Use Hough Circles to detect iris
    circles = cv2.HoughCircles(gray_eye, cv2.HOUGH_GRADIENT, 1, 20,
                             param1=50, param2=30, minRadius=5, maxRadius=30)
    
    if circles is not None:
        iris_x, iris_y = circles[0][0][0], circles[0][0][1]
        return self.calculate_gaze_ratio(eye_points, iris_x, iris_y)
    
    return 0.5  # Default center position