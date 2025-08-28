🎓 Student Performance Prediction

App link:https://randomforest-naivebayes-cnebgz2gifmsxgvkzubtuq.streamlit.app/


This project predicts whether a student will Pass ✅ or Fail ❌ using machine learning models (Random Forest and Naïve Bayes).


The prediction is based on four features:

📘 Study hours per week

😴 Sleep hours per day

🏫 Attendance percentage

📝 Assignments completed


📂 Project Files

app.py → Streamlit frontend for user input and prediction

trained_model.py → Script to train and save the ML model

student_model.pkl → Pre-trained model file

Random_forest & Naive_bayes.ipynb → Jupyter notebook (experiments)



🚀 How to Run Locally

1.Clone the repository

git clone https://github.com/USERNAME/Random_forest-Naive_bayes.git
cd Random_forest-Naive_bayes



2.Install dependencies

pip install -r requirements.txt


3.Run the app

requirements.txt → List of Python dependencies
streamlit run app.py


4.Open the local URL provided by Streamlit (usually http://localhost:8501)


🌐 Deployment on Streamlit Cloud

Push all files (including student_model.pkl) to GitHub.

Go to Streamlit Cloud
 and connect your repo.

Set the entry point as app.py.

The app will be live and sharable with anyone! 🎉



🖼️ App Preview

Enter your study hours, sleep hours, attendance, and assignments completed.

Click Predict → The model tells you if the student will Pass ✅ or Fail ❌.


📌 Requirements

Python 3.8+

scikit-learn

pandas

numpy

streamlit

(Already listed in requirements.txt)


Screenshot for app:


<img width="931" height="769" alt="Screenshot 2025-08-28 204721" src="https://github.com/user-attachments/assets/ccf4e28f-b01c-414a-ba90-6c366c1e9247" />
