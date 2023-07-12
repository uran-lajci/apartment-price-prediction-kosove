import pandas as pd
import numpy as np

def get_season(date):
    if 3 <= date.month <= 5:
        return 'Spring'
    elif 6 <= date.month <= 8:
        return 'Summer'
    elif 9 <= date.month <= 11:
        return 'Autumn'
    else:
        return 'Winter'

df = pd.read_csv("datasets/raw_apartment_renting_data.csv")

# Clean 'title' attribute and rename it to property_description
df = df[~df['title'].str.contains('shitet', case=False, na=False)]
df['title'] = df['title'].str.lower() # convert to lowercase
df['title'] = df['title'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True) # remove non-alphanumeric characters
df['title'] = df['title'].str.strip() # remove leading and trailing whitespaces
df = df.rename(columns={'title': 'property_description'})

# Preprocess the 'number_of_rooms' attribute
df['number_of_rooms'] = pd.to_numeric(df['number_of_rooms'], errors='coerce')
df = df.dropna(subset=['number_of_rooms'])
df = df[(df['number_of_rooms'] >= 0) & (df['number_of_rooms'] <= 5)]
df['number_of_rooms'] = df['number_of_rooms'].astype(int)
df = df.rename(columns={'number_of_rooms': 'number of rooms'})

# Preprocess the 'price' attribute
df['price'] = df['price'].replace({'€': ''}, regex=True).apply(pd.to_numeric, errors='coerce')
df = df[(df['price'] >= 60) & (df['price'] <= 2000)]
df = df.rename(columns={'price': 'price (euro)'})

# Preprocess the 'date' attribute and create a new 'seasons' attribute
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df['seasons'] = df['date'].apply(get_season)

# Preprocess the 'quadrat' attribute
df['quadrat'] = df['quadrat'].replace({'m 2': ''}, regex=True).apply(pd.to_numeric, errors='coerce')
room_quadrat_means = df[df['quadrat'] > 1].groupby('number of rooms')['quadrat'].mean().to_dict()
df.loc[df['quadrat'] <= 1, 'quadrat'] = df.loc[df['quadrat'] <= 1, 'number of rooms'].map(room_quadrat_means)
df = df.rename(columns={'quadrat': 'quadrat (m^2)'})

# Preprocess the 'region' attribute
acceptable_regions = ['Drenas', 'Ferizaj', 'Fushe Kosove', 'Gjakove', 'Gjilan', 
                      'Kline', 'Lipjan', 'Malisheve', 'Mitrovice', 'Peje', 
                      'Prishtine', 'Prizren', 'Vushtrri']
df = df[df['region'].isin(acceptable_regions)]
majority_region = 'Prishtine'
df['region'] = np.where(df['region'] == majority_region, majority_region, 'other region in kosove')

# Perform one-hot encoding on 'region', 'seasons' columns
df = pd.get_dummies(df, columns=['region', 'seasons'])

# Reset the DataFrame indexes
df = df.reset_index(drop=True)

df.to_csv("datasets/preprocessed_apartment_renting_data.csv")

print("Data preprocessing completed and saved to preprocessed_apartment_renting_data.csv.")