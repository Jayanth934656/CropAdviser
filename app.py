import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('cropapp1')

# Define the UI layout and user inputs
st.set_page_config(
    page_title="Crop Advisor🌾",
    page_icon="🌾",
    layout="wide"
)

st.title('Crop Recommendation🌾')
st.write('Created by Team 7')
st.write('Enter the values for Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall to get the recommended crop.')

# User inputs using text boxes
try:
    nitrogen = float(st.text_input('Nitrogen (0-100)', '50'))
    phosphorus = float(st.text_input('Phosphorus (0-100)', '50'))
    potassium = float(st.text_input('Potassium (0-100)', '50'))
    temperature = float(st.text_input('Temperature (0.0-50.0)', '25.0'))
    humidity = float(st.text_input('Humidity (0.0-100.0)', '50.0'))
    ph = float(st.text_input('pH (0.0-14.0)', '7.0'))
    rainfall = float(st.text_input('Rainfall (0.0-500.0 mm)', '100.0'))

    # Prepare the user input in the required format
    user_input = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]

    # Predict the crop
    prediction = model.predict(user_input)

    # Display the prediction with larger font size using HTML markup
    st.write(f'<p style="font-size: 24px;">Predicted Crop: {prediction[0]}</p>', unsafe_allow_html=True)

except ValueError:
    st.error("Please enter valid numerical values for all fields.")
