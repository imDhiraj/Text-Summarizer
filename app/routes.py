from fastapi import APIRouter
from pydantic import BaseModel
from app.summarizer import summarize_text
from fastapi import UploadFile, File
from PyPDF2 import PdfReader  # for PDF handling
from app.summarizer import summarize_text
from fastapi import APIRouter, UploadFile, File
from app.summarizer import summarize_text

router = APIRouter()

class SummaryRequest(BaseModel):
    text: str

@router.post("/upload-summary")
async def upload_summary(file: UploadFile = File(...)):
    contents = await file.read()

    if file.filename.endswith(".txt"):
        text = contents.decode("utf-8")
    elif file.filename.endswith(".pdf"):
        pdf = PdfReader(file.file)
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    else:
        return {"error": "Unsupported file format. Use .txt or .pdf"}

    summary = summarize_text(text)
    return {"summary": summary}

@router.post("/summarize")
def summarize(request: SummaryRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}
