# Third-party imports
import json
import openai
import re
from fastapi import FastAPI, Form, Depends
from decouple import config
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

# Internal imports
import response_model
from models import Conversation, SessionLocal
from utils import send_message, logger

app = FastAPI()
# Set up the OpenAI API client
openai.api_key = config("OPENAI_API_KEY")
whatsapp_number = config("TO_NUMBER")

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Function to read JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def extract_phone_number(whatsapp_string):
    match = re.search(r'#whatsapp:(\+\d+)', whatsapp_string)
    if match:
        return match.group(1)
    return None

def get_information_from_chatgpt(question_string, json_reference):

    # Convert the JSON reference to a string
    json_reference_str = json.dumps(json_reference, indent=2)

    question_str = response_model.format_beggning + json_reference_str + response_model.format_greeting + response_model.format_order +response_model.format_ending+ "The following is the question made by the user" + question_string

    stream = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question_str}],
        stream=True,
    )

     # Initialize an empty string to accumulate the response
    response = ""
    
    # Iterate through the streamed chunks and concatenate the content to the response string
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
    
    # Return the accumulated response
    return response

@app.post("/webook")
async def reply(Body: str = Form(), From: str = Form(), db: Session = Depends(get_db)):
    logger.info(f"The sender number #{From.replace("whatsapp:", "")} ")
        # Read the JSON reference from the file
    json_reference = read_json_file('Components/test_menu.json')

    # The generated text
    chat_response = get_information_from_chatgpt(Body, json_reference)

    # Store the conversation in the database
    try:
        conversation = Conversation(
            sender=From,
            message=Body,
            response=chat_response
            )
        db.add(conversation)
        db.commit()
        logger.info(f"Conversation #{conversation.id} stored in database")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error storing conversation in database: {e}")
    send_message(From.replace("whatsapp:", ""), chat_response)
    return ""