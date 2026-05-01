# 🌾 Ensemble-Based Crop Yield Prediction using Random Forest & XGBoost

## 📌 Overview
This project focuses on predicting crop yield using machine learning techniques. It implements an **ensemble learning approach** by combining **Random Forest** and **XGBoost** models to achieve higher prediction accuracy and better generalization.

The system analyzes agricultural and environmental factors such as rainfall, fertilizer usage, and crop type to estimate crop yield effectively.

---

## 🎯 Objective
- Predict crop yield based on input features
- Compare performance of multiple ML models
- Improve prediction accuracy using ensemble techniques
- Provide a simple and interactive user interface for predictions

---

## 🧠 Models Used
- Random Forest Regressor
- XGBoost Regressor
- Ensemble Model (combination of both models)

---

## 📊 Dataset
The dataset used in this project contains the following features:

- Crop  
- Crop_Year  
- Season  
- State  
- Area  
- Production  
- Annual_Rainfall  
- Fertilizer  
- Pesticide  
- Yield (Target Variable)

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Handled missing values  
- Encoded categorical features  
- Checked data consistency  

### 2. Feature Engineering
- Selected important features  
- Analyzed correlations between variables  

### 3. Model Training
- Trained Random Forest model  
- Trained XGBoost model  
- Combined both models using ensemble approach  

### 4. Model Evaluation
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---

## 📈 Results
The ensemble model outperformed individual models by providing better accuracy and stability.

| Model            | Performance |
|------------------|------------|
| Random Forest    | Good       |
| XGBoost          | Better     |
| Ensemble Model   | Best ✅     |

---

## 💻 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib, Seaborn  
- Streamlit  

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/naikawadibhargavi/ML-PROJECT.git
cd ML-PROJECT
