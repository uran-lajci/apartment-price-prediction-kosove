import streamlit as st
import joblib
import warnings

warnings.filterwarnings("ignore")

# Select between Classification or Regression
prediction_type = st.selectbox("Select Prediction Type", ['Regression', 'Classification'])

# Load the appropriate model based on the prediction type
if prediction_type == 'Regression':
    models = ['Linear Regression', 'K-nn', 'Decision Tree', 'Random Forest']
    model_file_names = ['linear_regression_model', 'knn_model', 'decision_tree_model', 'random_forest_model']
else:
    models = ['Logistic Regression', 'K-nn', 'Decision Tree', 'Naive Bayes', 'Random Forest']
    model_file_names = ['logistic_regression_model', 'knn_model', 'decision_tree_model', 'naive_bayes_model', 'random_forest_model']

# Select the ml model
selected_model = st.selectbox("Select the Machine Learning Model", models)

# Load the trained machine learning model
model_file_name = model_file_names[models.index(selected_model)]
model = joblib.load(f'{prediction_type.lower()} models/{model_file_name}.joblib')

# Number of rooms
number_of_rooms = st.number_input("Number of Rooms", min_value=0, max_value=5)

# Define room to m^2 mapping
room_to_m2_mapping = {
    0: {"min": 18, "max": 37},  # studio
    1: {"min": 37, "max": 56},  # 1 bedroom
    2: {"min": 56, "max": 93},  # 2 bedrooms
    3: {"min": 93, "max": 140},  # 3 bedrooms
    4: {"min": 130, "max": 170},  # 4 bedrooms
    5: {"min": 170, "max": 500}  # 5 bedrooms
}

# Get min and max for the selected number of rooms
min_m2 = room_to_m2_mapping[number_of_rooms]["min"]
max_m2 = room_to_m2_mapping[number_of_rooms]["max"]

# Quadrat (m^2)
quadrat = st.number_input("Quadrat (m^2)", min_value=min_m2, max_value=max_m2)

# Select region
region = st.selectbox("Select Region", ['Prishtine', 'Other'])

# Select season
season = st.selectbox("Select Season", ['Spring', 'Summer', 'Autumn', 'Winter'])

# When predicting, handle differently based on the prediction type
if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = {
        'number_of_rooms': number_of_rooms,
        'quadrat': quadrat,
        'region_Prishtine': 1 if region == 'Prishtine' else 0,
        'region_other region in Kosove': 1 if region == 'Other' else 0,
        'seasons_Autumn': 1 if season == 'Autumn' else 0,
        'seasons_Spring': 1 if season == 'Spring' else 0,
        'seasons_Summer': 1 if season == 'Summer' else 0,
        'seasons_Winter': 1 if season == 'Winter' else 0
    }

    # Convert input data to a 2D array for prediction
    input_array = [list(input_data.values())]

    prediction_ranges = {
        '60-120': '60 to 120',
        '120-180': '120 to 180',
        '180-240': '180 to 240',
        '240-300': '240 to 300',
        '300-360': '300 to 360',
        '360+': 'greater than 360'
    }

    # Perform prediction using the loaded model
    prediction = model.predict(input_array)[0]

    # Check if the prediction type is classification or regression
    if prediction_type == 'Classification':
        # Use the predicted value to get the corresponding range
        st.write("Predicted Price Range: ", prediction_ranges[prediction])
    else:
        st.write("Predicted Price: ", int(prediction), " euro")