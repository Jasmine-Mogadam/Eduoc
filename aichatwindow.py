import pdf_or_text_chat
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__, template_folder='templates')

# Simple in-memory store for messages
messages = []

def concatenate_messages(messages):
    return_val = ' '.join(messages)
    return return_val

@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/send', methods=['POST'])
def send():
    message = request.json.get('message')
    messages.append(f'You: {message}')
    return jsonify({"status": "success", "response": "Your message was received!"})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})

if __name__ == "__main__":
    app.run(debug=True)
#read documentation, put it on top of mind before coding

"""
def load_pdf() 


def LLM_API_CALL() 
    
#vector search fails when not enough information concerning query
#need to handle validation check to handle fail cases
#also rejection case by USEr to flush out bad responses or queries

def chat_interface()

def chat_history()

def reroute_info_to_doc()
    #toggle what messages user wants doctor to see
    #reroutes information


#options to consider
    #1. overhead tracking of consent, multilevel consent on metadata to certain data
    #2. info passed through chatpgt that has metadata consent or clearance levels needs to perserve it accross information exchange
    #constitutional ai

"""
