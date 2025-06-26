from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    
    str = f"""For the given statement, the system response is 'anger': {result['anger']}, 
    'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy':{result['joy']} 
    and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."""

    return str


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    
