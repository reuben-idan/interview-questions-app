from flask import Flask, request, jsonify, send_from_directory
from google import genai
from dotenv import load_dotenv
import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = Flask(__name__, static_folder='public')

def get_client():
    return genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))


@app.route('/')
def index():
    return send_from_directory('public', 'index.html')


@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    job_title = data.get('jobTitle', '').strip()

    if not job_title:
        return jsonify({'error': 'Job title is required.'}), 400

    try:
        prompt = (
            f'Generate exactly 3 thoughtful, role-specific interview questions for a "{job_title}" position. '
            'The questions should assess both technical competence and behavioral fit. '
            'Return ONLY a JSON array of 3 strings. Example: ["Q1?", "Q2?", "Q3?"]'
        )

        response = get_client().models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = response.text.strip()
        start, end = text.find('['), text.rfind(']') + 1
        if start == -1 or end == 0:
            raise ValueError('Invalid response format')

        questions = json.loads(text[start:end])
        return jsonify({'questions': questions})

    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': 'Failed to generate questions. Please try again.'}), 500


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 3000)), debug=True)
