import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("datasets/preprocessed_apartment_renting_data.csv")

print("Basic info about the dataset")
print(df.info())

print("\nStatistical information about numerical columns")
print(df.describe())

print("\nThe number of unique values in each column")
print(df.nunique())

# the distribution of the number of rooms and prices
plt.figure(figsize=(10, 6))
sns.histplot(df['number of rooms'], kde=False, bins=30)
plt.title('Distribution of Number of Rooms')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['price (euro)'], kde=False, bins=30)
plt.title('Distribution of Prices')
plt.show()

# visualizing the relationship between the number of rooms and prices
plt.figure(figsize=(10, 6))
sns.boxplot(x='number of rooms', y='price (euro)', data=df)
plt.title('Number of Rooms vs. Price')
plt.show()