import google.generativeai as genai
from src.app.core.config import settings

if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)


def get_gemini_client():
    """
    Returns configured GenerativeModel or helper.
    """
    # Use standard gemini-1.5-flash as default model
    return genai.GenerativeModel('gemini-1.5-flash')
