import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query("Can you please let us know more details about your ")
print(output)

st.title('Text Generation app')
input=st.text_area('Please enter your text')

if st.button('Generate'):
    result=query(input)
    st.subheader('Your Generated Text')
    st.write(result[0]['generated_text'])