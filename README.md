# EduGenie - Google Gemini Powered Learning Assistant

EduGenie is a lightweight educational assistant built with FastAPI, HTML/CSS, and the Google Gemini API.

## Features
- Question & Answer
- Simple topic explanation
- 3-question MCQ quiz generation
- Text summarization
- Personalized learning path

## Project structure
```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 1. Open the project in VS Code
Extract the ZIP and open the `EduGenie` folder in VS Code.

## 2. Check Python
```powershell
python --version
```
Python 3.10+ is recommended.

## 3. Create a virtual environment
```powershell
python -m venv .venv
```

## 4. Activate it on Windows PowerShell
```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:
```cmd
.venv\Scripts\activate
```

## 5. Install packages
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 6. Add your Gemini API key
Copy `.env.example` to `.env`:
```powershell
copy .env.example .env
```

Open `.env` and replace:
```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```
with your own Gemini API key.

NEVER upload `.env` to GitHub. `.gitignore` already excludes it.

## 7. Run
```powershell
uvicorn main:app --reload
```

Open:
http://127.0.0.1:8000

Health check:
http://127.0.0.1:8000/health

## 8. GitHub
```powershell
git init
git add .
git commit -m "Initial EduGenie project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Do not commit your `.env` file or API key.

## Troubleshooting
- `No module named ...`: run `pip install -r requirements.txt`.
- `GEMINI_API_KEY is not set`: check that `.env` exists beside `main.py`.
- PowerShell activation issue: use Command Prompt and `.venv\Scripts\activate`.
- Port already in use: run `uvicorn main:app --reload --port 8001` and open http://127.0.0.1:8001.
