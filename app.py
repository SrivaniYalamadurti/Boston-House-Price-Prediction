import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Boston House Price Prediction",
    page_icon="🏠"
)

st.title("🏠 Boston House Price Prediction")

st.write("Enter the house details below to predict the house price.")

st.subheader("House Details")

crim = st.number_input("Crime Rate (CRIM)", min_value=0.0)
zn = st.number_input("Residential Land Zone (ZN)", min_value=0.0)
indus = st.number_input("Industrial Area (INDUS)", min_value=0.0)
chas = st.number_input("Charles River (CHAS)", min_value=0.0, max_value=1.0)
nox = st.number_input("Nitric Oxide Concentration (NOX)", min_value=0.0)
rm = st.number_input("Average Number of Rooms (RM)", min_value=0.0)
age = st.number_input("Age of Houses (AGE)", min_value=0.0)
dis = st.number_input("Distance to Employment Centers (DIS)", min_value=0.0)
rad = st.number_input("Accessibility to Highways (RAD)", min_value=0.0)
tax = st.number_input("Property Tax Rate (TAX)", min_value=0.0)
ptratio = st.number_input("Pupil-Teacher Ratio (PTRATIO)", min_value=0.0)
b = st.number_input("Black Population Index (B)", min_value=0.0)
lstat = st.number_input("Lower Status Population (LSTAT)", min_value=0.0)

if st.button("🏠 Predict House Price"):

    input_data = np.array([[
        crim,
        zn,
        indus,
        chas,
        nox,
        rm,
        age,
        dis,
        rad,
        tax,
        ptratio,
        b,
        lstat
    ]])

    model = joblib.load("house_price_model.pkl")

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: {prediction[0]:.2f}")