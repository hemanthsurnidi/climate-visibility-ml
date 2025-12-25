# 🌤️ Climate Visibility Prediction using Machine Learning

## 📌 Project Overview
This project is an end-to-end Machine Learning application that predicts atmospheric visibility (in kilometers) based on weather conditions such as temperature, humidity, wind, pressure, and precipitation.

The trained model is deployed using a Flask web application with a clean and user-friendly interface that allows users to input weather parameters and instantly receive visibility predictions.

---

## 🎯 Problem Statement
Weather conditions like fog, rain, and high humidity significantly affect visibility, which is critical for:
- Road transportation safety
- Aviation operations
- Outdoor planning and logistics

The objective of this project is to predict visibility distance using historical climate data and machine learning techniques.

---

## 🧠 Machine Learning Details
- Problem Type: Regression  
- Target Variable: VISIBILITY  
- Final Model Used: Random Forest Regressor  

### Why Random Forest?
- Captures non-linear relationships effectively  
- Robust to noise and outliers  
- Performs better than baseline linear regression  

---

## 📊 Input Features
The model uses the following weather parameters:
- Dry Bulb Temperature
- Wet Bulb Temperature
- Dew Point Temperature
- Relative Humidity
- Wind Speed
- Wind Direction
- Station Pressure
- Sea Level Pressure
- Precipitation

---

## 🧪 Project Workflow
1. Dataset loading and exploratory data analysis (EDA)
2. Data preprocessing:
   - Handling missing values
   - Feature scaling using StandardScaler
3. Model training:
   - Baseline Linear Regression
   - Random Forest Regressor
4. Model evaluation and comparison
5. Selection of final model
6. Saving trained model and scaler
7. Flask app integration
8. UI design and prediction display
9. Version control and GitHub upload

---

## 🖥️ Web Application
The Flask web application allows users to:
- Enter weather conditions
- Predict visibility instantly
- View results on a clean and modern interface

---

## 📂 Project Structure
Climate_Visibility/
├── app.py
├── requirements.txt
├── README.md
├── artifacts/
│   ├── random_forest_model.pkl
│   └── scaler.pkl
├── data/
│   └── data.csv
├── notebooks/
│   └── EDA.ipynb
└── templates/
    ├── index.html
    └── result.html

---

## ⚙️ How to Run the Project Locally

### Clone the repository
git clone https://github.com/hemanthsurnidi/climate-visibility-ml.git  
cd climate-visibility-ml  

### Create and activate virtual environment
python -m venv venv  
venv\Scripts\activate  

### Install dependencies
pip install -r requirements.txt  

### Run the Flask application
python app.py  

### Open in browser
http://127.0.0.1:5000/

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Random Forest Regressor
- Flask
- HTML & CSS
- Git & GitHub

---

## 🚀 Key Learnings
- End-to-end machine learning project development
- Data preprocessing and feature scaling
- Model training, evaluation, and selection
- Saving and loading machine learning models
- Flask integration with ML models
- GitHub version control workflow

---

## 📌 Future Enhancements
- Use Git LFS or cloud storage for large model files
- Deploy the application on cloud platforms
- Integrate real-time weather APIs
- Improve UI responsiveness and design

---

## 👨‍💻 Author
Hemanth Surnidi  
Data Science & Machine Learning Enthusiast
