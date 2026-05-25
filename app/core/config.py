import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY")

APP_NAME = os.getenv("APP_NAME", "FeedbackSDK")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

TEST_API_KEY = os.getenv("TEST_API_KEY")

USE_TEST_MODE = os.getenv("USE_TEST_MODE") == "true"