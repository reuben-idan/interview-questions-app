@echo off
REM ============================================
REM  AWS Elastic Beanstalk Deployment Script
REM  InterviewIQ - AI Question Generator
REM ============================================

SET APP_NAME=interview-questions-app
SET ENV_NAME=interviewiq-env
SET REGION=us-east-1
SET PLATFORM="Python 3.12 running on 64bit Amazon Linux 2023"

echo [1/5] Initializing Elastic Beanstalk...
eb init %APP_NAME% --region %REGION% --platform %PLATFORM%

echo [2/5] Creating environment...
eb create %ENV_NAME% --single --instance-type t3.micro

echo [3/5] Setting environment variables...
aws elasticbeanstalk update-environment ^
  --environment-name %ENV_NAME% ^
  --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=GEMINI_API_KEY,Value=%GEMINI_API_KEY%

echo [4/5] Deploying application...
eb deploy %ENV_NAME%

echo [5/5] Opening application...
eb open

echo Done! Your app is live.
