import pandas as pd

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Define the neighborhoods dictionary
neighborhoods = {
    "Qendra": ["qendra", "kampusi universitar", "universitar", "kampusi", "Qender", "Xhamia e Llapit", "Qendër"],
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
    "Sami Frasheri": ["Sami Frasheri", "Frasheri"],
    "Mihal Grameno": ["Mihal", "Grameno"],
    "Nena Tereze": ["Nena Tereze", "Tereze"]
}

# Create a DataFrame with the rent headlines
df = pd.read_csv("property_data.csv")

# Function to map the neighborhood for each rent headline
def get_neighborhood(rent_headline):
    for neighborhood, keywords in neighborhoods.items():
        if any(keyword.lower() in rent_headline.lower() for keyword in keywords):
            return neighborhood
    return None

# Apply the function to create a new column 'Neighborhood'
df['Neighborhood'] = df['title'].apply(get_neighborhood)

print(df["Neighborhood"].value_counts())

df.to_csv("add_neighborhood.csv")

