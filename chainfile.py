import os
import google.generativeai as genai
import streamlit as st

st.title('Text Summarization + Sentiment Analysis by Akshat')

os.environ['GOOGLE_API_KEY'] = "AIzaSyBl31kKtxz3e4mIpm9oTqfRi3gcth3I-1g"  
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter Your Content")
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-001")

if st.button('Summary'):
    # Step 1: Summarize content
    prompt1 = f"""
    You are an expert linguist who is good at summarizing content.
    Please summarize the following content into 2 lines:
    ```
    {user_input}
    ```
    """
    response1 = model.generate_content(prompt1)
    summary = response1.text.strip() if response1.text else "Summary not available."
    
    # Step 2: Analyze sentiment
    prompt2 = f"""
    Analyze the sentiment of the following text as either Positive or Negative.
    ```
    {summary}
    ```
    """
    try:
        response2 = model.generate_content(prompt2)
        sentiment = response2.text.strip() if response2.text else "Sentiment not available."
    except Exception as e:
        sentiment = f"Error analyzing sentiment: {str(e)}"

    # Display results
    st.success(f"Summary: {summary}")
    st.success(f"Sentiment: {sentiment}")
