''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion and its confidence 
        score for the provided text.
    '''
    text = request.args.get('textToAnalyze')
    if not text:  # Handle missing text
        return "Invalid text! Please try again!"  # Bad Request

    response = emotion_detector(text)

    # Handle invalid responses or blank input scenarios
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"  # Bad Request

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    return (f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.errorhandler(500)
def server_error(error):
    ''' This function handles server errors
    '''
    return (f"Internal Server Error. Please try again later.{error}"), 500

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
