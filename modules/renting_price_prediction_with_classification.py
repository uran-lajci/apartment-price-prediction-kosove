import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from joblib import dump
import threadpoolctl
import warnings

warnings.filterwarnings("ignore")
threadpoolctl.threadpool_limits(limits=1)

df = pd.read_csv("datasets/preprocessed_apartment_renting_data.csv")

# Assuming df is your DataFrame and 'price' is the column with the prices
bins = [60, 120, 180, 240, 300, 360, float('inf')]
labels = ['60-120', '120-180', '180-240', '240-300', '300-360', '360+']
df['price_group'] = pd.cut(df['price (euro)'], bins=bins, labels=labels, include_lowest=True)

X = df[['number of rooms','quadrat (m^2)','region_Prishtine','region_other region in kosove','seasons_Autumn','seasons_Spring','seasons_Summer','seasons_Winter']]
y = df['price_group']  # Use price_group as target variable

# Logistic Regression
logistic_regression_model = LogisticRegression()
logistic_regression_model.fit(X, y)

# Save the trained logistic regression model to a file
dump(logistic_regression_model, 'classification models/logistic_regression_model.joblib')

logistic_regression_predictions = logistic_regression_model.predict(X)
logistic_regression_accuracy = accuracy_score(y, logistic_regression_predictions)

print("Logistic Regression")
print("Accuracy: ", logistic_regression_accuracy)

logistic_regression_scores = cross_val_score(logistic_regression_model, X, y, cv=5, scoring='accuracy')
logistic_regression_avg_cross_val_score = np.mean(logistic_regression_scores)
print("Cross validation score: ", logistic_regression_avg_cross_val_score)

# KNN
knn_model = KNeighborsClassifier()
knn_model.fit(X, y)

# Save the trained knn model to a file
dump(knn_model, 'classification models/knn_model.joblib')

knn_predictions = knn_model.predict(X)
knn_accuracy = accuracy_score(y, knn_predictions)

print("\nKNN")
print("Accuracy: ", knn_accuracy)

knn_scores = cross_val_score(knn_model, X, y, cv=5, scoring='accuracy')
knn_avg_cross_val_score = np.mean(knn_scores)
print("Cross validation score: ", knn_avg_cross_val_score)


# Decision Tree
decision_tree_model = DecisionTreeClassifier()
decision_tree_model.fit(X, y)

# Save the trained decision tree model to a file
dump(decision_tree_model, 'classification models/decision_tree_model.joblib')

decision_tree_predictions = decision_tree_model.predict(X)
decision_tree_accuracy = accuracy_score(y, decision_tree_predictions)

print("\nDecision Trees")
print("Accuracy: ", decision_tree_accuracy)

decision_tree_scores = cross_val_score(decision_tree_model, X, y, cv=5, scoring='accuracy')
decision_tree_avg_cross_val_score = np.mean(decision_tree_scores)
print("Cross validation score: ", decision_tree_avg_cross_val_score)


# Naive Bayes
naive_bayes_model = GaussianNB()
naive_bayes_model.fit(X, y)

# Save the trained naive bayes model to a file
dump(naive_bayes_model, 'classification models/naive_bayes_model.joblib')

naive_bayes_predictions = naive_bayes_model.predict(X)
naive_bayes_accuracy = accuracy_score(y, naive_bayes_predictions)

print("\nNaive Bayes")
print("Accuracy: ", naive_bayes_accuracy)

naive_bayes_scores = cross_val_score(naive_bayes_model, X, y, cv=5, scoring='accuracy')
naive_bayes_avg_cross_val_score = np.mean(naive_bayes_scores)
print("Cross validation score: ", naive_bayes_avg_cross_val_score)


# Random Forest
random_forest_model = RandomForestClassifier()
random_forest_model.fit(X, y)

# Save the trained random forest model to a file
dump(random_forest_model, 'classification models/random_forest_model.joblib')

random_forest_predictions = random_forest_model.predict(X)
random_forest_accuracy = accuracy_score(y, random_forest_predictions)

print("\nRandom Forest")
print("Accuracy: ", random_forest_accuracy)

random_forest_scores = cross_val_score(random_forest_model, X, y, cv=5, scoring='accuracy')
random_forest_avg_cross_val_score = np.mean(random_forest_scores)
print("Cross validation score: ", random_forest_avg_cross_val_score)