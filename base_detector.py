import cv2
import dlib
import numpy as np
import pyautogui

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