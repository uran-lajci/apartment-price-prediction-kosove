import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("preprocessed_apartment_data.csv")

# 1. Visualize by the number of cities (regions)
df['region'].value_counts().plot(kind='bar')
plt.xlabel('Region')
plt.ylabel('Number of Apartments')
plt.show()

# # 2. Visualize by the number of headlines per year
# df['year'] = df['date'].dt.year
# df['year'].value_counts().sort_index().plot(kind='line')
# plt.xlabel('Year')
# plt.ylabel('Number of Apartments')
# plt.show()

# 3. Visualize by the price
df['price'].plot(kind='hist', bins=50)
plt.xlabel('Price')
plt.ylabel('Number of Apartments')
plt.show()

# 4. Visualize by the quadrat
df['quadrat'].plot(kind='hist', bins=50)
plt.xlabel('Quadrat')
plt.ylabel('Number of Apartments')
plt.show()

# 5. Visualize by the rooms
df['number_of_rooms'].value_counts().plot(kind='bar')
plt.xlabel('Number of Rooms')
plt.ylabel('Number of Apartments')
plt.show()
