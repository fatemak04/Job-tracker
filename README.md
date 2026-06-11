# Job Application Tracker

A simple web app to track internship and job applications — built with Python/Flask.

![CI/CD Pipeline](https://github.com/fatemak04/job-tracker/actions/workflows/ci.yml/badge.svg)

## Features
- Add, view, and delete job applications
- Update application status (Applied, OA, Interview, Offer, Rejected)
- Automated tests and deployment via GitHub Actions

## CI/CD Pipeline
Every push to `main`:
1. GitHub Actions installs dependencies
2. Runs automated tests with pytest
3. If tests pass, deploys automatically to Render

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
