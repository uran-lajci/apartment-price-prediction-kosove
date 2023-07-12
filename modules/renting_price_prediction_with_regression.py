import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
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

# Linear Regression
linear_regression_model = LinearRegression()
linear_regression_model.fit(X, y)

# Save the trained linear regression model to a file
dump(linear_regression_model, 'regression models/linear_regression_model.joblib')

linear_regression_predictions = linear_regression_model.predict(X)
linear_regression_mae = mean_absolute_error(y, linear_regression_predictions)
linear_regression_mse = mean_squared_error(y, linear_regression_predictions)
linear_regression_rmse = sqrt(linear_regression_mse)

print("Linear Regression")
print("Mean absolute error: ", linear_regression_mae)
print("Mean squared error: ", linear_regression_mse)
print("Root Mean squared error: ", linear_regression_rmse)

linear_regression_scores = cross_val_score(linear_regression_model, X, y, cv=5, scoring='neg_mean_squared_error')
linear_regression_avg_cross_val_score = np.mean(np.sqrt(np.abs(linear_regression_scores)))
print("Cross validation score: ", linear_regression_avg_cross_val_score)

# Decision Trees
decision_tree_model = DecisionTreeRegressor()
decision_tree_model.fit(X, y)

# Save the trained decision tree regression model to a file
dump(decision_tree_model, 'regression models/decision_tree_model.joblib')

decision_tree_predictions = decision_tree_model.predict(X)
decision_tree_mae = mean_absolute_error(y, decision_tree_predictions)
decision_tree_mse = mean_squared_error(y, decision_tree_predictions)
decision_tree_rmse = sqrt(decision_tree_mse)

print("\nDecision Trees")
print("Mean absolute error: ", decision_tree_mae)
print("Mean squared error: ", decision_tree_mse)
print("Root Mean squared error: ", decision_tree_rmse)

decision_tree_scores = cross_val_score(decision_tree_model, X, y, cv=5, scoring='neg_mean_squared_error')
decision_tree_avg_cross_val_score = np.mean(np.sqrt(np.abs(decision_tree_scores)))
print("Cross validation score: ", decision_tree_avg_cross_val_score)

# Random Forest
random_forest_model = RandomForestRegressor()
random_forest_model.fit(X, y)

# Save the trained random forest regression model to a file
dump(random_forest_model, 'regression models/random_forest_model.joblib')

random_forest_predictions = random_forest_model.predict(X)
random_forest_mae = mean_absolute_error(y, random_forest_predictions)
random_forest_mse = mean_squared_error(y, random_forest_predictions)
random_forest_rmse = sqrt(random_forest_mse)

print("\nRandom Forest")
print("Mean absolute error: ", random_forest_mae)
print("Mean squared error: ", random_forest_mse)
print("Root Mean squared error: ", random_forest_rmse)

random_forest_scores = cross_val_score(random_forest_model, X, y, cv=5, scoring='neg_mean_squared_error')
random_forest_avg_cross_val_score = np.mean(np.sqrt(np.abs(random_forest_scores)))
print("Cross validation score: ", random_forest_avg_cross_val_score)

# KNN
knn_model = KNeighborsRegressor()
knn_model.fit(X, y)

# Save the trained knn regression model to a file
dump(knn_model, 'regression models/knn_model.joblib')

knn_predictions = knn_model.predict(X)
knn_mae = mean_absolute_error(y, knn_predictions)
knn_mse = mean_squared_error(y, knn_predictions)
knn_rmse = sqrt(knn_mse)

print("\nKNN")
print("Mean absolute error: ", knn_mae)
print("Mean squared error: ", knn_mse)
print("Root Mean squared error: ", knn_rmse)

knn_scores = cross_val_score(knn_model, X, y, cv=5, scoring='neg_mean_squared_error')
knn_avg_cross_val_score = np.mean(np.sqrt(np.abs(knn_scores)))
print("Cross validation score: ", knn_avg_cross_val_score)

# Naive Bayes
naive_bayes_model = GaussianNB()
naive_bayes_model.fit(X, y)

# Save the trained naive bayes regression model to a file
dump(naive_bayes_model, 'regression models/naive_bayes_model.joblib')

naive_bayes_predictions = naive_bayes_model.predict(X)
naive_bayes_mae = mean_absolute_error(y, naive_bayes_predictions)
naive_bayes_mse = mean_squared_error(y, naive_bayes_predictions)
naive_bayes_rmse = sqrt(naive_bayes_mse)

print("\nNaive Bayes")
print("Mean absolute error: ", naive_bayes_mae)
print("Mean squared error: ", naive_bayes_mse)
print("Root Mean squared error: ", naive_bayes_rmse)

naive_bayes_scores = cross_val_score(naive_bayes_model, X, y, cv=5, scoring='neg_mean_squared_error')
naive_bayes_avg_cross_val_score = np.mean(np.sqrt(np.abs(naive_bayes_scores)))
print("Cross validation score: ", naive_bayes_avg_cross_val_score)