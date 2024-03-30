import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import pickle

# Load CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# web app
st.title("Job Placement Prediction Model")

st.write('On entering the following Information, we will predict whether you will get placed or not')

# Inputs
name = st.text_input("Enter your name", "")
age = st.slider("Select your Age", 0, 100, 25)

gender_input = st.selectbox("Select your gender", ["Female", "Male"])
gender_M = 0 if gender_input == "Female" else 1

ssc_percentage = st.text_input("Enter your 10th Class Percentage", "")
SSC_board_input = st.selectbox("Select your SSC Board", ["Central", "Other"])
ssc_board_Others = 0 if SSC_board_input == "Central" else 1

hsc_percentage = st.text_input("Enter your 12th Class Percentage", "")
HSC_board_input = st.selectbox("Select your HSC Board", ["Central Board", "Other Board"])
hsc_board_Others = 0 if HSC_board_input == "Central Board" else 1

options = ['Computer Science', 'Electronics and Communication', 'Information Technology', 'Mechanical', 'Civil', 'Electrical']
selected_option = st.selectbox('Select your Branch of Study for Engineering', options)

degree_percentage = st.text_input("Enter your Engineering Percentage", "")
quant_prowess = st.slider("Rate your Quantitative Ability (1-100)", 1, 100, 25)
verbal_prowess = st.slider("Rate your Verbal Ability (1-100)", 1, 100, 25)
internships = st.text_input("Number of internships", "")
backlogs = st.text_input("Number of backlogs", "")
projects = st.text_input("Number of projects", "")
hackathons = st.text_input("Number of hackathons participated", "")
college_tier = st.selectbox("Select your College Tier", [1, 2, 3])

# Load model
with open('placement.pkl', 'rb') as f:
    model = pickle.load(f)

# Submit button
if st.button("Submit"):
    # Make prediction
    predictions = model.predict([[float(ssc_percentage), float(hsc_percentage), float(degree_percentage), float(quant_prowess), float(verbal_prowess), int(gender_M), int(ssc_board_Others), int(hsc_board_Others)]])
    result = "Congratulations! You will be placed!" if predictions == 1 else "Sorry, you will not be placed. Keep working harder!"

    # Display result
    st.markdown(f"<h2 style='text-align: center; color: {'green' if predictions == 1 else 'red'};'>{result}</h2>", unsafe_allow_html=True)
