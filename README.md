# InterviewIQ — AI Interview Question Generator

A minimal, elegant web app that generates role-specific interview questions using Google Gemini AI. Built with Flask, vanilla JS, and a frosted-glass UI.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.0%20Flash-orange)
![Deploy](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-yellow)

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/reuben-idan/interview-questions-app.git
cd interview-questions-app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Gemini API key (get one free at https://ai.google.dev)
set GEMINI_API_KEY=your_key_here

# 4. Run the app
python app.py

# 5. Open in browser
start http://localhost:3000
```

## Project Structure

```
interview-questions-app/
├── app.py                  # Flask server + Gemini API integration
├── public/
│   └── index.html          # Frontend (HTML/CSS/JS single file)
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn config for production
├── deploy.bat              # One-click AWS deployment script
├── .ebextensions/
│   └── 01_python.config    # Elastic Beanstalk settings
└── .env                    # API key (not committed)
```

## Deploy

### Render (Free)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com), connect your GitHub repo
3. Create a new **Web Service**, select this repo
4. Add environment variable: `GEMINI_API_KEY` = your key
5. Deploy — Render auto-detects the `render.yaml` config

### AWS Elastic Beanstalk

Prerequisites: AWS CLI configured (`aws configure`) and EB CLI installed (`pip install awsebcli`).

```bash
set GEMINI_API_KEY=your_key_here
deploy.bat
```

Or step by step:

```bash
eb init interview-questions-app --region us-east-1 --platform "Python 3.12 running on 64bit Amazon Linux 2023"
eb create interviewiq-env --single --instance-type t3.micro
aws elasticbeanstalk update-environment --environment-name interviewiq-env --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=GEMINI_API_KEY,Value=YOUR_KEY
eb deploy
eb open
```

## Tech Stack

| Layer | Choice | Why |
|-------|--------|-----|
| AI | Google Gemini 2.0 Flash | Fast, free tier, great structured output |
| Backend | Python + Flask | Clean, readable, minimal boilerplate |
| Frontend | Vanilla HTML/CSS/JS | Zero build step, instant load |
| UI Style | Apple glassmorphic | Frosted glass + animated liquid background |
| Hosting | AWS Elastic Beanstalk | Production-grade, auto-scaling, easy CLI deploy |

## License

MIT
