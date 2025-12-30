
import cv2
from datetime import datetime
import time

class EventDetector:
    def __init__(self):
        self.prev_gray = None
        self.last_event_time = 0
        self.motion_counter = 0

        # Tuning parameters
        self.MIN_MOTION_AREA = 2500
        self.REQUIRED_FRAMES = 3     # motion must persist
        self.COOLDOWN_SECONDS = 2    # no spam events

    def detect_motion(self, gray):
        if self.prev_gray is None:
            self.prev_gray = gray
            return None

        frame_delta = cv2.absdiff(self.prev_gray, gray)
        thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        motion_area = 0
        for c in contours:
            area = cv2.contourArea(c)
            if area < self.MIN_MOTION_AREA:
                continue
            motion_area += area

        self.prev_gray = gray

        # ---- Stability check ----
        if motion_area > 0:
            self.motion_counter += 1
        else:
            self.motion_counter = 0

        current_time = time.time()

        # ---- Trigger event only if motion is stable ----
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

