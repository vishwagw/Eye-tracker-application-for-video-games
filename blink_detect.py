def detect_blink(self, eye_aspect_ratio, threshold=0.2):
    if eye_aspect_ratio < threshold:
        self.blink_counter += 1
        if self.blink_counter > 3:  # Sustained blink
            return True
    else:
        self.blink_counter = 0
    return False