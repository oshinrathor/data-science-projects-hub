# Applicant Tracking System Resume Analyzer

## OVERVIEW
This is a Streamlit-based ATS (Applicant Tracking System) Resume Analyzer that leverages Google Gemini LLM to analyze resumes against a provided job description. The application provides professional resume insights, match percentages, and actionable suggestions for improvement in a structured and easy-to-read format.

---

## FEATURES
1. **Resume Upload:** Users can upload resumes in PDF format.  
2. **Job Description Input:** Users provide the job description to compare with the resume.  
3. **Resume Analysis:** The system extracts technical skills, soft skills, education, work experience, and projects from the resume.  
4. **Match Evaluation:** Compares the uploaded resume against the job description and calculates a match percentage.  
5. **Recommendations:** Highlights missing skills or keywords and provides suggestions to optimize the resume for ATS.  
6. **Visual Output:** The results are displayed in a clean, well-structured, and easy-to-understand format.  

---

## SCREENSHOTS
The following images illustrate the app's interface and output:

<p float="left">
  <img src="Applicant Tracking System Resume Analyzer/Screenshot 10.png" width="300" />
  <img src="Applicant Tracking System Resume Analyzer/Screenshot 11.png" width="300" />
</p>

<p float="left">
  <img src="Applicant Tracking System Resume Analyzer/Screenshot 12.png" width="300" />
  <img src="Applicant Tracking System Resume Analyzer/Screenshot 13.png" width="300" />
</p>

---

## STEP-BY-STEP DOCUMENTATION

### 1. Environment Setup
The application uses environment variables stored in a `.env` file, including the Google API key. This allows secure access to the Google Gemini API without exposing sensitive credentials in the code.

---

### 2. Import Required Libraries
The system uses several libraries for different purposes:  
- **Streamlit:** For creating the web interface.  
- **OS:** To interact with environment variables and system files.  
- **Pillow (PIL):** To process images extracted from PDFs.  
- **pdf2image:** To convert PDF pages into images.  
- **Google Gemini AI client:** To send the resume and job description for AI-based analysis.  
- **io and base64:** For handling image data in memory and encoding it in a format suitable for the AI model.  

---

### 3. Configure Google Gemini API
The AI model is configured using the Google API key. This setup allows the application to send prompts and content to the Gemini LLM and receive structured responses.  

---

### 4. Resume Analysis Function
A dedicated function sends the resume content, job description, and prompts to the AI model. The AI then returns a professional analysis of the resume, including technical skills, soft skills, education, experience, and projects.  

---

### 5. PDF Processing Function
The uploaded PDF resume is converted into images (one per page), and only the first page is used for analysis. The image is processed and encoded into a format suitable for the AI model. This ensures that the resume content can be effectively read and interpreted.  

---

### 6. Streamlit App Interface
The interface provides:  
- A text area for entering the job description.  
- A file uploader to upload PDF resumes.  
- Feedback when the PDF is successfully uploaded.  

---

### 7. User Actions
Users interact with the app via two main buttons:  
- **Tell Me About The Resume:** Triggers a detailed resume analysis by the AI, highlighting skills, education, experience, and projects.  
- **Percentage Match With Job Description:** Triggers a match evaluation, providing a match score and suggestions for improvement.  

---

### 8. Prompts for AI Analysis
Strict prompts guide the AI model to:  
- Extract only information explicitly mentioned in the resume.  
- Provide professional comparisons between the resume and the job description.  
- Highlight strengths, weaknesses, and match levels.  
- Identify missing skills or keywords and suggest actionable improvements to increase ATS compatibility.  

---

### 9. Handling User Actions
The app dynamically responds based on the button clicked:  
- **Resume Analysis:** Sends the resume and job description to the AI for detailed insights.  
- **Match Percentage:** Sends the resume and job description to the AI to calculate match percentage and provide improvement suggestions.  
- Users are prompted to upload a resume if they attempt actions without uploading a file.  

---

## NOTES
- Only the first page of the uploaded PDF is analyzed.  
- Poppler must be installed and the correct path provided for PDF-to-image conversion.  
- The application focuses on technical roles such as Data Analytics, Data Science, Machine Learning, AI, Web Development, Software Engineering, Cloud Computing, and DevOps.  

---

## ACKNOWLEDGMENTS
- [Streamlit](https://streamlit.io/) for building the web interface.  
- [Google Gemini AI](https://developers.generativeai.google/) for resume analysis.  
- [pdf2image](https://pypi.org/project/pdf2image/) for PDF to image conversion.  


