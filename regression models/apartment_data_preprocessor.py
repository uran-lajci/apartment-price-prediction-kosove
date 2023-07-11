import pandas as pd
import numpy as np

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("raw_apartment_data.csv")

print(df.head(5))

df['quadrat'] = df['quadrat'].str.replace('m 2', '').astype(float)
df['price'] = df['price'].str.replace('�', '')

def convert_price(price):
    # Remove leading/trailing whitespace and commas
    price = price.strip().replace(',', '')
    # Convert to float
    return float(price)

df["price"] = df["price"].apply(convert_price)

print(df.head(5))

print(df.info())

print(df.describe())

# Assuming your data is stored in a DataFrame called 'df'
threshold = 5  # Adjust this value as needed

# Select only numeric columns
numeric_cols = df.select_dtypes(include=np.number)

# Calculate z-scores for each numeric column
z_scores = np.abs((numeric_cols - numeric_cols.mean()) / numeric_cols.std())

# Remove data points with z-score above the threshold for each numeric column
df_cleaned_numeric = df[(z_scores < threshold).all(axis=1)]

# Merge cleaned numeric columns with non-numeric columns
# df_cleaned = pd.concat([df_cleaned_numeric, df.select_dtypes(exclude=np.number)], axis=1)

df_cleaned = df_cleaned_numeric

# Assuming your dataset is stored in a DataFrame called 'df'
df_cleaned = df_cleaned[(df_cleaned['number_of_rooms'] >= 0) & (df_cleaned['quadrat'] >= 20) & (df_cleaned['price'] > 100)]

# Optionally, you can reset the index if needed
df_cleaned = df_cleaned.reset_index(drop=True)

print(df_cleaned.info())

print(df_cleaned.describe())

df_cleaned.to_csv("preprocessed_apartment_data.csv")