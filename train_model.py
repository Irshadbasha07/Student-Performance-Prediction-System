import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load data
try:
    df = pd.read_csv('student_data.csv')
except FileNotFoundError:
    print("Error: student_data.csv not found.")
    exit()

# Preprocessing
# 1. Map Categorical Variables
# ParentalEducation: None-0, Primary-1, Secondary-2, Higher-3
edu_map = {'None': 0, 'Primary': 1, 'Secondary': 2, 'Higher': 3}
df['parentalEducation'] = df['parentalEducation'].map(edu_map)

# InternetAccess: No-0, Yes-1
net_map = {'No': 0, 'Yes': 1}
df['InternetAccess'] = df['InternetAccess'].map(net_map)

# Select features
features = ['parentalEducation', 'AttendancePercentage', 'PreviousYearPercentage', 'StudyHoursPerWeek', 'InternetAccess']
target = 'PresentPercentage'

X = df[features]
y = df[target]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Trained Successfully.")
print(f"MAE: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# Save Model
joblib.dump(model, 'student_performance_model.pkl')
print("Model saved to student_performance_model.pkl")
