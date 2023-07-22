import streamlit as st
import numpy as np
import joblib
from keras.models import load_model

model = load_model('Contract_prediction_model.h5')
scaler = joblib.load('scaler.pkl')

def predict_revised_amount(original_amount, gdp_growth, inflation, manufacturing_value_added):

    input_data = np.array([[original_amount, gdp_growth, inflation, manufacturing_value_added]])
    input_data_scaled = scaler.transform(input_data)

    predicted_revised_amount = model.predict(input_data_scaled)[0][0]

    return predicted_revised_amount

def main():
    st.title('Contract Amount Prediction')
    st.markdown(
            "<p class='footer'>Created with ❤️ by Aditya Shirke</p>",
            unsafe_allow_html=True
        )

    original_amount = st.number_input('Original Amount($)')
    gdp_growth = st.number_input('GDP Growth(%)')
    inflation = st.number_input('Inflation(%)')
    manufacturing_value_added = st.number_input('Manufacturing Value Added(%)')

    if st.button('Predict Revised Amount'):
        predicted_amount = predict_revised_amount(original_amount, gdp_growth, inflation, manufacturing_value_added)
        st.success(f'Predicted Revised Amount: {predicted_amount:.2f} $')
        st.info('Model is built on US-specific dataset and contains little amount inconsistencies. It just aims to roughly estimate the amount !',icon="ℹ️")

if __name__ == '__main__':
    main()
