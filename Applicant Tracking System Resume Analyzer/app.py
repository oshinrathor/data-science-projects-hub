from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-2.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the pdf to image
        images=pdf2image.convert_from_bytes(uploaded_file.read(),
            poppler_path=r"C:\Users\hp\OneDrive\Desktop\Professional\Machine Learning\ATS\Release-25.11.0-0\poppler-25.11.0\Library\bin")
        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
## Streamlit App

st.set_page_config(page_title="ATS Resume Expert", layout="wide")
st.header("Applicant Tracking System")
input_text=st.text_area("Job Description", key="input", height=200)
uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About The Resume")
# submit2 = st.button("How Can I Improvise my Skills?")
# submit3 = st.button("What Keywords Should I Add To Get Selected?")
submit2 = st.button("Percentage Match With Job Description")


input_prompt1 = """
You are an experienced Technical HR Manager in the field of Data Analytics, Business Intelligence, Data Science, Data Engineering, Data Visualization, Machine Learning, Artificial Intelligence, Web Development, Full Stack Development, Software Engineering, Cloud Computing, DevOps.
Extract technical skills, soft skills, education details, and experience/project information directly from the resume. Only include information explicitly stated in the resume for each category.
Given a resume and a job description, provide a professional and accurate comparison between them, highlighting the technical skill stack and illustrating the match. Use cues to represent high, medium, and low match areas, highlighting strengths and weaknesses.
"""



input_prompt2 = """
You are a highly skilled ATS (Applicant Tracking System) specialist tasked solely with analyzing and optimizing resumes for technical roles in the following domains, in this exact order: Data Analytics, Business Intelligence, Data Science, Data Engineering, Data Visualization, Machine Learning, Artificial Intelligence, Web Development, Full Stack Development, Software Engineering, Cloud Computing, DevOps, and you will not perform any other task or provide any unrelated information.
Prioritize based on frequency and relevance to the job. Give me the percentage match between the resume and the job description, considering relevant skills, experience, and keywords. First the output should be a single percentage number followed by keywords that are missing in the resume to improve the match.
Provide suggestions for integrating these keywords into the resume, emphasizing achievements and quantifiable results.
Your task is to analyze the provided resume against the job description for these roles. 
"""



if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text   )
        st.subheader("ATS Expert Analysis:")
        st.write(response)
    else:
        st.write("Please upload a PDF resume to proceed.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("Resume Match Percentage and Suggestions:")
        st.write(response)
    else:
        st.write("Please upload a PDF resume to proceed.")