# AI JobShield: Fake Job Posting Detector

_A step by step guide to install, run, and understand AI JobShield, a Streamlit web app that uses machine learning to spot scam job ads._

---

## Overview

**AI JobShield** helps you tell real job postings from fraudulent ones by analyzing the text of any job advertisement. Behind the scenes, it uses:

- Natural Language Processing (NLP) to turn words into numbers.
- TF-IDF vectorization to highlight terms that matter.
- A Logistic Regression classifier to decide “Real” vs “Fake.”

All of this is wrapped in a Streamlit web interface so you can paste in a job description, click **Predict**, and get an instant verdict.

---
## Key Features

1. One-click prediction: Paste job text, hit Predict.
2. Color-coded output:  
   - Green = Likely Real  
   - Red = Likely Fake  
3. Confidence score: See how sure the model is.
4. Optional retraining: Jupyter notebook included for anyone wanting to make an update on it.

---

## Who Is This For?

- Job Seekers who want a quick sanity check on a posting.
- Recruiters & Moderators who need to triage listings.
- Developers & Students learning how to deploy NLP models as web apps.

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.8+ installed  
- A code editor or IDE (I recommend PyCharm )
- A terminal or command prompt  
- Internet access to download the dataset from Kaggle
