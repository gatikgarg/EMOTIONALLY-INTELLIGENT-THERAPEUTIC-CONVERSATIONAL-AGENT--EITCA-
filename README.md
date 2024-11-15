### Detailed Description of the EIMTCA Project

The **Emotionally Intelligent Multi-Modal Therapeutic Conversational Agent (EIMTCA)** was developed to provide personalized mental health support through a conversational AI platform. The project integrates various technologies like deep learning, NLP, and emotion recognition to offer a more empathetic and effective user experience, especially for mental health concerns.

#### Development Process:
1. **Project Planning & Design:**
   - The project started with designing a user-friendly conversational flow aimed at providing mental health support. I researched existing mental health chatbots and therapies like **Cognitive Behavioral Therapy (CBT)**, to ensure the chatbot would offer scientifically backed suggestions.
   - The overall architecture of the system was designed to handle both text and speech inputs for diverse user needs, integrating **emotion recognition** to gauge the emotional state of the user.

2. **Data Collection & Preprocessing:**
   - A custom dataset was collected to train the NLP models, and user conversations were analyzed to build conversational intent models.
   - Text preprocessing techniques, such as tokenization, lemmatization, and intent classification, were applied using **TensorFlow**, **Keras**, and **NLTK** for better understanding and handling of user inputs.

3. **Model Training:**
   - I developed a **deep learning-based classification model** using **Keras** to classify user intents and generate meaningful responses. This model was trained using a variety of text-based data.
   - The **tokenizer** was created and integrated to process user input and convert it into sequences of tokens that could be fed into the neural network for classification.

4. **Emotion Recognition Integration:**
   - **Emotion recognition** was integrated into the system using machine learning techniques, which analyzed the user's text and voice inputs to detect emotions like anxiety, sadness, or stress. This helped tailor responses empathetically, aligning with psychological principles of active listening and emotional validation.

5. **API Integration:**
   - For advanced conversational capabilities, I integrated the **Gemini AI API** for generating natural language responses to user queries. This allows for dynamic responses that are contextually aware and conversationally relevant.

6. **Deployment:**
   - The final model was deployed as a **command-line chatbot** where users can interact in real-time. The system continuously learns and adapts to better meet the emotional and informational needs of users.

#### Technologies Used:
- **Deep Learning Frameworks**: **Keras**, **TensorFlow** for model development and training.
- **NLP**: **NLTK**, **TensorFlow** for preprocessing text and training models.
- **Emotion Recognition**: Integrated emotion detection using both text and voice inputs.
- **Gemini API**: For advanced response generation.
- **Model Deployment**: The chatbot is deployed via a simple command-line interface.

EIMTCA is designed to provide scalable, empathetic support, making use of the latest AI and machine learning techniques to cater to individuals seeking mental health guidance.

# HOW TO RUN THIS REPOSITORY?
First, clone this repository. 
Create a virtual environment using:
```
python -m venv <environment name>
```
Activate the virtual environment and then install the necessary libraries using:
```
pip install -r requirements.txt
```
Train the model using:
```
python model.py
```
Now run Pandora using:
```
python chat.py
```

You can modify Pandora by inserting your own text in the `intents.json` file.

# A CONVERSATION WITH EIMTCA
![EITCA WORKING](https://github.com/user-attachments/assets/378743fc-65e6-4fd5-8de7-ba2122c4b0fd)
![EITCA WORKING 2](https://github.com/user-attachments/assets/f534b2ef-ed51-444c-adee-765611f98d8f)





# AREAS OF IMPROVEMENT / CONTRIBUTION FOR FUTURE WORK
- [ ] Upgrade to a More Advanced LLM: Use models like GPT-3 or GPT-4 for more accurate, context-aware responses.
- [ ] Improve Intent Classification: Enhance intent detection with models like BERT or RoBERTa for better contextual understanding.
- [ ] Add Voice Interaction: Implement Text-to-Speech (TTS) and Speech-to-Text (STT) for a more natural, accessible user experience.
- [ ] Facial Recognition for Emotion Detection: Integrate facial recognition to detect emotions from users' faces, providing more personalized responses.
- [ ] Expand the Dataset: Include diverse user interactions to improve the chatbot’s ability to handle different scenarios.
- [ ] Enhance Security: Implement encryption and secure authentication to protect user data.
- [ ] Web Application Deployment: Shift to a web-based platform for easier access and a more intuitive interface.






 


