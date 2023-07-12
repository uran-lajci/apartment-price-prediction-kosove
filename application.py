import streamlit as st
import joblib
import warnings

warnings.filterwarnings("ignore")

# Select the ml model
season = st.selectbox("Select the Machine Learning Model", ['Linear Regression', 'K-nn', 'Decision Tree', 'Naive Bayes', 'Random Forest'])

# Load the trained machine learning model
model = None

if season == 'Linear Regression':
    model = joblib.load('regression models/linear_regression_model.joblib')
elif season == 'K-nn':
    model = joblib.load('regression models/knn_model.joblib')
elif season == 'Decision Tree':
    model = joblib.load('regression models/decision_tree_model.joblib')
elif season == 'Naive Bayes':
    model = joblib.load('regression models/naive_bayes_model.joblib')
elif season == 'Random Forest':
    model = joblib.load('regression models/random_forest_model.joblib')

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
region = st.selectbox("Select Region", ['region_Prishtine', 'region_other region in Kosove'])

# Select season
season = st.selectbox("Select Season", ['seasons_Autumn', 'seasons_Spring', 'seasons_Summer', 'seasons_Winter'])

# Make prediction when all necessary fields are filled
if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = {
        'number_of_rooms': number_of_rooms,
        'quadrat': quadrat,
        'region_Prishtine': 1 if region == 'region_Prishtine' else 0,
        'region_other region in Kosove': 1 if region == 'region_other region in Kosove' else 0,
        'seasons_Autumn': 1 if season == 'seasons_Autumn' else 0,
        'seasons_Spring': 1 if season == 'seasons_Spring' else 0,
        'seasons_Summer': 1 if season == 'seasons_Summer' else 0,
        'seasons_Winter': 1 if season == 'seasons_Winter' else 0
    }

    # Convert input data to a 2D array for prediction
    input_array = [list(input_data.values())]

    # Perform prediction using the loaded model
    prediction = model.predict(input_array)[0]

    # Display the predicted price
    st.write("Predicted Price: ", int(prediction), " euro")