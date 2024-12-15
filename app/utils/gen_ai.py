from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from app.utils.prompts import system_message, human_message
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# create the model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

def generate_response(user_preferences: dict):
  # create messages
  messages = [
    ("system", system_message),
    ("human", human_message)]

  # create prompt
  prompt_template = ChatPromptTemplate.from_messages(messages)

  # fill in the template
  ai_prompt = prompt_template.invoke(user_preferences)

  # invoke the model
  result = llm.invoke(ai_prompt)

  # return json response
  return result.content