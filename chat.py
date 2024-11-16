import json
import requests
import random
import warnings
import os
import pickle
import numpy as np
from tensorflow import keras
from colorama import Fore, Style

warnings.filterwarnings("ignore")

# Set up your API key directly here (use environment variables for better security in production)
api_key = ''

# Load the intents file
with open('intents.json') as file:
    data = json.load(file)

# Call Gemini API for a response
def get_gemini_response(user_input):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": user_input}]}]
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        if 'candidates' in response_data:
            return response_data['candidates'][0]['content']['parts'][0]['text']
        else:
            return None
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None

# Define chat function to interact with user
def chat():
    # Load trained model
    model = keras.models.load_model('chat-model.keras')

    # Load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # Load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # Parameters for text processing
    max_len = 20

    while True:
        print(Fore.LIGHTBLUE_EX + 'User: ' + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == 'quit':
            print(Fore.GREEN + 'EIMTCA:' + Style.RESET_ALL, "Take care. See you soon.")
            break

        # Check for specific question "Who made you?"
        if inp.lower() == "who made you":
            print(Fore.GREEN + 'EIMTCA:' + Style.RESET_ALL, "I was developed by a joint effort of Gatik and Rishit.")
            continue  # Skip to the next iteration, no need to call Gemini or model prediction

        # Predict tag using the trained model
        result = model.predict(keras.preprocessing.sequence.pad_sequences(
            tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        # Call Gemini API for response generation based on user input
        gemini_response = get_gemini_response(inp)

        # Output the response from Gemini API, or a fallback message if it fails
        if gemini_response:
            print(Fore.GREEN + 'EIMTCA:' + Style.RESET_ALL, gemini_response)
        else:
            print(Fore.GREEN + 'EIMTCA:' + Style.RESET_ALL, "I'm here to listen if you want to share more.")

# Start chatting with EIMTCA
print(Fore.YELLOW + 'Start talking with EIMTCA, your Personal Therapeutic AI Assistant. (Type quit to stop talking)' + Style.RESET_ALL)
chat()
