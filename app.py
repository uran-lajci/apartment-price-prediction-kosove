import streamlit as st
from joblib import load

# Load the model
model = load('linear_regression_model.joblib')

# Define the app
def run():

    # Create inputs for all your features
    st.sidebar.header('User Input Features')

    # Use sliders for number_of_rooms and quadrat, adjusting the min and max values to match your data
    number_of_rooms = st.sidebar.slider(label='Number of Rooms', min_value=1, max_value=5, value=2, step=1)
    quadrat = st.sidebar.slider(label='Quadrat', min_value=20, max_value=240, value=70, step=1)

    # Use a select box for the region feature
    region = st.sidebar.selectbox('Region', ['region_Prishtine', 'region_Peje', 'region_Ferizaj', 'region_Fushe Kosove'])

    # Create a dictionary to encode the selected region
    region_encoded = {r: int(region == r) for r in ['region_Prishtine', 'region_Peje', 'region_Ferizaj', 'region_Fushe Kosove']}

    # Combine the features into a single dictionary
    user_input = {'number_of_rooms': number_of_rooms, 'quadrat': quadrat, **region_encoded}

    # Make predictions
    st.subheader('Prediction')

    # Extract the values in the correct order
    input_data = [user_input[feature] for feature in ['number_of_rooms', 'quadrat', 'region_Prishtine']]

    prediction = model.predict([input_data])
    st.write(f'Predicted price is {prediction[0]}')

# Run the app
if __name__ == '__main__':
    run()