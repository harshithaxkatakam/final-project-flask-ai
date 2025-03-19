# 📝 Emotion Detection Web Application

This project is a **Flask-based web application** that performs **emotion detection** on user-provided text using an external **AI-powered sentiment analysis API**.

## 📌 Features

- **Real-time Emotion Detection**: Analyzes text and returns emotions (anger, disgust, fear, joy, sadness).
- **Dominant Emotion Calculation**: Identifies the strongest emotion in the given text.
- **Flask API with Error Handling**: Handles blank input and invalid responses.
- **Web Interface**: A simple front-end to interact with the API.
- **Deployment Ready**: Can be hosted locally or on a cloud platform.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **API**: Watson Emotion Analysis API
- **Deployment**: Localhost / Cloud-based (optional)

## 📂 Project Structure
bash
```
📁 final_project/
│── 📁 oaqjp-final-project-emb-ai/
│   │── 📁 templates/         # Contains HTML files (index.html)
│   │── 📁 static/            # Contains CSS, JavaScript
│   │── 📝 README.md          # Project Documentation
│   │── 📜 server.py          # Flask Application
│   │── 📜 emotion_detection.py  # API Integration & Error Handling
│   │── 📜 requirements.txt   # Dependencies

```

## 🚀 Getting Started

### 1️⃣ Install Dependencies
First, install required Python packages:
```
pip install -r requirements.txt
```
### 2️⃣ Run the Flask Server
Start the server with:
```
python3 server.py
```
The application will be available at: http://localhost:5000
### 3️⃣ Using the API
To analyze text via API, send a GET request to:
```
http://localhost:5000/emotionDetector?textToAnalyze=Your+text+here
http://localhost:5000/emotionDetector?textToAnalyze=I love my life
```
📌 Response Example:
```
For the given statement, the system response is 'anger': 0.0021, 'disgust': 0.0018, 'fear': 0.0042, 'joy': 0.9804 and 'sadness': 0.0115. The dominant emotion is joy.
```
🛑 Error Handling
-  Blank Input:
```
Response: "Invalid text! Please try again!"
Status Code: 400 Bad Request
```
-  Server Errors:
```
Response: "Internal Server Error. Please try again later."
Status Code: 500 Internal Server Error
```
