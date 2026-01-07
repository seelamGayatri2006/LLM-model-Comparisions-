from openai import OpenAI
import streamlit as st

def chatgpt_response(prompt: str) -> str:
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
    except KeyError:
        return "OPENAI_API_KEY not found in Streamlit Secrets"

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
