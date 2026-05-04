🌾 Crop Yield Prediction using Machine Learning
📌 Overview

This project focuses on predicting agricultural crop yield using Machine Learning techniques. It helps farmers and policymakers make data-driven decisions by analyzing historical agricultural data such as rainfall, fertilizer usage, pesticide usage, and crop type.

The system uses ensemble learning models to provide accurate yield predictions and includes a user-friendly interface for real-time input and results.

🚀 Features
Predict crop yield based on multiple input factors
Uses advanced ML algorithms (Random Forest & XGBoost)
Data preprocessing (handling missing values, encoding, scaling)
Model comparison using performance metrics
Simple and interactive UI built with Streamlit
Helps in better crop planning and resource management
🧠 Machine Learning Models Used
🌲 Random Forest Regressor
⚡ XGBoost Regressor

📊 Performance:

Random Forest → R² Score: 99.45%
XGBoost → R² Score: 98.92%

(Random Forest performed slightly better in this project )

📂 Dataset Information
Source: Kaggle Crop Yield Dataset
Total Records: ~19,698
Features:
Crop
Crop Year
Season
State
Area
Production
Annual Rainfall
Fertilizer
Pesticide
Target:
Yield
⚙️ Project Workflow
Data Collection
Data Preprocessing
Handling missing values
Encoding categorical data
Feature scaling
Train-Test Split (80% Training, 20% Testing)
Model Training (RF & XGBoost)
Hyperparameter Tuning (GridSearchCV)
Model Evaluation (MAE, RMSE, R² Score)
Deployment using Streamlit UI
📊 Evaluation Metrics
R² Score → Accuracy of prediction
MAE (Mean Absolute Error) → Average error
RMSE (Root Mean Square Error) → Penalizes large errors
🖥️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
XGBoost
Matplotlib, Seaborn
Streamlit
💡 How It Works
User inputs:
Crop type
Area
Rainfall
Fertilizer usage
Pesticide usage
Model processes the data
Predicts expected crop yield
Displays result instantly on UI
📈 Results
High prediction accuracy achieved using ensemble models
Random Forest showed better performance with lower error rates
Model effectively captures relationships between agricultural factors and yield
🔮 Future Improvements
Integration with real-time weather APIs
Soil health analysis
Satellite/drone data integration
Mobile application for farmers
Multi-language support for accessibility
📌 Applications
Smart farming
Crop planning
Resource optimization
Government policy planning
Agricultural analytics
👩‍💻 Contributors
Bhargavi
Team Members
📎 Conclusion

This project demonstrates how Machine Learning can significantly improve agricultural productivity by providing accurate and reliable crop yield predictions. It reduces dependency on guesswork and supports smart farming practices.
