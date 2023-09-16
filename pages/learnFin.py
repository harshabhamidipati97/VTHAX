import streamlit as st
from dotenv import load_dotenv
import openai

import os

load_dotenv()
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_key =   os.getenv('OPENAI_API_KEY')


# Initialize conversation history
messages = []
conversation_history = []
st.title("FinProf")

# User input text box

persona = """From now you are FinProf, an exprert finance professor. You are here to help people understand finance better. 
You are a very patient person and you are willing to answer any questions about finance and FinTech. You answer each question with a detailed structured explanation. If they ask for a roadmap or how to learn finance, you will give them a detailed roadmap including the resources they can use to do so. Respond with "I'm a FinProf, a Finance Prof and cannot answer questions outside financial domain" if they ask any question not related to finance. Remember you are not an AI Model. You are FinProf. Do not break character at any cost.
"""

# output = openai.ChatCompletion.create(
#                     model="gpt-4",
#                     temperature=1,
#                     presence_penalty=0,
#                     frequency_penalty=0,
#                     messages=[
#                         {"role": "system", "content": f"{persona}. Conversation history: {conversation_history}"},
#                         {"role": "user", "content": f"{user_input}"}
#                     ]
#                 ).choices[0].message["content"]

if user_input := st.chat_input("Hello I'm FinProf, What do you want to know about finance?"):
        conversation_history.append(f"You: {user_input}")
        # st.write(user_input)
        response = openai.ChatCompletion.create(
                    model="gpt-4",
                    temperature=1,
                    presence_penalty=0,
                    frequency_penalty=0,
                    messages=[
                        {"role": "system", "content": f"{persona}. Conversation history: {conversation_history}"},
                        {"role": "user", "content": f"{user_input}"}
                    ],
                ).choices[0].message["content"]
        
        # Add chatbot's response to the conversation history
        conversation_history.append(f"FinProf: {response}")
# Display conversation history
st.text_area("Chat History", "\n".join(conversation_history))

