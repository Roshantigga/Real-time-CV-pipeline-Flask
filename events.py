import cv2
import time
from datetime import datetime

class EventDetector:
    def __init__(self):
        self.prev_gray = None
        self.last_event_time = 0
        self.motion_counter = 0

        self.MIN_MOTION_AREA = 2500
        self.REQUIRED_FRAMES = 3
        self.COOLDOWN_SECONDS = 2

    def detect_motion(self, gray):
        if self.prev_gray is None:
            self.prev_gray = gray
            return None

        delta = cv2.absdiff(self.prev_gray, gray)
        thresh = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        motion_area = 0
        for c in contours:
            if cv2.contourArea(c) < self.MIN_MOTION_AREA:
                continue
            motion_area += cv2.contourArea(c)

        self.prev_gray = gray

        if motion_area > 0:
            self.motion_counter += 1
        else:
            self.motion_counter = 0

        current_time = time.time()

        if (
            self.motion_counter >= self.REQUIRED_FRAMES and
            current_time - self.last_event_time > self.COOLDOWN_SECONDS
        ):
            self.last_event_time = current_time
            self.motion_counter = 0

            return {
                "timestamp": datetime.utcnow().isoformat(),
                "event_type": "motion_detected",
                "value": motion_area
            }

        return None
