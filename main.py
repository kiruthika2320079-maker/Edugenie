from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie - Google Gemini Powered Learning Assistant")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request, "result": None, "error": None})

@app.post("/run", response_class=HTMLResponse)
async def run_task(request: Request, task: str = Form(...), text: str = Form(...)):
    result = None
    error = None
    try:
        if not text.strip():
            raise ValueError("Please enter some text.")
        if task == "qa":
            result = answer_question(text)
        elif task == "explain":
            result = explain_topic(text)
        elif task == "quiz":
            result = generate_quiz(text)
        elif task == "summarize":
            result = summarize_text(text)
        elif task == "learn":
            result = get_learning_recommendations(text)
        else:
            raise ValueError("Unknown task selected.")
    except Exception as exc:
        error = str(exc)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "result": result, "error": error, "selected_task": task, "input_text": text},
    )

@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}
