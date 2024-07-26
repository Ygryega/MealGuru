# Third-party imports
import openai
from fastapi import FastAPI, Form, Depends
from decouple import config
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

# Internal imports
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

def get_information_from_chatgpt(web_content):
    stream = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": web_content}],
        stream=True,
    )
     # Initialize an empty string to accumulate the response
    response = ""
    
    # Iterate through the streamed chunks and concatenate the content to the response string
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
    
    # Return the accumulated response
    return response

@app.post("/message")
async def reply(Body: str = Form(), db: Session = Depends(get_db)):
    # The generated text
    chat_response = get_information_from_chatgpt(Body)

    # Store the conversation in the database
    try:
        conversation = Conversation(
            sender=whatsapp_number,
            message=Body,
            response=chat_response
            )
        db.add(conversation)
        db.commit()
        logger.info(f"Conversation #{conversation.id} stored in database")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error storing conversation in database: {e}")
    send_message(whatsapp_number, chat_response)
    return ""