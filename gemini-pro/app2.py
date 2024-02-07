import google.generativeai as genai
import streamlit as st

genai.configure(api_key='Hidden_API') #I have hidden this key fro security reason
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Question and Answer")
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key='input')
submit=st.button("Ask the question")
if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)