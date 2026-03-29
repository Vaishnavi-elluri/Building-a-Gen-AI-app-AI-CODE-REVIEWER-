
import streamlit as st
import google.generativeai as genai
import os
import time
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("🚀An AI Code Reviewer🚀")

user_prompt= st.text_area("Enter your Python code here..")

if st.button("Generate Answer"):
    model = genai.GenerativeModel(
        model_name="models/gemini-2.0-flash",
        system_instruction="""You are a helpful AI Code Reviewer.
Given a python code you are allowed to review and analyze the submitted code.
Provide feedback.
Give bug report, errors, and areas of improvement.
Provide fixed code snippets.
Explain the corrections.
If the code is not Python, politely say you are a Python code reviewer."""
    )

    if user_prompt:
          with st.spinner("Generating response..."):
                try:
                    start = time.time()
                    response = model.generate_content(user_prompt)
                    end = time.time()
            
                    st.write(f"Response time: {round(end - start, 2)} seconds")
                    st.write(response.text)
            
                except Exception as e:
                    st.error(f"Error: {e}")
            
