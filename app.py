import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_text = request.form['text']
    api_key = "YOUR_API_KEY"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    params = {
        "prompt": user_text,
        "max_tokens": 100
    }
    response = requests.get(
        "https://api.openai.com/v1/engines/text-davinci-002/completions",
        headers=headers,
        params=params
    )
    if response.status_code == 200:
        response_text = response.json()['choices'][0]['text']
        return render_template('index.html', response_text=response_text)
    else:
        return render_template('index.html', response_text="Sorry, I am unable to respond at the moment.")

if __name__ == '__main__':
    app.run(debug=True)
