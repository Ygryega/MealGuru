from sqlalchemy.orm import Session
from models import Conversation, SessionLocal

def retrieve_conversations():
    # Create a new session
    db = SessionLocal()

    # Query the Conversation table
    conversations = db.query(Conversation).all()

    # Iterate over the results
    for conversation in conversations:
        print(f"ID: {conversation.id}, Sender: {conversation.sender}, Message: {conversation.message}, Response: {conversation.response}")

    # Close the session
    db.close()

if __name__ == "__main__":
    retrieve_conversations()