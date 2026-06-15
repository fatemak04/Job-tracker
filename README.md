# Job Application Tracker

The Job Application Tracker is a web-based application designed to help students efficiently manage, organize, and monitor their job applications throughout the recruitment process. The project demonstrate full-stack application development, automated testing, continuous integration, and deployment practices.

![CI/CD Pipeline](https://github.com/fatemak04/Job-tracker/actions/workflows/ci.yml/badge.svg)

## Live Demo
🌐 [View Live App](https://job-tracker-82ag.onrender.com)

## Features
- Add job applications with company, position, and date 
- Update application status (Applied, OA, Interview, Offer, Rejected)
- Delete applications no longer needed for tracking
- Automated tests and deployment via GitHub Actions

## CI/CD Pipeline
Every push to `main`:
1. GitHub Actions installs dependencies
2. Runs automated tests with pytest
3. If tests pass, deploys automatically to Render <br>
If tests fail, deployment blocked and notified instantly

## Run locally
```bash
pip install -r requirements.txt
python app.py
```
Then open http://localhost:5000

## Tech stack
- Python + Flask
- SQLite
- pytest
- GitHub Actions
- Render (hosting)
