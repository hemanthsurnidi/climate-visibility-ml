# 🌤️ Climate Visibility Prediction using Machine Learning

## 📌 Project Overview
This project is an **end-to-end Machine Learning application** that predicts **atmospheric visibility (in kilometers)** based on weather conditions such as temperature, humidity, wind, pressure, and precipitation.

The trained machine learning model is integrated into a **Flask web application** with a clean and user-friendly interface, allowing users to input weather data and instantly get visibility predictions.

---

## 🎯 Problem Statement
Weather conditions like fog, rain, and high humidity significantly affect visibility, which is critical for:
- Road transportation safety
- Aviation operations
- Outdoor planning and logistics

The goal of this project is to **predict visibility distance** using historical climate data and machine learning techniques.

---

## 🧠 Machine Learning Details
- **Problem Type:** Regression
- **Target Variable:** `VISIBILITY`
- **Final Model Used:** Random Forest Regressor

### Why Random Forest?
- Captures non-linear relationships
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
1. Dataset loading and exploration (EDA)
2. Data preprocessing:
   - Handling missing values
   - Feature scaling using StandardScaler
3. Model training:
   - Baseline Linear Regression
   - Random Forest Regressor
4. Model evaluation and comparison
5. Saving trained model and scaler
6. Flask app integration
7. UI design and result display
8. Version control using GitHub

---

## 🖥️ Web Application
The Flask application allows users to:
- Enter weather conditions
- Predict visibility instantly
- View results on a clean, modern interface

---

## 📂 Project Structure
