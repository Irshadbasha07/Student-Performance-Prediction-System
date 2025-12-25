# 🎓 Student Performance Prediction System

## 📌 Project Description
The **Student Performance Prediction System** is a full-stack machine learning web application that predicts a student’s **Present Percentage** based on academic, behavioral, and environmental factors.

This project combines:
- **Machine Learning (Random Forest Regressor)**
- **Flask Backend API**
- **Modern HTML/CSS/JavaScript Frontend**
to deliver accurate predictions through an interactive web interface.

---

## 🚀 Key Features
- Predicts student present percentage in real-time
- Machine learning model trained on synthetic but realistic data
- REST API built using Flask
- Clean, responsive, and animated UI
- End-to-end integration (Frontend → Backend → ML Model)
- Reset and re-predict functionality

---

## 🧠 Machine Learning Details
- **Algorithm:** Random Forest Regressor  
- **Dataset Size:** 1000 student records  
- **Target Variable:** PresentPercentage  

### 📊 Input Features
- Parental Education  
- Attendance Percentage  
- Previous Year Percentage  
- Study Hours per Week  
- Internet Access  

### 📈 Model Evaluation
- Mean Absolute Error (MAE)
- R² Score
- Model serialized using `joblib`

---

## 🛠️ Technology Stack

### 🔹 Frontend
- HTML5
- CSS3 (Glassmorphism UI)
- JavaScript (Fetch API, Animations)

### 🔹 Backend
- Python
- Flask (REST API)

### 🔹 Machine Learning
- Pandas
- NumPy
- Scikit-learn
- RandomForestRegressor

---

## 📂 Project Structure
├── app.py            # Flask backend
├── train_model.py    # Model training script
├── generate_data.py  # Dataset generation
├── test_api.py       # API testing script
├── student_data.csv  # Dataset
├── student_performance_model.pkl
├── requirements.txt
├── templates/
│ └── index.html      # Frontend HTML
└── static/
├── style.css         # Styling
└── script.js         # Frontend logic


---
 
## ⚙️ How the System Works
1. User enters student details in the web UI
2. Data is sent to Flask API (`/predict`)
3. Input is preprocessed
4. Trained ML model predicts present percentage
5. Result is returned and displayed with animation

---
