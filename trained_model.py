# trained_model.py
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load your dataset
df = pd.read_csv(r"C:\Users\DELL\Downloads\student_study_habits.csv",encoding='latin1')  # replace with your actual dataset filename

df['pass_fail'] = (df['final_grade'] >= 50).astype(int)
# Independent and dependent features
X = df[['study_hours_per_week', 'sleep_hours_per_day', 'attendance_percentage', 'assignments_completed']]
y = df['pass_fail']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save trained model
with open("student_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as student_model.pkl")
