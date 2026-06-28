from fastapi import APIRouter, Depends, UploadFile, File, Form
from src.app.core.security import get_current_user
from src.app.ai.integrations.gemini import get_gemini_client

router = APIRouter()


@router.post("/generate-cover-letter")
async def generate_cover_letter(
    job_description: str = Form(...),
    resume_text: str = Form(...),
    current_user: dict = Depends(get_current_user)
):
    """
    Generates a personalized cover letter using Gemini AI model.
    """
    model = get_gemini_client()
    prompt = (
        f"Write a highly professional cover letter tailored for this job description:\n"
        f"{job_description}\n\nUsing this resume details:\n{resume_text}"
    )
    response = model.generate_content(prompt)
    return {"cover_letter": response.text}
