import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = pd.read_csv("COVID-19_Outcomes_by_Vaccination_Status_-_Historical.csv")


# Display basic information about the datasets
print("Shape of the dataset:", df.shape)
print("\nColumn names and data types:\n")
print(df.dtypes)
print("\nPreview of dataset:\n")
print(df.head())
print("\nMissing values per column:\n")
print(df.isnull().sum())
print("\nUnique values per column:\n")
print(df.nunique())

# Clean column names: strip whitespace, convert to lowercase, and replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\nColumn names after cleaning:\n")
print(df.columns.tolist())
print("\nMissing values before filling:\n")
print(df.isnull().sum())

# Handle 'week_end' column int same format
if 'week_end' in df.columns:
    df['week_end'] = pd.to_datetime(df['week_end'], errors='coerce')  # Convert to datetime
    df['week_end'] = df['week_end'].fillna(method='ffill')  # Forward fill missing dates

#Fill missing values in numeric columns with 0
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

#Drop duplicate rows
df = df.drop_duplicates()

#Clean 'vaccination_status' column if it exists
if 'vaccination_status' in df.columns:
    df['vaccination_status'] = df['vaccination_status'].str.strip().str.title()

#Sort the dataset by 'as_of_date' if the column exists
if 'as_of_date' in df.columns:
    df = df.sort_values(by='as_of_date')
#Drop the column which have large values missing
drop_column = [
'age-adjusted_unvaccinated_rate',    
'age-adjusted_vaccinated_rate',     
'age-adjusted_boosted_rate',       
'age-adjusted_vaccinated_ratio',   
'age-adjusted_boosted_ratio' 
]
df = df.drop(columns=drop_column)
#Clean 'age_group' column 
valid_age_groups = ['05-11', '18-29', '30-49', '50-64', '65-79', '80+', 'All']

df['age_group'] = df['age_group'].where(df['age_group'].isin(valid_age_groups), np.nan)

# Drop rows where age_group is NaN (i.e., invalid entries like 'Dec-17', '05-Nov')
df = df.dropna(subset=['age_group'])

#Display unique values in 'age_group' column after cleaning
print("\nUnique values in 'age_group' column after cleaning:\n")
print(df['age_group'].unique())




#Display missing values after handling
print("\nMissing values after filling:\n")
print(df.isnull().sum())

#Display the shape and preview of the cleaned dataset
print("\nShape of the dataset after cleaning:", df.shape)
print("\nPreview of cleaned dataset:\n")
print(df.head())

#Save the cleaned dataset to a new CSV file
df.to_csv("Cleaned_Dataset.csv", index=False)
print("\nCleaned dataset saved as 'Cleaned_Dataset.csv'.")
