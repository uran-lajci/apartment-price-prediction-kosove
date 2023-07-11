import pandas as pd
import numpy as np

df = pd.read_csv("raw_apartment_data.csv")

df['quadrat'] = df['quadrat'].str.replace('m 2', '').astype(float)
df['price'] = df['price'].str.replace('�', '')

def convert_price(price):
    # Remove leading/trailing whitespace and commas
    price = price.strip().replace(',', '')
    # Convert to float
    return float(price)

df["price"] = df["price"].apply(convert_price)

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

# Define the neighborhoods dictionary
neighborhoods = {
    "Qendra": ["qendra", "kampusi universitar", "universitar", "kampusi", "Qender", "Xhamia e Llapit", "Qendër", "Nena Tereze", "Tereze", "Sami Frasheri", "Frasheri", "Mihal", "Grameno"],
    "Lakrishta": ["lakrishta", "lakrishte", "lakrisht", "lagjja pejton", "pejton", "rilindjes", "rilindjes"],
    "Dardania": ["dardania", "lagja dardania", "lagja kalabria", "kalabria", "zona ekonomike", "kompleksi i fsk", "dardani"],
    "Ulpiana": ["ulpiana", "ulpiane", "ulpian"],
    "Ulpiana 1": ["ulpiana 1", "lagja mati", "mati", "kompleksi i qkuk", "prishtina e re", "mat"],
    "Kodra e Diellit": ["kodra e diellit", "lagja aktashi", "aktashi", "banesa e bardha", "Bregu i Diellit", "Bregun e Dillit", "Bregu", "Dielli", "Dilli"],
    "Lagjja e Muhaxherëve": ["lagjja e muhaxherëve", "muhaxhereve", "parku i qytetit", "parkut te qytetit", "lagja dodona", "dodona", "Muhaxherve", "Lagjen e Muhagjerve", "Muhaxheret"],
    "1 Lagjja e Muhaxherëve": ["1 lagjja e muhaxherëve", "muhaxhire", "varri i ish. presidentit i. rugova", "ibrahim rrugova", "rugova" "varrezat e deshmorëve"],
    "2 Lagjja e Muhaxherëve (Matiçan)": ["2 lagjja e muhaxherëve (matiçan)", "zona kadastrale mati", "matican"],
    "Taukbashqe (Sofali)": ["taukbashqe (sofali)", "zona kadastrale sofalia", "parku i taslixhes"],
    "Taukbashqe": ["taukbashqe"],
    "1 Taukbashqe": ["1 taukbashqe"],
    "Blloku B": ["blloku b"],
    "Kodra e Trimave": ["kodra e trimave"],
    "1 Kodra e Trimave": ["1: kodra e trimave", "varrezat e qytetit"],
    "2 Kodra e Trimave": ["2 - kodra e trimave"],
    "Tophane": ["tophane"],
    "Tophane 2": ["tophane 2"],
    "Arbëria (Dragodani)": ["arbëria (dragodani)", "rruga për mitrovicë", "mitrovicë", "Arberia", "Arbëria", "dragodan", "arberi", "Dargodan", "arbëria", "arbëri"],
    "Kalabria": ["kalabria", "Emshir", "Kalabri"],
    "Lagjen e Spitalit": ["Lagjen e Spitalit", "Spitalit"],
    "Rruga C": ["Rrugen C", "Rruga C"],
    "Aktash": ["Aktash"],
    "Rruga B": ["Rruga B", "Rrugen B", "Rruge B"],
    "Qafa": ["Qafa"],
    "4 Lullat": ["4 Llullat", "Llullat"],
    "Fakultetit Teknik": ["Fakultetit Teknik"],
    "Sllovenia e Sportit": ["Sllovenia e Sportit", "Sllovenia", "Slovenia Sporti", "Slovenia"],
    "Siriusi": ["Siriusi", "Sirius"],
    "Mrapa Teatrit": ["Mrapa Teatrit", "Teatrit", "Teatri", "Teater"],
    "Muharrem Fejza": ["Muharrem Fejza"],
    "Velania": ["Velania", "Velani"],
    "Fushe Kosove": ["fushkosov","fushë kosovë", "fushe kosove", "FusheKosove"],
    "Shtepia e Pleqve": ["Shtepia e Pleqve", "Domi", "Pleqve"],
    "Vellushe":["Vellushe"],
    "Germi": ["Germi"],
    "Veternik": ["Veternik"],
}

# Function to map the neighborhood for each rent headline
def get_neighborhood(rent_headline):
    for neighborhood, keywords in neighborhoods.items():
        if any(keyword.lower() in rent_headline.lower() for keyword in keywords):
            return neighborhood
    return None

# Apply the function to create a new column 'Neighborhood'
df_cleaned['Neighborhood'] = df_cleaned['title'].apply(get_neighborhood)

df_cleaned.to_csv("preprocessed_apartment_data.csv")