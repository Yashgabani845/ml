import pandas as pd
from kmodes.kmodes import KModes
# Create a DataFrame with categorical data
data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female'],
    'Occupation': ['Doctor', 'Engineer', 'Artist', 'Engineer', 'Doctor', 'Artist', 'Doctor', 'Engineer'],
    'Marital_Status': ['Single', 'Married', 'Single', 'Single', 'Married', 'Married', 'Single', 'Married'],
    'Favorite_Color': ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Green', 'Red', 'Blue']
}

df = pd.DataFrame(data)
print(df)
# Initialize the KMode algorithm
km = KModes(n_clusters=2, init='Cao', n_init=5, verbose=1)

# Fit the data to the model and predict the clusters
clusters = km.fit_predict(df)

# Add cluster labels to the DataFrame
df['Cluster'] = clusters

# Output the clusters
print(df)
