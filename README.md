# VISTA – AI Virtual Assistant with Jarvis-Style UI

**VISTA** is an advanced virtual assistant inspired by Marvel’s JARVIS, combining multiple AI models like OpenAI, Gemini, and OpenRouter. It automatically falls back to Wikipedia when no AI services are available. Designed with a modern user interface and built using Flask for the backend.

---

## Features

- Smart response handling using OpenAI, Gemini, and OpenRouter
- Automatic fallback to Wikipedia summaries
- Responsive and animated JARVIS-like UI
- Flask backend with secure API key handling
- Easily customizable frontend and backend code

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/vista.git
   cd vista

2. (Optional) Create a virtual environment

python -m venv venv
venv\Scripts\activate # Windows
# or
source venv/bin/activate # macOS/Linux


3. Install dependencies

pip install -r requirements.txt


4. Add your API keys

In app.py, replace the placeholder strings with your real API keys:

OPENAI_API_KEY = "your-openai-api-key"
GEMINI_API_KEY = "your-gemini-api-key"
OPENROUTER_API_KEY = "your-openrouter-api-key"


5. Run the project

python app.py


6. Visit the app

Open your browser and go to:

http://127.0.0.1:5000/




---

File Structure

vista/
├── static/
│ ├── css/
│ └── js/
├── templates/
│ └── index.html
├── app.py
├── requirements.txt
├── .gitignore
├── README.md


---

.gitignore

Ensure you don't upload your sensitive files:

.env
*.pyc
__pycache__/
venv/
.idea/
*.log


---

License

This project is open-source and available under the MIT License.


---

Acknowledgements

OpenAI API

Google Gemini

OpenRouter AI

Wikipedia Python Library



---

Contact

Created by Sania Sharma. Feel free to contribute or ask questions by raising issues on GitHub.
