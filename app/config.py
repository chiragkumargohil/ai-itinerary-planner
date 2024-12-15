import os

class Config:
  LANGCHAIN_ENDPOINT = os.environ.get("LANGCHAIN_ENDPOINT")
  LANGCHAIN_API_KEY = os.environ.get("LANGCHAIN_API_KEY")
  LANGCHAIN_API_SECRET = os.environ.get("LANGCHAIN_PROJECT")
  GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")