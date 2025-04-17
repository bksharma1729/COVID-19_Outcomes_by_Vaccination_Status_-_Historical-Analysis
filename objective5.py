# Objective 6: Temporal Trends Analysis
# The goal here is to examine how outcomes change week by week to uncover seasonal patterns, outbreak waves, or the impact of public health interventions.
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Load the dataset
df = pd.read_csv("Cleaned_Dataset.csv")

# Step 1: Ensure week_end is in datetime format
df['week_end'] = pd.to_datetime(df['week_end'])

# Step 2: Filter for one outcome type (e.g., "Cases")
cases_weekly = df[df['outcome'] == 'Cases'].groupby('week_end')[
    ['outcome_unvaccinated', 'outcome_vaccinated', 'outcome_boosted']
].sum().reset_index()

# Step 3: Plotting
plt.figure(figsize=(10, 6))
plt.plot(cases_weekly['week_end'], cases_weekly['outcome_unvaccinated'], label='Unvaccinated', color='red')
plt.plot(cases_weekly['week_end'], cases_weekly['outcome_vaccinated'], label='Vaccinated', color='blue')
plt.plot(cases_weekly['week_end'], cases_weekly['outcome_boosted'], label='Boosted', color='green')

plt.title('Weekly COVID-19 Cases by Vaccination Status', fontsize=14)
plt.xlabel('Week')
plt.ylabel('Total Weekly Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
