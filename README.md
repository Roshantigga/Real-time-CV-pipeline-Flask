🖥️ Real-Time Computer Vision Pipeline (Flask + OpenCV)
📌 Overview

This project implements a basic real-time computer vision pipeline using Python.
It captures live video from a webcam, performs real-time frame processing, detects motion-based events, and communicates those events to a web interface using WebSockets. Detected events are also stored persistently for later analysis.

The project demonstrates understanding of:

Computer vision fundamentals

Real-time processing

Backend integration

Event-driven system design

🎯 Objective

To design and implement a real-time vision system that:

Reads a live video stream

Processes frames in real time

Detects meaningful events

Sends events to a web client

Stores events for persistence

🧠 System Architecture
Webcam → OpenCV → Event Detection → WebSocket → Browser UI
                              ↓
                          SQLite DB

🛠️ Tech Stack
Component	Technology
Backend	Flask
Real-time Communication	Flask-SocketIO (WebSockets)
Computer Vision	OpenCV
Database	SQLite
Frontend	HTML + JavaScript
Language	Python
📁 Project Structure
cv-realtime-flask/
│
├── app.py          # Flask app & WebSocket server
├── camera.py       # Video capture and frame processing
├── events.py       # Motion detection logic
├── database.py     # SQLite database handling
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html  # Web UI
│
└── static/
    └── script.js   # WebSocket client logic

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>
cd cv-realtime-flask

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000

🔍 Implementation Details
📷 Video Capture & Processing

Live webcam feed captured using OpenCV

Frames converted to grayscale

Gaussian blur applied to reduce noise

FPS calculated for performance monitoring

🚨 Event Detection Logic

Motion detection using frame differencing

Contours extracted to measure motion area

Event triggered if motion exceeds a threshold

Each event includes:

Timestamp (UTC)

Event type

Numeric motion value

🔄 Real-Time Communication

Events sent to frontend using WebSockets

JSON structured messages

No page refresh required

💾 Data Storage

SQLite database

Persistent storage of all detected events

Schema:

timestamp

event_type

value

📡 Example Event JSON
{
  "timestamp": "2025-01-01T12:45:30.123Z",
  "event_type": "motion_detected",
  "value": 5420.75
}
# Real-time-CV-pipeline-Flask
