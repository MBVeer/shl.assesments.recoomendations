import streamlit as st
from app.recommender import recommend_assessments
from bs4 import BeautifulSoup
import requests

# Title and input options
st.title("🔍 SHL Assessment Recommender")
input_type = st.radio("Select input type", ("Text Query", "Job Description URL"))

user_input = ""
if input_type == "Text Query":
    user_input = st.text_area("Enter your job description or query:")
elif input_type == "Job Description URL":
    job_url = st.text_input("Paste the job description URL here:")
    if job_url:
        try:
            response = requests.get(job_url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            user_input = soup.get_text()
        except requests.exceptions.RequestException as e:
            st.error(f"Could not retrieve job description: {e}")

# Process the input
if st.button("Done"):
    if user_input.strip():  # Avoid empty input
        try:
            results = recommend_assessments(user_input)
            if results is not None and not results.empty:
                st.success("Recommendations:")
                st.dataframe(results)
            else:
                st.warning("No relevant assessments found.")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter or retrieve a valid job description.")
