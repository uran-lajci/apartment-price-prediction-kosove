import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump

# Load the data into a pandas DataFrame
data = pd.read_csv("preprocessed_apartment_data.csv")

# Encode categorical variables
data = pd.get_dummies(data, columns=['region'])

# print(data.head())

# Split the data into training and testing sets
X = data[['number_of_rooms', 'quadrat', 'region_Prishtine']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file
dump(model, 'linear_regression_model.joblib')

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")