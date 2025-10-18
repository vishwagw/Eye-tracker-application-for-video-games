# basic application with fundamental features:

import cv2
import dlib
import numpy as np
import pyautogui

# create the class for eyetracker:
class EyeTracker:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.screen_width, self.screen_height = pyautogui.size()
        
    def get_eye_region(self, landmarks):
        # Extract left and right eye coordinates
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]
        return left_eye, right_eye
    
# estimatig the gaze direction:
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

# mapping the gaze to screen coordinates:
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