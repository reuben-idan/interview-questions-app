# InterviewIQ

AI-powered interview question generator. Enter any job title, get 3 tailored interview questions instantly.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash%20Lite-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Live Demo

🔗 [https://interview-questions-app-8xn9.onrender.com](https://interview-questions-app-8xn9.onrender.com)

## Features

- Role-specific question generation via Google Gemini 2.5 Flash Lite
- Clean glassmorphic UI with animated loading state
- Error handling with user-friendly feedback
- Single-page frontend, zero build step

## Tech Stack

| Layer | Technology |
|-------|-----------|
| AI | Google Gemini 2.5 Flash Lite |
| Backend | Python, Flask |
| Frontend | Vanilla HTML/CSS/JS |
| Hosting | Render |

## Run Locally

```bash
git clone https://github.com/reuben-idan/interview-questions-app.git
cd interview-questions-app
pip install -r requirements.txt
set GEMINI_API_KEY=your_key_here
python app.py
```

Open http://localhost:3000

## Project Structure

```
├── app.py              # Flask server + Gemini integration
├── public/
│   └── index.html      # Frontend (single file)
├── requirements.txt    # Dependencies
├── render.yaml         # Render deployment config
├── Procfile            # Production server command
└── .env                # API key (not committed)
```

## Deployment

### Render (Free)

1. Connect this repo at [render.com](https://render.com)
2. Add env var: `GEMINI_API_KEY`
3. Deploy — auto-configured via `render.yaml`

### AWS Elastic Beanstalk

```bash
set GEMINI_API_KEY=your_key_here
deploy.bat
```

## Design Decisions

- **Gemini 2.5 Flash Lite** — fast inference, free tier, reliable structured output
- **Flask** — minimal overhead for a single-endpoint API
- **Vanilla JS** — no framework needed for a focused UI; instant load
- **Prompt engineering** — requests exactly 3 questions as a JSON array, assessing both technical and behavioral fit

## License

MIT
