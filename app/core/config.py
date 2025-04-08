import os
from dotenv import load_dotenv

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key_for_safety") 
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")