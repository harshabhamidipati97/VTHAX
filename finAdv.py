import streamlit as st

from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_key =   os.getenv('OPENAI_API_KEY')

st.header('Know Your Fin')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def converse(prompt, messages=None, model="gpt-3.5-turbo", max_tokens=2500, temperature=0, top_p=1, frequency_penalty=0,
            presence_penalty=0):
    # Add the user's message to the list of messages
    if messages is None:
        messages = []

    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    ).choices[0].message["content"]

    # Add the assistant's message to the list of messages
    messages.append({"role": "assistant", "content": response})

    return response, messages


input_text = st.text_area('Enter your text here')
messages = []
prompt = input_text
response, messages = converse(prompt,messages)
st.write(response)
