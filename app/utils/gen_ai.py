from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from app.utils.prompts import llm_system_message, llm_human_message
from dotenv import load_dotenv
import json

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

def generate_response(user_preferences: dict) -> dict:
  # create messages
  messages = [
    ("system", llm_system_message),
    ("human", llm_human_message)]

  # create prompt
  prompt_template = ChatPromptTemplate.from_messages(messages)

  # fill in the template
  ai_prompt = prompt_template.invoke(user_preferences)

  # invoke the model
  result = llm.invoke(ai_prompt)

  # clean response
  # remove ```json from beginning and ``` from end
  cleaned_response = result.content.strip("```json\n").strip("```")

  try:
    return json.loads(cleaned_response)
  except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)
    return None