from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from camera import VideoCamera
from events import EventDetector
from database import insert_event
import cv2

app = Flask(__name__)
socketio = SocketIO(app)

camera = VideoCamera()
detector = EventDetector()

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    while True:
        frame, gray = camera.get_frame()
        if frame is None:
            continue

        event = detector.detect_motion(gray)
        if event:
            insert_event(event)
            socketio.emit("event", event)

        cv2.putText(frame, f"FPS: {int(camera.fps)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               buffer.tobytes() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    socketio.run(app, debug=True)

