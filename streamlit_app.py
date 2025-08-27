import streamlit as st
import pandas as pd
import joblib

st.title('House Price Prediction')

st.write('Enter the details of the house below:')

area = st.number_input('Area (sq ft)', min_value=100, max_value=10000, value=1000)
bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3)
bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
location = st.text_input('Location', value='Downtown')

try:
    model = joblib.load('model.joblib')
except Exception:
    st.warning('Model file not found. Please train and save your model as model.joblib.')
    model = 'model.joblib'

if st.button('Predict Price'):
    if model:
        input_df = pd.DataFrame({
            'area': [area],
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms]
        })
        try:
            prediction = model.predict(input_df)[0]
            st.success(f'Predicted House Price: ${prediction:,.2f}')
        except Exception as e:
            st.error(f'Prediction failed: {e}')
    else:
        st.error('Model not loaded.')

st.write('Note: Update the input fields and model loading logic as per your notebook features and trained model.')
