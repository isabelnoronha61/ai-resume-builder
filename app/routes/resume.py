from fastapi import APIRouter, UploadFile, File
from app.services.parser import extract_text_from_pdf

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    content =  await file.read()

    extracted_text = extract_text_from_pdf(content)

    return {
        "filename": file.filename,
        "text_preview": extracted_text[:500]  
    }