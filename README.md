# AI-Powered Emotion Detection Web Application

This project is an **AI-powered web application** that detects emotions from text input using IBM Watson NLP Embedded AI libraries. The application is built with **Python** and **Flask**, providing a web interface for real-time emotion detection.

---

## 🔹 Features

- Detects five primary emotions: `anger`, `disgust`, `fear`, `joy`, `sadness`.
- Identifies the **dominant emotion** in the text.
- Handles blank or invalid input with error messages.
- User-friendly web interface using Flask.
- Modular design for easy integration and packaging.

---

## 🔹 Technologies Used

- Python 3.11
- Flask (Web Framework)
- IBM Watson NLP Embedded AI Libraries
- HTML, JavaScript (Frontend)
- PyLint (Static Code Analysis)
- Git and GitHub (Version Control)

---

## 🔹 Project Structure

```

final_project/
│
├── EmotionDetection/
│   ├── **init**.py
│   └── emotion_detection.py       # Emotion detection logic
│
├── templates/
│   └── index.html                 # Web interface
│
├── static/
│   └── mywebscript.js             # Frontend JS
│
├── server.py                      # Flask application server
├── test_emotion_detection.py      # Unit tests
└── README.md

````

---

## 🔹 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Hadi-Wasim/aiflask-final-project-emb-ai.git
cd final_project
````

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* Windows:

```bash
venv\Scripts\activate
```

* Linux / macOS:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

> Note: Watson NLP libraries are embedded and pre-installed in the Cloud IDE.

---

## 🔹 Usage

1. **Run the Flask application**

```bash
python server.py
```

2. **Access the web interface**

* Open your browser and go to: `http://127.0.0.1:5000`

3. **Enter a statement** in the input box and click **Run Sentiment Analysis**.

   * Example input: `I love this new technology.`
   * Output:

   ```json
   {
     "anger": 0.005,
     "disgust": 0.001,
     "fear": 0.002,
     "joy": 0.980,
     "sadness": 0.012,
     "dominant_emotion": "joy"
   }
   ```

4. **Error handling**

   * If the input is blank or invalid, the application returns:

   ```
   Invalid text! Please try again!
   ```

---

## 🔹 Running Unit Tests

Unit tests validate the emotion detection functionality:

```bash
python test_emotion_detection.py
```

* Example test cases:
  | Statement | Dominant Emotion |
  |-----------|----------------|
  | I am glad this happened | joy |
  | I am really mad about this | anger |
  | I feel disgusted just hearing about this | disgust |
  | I am so sad about this | sadness |
  | I am really afraid that this will happen | fear |

---

## 🔹 Code Quality

* Static code analysis is performed using **PyLint**.
* Aim for **10/10 PyLint score** for maintainable and clean code.

---

## 🔹 Author

**Hadi Wasim**
GitHub: [https://github.com/Hadi-Wasim](https://github.com/Hadi-Wasim)

---

## 🔹 License

This project is open-source and free to use under the MIT License.

```

---

If you want, I can also create a **shorter, visually appealing version** with badges and quick links for your GitHub repository so it looks more professional.  

Do you want me to do that?
```
