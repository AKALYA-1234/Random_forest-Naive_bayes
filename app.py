# app.py
import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Performance Predictor")
st.write("Enter student details to predict if they will **Pass or Fail**")

# Input fields
study_hours = st.number_input("Study Hours per Week", min_value=0.0, max_value=100.0, step=1.0)
sleep_hours = st.number_input("Sleep Hours per Day", min_value=0.0, max_value=24.0, step=0.5)
attendance = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0, step=1.0)
assignments = st.number_input("Assignments Completed", min_value=0, max_value=50, step=1)

# Predict button
if st.button("Predict"):
    features = np.array([[study_hours, sleep_hours, attendance, assignments]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ The student is likely to PASS")
    else:
        st.error("❌ The student is likely to FAIL")
