from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    content =  file.read()

    return { "filename": file.filename, "size": len(content) }
