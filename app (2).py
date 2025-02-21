
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDxq34Z3EtWUEA8uSfgOAigJgwOAQQ0yCc")

st.title("🚀An AI Code Reviewer🚀")

user_prompt= st.text_area("Enter your Python code here..")

if st.button("Generate Answer")== True:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest",
                         system_instruction= """"" You are a helpful AI Code Reviewer
                         Given a python code you are allowed to review and analyze the submitted code.
                         Provide feedback
                         Give the bug report and  errors and areas of improvement
                         Provide the fixed code snippets.
                         Explain the code corrections or suggestions. If the code  is not from the python
                         politely tell the user that you are a python code reviewer.""""")

if user_prompt:
    response= model.generate_content(user_prompt)

    st.write(response.text)
    st.markdown(response.text)
