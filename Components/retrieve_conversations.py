import json
from sqlalchemy.orm import Session
from models import Conversation, SessionLocal

def retrieve_conversations(sender=None):
    # Create a new session
    db = SessionLocal()

    if sender:
        # Query the Conversation table for a specific phone number
        conversations = db.query(Conversation).filter_by(sender=sender).all()
    else:
        # Query the Conversation table for all conversations
        conversations = db.query(Conversation).all()

        # Format the results as a list of dictionaries
    conversation_list = [{
        'id': conversation.id,
        'sender': conversation.sender,
        'message': conversation.message,
        'response': conversation.response
    } for conversation in conversations]

    # Close the session
    db.close()

     # Convert the list of dictionaries to a JSON string
    return json.dumps(conversation_list, indent=4)

if __name__ == "__main__":
    # Example usage: retrieve conversations for a specific phone number
    sender = "+393408835717"
    retrieve_conversations(sender)
    conversations_json = retrieve_conversations(sender)
    print(conversations_json)