import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt
from joblib import dump
import threadpoolctl
import warnings

warnings.filterwarnings("ignore")
threadpoolctl.threadpool_limits(limits=1)

df = pd.read_csv("datasets/preprocessed_apartment_renting_data.csv")
X = df[['number of rooms','quadrat (m^2)','region_Prishtine','region_other region in kosove','seasons_Autumn','seasons_Spring','seasons_Summer','seasons_Winter']]
y = df['price (euro)']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Models
models = [LinearRegression(), DecisionTreeRegressor(), RandomForestRegressor(), KNeighborsRegressor(), GaussianNB()]
model_names = ["Linear Regression", "Decision Trees", "Random Forest", "KNN", "Naive Bayes"]
model_files = ['linear_regression_model.joblib', 'decision_tree_model.joblib', 'random_forest_model.joblib', 'knn_model.joblib', 'naive_bayes_model.joblib']

for model, name, file in zip(models, model_names, model_files):
    model.fit(X_train, y_train)

    # Save the trained model to a file
    dump(model, f'regression models/{file}')

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = sqrt(mse)

    print("\n" + name)
    print("Mean absolute error: ", mae)
    print("Mean squared error: ", mse)
    print("Root Mean squared error: ", rmse)

    scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    avg_cross_val_score = np.mean(np.sqrt(np.abs(scores)))
    print("Cross validation score: ", avg_cross_val_score)