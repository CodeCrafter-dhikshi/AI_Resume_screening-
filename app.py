import streamlit as st

st.title("AI Resume Screening Tool")
st.write("Upload a job description and candidate resumes to rank them based on relevance.")

import streamlit as st
import fitz  # PyMuPDF
import os

st.title("AI Resume Screening Tool")
st.write("Upload a job description and candidate resumes to rank them based on relevance.")

# File uploader for Job Description
job_desc_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

# File uploader for multiple resumes
resume_files = st.file_uploader("Upload Resumes (PDFs)", type=["pdf"], accept_multiple_files=True)

# Function to extract text from PDF using fitz (PyMuPDF)
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

if job_desc_file and resume_files:
    st.subheader("Extracted Texts")
    
    # Extract job description text
    job_desc_text = extract_text_from_pdf(job_desc_file)
    st.write("📄 **Job Description Text:**")
    st.write(job_desc_text)

    # Extract each resume text
    for resume in resume_files:
        resume_text = extract_text_from_pdf(resume)
        st.write(f"📄 **Resume: {resume.name}**")
        st.write(resume_text)

import streamlit as st
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Screening Tool")
st.write("Upload a job description and candidate resumes to rank them based on relevance.")

# Upload Job Description
job_desc_file = st.file_uploader("📄 Upload Job Description (PDF)", type=["pdf"], key="jobdesc")


# Upload Resumes
resume_files = st.file_uploader("📄 Upload Resumes (PDFs)", type=["pdf"], accept_multiple_files=True, key="resumes")


# Function to extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Matching function using TF-IDF and Cosine Similarity
def match_score(jd_text, resume_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([jd_text, resume_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)  # Convert to percentage

# Run only if files are uploaded
if job_desc_file and resume_files:
    jd_text = extract_text_from_pdf(job_desc_file)
    st.subheader("📝 Matching Results")

    for resume in resume_files:
        resume_text = extract_text_from_pdf(resume)
        score = match_score(jd_text, resume_text)
        st.write(f"📄 **{resume.name}** - Match Score: **{score}%**")


import streamlit as st
import fitz  # PyMuPDF
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords if not already
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

st.title("💼 AI Resume Screening Tool")
st.write("Upload a job description and candidate resumes to rank them by relevance.")

# Upload Job Description
job_desc_file = st.file_uploader("📄 Upload Job Description (PDF)", type=["pdf"])
# Upload Resumes
resume_files = st.file_uploader("📄 Upload Resume(s) (PDF)", type=["pdf"], accept_multiple_files=True)

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Clean the text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)  # Remove special characters
    words = [word for word in text.split() if word not in stop_words]
    return ' '.j
