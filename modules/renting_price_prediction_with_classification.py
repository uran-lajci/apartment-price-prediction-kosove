import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
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

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Models
models = [LogisticRegression(), KNeighborsClassifier(), DecisionTreeClassifier(), GaussianNB(), RandomForestClassifier()]
model_names = ["Logistic Regression", "KNN", "Decision Trees", "Naive Bayes", "Random Forest"]
model_files = ['logistic_regression_model.joblib', 'knn_model.joblib', 'decision_tree_model.joblib', 'naive_bayes_model.joblib', 'random_forest_model.joblib']

for model, name, file in zip(models, model_names, model_files):
    model.fit(X_train, y_train)

    # Save the trained model to a file
    dump(model, f'classification models/{file}')

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\n" + name)
    print("Accuracy: ", accuracy)

    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    avg_cross_val_score = np.mean(scores)
    print("Cross validation score: ", avg_cross_val_score)