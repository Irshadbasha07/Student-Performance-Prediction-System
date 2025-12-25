import pandas as pd
import numpy as np

# Set random seed
np.random.seed(42)

# Config
n_samples = 1000

# Synthetic Data
data = {
    'studentId': np.arange(1001, 1001 + n_samples),
    'Gender': np.random.choice(['Male', 'Female'], n_samples),
    'parentalEducation': np.random.choice(['None', 'Primary', 'Secondary', 'Higher'], n_samples, p=[0.1, 0.3, 0.4, 0.2]),
    'AttendancePercentage': np.random.normal(80, 10, n_samples).clip(0, 100).round(1),
    'PreviousYearPercentage': np.random.normal(70, 15, n_samples).clip(0, 100).round(1),
    'StudyHoursPerWeek': np.random.randint(1, 20, n_samples),
    'InternetAccess': np.random.choice(['No', 'Yes'], n_samples, p=[0.3, 0.7])
}

df = pd.DataFrame(data)

# Logic to calculate PresentPercentage based on inputs + noise
def calculate_present_percentage(row):
    # Base score
    score = 40
    
    # Impact of Attendance (Strong correlation)
    score += (row['AttendancePercentage'] * 0.4)
    
    # Impact of Previous Year (Medium correlation)
    score += (row['PreviousYearPercentage'] * 0.15)
    
    # Impact of Parental Education
    edu_map = {'None': 0, 'Primary': 2, 'Secondary': 5, 'Higher': 8}
    score += edu_map[row['parentalEducation']]
    
    # Impact of Study Hours
    score += (row['StudyHoursPerWeek'] * 0.5)
    
    # Impact of Internet
    if row['InternetAccess'] == 'Yes':
        score += 2
        
    # Random noise
    noise = np.random.normal(0, 3)
    score += noise
    
    return min(max(score, 0), 100)

df['PresentPercentage'] = df.apply(calculate_present_percentage, axis=1).round(1)

# Save
df.to_csv('student_data.csv', index=False)
print("student_data.csv generated successfully.")
