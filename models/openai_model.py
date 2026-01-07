import streamlit as st
from openai import OpenAI

def chatgpt_response(prompt: str) -> str:
    api_key = st.secrets["OPENAI_API_KEY"]
    
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
