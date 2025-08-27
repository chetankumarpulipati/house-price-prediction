import streamlit as st
import pandas as pd
import joblib
import io

st.title('House Price Prediction')

# Load model before any logic
try:
    model = joblib.load('model.joblib')
except Exception:
    st.warning('Model file not found. Please train and save your model as model.joblib.')
    model = None

# User chooses prediction mode
st.header('Choose Prediction Mode')
option = st.radio('Select input method:', ('Upload Custom Dataset', 'Manual Input Fields'))

if option == 'Upload Custom Dataset':
    st.subheader('Upload Your Own Dataset')
    uploaded_file = st.file_uploader('Choose a CSV file', type=['csv'])
    if uploaded_file is not None:
        try:
            user_df = pd.read_csv(uploaded_file)
            st.write('Preview of uploaded dataset:')
            st.dataframe(user_df.head())
            st.write('Columns:', list(user_df.columns))
            st.success('Dataset uploaded successfully!')

            # Predict prices for uploaded dataset
            if model:
                required_cols = ['area', 'bedrooms', 'bathrooms']
                if all(col in user_df.columns for col in required_cols):
                    preds = model.predict(user_df[required_cols])
                    user_df['Predicted Price'] = preds
                    st.write('Predicted Prices:')
                    st.dataframe(user_df[[*required_cols, 'Predicted Price']].head(10))
                    st.write('Basic Statistics of Predicted Prices:')
                    st.write(user_df['Predicted Price'].describe())
                    st.write('Distribution of Predicted Prices:')
                    import matplotlib.pyplot as plt
                    fig, ax = plt.subplots()
                    user_df['Predicted Price'].plot(kind='hist', bins=20, ax=ax)
                    st.pyplot(fig)
                else:
                    st.warning(f"Dataset must contain columns: {required_cols}")
            else:
                st.warning('Model not loaded. Cannot predict on uploaded dataset.')
        except Exception as e:
            st.error(f'Error reading file: {e}')

elif option == 'Manual Input Fields':
    st.subheader('Enter the details of the house below:')
    area = st.number_input('Area (sq ft)', min_value=100, max_value=10000, value=1000)
    bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3)
    bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
    # location = st.text_input('Location', value='Downtown')

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