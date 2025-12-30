🖥️ Real-Time Computer Vision Pipeline
(Flask + OpenCV)
📌 Overview

This project implements a basic real-time computer vision pipeline using Python.
It captures live video from a webcam, performs real-time frame processing, detects motion-based events, and communicates those events to a web interface using WebSockets. Detected events are also stored persistently for later analysis.

This project demonstrates understanding of:

Computer vision fundamentals

Real-time processing concepts

Backend integration

Event-driven system design

🎯 Objective

To design and implement a real-time vision system that:

Reads a live video stream

Processes frames in real time

Detects meaningful events (motion)

Sends events to a web client

Stores events for persistence

Webcam → OpenCV → Event Detection → WebSocket → Browser UI
                               ↓
                           SQLite Database
| Component               | Technology                  |
| ----------------------- | --------------------------- |
| Backend                 | Flask                       |
| Real-Time Communication | Flask-SocketIO (WebSockets) |
| Computer Vision         | OpenCV                      |
| Database                | SQLite                      |
| Frontend                | HTML, JavaScript            |
| Language                | Python                      |


cv-realtime-flask/
│
├── app.py              # Flask app & WebSocket server
├── camera.py           # Video capture and frame processing
├── events.py           # Motion detection logic
├── database.py         # SQLite database handling
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html      # Web UI
│
└── static/
    └── script.js       # WebSocket client logic


Clone the Repository
git clone <repository-url>
cd cv-realtime-flask

Install Dependencies
pip install -r requirements.txt

Run the Application
python app.py


