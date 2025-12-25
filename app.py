from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load Model
model = joblib.load('student_performance_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features
        parental_education = data.get('parentalEducation')
        attendance_percentage = float(data.get('attendancePercentage'))
        previous_year_percentage = float(data.get('previousYearPercentage'))
        study_hours = int(data.get('studyHours'))
        internet_access = data.get('internetAccess') # 'No' or 'Yes'
        
        # Preprocessing (same as training)
        edu_map = {'None': 0, 'Primary': 1, 'Secondary': 2, 'Higher': 3}
        # Handle case sensitivity just in case
        p_edu = edu_map.get(parental_education, 0)
        
        net_map = {'No': 0, 'Yes': 1}
        net_acc = net_map.get(internet_access, 0)
        
        # Create DF for prediction
        input_data = pd.DataFrame([{
            'parentalEducation': p_edu,
            'AttendancePercentage': attendance_percentage,
            'PreviousYearPercentage': previous_year_percentage,
            'StudyHoursPerWeek': study_hours,
            'InternetAccess': net_acc
        }])
        
        prediction = model.predict(input_data)[0]
        
        return jsonify({'success': True, 'presentPercentage': round(prediction, 2)})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
