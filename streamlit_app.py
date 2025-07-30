import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("gbm.pkl")  # model filename
encoder = joblib.load("encoder.pkl")       # used OneHotEncoder 

st.title("🚗 Vehicle Price Prediction App")
st.write("Enter vehicle details to estimate its price.")

# Input fields
manufacturer = st.selectbox("Manufacturer", ["Ford", "Toyota", "BMW", "Other"])
model_name = st.text_input("Model Name")
fuel = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Electric", "Hybrid"])
year = st.slider("Year", 1990, 2025, 2020)
mileage = st.number_input("Mileage (in miles)", min_value=0, value=50000)

# Create input DataFrame
input_df = pd.DataFrame({
    "manufacturer": [manufacturer],
    "model": [model_name],
    "fuel": [fuel],
    "year": [year],
    "mileage": [mileage]
})

# Encode and predict
# input_encoded = encoder.transform(input_df)  # Uncomment if needed
prediction = model.predict(input_df)[0]

st.subheader(f"💰 Estimated Price: ${prediction:,.2f}")
