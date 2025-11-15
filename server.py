"""Flask web server for Emotion Detection using Watson NLP library."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Initialize Flask application
app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/emotion_detector', methods=['GET', 'POST'])
def emotion_detector_route():
    """Process user input and return emotion detection results.

    Handles both POST form data and GET query parameters. Returns a
    formatted string of emotion scores and the dominant emotion.
    """
    text_to_analyse = ''
    if request.method == 'POST':
        text_to_analyse = request.form.get('statement', '').strip()
    else:
        text_to_analyse = request.args.get('textToAnalyze', '').strip()

    if not text_to_analyse:
        return "Invalid text! Please try again!", 200

    result = emotion_detector(text_to_analyse)

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!", 200

    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_result


if __name__ == "__main__":
    app.run(debug=True)
