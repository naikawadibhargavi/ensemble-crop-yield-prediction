import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load trained model and encoders
model = joblib.load("best_model.pkl")
crop_encoder = joblib.load("crop_encoder.pkl")
season_encoder = joblib.load("season_encoder.pkl")
state_encoder = joblib.load("state_encoder.pkl")

st.title("Crop Yield Prediction 🌾")
st.markdown("Provide the following inputs to estimate the *Crop Yield*:")

# User Inputs
crop = st.selectbox("Crop", crop_encoder.classes_)
crop_year = st.number_input("Crop Year", min_value=2000, max_value=2025, value=2023)
season = st.selectbox("Season", season_encoder.classes_)
state = st.selectbox("State", state_encoder.classes_)
area = st.number_input("Area (in Hectares)", min_value=0.1, value=1000.0)
rainfall = st.number_input("Annual Rainfall (mm)", min_value=0.0, value=800.0)
production = st.number_input("Production (in tonnes)", min_value=0.0, format="%.2f")
fertilizer = st.number_input("Fertilizer Used (kg)", min_value=0.0, value=200.0)
pesticide = st.number_input("Pesticide Used (kg)", min_value=0.0, value=50.0)

# Encode categorical features
crop_encoded = crop_encoder.transform([crop])[0]
season_encoded = season_encoder.transform([season])[0]
state_encoded = state_encoder.transform([state])[0]

# Prepare input dataframe
input_data = pd.DataFrame([{
    "Crop": crop_encoded,
    "Crop_Year": crop_year,
    "Season": season_encoded,
    "State": state_encoded,
    "Area": area,
    "Annual_Rainfall": rainfall,
    "Production": production,
    "Fertilizer": fertilizer,
    "Pesticide": pesticide
}])

# Predict yield
if st.button("Predict Yield"):
    predicted_yield = model.predict(input_data)
    st.success(f"Estimated Crop Yield: *{predicted_yield[0]:,.2f} tonnes*")