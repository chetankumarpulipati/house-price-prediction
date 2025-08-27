# House Price Prediction with Linear Regression

## Project Description

The goal of this project is to build a basic house price prediction model using a Linear Regression algorithm. The dataset used for this analysis contains information about various houses, including their price, area, number of bedrooms, bathrooms, and other features.

## Dataset

You can download the dataset from [Google Drive](https://drive.google.com/file/d/1kQfIK4aKWArFL12H9i1S77Oajb3w3FG7/view?usp=sharing).

## Libraries Used

The following Python libraries were used in this project:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Data Preprocessing

The following data preprocessing steps were performed:

1. Loaded the dataset from a CSV file into a pandas DataFrame.
2. Explored the dataset using methods like `head()`, `describe()`, `shape`, and `unique()`.
3. Handled missing values (if any).
4. Selected relevant features for the model: price, area, bedrooms, bathrooms.
5. Split the dataset into training and testing sets (80% train, 20% test).

## Model Building and Evaluation

1. A Linear Regression model was trained using the training data.
2. Predictions were made on the test data using the trained model.
3. The model's performance was evaluated using Mean Squared Error (MSE) and R-squared score.
4. Visualizations were created to analyze the relationship between features and the predicted prices.

## Results

The Linear Regression model achieved the following results:

- **Mean Squared Error:** 2,750,040,479,309.0522
- **R-Squared:** 0.4559299118872445

## Conclusion

This project demonstrates a basic implementation of Linear Regression for house price prediction. The model shows some predictive power; however, the relatively low R-squared score suggests that other factors or more complex models could potentially improve the accuracy of predictions.

## Fork to develop the following:

1. Explore and engineer additional features for the model (e.g., location, amenities).
2. Experiment with other regression algorithms (e.g., Ridge Regression, Lasso Regression).
3. Fine-tune hyperparameters to optimize model performance.
4. Deploy the model as a web application for interactive use.

## Streamlit Web Application

This project includes a Streamlit app for interactive house price prediction.

### How to Run the Streamlit App

1. Install dependencies:
	```
	pip install -r requirements.txt
	```
2. Ensure your trained model is saved as `model.joblib` in the project folder.
3. Start the app:
	```
	streamlit run streamlit_app.py
	```
4. Enter house details in the web interface to get price predictions.

### Features
- User-friendly interface for entering house details (area, bedrooms, bathrooms)
- Predicts house price using the trained model
- Error handling for missing model file or prediction issues
- Option for users to upload and preview their own dataset (CSV)

### Upload and Process Your Own Dataset
You can upload your own CSV dataset using the file uploader in the Streamlit app. The app will display a preview and column names of your uploaded data. This feature allows you to explore and process custom datasets interactively.

### Deployment
You can deploy this app to Streamlit Community Cloud or other cloud platforms for public access. For Streamlit Cloud, simply upload your repository and set the main file to `streamlit_app.py`.

