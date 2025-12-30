import cv2
import time

class VideoCamera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.prev_frame = None
        self.last_time = time.time()
        self.fps = 0

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # FPS calculation
        current_time = time.time()
        self.fps = 1 / (current_time - self.last_time)
        self.last_time = current_time

        return frame, gray

