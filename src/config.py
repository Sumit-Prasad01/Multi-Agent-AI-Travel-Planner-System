import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    GROQ_API_KEY : str = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY : str = os.getenv("TAVILY_API_KEY")
    AVIATIONSTACK_API_KEY : str = os.getenv("AVIATIONSTACK_API_KEY")
    DATABASE_URL : str = os.getenv("DATABASE_URL")
    
    MODEL : str = "llama-3.3-70b-versatile"


settings = Settings()