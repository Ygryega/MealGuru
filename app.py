import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    # Get the message the user sent
    incoming_msg = request.values.get('Body', '').lower()
    
    # Create a Twilio response object
    resp = MessagingResponse()
    msg = resp.message()
    
    # Your AI chatbot logic here
    if 'hello' in incoming_msg:
        response = 'Hi there! How can I help you today?'
    else:
        response = 'I am an AI chatbot. How can I assist you?'
    
    # Send the response back to the user
    msg.body(response)
    return str(resp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)