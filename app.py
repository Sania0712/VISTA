from flask import Flask, render_template, request, jsonify
import requests
import wikipedia

app = Flask(__name__)

# === API KEYS REMOVED FOR GIT UPLOAD.....ENTER YOUR OWN API ID TO USE THE PROJECT....YOU CAN GET YOUR API IDS ON OPENAI,GEMINI AND OPENROUTER.
OPENAI_API_KEY = 'ENTER YOUR API ID'
GEMINI_API_KEY = 'ENTER YOUR API ID'
OPENROUTER_API_KEY = 'ENTER YOUR API ID'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message', '')

    # === 1. Try OpenAI ===
    if OPENAI_API_KEY:
        try:
            openai_response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": user_input}]
                }
            )
            if openai_response.status_code == 200:
                reply = openai_response.json()['choices'][0]['message']['content']
                return jsonify({'reply': reply.strip()})
        except Exception:
            pass

    # === 2. Try Gemini ===
    if GEMINI_API_KEY:
        try:
            gemini_response = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}",
                json={"contents": [{"parts": [{"text": user_input}]}]}
            )
            if gemini_response.status_code == 200:
                candidates = gemini_response.json()['candidates']
                reply = candidates[0]['content']['parts'][0]['text']
                return jsonify({'reply': reply.strip()})
        except Exception:
            pass

    # === 3. Try OpenRouter ===
    if OPENROUTER_API_KEY:
        try:
            openrouter_response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openrouter/auto",
                    "messages": [{"role": "user", "content": user_input}]
                }
            )
            if openrouter_response.status_code == 200:
                reply = openrouter_response.json()['choices'][0]['message']['content']
                return jsonify({'reply': reply.strip()})
        except Exception:
            pass

    # === 4. Wikipedia Fallback ===
    try:
        topic = user_input.lower().replace('wikipedia', '').strip()
        summary = wikipedia.summary(topic, sentences=2)
        return jsonify({'reply': summary})
    except Exception:
        return jsonify({'reply': "Sorry, I couldn't find any information."})

if __name__ == '__main__':
    app.run(debug=True)
