import streamlit as st
import joblib

#load the trained model pipeline
model = joblib.load('models/job_posting_model.pkl')

#set up the app title and description
st.title("AI JobShield – Job Posting Legitimacy Checker")
st.write("""
**AI JobShield** uses a machine learning model to detect fake job postings.
Enter the details of a job advertisement below, and click **Predict** to check if it's real or a scam.
""")

#text input for the job posting content
job_text = st.text_area("Job Posting Content:",
                        "Paste the job description and details here...")
#predict button
if st.button("Predict"):
    if job_text.strip() == "":
        st.warning("Please enter the job posting details in the text area above.")
    else:
        #use the model to predict (the model expects an array-like input of texts)
        prediction = model.predict([job_text])[0]  # 0 for real, 1 for fake
        prediction_proba = model.predict_proba([job_text])[0]  # probability for [Real, Fake]
        fake_prob = prediction_proba[1]

        #display results
        if prediction == 1:
            st.error(f"**Warning:** This job posting appears to be **FAKE** (fraudulent).")
            st.write(f"Model confidence that this is fake: **{fake_prob * 100:.1f}%**")
        else:
            st.success("This job posting is likely **Legitimate** (real).")
            st.write(f"Model confidence that this is real: **{(1 - fake_prob) * 100:.1f}%**")
