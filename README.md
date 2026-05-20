# InterviewIQ — AI Interview Question Generator

A minimal, elegant web app that generates role-specific interview questions using Google Gemini AI.

## Local Setup

1. Get a free Gemini API key at [ai.google.dev](https://ai.google.dev)

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your API key:
```bash
set GEMINI_API_KEY=your_key_here
```

4. Run:
```bash
python app.py
```

5. Open http://localhost:3000

## Deploy to AWS (Elastic Beanstalk)

Prerequisites: AWS CLI configured (`aws configure`) and EB CLI installed (`pip install awsebcli`).

```bash
set GEMINI_API_KEY=your_key_here
deploy.bat
```

Or manually:
```bash
eb init interview-questions-app --region us-east-1 --platform "Python 3.12 running on 64bit Amazon Linux 2023"
eb create interviewiq-env --single --instance-type t3.micro
aws elasticbeanstalk update-environment --environment-name interviewiq-env --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=GEMINI_API_KEY,Value=YOUR_KEY
eb deploy
eb open
```

## Tech Decisions

- **Google Gemini 2.0 Flash** — fast, free tier, excellent at structured output
- **Python + Flask** — clean, readable, easy to explain in a walkthrough
- **Vanilla HTML/CSS/JS frontend** — zero build step, instant load
- **Apple glassmorphic UI** — frosted glass aesthetic with animated liquid background
- **AWS Elastic Beanstalk** — production-grade hosting, auto-scaling, easy CLI deploy
